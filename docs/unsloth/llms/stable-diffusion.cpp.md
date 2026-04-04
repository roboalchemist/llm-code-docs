# Source: https://unsloth.ai/docs/fr/modeles/tutorials/qwen-image-2512/stable-diffusion.cpp.md

# Source: https://unsloth.ai/docs/de/modelle/tutorials/qwen-image-2512/stable-diffusion.cpp.md

# Source: https://unsloth.ai/docs/jp/moderu/tutorials/qwen-image-2512/stable-diffusion.cpp.md

# Source: https://unsloth.ai/docs/zh/mo-xing/tutorials/qwen-image-2512/stable-diffusion.cpp.md

# Source: https://unsloth.ai/docs/models/tutorials/qwen-image-2512/stable-diffusion.cpp.md

# Run Qwen-Image-2512 in stable-diffusion.cpp Tutorial

**Qwen-Image-2512** is Qwen's new text-to-image foundational model and you can now run it on your local device via stable-diffusion.cpp. See below for instructions:

## 📖 stable-diffusion.cpp Tutorial

[stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) is an open-source library for efficient and local inference of diffusion image models written in pure C/C++.

To run, you don't need a GPU, just a CPU with RAM will work. For best results, ensure your total usable memory (RAM + VRAM / unified) is larger than the GGUF size; e.g. 4-bit (Q4\_K\_M) `unsloth/Qwen-Image-Edit-2512-GGUF` is 13.1 GB, so you should have 13.2+ GB of combined memory.

The tutorial will focus on machines with CUDA available, but instructions to build with on Apple or CPU only are similar and available in the repo.

### #1. Setup environment

We will be building from source so we need to first be sure your build software is installed

```bash
sudo apt update
sudo apt install -y git cmake build-essential pkg-config
```

{% hint style="info" %}
[Releases Page](https://github.com/leejet/stable-diffusion.cpp/releases) may have pre built binaries available for your hardware if you don't want to go through the build process.
{% endhint %}

Make sure CUDA environment variables are set:

```bash
export CUDA_HOME=/usr/local/cuda
export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="$CUDA_HOME/lib64:${LD_LIBRARY_PATH:-}"
```

You can confirm if set correctly by running:

```bash
nvcc --version  // if not found install nvidia-cuda-toolkit
ldconfig -p | grep -E 'libcudart\.so|libcublas\.so'
```

We can now clone the repo and build:

{% code expandable="true" %}

```bash
git clone --recursive https://github.com/leejet/stable-diffusion.cpp
cd stable-diffusion.cpp

mkdir -p build
cd build

cmake .. -DCMAKE_BUILD_TYPE=Release -DSD_CUDA=ON
cmake --build . -j"$(nproc)"
```

{% endcode %}

Confirm sd-cli was built:

```bash
ls bin/sd-cli
```

### #2. Download Models

Diffusion models typically need 3 components. A Variational AutoEncoder (VAE) that encodes image pixel space to latent space, a text encoder to translate text to input embeddings, and the actual diffusion transformer. Both the diffusion model and text encoder can be GGUF format while we typically use safetensors for the vae. Let's download the models we will use:

```bash
cd .. 
mkdir models
mkdir outputs

## Diffusion Models
curl -L -C - -o models/qwen-image-2512-Q4_K_M.gguf \
  https://huggingface.co/unsloth/Qwen-Image-2512-GGUF/resolve/main/qwen-image-2512-Q4_K_M.gguf
curl -L -C - -o models/qwen-image-edit-2511-Q4_K_M.gguf \
  https://huggingface.co/unsloth/Qwen-Image-Edit-2511-GGUF/resolve/main/qwen-image-edit-2511-Q4_K_M.gguf
 
## Text Encoder + VAE   
curl -L -C - -o models/Qwen2.5-VL-7B-Instruct-UD-Q4_K_XL.gguf \
  https://huggingface.co/unsloth/Qwen2.5-VL-7B-Instruct-GGUF/resolve/main/Qwen2.5-VL-7B-Instruct-UD-Q4_K_XL.gguf
curl -L -C - -o models/qwen_image_vae.safetensors \
  https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors

```

We are using Q4 GGUF variants, but you can try smaller or larger quant types depending on how much VRAM/RAM you have.

{% hint style="warning" %}
The format of the vae and diffusion model might be different than the diffusers checkpoints. Only use checkpoints that are compatible with stable-diffusion.cpp and ComfyUI.
{% endhint %}

#### Workflow and Hyperparameters

You can view our detailed [#workflow-and-hyperparameters-1](https://unsloth.ai/docs/blog/comfyui#workflow-and-hyperparameters-1 "mention") Guide.

### #3. Inference

We can now run the binary that we built. This is an example of a basic text to image command:

```bash
./build/bin/sd-cli --diffusion-model models/qwen-image-2512-Q4_K_M.gguf \
    --vae models/qwen_image_vae.safetensors \
    --llm models/Qwen2.5-VL-7B-Instruct-UD-Q4_K_XL.gguf \
    --cfg-scale 2.5 --sampling-method euler -v --steps 40 \
    -H 1024 -W 1024 --diffusion-fa --flow-shift 3 \
    -p 'Aerial drone photograph of a vast field of bright yellow wildflowers with the text "Unsloth + Diffusion" spelled out in deep purple lavender flowers, sharp contrast between yellow and purple, natural organic letter shapes formed by flower beds, golden hour lighting, rolling countryside landscape, high altitude perspective looking straight down, photorealistic, 8K resolution'  \
    --offload-to-cpu -o outputs/unsloth_diffusion.png
```

{% hint style="success" %}
No need for `--offload-to-cpu` if you have enough VRAM.
{% endhint %}

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FFd4q6TxbtyQPcK7zAOIK%2Funsloth_diffusion.png?alt=media&#x26;token=182e8d80-f27e-4d86-9f46-c21d4d29840a" alt="" width="188"><figcaption></figcaption></figure>
