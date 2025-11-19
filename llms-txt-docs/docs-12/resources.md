# Source: https://docs.baseten.co/deployment/resources.md

# Resources

> Manage and configure model resources

Every AI/ML model on Baseten runs on an **instance**, a dedicated set of hardware allocated to the model server. Selecting the right instance type ensures **optimal performance** while controlling **compute costs**.

* **Insufficient resources** → Slow inference or failures.
* **Excess resources** → Higher costs without added benefit.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=028f7b8a7c5e1d92f0b55f2eec8aad11" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployment-resources.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5bc11192879c6aa199388df6c531a5a0 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=acbafbbe854fa0701fc63f47ab84a8f0 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5d677c56115318ebfb994e554a1f657c 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b1fd3e5c69b2b965884044cb6975d2c6 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5ed48475146334e0a2fc56f11511d599 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c8045c2ee7a60d89a940119536d71005 2500w" />

## Instance type resource components

* **Instance** → The allocated hardware for inference.
* **vCPU** → Virtual CPU cores for general computing.
* **RAM** → Memory available to the CPU.
* **GPU** → Specialized hardware for accelerated ML workloads.
* **VRAM** → Dedicated GPU memory for model execution.

***

# Configuring model resources

Resources can be defined **before deployment** in Truss or **adjusted later** via the Baseten UI.

### Defining resources in Truss

Define resource requirements in `config.yaml` before running `truss push`. Any changes after deployment will not impact previous deployments. Running `truss push` again will create a new deployment using the resources specified in the `config.yaml`.

<Info>
  The only exception is the **development** deployment. It will be redeployed with the new specified resources.
</Info>

**Example (Stable Diffusion XL):**

```yaml config.yaml theme={"system"}
resources:
  accelerator: L4
  cpu: "4"
  memory: 16Gi
  use_gpu: true
```

Baseten provisions the **smallest instance that meets the specified constraints**:

* \*\*cpu: "3" or "4" → \*\*Maps to a 4-core instance.
* \*\*cpu: "5" to "8" → \*\*Maps to an 8-core instance.

<Info>
  `Gi` in `resources.memory` refers to **Gibibytes**, which are slightly larger
  than **Gigabytes**.
</Info>

### Updating resources in the Baseten UI

Once deployed, resource configurations can only be updated **through the Baseten UI**. Changing the instance type will deploy a new copy of the deployment using the new specified instance type.

<Info>
  Like when running `truss push`, the **development** deployment will be redeployed with the new specified instance type.
</Info>

