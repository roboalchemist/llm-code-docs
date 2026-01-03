# Amphion Installation Guide

## Overview

Amphion can be installed through two methods:
1. Setup Installer (Python environment)
2. Docker Image (containerized with GPU support)

## Method 1: Setup Installer

### Prerequisites

- Git
- Conda (Anaconda or Miniconda)
- Python 3.9+ (recommended: 3.9.15)
- CUDA toolkit (for GPU support)
- cuDNN (for GPU support)

### Installation Steps

#### Step 1: Clone the Repository

```bash
git clone https://github.com/open-mmlab/Amphion.git
cd Amphion
```

#### Step 2: Create Conda Environment

```bash
conda create --name amphion python=3.9.15
conda activate amphion
```

#### Step 3: Install Dependencies

Amphion provides an installation script that handles all Python package dependencies:

```bash
sh env.sh
```

This script will install:
- Core dependencies (PyTorch, torchaudio, librosa)
- Model dependencies (diffusers, transformers, julius)
- Audio processing (soundfile, scipy, matplotlib)
- Data processing (numpy, pandas)
- ML utilities (lightning, tensorboard, wandb)

#### Step 4: Verify Installation

To verify your installation is working:

```bash
python -c "import amphion; print('Amphion installed successfully')"
```

### Troubleshooting

**CUDA/GPU Issues**: If you encounter CUDA errors, ensure you have:
- Compatible NVIDIA drivers installed
- CUDA toolkit matching your PyTorch installation
- cuDNN properly configured

**Memory Issues**: If you encounter out-of-memory errors:
- Reduce batch size in configuration files
- Use gradient accumulation
- Enable gradient checkpointing

## Method 2: Docker Installation

### Prerequisites

- Docker
- NVIDIA Driver (latest version recommended)
- NVIDIA Container Toolkit
- CUDA toolkit (compatible with your NVIDIA driver)

### Installation Steps

#### Step 1: Install Docker Dependencies

If not already installed:

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install NVIDIA Container Toolkit
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

#### Step 2: Clone Repository and Pull Docker Image

```bash
git clone https://github.com/open-mmlab/Amphion.git
cd Amphion

docker pull realamphion/amphion
```

#### Step 3: Run Docker Container

Run the Docker container with GPU support:

```bash
docker run --runtime=nvidia --gpus all -it -v .:/app realamphion/amphion
```

#### Step 4: Mount Datasets

To use your own datasets with Docker, mount them as volumes:

```bash
docker run --runtime=nvidia --gpus all -it \
  -v .:/app \
  -v /path/to/datasets:/app/datasets \
  realamphion/amphion
```

For detailed Docker volume mounting instructions, see:
- [Mount Dataset in Docker Container](../egs/datasets/docker.md)
- [Docker Documentation](https://docs.docker.com/engine/reference/commandline/container_run/#volume)

### Available Docker Images

The official Docker image includes:
- Pre-installed PyTorch with CUDA support
- All Amphion dependencies and models
- NVIDIA CUDA runtime
- Ready-to-use development environment

## System Requirements

### Minimum Requirements

- **CPU**: 4+ cores
- **RAM**: 8GB (16GB+ recommended)
- **GPU**: NVIDIA GPU with 2GB+ VRAM (for inference)
  - 8GB+ VRAM recommended for training
- **Disk Space**: 20GB+ for models and datasets

### Recommended Configuration

- **CPU**: 8+ cores
- **RAM**: 32GB+
- **GPU**: NVIDIA GPU with 24GB+ VRAM (for training)
  - RTX 3090, RTX 4090, H100, or A100 recommended
- **Storage**: SSD with 100GB+ free space

## Quick Start After Installation

### Python Usage

After installation, use Amphion in your Python code:

```python
from amphion.utils import load_config
from amphion.models import build_model

# Load configuration
config = load_config('path/to/config.yaml')

# Build and use model
model = build_model(config)
```

### Command Line Usage

Access Amphion's CLI tools:

```bash
# Activate environment
conda activate amphion

# Run preprocessing
python bins/data/preprocess_dataset.py --config config/...

# Train a model
python bins/train.py --config config/...

# Inference
python bins/inference.py --config config/...
```

### Docker Usage

Inside Docker container:

```bash
cd /app

# Run preprocessing
python bins/data/preprocess_dataset.py --config config/...

# Train a model
python bins/train.py --config config/...

# Exit container
exit
```

## Configuration Files

Amphion uses YAML configuration files for all tasks. Configuration templates are located in:

```
Amphion/
├── config/
│   ├── tts/           # Text-to-Speech configs
│   ├── svc/           # Singing Voice Conversion configs
│   ├── vc/            # Voice Conversion configs
│   ├── tta/           # Text-to-Audio configs
│   └── vocoder/       # Vocoder configs
```

## Environment Variables

Optional environment variables for advanced configuration:

```bash
# Set number of CPU threads
export OMP_NUM_THREADS=8

# Set CUDA device
export CUDA_VISIBLE_DEVICES=0,1

# Enable mixed precision
export AMPHION_MIXED_PRECISION=fp16
```

The `env.sh` script is provided to set up common environment variables:

```bash
source env.sh
```

## Next Steps

After successful installation:

1. **Choose a Task**:
   - [Text-to-Speech (TTS)](../egs/tts/README.md)
   - [Singing Voice Conversion (SVC)](../egs/svc/README.md)
   - [Voice Conversion (VC)](../models/vc/vevo/README.md)
   - [Text-to-Audio (TTA)](../egs/tta/README.md)

2. **Download Datasets**: Check available preprocessed datasets in `egs/datasets/README.md`

3. **Run Examples**: Start with provided recipes and examples

4. **Join Community**: Participate in discussions on [Discord](https://discord.com/invite/drhW7ajqAG)

## Getting Help

- **GitHub Issues**: https://github.com/open-mmlab/Amphion/issues
- **Discord Community**: https://discord.com/invite/drhW7ajqAG
- **Documentation**: https://amphion.dev
- **Papers & Reports**: https://arxiv.org/search/?query=amphion
