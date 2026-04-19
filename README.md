# InstagramManager-agent

Handles instagram posts and curation.

## Darkside Pixel Prompt Template (2026)

This repository now includes a reusable prompt-engineering template that mirrors a dark atmospheric tech-noir/cyberpunk pixel-art aesthetic, plus a Python utility that dynamically inserts only the subject while automatically appending consistent style variables.

### Master Prompt Structure

```markdown
/imagine prompt:
[AESTHETIC STYLE]: Detailed 32-bit pixel art, high fidelity, isometric perspective, tech-noir, atmospheric.
[THE SUBJECT]: <INSERT YOUR SUBJECT HERE>
[LIGHTING & COLOR]: High contrast lighting, deep volumetric shadows, moody color palette dominated by obsidian blacks, electric blue and magenta neon, and subtle emerald green accents, specular highlights.
[ATMOSPHERE]: Melancholic, nocturnal, futuristic, dense fog, light rain, reflective surfaces, low-fi grit.
--no [NEGATIVE PROMPT]: Bright colors, daylight, sunlight, pastel, joyful, photorealistic, low fidelity, low quality, 3D render, cartoon.
```

### Included Use Cases

- Moody Cityscape (Cyberpunk-Noir)
- Character & Interior (Tech-Noir Solitude)
- Geometric Abstract (Pixel-Minimalism)

See `darkside_prompt_generator.py` for ready-to-use template presets.

## Dynamic Prompt Generation

Generate a prompt with a changing subject while preserving style identity:

```bash
python darkside_prompt_generator.py --subject "A lone figure standing on a rain-slicked balcony overlooking a cyberpunk Neo-Tokyo cityscape."
```

Use one of the built-in examples:

```bash
python darkside_prompt_generator.py --use-case moody_cityscape
```
