# arabic-ui-copy

[العربية](README.ar.md)

A free Agent Skill for Arabic product work, by Ramy ([@BaicheRamy](https://github.com/BaicheRamy)), product designer.

| Skill | What it does |
| --- | --- |
| [arabic-ui-copy](skills/arabic-ui-copy) | Arabic interface text that reads as native product Arabic, not translated English, with a checker for locale files |

```bash
npx skills add BaicheRamy/arabic-ui-copy
```

## Evidence

- `evidence/arabic-ui-copy/strings.csv`: 438 live Arabic UI strings with product, source URL and date collected.
- `evidence/arabic-ui-copy/evals/`: 38 test cases run with and without the skill on five models (Claude Haiku, Sonnet and Opus, Grok, Gemini), with raw outputs and the scorer.
- `tests/arabic-ui-copy/`: checker tests, run on every push.

MIT licence.
