# Evaluation Metrics and Vocoders in Amphion

## Overview

Amphion provides comprehensive objective evaluation capabilities and multiple state-of-the-art neural vocoders for audio synthesis tasks.

## Evaluation Metrics

Amphion implements a complete set of evaluation metrics for assessing audio generation quality across multiple dimensions:

### F0 Modeling Metrics

Evaluate pitch/fundamental frequency accuracy:

- **F0 Pearson Coefficient**: Correlation between predicted and ground truth F0
  - Range: -1.0 to 1.0
  - Higher is better
  - Measures pitch contour tracking

- **F0 Periodicity RMSE**: Root Mean Square Error for voiced/unvoiced detection
  - Measures periodicity accuracy
  - Lower is better

- **F0 RMSE**: Root Mean Square Error for pitch value prediction
  - Measures absolute pitch accuracy
  - Lower is better

- **Voiced/Unvoiced F1 Score**: Binary classification accuracy
  - Measures ability to detect voiced vs unvoiced segments
  - Range: 0-1, higher is better

```python
from amphion.evaluation import F0Metrics

f0_metrics = F0Metrics()

# Compute metrics
pearson_coef = f0_metrics.pearson_coefficient(pred_f0, gt_f0)
voicing_f1 = f0_metrics.voicing_f1(pred_voicing, gt_voicing)
rmse = f0_metrics.f0_rmse(pred_f0, gt_f0)
```

### Energy Modeling Metrics

Evaluate energy/amplitude accuracy:

- **Energy RMSE**: Root Mean Square Error for energy prediction
  - Lower is better
  - Measures amplitude accuracy

- **Energy Pearson Coefficient**: Correlation with ground truth energy
  - Range: -1.0 to 1.0
  - Higher is better

```python
from amphion.evaluation import EnergyMetrics

energy_metrics = EnergyMetrics()

rmse = energy_metrics.energy_rmse(pred_energy, gt_energy)
pearson = energy_metrics.pearson_coefficient(pred_energy, gt_energy)
```

### Intelligibility Metrics

Measure content preservation and clarity:

- **Character Error Rate (CER)**: Character-level WER
  - Requires ASR model (Whisper)
  - Lower is better (0% = perfect)

- **Word Error Rate (WER)**: Word-level error rate
  - Requires ASR model (Whisper)
  - Lower is better (0% = perfect)

```python
from amphion.evaluation import IntelligibilityMetrics
from amphion.models import WhisperExtractor

intelligibility = IntelligibilityMetrics(
    asr_model=WhisperExtractor('base')
)

wer = intelligibility.word_error_rate(audio, reference_text)
cer = intelligibility.character_error_rate(audio, reference_text)
```

### Spectrogram Distortion Metrics

Measure audio quality and similarity:

#### Frechet Audio Distance (FAD)

- **Purpose**: Perceptual audio quality metric
- **Range**: 0 to infinity (lower is better)
- **Based on**: VGGish audio feature embeddings
- **Interpretation**: Distance between distributions

```python
from amphion.evaluation import FADMetrics

fad_metrics = FADMetrics()

# Compute FAD
fad = fad_metrics.compute(generated_audio, reference_audio)
# Typical good value: < 3.0
```

#### Mel-Cepstral Distortion (MCD)

- **Purpose**: Spectral similarity measure
- **Range**: 0 to infinity (lower is better)
- **Best For**: Voice conversion, TTS
- **Unit**: dB

```python
from amphion.evaluation import MCDMetrics

mcd_metrics = MCDMetrics()

# Compute MCD
mcd = mcd_metrics.compute(predicted, reference)
# Typical good value: < 5.0 dB
```

#### Multi-Resolution STFT Distance (MSTFT)

- **Purpose**: Multi-scale spectral comparison
- **Uses**: Multiple window sizes and FFT lengths
- **Range**: 0 to infinity (lower is better)

```python
from amphion.evaluation import MSTFTMetrics

mstft_metrics = MSTFTMetrics()

mag_loss, phase_loss = mstft_metrics.compute(predicted, reference)
```

#### PESQ (Perceptual Evaluation of Speech Quality)

- **Purpose**: Subjective speech quality prediction
- **Range**: -0.5 to 4.5 (higher is better)
- **Best For**: Speech synthesis quality
- **Correlation**: High correlation with MOS

