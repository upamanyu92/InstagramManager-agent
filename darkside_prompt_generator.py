"""Generate Darkside Pixel aesthetic prompts for image generation agents."""

from __future__ import annotations

import argparse
from typing import Dict

DEFAULT_AESTHETIC_STYLE = (
    "Detailed 32-bit pixel art, high fidelity, isometric perspective, tech-noir, atmospheric."
)
DEFAULT_LIGHTING_AND_COLOR = (
    "High contrast lighting, deep volumetric shadows, moody color palette dominated by "
    "obsidian blacks, electric blue and magenta neon, and subtle emerald green accents, "
    "specular highlights."
)
DEFAULT_ATMOSPHERE = (
    "Melancholic, nocturnal, futuristic, dense fog, light rain, reflective surfaces, low-fi grit."
)
DEFAULT_NEGATIVE_PROMPT = (
    "Bright colors, daylight, sunlight, pastel, joyful, photorealistic, low fidelity, "
    "low quality, 3D render, cartoon."
)

USE_CASES: Dict[str, Dict[str, str]] = {
    "moody_cityscape": {
        "aesthetic_style": "Detailed 32-bit pixel art, high fidelity, isometric, tech-noir.",
        "subject": (
            "An expansive, dense dystopian cityscape at night, massive towering structures "
            "linked by skybridges, a small cyber-monorail moving between buildings, "
            "thousands of tiny glowing windows."
        ),
        "lighting_and_color": (
            "Ultra-high contrast. Deepest blacks defining the structures. Pockets of intense, "
            "sharp neon: electric blue, violent purple, and toxic green, casting reflections "
            "on wet surfaces. Minimalist color application."
        ),
        "atmosphere": "Nocturnal, overwhelming scale, melancholic, low-fi grit, dense volumetric haze.",
        "negative_prompt": "Bright colors, daylight, photorealistic, cartoon, happy.",
    },
    "character_interior": {
        "aesthetic_style": "64-bit pixel art, high-definition retro-futurism, cinematic composition.",
        "subject": (
            "A medium shot of a solitary figure wearing a dark techwear jacket, sitting in a "
            "dimly lit, futuristic ramen stand. They are looking at a small holographic interface."
        ),
        "lighting_and_color": (
            "Moody and directional. A single overhead light source (cool white), contrasting "
            "sharply with the deep shadows of the interior and the warm amber glow of the "
            "ramen stand's sign."
        ),
        "atmosphere": "Nostalgic, melancholic, atmospheric, quiet solitude, heavy shadows.",
        "negative_prompt": "Sunlight, bright, happy, photorealistic, low resolution.",
    },
    "geometric_abstract": {
        "aesthetic_style": "Low-poly pixel art, minimalism, glitch aesthetic, 16-bit fidelity.",
        "subject": (
            "An abstract arrangement of fractured obsidian geometric shapes and glowing "
            "cybernetic data streams. The forms are sharp and defined by pixel grids."
        ),
        "lighting_and_color": (
            "Internal glow. Deep space black background, with shapes defined by sharp edges "
            "of electric blue and magenta light."
        ),
        "atmosphere": "Tech-noir, futuristic, digital consciousness, cool, sterile yet moody.",
        "negative_prompt": "Daylight, soft colors, analog, hand-drawn, cartoon.",
    },
}


def generate_prompt(
    subject: str,
    *,
    aesthetic_style: str = DEFAULT_AESTHETIC_STYLE,
    lighting_and_color: str = DEFAULT_LIGHTING_AND_COLOR,
    atmosphere: str = DEFAULT_ATMOSPHERE,
    negative_prompt: str = DEFAULT_NEGATIVE_PROMPT,
) -> str:
    """Build a Darkside Pixel prompt where only subject is expected to change."""
    if not subject or not subject.strip():
        raise ValueError("subject must be a non-empty string")

    return (
        "/imagine prompt:\n"
        f"[AESTHETIC STYLE]: {aesthetic_style}\n"
        f"[THE SUBJECT]: {subject.strip()}\n"
        f"[LIGHTING & COLOR]: {lighting_and_color}\n"
        f"[ATMOSPHERE]: {atmosphere}\n"
        f"--no [NEGATIVE PROMPT]: {negative_prompt}"
    )


def generate_use_case_prompt(use_case_name: str) -> str:
    """Return one of the predefined Darkside Pixel use-case prompts."""
    try:
        values = USE_CASES[use_case_name]
    except KeyError as exc:
        supported = ", ".join(sorted(USE_CASES))
        raise ValueError(f"Unsupported use case '{use_case_name}'. Supported: {supported}") from exc

    return generate_prompt(
        values["subject"],
        aesthetic_style=values["aesthetic_style"],
        lighting_and_color=values["lighting_and_color"],
        atmosphere=values["atmosphere"],
        negative_prompt=values["negative_prompt"],
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--subject", help="Subject to insert into the Darkside Pixel master template")
    parser.add_argument(
        "--use-case",
        choices=sorted(USE_CASES.keys()),
        help="Generate one of the predefined use-case prompts",
    )
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    if args.use_case:
        print(generate_use_case_prompt(args.use_case))
        return 0

    if args.subject:
        print(generate_prompt(args.subject))
        return 0

    parser.error("Provide either --subject or --use-case.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
