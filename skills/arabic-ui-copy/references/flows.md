# Flows: undo toasts, onboarding, paywalls and subscriptions, screen-reader labels

Read this when you write any of these. Everything in SKILL.md still applies; for payment states and permission prompts, see sensitive-states.md.

## Undo toast

- What happened as a passive past verb, then تراجع as the action. No exclamation mark, no full stop.

  | Moment | Example |
  | --- | --- |
  | Toast | حُذفت الرسالة · تراجع |
  | Toast, a count | حُذفت 3 رسائل · تراجع |
  | After undo | استُعيدت الرسالة |

- تراجع only undoes. A toast that opens something uses the verbal noun of that action: أُضيف إلى السلة · عرض السلة.

## Onboarding

- One idea per screen: a short title that names the benefit and one sentence of body. Light dialect is allowed here (SKILL.md), but the buttons stay standard.

  | Part | Example |
  | --- | --- |
  | Title | تابع طلباتك لحظة بلحظة |
  | Body | نُعلمك عند شحن الطلب وعند وصوله. |
  | Buttons | التالي · تخطٍّ |
  | Last screen | بدء الاستخدام |

- Skip is تخطٍّ: an indefinite verbal noun keeps its tanween, the same rule as جارٍ.
- Don't ask for a permission on a welcome screen; ask when the feature needs it (sensitive-states.md).

## Paywalls, trials and subscriptions

- The price always comes with its currency and period, as large as the button: 29 ر.س شهريًا · 290 ر.س سنويًا.
- A trial says how long, what it costs after, and how to stop, only with facts the source gives:
  جرّب مجانًا لمدة 7 أيام، ثم 29 ر.س شهريًا. يمكنك الإلغاء في أي وقت قبل انتهاء الفترة التجريبية.
- Declining is neutral: ليس الآن. Never shame the user (لا، لا أريد التوفير).
- Cancelling a subscription says when access ends and what stops:
  سيبقى اشتراكك فعالًا حتى 5 مارس 2026، ثم يتوقف التجديد.
  Buttons: إلغاء الاشتراك · الاحتفاظ بالاشتراك. Never a bare إلغاء in this dialog: it can mean both "cancel the subscription" and "close".
- Terms: subscription اشتراك, free trial تجربة مجانية (the period: الفترة التجريبية), renewal تجديد, renews automatically يُجدَّد تلقائيًا.

## Screen-reader labels

- An icon-only button gets the label of the visible button it would have: حذف، بحث، إغلاق، مشاركة. When several look alike on one screen, add the object: حذف الصورة.
- Don't put the role in the label (no زر حذف): the screen reader already says "زر".
- State goes in the value, not the label: label الوضع الليلي, value مفعّل.
- Images: describe what matters in the picture (طفل يحمل حقيبة مدرسية), with no صورة لـ. Decorative images get an empty label.
- Hints, where the platform has them, are one present-tense sentence about the result: يفتح تفاصيل الطلب.
- Counts follow the plural rules: 3 إشعارات غير مقروءة. Set the page or view language to Arabic (lang="ar") so the Arabic voice reads it.