```python
from amphion.evaluation import PESQMetrics

pesq_metrics = PESQMetrics()

score = pesq_metrics.compute(reference, generated)
# Typical good value: > 3.0
```

#### STOI (Short Time Objective Intelligibility)

- **Purpose**: Speech intelligibility metric
- **Range**: 0 to 1 (higher is better)
- **Based on**: SNR estimates in bark bands

```python
from amphion.evaluation import STOIMetrics

stoi_metrics = STOIMetrics()

score = stoi_metrics.compute(reference, generated)
# Typical good value: > 0.8
```

### Speaker Similarity Metrics

Measure speaker identity preservation:

Supported speaker verification models:
- **RawNet3**: End-to-end speaker recognition
- **Resemblyzer**: Simple speaker embedding
- **WeSpeaker**: WeNet speaker embedding
- **WavLM**: Large multilingual model

```python
from amphion.evaluation import SpeakerSimilarityMetrics
from amphion.models import RawNet3

speaker_metrics = SpeakerSimilarityMetrics(
    extractor=RawNet3()
)

# Cosine similarity
similarity = speaker_metrics.cosine_similarity(audio1, audio2)
# Range: -1 to 1 (higher = more similar speaker)
```

## Evaluation Workflow

### Complete Evaluation Script

```python
from amphion.evaluation import (
    FADMetrics, MCDMetrics, PESQMetrics,
    SpeakerSimilarityMetrics, IntelligibilityMetrics
)
import numpy as np

# Initialize metrics
fad = FADMetrics()
mcd = MCDMetrics()
pesq = PESQMetrics()
speaker_sim = SpeakerSimilarityMetrics()
intelligibility = IntelligibilityMetrics()

# Load generated and reference audio
generated_audio = load_audio('generated.wav')
reference_audio = load_audio('reference.wav')

# Compute all metrics
results = {
    'fad': fad.compute(generated_audio, reference_audio),
    'mcd': mcd.compute(generated_audio, reference_audio),
    'pesq': pesq.compute(reference_audio, generated_audio),
    'speaker_sim': speaker_sim.cosine_similarity(
        generated_audio, reference_audio
    ),
}

# Print results
for metric, value in results.items():
    print(f"{metric}: {value:.4f}")
```

### Batch Evaluation

```bash
python bins/metrics/eval.py \
  --config config/tts/VITS/vits.yaml \
  --checkpoint checkpoints/vits.pt \
  --test-dir path/to/test/data \
  --output-csv results.csv
```

Configuration for batch evaluation:

```yaml
evaluation:
  metrics:
    - fad
    - mcd
    - pesq
    - speaker_similarity
    - intelligibility

  fad:
    model: vggish

  pesq:
    sample_rate: 16000

  speaker_similarity:
    extractor: rawnet3

  intelligibility:
    asr_model: whisper-base
```

## Neural Vocoders

Vocoders convert acoustic features (mel-spectrograms) to waveforms. Amphion supports multiple vocoder architectures.

### GAN-Based Vocoders

#### HiFi-GAN

**Paper**: https://arxiv.org/abs/2010.05646

**Key Features**:
- High-quality audio generation
- Fast inference
- Lightweight architecture
- Multi-scale discriminators

**Configuration**:
```yaml
vocoder:
  type: hifigan
  pretrained: true
  checkpoint: pretrained/vocoders/hifigan.pt
```

**Performance**:
- MOS: ~3.8-4.0
- Inference speed: Real-time (>10x)
- Model size: ~3.6M parameters

#### NSF-HiFiGAN

**Enhancement**: NSF (Neural Source Filter) + HiFi-GAN

**Key Features**:
- Improved pitch accuracy
- Better F0 modeling
- Faster convergence

```yaml
vocoder:
  type: nsf_hifigan
  f0_quantizer: linear
```

#### BigVGAN

**Paper**: https://arxiv.org/abs/2206.04658

**Key Features**:
- Larger capacity model
- Superior audio quality
- Better generalization
- Improved high-frequency content

```yaml
vocoder:
  type: bigvgan
  pretrained: true
```

#### APNet

**Paper**: https://arxiv.org/abs/2305.07952

**Key Features**:
- Adaptive parallel architecture
- Efficient design
- High-quality output

