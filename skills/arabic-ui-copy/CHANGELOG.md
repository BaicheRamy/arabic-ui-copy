# Changelog

Versions follow semantic versioning: a major version changes a house rule, a minor version adds rules or coverage, a patch fixes wording or the checker.

## 1.0.0 (2026-10-29)

First public release.

- House style from a 59-question review of about 430 live strings; every pick and later change is in the decision log (evidence/arabic-ui-copy/decisions.md in the repository).
- References: glossary, examples, feedback and messages, sensitive states (payments, deleting, permissions, untrusted text, locale files), flows (undo toast, onboarding, paywalls, subscriptions, screen-reader labels).
- Regional profiles for the checker: gulf, egypt, maghreb (`--profile`).
- Checker rules added in this release: تم/يتم + verbal noun, قم بـ, Latin glued to Arabic, Hebrew or CJK characters, placeholders written in Arabic, curly-quote punctuation; digits before month names, currencies and ranges are no longer flagged.
- House changes after outside review: جارٍ for progress, shadda on verbs and participles only, delete dialogs end in إلغاء and say whether the action can be undone, the assistant's first message says it is automated, a full-stop rule.

## Before 1.0.0

- 0.3 (2026-10-29): feedback, support and message channels, from a CX book review.
- 0.2 (2026-10-29): plural rules, "translate, don't add", benchmark against no skill and JKc66/arabic-ui.
- 0.1 (2026-10-29): first draft from the interview.
