# Theme: Cyberpunk Rainy Neon Cityscape

## Vision
A high-contrast, visually dense futuristic city environment at night during a heavy rainstorm. The scene features glowing neon signs, wet asphalt reflecting vibrant colors, and smooth motion of flying vehicles or high-tech cars.

## Core Elements
- **Visual Style:** High contrast, deep blues and purples, vibrant neon pinks and cyans. Cinematic lighting with realistic rain particles and surface reflections.
- **Motion Types:** 
  - Vertical falling rain (fast).
  - Horizontal movement of vehicles (medium speed).
  - Flickering/pulsing neon lights (stochastic).
  - Subtle camera movement (slow pan or zoom).
- **Emotional Tone:** Melancholic yet energetic, immersive, and high-tech.

## Prompt Engineering Strategy
Prompts will be structured to emphasize both static details and dynamic motion:
- **Template:** `A cinematic video of [Subject] in a [Setting], heavy rain, neon lights, cyberpunk aesthetic, [Motion Description], highly detailed, 4k, realistic reflections.`
- **Standard Benchmark Prompts:**
  1. `A cinematic video of a futuristic car driving through a neon-lit Tokyo street at night, heavy rain, reflections on wet asphalt, slow motion.`
  2. `Close-up of a neon "OPEN" sign flickering in a dark cyberpunk alleyway, raindrops hitting the sign, steam rising from the ground.`
  3. `A wide shot of a cyberpunk skyline with flying vehicles weaving through skyscrapers, heavy rainstorm, lightning in the distance, cinematic lighting.`
  4. `A cybernetic character standing under a bus stop in the rain, neon glow on their metallic skin, looking at a holographic advertisement.`
  5. `Raindrops splashing on a wet window overlooking a crowded futuristic city street, blurred neon lights in the background, melancholic atmosphere.`

## Impact on System Design
- **Temporal Consistency:** The rain and reflections will test the model's ability to maintain coherent motion across frames.
- **Semantic Alignment:** The specific cyberpunk elements (neon, holograms, futuristic vehicles) will be used to evaluate CLIP-SIM scores.
- **Evaluation:** Realism of rain and reflections will be a key metric in subjective user studies.
