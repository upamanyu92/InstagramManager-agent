import unittest

from darkside_prompt_generator import (
    DEFAULT_AESTHETIC_STYLE,
    generate_prompt,
    generate_use_case_prompt,
)


class DarksidePromptGeneratorTests(unittest.TestCase):
    def test_generate_prompt_inserts_subject_with_default_style(self):
        subject = "A drone hovers above a rainy neon market"

        prompt = generate_prompt(subject)

        self.assertIn(f"[THE SUBJECT]: {subject}", prompt)
        self.assertIn(f"[AESTHETIC STYLE]: {DEFAULT_AESTHETIC_STYLE}", prompt)
        self.assertIn("--no [NEGATIVE PROMPT]:", prompt)

    def test_generate_prompt_rejects_empty_subject(self):
        with self.assertRaises(ValueError):
            generate_prompt("   ")

    def test_generate_use_case_prompt(self):
        prompt = generate_use_case_prompt("moody_cityscape")

        self.assertIn("dystopian cityscape", prompt)
        self.assertIn("--no [NEGATIVE PROMPT]: Bright colors, daylight, photorealistic, cartoon, happy.", prompt)


if __name__ == "__main__":
    unittest.main()
