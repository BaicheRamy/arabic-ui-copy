"""Checker tests, no dependencies: python3 run_tests.py

1. cases.tsv: expected message fragment (or "none"), file extension, text.
2. profile-cases.tsv: the same, with a regional profile first ("house" for none).
3. Every correct string in references/examples.md ("Write" column) must pass with no findings.
"""
import os, sys
sys.dont_write_bytecode = True  # keep __pycache__ out of the skill folder
HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.environ.get("SKILL_DIR", os.path.join(HERE, "..", "skill", "arabic-ui-copy"))
sys.path.insert(0, os.path.join(SKILL, "scripts"))
import check_copy as cc

fails = 0


def run(profile, expect, ext, text):
    global fails
    terms, allowed = cc.load_glossary(profile)
    off = cc.load_profile(profile)[1] if profile else []
    msgs = [m for _, _, m in cc.check_text("case" + ext, text, terms, allowed, rules_off=off)]
    ok = not msgs if expect == "none" else any(expect in m for m in msgs)
    if not ok:
        fails += 1
        print(f"FAIL  [{profile or 'house'}] {text}\n      expected: {expect}\n      got: {msgs or 'nothing'}")


def rows(name):
    for raw in open(os.path.join(HERE, name), encoding="utf-8"):
        if raw.strip() and not raw.startswith("#"):
            yield raw.rstrip("\n").split("\t")


n = 0
for expect, ext, text in rows("cases.tsv"):
    run(None, expect, ext, text); n += 1
for profile, expect, ext, text in rows("profile-cases.tsv"):
    run(None if profile == "house" else profile, expect, ext, text); n += 1
for line in open(os.path.join(SKILL, "references", "examples.md"), encoding="utf-8"):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if line.startswith("|") and len(cells) >= 4 and cells[0] != "English" and not set(cells[0]) <= {"-"}:
        run(None, "none", ".txt", cells[2]); n += 1
print(f"{n} checks, {fails} failure(s)")
sys.exit(1 if fails else 0)
