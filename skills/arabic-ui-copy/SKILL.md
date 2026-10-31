---
name: arabic-ui-copy
description: Write, translate or review Arabic interface text (buttons, form labels, errors, empty states, dialogs, toasts, status labels, navigation, rating and feedback prompts, support replies, and push, SMS and email notifications) so it reads as native product Arabic, not translated English. Use whenever a UI string is in Arabic or must be, for any product with lang="ar", dir="rtl", Arabic locale files, or an Arabic version of an English app.
license: MIT
metadata:
  version: "1.1.0"
  author: BaicheRamy
---

# Arabic UI copy

House rules for Arabic interface text, set by a native Arabic product designer after comparing about 470 live strings from Apple, Google, Microsoft, Gulf government services, Arab commerce apps and Thmanyah. Where products disagree, these rules pick one answer. Follow them exactly; do not fall back to "what most apps do".

## How to work

1. Decide what the string is: button, link, label, placeholder, helper text, error, success, progress, empty state, dialog, status, navigation, rating prompt, support reply, notification, or marketing.
2. Write it from the pattern for that type below. Do not translate the English word by word.
3. Look up every product term in [references/glossary.md](references/glossary.md) and use the chosen term only.
4. For a full screen or many strings, read [references/examples.md](references/examples.md) first: it shows the mistakes agents make most and the fixes. For rating or survey prompts, support or assistant replies, milestones, or SMS, push and email text, also read [references/feedback-and-messages.md](references/feedback-and-messages.md). For payments, deleting, permission prompts, locale files or pasted text, read [references/sensitive-states.md](references/sensitive-states.md); for undo toasts, onboarding, paywalls, subscriptions and screen-reader labels, read [references/flows.md](references/flows.md).
5. If you are editing files, run `python3 scripts/check_copy.py <files or folders>` and fix what it reports.
6. Before answering, go through the checklist at the end.

## Voice

- **Register.** Modern Standard Arabic in the product. Light dialect is allowed only in marketing pages and onboarding, never in buttons, errors, forms or settings.
- **No English loanwords.** Use the Arabic term (البريد الإلكتروني, not الإيميل; الرئيسية, not داشبورد). Brand and product names stay in Latin script: Apple Pay, Visa, iPhone.
- **Address one person.** أهلاً بك, not أهلاً بكم.
- **Gender.** Prefer forms that address nobody in particular when they cost no extra length: a passive verb with a verbal noun (يُرجى إدخال الاسم) or a passive verb alone (أُرسل رمز التحقق). Short direct commands in the masculine singular are acceptable where a neutral form would be much longer (أدخل, جرّب, ابحث).
- **Translate, don't add.** Do not add reasons, instructions, examples, roles or "now" that the source does not have, unless a pattern below requires it. Arabic UI text should stay about as long as the source; when in doubt, cut. Patterns and examples give the form, never the content: when you translate, keep what the source says (a source that says "Thanks for reaching out" gets thanks, not استلمنا طلبك).
- **Drop English possessives.** Write كلمة السر, not كلمة السر الخاصة بك; السلة, not سلتك الخاصة.
- **Exclamation marks**: at most one, and only in welcomes, milestone success and thanks (أهلاً بك! · تهانينا على أول عملية بيع! · شكرًا على رأيك!). Never in routine success (حُفظت التغييرات), errors, warnings or dialogs.
- **Apologise only for our own faults, and at most once.** The generic error is the house apology (عذرًا، حدث خطأ. يُرجى إعادة المحاولة.). A named failure (حدث خطأ أثناء…) and anything about the user's input carry no apology (هذا الحقل مطلوب, not عذرًا، هذا الحقل مطلوب). نعتذر is for support replies and incident notices where the user lost time or money, and the fix or next step follows in the same message.
- **Don't repeat a button in the message.** Next to a Retry button, an error stops at what happened: حدث خطأ أثناء تحميل التعليقات + أعد المحاولة. Without a button, the message says what to do.
- **Please depends on the surface.** Instructions in helper text and errors: يُرجى + verbal noun (يُرجى إدخال رمز التحقق), formal and gender-neutral. Helper text that only informs is a plain statement (سنرسل لك رمز التحقق برسالة نصية). Conversational surfaces (onboarding, support chat, assistant replies, survey invitations, invitations in empty states): من فضلك or الرجاء is fine. Short field commands and buttons: no please at all (أدخل، ابحث).

