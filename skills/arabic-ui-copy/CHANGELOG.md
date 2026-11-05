# Changelog

Versions follow semantic versioning: a major version changes a house rule, a minor version adds rules or coverage, a patch fixes wording or the checker.

## 1.3.0 (2026-11-05)

- A project's own glossary or style sheet wins over this one. The agent keeps its terms and says where they differ; the checker skips them with `--keep "كلمة المرور,تنزيل"`.
- Failures: حدث خطأ أثناء when something broke on our side; تعذّر + verbal noun, then what to check, when the cause may be the user's file, link or access, or nothing was found.
- A verb that replaces تم + verbal noun must name what it is about and read one way without vowel marks (بلغت الباقة حدها, not بلغت الحد). If no verb does both, تم stays.
- One meaning, one term: when the English uses one word for two things, each gets its own Arabic term in every string.
- Nothing the source says is dropped. A search placeholder is ابحث alone only when the source is just "Search"; otherwise it keeps what it searches.
- Fix a flagged term only after reading the English: إعادة تعيين for Reassign becomes إعادة إسناد, not إعادة ضبط. Glossary: Assign, reassign is إسناد · إعادة إسناد.
- منذ stays for how long something has lasted (بانتظار منذ 5 دقائق); the checker no longer flags it after انتظار.
- Examples: dialog buttons are نعم، احذف / إلغاء everywhere (one row still said لا); new rows for a failure caused by the file, a full storage limit and a search field that names what it searches.

## 1.2.0 (2026-11-01)

- Text that speaks to all users at once (release notes, announcements, thanks to everyone) addresses them in the plural throughout: شكرًا على ملاحظاتكم.
- A product or plan whose name is an Arabic word, or has an official Arabic name, is written in Arabic (رفيد, not Rafeed). Other brand names stay in Latin script.

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
