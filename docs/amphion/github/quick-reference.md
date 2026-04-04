# Amphion Quick Reference Guide

## Repository Structure

```
Amphion/
├── bins/                  # Command-line scripts
│   ├── train.py          # Training entrypoint
│   ├── inference.py      # Inference entrypoint
│   └── metrics/          # Evaluation scripts
├── config/               # Configuration files (YAML)
│   ├── tts/             # Text-to-Speech configs
│   ├── svc/             # Singing Voice Conversion configs
│   ├── vc/              # Voice Conversion configs
│   ├── tta/             # Text-to-Audio configs
│   └── vocoder/         # Vocoder configs
├── models/              # Model implementations
│   ├── tts/            # TTS models
│   ├── vc/             # VC models (Vevo, FACodec, etc.)
│   ├── svc/            # SVC models
│   ├── codec/          # Neural codecs
│   └── vocoders/       # Vocoders
├── modules/            # Neural network modules
├── preprocessors/      # Data preprocessing
│   └── Emilia/         # Emilia dataset preprocessing
├── evaluation/         # Evaluation metrics
├── egs/               # Example recipes
│   ├── tts/           # TTS recipes
│   ├── svc/           # SVC recipes
│   ├── vc/            # VC recipes
│   ├── tta/           # TTA recipes
│   ├── datasets/      # Dataset instructions
│   ├── metrics/       # Evaluation guides
│   └── visualization/ # SingVisio visualization
└── pretrained/        # Pre-trained model checkpoints
```

## Essential Commands

### Installation

```bash
# Clone repository
git clone https://github.com/open-mmlab/Amphion.git
cd Amphion

# Setup Python environment
conda create --name amphion python=3.9.15
conda activate amphion

# Install dependencies
sh env.sh

# Docker alternative
docker pull realamphion/amphion
docker run --runtime=nvidia --gpus all -it -v .:/app realamphion/amphion
```

### Data Preparation

```bash
# Generic dataset preprocessing
python bins/data/preprocess_dataset.py \
  --config config/tts/VITS/prepare_libritts.yaml \
  --datasets libritts

# Emilia dataset preprocessing
python bins/data/preprocess_dataset.py \
  --config config/preprocessors/Emilia/emilia_pipe.yaml \
  --raw-data-dir /path/to/raw/audio
```

### Training

```bash
# Basic training
python bins/train.py \
  --config config/tts/VITS/vits.yaml \
  --exp-name my_experiment

# Resume training
python bins/train.py \
  --config config/tts/VITS/vits.yaml \
  --exp-name my_experiment \
  --resume

# Distributed training (8 GPUs)
python -m torch.distributed.launch \
  --nproc_per_node=8 \
  bins/train.py \
  --config config/tts/VITS/vits.yaml \
  --exp-name my_experiment

# Mixed precision training
python bins/train.py \
  --config config/tts/VITS/vits.yaml \
  --exp-name my_experiment \
  --mixed_precision fp16
```

### Inference

```bash
# TTS inference
python bins/inference.py \
  --config config/tts/VITS/vits.yaml \
  --checkpoint checkpoints/my_model/ckpt.pt \
  --text "Your text here" \
  --output output.wav

# Voice Conversion inference
python bins/inference.py \
  --config config/vc/vevo/vevo.yaml \
  --checkpoint checkpoints/vevo.pt \
  --source-audio source.wav \
  --reference-audio reference.wav \
  --output output.wav

# SVC inference
python bins/inference.py \
  --config config/svc/DiffComoSVC/diffcomosvc.yaml \
  --checkpoint checkpoints/svc.pt \
  --source-audio source.wav \
  --target-speaker speaker_id \
  --output output.wav
```

### Evaluation

```bash
# Evaluate model
python bins/metrics/eval.py \
  --config config/tts/VITS/vits.yaml \
  --checkpoint checkpoints/my_model/ckpt.pt \
  --test-dir test_data/ \
  --output metrics.json

# Compute FAD score
python bins/metrics/compute_fad.py \
  --generated-dir generated_audio/ \
  --reference-dir reference_audio/

# ASR evaluation (Word Error Rate)
python bins/metrics/compute_asr.py \
  --audio-dir generated_audio/ \
  --reference-text reference_text.txt
```