For a list of available instance types, see the [instance type reference](/deployment/resources#instance-type-reference).

***

# Instance Type Reference

Specs and benchmarks for every Baseten instance type.

Choosing the right instance for model inference means balancing performance and cost. This page lists all available instance types on Baseten to help you deploy and serve models effectively.

## CPU-only Instances

Cost-effective options for lighter workloads. No GPU.

* **Starts at**: \$0.00058/min
* **Best for**: Transformers pipelines, small QA models, text embeddings

| Instance | \$/min    | vCPU | RAM    |
| -------- | --------- | ---- | ------ |
| 1×2      | \$0.00058 | 1    | 2 GiB  |
| 1×4      | \$0.00086 | 1    | 4 GiB  |
| 2×8      | \$0.00173 | 2    | 8 GiB  |
| 4×16     | \$0.00346 | 4    | 16 GiB |
| 8×32     | \$0.00691 | 8    | 32 GiB |
| 16×64    | \$0.01382 | 16   | 64 GiB |

**Example workloads:**

* `1x2`: Text classification (e.g., Truss quickstart)
* `4x16`: LayoutLM Document QA
* `4x16+`: Sentence Transformers embeddings on larger corpora

## GPU Instances

Accelerated inference for LLMs, diffusion models, and Whisper.

| Instance       | \$/min    | vCPU | RAM      | GPU                    | VRAM    |
| -------------- | --------- | ---- | -------- | ---------------------- | ------- |
| T4x4x16        | \$0.01052 | 4    | 16 GiB   | NVIDIA T4              | 16 GiB  |
| T4x8x32        | \$0.01504 | 8    | 32 GiB   | NVIDIA T4              | 16 GiB  |
| T4x16x64       | \$0.02408 | 16   | 64 GiB   | NVIDIA T4              | 16 GiB  |
| L4x4x16        | \$0.01414 | 4    | 16 GiB   | NVIDIA L4              | 24 GiB  |
| L4:2x4x16      | \$0.04002 | 24   | 96 GiB   | 2 NVIDIA L4s           | 48 GiB  |
| L4:4x48x192    | \$0.08003 | 48   | 192 GiB  | 4 NVIDIA L4s           | 96 GiB  |
| A10Gx4x16      | \$0.02012 | 4    | 16 GiB   | NVIDIA A10G            | 24 GiB  |
| A10Gx8x32      | \$0.02424 | 8    | 32 GiB   | NVIDIA A10G            | 24 GiB  |
| A10Gx16x64     | \$0.03248 | 16   | 64 GiB   | NVIDIA A10G            | 24 GiB  |
| A10G:2x24x96   | \$0.05672 | 24   | 96 GiB   | 2 NVIDIA A10Gs         | 48 GiB  |
| A10G:4x48x192  | \$0.11344 | 48   | 192 GiB  | 4 NVIDIA A10Gs         | 96 GiB  |
| A10G:8x192x768 | \$0.32576 | 192  | 768 GiB  | 8 NVIDIA A10Gs         | 188 GiB |
| V100x8x61      | \$0.06120 | 16   | 61 GiB   | NVIDIA V100            | 16 GiB  |
| A100x12x144    | \$0.10240 | 12   | 144 GiB  | 1 NVIDIA A100          | 80 GiB  |
| A100:2x24x288  | \$0.20480 | 24   | 288 GiB  | 2 NVIDIA A100s         | 160 GiB |
| A100:3x36x432  | \$0.30720 | 36   | 432 GiB  | 3 NVIDIA A100s         | 240 GiB |
| A100:4x48x576  | \$0.40960 | 48   | 576 GiB  | 4 NVIDIA A100s         | 320 GiB |
| A100:5x60x720  | \$0.51200 | 60   | 720 GiB  | 5 NVIDIA A100s         | 400 GiB |
| A100:6x72x864  | \$0.61440 | 72   | 864 GiB  | 6 NVIDIA A100s         | 480 GiB |
| A100:7x84x1008 | \$0.71680 | 84   | 1008 GiB | 7 NVIDIA A100s         | 560 GiB |
| A100:8x96x1152 | \$0.81920 | 96   | 1152 GiB | 8 NVIDIA A100s         | 640 GiB |
| H100           | \$0.16640 | -    | -        | 1 NVIDIA H100          | 80 GiB  |
| H100:2         | \$0.33280 | -    | -        | 2 NVIDIA H100s         | 160 GiB |
| H100:4         | \$0.66560 | -    | -        | 4 NVIDIA H100s         | 320 GiB |
| H100:8         | \$1.33120 | -    | -        | 8 NVIDIA H100s         | 640 GiB |
| H100MIG        | \$0.08250 | -    | -        | Fractional NVIDIA H100 | 40 GiB  |

## GPU Details & Workloads

### T4

Turing-series GPU

* 2,560 CUDA / 320 Tensor cores
* 16 GiB VRAM
* **Best for:** Whisper, small LLMs like StableLM 3B

### L4

Ada Lovelace-series GPU

* 7,680 CUDA / 240 Tensor cores
* 24 GiB VRAM, 300 GiB/s
* 24 GiB VRAM, 300 GiB/s
* 121 TFLOPS (fp16)
* **Best for**: Stable Diffusion XL
* **Limit**: Not suitable for LLMs due to bandwidth

### A10G

Ampere-series GPU

* 9,216 CUDA / 288 Tensor cores
* 24 GiB VRAM, 600 GiB/s
* 70 TFLOPS (fp16)
* **Best for**: Mistral 7B, Whisper, Stable Diffusion/SDXL

### V100

Volta-series GPU

* 16 GiB VRAM
* **Best for**: Legacy workloads needing V100-specific support

### A100

Ampere-series GPU

* 6,912 CUDA / 432 Tensor cores
* 80 GiB VRAM, 1.94 TB/s
* 312 TFLOPS (fp16)
* **Best for**: Mixtral, Llama 2 70B (2 A100s), Falcon 180B (5 A100s), SDXL

### H100

Hopper-series GPU

* 16,896 CUDA / 640 Tensor cores
* 80 GiB VRAM, 3.35 TB/s
* 990 TFLOPS (fp16)
* **Best for**: Mixtral 8x7B, Llama 2 70B (2×H100), SDXL

### H100MIG

Fractional H100 (3/7 compute, ½ memory)

* 7,242 CUDA cores, 40 GiB VRAM
* 1.675 TB/s bandwidth
* **Best for**: Efficient LLM inference at lower cost than A100