## Patterns by string type

| Type | Pattern | Example |
| --- | --- | --- |
| Button (default) | Verbal noun | حفظ · إضافة · حذف · استمرار · إتمام الطلب · عرض الكل |
| Button inviting or recovering | Imperative, only for these cases: sign in, sign up, retry, confirming a destructive action | سجّل دخولك · سجّل الآن · أعد المحاولة · نعم، احذف |
| "Now" | Only in marketing call-to-action buttons and in the sign-up invitation سجّل الآن; never in other product buttons | اشترِ الآن · سجّل الآن |
| Instruction (helper text that asks the user to act) | يُرجى + verbal noun (see "Please" above) | يُرجى اختيار طريقة الدفع |
| Informational helper text | A plain statement, in the we-form when the product acts | سنرسل لك رمز التحقق برسالة نصية |
| Success | Passive past verb, mark the passive with a damma. When a process finishes, اكتمل + verbal noun reads better | حُفظت التغييرات · حُذف المشروع · أُرسل رمز التحقق · اكتمل الدفع · اكتمل الرفع |
| Action failed | حدث خطأ أثناء + verbal noun + object, without عذرًا. A known cause goes in its own short sentence after it | حدث خطأ أثناء حفظ التغييرات · حدث خطأ أثناء رفع الملف. حجمه أكبر من 25 ميجابايت. |
| Generic error | Fixed string | عذرًا، حدث خطأ. يُرجى إعادة المحاولة. |
| Error with a fix | What happened or why, then what to do, only when the user can act on it. At most two short sentences; never repeat a word across them | الصورة أكبر من 25 ميجابايت. يُرجى اختيار ملف أصغر. |
| No connection | Fixed string | تحقّق من اتصالك بالإنترنت ثم حاول مرة أخرى |
| Session expired | Fixed string: the reason in the user's terms, then the next step | لحمايتك، سجّلنا خروجك. سجّل الدخول للمتابعة. |
| Progress | جارٍ + verbal noun + ellipsis character | جارٍ الحفظ… · جارٍ التحميل… |
| Empty list | If the user can create the item on this screen: an invitation, then a verbal-noun button. Otherwise: what is missing + بعد | ابدأ بإنشاء أول مشروع + إنشاء مشروع · لا توجد منتجات في السلة بعد |
| No search results | Name the query, suggest the next step | لم نجد نتائج لـ«ساعة». جرّب كلمة أخرى. |
| Destructive dialog | Title: هل أنت متأكّد من + verbal noun؟ Body: what goes, and لا يمكن التراجع عن ذلك if it's final. Buttons: نعم، + imperative / إلغاء | هل أنت متأكّد من حذف المشروع؟ · سيُحذف المشروع وكل ملفاته، ولا يمكن التراجع عن ذلك. · نعم، احذف · إلغاء |
| Confirmation dialog (not destructive) | Title: هل تريد + verbal noun؟ Buttons: the action as a verbal noun / إلغاء | هل تريد تسجيل الخروج؟ · تسجيل الخروج · إلغاء |
| Required field | Fixed string | هذا الحقل مطلوب |
| Invalid value | Say what to enter. Show an example only for a format (phone, email, date), never an invented code, name or amount | أدخل رقم هاتف صحيحًا، مثل 05XXXXXXXX · قسيمة الخصم غير صالحة |
| Optional field | Label then (اختياري) | الاسم (اختياري) |
| Search placeholder | One word | ابحث |
| Status labels | Fixed set | معلّق · قيد المراجعة · مكتمل · فشل |
| Rating question | ما مدى + رضاك عن / احتمال أن توصي بـ / سهولة + object؟ Label both scale ends in words | ما مدى رضاك عن إتمام الطلب؟ · غير راضٍ إطلاقًا … راضٍ جدًا |
| Milestone success | Warm, one exclamation mark; تهانينا in the product | تهانينا على أول عملية بيع! |
| Support reply | Acknowledge, then the next step and when, only from facts the source gives. A vague source time stays vague (قريبًا) | استلمنا طلبك وسنردّ عليك خلال 24 ساعة. |
| Counts with a noun | Arabic plural rules, never one form for every number (see "Counts and plurals") | ملف واحد · ملفان · 3 ملفات · 15 ملفًا · 100 ملف |

