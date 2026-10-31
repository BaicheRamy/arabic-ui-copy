#!/usr/bin/env python3
"""Flag Arabic UI copy that breaks the arabic-ui-copy house rules.

Usage: python3 check_copy.py [--universal] [--sms] [--profile NAME] <file or folder> [...]
  --universal  only rules that hold for any Arabic UI style (no glossary, no house choices)
  --profile    a regional profile from ../references/profiles/ (gulf, egypt, maghreb): its rows
               replace the glossary rows with the same concept, and its "Rules off" are skipped
  --sms        also flag every Arabic string over 70 characters (one Arabic SMS). Pass only
               SMS template files: in any other file every long line is reported. Without it,
               only JSON keys containing "sms" are length-checked
Scans text files (json, js, ts, tsx, jsx, html, md, po, yaml, strings, arb, xml, csv, txt).
Avoided terms come from ../references/glossary.md, so the glossary stays the single source.
Exit code 1 when anything is reported. Every finding is a suggestion: read it in context.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GLOSSARY = os.path.join(HERE, "..", "references", "glossary.md")
PROFILES = os.path.join(HERE, "..", "references", "profiles")
EXTS = {".json", ".js", ".ts", ".tsx", ".jsx", ".html", ".htm", ".md", ".mdx", ".po",
        ".yaml", ".yml", ".strings", ".arb", ".xml", ".csv", ".txt", ".vue", ".svelte"}
# Files where a straight quote is prose, not a string delimiter.
TEXT_EXTS = {".md", ".mdx", ".txt", ".html", ".htm"}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next"}

AR = "؀-ۿ"
LETTER = "ء-ي"
# Vowel marks, shadda, sukun, dagger alif and tatweel: stripped before words are matched,
# so تنزيلًا, التنزيل and التنزيل all count as تنزيل.
MARKS = re.compile("[ً-ْٰـ]")
# Clitics a word can carry: conjunction, preposition and article before it; pronoun,
# feminine and plural endings after it. A term that already starts with ال only takes و or ف,
# so بالضبط ("exactly") is never read as the avoided الضبط.
PREFIX = "(?:وال|فال|بال|كال|لل|ال|و|ف|ب|ل|ك)?"
PREFIX_AL = "(?:و|ف)?"
SUFFIX = "(?:هما|ها|هم|هن|كما|كم|كن|نا|وا|ك|ه|ي|ة|ات|ان|ين|ون|ا)?"


def strip_marks(s):
    return MARKS.sub("", s)


def word_re(term):
    """Whole word on mark-stripped text, clitics allowed around it."""
    prefix = PREFIX_AL if term.startswith("ال") else PREFIX
    return re.compile("(?<![" + LETTER + "])" + prefix + re.escape(term) + SUFFIX + "(?![" + LETTER + "])")


def table_rows(path):
    """Concept -> (use, avoid) for every row of the markdown tables in a file."""
    rows = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not line.startswith("|") or len(cells) < 3 or cells[0] in ("Concept", "---") or set(cells[0]) <= {"-"}:
                continue
            rows[cells[0]] = (cells[1], cells[2])
    return rows


def load_profile(name):
    """Return (rows, rules off) for a regional profile; rows replace glossary rows with the same concept."""
    path = os.path.join(PROFILES, name + ".md")
    if not os.path.exists(path):
        names = sorted(f[:-3] for f in os.listdir(PROFILES) if f.endswith(".md"))
        sys.exit(f"Unknown profile {name!r}. Profiles: {', '.join(names)}")
    off, in_off = [], False
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            in_off = line.strip().lower() == "## rules off"
        elif in_off and line.startswith("- "):
            off.append(line[2:].strip())
    return table_rows(path), off


def load_glossary(profile=None):
    """Return (avoided term, what to use) pairs, and the Use phrases that contain an avoided term."""
    uses_for, use_phrases = {}, set()
    rows = table_rows(GLOSSARY)
    if profile:
        rows.update(load_profile(profile)[0])
    for use, avoid in rows.values():
        use_phrases.update(re.findall("[" + LETTER + "]+(?: [" + LETTER + "]+)*", strip_marks(use)))
        for bad in (strip_marks(t.strip()) for t in avoid.split(" / ")):
            if bad and bad != "—" and use not in uses_for.setdefault(bad, []):
                uses_for[bad].append(use)
    terms = [(bad, " or ".join(uses)) for bad, uses in uses_for.items()]
    # A chosen phrase such as اضغط مع الاستمرار must not be flagged for the avoided اضغط inside it.
    allowed = [p for p in use_phrases if any(bad != p and word_re(bad).search(p) for bad in uses_for)]
    return terms, allowed


# Words that start with a connecting alif (hamzat wasl) and must not carry a hamza.
HAMZA_SLIPS = ["إتصل", "إتصال", "إكتشف", "إنضم", "إختر", "إختيار", "إبحث", "إستمرار",
               "إستخدام", "إستعادة", "إسترداد", "إسم", "إضغط", "إنتظار", "إرتفاع", "إنتهى", "إنتهت"]
# Common letter swaps: (typo, fix).
TYPOS = [("انظم", "انضم")]

# Rules that are errors in any Arabic UI style; the rest are this skill's house choices.
UNIVERSAL = {"Latin question mark after Arabic: use ؟", "Latin comma between Arabic words: use ،",
             "Latin semicolon between Arabic words: use ؛", "Calqued possessive: drop الخاص بك / الخاصة بك",
             "Bracketed plural ending: use the six plural forms",
             "Digit 1 or 2 before a noun: write the singular + واحد, or the dual, with no digit",
             "Numbers 3-10 take the plural: 5 ملفات, not 5 ملفًا",
             "Numbers 11-99 take the singular: 15 ملفًا, not 15 ملفات",
             "منذ and مضت together: keep one", "More than one exclamation mark",
             "People after 3-10 take the genitive plural: 3 مستخدمين, not 3 مستخدمون",
             "A non-human plural takes a feminine singular adjective: إشعارات غير مقروءة",
             "Placeholder written in Arabic: keep it exactly as in the source ({name})",
             "Hebrew or CJK characters in Arabic text",
             "Latin letters glued to Arabic: add a space (باستخدام Apple Pay)",
             "Numbers 11-99 take a singular with tanween: 11 متابعًا, not 11 متابع", "Space before ؟ ، ؛: remove it"}

# Nouns after which a digit is a label (الخطوة 1, الإصدار 2), not a count.
LABEL_NOUNS = ["رقم", "الخطوة", "الصفحة", "الإصدار", "المستوى", "المرحلة", "الجزء", "الفصل", "الدرس", "البند"]
NOT_LABEL = "".join("(?<!" + w + " )" for w in LABEL_NOUNS)
# Month names of every Arabic market: Gulf and Egypt, Algeria and Tunisia, Morocco, the Levant and Iraq.
MONTHS = ("(?:يناير|فبراير|مارس|أبريل|مايو|يونيو|يوليو|أغسطس|سبتمبر|أكتوبر|نوفمبر|ديسمبر"
          "|جانفي|فيفري|أفريل|ماي|جوان|جويلية|أوت|يوليوز|غشت|شتنبر|نونبر|دجنبر"
          "|كانون الثاني|شباط|آذار|نيسان|أيار|حزيران|تموز|آب|أيلول|تشرين الأول|تشرين الثاني|كانون الأول)")
CURRENCIES = ("(?:ر\\.س|ريال|ريالات|د\\.إ|درهم|دراهم|ج\\.م|جنيه|جنيهات|د\\.ج|دج|دينار|دنانير|د\\.ك|د\\.ب|ر\\.ق|ر\\.ع"
              "|د\\.أ|د\\.ت|د\\.م|ل\\.ل|ليرة|دولار|يورو)")
TIME_UNITS = ("(?:ثوان|ثانية|ثانيتين|دقيقة|دقيقتين|دقائق|ساعة|ساعتين|ساعات|يوما?|يومين|أيام"
              "|أسبوعا?|أسبوعين|أسابيع|شهرا?|شهرين|أشهر|سنة|سنتين|سنوات|عاما?|عامين|أعوام)")

# A quote mark or bracket can sit between an Arabic word and a Latin mark: «الاسم», «العمر».
# Straight quotes are left out, because in code "الاسم", "العمر" is syntax, not copy.
CLOSE = "[”»)]?"
OPEN = "[“«(]?"

# (message, pattern, matched on mark-stripped text?)
RULES = [
    ("Latin question mark after Arabic: use ؟", re.compile(r"[" + AR + r"]" + CLOSE + r"\s*\?"), False),
    ("Latin comma between Arabic words: use ،", re.compile(r"[" + AR + r"]" + CLOSE + r"\s*,\s*" + OPEN + r"[" + AR + r"]"), False),
    ("Latin semicolon between Arabic words: use ؛", re.compile(r"[" + AR + r"]" + CLOSE + r"\s*;\s*" + OPEN + r"[" + AR + r"]"), False),
    ("Curly quotes “ ”: house quotes are « »", re.compile(r"[“”]"), False),
    ("Straight quotes around Arabic: use « »", re.compile(r'[ء-ي]\\?"[ء-ي]|\\"[ء-ي]|[ء-ي]\\"'), False),
    ("Arabic-Indic digits: use Western 0-9", re.compile(r"[٠-٩۰-۹]"), False),
    ("Three dots: use the single character …", re.compile(r"[" + AR + r"]" + CLOSE + r"\s*\.\.\."), False),
    ("Calqued possessive: drop الخاص بك / الخاصة بك", re.compile(r"(?<![ء-ي])(?:ال)?خاص(?:ة)? بك(?:م|ما|ن)?(?![ء-ي])"), True),
    ("Decimal comma: use a decimal point (1,234.5)", re.compile(r"(?<![\d,])\d+,\d{1,2}(?![\d,])"), False),
    ("Bracketed plural ending: use the six plural forms", re.compile(r"[ء-ي]\((?:ات|ون|ين|ان)\)|[ء-ي]/(?:ات|ون|ين)(?![ء-ي])"), False),
    ("Digit 1 or 2 before a noun: write the singular + واحد, or the dual, with no digit",
     re.compile(r"(?<![\d.,/:\-–ء-ي])(?<!إلى )(?<!حتى )" + NOT_LABEL + r"[12]\s+(?!من\s|إلى\s|حتى\s|[-–]\s*\d|"
                + MONTHS + r"(?![ء-ي])|" + CURRENCIES + r"(?![ء-ي]))[ء-ي]"), True),
    ("Numbers 3-10 take the plural: 5 ملفات, not 5 ملفًا", re.compile(r"(?<![\d.,/:])" + NOT_LABEL + r"(?:[3-9]|10)\s+[ء-ي]+(?:ًا|اً)(?![ء-ي])"), False),
    ("Numbers 11-99 take the singular: 15 ملفًا, not 15 ملفات", re.compile(r"(?<![\d.,/:])" + NOT_LABEL + r"(?:1[1-9]|[2-9]\d)\s+(?!من\s|إلى\s)[ء-ي]{2,}ات(?![ء-ي])"), True),
    ("People after 3-10 take the genitive plural: 3 مستخدمين, not 3 مستخدمون", re.compile(r"(?<![\d.,/:])(?:[3-9]|10)\s+(?!مليون)م[ء-ي]{2,}ون(?![ء-ي])"), True),
    ("A non-human plural takes a feminine singular adjective: إشعارات غير مقروءة", re.compile(r"[ء-ي]{2,}ات\s+غير\s+[ء-ي]+ين(?![ء-ي])"), True),
    ("Dates: day, month name, year (5 مارس 2026)", re.compile(MONTHS + r"\s+\d{1,2}\s*[,،]?\s*\d{4}"), True),
    ("State label: use مفعّل / غير مفعّل; تفعيل and إيقاف are actions", re.compile(r":\s*(?:إيقاف|تفعيل|تشغيل)(?![ء-ي])"), True),
    ("Exclamation mark next to an error word", re.compile(r"(?:خطأ|تعذّر|تعذر|فشل)[^\n!]{0,40}!"), False),
    ("جاري: write جارٍ (جارٍ الحفظ…)", re.compile(r"(?<![ء-ي])جاري(?=\s+[ء-ي])"), False),
    ("Calqued English phrasing: ask with ما مدى; reply is سنرد عليك", re.compile(r"كم (?:من المحتمل|كان من السهل|من السهل)|سنعود إليك|سنعود اليك"), True),
    ("Gendered greeting before a name variable: use مرحبًا {name}،", re.compile(r"عزيز(?:ي|تي)\s*(?:\{|%|\$)"), True),
    ("More than one exclamation mark", re.compile(r"!{2,}|!\s*!"), False),
    ("Apology on a user-input error: drop عذرًا", re.compile(r"عذر[ًا]{1,2}\s*[،,]?\s*(?:هذا الحقل|أدخل|يُرجى إدخال|يرجى إدخال|[^.\n]{0,30}غير (?:صالح|صحيح))"), False),
    ("منذ and مضت together: keep one", re.compile(r"منذ [^.\n،]{0,25}مضت"), True),
    ("تم/يتم + verbal noun: use a passive or plain verb (حُفظت التغييرات, not تم حفظ التغييرات)",
     re.compile(r"(?<![ء-ي])(?:و|ف)?(?:تم|تمت|يتم|تتم|سيتم|ستتم)\s+[ء-ي]"), True),
    ("قم بـ + verbal noun: use the verb itself (أدخل, not قم بإدخال)",
     re.compile(r"(?<![ء-ي])(?:و|ف)?(?:قم|قومي|قوموا)\s+ب|(?:يرجى|الرجاء)\s+القيام\s+ب"), True),
    ("Placeholder written in Arabic: keep it exactly as in the source ({name})",
     re.compile(r"(?<!zero )(?<!one )(?<!two )(?<!few )(?<!many )(?<!other )(?<!zero)(?<!one)(?<!two)(?<!few)(?<!many)(?<!other)"
                r"(?<!=\d )(?<!=\d)\{\{?[ء-ي_]+\}\}?|%\d\$[ء-ي]"), False),
    ("Hebrew or CJK characters in Arabic text", re.compile(r"[\u0590-\u05FF\u3040-\u30FF\u3400-\u9FFF\uAC00-\uD7AF]"), False),
    ("Relative time: house form is قبل (قبل 5 دقائق)", re.compile(r"(?<![ء-ي])منذ (?:\d+\s+)?" + TIME_UNITS + r"(?![ء-ي])"), True),
]
class Glued:
    """Latin letters touching Arabic letters with no space (ادفع باستخدامApple Pay). A one-letter و, ب or ل
    before a brand name is fine (وApple Pay, بـApple Pay); printf placeholders and escapes like \\n are skipped."""
    rx = re.compile(r"[ء-يـ][A-Za-z]|[A-Za-z][ء-ي]")
    skip = re.compile(r"(?<![ء-ي])[وبل]ـ?(?=[A-Za-z])|%\d*\$?[sd@]|\\[ntr]|&[a-z]+;|</?[a-z]+")

    def search(self, s):
        return self.rx.search(self.skip.sub(" ", s))


RULES.append(("Latin letters glued to Arabic: add a space (باستخدام Apple Pay)", Glued(), False))


class Tatweel:
    """The stretching character ـ inside words (تابــع). A one-letter prefix before a quote, a Latin word or a
    digit (لـ«ساعة», بـApple Pay) and the Hijri date suffix هـ are fine."""
    skip = re.compile(r"(?<![ء-ي])[بلكوف]ـ(?![ء-ي])|(?<![ء-ي])هـ(?![ء-ي])")

    def search(self, s):
        return "ـ" in self.skip.sub(" ", s)


class ManyBare:
    """A number ending in 11-99 (11, 25, 199) before a masculine noun with no tanween: 11 متابع -> 11 متابعًا.
    Feminine nouns in ة take nothing (15 رسالة). Years, times, labels (رقم 15) and abbreviations are skipped."""
    rx = re.compile(r"(?<![\d.,/:])" + NOT_LABEL + r"(\d{1,3}(?:,\d{3})*|\d+)\s+([ء-ي]+)([ًٌٍَُِّْ]*)(?![:\d])")
    skip_words = {"من", "إلى", "الى", "في", "على", "أو", "او", "و", "ثم", "حتى", "عن", "مع", "كم", "سم", "مم", "كغ", "غ", "مل", "ألف", "مليون", "مليار",
                  # units written as loanwords, which products never inflect
                  "بايت", "كيلوبايت", "ميجابايت", "ميغابايت", "جيجابايت", "غيغابايت", "تيرابايت", "بكسل", "كيلو", "كيلومتر", "متر", "سنتيمتر", "ملليمتر", "كيلوغرام", "كيلوجرام", "جرام", "غرام", "لتر", "واط", "فولت"}

    def search(self, s):
        for m in self.rx.finditer(s):
            num, word, marks = m.group(1).replace(",", ""), m.group(2), m.group(3)
            n = int(num)
            if len(num) == 4 and num[:2] in ("19", "20", "14"):
                continue  # a year, Gregorian or Hijri
            if not 11 <= n % 100 <= 99 or len(word) < 3 or word.startswith("ال") or word in self.skip_words:
                continue
            if "ً" in marks or word.endswith(("ة", "ات", "ى", "ي", "و", "ا")) or re.match(MONTHS + "$", word) or re.match(CURRENCIES + "$", word):
                continue
            return True
        return False


RULES.append(("Tatweel ـ in UI text: remove it; it breaks search and copy-paste", Tatweel(), False))
RULES.append(("Numbers 11-99 take a singular with tanween: 11 متابعًا, not 11 متابع", ManyBare(), False))
RULES.append(("Space before ؟ ، ؛: remove it", re.compile(r"[ء-ي»)\d][ \t]+[؟،؛]"), False))

# Only in prose files, where a straight quote before an Arabic word is never a delimiter.
TEXT_RULES = [("Straight quotes around Arabic: use « »", re.compile(r'(?:^|[\s(|])"[ء-ي]'), False)]

SMS_LIMIT = 70
KEY_VALUE = re.compile(r'"([^"]*)"\s*:\s*"((?:[^"\\]|\\.)*)"')
QUOTED = re.compile(r'"((?:[^"\\]|\\.)*)"')


def sms_strings(line, all_strings):
    """Arabic strings on a line that are SMS text: every one with --sms, else values of keys containing "sms"."""
    pairs = KEY_VALUE.findall(line)
    if all_strings:
        vals = [v for _, v in pairs] or QUOTED.findall(line) or [line.strip()]
    else:
        vals = [v for k, v in pairs if "sms" in k.lower()]
    return [v for v in vals if re.search("[" + AR + "]", v)]


def word_hits(plain, entries):
    """Messages for word entries (longest term first); a match inside an earlier match is skipped."""
    spans, msgs = [], []
    for rx, msg in entries:
        for m in rx.finditer(plain):
            if any(a <= m.start() and m.end() <= b for a, b in spans):
                continue
            spans.append(m.span())
            msgs.append(msg)
    return msgs


def check_text(path, text, terms, allowed=(), universal=False, sms=False, rules_off=()):
    found = []
    rules = RULES + (TEXT_RULES if os.path.splitext(path)[1].lower() in TEXT_EXTS else [])
    if universal:
        rules = [r for r in rules if r[0] in UNIVERSAL]
    rules = [r for r in rules if not any(r[0].startswith(off) for off in rules_off)]
    words = [(bad, f"Glossary: use {use} instead of {bad}") for bad, use in terms]
    words += [(w, f"Hamza on a connecting alif: {w} -> {w.replace('إ', 'ا', 1)}") for w in HAMZA_SLIPS]
    words += [(w, f"Likely typo: {w} -> {fix}") for w, fix in TYPOS]
    words = [(word_re(w), msg) for w, msg in sorted(words, key=lambda e: -len(e[0]))]
    allowed_res = [word_re(p) for p in sorted(allowed, key=len, reverse=True)]
    for n, line in enumerate(text.splitlines(), 1):
        if not re.search("[" + AR + "]", line):
            continue
        plain = strip_marks(line)
        masked = plain
        for rx in allowed_res:
            masked = rx.sub(lambda m: " " * len(m.group()), masked)
        msgs = word_hits(masked, words)
        msgs += [msg for msg, rx, on_plain in rules if rx.search(plain if on_plain else line)]
        msgs += [f"SMS over {SMS_LIMIT} characters ({len(v)}): Arabic SMS splits into 67-character parts"
                 for v in sms_strings(line, sms) if len(v) > SMS_LIMIT]
        found += [(n, m) for m in dict.fromkeys(msgs)]
    return [(path, n, m) for n, m in found]


def files(args):
    for a in args:
        if os.path.isdir(a):
            for root, dirs, names in os.walk(a):
                dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
                for name in names:
                    if os.path.splitext(name)[1].lower() in EXTS:
                        yield os.path.join(root, name)
        else:
            yield a


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 2
    universal = "--universal" in argv
    sms = "--sms" in argv
    profile = None
    for i, a in enumerate(argv):
        if a.startswith("--profile"):
            profile = a.split("=", 1)[1] if "=" in a else (argv[i + 1] if i + 1 < len(argv) else "")
            argv = argv[:i] + argv[i + (1 if "=" in a else 2):]
            break
    argv = [a for a in argv if a not in ("--universal", "--sms")]
    rules_off = load_profile(profile)[1] if profile else []
    terms, allowed = ([], []) if universal else load_glossary(profile)
    results = []
    for path in files(argv):
        try:
            with open(path, encoding="utf-8") as f:
                results += check_text(path, f.read(), terms, allowed, universal, sms, rules_off)
        except (UnicodeDecodeError, OSError) as e:
            print(f"{path}: skipped ({e.__class__.__name__})", file=sys.stderr)
    for path, n, msg in results:
        print(f"{path}:{n}: {msg}")
    print(f"{len(results)} finding(s)")
    return 1 if results else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
