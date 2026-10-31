# Examples: what agents write, and what to write instead

Each pair shows a typical machine-translated or agent-written string, the house version, and why. Copy the pattern, not just the string.

## Buttons and links

| English | Agent writes | Write | Why |
| --- | --- | --- | --- |
| Save | احفظ | حفظ | Product buttons are verbal nouns. |
| Add to cart | أضف إلى السلة | إضافة إلى السلة | Same rule. |
| Continue | المتابعة | استمرار | Glossary term, no ال on a button. |
| Cancel | إلغاء الأمر | إلغاء | Glossary term; إلغاء الأمر is a Windows-era calque. |
| Undo | إلغاء | تراجع | Cancel and Undo are different words. |
| Try again | إعادة المحاولة | أعد المحاولة | Retry is one of the four imperative exceptions. |
| Sign in | تسجيل الدخول | سجّل دخولك | Sign-in button is an invitation, so imperative. Keep تسجيل الدخول for the page title. |
| Download invoice | تنزيل الفاتورة | تحميل الفاتورة | Glossary: تحميل for download. |
| Learn more | اعرف المزيد | قراءة المزيد | Glossary term, and verbal-noun form. |
| Touch and hold the photo (help text) | المس الصورة مطولًا | اضغط مع الاستمرار على الصورة | Glossary: long press; انقر is only a tap. |
| Get started now (product screen) | ابدأ الآن | بدء الاستخدام | "Now" belongs only to marketing CTAs. On a marketing page, ابدأ الآن is fine. |
| Apply coupon | تطبيق الكوبون | تطبيق القسيمة | No loanwords; glossary term. |

## Success, progress and errors

| English | Agent writes | Write | Why |
| --- | --- | --- | --- |
| Your changes have been saved successfully! | لقد تم حفظ تغييراتك بنجاح! | حُفظت التغييرات | Passive past verb; drop لقد, بنجاح and the possessive. |
| Code sent | تم إرسال الكود | أُرسل رمز التحقق | Passive verb; no loanword. |
| Saving... | جاري الحفظ... | جارٍ الحفظ… | Standard spelling جارٍ; single ellipsis character. |
| Loading | تحميل | جارٍ التحميل… | Progress needs جارٍ; bare تحميل reads as a Download button. |
| Oops! Something went wrong. | عفوًا! حدث خطأ ما. | عذرًا، حدث خطأ. يُرجى إعادة المحاولة. | Fixed generic error; no exclamation mark in errors; say what to do. |
| Failed to save changes | فشل في حفظ التغييرات | حدث خطأ أثناء حفظ التغييرات | House pattern for a failed action. |
| Network error | خطأ في الشبكة | تحقّق من اتصالك بالإنترنت ثم حاول مرة أخرى | House fixed string; errors tell the user what to do. |
| Your session has expired. Please log in again. | انتهت صلاحية جلستك. الرجاء تسجيل الدخول مرة أخرى. | لحمايتك، سجّلنا خروجك. سجّل الدخول للمتابعة. | House fixed string: the reason in the user's terms, then the next step. |
| Couldn't load comments. + a Retry button | عذرًا، تعذّر تحميل التعليقات. يُرجى إعادة المحاولة. | حدث خطأ أثناء تحميل التعليقات + أعد المحاولة | No عذرًا on a named failure; the button already says retry. |

## Forms

| English | Agent writes | Write | Why |
| --- | --- | --- | --- |
| Enter your password | أدخل كلمة المرور الخاصة بك | كلمة السر (as the label) | Glossary term; no "الخاصة بك"; a label is a noun. |
| Email address | عنوان الإيميل | البريد الإلكتروني | No loanwords. |
| This field is required | هذا الحقل إلزامي | هذا الحقل مطلوب | Fixed string. |
| Invalid phone number | رقم الجوال غير صالح | أدخل رقم هاتف صحيحًا، مثل 05XXXXXXXX | Say what to enter, show an example; glossary term رقم الهاتف. |
| Company (optional) | الشركة - اختياري | الشركة (اختياري) | House marker. |
| Choose a payment method | اختر طريقة الدفع الخاصة بك | يُرجى اختيار طريقة الدفع | Helper text uses يُرجى + verbal noun, which also avoids gender. |
| Search products... | البحث عن المنتجات... | ابحث | One-word placeholder. |
| We'll text you a code (helper text) | يُرجى إرسال رمز التحقق برسالة نصية | سنرسل لك رمز التحقق برسالة نصية | Helper text that informs is a statement; يُرجى is for instructions. |
| First name, when it must be in Arabic script | الاسم الأول | اسمك الأول، بالعربية | Say which script when it matters, or users type it in Latin letters. |

