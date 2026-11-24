"""Structure checks for the sample set. Run: python -m unittest discover -s tests -v"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = {"hi": re.compile("[ऀ-ॿ]"), "gu": re.compile("[઀-૿]")}


def load(lang):
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "evals" / lang).glob("*.json"))]


class StructureTests(unittest.TestCase):
    def test_fifteen_per_language_with_unique_ids(self):
        ids = []
        for lang in ("hi", "gu"):
            items = load(lang)
            self.assertEqual(len(items), 15, lang)
            ids += [i["id"] for i in items]
        self.assertEqual(len(ids), len(set(ids)))

    def test_prompts_are_in_the_right_script(self):
        for lang, pattern in SCRIPT.items():
            for item in load(lang):
                self.assertRegex(item["prompt"], pattern, item["id"])

    def test_only_the_script_test_cases_may_use_roman_answers(self):
        roman = re.compile("[A-Za-z]{4,}")
        for lang in ("hi", "gu"):
            for item in load(lang):
                for key, text in item["responses"].items():
                    if roman.search(re.sub(r"UPI|NPCI|VPA|IMPS|WhatsApp|QR|mg|PIN|real-time|interbank|payment|system|develop|instant|transactions|enable|architecture|based|through", "", text)):
                        self.assertIn(item["flaw_in_weaker_response"], {"wrong_script", "jargon_mixing"}, item["id"])

    def test_winner_position_is_balanced(self):
        for lang in ("hi", "gu"):
            wins = {"A": 0, "B": 0}
            for item in load(lang):
                totals = {k: sum(v.values()) for k, v in item["scores"].items()}
                wins[max(totals, key=totals.get)] += 1
            self.assertLessEqual(abs(wins["A"] - wins["B"]), 3, lang)

    def test_every_note_is_present(self):
        for lang in ("hi", "gu"):
            for item in load(lang):
                self.assertEqual(set(item["notes"]), set(item["responses"]))
                self.assertTrue(all(len(n) > 10 for n in item["notes"].values()))


if __name__ == "__main__":
    unittest.main()
