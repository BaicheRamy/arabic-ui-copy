# Decision log: arabic-ui-copy

Every house rule in the skill comes from one of these 59 questions. For each one, a native Arabic product designer (Ramy) picked an option or wrote his own after seeing which products use which wording. The research behind the options is in [strings.csv](strings.csv) and the research notes.

- **Options** lists every choice offered, with the products or guides that use it, as found in the research (2026-10-28). The ones not picked are where products disagree with the house style.
- **Changed since** records every later change and why. Nothing changed silently.
- **Override** names a regional profile that switches the rule off or swaps the term, for teams that need the other answer.

A house style picks one answer where correct Arabic allows several. كلمة السر and تحميل are choices, not corrections: use a profile or fork the glossary if your product needs the other word.


## A. Voice and grammar

| # | Question | Options (who uses them) | Picked | Changed since | Override |
| --- | --- | --- | --- | --- | --- |
| A1 | Button labels: verbal noun or command? | حفظ · إضافة · حذف (WordPress, Proton, UAE Design System, Google buttons) · احفظ · أضف · احذف (Arabeyes (quoted by WordPress); Tabby's احذف الحساب) · Noun for product actions, command for marketing CTAs (اطلب الآن، جرّب مجانًا) (Proton; Tamara and HungerStation in practice) | حفظ · إضافة · حذف |  |  |
| A2 | Instructions and helper text: how do we tell the user to do something? | اختر طريقة الدفع (UAE Design System, Apple, most products) · يرجى اختيار طريقة الدفع (Government services, Google help) · اختيار طريقة الدفع (no verb aimed at the user) (Proton's gender-neutral rephrasing) | يرجى اختيار طريقة الدفع | Written يُرجى (with the passive damma). |  |
| A3 | Gender: how do we address the user? | Masculine singular is fine (اختر، أدخل) (All 20+ products checked) · Rephrase to stay neutral where it costs nothing (يرجى إدخال، تم إرسال الرمز إليك) (Proton guidance) · Support a gender setting and inflect (اختر / اختاري) (Twitter feminine Arabic, Android 14 inflection API) | Rephrase to stay neutral where it costs nothing (يرجى إدخال، تم إرسال الرمز إليك) | Examples now use أُرسل, not تم إرسال: the skill avoids تم + verbal noun. |  |
| A4 | Singular or plural when greeting the user? | أهلاً بك (Tawakkalna, most apps) · أهلاً بكم (Absher) · Singular in product, plural on marketing pages | أهلاً بك |  |  |
| A5 | Register: standard Arabic or dialect? | Modern Standard Arabic everywhere (WordPress, UAE, Onetime Secret) · MSA in the product, light dialect allowed in marketing and onboarding (Tamara, HungerStation mix) · The local dialect of each market (Product-Led Alliance article) | MSA in the product, light dialect allowed in marketing and onboarding |  |  |
| A6 | When do we say "please"? | Always يرجى in requests and errors (UAE Design System, Ministry of Finance) · Only in errors and requests that cost the user effort; plain commands otherwise (Proton) · Never; keep it direct (Apple, Tawakkalna) · الرجاء or من فضلك instead of يرجى (Microsoft (once)) | الرجاء or من فضلك instead of يرجى | Refined 2026-10-29: يُرجى in helper text and errors; من فضلك or الرجاء only on conversational surfaces (onboarding, support chat, assistant replies). |  |
| A7 | Success message after saving | تم الحفظ · تم حفظ التغييرات · حُفظت التغييرات (Purist form, avoids تم + noun) · تم الحفظ بنجاح | حُفظت التغييرات |  |  |
| A8 | Failure message when an action fails | تعذّر حفظ التغييرات (Proton) · فشل حفظ التغييرات · لم يتم حفظ التغييرات · حدث خطأ أثناء حفظ التغييرات | حدث خطأ أثناء حفظ التغييرات |  |  |
| A9 | Progress text while something runs | جارٍ الحفظ… (Proton, Google (جارٍ التحميل)) · جاري الحفظ… (Common spelling in apps) · يتم الحفظ… | جاري الحفظ… | Changed 2026-10-29 to جارٍ after the Grok/Gemini review: no string in the research used جاري, Google and Proton write جارٍ, and it is the standard spelling. |  |
| A10 | "Now" in call-to-action buttons | Allowed in marketing CTAs only (اشترِ الآن، سجّل الآن) (noon, HungerStation) · Never in buttons; it adds nothing · الحين is fine for a Gulf brand voice (Tamara, HungerStation) | Allowed in marketing CTAs only (اشترِ الآن، سجّل الآن) | سجّل الآن (B2) is the one product button that keeps الآن. |  |
| A11 | Diacritics in UI text | None, ever · Only where they prevent a misreading (تعذّر، حمّل، جارٍ) (Google, Proton) · Shadda always, other marks only to disambiguate | Shadda always, other marks only to disambiguate | Narrowed 2026-10-29 to verbs and participles: taken literally, "always" would mark about 70 words that no product marks (كلمة السرّ، مرّة، أوّل). |  |
| A12 | Exclamation marks in success and welcome messages | Never · One, only in welcome or celebration moments (أهلاً بك!) · Fine anywhere the tone is warm | Fine anywhere the tone is warm | Narrowed 2026-10-29: at most one, only in welcomes, milestone success and thanks; never in routine success, errors or dialogs. |  |

## B. Terms

| # | Question | Options (who uses them) | Picked | Changed since | Override |
| --- | --- | --- | --- | --- | --- |
| B1 | Sign in | تسجيل الدخول (Apple, Google, Microsoft, most) · الدخول · دخول (Absher button) · سجّل دخولك (Commerce apps) | سجّل دخولك |  |  |
| B2 | Sign up | إنشاء حساب (Google, Apple) · تسجيل · سجّل الآن (Commerce apps) · حساب جديد | سجّل الآن |  |  |
| B3 | Sign out | تسجيل الخروج (Big tech) · الخروج · خروج | تسجيل الخروج |  |  |
| B4 | Password | كلمة المرور (Google, Microsoft, Tawakkalna) · كلمة السر (Apple) · الرقم السري (Banking apps) | كلمة السر |  | gulf profile: كلمة المرور |
| B5 | One-time verification code (OTP) | رمز التحقق · كود التحقق (stc style) · رمز التحقق لمرة واحدة | رمز التحقق |  |  |
| B6 | Download and upload | تنزيل / رفع (Apple, Google, Microsoft) · تحميل / رفع (Government apps (حمّل)) · تنزيل / تحميل | تحميل / رفع |  |  |
| B7 | Delete vs remove | حذف destroys data; إزالة takes something out of a list (Google (help text vs buttons)) · حذف for both · إزالة for both | حذف destroys data; إزالة takes something out of a list |  |  |
| B8 | Turn a setting on and off | تفعيل / إيقاف (Google) · تشغيل / إيقاف التشغيل (Apple, Microsoft) · تمكين / تعطيل | تفعيل / إيقاف |  |  |
| B9 | Dark mode | الوضع الداكن · النمط الداكن (Apple) · الوضع المعتم (Google) · الوضع الليلي | الوضع الليلي |  |  |
| B10 | Reset | إعادة تعيين (Apple, Microsoft) · إعادة ضبط (Google) | إعادة ضبط |  |  |
| B11 | Two-step verification | التحقق بخطوتين (Google) · المصادقة بخطوتين (Apple) · التحقق على خطوتين (Microsoft) · المصادقة الثنائية | المصادقة الثنائية |  |  |
| B12 | Dashboard | لوحة التحكم · لوحة المعلومات · الرئيسية · داشبورد | الرئيسية |  |  |
| B13 | Shopping cart | السلة (Salla, Zid) · سلة التسوق (Tabby) · عربة التسوق (noon) | سلة التسوق |  |  |
| B14 | Checkout button | إتمام الشراء · إتمام الطلب · الدفع · متابعة الدفع | إتمام الطلب |  |  |
| B15 | Discount code | رمز الخصم (Salla) · كود الخصم (stc) · كوبون الخصم (Salla) · قسيمة الخصم | قسيمة الخصم |  |  |
| B16 | Continue / next step button | متابعة · التالي · استمرار (Tabby) | استمرار |  |  |
| B17 | Cancel button | إلغاء · إلغاء الأمر · تراجع | تراجع | Changed 2026-10-29: إلغاء for Cancel, تراجع for Undo, so the two never share a word. |  |
| B18 | Retry button | إعادة المحاولة (Google) · حاول مرة أخرى · أعد المحاولة | أعد المحاولة |  |  |
| B19 | View all | عرض الكل · مشاهدة الكل · الكل | عرض الكل |  |  |
| B20 | Learn more | اعرف المزيد · اعرف أكثر · قراءة المزيد · المزيد | قراءة المزيد |  |  |
| B21 | Help center | مركز المساعدة · المساعدة · مركز الدعم · الدعم الفني | مركز الدعم |  |  |
| B22 | Contact us | تواصل معنا (Most products) · اتصل بنا (Talabat (spelled إتصل)) | تواصل معنا |  |  |
| B23 | FAQ | الأسئلة الشائعة (Most) · الأسئلة المتكررة · أسئلة وأجوبة | الأسئلة الشائعة |  |  |
| B24 | Email | البريد الإلكتروني · الإيميل · البريد | البريد الإلكتروني |  |  |
| B25 | Phone number field label | رقم الجوال (Saudi products) · رقم الهاتف · رقم الموبايل · رقم الهاتف المحمول | رقم الهاتف |  | gulf profile: رقم الجوال |
| B26 | Security (settings section) | الأمان (Google, Microsoft) · الأمن (Apple) | الأمان |  |  |
| B27 | Verb for click/tap in help text | اضغط · انقر (Google, Apple on Mac) · حدد (Microsoft) · اضغط on mobile, انقر on desktop (Apple) | انقر |  |  |
| B28 | English loanwords in general (أونلاين، كاش باك، الويتر) | Avoid; always use the Arabic term (WordPress glossary) · Allow ones people actually say, in marketing only · Allow them anywhere they read more naturally (Foodics, Zid) | Avoid; always use the Arabic term |  |  |

## C. Messages

| # | Question | Options (who uses them) | Picked | Changed since | Override |
| --- | --- | --- | --- | --- | --- |
| C1 | Title of a delete confirmation dialog | حذف المشروع؟ · هل تريد حذف المشروع؟ · هل أنت متأكد من حذف المشروع؟ | هل أنت متأكد من حذف المشروع؟ | Written متأكّد (shadda on participles, A11). |  |
| C2 | Buttons of that dialog | حذف · إلغاء · نعم، احذف · لا · حذف المشروع · إلغاء · تأكيد · إلغاء | نعم، احذف · لا | Changed 2026-10-29: نعم، احذف · إلغاء, with a body line saying what goes and لا يمكن التراجع عن ذلك. |  |
| C3 | Generic error | حدث خطأ ما. حاول مرة أخرى. (stc 404, Google) · عذرًا، حدث خطأ. يُرجى إعادة المحاولة. (Google sign-up page) · حدث خطأ غير متوقع. حاول مرة أخرى بعد قليل. | عذرًا، حدث خطأ. يُرجى إعادة المحاولة. |  |  |
| C4 | No internet connection | لا يوجد اتصال بالإنترنت · أنت غير متصل بالإنترنت · تحقق من اتصالك بالإنترنت ثم حاول مرة أخرى | تحقق من اتصالك بالإنترنت ثم حاول مرة أخرى | Written تحقّق (shadda on verbs, A11). |  |
| C5 | Session expired | انتهت الجلسة. سجّل الدخول مرة أخرى. · انتهت صلاحية الجلسة، يرجى تسجيل الدخول من جديد. · لحمايتك، سجّلنا خروجك. سجّل الدخول للمتابعة. | لحمايتك، سجّلنا خروجك. سجّل الدخول للمتابعة. |  |  |
| C6 | Required field left empty | هذا الحقل مطلوب · أدخل الاسم · يرجى إدخال الاسم · الاسم مطلوب | هذا الحقل مطلوب |  |  |
| C7 | Invalid phone number | رقم الجوال غير صحيح · أدخل رقم جوال صحيح، مثل 05XXXXXXXX · رقم الجوال غير صالح | أدخل رقم جوال صحيح، مثل 05XXXXXXXX | Written أدخل رقم هاتف صحيحًا، مثل 05XXXXXXXX to match B25 (all three options used جوال). |  |
| C8 | No search results | لا توجد نتائج · لا توجد نتائج لـ«ساعة» · لم نجد نتائج لـ«ساعة». جرّب كلمة أخرى. | لم نجد نتائج لـ«ساعة». جرّب كلمة أخرى. | Written with “ ” (D3). |  |
| C9 | Empty cart | سلتك فارغة · السلة فارغة · لا توجد منتجات في السلة بعد | لا توجد منتجات في السلة بعد |  |  |
| C10 | Empty list with a call to action (no projects yet) | لا توجد مشاريع بعد · إنشاء مشروع · ابدأ بإنشاء أول مشروع · إنشاء مشروع · لم تنشئ أي مشروع بعد · مشروع جديد | ابدأ بإنشاء أول مشروع · إنشاء مشروع |  |  |
| C11 | Status labels: pending, in review, completed, failed | قيد الانتظار · قيد المراجعة · مكتمل · فشل · معلّق · قيد المراجعة · مكتمل · فاشل · بانتظار · تحت المراجعة · تم · تعذّر | معلّق · قيد المراجعة · مكتمل · فاشل | Changed 2026-10-29: فشل, the status noun, not the adjective فاشل. |  |
| C12 | Search field placeholder | ابحث · بحث · ابحث عن منتج أو متجر | ابحث |  |  |
| C13 | Optional field marker | الاسم (اختياري) (Zid) · الاسم — اختياري · Mark required fields with * instead | الاسم (اختياري) |  |  |

## D. Numbers and punctuation

| # | Question | Options (who uses them) | Picked | Changed since | Override |
| --- | --- | --- | --- | --- | --- |
| D1 | Default digits in Arabic UI | Western digits 0-9 everywhere (Most Gulf apps) · Arabic-Indic ٠-٩ everywhere · Western for Gulf and Maghreb, Arabic-Indic for Egypt and the Levant · Western in data and inputs, Arabic-Indic allowed in prose and marketing | Western digits 0-9 everywhere |  |  |
| D2 | Decimal and thousands separators | 1,234.5 (UAE Design System, WordPress) · 1234,5 (decimal comma, no thousands mark) (Proton) · ١٬٢٣٤٫٥ when digits are Arabic-Indic, 1,234.5 otherwise | 1234,5 (decimal comma, no thousands mark) | Changed 2026-10-29 to 1,234.5: to a Gulf reader 2,500 means two thousand five hundred. Maghreb readers use a decimal comma: --profile maghreb. | maghreb profile: decimal comma |
| D3 | Quotation marks | «» (UAE Design System) · “” (WordPress) | “” |  |  |
| D4 | Brand and product names | Keep in Latin script (Apple Pay) · Write in Arabic (أبل باي) · Use the brand's official Arabic name if one exists, else Latin | Keep in Latin script (Apple Pay) |  |  |
| D5 | Time of day | 3:00 م · 3:00 مساءً · 15:00 (24-hour) | 3:00 مساءً |  |  |
| D6 | How strict on spelling (hamza, taa marbuta, اتصل not إتصل)? | Strict: the agent must always spell correctly and flag slips it sees · Strict in UI, flag but don't block in user content | Strict in UI, flag but don't block in user content |  |  |

## Later decisions

Rules added after the interview, each approved by the designer:

- 2026-10-29 (CX book review): feedback آراء, survey استطلاع, support chat المحادثة, assistant المساعد, تهانينا in the product (مبروك in marketing), apologise only for our own faults.
- 2026-10-29 (Grok and Gemini review): phone label stays رقم الهاتف, with helper text on fields that receive a code; the assistant's first message says it is automated (أنا المساعد الآلي في {app}); no full stop on labels, buttons, titles, helper text, toasts, banners or one-sentence errors.
- 2026-10-29: payment, delete and permission rules (references/sensitive-states.md) and regional profiles (references/profiles/).
