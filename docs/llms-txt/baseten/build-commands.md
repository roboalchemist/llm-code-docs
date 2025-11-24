# Source: https://docs.baseten.co/development/model/build-commands.md

# Custom build commands

> How to run your own docker commands during the build stage

The `build_commands` feature allows you to **run custom Docker commands** during the **build stage**, enabling **advanced caching**, **dependency management**, **and environment setup**.

**Use Cases:**

* Clone GitHub repositories
* Install dependencies
* Create directories
* Pre-download model weights

## 1. Using Build Commands in `config.yaml`

Add `build_commands` to your `config.yaml`:

```yaml  theme={"system"}
build_commands:
  - git clone https://github.com/comfyanonymous/ComfyUI.git
  - cd ComfyUI && git checkout b1fd26fe9e55163f780bf9e5f56bf9bf5f035c93 && pip install -r requirements.txt
model_name: Build Commands Demo
python_version: py310
resources:
  accelerator: A100
  use_gpu: true
```

**What happens?**

* The GitHub repository is cloned.
* The specified commit is checked out.
* Dependencies are installed.
* **Everything is cached at build time**, reducing deployment cold starts.

## 2. Creating Directories in Your Truss

Use `build_commands` to **create directories** directly in the container.

```yaml  theme={"system"}
build_commands:
  - git clone https://github.com/comfyanonymous/ComfyUI.git
  - cd ComfyUI && mkdir ipadapter
  - cd ComfyUI && mkdir instantid
```

<Info>Useful for **large codebases** requiring additional structure.</Info>

## 3. Caching Model Weights Efficiently

<Warning>For large weights (10GB+), use `model_cache` or `external_data`.</Warning>

For smaller weights, **use** `wget` in `build_commands`:

```yaml  theme={"system"}
build_commands:
  - git clone https://github.com/comfyanonymous/ComfyUI.git
  - cd ComfyUI && pip install -r requirements.txt
  - cd ComfyUI/models/controlnet && wget -O control-lora-canny-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-canny-rank256.safetensors
  - cd ComfyUI/models/controlnet && wget -O control-lora-depth-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors
model_name: Build Commands Demo
python_version: py310
resources:
  accelerator: A100
  use_gpu: true
system_packages:
  - wget
```

**Why use this?**

* **Reduces startup time** by **preloading model weights** during the build stage.
* **Ensures availability** without runtime downloads.

## 4. Running Any Shell Command

The `build_commands` feature lets you execute **any** shell command as if running it locally, with the benefit of **caching the results** at build time.

**Key Benefits:**

* **Reduces cold starts** by caching dependencies & data.
* **Ensures reproducibility** across deployments.
* **Optimizes environment setup** for fast execution.
