# Voice Conversion (VC) in Amphion

## Overview

Amphion's Voice Conversion module enables zero-shot and few-shot voice conversion with fine-grained control over speaker characteristics. It supports multiple advanced models designed for quality, naturalness, and flexibility.

## Voice Conversion Capabilities

Voice Conversion in Amphion can handle:

- **Voice Conversion (VC)**: Convert speaker identity while preserving content
- **Accent Conversion (AC)**: Change accent while maintaining speaker characteristics
- **Timbre Conversion**: Adjust voice timbre and color
- **Style Conversion**: Modify speaking/singing style

## Supported Voice Conversion Models

### 1. Vevo (VersatileVoice)

**Architecture**: Zero-shot voice imitation framework with controllable timbre and style

**Released**: December 2024

**Key Features**:
- **Zero-shot capabilities**: Convert any voice without fine-tuning
- **Controllable generation**: Independent control of timbre and style
- **Dual-branch design**:
  - **Vevo-Timbre**: Style-preserved voice conversion
  - **Vevo-Voice**: Style-converted voice conversion
- **Multi-task capability**:
  - Voice Conversion (VC)
  - Text-to-Speech (TTS)
  - Accent Conversion (AC)
  - Speech Enhancement

**Model Details**:
- Autoregressive Transformer + Flow-Matching Transformer
- Trained on Emilia dataset (101k+ hours)
- State-of-the-art zero-shot VC performance
- Pre-trained models available on HuggingFace

**Paper**: https://openreview.net/pdf?id=anQDiQZhDP

**Configuration Location**: `models/vc/vevo/`

#### Vevo Usage Example

```python
from amphion.models import build_model

# Load pre-trained Vevo model
model = build_model(config)
model.load_pretrained('amphion/vevo')

# Voice conversion with style preservation
output = model.inference(
    source_audio='input.wav',
    target_speaker_audio='reference.wav',
    mode='timbre'  # Preserve style
)

# Voice conversion with style transfer
output = model.inference(
    source_audio='input.wav',
    target_speaker_audio='reference.wav',
    mode='voice'   # Convert both timbre and style
)
```

#### Vevo1.5 (April 2025)

Enhanced version extending Vevo with:
- Unified speech and singing voice generation
- More robust generation
- Extended zero-shot capabilities
- Better accent conversion

**Blog**: https://veiled-army-9c5.notion.site/Vevo1-5-1d2ce17b49a280b5b444d3fa2300c93a

### 2. FACodec (Frequency Augmentative Codec)

**Architecture**: Neural audio codec with decomposition

**Key Features**:
- Decomposes speech into subspaces:
  - **Content**: Linguistic information
  - **Prosody**: Pitch and duration patterns
  - **Timbre**: Speaker-specific characteristics
- Zero-shot voice conversion
- Flexible audio manipulation
- Continuous representation

**Paper**: https://arxiv.org/abs/2403.03100

**Available Models**:
- NaturalSpeech3 FACodec
- Pre-trained checkpoint on HuggingFace

**Usage**:

```python
from amphion.models import build_model

# Load FACodec
model = build_model(config)
model.load_pretrained('amphion/naturalspeech3_facodec')

# Decompose speech
content, prosody, timbre = model.decompose(audio)

# Reconstruct with different timbre
output = model.reconstruct(content, prosody, target_timbre)
```

### 3. Noro (Noise-Robust Voice Conversion)

**Architecture**: Zero-shot voice conversion for noisy conditions

**Released**: 2024

**Key Features**:
- **Noise robustness**: Handles noisy reference speeches
- **Dual-branch reference encoding**:
  - Speech branch: Capture voice characteristics
  - Noise branch: Suppress noise information
- **Contrastive learning**: Noise-agnostic speaker loss
- Zero-shot capability
- Robust to various noise types

**Paper**: https://arxiv.org/abs/2411.19770

**Best For**: Real-world voice conversion with background noise

**Configuration Location**: `egs/vc/Noro/`

## Metis Foundation Model (February 2025)

**Purpose**: Unified speech generation foundation model

**Capabilities**:
- Zero-shot text-to-speech
- Voice conversion
- Target speaker extraction
- Speech enhancement
- Lip-to-speech

**Pre-trained Models**: Available on HuggingFace

**Paper**: https://arxiv.org/pdf/2502.03128

## VC Workflow

### 1. Voice Conversion Inference

Using Vevo for zero-shot VC:

```bash
# Command line inference
python bins/inference.py \
  --config config/vc/vevo/vevo.yaml \
  --checkpoint pretrained/vevo/vevo.pt \
  --input-audio source.wav \
  --reference-audio target_speaker.wav \
  --output-path output.wav
```

### 2. Python API

```python
from amphion.models import build_model
from amphion.utils import load_config
import librosa
import soundfile as sf

# Load model configuration
config = load_config('config/vc/vevo/vevo.yaml')
model = build_model(config)

# Load pre-trained weights
model.load_pretrained('amphion/vevo')
model.eval()

# Load audio files
source_audio, sr = librosa.load('source.wav', sr=16000)
reference_audio, _ = librosa.load('reference.wav', sr=16000)

# Perform voice conversion
with torch.no_grad():
    output = model.inference(
        source_audio=source_audio,
        target_speaker_audio=reference_audio,
        mode='timbre',  # or 'voice'
        pitch_scale=1.0,
        energy_scale=1.0
    )

# Save output
sf.write('output.wav', output.cpu().numpy(), sr)
```

## VC Applications

### 1. Voice Cloning

Clone a speaker's voice for new content:

