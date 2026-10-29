# Evals: arabic-ui-copy with and without the skill

38 UI strings (`prompts.json`), each with a reference answer, required phrases and banned phrases (`cases.json`). 20 are **universal**: things any careful Arabic writer gets right (plurals, placeholders, payment timeouts, permission promises, digits). 18 are **house**: the skill's own choices (كلمة السر, تحميل, جارٍ, الوضع الليلي). Each model wrote all 38 once with the skill and once without it, on 2026-10-29. Haiku, Sonnet and Opus ran as agents with the skill installed. Grok and Gemini ran in their chat apps with the whole skill pasted into the prompt (`other-models/`). Raw outputs are in `outputs/`; rerun the scores with `python3 score.py`.

| Run | All | Universal | House | Unseen | Checker, universal rules | Checker, all rules | Failed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| gemini-base | 27/38 | 19/20 | 8/18 | 10/13 | 1 | 17 | E03, E04, E09, E10, E11, E17, E25, E29, E32, E36, E37 |
| gemini-skill | 38/38 | 20/20 | 18/18 | 13/13 | 0 | 0 |  |
| grok-base | 29/38 | 18/20 | 11/18 | 11/13 | 0 | 12 | E03, E09, E10, E11, E23, E24, E25, E32, E37 |
| grok-skill | 38/38 | 20/20 | 18/18 | 13/13 | 0 | 0 |  |
| haiku-base | 25/38 | 16/20 | 9/18 | 10/13 | 1 | 14 | E03, E09, E10, E11, E17, E21, E23, E24, E25, E29, E32, E36, E37 |
| haiku-skill | 37/38 | 20/20 | 17/18 | 12/13 | 0 | 0 | E37 |
| opus-base | 31/38 | 20/20 | 11/18 | 11/13 | 0 | 12 | E03, E09, E10, E11, E25, E32, E37 |
| opus-skill | 38/38 | 20/20 | 18/18 | 13/13 | 0 | 0 |  |
| sonnet-base | 30/38 | 20/20 | 10/18 | 11/13 | 1 | 14 | E03, E09, E10, E11, E25, E32, E36, E37 |
| sonnet-skill | 38/38 | 20/20 | 18/18 | 13/13 | 0 | 0 |  |

"Unseen" counts the 13 cases whose answer is not written anywhere in the skill (SKILL.md or references/). The other 25 are in it word for word or close.

## What this does and doesn't show

- **Without the skill, every model fails some serious case.** Grok told the user to pay again after a payment timeout (E23) and promised "we don't store your data" when the brief said location is kept for 30 days (E24). Haiku did both too. Gemini wrote a cancel-subscription dialog whose buttons are تراجع and تأكيد الإلغاء (E29), which is easy to misread. With the skill, all five pass all 20 universal cases.
- **Those fixes come from cases the skill teaches directly.** On the 9 universal cases that are unseen, all five models already pass without the skill. So this suite shows the skill's rules being followed. It doesn't show that the skill helps with strings it has never seen. That needs new cases written by someone who hasn't read the skill.
- **Most of the score is house style.** Without the skill, models follow 8 to 11 of the 18 house choices. With it, they follow 17 or 18. That is the point of a house style, but a team with other preferences would score the base runs higher.
- **The grader is the author.** The people who wrote the skill also wrote the cases, the references and the pass rules. The checks are phrase matches, not judgment. A phrase match can't catch every slip: Grok with the skill wrote انقر الإعدادات, without على, and still passed E37.
- **Pasting is not installing.** With the full skill text in the prompt, Grok and Gemini saw every reference file. Installed, an agent opens a reference file only when it decides to. Their skill runs are a best case.
- **Still to do:** two native reviewers from different markets rating the outputs blind, and fresh held-out cases.