## Configuration Quick Reference

### Common Config Structure

```yaml
# Model definition
model:
  type: VITS  # Model architecture
  hidden_size: 384
  encoder_hidden_size: 384
  num_mels: 80

# Data loading
data:
  dataset: libritts
  data_dir: /path/to/data
  batch_size: 16
  num_workers: 4
  pin_memory: true

# Training
train:
  max_epochs: 100
  learning_rate: 1e-3
  optimizer: adam
  betas: [0.9, 0.999]
  weight_decay: 0.0
  grad_clip: 5.0
  grad_accumulation_steps: 1

# Validation
valid:
  interval: 5000
  num_samples: 10

# Checkpointing
ckpt:
  keep_last: 3
  keep_best_by_state_dict: true

# Logging
log:
  log_interval: 10
  log_tensorboard: true
```

### Task-Specific Configs

#### TTS Configuration
```yaml
model:
  type: VITS  # or FastSpeech2, VALL-E, Jets

# Speaker information (for multi-speaker)
speaker:
  num_speakers: 100
  embedding_dim: 256

# Vocoder
vocoder:
  type: hifigan
  checkpoint: pretrained/vocoders/hifigan.pt
```

#### SVC Configuration
```yaml
# Content feature extractor
acoustic_features:
  content_feature:
    type: whisper  # or weinet, contentvec

  prosody:
    extract_f0: true
    extract_energy: true

# Acoustic decoder
acoustic_decoder:
  type: DiffComoSVC

# Speaker info
speaker:
  num_speakers: 100
  embedding_dim: 256
```

#### VC Configuration
```yaml
model:
  type: Vevo  # or FACodec, Noro

# Inference settings
inference:
  mode: timbre  # or voice
  pitch_scale: 1.0
  energy_scale: 1.0
```

## Quick Start Recipes

### TTS with VITS

```bash
# 1. Prepare data
python bins/data/preprocess_dataset.py \
  --config config/tts/VITS/prepare_libritts.yaml \
  --datasets libritts

# 2. Train
python bins/train.py \
  --config config/tts/VITS/vits.yaml \
  --exp-name vits_libritts

# 3. Infer
python bins/inference.py \
  --config config/tts/VITS/vits.yaml \
  --checkpoint checkpoints/vits_libritts/ckpt.pt \
  --text "Hello, this is a test." \
  --output output.wav
```

### SVC with DiffComoSVC

```bash
# 1. Prepare dataset
python bins/data/preprocess_dataset.py \
  --config config/svc/prepare_svcc.yaml \
  --datasets svcc

# 2. Extract features
python bins/data/extract_acoustic_features.py \
  --config config/svc/extract_whisper_feature.yaml

# 3. Train
python bins/train.py \
  --config config/svc/DiffComoSVC/diffcomosvc.yaml \
  --exp-name diffcomosvc_svcc

# 4. Infer
python bins/inference.py \
  --config config/svc/DiffComoSVC/diffcomosvc.yaml \
  --checkpoint checkpoints/diffcomosvc_svcc/ckpt.pt \
  --source-audio source.wav \
  --target-speaker 1 \
  --output output.wav
```

### Voice Conversion with Pre-trained Model

```bash
# Download and use pre-trained Vevo
python -c "
from amphion.models import build_model
model = build_model(config)
model.load_pretrained('amphion/vevo')
"

# Run inference
python bins/inference.py \
  --config config/vc/vevo/vevo.yaml \
  --checkpoint pretrained/vevo/vevo.pt \
  --source-audio source.wav \
  --reference-audio reference.wav \
  --output output.wav
```

## Common File Locations

| Item | Location |
|------|----------|
| Training scripts | `bins/train.py` |
| Inference scripts | `bins/inference.py` |
| Evaluation scripts | `bins/metrics/` |
| Data preprocessing | `bins/data/` |
| Model weights | `pretrained/` |
| TTS configs | `config/tts/` |
| SVC configs | `config/svc/` |
| VC configs | `config/vc/` |
| TTA configs | `config/tta/` |
| Vocoder configs | `config/vocoder/` |
| Model code | `models/` |
| Dataset recipes | `egs/datasets/` |
| Example configs | `egs/<task>/` |