```python
# Reference audio from target speaker
reference_audio, sr = librosa.load('speaker_voice.wav')

# Text to convert (via TTS first, or use existing speech)
source_speech, _ = librosa.load('source_speech.wav')

# Convert
output = model.voice_conversion(
    source_speech,
    reference_audio,
    mode='voice'
)
```

### 2. Accent Conversion

Modify accent while preserving speaker identity:

```python
# Reference audio with target accent
reference_audio, sr = librosa.load('target_accent.wav')

# Apply accent conversion
output = model.accent_conversion(
    source_speech,
    reference_audio
)
```

### 3. Timbre Adjustment

Modify voice characteristics:

```python
# Reference audio with desired timbre
reference_audio, sr = librosa.load('reference.wav')

# Apply timbre modification
output = model.timbre_conversion(
    source_speech,
    reference_audio,
    preservation_strength=0.7  # Balance between preservation and conversion
)
```

### 4. Real-World Applications

With Noro for robust VC:

```python
# Handle noisy reference audio
noisy_reference_audio, sr = librosa.load('noisy_reference.wav')

output = model.robust_voice_conversion(
    source_speech,
    noisy_reference_audio,
    noise_robustness=True
)
```

## Configuration Structure

```yaml
# Model architecture
model:
  type: Vevo  # or FACodec, Noro, Metis
  hidden_size: 256
  num_layers: 12

# Encoder configuration
encoder:
  type: transformer
  num_heads: 8

# Decoder configuration
decoder:
  type: transformer
  num_heads: 8

# Vocoder
vocoder:
  type: hifigan
  checkpoint: pretrained/vocoders/hifigan.pt

# Inference settings
inference:
  mode: timbre  # or voice
  pitch_scale: 1.0
  energy_scale: 1.0
  duration_scale: 1.0
```

## Audio Quality Control

Control output characteristics:

```python
output = model.inference(
    source_audio=source,
    target_speaker_audio=reference,

    # Voice quality parameters
    pitch_scale=1.0,        # Adjust pitch (0.5-2.0)
    energy_scale=1.0,       # Adjust loudness (0.5-2.0)
    duration_scale=1.0,     # Adjust speaking rate (0.5-2.0)

    # Conversion intensity
    conversion_strength=1.0,  # 0.0 = no change, 1.0 = full conversion
)
```

## Pre-trained Models

### Vevo
- HuggingFace: https://huggingface.co/amphion/Vevo
- ModelScope: https://modelscope.cn/models/amphion/Vevo
- All pre-trained on Emilia dataset

### FACodec
- HuggingFace: https://huggingface.co/amphion/naturalspeech3_facodec
- Pre-trained model checkpoint included

### Noro
- Available in repository
- Trained on multiple voice conversion datasets

### Metis
- HuggingFace: https://huggingface.co/amphion/metis
- Foundation model for unified speech generation

## Supported Datasets for Training

- **VCTK**: Multi-speaker English speech
- **TIMIT**: Phonetically balanced speech
- **VoxCeleb**: Speaker recognition dataset
- **Emilia**: Large-scale multilingual in-the-wild data
- **Custom datasets**: With proper preprocessing

## Performance Metrics

Evaluate voice conversion using:

- **MCD (Mel-Cepstral Distortion)**: Spectral similarity
- **FAD (Frechet Audio Distance)**: Perceptual quality
- **Speaker Similarity**: Via speaker verification models
  - RawNet3
  - WeSpeaker
  - WavLM
- **Content Preservation**: Via ASR (Whisper)
- **PESQ**: Voice quality metric

## Comparison with Baselines

| Model | Zero-Shot | Robustness | Speed | Quality |
|-------|-----------|-----------|-------|---------|
| Vevo | Yes | Medium | Fast | High |
| Vevo1.5 | Yes | High | Fast | Very High |
| FACodec | Yes | Medium | Fast | High |
| Noro | Yes | Very High | Medium | High |
| Metis | Yes | High | Medium | Very High |

## Advanced Features

### Multi-Reference Voice Cloning

Use multiple reference speakers:

```python
# Multiple references
references = [
    ('speaker1.wav', 0.3),
    ('speaker2.wav', 0.5),
    ('speaker3.wav', 0.2),
]

output = model.multi_reference_conversion(
    source_audio,
    references=references
)
```

### Fine-tuning for Custom Voices

```bash
python bins/train.py \
  --config config/vc/vevo/vevo_finetune.yaml \
  --pretrained-model-name amphion/vevo \
  --custom-speaker-data path/to/speaker/data
```

### Streaming/Online Voice Conversion

For real-time applications:

```python
model.set_inference_mode('streaming')
output = model.streaming_inference(
    audio_stream,  # Streaming audio input
    reference_audio,
    chunk_length=8000  # Process in chunks
)
```

## Troubleshooting

### Voice Quality Issues

1. **Artifacts**: Use higher-quality reference audio
2. **Unnatural pitch**: Adjust pitch_scale parameter
3. **Poor timbre**: Try different reference speakers
4. **Noisy output**: Increase reference audio quality or use Noro

### Inference Speed

- Use GPU acceleration
- Reduce audio length
- Use VQ-based models for faster inference

### Memory Issues

```python
# Enable gradient checkpointing if training
model.enable_gradient_checkpointing()

# Reduce batch size for inference
model.set_batch_size(1)
```

## Resources

- **GitHub VC Module**: https://github.com/open-mmlab/Amphion/tree/main/models/vc
- **Vevo Paper**: https://openreview.net/pdf?id=anQDiQZhDP
- **FACodec Paper**: https://arxiv.org/abs/2403.03100
- **Noro Paper**: https://arxiv.org/abs/2411.19770
- **Metis Paper**: https://arxiv.org/pdf/2502.03128
- **Demo**: https://versavoice.github.io/
- **Community**: https://discord.com/invite/drhW7ajqAG
