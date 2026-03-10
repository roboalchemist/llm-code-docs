# Source: https://docs.axolotl.ai/docs/installation.html

Title: Installation – Axolotl

URL Source: https://docs.axolotl.ai/docs/installation.html

Markdown Content:
This guide covers all the ways you can install and set up Axolotl for your environment.

Requirements
------------

* NVIDIA GPU (Ampere architecture or newer for `bf16` and Flash Attention) or AMD GPU
* Python ≥3.11
* PyTorch ≥2.6.0

Installation Methods
--------------------

Important

For Blackwell GPUs, please use Pytorch 2.9.1 and CUDA 12.8.

### PyPI Installation (Recommended)

```
pip3 install -U packaging setuptools wheel ninja
pip3 install --no-build-isolation axolotl[flash-attn,deepspeed]
```

We use `--no-build-isolation` in order to detect the installed PyTorch version (if installed) in order not to clobber it, and so that we set the correct version of dependencies that are specific to the PyTorch version or other installed co-dependencies.

### uv Installation

uv is a fast, reliable Python package installer and resolver built in Rust. It offers significant performance improvements over pip and provides better dependency resolution, making it an excellent choice for complex environments.

Install uv if not already installed

```
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
```

Choose your CUDA version to use with PyTorch; e.g.`cu124`, `cu126`, `cu128`, then create the venv and activate

```
export UV_TORCH_BACKEND=cu126
uv venv --no-project --relocatable
source .venv/bin/activate
```

Install PyTorch - PyTorch 2.6.0 recommended

```
uv pip install packaging setuptools wheel
uv pip install torch==2.6.0
uv pip install awscli pydantic
```

Install axolotl from PyPi

```
uv pip install --no-build-isolation axolotl[deepspeed,flash-attn]

# optionally install with vLLM if you're using torch==2.6.0 and want to train w/ GRPO
uv pip install --no-build-isolation axolotl[deepspeed,flash-attn,vllm]
```

### Edge/Development Build

For the latest features between releases:

```
git clone https://github.com/axolotl-ai-cloud/axolotl.git
cd axolotl
pip3 install -U packaging setuptools wheel ninja
pip3 install --no-build-isolation -e '.[flash-attn,deepspeed]'
```

### Docker

`docker run --gpus '"all"' --rm -it axolotlai/axolotl:main-latest`

For development with Docker:

`docker compose up -d`

Tip Advanced Docker Configuration

```
docker run --privileged --gpus '"all"' --shm-size 10g --rm -it \
  --name axolotl --ipc=host \
  --ulimit memlock=-1 --ulimit stack=67108864 \
  --mount type=bind,src="${PWD}",target=/workspace/axolotl \
  -v ${HOME}/.cache/huggingface:/root/.cache/huggingface \
  axolotlai/axolotl:main-latest
```

Important

For Blackwell GPUs, please use `axolotlai/axolotl:main-py3.11-cu128-2.9.1` or the cloud variant `axolotlai/axolotl-cloud:main-py3.11-cu128-2.9.1`.

Please refer to the [Docker documentation](https://docs.axolotl.ai/docs/docker.html) for more information on the different Docker images that are available.

Cloud Environments
------------------

### Cloud GPU Providers

For providers supporting Docker:

* Use `axolotlai/axolotl-cloud:main-latest`
* Available on:
  * [RunPod](https://runpod.io/gsc?template=v2ickqhz9s&ref=6i7fkpdz)
  * [Vast.ai](https://cloud.vast.ai/?ref_id=62897&template_id=bdd4a49fa8bce926defc99471864cace&utm_source=axolotl&utm_medium=partner&utm_campaign=template_launch_july2025&utm_content=docs_link)
  * [PRIME Intellect](https://app.primeintellect.ai/dashboard/create-cluster?image=axolotl&location=Cheapest&security=Cheapest&show_spot=true)
  * [Modal](https://www.modal.com/?utm_source=github&utm_medium=github&utm_campaign=axolotl)
  * [Novita](https://novita.ai/gpus-console?templateId=311)
  * [JarvisLabs.ai](https://jarvislabs.ai/templates/axolotl)
  * [Latitude.sh](https://latitude.sh/blueprint/989e0e79-3bf6-41ea-a46b-1f246e309d5c)

### Google Colab

[![Image 1](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/axolotl-ai-cloud/axolotl/blob/main/examples/colab-notebooks/colab-axolotl-example.ipynb#scrollTo=msOCO4NRmRLa)

Platform-Specific Instructions
------------------------------

### macOS

`pip3 install --no-build-isolation -e '.'`

See [Section 6](https://docs.axolotl.ai/docs/installation.html#sec-troubleshooting) for Mac-specific issues.

### Windows

Important

We recommend using WSL2 (Windows Subsystem for Linux) or Docker.

Environment Managers
--------------------

### Conda/Pip venv

1. Install Python ≥3.11

2. Install PyTorch: https://pytorch.org/get-started/locally/

3. Install Axolotl:

```
pip3 install -U packaging setuptools wheel ninja
pip3 install --no-build-isolation -e '.[flash-attn,deepspeed]'
```
1. (Optional) Login to Hugging Face:

`hf auth login`

Troubleshooting
---------------

If you encounter installation issues, see our [FAQ](https://docs.axolotl.ai/docs/faq.html) and [Debugging Guide](https://docs.axolotl.ai/docs/debugging.html).