## Empty states and dialogs

| English | Agent writes | Write | Why |
| --- | --- | --- | --- |
| Your cart is empty | عربة التسوق الخاصة بك فارغة | لا توجد منتجات في السلة بعد | Glossary term; بعد implies it will fill. |
| No projects yet. Create one! | لا توجد مشاريع حتى الآن. أنشئ واحدًا! | ابدأ بإنشاء أول مشروع + button إنشاء مشروع | Invitation, then a verbal-noun button. |
| No results found | لم يتم العثور على نتائج | لم نجد نتائج لـ«ساعة». جرّب كلمة أخرى. | Name the query in « »; suggest a next step. |
| Are you sure you want to delete this project? | هل أنت متأكد أنك تريد حذف هذا المشروع؟ | هل أنت متأكّد من حذف المشروع؟ | Shorter house pattern. |
| Delete / Cancel (dialog buttons) | حذف / إلغاء | نعم، احذف / لا | House dialog buttons. |
| Sign out? (dialog) | هل أنت متأكد أنك تريد تسجيل الخروج؟ · نعم · لا | هل تريد تسجيل الخروج؟ · تسجيل الخروج · إلغاء | Not destructive: هل تريد, and the action as the button. |

## Settings and status

| English | Agent writes | Write | Why |
| --- | --- | --- | --- |
| Dark mode: On | الوضع الداكن: تشغيل | الوضع الليلي: مفعّل | Glossary terms; shadda. |
| Two-factor authentication | التحقق بخطوتين | المصادقة الثنائية | Glossary term. |
| Reset settings | إعادة تعيين الإعدادات | إعادة ضبط الإعدادات | Glossary term. |
| Pending | قيد الانتظار | معلّق | House status set. |
| Failed | فاشل | فشل | فاشل judges the thing as "a failure"; فشل names the event. |
| Notifications: Off | الإشعارات: إيقاف | الإشعارات: غير مفعّلة | A state is مفعّل / غير مفعّل, agreeing with the setting; إيقاف is the action. |
| Online (presence) | أونلاين | متّصل | No loanword; عبر الإنترنت is for a channel. |

## Counts

| English | Agent writes | Write | Why |
| --- | --- | --- | --- |
| 2 files selected | 2 ملفات محددة | حُدِّد ملفان | Dual, no digit; shadda on the doubled letter. |
| 3 unread notifications | 3 إشعارات غير مقروءين | 3 إشعارات غير مقروءة | A non-human plural takes a feminine singular adjective. |
| 3 active users | 3 مستخدمون نشطون | 3 مستخدمين نشطين | People after 3-10 take the genitive plural. |
| 15 items | 15 عناصر | 15 عنصرًا | 11-99 take the singular with tanween. |
| 1 new message | 1 رسائل جديدة | رسالة جديدة واحدة | One: singular + واحد, no digit. |
| 0 results | 0 نتائج | لا توجد نتائج | Zero is a sentence. |
| {n} file(s) | {n} ملف(ات) | six plural forms in code | Never a bracketed ending. |
| 11 followers | 11 متابع | 11 متابعًا | Live counts follow the plural rules too; if the code can't, use a label: المتابعون: 11. |

## Feedback, support and messages

