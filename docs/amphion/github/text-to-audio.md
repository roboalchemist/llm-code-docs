# Text-to-Audio (TTA) in Amphion

## Overview

Amphion's Text-to-Audio (TTA) module enables generation of diverse audio content from natural language descriptions. It uses a latent diffusion model architecture similar to AudioLDM, Make-an-Audio, and AUDIT.

## Architecture Overview

The TTA system uses a two-stage approach:

### Stage 1: Latent Space Learning

Train an autoencoder to compress audio into a latent space:

```
Raw Audio → Encoder → Latent Codes → Decoder → Reconstructed Audio
                      (Compressed)
```

**Component**: `AutoencoderKL` in Amphion
- Variational autoencoder with KL divergence
- Compresses audio by ~4x
- Learns meaningful latent representations

### Stage 2: Conditional Diffusion in Latent Space

Train a diffusion model to generate latent codes conditioned on text:

```
Text Description → Text Encoder → CLIP/CLAP embeddings
                                    ↓
                            Diffusion Model
                                    ↓
              Latent Codes → Decoder → Generated Audio
```

**Component**: `AudioLDM` in Amphion
- Conditional latent diffusion model
- Text-conditioned generation
- Multiple sampling strategies

## TTA Capabilities

### Diverse Audio Generation

Generate different types of audio from descriptions:

- **Sound Effects**: Thunder, water splash, door knock
- **Music**: Ambient, electronic, acoustic styles
- **Environmental Audio**: Forest, traffic, rain sounds
- **Speech**: Various prosody and emotion
- **Hybrid Content**: Mixed audio scenarios

### Control and Conditioning

Fine-grained control over generation:

- **Text Prompts**: Descriptive text for generation
- **Negative Prompts**: Specify unwanted characteristics
- **Duration Control**: Control output length
- **Style Control**: Specify audio style/genre
- **Intensity Control**: Adjust generation strength

## TTA Workflow

### 1. Model Architecture Setup

Configure the two-stage model:

```yaml
# Stage 1: VAE (AutoencoderKL)
autoencoder_kl:
  type: AutoencoderKL
  in_channels: 1
  out_channels: 1
  latent_channels: 8
  hidden_channels: 128

# Stage 2: Diffusion Model
diffusion_model:
  type: AudioLDM
  latent_channels: 8
  text_encoder: t5  # or clap, clip
  num_steps: 1000  # Diffusion steps
```

### 2. Data Preparation

Prepare audio-text pairs:

```bash
# Directory structure
dataset/
├── audio/
│   ├── sound_001.wav
│   ├── sound_002.wav
│   └── ...
└── text_descriptions/
    ├── sound_001.txt
    ├── sound_002.txt
    └── ...

# Each text file contains description of corresponding audio
```

Preprocess audio:

```bash
python bins/data/preprocess_tta.py \
  --audio-dir path/to/audio \
  --text-dir path/to/descriptions \
  --output-dir processed_data
```

### 3. Stage 1: Train AutoencoderKL

First, train the VAE to learn latent representation:

```bash
python bins/train.py \
  --config config/tta/autoencoderkl.yaml \
  --exp-name tta_vae
```

Configuration:

```yaml
model:
  type: AutoencoderKL
  # ... architecture parameters

data:
  dataset: audio_descriptions
  batch_size: 32
  num_workers: 4

train:
  max_epochs: 50
  learning_rate: 1e-3
  loss_type: mse  # Reconstruction loss
```

### 4. Stage 2: Train AudioLDM

After VAE training, train the diffusion model:

```bash
python bins/train.py \
  --config config/tta/audioldm.yaml \
  --exp-name tta_diffusion
```

Configuration:

```yaml
model:
  type: AudioLDM
  # ... architecture parameters
  pretrained_vae: path/to/vae_checkpoint.pt  # From stage 1

# Text encoder for conditioning
text_encoder:
  type: t5  # or clap, clip
  model_name: t5-base
  freeze_encoder: false

data:
  batch_size: 16

train:
  max_epochs: 100
  learning_rate: 5e-5
  # Diffusion training specifics
```

### 5. Inference

Generate audio from text descriptions:

```python
from amphion.models import build_model
from amphion.utils import load_config
import torch
import torchaudio

# Load models
config = load_config('config/tta/audioldm.yaml')
vae = build_model(config.vae_config)
diffusion_model = build_model(config.diffusion_config)

# Load checkpoints
vae.load_state_dict(torch.load('checkpoints/vae.pt'))
diffusion_model.load_state_dict(torch.load('checkpoints/diffusion.pt'))

vae.eval()
diffusion_model.eval()

# Generate audio
text_prompt = "A dog barking in the distance with ambient traffic noise"

with torch.no_grad():
    # Text encoding
    text_embeddings = diffusion_model.encode_text(text_prompt)

    # Diffusion sampling in latent space
    latent_codes = diffusion_model.sample(
        embeddings=text_embeddings,
        num_steps=50,
        guidance_scale=7.5
    )

    # Decode to audio
    audio = vae.decode(latent_codes)

# Save generated audio
torchaudio.save('output.wav', audio.squeeze(0), 16000)
```

### 6. Advanced Inference Options

#### Negative Prompts

Specify what NOT to generate:

```python
output = diffusion_model.sample(
    prompt="Dog barking",
    negative_prompt="cat, bird, quiet",
    guidance_scale=7.5
)
```

#### Classifier-Free Guidance

Control generation strength:

```python
output = diffusion_model.sample(
    prompt="Thunder storm with heavy rain",
    guidance_scale=10.0  # Higher = stronger adherence to prompt
)
```

#### Sampling Methods

