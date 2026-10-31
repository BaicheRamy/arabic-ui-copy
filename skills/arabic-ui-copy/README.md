# arabic-ui-copy

An Agent Skill that makes coding agents write Arabic interface text the way a native product designer would: buttons, forms, errors, empty states, dialogs, status labels, settings, payments, permission prompts, rating prompts, support replies and notifications.

AI agents write Arabic UI text that reads as translated English: احفظ instead of حفظ, "كلمة المرور الخاصة بك", تم حفظ, English question marks, Arabic-Indic digits in one place and Western in the next. This skill gives the agent one consistent house style, a glossary of about 60 terms, before-and-after examples, and a checker script with tests.

The rules come from comparing about 470 live strings from Apple, Google, Microsoft, Gulf government services, Arab commerce apps and Thmanyah, then settling where they disagree into one house style, set by a native Arabic product designer. 438 of those strings, with source and date, are published in the repository under `evidence/arabic-ui-copy/`.

Version 1.0.0. See [CHANGELOG.md](CHANGELOG.md).

## Install

```bash
npx skills add BaicheRamy/arabic-ui-copy
```

Or copy the `arabic-ui-copy` folder into `.claude/skills/` (Claude Code) or your agent's skills folder.

## What's inside

| File | What it does |
| --- | --- |
| `SKILL.md` | Voice, patterns per string type, punctuation, numbers, checklist |
| `references/glossary.md` | One term per concept, with the terms to avoid |
| `references/examples.md` | What agents write, what to write, and why |
| `references/feedback-and-messages.md` | Rating and survey prompts, support replies, milestones, SMS, push and email |
| `references/sensitive-states.md` | Payments, deleting, permission prompts, pasted text, locale files |
| `references/flows.md` | Undo toasts, onboarding, paywalls and subscriptions, screen-reader labels |
| `references/profiles/` | Regional profiles for the checker: gulf, egypt, maghreb |
| `scripts/check_copy.py` | Flags glossary misses, translationese (تم + verbal noun, قم بـ), Latin punctuation, hamza slips, plural and digit errors, translated placeholders and SMS over 70 characters |

The agent reads SKILL.md every time and a reference file only when the string needs it.

```bash
python3 scripts/check_copy.py src/locales/ar.json
python3 scripts/check_copy.py --profile gulf src/locales/ar.json   # accepts كلمة المرور and رقم الجوال
python3 scripts/check_copy.py --universal src/locales/ar.json      # only rules that hold in any style
python3 scripts/check_copy.py --sms templates/sms/
```

## Scope

Modern Standard Arabic for product UI and the messages it sends, with light dialect allowed in marketing and onboarding. Western digits, with number and date formats as Gulf and Egyptian readers expect them; the maghreb profile switches to a decimal comma. This is one house style, not the only correct Arabic: كلمة السر and تحميل are deliberate choices. Use a profile (the gulf profile accepts كلمة المرور), or fork the glossary to change a term, and the checker follows it.

## Author

Ramy ([@BaicheRamy](https://github.com/BaicheRamy)), product designer. MIT licence, see [LICENSE](LICENSE).
