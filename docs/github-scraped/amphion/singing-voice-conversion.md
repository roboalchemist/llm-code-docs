# Singing Voice Conversion (SVC) in Amphion

## Overview

Amphion's Singing Voice Conversion (SVC) module enables the conversion of singing voice from one speaker or musical style to another. It supports multiple state-of-the-art architectures and has been the subject of peer-reviewed research published at IEEE SLT 2024.

## Architecture Overview

The SVC pipeline typically consists of three main components:

1. **Speaker-Agnostic Feature Extraction**: Extract content representations from source audio
2. **Speaker Embedding Injection**: Inject target speaker information
3. **Waveform Reconstruction**: Generate the output waveform using a vocoder

```
Source Audio → Content Features + Prosody → Acoustic Decoder → Vocoder → Target Audio
                                ↓
                          Speaker Embedding
```

## Content Feature Extraction

SVC uses speaker-agnostic representations from multiple pretrained models:

### Content Features

Extract linguistic content from audio using:

- **WeNet**: Automatic Speech Recognition (ASR) based features
  - Chinese and English support
  - Robust content representation
  - https://github.com/wenet-e2e/wenet

- **Whisper**: OpenAI's multilingual ASR model
  - Multi-language support
  - Robust to noise
  - Easy integration
  - https://github.com/openai/whisper

- **ContentVec**: Self-supervised content representation
  - Language-universal features
  - Pre-trained on multilingual data
  - https://github.com/auspicious3000/contentvec

### Prosody Features

Extract prosodic characteristics:

- **F0 (Fundamental Frequency)**: Pitch estimation
- **Energy**: Speech intensity and power

Configuration example:

```yaml
content_feature:
  type: whisper  # or weinet, contentvec
  use_frame_alignment: true

prosody:
  extract_f0: true
  extract_energy: true
```

## Speaker Embeddings

Represent target speaker characteristics:

### Speaker Look-Up Table

- Pre-computed embeddings for each speaker
- Fast inference
- Requires speaker ID at test time

### Reference Encoder (Developing)

- Extract speaker information from reference audio
- Enable zero-shot SVC
- No need for pre-computed embeddings

```python
# Using speaker embeddings
speaker_embedding = model.extract_speaker_embedding(reference_audio)
output = model.inference(source_audio, speaker_embedding)
```

## Acoustic Decoders

### Diffusion-Based Models

#### DiffWaveNetSVC

**Architecture**: Bidirectional Non-Causal Dilated CNN

**Key Features**:
- Diffusion probabilistic model framework
- Similar to WaveNet and DiffWave
- Multiple sampling algorithms support
- Deterministic inference possible

**Sampling Algorithms**:
- **DDPM** (Denoising Diffusion Probabilistic Models): Standard diffusion sampling
- **DDIM** (Denoising Diffusion Implicit Models): Faster inference
- **PNDM** (Pseudo Numerical Methods): Improved quality
- **Consistency Model**: Single-step fast inference

**Configuration**:
```yaml
acoustic_decoder:
  type: DiffWaveNetSVC
  num_layers: 20
  num_channels: 128

inference:
  sampler: ddim  # or ddpm, pndm, consistency
  steps: 50
```

#### DiffComoSVC

**Architecture**: Consistency Model based Diffusion

**Key Features**:
- Significantly faster inference than standard diffusion
- Single-step or multi-step sampling
- Maintains quality while reducing latency
- Based on consistency models

**Best For**: Real-time SVC applications

### Transformer-Based Models

#### TransformerSVC

**Architecture**: Encoder-only Non-autoregressive Transformer

**Key Features**:
- Pure attention mechanism
- Parallel decoding for fast inference
- Maintains long-range dependencies
- Simple and efficient

**Configuration**:
```yaml
acoustic_decoder:
  type: TransformerSVC
  hidden_size: 384
  num_layers: 6
  num_heads: 4
  feedforward_size: 1536
```

### VAE and Flow-Based Models

#### VitsSVC

**Architecture**: VITS-like Model with Content Features

**Key Features**:
- Variational autoencoder based
- Conditional generation
- Normalizing flow for flexible posterior
- Similar to so-vits-svc

**Paper**: https://arxiv.org/abs/2106.06103

## Waveform Synthesis (Vocoders)

After acoustic decoding, use a vocoder to generate the final waveform:

Available vocoders:
- **HiFi-GAN**: High-quality GAN-based
- **NSF-HiFiGAN**: Noise suppression enhanced
- **BigVGAN**: Large capacity GAN
- **MelGAN**: Lightweight GAN
- **WaveGlow**: Flow-based vocoder
- **Diffwave**: Diffusion-based vocoder

```yaml
vocoder:
  type: hifigan
  checkpoint: pretrained/vocoders/hifigan.pt
```

## SVC Workflow

### 1. Data Preparation

```bash
# Prepare SVC dataset
python bins/data/preprocess_dataset.py \
  --config config/svc/prepare_svcc.yaml \
  --datasets svcc

# For custom datasets:
# - Structure: speaker_id/song_name/audio.wav
# - Prepare annotations with content and prosody info
```

### 2. Feature Extraction

