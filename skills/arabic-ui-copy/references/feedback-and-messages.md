# Feedback prompts, support replies and messages outside the app

Read this when you write rating or survey prompts, support or assistant replies, milestone messages, or text sent by SMS, push or email. Everything in SKILL.md still applies.

## Rating and feedback prompts

| Prompt | Pattern | Example | Scale ends (low · high) |
| --- | --- | --- | --- |
| Satisfaction (CSAT, 1-5) | ما مدى رضاك عن + object؟ | ما مدى رضاك عن إتمام الطلب؟ | غير راضٍ إطلاقًا · راضٍ جدًا |
| Recommend (NPS, 0-10) | ما مدى احتمال أن توصي بـ + product + لصديق؟ | ما مدى احتمال أن توصي بـ{app} لصديق؟ | غير محتمل إطلاقًا · محتمل جدًا |
| Ease (CES, 1-7) | ما مدى سهولة + verbal noun؟ | ما مدى سهولة إتمام الطلب؟ | صعب جدًا · سهل جدًا |
| Rate (when the source says "rate") | كيف تقيّم + object؟ | كيف تقيّم تجربتك معنا اليوم؟ | |
| Follow-up | Fixed string | ما سبب تقييمك؟ (اختياري) | |
| Invitation | Fixed string | شاركنا رأيك | |
| Thanks | Fixed string, warm | شكرًا على رأيك! | |
| Dismiss | Fixed string | ليس الآن | |
| Rate (button) | Verbal noun | تقييم | |

- One question per prompt, and the question the source asks: "rate" stays كيف تقيّم, "satisfied" is ما مدى رضاك. Name what is rated only when the source or the screen names it.
- Ask "how much" questions with ما مدى. Never كم من المحتمل or كم كان من السهل: they copy "how likely" and "how easy was it".
- Label both ends of every scale in words; a number alone doesn't say which end is good. Mirror the scale with the layout so each label stays beside its number.
- Scale labels use the short masculine form (راضٍ), because a neutral form would be much longer (the gender rule in SKILL.md).
- Where the scale isn't visible (SMS, voice), the message states it: ما مدى رضاك عن طلبك اليوم؟ أرسل رقمًا من 1 إلى 5.

## Support and assistant replies

- Acknowledge in a few words, then say the next step and when. Use only facts the source gives; never invent a time, a team or a name.
- No promise without a what or a when. سنعمل على حل مشكلتك في أقرب وقت ممكن says nothing; استلمنا طلبك وسنردّ عليك خلال 24 ساعة. says something, when the source gives the 24 hours.
- That rule is for copy you write. When you translate, a vague source time stays vague (soon: قريبًا) and a missing one stays missing; never invent a number.
- Reply is سنردّ عليك, not سنعود إليك (a copy of "get back to you"). Thanks for contacting us is شكرًا لتواصلك!
- Apologise only for our own faults (SKILL.md). نعتذر is for a delay, outage or charge error that cost the user time or money, and the fix or next step follows in the same message.
- The chatbot or assistant is المساعد. Its first message says it's automated (مرحبًا، أنا المساعد الآلي في {app}.), so no one mistakes it for a person; after that, المساعد alone is enough.
- Support chat is المحادثة; live chat is المحادثة المباشرة.

## Milestones

Routine success stays plain, with no exclamation mark: حُفظت التغييرات. A milestone (first project, first sale, goal reached) can be warm, with one exclamation mark, and stays short: تهانينا على أول عملية بيع! Use تهانينا in the product and keep مبروك for marketing.

## SMS, push and email

- **One glossary for every channel.** Run `scripts/check_copy.py` on push and email templates, and `scripts/check_copy.py --sms` on SMS templates.
- **SMS length.** One Arabic letter switches the whole SMS to UCS-2 encoding: 70 characters fit in one message, and once it splits each part holds 67. Latin-only text fits 160. Count with the longest value each variable can take, and cut words, never facts or actions: رمز التحقق: 482913, not رمز التحقق الخاص بك هو 482913. If every fact and action can't fit, say so instead of dropping one.
- **Push titles and email subjects.** Lead with the fact; lock screens and inboxes cut the end.
- **Names.** Greet with مرحبًا {name}، and never عزيزي or عزيزتي: a name doesn't tell you the reader's gender. Don't follow a name with a gendered adjective either.
- **Bidi in plain text.** SMS and email subjects have no component to isolate a Latin name or a number in. Test every template with a Latin name and a number in it.
