# Changelog

Versions follow semantic versioning: a major version changes a house rule, a minor version adds rules or coverage, a patch fixes wording or the checker.

## 1.1.0 (2026-10-31)

- Quotation marks are now « » (were “ ”). Real Arabic products and the UAE Design System use « »; the checker now flags “ ” instead.
- New checker rules: a number ending in 11 to 99 before a noun with no tanween (11 متابع → 11 متابعًا), tatweel in UI text (تابــع), and a space before ؟ ، ؛.
- SKILL.md: live counts use the plural forms or a label (المتابعون: 11); no tatweel; no space before Arabic punctuation.
- Glossary: Follow (button) is متابعة.
- Examples: an Arabic-script name field, a live follower count, an FAQ question in the user's voice.
- Evidence: 36 strings from Thmanyah added to strings.csv (438 in total).

## 1.0.0 (2026-10-29)

First public release.

- House style built from about 430 live strings; 402 of them, with source and date, are in evidence/arabic-ui-copy/strings.csv in the repository.
- References: glossary, examples, feedback and messages, sensitive states (payments, deleting, permissions, untrusted text, locale files), flows (undo toast, onboarding, paywalls, subscriptions, screen-reader labels).
- Regional profiles for the checker: gulf, egypt, maghreb (`--profile`).
- Checker rules added in this release: تم/يتم + verbal noun, قم بـ, Latin glued to Arabic, Hebrew or CJK characters, placeholders written in Arabic, curly-quote punctuation; digits before month names, currencies and ranges are no longer flagged.
- House rules settled before release: جارٍ for progress, shadda on verbs and participles only, delete dialogs end in إلغاء and say whether the action can be undone, the assistant's first message says it is automated, a full-stop rule.

## Before 1.0.0

- 0.1 to 0.3 (2026-10-29): pre-release drafts.
