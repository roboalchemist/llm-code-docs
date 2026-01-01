# Source: https://github.com/pyannote/pyannote-audio

# pyannote.audio Documentation

pyannote.audio is an open-source Python toolkit for speaker diarization, providing neural building blocks for identifying who spoke when in audio files.

## Overview

pyannote.audio is built on PyTorch and PyTorch Lightning, offering:

- State-of-the-art speaker diarization models
- Pretrained pipelines available on Hugging Face
- Support for voice activity detection (VAD), speaker change detection, and overlapped speech detection
- Multi-GPU training with PyTorch Lightning
- Flexible pipeline-based architecture for composing tasks
- Premium pyannoteAI cloud API for production deployments

## Key Features

- **Speaker Diarization**: Identify who spoke when in audio files
- **Voice Activity Detection (VAD)**: Detect speech regions in audio
- **Speaker Change Detection**: Identify points where speakers change
- **Overlapped Speech Detection**: Detect when multiple speakers talk simultaneously
- **Speaker Embedding**: Generate speaker representations for verification
- **Speaker Verification**: Identify speakers using voiceprints
- **Pretrained Models**: Download pretrained models from Hugging Face
- **Training Support**: Train custom models on your own data
- **Multi-GPU Training**: Leverage multiple GPUs with PyTorch Lightning

## Installation

```bash
# Install with pip
pip install pyannote.audio

# Install with uv (recommended)
uv add pyannote.audio
```

### Requirements

- Python 3.8+
- PyTorch 1.12+
- FFmpeg (for audio decoding via torchcodec)
- CUDA/GPU (recommended for inference, required for training)

## Quick Start

### Community Open-Source Model

```python
from pyannote.audio import Pipeline

# Load pretrained community-1 pipeline
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-community-1",
    use_auth_token="HUGGINGFACE_TOKEN"
)

# Apply to audio file
output = pipeline("audio.wav")

# Print results
for turn, speaker in output.speaker_diarization:
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
```

### Premium pyannoteAI API

```python
from pyannote.audio import Pipeline

# Use premium precision-2 model via API
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-precision-2",
    token="PYANNOTEAI_API_KEY"
)

# Apply to audio file (runs on pyannoteAI servers)
output = pipeline("audio.wav")

for turn, speaker in output.speaker_diarization:
    print(f"start={turn.start:.1f}s stop={turn.end:.1f}s {speaker}")
```

## Available Models

### Speaker Diarization
- `pyannote/speaker-diarization-community-1` - Free, open-source model
- `pyannote/speaker-diarization-3.1` - Legacy v3.1 model
- `pyannote/speaker-diarization-precision-2` - Premium cloud-based API

### Voice Activity Detection
- `pyannote/voice-activity-detection` - Detect speech regions
- `pyannote/voice-activity-detection-v3` - Latest VAD model

### Speaker Segmentation
- Speaker segmentation models for custom pipelines
- Customizable for fine-tuning on domain-specific data

## Configuration Options

### Pipeline Parameters

```python
# Limit number of speakers
output = pipeline("audio.wav", num_speakers=2)

# Set speaker count bounds
output = pipeline("audio.wav", min_speakers=1, max_speakers=3)

# Use progress hook for long audio
from pyannote.audio.pipelines.utils.hook import ProgressHook
with ProgressHook() as hook:
    output = pipeline("audio.wav", hook=hook)
```

### GPU Acceleration

```python
import torch
pipeline.to(torch.device("cuda"))  # Use GPU for inference
```

## Output Format

Speaker diarization output is a `DiarizationResult` object:

```python
for turn, speaker in output.speaker_diarization:
    print(f"Speaker {speaker}: {turn.start:.2f}s - {turn.end:.2f}s")
    print(f"Duration: {turn.duration:.2f}s")

# Export to RTTM format
with open("output.rttm", "w") as rttm:
    output.write_rttm(rttm)
```

## Training Custom Models

### Basic Training

```python
from pyannote.audio.models import SpeakerDiarization

# Define model
model = SpeakerDiarization(encoder="wav2vec2-large-xlsr-53-english")

# Train on your data
from pytorch_lightning import Trainer
trainer = Trainer(max_epochs=100, gpus=1)
trainer.fit(model, train_loader, val_loader)
```

### Fine-tuning Pretrained Models

```python
# Load pretrained model
from pyannote.audio import Model
model = Model.from_pretrained("pyannote/speaker-diarization-3.1")

# Fine-tune on your data
trainer = Trainer(max_epochs=50, gpus=1)
trainer.finetune(model, train_loader, val_loader)
```

## API Reference

### Pipeline

- `Pipeline.from_pretrained(model_id, token=None)` - Load pretrained pipeline
- `pipeline(audio_path, num_speakers=None, min_speakers=None, max_speakers=None)` - Process audio file
- `pipeline.to(device)` - Move pipeline to device (GPU/CPU)

### Output

- `output.speaker_diarization` - Iterator over (turn, speaker) tuples
- `output.write_rttm(file_handle)` - Export results to RTTM format
- `output.to_dataframe()` - Convert to pandas DataFrame

### Models

- `Model.from_pretrained(model_id, token=None)` - Load pretrained model
- `Model.custom(architecture, pretrained=False)` - Create custom model

## Benchmarks

As of September 2025, performance on standard benchmarks:

| Dataset | Legacy (3.1) | Community-1 | Precision-2 |
|---------|-------------|------------|------------|
| AISHELL-4 | 12.2% | 11.7% | 11.4% |
| AMI (IHM) | 18.8% | 17.0% | 12.9% |
| VoxConverse | 11.2% | 11.2% | 8.5% |
| DIHARD 3 | 21.4% | 20.2% | 14.7% |

Diarization Error Rate (DER) in %, lower is better.

## Telemetry

pyannote.audio tracks usage for research purposes:

```python
from pyannote.audio.telemetry import set_telemetry_metrics

# Enable metrics (default)
set_telemetry_metrics(True, save_choice_as_default=True)

# Disable metrics
set_telemetry_metrics(False, save_choice_as_default=True)
```

## Resources

- **Official Website**: https://pyannote.ai
- **GitHub Repository**: https://github.com/pyannote/pyannote-audio
- **Documentation**: https://docs.pyannote.ai (pyannoteAI)
- **Hugging Face Models**: https://huggingface.co/pyannote
- **Paper**: See GitHub repository for academic publications
- **Issues & Questions**: GitHub Issues for bug reports and feature requests

## Related Projects

- **pyannote.metrics**: Evaluation metrics for diarization
- **pyannote.core**: Core data structures (Annotation, Timeline, etc.)
- **pyannoteAI**: Premium cloud-based speaker diarization service

## License

MIT License - See LICENSE file in repository

## Citation

If you use pyannote.audio in published research, please cite the appropriate paper(s) from the GitHub repository.

## Support

- **FAQ**: See FAQ.md
- **GitHub Issues**: https://github.com/pyannote/pyannote-audio/issues
- **Discussion**: https://github.com/pyannote/pyannote-audio/discussions
- **Documentation**: https://docs.pyannote.ai (for premium API)
