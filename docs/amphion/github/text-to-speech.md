# Text-to-Speech (TTS) in Amphion

## Overview

Amphion's Text-to-Speech (TTS) module provides state-of-the-art text-to-speech capabilities with multiple supported architectures. The TTS system converts natural language text into high-quality synthesized speech with controllable prosody and speaker characteristics.

## Supported TTS Models

### 1. FastSpeech2

**Architecture**: Non-autoregressive Transformer-based

**Key Features**:
- Feed-forward Transformer blocks
- Faster inference than autoregressive models
- Supports multiple speakers
- Duration prediction for prosody control
- Pitch and energy prediction

**Best For**: Real-time TTS applications, multi-speaker synthesis

**Configuration Location**: `config/tts/FastSpeech2/`

### 2. VITS (Variational Inference with adversarial Learning for end-to-end Text-to-Speech)

**Architecture**: End-to-end with Conditional VAE and Adversarial Learning

**Key Features**:
- Conditional variational autoencoder
- Adversarial training with discriminator
- Integrated vocoder for waveform generation
- Excellent voice quality
- Supports multiple speakers

**Best For**: High-quality speech synthesis, end-to-end training

**Paper**: https://arxiv.org/abs/2106.06103

**Configuration Location**: `config/tts/VITS/`

### 3. VALL-E (Voice Across Languages Language Encoding)

**Architecture**: Neural Codec Language Model with Discrete Codes

**Key Features**:
- Zero-shot TTS capabilities
- Uses discrete audio tokens
- Few-shot voice adaptation
- Multilingual support
- Large-scale pre-training

**Best For**: Zero-shot voice cloning, multilingual synthesis

**Paper**: https://arxiv.org/abs/2301.02111

**Configuration Location**: `config/tts/VALLE/`

### 4. NaturalSpeech2

**Architecture**: Latent Diffusion Model

**Key Features**:
- Diffusion-based generation
- Natural prosody modeling
- Improved speech quality
- Controllable generation
- Superior naturalness

**Best For**: Natural-sounding speech, research and development

**Paper**: https://arxiv.org/abs/2304.09116

**Configuration Location**: `config/tts/NaturalSpeech2/`

### 5. Jets (Joint End-to-end Text-to-Speech)

**Architecture**: Joint Training of FastSpeech2 and HiFi-GAN

**Key Features**:
- Joint optimization of acoustic model and vocoder
- Alignment module for duration prediction
- End-to-end training
- Improved consistency between stages

**Best For**: Unified acoustic and vocoder training

**Configuration Location**: `config/tts/Jets/`

### 6. MaskGCT (Masked Generator-Conditioner-Target)

**Architecture**: Fully Non-autoregressive Architecture

**Key Features**:
- Eliminates explicit text-speech alignment requirements
- Fully non-autoregressive generation
- State-of-the-art performance
- Zero-shot capabilities
- Fast inference

**Best For**: Fast, alignment-free TTS, zero-shot synthesis

**Paper**: https://arxiv.org/abs/2409.00750

**Availability**: Pre-trained models on HuggingFace and ModelScope

### 7. Vevo-TTS

**Architecture**: Autoregressive + Flow-Matching Transformer

**Key Features**:
- Zero-shot TTS with controllable timbre and style
- Flexible voice control
- Speech and singing voice synthesis
- Multiple voice aspects controllable
- Style transfer capabilities

**Best For**: Controllable zero-shot TTS, voice cloning with style control

**Paper**: https://openreview.net/pdf?id=anQDiQZhDP

**Configuration Location**: `models/vc/vevo/`

## Common TTS Workflow

### 1. Data Preparation

```bash
# Prepare your dataset
cd Amphion
python bins/data/preprocess_dataset.py \
  --config config/tts/VITS/prepare_libritts.yaml \
  --datasets libritts

# For custom datasets, modify the configuration file to point to your data
```

### 2. Training

```bash
# Train a TTS model
python bins/train.py \
  --config config/tts/VITS/vits.yaml \
  --exp-name my_tts_model

# Resume from checkpoint
python bins/train.py \
  --config config/tts/VITS/vits.yaml \
  --exp-name my_tts_model \
  --resume
```

### 3. Inference

```python
from amphion.models import build_model
from amphion.utils import load_config
import torch

# Load model
config = load_config('config/tts/VITS/vits.yaml')
model = build_model(config)
checkpoint = torch.load('path/to/checkpoint.pt')
model.load_state_dict(checkpoint['model'])
model.eval()

# Generate speech
with torch.no_grad():
    text = "Hello, this is a test."
    output = model.inference(text)
```

### 4. Evaluation

```bash
# Evaluate TTS model
python bins/metrics/eval.py \
  --config config/tts/VITS/vits.yaml \
  --checkpoint path/to/checkpoint.pt
```

## Configuration Structure

TTS configurations follow this general structure:

```yaml
# Model architecture
model:
  type: VITS  # or FastSpeech2, VALL-E, etc.
  hidden_size: 384
  encoder_hidden_size: 384
  # ... model-specific parameters

# Data configuration
data:
  dataset: libritts
  data_dir: /path/to/data
  batch_size: 16
  num_workers: 4

# Training configuration
train:
  max_epochs: 100
  learning_rate: 1e-3
  optimizer: adam
  grad_clip: 5.0

# Inference configuration
inference:
  speaker_id: 0  # For multi-speaker models
  duration_scale: 1.0
  pitch_scale: 1.0
```

## Multi-Speaker TTS

For models supporting multiple speakers:

```python
# Specify speaker ID during inference
output = model.inference(
    text="Hello world",
    speaker_id=1
)

# Or use speaker embedding
speaker_embedding = model.get_speaker_embedding(speaker_id=1)
output = model.inference(text="Hello world", speaker_embedding=speaker_embedding)
```

## Supported Datasets

Amphion supports preprocessing for these TTS datasets:

- **LibriTTS**: Large-scale multi-speaker English speech
- **LJSpeech**: Single-speaker English speech
- **VCTK**: Multi-speaker English speech
- **OpenSinger**: Chinese singing voice
- **M4Singer**: Chinese multi-speaker singing
- **Emilia**: Multilingual in-the-wild speech (101k+ hours)

## Voice Characteristics Control

Different TTS models offer various levels of control:

### Duration Control (FastSpeech2, VITS)

```python
# Speed up or slow down speech
output = model.inference(
    text="Hello world",
    duration_scale=0.8  # 20% faster
)
```

### Pitch Control

```python
# Modify fundamental frequency
output = model.inference(
    text="Hello world",
    pitch_scale=1.2  # Higher pitch
)
```

### Energy Control

```python
# Adjust speaking energy/intensity
output = model.inference(
    text="Hello world",
    energy_scale=0.9
)
```

## Vocoder Integration

Most TTS models require a vocoder to convert acoustic features to waveform:

```bash
# Train with HiFi-GAN vocoder
python bins/train.py \
  --config config/tts/VITS/vits_hifigan.yaml
```

Available vocoders:
- HiFi-GAN (default)
- BigVGAN
- NSF-HiFiGAN
- MelGAN
- WaveGlow

## Pre-trained Models

Access pre-trained models from:

- **HuggingFace**: https://huggingface.co/amphion
  - MaskGCT, Vevo, and others

- **ModelScope**: https://modelscope.cn/organization/amphion
  - MaskGCT, Metis, and others

- **Local**: Provided in `pretrained/` directory

### Using Pre-trained Models

```python
from amphion.models import build_model

# Load pre-trained VALL-E
model = build_model(config)
model.load_pretrained('amphion/vall-e')

# Inference
output = model.inference("Your text here")
```

## TTS Demo Samples

Listen to TTS samples from Amphion models:
https://openhlt.github.io/Amphion_TTS_Demo/

## Performance Metrics

TTS quality is evaluated using:

- **MOS (Mean Opinion Score)**: Subjective speech quality (scale 1-5)
- **PESQ (Perceptual Evaluation of Speech Quality)**: Objective speech quality
- **FAD (Frechet Audio Distance)**: Distribution distance metric
- **WER (Word Error Rate)**: Via ASR (Whisper)
- **Speaker Similarity**: Via speaker verification models

## Troubleshooting

### Out-of-Memory Errors

```yaml
# Reduce batch size
train:
  batch_size: 8  # Decrease from default

# Enable gradient accumulation
gradient_accumulation_steps: 2

# Enable gradient checkpointing
model:
  use_checkpoint: true
```

### Poor Voice Quality

- Ensure high-quality training data
- Increase training duration
- Adjust learning rate schedule
- Try different vocoder

### Alignment Issues (for models needing alignment)

- Use Montreal Forced Aligner (MFA) for better alignment
- Adjust forced alignment configuration
- Check data quality

## Advanced Topics

### Fine-tuning Pre-trained Models

```bash
python bins/train.py \
  --config config/tts/VITS/vits.yaml \
  --exp-name fine_tune \
  --pretrained-model-name amphion/vits-libritts \
  --resume
```

### Knowledge Distillation

Train a student model from a teacher:

```yaml
distillation:
  enabled: true
  teacher_model: vits
  temperature: 5.0
  alpha: 0.5
```

### Data Augmentation

```yaml
data_augmentation:
  speed_perturb: [0.95, 1.05]
  pitch_shift: [-2, 2]
  energy_scale: [0.9, 1.1]
```

## Resources

- **Official Docs**: https://amphion.dev
- **GitHub Repo**: https://github.com/open-mmlab/Amphion
- **Paper**: https://arxiv.org/abs/2312.09911
- **Community**: https://discord.com/invite/drhW7ajqAG