Different diffusion samplers:

```python
# DDPM (standard)
output = diffusion_model.sample(sampler='ddpm', num_steps=1000)

# DDIM (faster)
output = diffusion_model.sample(sampler='ddim', num_steps=50)

# PNDM (quality + speed balance)
output = diffusion_model.sample(sampler='pndm', num_steps=50)

# Euler
output = diffusion_model.sample(sampler='euler', num_steps=30)
```

#### Seed Control

Reproducible generation:

```python
torch.manual_seed(42)
output1 = diffusion_model.sample(prompt="dog barking")

torch.manual_seed(42)
output2 = diffusion_model.sample(prompt="dog barking")
# output1 and output2 are identical
```

## Text Encoders

TTA can use different text encoders:

### T5 (Text-to-Text Transfer Transformer)

```python
text_encoder = T5Tokenizer.from_pretrained('t5-base')
embeddings = text_encoder('A dog barking')
# Shape: [1, seq_length, 768]
```

### CLAP (Contrastive Language-Audio Pre-training)

```python
# CLAP embeddings are audio-aligned
text_encoder = CLAPTextEncoder()
embeddings = text_encoder('A dog barking')
# Shape: [1, 512] - audio-aligned representations
```

### CLIP (Vision-Language Model)

Alternative multi-modal conditioning

## Supported Datasets

Amphion supports TTA training on:

- **AudioCaps**: 49k audio clips with captions
- **Clotho**: 5k audio samples with multiple descriptions
- **Emilia**: Large-scale speech descriptions
- **Custom Datasets**: With proper annotation format

Dataset structure:

```yaml
dataset:
  name: audiocaps
  root_dir: /path/to/audiocaps
  split: train  # or val, test

  # Preprocessing
  preprocessing:
    sample_rate: 16000
    num_mels: 64
    n_fft: 400
    hop_length: 160
```

## Configuration Structure

Complete TTA configuration:

```yaml
# Stage 1: VAE Configuration
vae_config:
  model:
    type: AutoencoderKL
    in_channels: 1
    latent_channels: 8
    hidden_channels: 128
    num_res_blocks: 2

  train:
    learning_rate: 1e-3
    batch_size: 32
    max_epochs: 50

# Stage 2: Diffusion Configuration
diffusion_config:
  model:
    type: AudioLDM
    latent_channels: 8
    hidden_channels: 512
    num_layers: 24
    attention_heads: 8

  text_encoder:
    type: t5  # or clap
    freeze: false

  diffusion:
    beta_schedule: linear
    num_steps: 1000

  train:
    learning_rate: 5e-5
    batch_size: 16
    max_epochs: 100
    warmup_steps: 5000

# Data configuration
data:
  dataset: audiocaps
  sample_rate: 16000
  num_mels: 64

# Inference configuration
inference:
  sampler: ddim
  num_steps: 50
  guidance_scale: 7.5
```

## Performance Metrics

Evaluate TTA quality using:

- **FAD (Frechet Audio Distance)**: Audio distribution similarity
- **KL Divergence**: Distribution divergence metric
- **PESQ**: Perceived speech quality (for speech-like audio)
- **Inception Score**: Diversity and quality metric
- **Text Alignment Score**: How well generated audio matches text

## Troubleshooting

### Poor Audio Quality

1. **Increase training**: More epochs, larger dataset
2. **Improve text descriptions**: More detailed, specific prompts
3. **Adjust guidance scale**: Higher values (7.5-15.0)
4. **Try different sampler**: PNDM often better than DDIM

### Mode Collapse (Repetitive Outputs)

1. Increase diversity regularization
2. Use higher temperature in sampling
3. Augment training data with more diverse examples

### Slow Inference

1. Use fewer diffusion steps (DDIM with 30-50 steps)
2. Use GPU acceleration
3. Reduce audio quality (lower sample rate)

### Training Instability

1. Lower learning rate
2. Smaller batch size
3. Gradient clipping
4. Warm-up scheduler

## Advanced Topics

### Fine-tuning Pre-trained Models

```bash
python bins/train.py \
  --config config/tta/audioldm_finetune.yaml \
  --pretrained-diffusion pretrained/audioldm.pt \
  --custom-data path/to/custom/data
```

### Conditioning on Audio Features

Additional conditioning beyond text:

```python
# Condition on audio duration
output = diffusion_model.sample(
    prompt="dog barking",
    duration=3.0  # 3 seconds
)

# Condition on loudness
output = diffusion_model.sample(
    prompt="dog barking",
    loudness_db=-10  # Target loudness
)
```

### Audio Style Transfer

Transfer audio style while maintaining content:

```python
# Reference audio for style
style_audio, sr = librosa.load('reference.wav')
style_embeddings = diffusion_model.extract_style(style_audio)

# Generate with style
output = diffusion_model.sample(
    prompt="dog barking",
    style_embeddings=style_embeddings
)
```

## Research Background

TTA in Amphion is based on:

- **AudioLDM**: Latent diffusion for audio generation (2301.12503)
- **Make-an-Audio**: Large-scale audio generation (2301.12661)
- **AUDIT**: Audio understanding through diffusion (2304.00830)

These models showed that latent diffusion is highly effective for audio synthesis.

## Resources

- **GitHub Recipe**: https://github.com/open-mmlab/Amphion/egs/tta/
- **Beginner Recipe**: https://github.com/open-mmlab/Amphion/egs/tta/RECIPE.md
- **Amphion Paper**: https://arxiv.org/abs/2304.00830
- **AudioLDM Paper**: https://arxiv.org/abs/2301.12503
- **Community**: https://discord.com/invite/drhW7ajqAG
