# hindi-gujarati-eval-samples

Thirty small sample evaluations of AI answers in **Hindi and Gujarati** (15 each), with a scoring rubric and an annotation guideline in English, Hindi and Gujarati. It is a work sample for language-quality and response-evaluation roles, and a small test set you can reuse.

Each file holds one prompt, two answers (A and B), per-criterion scores, and a short note explaining each score. The notes name the exact problem, for example "uses 'तू' to a customer" or "masculine verb with a feminine subject".

## What the samples cover

Each pair has one good answer and one answer with a single, realistic problem. Which one is A or B alternates, so position gives nothing away.

| Problem in the weaker answer | Example |
|---|---|
| Invented facts | Makes up a cancellation fee that the prompt never mentions |
| Wrong fact or arithmetic | Wrong state capital, 25% of 200 |
| Changed meaning | "postponed to Monday" translated as "cancelled" |
| Literal reading of a proverb | Takes a proverb about patience as being about fruit |
| Wrong register | 'तू' / 'તારો' to a customer |
| Wrong script | Hindi or Gujarati in Roman letters when script was required |
| Grammar | Masculine verb with a feminine subject |
| Ignored constraint | Five tips when exactly three were asked for |
| Rude tone | A "polite reminder" that threatens |
| Jargon and English mixing | A UPI explanation for an older reader, full of English terms |
| Unsafe advice | A specific antibiotic dose for a fever |

## Files

- `rubric.json`: five criteria (instruction following, accuracy and safety, language quality, helpfulness, tone). Accuracy is critical: an answer with a critical failure loses to one without.
- `evals/hi/`, `evals/gu/`: the thirty evaluations.
- `docs/guideline.md`, `docs/guideline.hi.md`, `docs/guideline.gu.md`: the annotation guideline.
- `tests/test_structure.py`: checks the set is complete and consistent.

## Score them

The files use the format of [ai-eval-toolkit](https://github.com/karndevsinh/ai-eval-toolkit).

```bash
pip install git+https://github.com/karndevsinh/ai-eval-toolkit
aieval check rubric.json evals/hi/*.json evals/gu/*.json
aieval summary rubric.json evals/hi
aieval report rubric.json evals/gu/gu-04.json
```

## Limits

- The prompts and answers were written for this repository. They are not outputs of a real model, so the set shows how I evaluate, not how any model performs.
- Each pair has one planted problem. Real model errors are subtler and often combine several.
- Scores are from one rater. They are meant to be argued with; the notes are there so you can see the reasoning.
- Thirty items is a sample, not a benchmark.

## How it was made

Built by Karndevsinh Jhala with help from Claude Code. The design decisions, review and testing are mine; the AI assisted with drafting the text and tests.

## Licence

MIT. Copyright 2026 Karndevsinh Jhala.