## Terms that cause the most mistakes

Full list in the glossary. These are the ones agents get wrong by default:

- Password: **كلمة السر** (not كلمة المرور)
- Download / upload: **تحميل / رفع** (not تنزيل)
- Delete / remove: **حذف** destroys data; **إزالة** takes an item out of a list and keeps it
- Turn on / off: **تفعيل / إيقاف**
- Dark mode: **الوضع الليلي**
- Two-step verification: **المصادقة الثنائية**
- Cancel: **إلغاء**; undo: **تراجع**
- Help center: **مركز الدعم**; learn more: **قراءة المزيد**
- Phone number: **رقم الهاتف**
- Discount code: **قسيمة الخصم**; checkout: **إتمام الطلب**
- Click, in help text: **انقر**; long press: **اضغط مع الاستمرار** (the only اضغط)
- Online: **عبر الإنترنت** for a channel, **متّصل** for presence
- Feedback: **آراء** (رأيك to one person: شاركنا رأيك); survey: **استطلاع**; chatbot or assistant: **المساعد** (its first message says it's automated: أنا المساعد الآلي في {app}); support chat: **المحادثة**

## Counts and plurals

Arabic has six plural forms, chosen by the number. A single string like "{n} ملفات" is wrong for most numbers. With digits, the noun changes as follows (CLDR categories, as returned by `Intl.PluralRules('ar')`):

| Category | Numbers | Pattern | ملف (file) | رسالة (message) |
| --- | --- | --- | --- | --- |
| zero | 0 | A sentence, no digit | لا توجد ملفات | لا توجد رسائل |
| one | 1 | Singular + واحد, no digit | ملف واحد | رسالة واحدة |
| two | 2 | Dual, no digit | ملفان (subject) · ملفين (after a verbal noun or preposition) | رسالتان · رسالتين |
| few | 3-10, 103-110… | Digit + plural | 3 ملفات | 3 رسائل |
| many | 11-99, 111-199… | Digit + singular with tanween; nothing added after ة | 15 ملفًا | 15 رسالة |
| other | 100-102, 200, 1000… and decimals | Digit + singular | 100 ملف | 100 رسالة |

- 101 and 102 are "other" too: 101 ملف, 102 ملف.
- Never write a number in words except واحد and the dual; digits avoid the gender agreement of ثلاثة/ثلاث.
- **Adjectives agree with the form the number chose.** A non-human plural takes a feminine singular adjective: 3 إشعارات غير مقروءة. With 11-99 the adjective follows the singular: 15 ملفًا جديدًا · 11 إشعارًا غير مقروء. The dual takes a dual adjective: إشعاران غير مقروءين. واحد comes last: رسالة جديدة واحدة.
- **People take the genitive plural after 3-10**: 3 مستخدمين, not 3 مستخدمون; then 15 مستخدمًا and 100 مستخدم.
- Never use a bracketed ending such as ملف(ات) or رسالة/رسائل.
- **Live counts** (followers, posts, views) need the same forms. If the code can't choose one, write the count as a label: المتابعون: 11, not 11 متابع.
- In code, keep six forms per message, not per noun: the dual and plural change with their place in the sentence (حُدِّد ملفان · جارٍ رفع ملفين). Pick the form with `new Intl.PluralRules('ar').select(n)`:

```js
const selected = { zero: 'لم يُحدَّد أي ملف', one: 'حُدِّد ملف واحد', two: 'حُدِّد ملفان', few: 'حُدِّد {n} ملفات', many: 'حُدِّد {n} ملفًا', other: 'حُدِّد {n} ملف' };
const label = (n) => selected[new Intl.PluralRules('ar').select(n)].replace('{n}', n.toLocaleString('en-US'));
```

ICU MessageFormat does the same: `{count, plural, zero {لم يُحدَّد أي ملف} one {حُدِّد ملف واحد} two {حُدِّد ملفان} few {حُدِّد # ملفات} many {حُدِّد # ملفًا} other {حُدِّد # ملف}}`. Format `#` with a Latin-digit locale (see "In code" under Numbers).

## Spelling, marks and punctuation

- **Shadda on verbs and participles** (سجّل، تحقّق، حُدِّد، معلّق، مفعّل، متّصل), not on nouns and adjectives that read one way without it (كلمة السر، مرة، أول، الإلكتروني، التحقق). Other vowel marks only where they prevent a misreading: the passive damma (حُفظت), tanween on adverbs (عذرًا، صحيحًا).
- **Hamza strictly.** Words that start with a connecting alif take no hamza: اتصل، اكتشف، اختر، ابحث، استمرار، انضم، اسم. In user-written content, flag a slip but do not change it.
- **Arabic punctuation**: ، ؛ ؟ in Arabic text, never , ; ? and no space before them.
- **No tatweel** (ـ) in UI text: تابع, not تابــع. It breaks search and copy-paste. Only a one-letter prefix before a quote, a Latin word or a digit keeps it (لـ«ساعة»، بـApple Pay).
- **Quotation marks**: guillemets « », not curly “ ” and not straight "".
- **Ellipsis**: the single character … not three dots.
- **Full stop**: none on labels, buttons, titles, helper text, toasts, banners and one-sentence errors (هذا الحقل مطلوب · حُفظت التغييرات). A full stop in body text, chat and support replies, and any message of two or more sentences (عذرًا، حدث خطأ. يُرجى إعادة المحاولة.).

## Numbers, dates and names

- **Market**: these rules follow Gulf and Egyptian readers. `Intl` writes a decimal comma for the Maghreb and Lebanon (1.234,5 in `ar-DZ`, `ar-MA`, `ar-LB`) and other month names in Algeria and Tunisia (جانفي) and in the Levant and Iraq (كانون الثاني). A product only for those markets formats with its own locale, and the decimal-comma rule and month list below don't apply.
- **Digits**: Western 0-9 everywhere, including inside Arabic sentences.
- **Decimals and thousands**: decimal point and a thousands comma, as Gulf users read them: 1,234.5 and 12,500 ر.س. Never a decimal comma: to a Gulf reader the comma marks thousands, so 2,500 means two thousand five hundred, never two and a half.
- **Time**: digits then صباحًا or مساءً: 3:00 مساءً.
- **Dates**: Gregorian unless the product uses Hijri. Day, month name, year, no comma: 5 مارس 2026; with a weekday: الخميس، 5 مارس 2026. Months: يناير، فبراير، مارس، أبريل، مايو، يونيو، يوليو، أغسطس، سبتمبر، أكتوبر، نوفمبر، ديسمبر. A Hijri date ends in هـ.
- **Relative time**: قبل + count, with the plural rules: قبل دقيقة واحدة · قبل دقيقتين · قبل 5 دقائق · قبل 11 دقيقة. الآن for just now, أمس for yesterday. Never منذ with مضت.
- **In code**, format with `Intl` and a Latin-digit locale: `new Intl.DateTimeFormat('ar-u-ca-gregory-nu-latn', { dateStyle: 'long' })` and `new Intl.RelativeTimeFormat('ar-u-nu-latn', { numeric: 'auto' })` give the forms above. Locales such as ar-SA and ar-EG print Arabic-Indic digits unless you add `-u-nu-latn`.
- **Brand names**: Latin script, never transliterated (Apple Pay, not أبل باي). Wrap Latin text inside Arabic in a bidi isolate in the component (`<bdi>` or `dir="auto"` on its element), never as markup inside a translation string.

## Checklist before answering

- [ ] Every product button is a verbal noun, unless it is sign in, sign up (سجّل الآن), retry or a destructive confirmation.
- [ ] Every term matches the glossary; no loanwords; no "الخاص بك".
- [ ] Success uses a passive verb or اكتمل; errors say what to do only when the user can act and no button already says it; no exclamation mark in errors.
- [ ] Nothing added that the source does not say; no invented example values; no longer than it needs to be.
- [ ] Arabic punctuation, « » quotes, single-character ellipsis.
- [ ] Shadda on verbs and participles; no hamza on connecting alif.
- [ ] Western digits; 1,234.5 format; dates like 5 مارس 2026; relative time with قبل; brand names in Latin.
- [ ] Every count uses the right plural form for its number, and its adjectives agree.
- [ ] No dialect outside marketing and onboarding.
- [ ] Apology only for our own faults; rating scales labelled at both ends; SMS within 70 characters.
