"""Score eval outputs: python3 score.py [outputs dir]

A case passes when every "must" group has one of its phrases and no "banned" phrase appears.
Phrases without vowel marks are matched on the output with its marks removed. "house" cases test
the skill's own choices (كلمة السر, تحميل); "universal" cases test what any careful writer gets right.
A case is "seen" when its English, its reference, or a part of its reference (title, body or
button row longer than 12 characters) is anywhere in the skill (SKILL.md or references/), so a
model with the skill had the answer in front of it; unseen cases are the fairer test.
"""
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.environ.get("SKILL_DIR") or next(
    (d for d in (os.path.join(HERE, "..", "..", "..", "skills", "arabic-ui-copy"),  # published repo
                 os.path.join(HERE, "..", "..", "skill", "arabic-ui-copy"))        # working folder
     if os.path.isdir(d)), "")
sys.path.insert(0, os.path.join(SKILL, "scripts"))
sys.dont_write_bytecode = True
import check_copy as cc

MARKS = re.compile("[ً-ْٰ]")
plain = lambda s: MARKS.sub("", s)
cases = json.load(open(os.path.join(HERE, "cases.json"), encoding="utf-8"))
ex = "\n".join(open(f, encoding="utf-8").read() for f in
               [os.path.join(SKILL, "SKILL.md")] + glob.glob(os.path.join(SKILL, "references", "**", "*.md"), recursive=True))
ex_en = {cell.strip().lower() for l in ex.splitlines() if l.startswith("|") for cell in l.split("|")}
parts = lambda ref: [p for p in ref.split(" · ") if len(p) > 12]
seen = {c["id"] for c in cases if c["source"].lower() in ex_en or c["reference"] in ex
        or any(p in ex or p.rstrip(".") in ex for p in parts(c["reference"]))}
terms, allowed = cc.load_glossary()


def has(out, phrase):
    return phrase in out or (not MARKS.search(phrase) and plain(phrase) in plain(out))


def score(out_by_id):
    res = {}
    for c in cases:
        o = out_by_id.get(c["id"], "")
        ok = bool(o) and all(any(has(o, p) for p in g) for g in c["must"]) and not any(has(o, b) for b in c["banned"])
        res[c["id"]] = ok
    return res


outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "outputs")
rows = []
for path in sorted(glob.glob(os.path.join(outdir, "*.json"))):
    name = os.path.basename(path)[:-5]
    outs = json.load(open(path, encoding="utf-8"))
    r = score(outs)
    def pct(ids):
        ids = list(ids); return f"{sum(r[i] for i in ids)}/{len(ids)}"
    text = "\n".join(str(v) for v in outs.values())
    house = len(cc.check_text("x.txt", text, terms, allowed))
    univ = len(cc.check_text("x.txt", text, [], [], universal=True))
    k = {c["id"]: c["kind"] for c in cases}
    rows.append((name, pct(r), pct(i for i in r if k[i] == "universal"), pct(i for i in r if k[i] == "house"),
                 pct(i for i in r if i not in seen), univ, house, [i for i in r if not r[i]]))
print(f"seen in the skill ({len(seen)}): {sorted(seen)}")
print("| Run | All | Universal | House | Unseen | Checker, universal rules | Checker, all rules | Failed |")
print("| --- | --- | --- | --- | --- | --- | --- | --- |")
for row in rows:
    print("| " + " | ".join(str(x) if not isinstance(x, list) else ", ".join(x) for x in row) + " |")
