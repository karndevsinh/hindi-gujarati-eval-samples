# Annotation guideline

Short guideline for comparing two answers (A and B) to the same Hindi or Gujarati prompt. It is written in English, Hindi and Gujarati. The Hindi and Gujarati versions are in `guideline.hi.md` and `guideline.gu.md`.

## Steps

1. Read the prompt and list every constraint: length, number of items, script, register (formal or friendly), format.
2. Read both answers fully. Do not choose from the first sentence.
3. Score each answer from 1 to 5 on each criterion in `rubric.json`.
4. Check accuracy first. A wrong fact, wrong calculation, changed meaning, invented detail or unsafe advice is a critical failure and loses to an answer without one, however well written it is.
5. Write one or two sentences of reasoning for each answer. Name the exact problem ("uses 'तू' to a customer"), not a general feeling ("sounds off").

## Language checks

- **Script:** Hindi in Devanagari, Gujarati in Gujarati script, unless the prompt asks otherwise. Roman-letter Hindi or Gujarati breaks a script instruction.
- **Register:** use 'आप' / 'આપ' for customers, patients, managers and elders. 'तुम'/'तू' and 'તું'/'તારો' are only for close friends or children.
- **Gender and number agreement:** the verb agrees with the subject ('बहन गई', not 'बहन गया').
- **English mixing:** common words such as 'WhatsApp' or 'QR' are fine. Replacing ordinary words with English, or heavy jargon for a lay reader, lowers language quality.
- **Meaning:** compare with the prompt, not with word-for-word translation. Natural wording that keeps the meaning is correct.

## Scoring notes

- 5 = nothing to fix. 3 = noticeable problem but usable. 1 = fails the criterion.
- Do not reward length. A shorter answer that follows the constraints beats a longer one that does not.
- Do not punish a valid regional word choice. Mark it down only if it is wrong or unclear.
- If both answers have the same critical failure, compare on the remaining criteria.
- If unsure about a fact, check a reliable source before scoring. Do not guess.