```yaml
vocoder:
  type: apnet
```

#### MelGAN

**Lightweight option for fast inference**

**Key Features**:
- Small model size
- Fast inference
- Mobile-friendly

```yaml
vocoder:
  type: melgan
```

### Flow-Based Vocoders

#### WaveGlow

**Paper**: https://arxiv.org/abs/1811.00002

**Key Features**:
- Normalizing flow model
- Parallel generation
- Invertible transformation

**Configuration**:
```yaml
vocoder:
  type: waveglow
  n_flows: 12
  n_group: 8
```

### Diffusion-Based Vocoders

#### Diffwave

**Paper**: https://arxiv.org/abs/2009.09761

**Key Features**:
- Diffusion-based generation
- High-quality audio
- Slower inference

**Configuration**:
```yaml
vocoder:
  type: diffwave
  num_steps: 50
  sampler: ddim
```

### Auto-Regressive Vocoders

#### WaveNet

**Paper**: https://arxiv.org/abs/1609.03499

**Key Features**:
- Dilated convolutions
- Causal generation
- High quality but slow

#### WaveRNN

**Paper**: https://arxiv.org/abs/1802.08435

**Key Features**:
- Efficient RNN-based
- Faster than WaveNet
- Still slower than GAN-based

## Vocoder Training

### Training a Custom Vocoder

```bash
python bins/train.py \
  --config config/vocoder/hifigan/train.yaml \
  --exp-name my_vocoder
```

Configuration:

```yaml
model:
  type: HiFiGAN
  generator:
    channels: 512
    upsample_scales: [8, 8, 2, 2]
    upsample_kernel_sizes: [16, 16, 4, 4]

  discriminator:
    scales: 3
    periods: [2, 3, 5, 7, 11]

data:
  dataset: libritts
  sample_rate: 16000
  batch_size: 32

train:
  learning_rate_g: 0.0002
  learning_rate_d: 0.0002
  betas: [0.5, 0.9]
  max_epochs: 100
```

### Vocoder Evaluation

```python
from amphion.models import build_vocoder
from amphion.evaluation import PESQMetrics

# Load vocoder
vocoder = build_vocoder('hifigan')

# Convert mel-spectrogram to audio
mel_spec = load_mel_spectrogram('test.pt')
audio = vocoder(mel_spec)

# Evaluate
pesq_metrics = PESQMetrics()
score = pesq_metrics.compute(reference_audio, audio)
```

## Vocoder Selection Guide

| Vocoder | Quality | Speed | Size | Best For |
|---------|---------|-------|------|----------|
| HiFi-GAN | High | Very Fast | Small | General purpose |
| NSF-HiFiGAN | High | Very Fast | Small | Pitch-critical tasks |
| BigVGAN | Very High | Fast | Medium | High-quality output |
| APNet | High | Very Fast | Small | Efficient systems |
| MelGAN | Medium | Very Fast | Tiny | Mobile/edge |
| WaveGlow | High | Medium | Large | Parallel generation |
| Diffwave | Very High | Slow | Medium | Offline generation |
| WaveNet | Very High | Slow | Large | Research |

## Advanced Evaluation

### Custom Metrics

Implement custom metrics:

```python
from amphion.evaluation import AudioMetric

class CustomMetric(AudioMetric):
    def __init__(self):
        super().__init__()

    def compute(self, predicted, reference):
        # Your metric implementation
        return metric_value

# Use custom metric
custom = CustomMetric()
value = custom.compute(generated_audio, reference_audio)
```

### Listening Tests Integration

Amphion can organize audio samples for listening tests:

```python
from amphion.evaluation import ListeningTestOrganizer

organizer = ListeningTestOrganizer(
    models=['model1', 'model2', 'model3'],
    reference_audios=['ref1.wav', 'ref2.wav'],
    output_dir='listening_test'
)

# Generates HTML interface for MOS collection
organizer.generate_mos_interface()
```

## Resources

- **Evaluation Code**: https://github.com/open-mmlab/Amphion/tree/main/egs/metrics/
- **Paper**: https://arxiv.org/abs/2312.09911
- **Multi-Scale CQT Discriminator**: https://arxiv.org/abs/2311.14957
- **Community**: https://discord.com/invite/drhW7ajqAG