| English | Agent writes | Write | Why |
| --- | --- | --- | --- |
| How satisfied are you with checkout? | ما مستوى رضاك عن عملية الدفع الخاصة بك؟ | ما مدى رضاك عن إتمام الطلب؟ | Glossary term; no possessive. |
| How likely are you to recommend {app} to a friend? | كم من المحتمل أن توصي بـ{app} لصديق؟ | ما مدى احتمال أن توصي بـ{app} لصديق؟ | كم من المحتمل copies "how likely". |
| How easy was it to find what you needed? | كم كان من السهل العثور على ما تحتاجه؟ | ما مدى سهولة العثور على ما تحتاج إليه؟ | Same calque; Arabic asks with ما مدى. |
| Thanks for your feedback! | شكرًا لك على ملاحظاتك! | شكرًا على رأيك! | Glossary: feedback is رأي; one exclamation mark in thanks. |
| Your verification code is 482913 (SMS) | رمز التحقق الخاص بك هو 482913 | رمز التحقق: 482913 | Every character counts in an Arabic SMS (70 per message). |
| Dear {name}, | عزيزي {name}، | مرحبًا {name}، | A name doesn't tell you the reader's gender. |
| We'll get back to you within 24 hours. | سنعود إليك في غضون 24 ساعات. | سنردّ عليك خلال 24 ساعة. | "Get back to you" calque; 24 takes the singular. |
| Congrats on your first sale! | تهانينا على أول عملية بيع خاصة بك!! | تهانينا على أول عملية بيع! | One exclamation mark; no possessive. |
| Sorry, this field is required | عذرًا، هذا الحقل مطلوب | هذا الحقل مطلوب | Apologise only for our own faults, never for the user's input. |
| Thanks for reaching out! We'll reply soon. | استلمنا طلبك وسنرد عليك قريبًا. | شكرًا لتواصلك! سنردّ عليك قريبًا. | Keep the source's thanks and its vague time; don't swap in a pattern's words. |
| Hi, I'm the {app} assistant. (first chat message) | مرحبًا، أنا مساعدك. | مرحبًا، أنا المساعد الآلي في {app}. | The first message says it's automated; المساعد alone can read as a person. |
| How do I install the font? (FAQ question) | كيف يمكنني تثبيت الخط؟ | كيف أثبّت الخط؟ | FAQ questions are in the user's voice; drop يمكنني. |

## Punctuation, numbers and names

| English | Agent writes | Write | Why |
| --- | --- | --- | --- |
| Continue? | المتابعة? | المتابعة؟ | Arabic question mark. |
| Name, email | الاسم, البريد الإلكتروني | الاسم، البريد الإلكتروني | Arabic comma. |
| Pay with Apple Pay | الدفع عبر أبل باي | الدفع عبر Apple Pay | Brand names stay in Latin script (isolate it in code). |
| 1,250.50 SAR | ١٬٢٥٠٫٥٠ ر.س | 1,250.50 ر.س | Western digits with a thousands comma and a decimal point. |
| 3:00 PM | ٣:٠٠ م | 3:00 مساءً | Western digits; full word. |
| Expires on March 5, 2026 | تنتهي في مارس 5, 2026 | تنتهي في 5 مارس 2026 | Day, month name, year; no comma. |
| Last updated 5 minutes ago | آخر تحديث منذ 5 دقائق مضت | آخر تحديث قبل 5 دقائق | قبل with the plural rules; never منذ with مضت. |
| Contact us | إتصل بنا | تواصل معنا | Glossary term; and اتصل never takes a hamza. |

## Money, deleting, permissions and flows

| English | Agent writes | Write | Why |
| --- | --- | --- | --- |
| Payment timed out. Please try again. | انتهت مهلة الدفع. يُرجى المحاولة مرة أخرى. | لم يصلنا تأكيد البنك بعد. لا تدفع مرة أخرى، وسنُعلمك بالنتيجة. | A timeout isn't a failure; paying again can charge twice. |
| Delete project? (dialog) | حذف المشروع؟ · نعم · لا | هل أنت متأكّد من حذف المشروع؟ · سيُحذف المشروع وكل ملفاته، ولا يمكن التراجع عن ذلك. · نعم، احذف · إلغاء | Say what goes and that it's final; إلغاء, not لا. |
| Allow location to see nearby stores. We never store your data. | اسمح بالوصول إلى موقعك. نحن لا نخزّن بياناتك أبدًا. | هل تريد السماح لـ{app} بالوصول إلى موقعك؟ · نستخدم موقعك لعرض المتاجر القريبة منك. يمكنك أيضًا إدخال الحي يدويًا. | Benefit, data used, alternative; no promise the copy can't keep. |
| Message deleted · Undo | تم حذف الرسالة! · تراجع | حُذفت الرسالة · تراجع | Passive verb, no تم, no exclamation mark. |
| Hello {name}! | مرحبًا {الاسم}! | مرحبًا {name}! | Placeholders stay exactly as in the source. |
| Cancel subscription? (dialog buttons) | إلغاء · لا | إلغاء الاشتراك · الاحتفاظ بالاشتراك | A bare إلغاء means both "end the plan" and "close". |
| Delete (icon button, screen-reader label) | زر الحذف | حذف | The reader already says "button"; use the visible button's word. |