```bash
# Extract content features
python bins/data/extract_acoustic_features.py \
  --config config/svc/extract_whisper_feature.yaml \
  --data-dir /path/to/svc/data

# Extract prosody features
python bins/data/extract_prosody.py \
  --config config/svc/extract_prosody.yaml
```

### 3. Training

```bash
# Train SVC model
python bins/train.py \
  --config config/svc/DiffComoSVC/diffcomosvc.yaml \
  --exp-name my_svc_model

# Distributed training
python -m torch.distributed.launch \
  --nproc_per_node=8 \
  bins/train.py \
  --config config/svc/DiffComoSVC/diffcomosvc.yaml
```

### 4. Inference

```python
from amphion.models import build_model
from amphion.utils import load_config
import torch
import soundfile as sf

# Load model
config = load_config('config/svc/DiffComoSVC/diffcomosvc.yaml')
model = build_model(config)
checkpoint = torch.load('checkpoints/my_svc_model.pt')
model.load_state_dict(checkpoint['model'])
model.eval()

# Load audio
import librosa
source_audio, sr = librosa.load('source_song.wav')

# Convert voice
with torch.no_grad():
    output = model.inference(
        source_audio,
        target_speaker_id=1,
        use_fastest=False  # For DiffComoSVC
    )

# Save output
sf.write('output.wav', output.cpu().numpy(), sr)
```

## Supported Datasets

Amphion provides recipes for:

- **SVCC** (Singing Voice Conversion Challenge)
- **VCTK** (Voice Conversion Challenge)
- **M4Singer** (Chinese multi-singer dataset)
- **Opencpop** (Chinese singing dataset)
- **OpenSinger** (Multi-speaker singing)
- **Emilia**: Large-scale multilingual singing data

## Model Architecture Comparison

| Model | Type | Speed | Quality | Zero-Shot | Custom Reference |
|-------|------|-------|---------|-----------|------------------|
| DiffWaveNetSVC | Diffusion | Medium | High | No | No |
| DiffComoSVC | Consistency | Fast | High | No | No |
| TransformerSVC | Transformer | Fast | Medium | No | No |
| VitsSVC | VAE/Flow | Fast | High | No | No |

## Configuration Structure

```yaml
# Content and prosody features
acoustic_features:
  content_feature:
    type: whisper  # whisper, weinet, contentvec

  prosody:
    extract_f0: true
    extract_energy: true

# Acoustic decoder
acoustic_decoder:
  type: DiffComoSVC  # Model selection
  hidden_size: 256
  num_layers: 20

# Speaker embedding
speaker_embedding:
  type: lookup  # or reference_encoder
  num_speakers: 100
  embedding_dim: 256

# Vocoder
vocoder:
  type: hifigan
  checkpoint: pretrained/vocoders/hifigan.pt

# Training
train:
  batch_size: 16
  num_epochs: 100
  learning_rate: 1e-3
  optimizer: adamw

# Inference
inference:
  sampler: ddim  # For diffusion models
  sampler_steps: 50
```

## Advanced Features

### Multiple Content Features

Amphion investigates multiple content representations in the official paper:

```yaml
# Use multiple content features
acoustic_features:
  content_features:
    - whisper
    - contentvec
    - weinet
  fusion_method: concatenate  # or weighted
```

### Zero-Shot SVC (Reference Encoder)

Extract speaker info from reference audio at inference time:

```python
reference_audio, sr = librosa.load('reference_song.wav')
speaker_embedding = model.extract_speaker_embedding(reference_audio)

output = model.inference(
    source_audio,
    speaker_embedding=speaker_embedding
)
```

## Evaluation Metrics

Evaluate SVC models using:

- **MCD (Mel-Cepstral Distortion)**: Spectral similarity
- **FAD (Frechet Audio Distance)**: Audio distribution distance
- **PESQ**: Speech quality assessment
- **Similarity Score**: Via speaker verification models (RawNet3, WeSpeaker)
- **Intelligibility**: Via ASR (Whisper)

## Research Insights

From the Amphion SLC 2024 paper on multiple content features:

- **WeNet**: Best for content representation in singing
- **Whisper**: Good multilingual support
- **ContentVec**: Competitive performance

Combining multiple features can improve overall quality.

## Troubleshooting

### Poor Output Quality

1. Check content feature extraction:
   - Verify alignment between source and extracted features
   - Try different content models

2. Verify speaker embeddings:
   - Ensure adequate speaker data
   - Check speaker embedding dimensions

3. Adjust vocoder:
   - Use higher-quality vocoder
   - Fine-tune vocoder on target domain

### Artifacts and Noise

1. Increase training duration
2. Use gradient accumulation for larger effective batch size
3. Try different sampler (DDIM → PNDM)
4. Increase sampler steps

### Slow Inference

- Use DiffComoSVC for fast diffusion
- Use fewer sampler steps
- Reduce audio length
- Use GPU acceleration

## Resources

- **GitHub Recipe**: https://github.com/open-mmlab/Amphion/egs/svc/
- **Paper**: https://arxiv.org/abs/2310.11160
- **Demo**: https://www.zhangxueyao.com/data/MultipleContentsSVC/index.html
- **Community**: https://discord.com/invite/drhW7ajqAG