## Environment Variables

```bash
# Set CUDA devices
export CUDA_VISIBLE_DEVICES=0,1,2,3

# Set number of CPU threads
export OMP_NUM_THREADS=8

# Enable mixed precision
export AMPHION_MIXED_PRECISION=fp16

# Set random seed for reproducibility
export PYTHONHASHSEED=0

# Enable deterministic behavior
export CUBLAS_WORKSPACE_CONFIG=:16:8
```

## Dataset Paths

### Pre-configured Datasets

```bash
# Place datasets in these locations for automatic detection:
./data/libritts/      # LibriTTS dataset
./data/ljspeech/      # LJSpeech dataset
./data/vctk/          # VCTK dataset
./data/svcc/          # SVCC dataset
./data/opensinger/    # OpenSinger dataset
./data/emilia/        # Emilia dataset
```

### Custom Dataset Format

```
custom_dataset/
├── train/
│   ├── speaker_001/
│   │   ├── audio_001.wav
│   │   ├── audio_002.wav
│   │   └── transcription.txt
│   └── speaker_002/
└── val/
    └── speaker_001/
```

## Pre-trained Model Hub

### HuggingFace Models

```bash
# Access pre-trained models
from transformers import AutoModel

# Text-to-Speech models
amphion/maskgct                # State-of-the-art TTS
amphion/vall-e                 # Zero-shot TTS
amphion/vits-libritts         # VITS trained on LibriTTS

# Voice Conversion models
amphion/vevo                   # Zero-shot VC
amphion/naturalspeech3_facodec # FACodec
amphion/metis                  # Foundation model for speech

# Visit: https://huggingface.co/amphion
```

### Local Pre-trained Models

```bash
# Download pre-trained weights
cd pretrained/
# Models are automatically fetched from HuggingFace

# Or manually download:
wget https://huggingface.co/amphion/vevo/resolve/main/vevo.pt
mv vevo.pt vevo/
```

## Troubleshooting Commands

```bash
# Check installation
python -c "import amphion; print(amphion.__version__)"

# Verify CUDA
python -c "import torch; print(torch.cuda.is_available())"

# Check GPU memory
python -c "import torch; print(torch.cuda.mem_get_info())"

# List available models
ls pretrained/

# View training logs
tail -f outputs/<exp-name>/logs/train.log

# Tensorboard visualization
tensorboard --logdir outputs/<exp-name>/tensorboard
```

## Performance Tips

### Memory Optimization

```yaml
# In configuration:
train:
  gradient_accumulation_steps: 2  # Simulate larger batch
  enable_gradient_checkpointing: true
  use_cuda_amp: true              # Mixed precision

model:
  use_checkpoint: true             # Gradient checkpointing
```

### Speed Optimization

```bash
# Use faster sampler for diffusion models
inference:
  sampler: ddim                  # Faster than DDPM
  num_steps: 30                  # Fewer steps
  use_fp16: true                 # Mixed precision

# Distributed data loading
data:
  num_workers: 8                 # CPU workers for data loading
  prefetch_factor: 2
```

### Quality Optimization

```yaml
# Higher quality settings
train:
  max_epochs: 200                # Longer training
  learning_rate: 5e-4            # Lower learning rate
  weight_decay: 1e-4             # L2 regularization
  grad_clip: 1.0                 # Tighter gradient clipping

model:
  hidden_size: 512               # Larger model
  num_layers: 12                 # More layers
```

## Resources

- **Official Documentation**: https://amphion.dev
- **GitHub Repository**: https://github.com/open-mmlab/Amphion
- **Paper (v0.2)**: https://arxiv.org/abs/2501.15442
- **Paper (v0.1)**: https://arxiv.org/abs/2312.09911
- **HuggingFace Models**: https://huggingface.co/amphion
- **ModelScope**: https://modelscope.cn/organization/amphion
- **Discord Community**: https://discord.com/invite/drhW7ajqAG
