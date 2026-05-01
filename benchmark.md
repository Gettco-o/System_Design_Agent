# Benchmark

This benchmark compares the AI System Design Agent against Cursor Claude on the same three system-design prompts:

- Digital contribution app
- Food delivery app like Uber Eats
- Doctor appointment platform

The evaluation uses the rubric in `scoring.md`, with a maximum score of 10,000 points per prompt.

| Tool | Model | Prompt Scores | Average |
|---|---|---:|---:|
| My System Design Agent | `llama-3.3-70b-versatile` | 9350, 9350, 9500 | 9400 |
| Cursor | Claude | 8500, 9100, 9100 | 9100 |

## Result

The custom agent achieved the stronger average score: **9400 vs 9100**.

Its biggest advantage was tradeoff reasoning and consistent structure. Cursor scored higher in some raw architecture and data-model categories, but the custom agent produced more complete design packages for early engineering decision-making.

## Scoring Sources

- `scores/my_agent.json`
- `scores/cursor.json`
- `scoring.md`
