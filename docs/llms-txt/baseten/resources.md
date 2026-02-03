# Source: https://docs.baseten.co/deployment/resources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Resources

> Manage and configure model resources

Every AI/ML model on Baseten runs on an **instance**, a dedicated set of hardware allocated to the model server. Selecting the right instance type ensures **optimal performance** while controlling **compute costs**.

* **Insufficient resources**: Slow inference or failures.
* **Excess resources**: Higher costs without added benefit.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=028f7b8a7c5e1d92f0b55f2eec8aad11" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployment-resources.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5bc11192879c6aa199388df6c531a5a0 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=acbafbbe854fa0701fc63f47ab84a8f0 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5d677c56115318ebfb994e554a1f657c 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b1fd3e5c69b2b965884044cb6975d2c6 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5ed48475146334e0a2fc56f11511d599 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c8045c2ee7a60d89a940119536d71005 2500w" />

## Instance type resource components

* **Instance**: The allocated hardware for inference.
* **vCPU**: Virtual CPU cores for general computing.
* **RAM**: Memory available to the CPU.
* **GPU**: Specialized hardware for accelerated ML workloads.
* **VRAM**: Dedicated GPU memory for model execution.

***

# Configuring model resources

Resources can be defined **before deployment** in Truss or **adjusted later** via the Baseten UI.

### Defining resources in Truss

Define resource requirements in [`config.yaml`](/development/model/configuration) before running `truss push`.

* **Development deployment** (`truss push --watch`): Deploys or overwrites the existing development deployment with live reload enabled. Use [`truss watch`](/development/model/deploy-and-iterate) for rapid iteration without redeploying.
* **Published deployment** (`truss push --publish`): Creates a new deployment (named sequentially: `deployment-1`, `deployment-2`, etc.) using the resources in [`config.yaml`](/development/model/configuration).
* **Production deployment** (`truss push --promote`): Creates a new deployment and promotes it to production, replacing the active deployment.
* **Environment deployment** (`truss push --environment <name>`): Deploys directly to a [custom environment](/deployment/environments) like staging.

<Note>
  When no flag is specified, `truss push` defaults to a published deployment. Use `--watch` for development deployments with live reload support.
</Note>

<Info>
  Changes to `config.yaml` only affect new deployments. To update resources on an existing published deployment, edit resources in the [Baseten UI](#updating-resources-in-the-baseten-ui).
</Info>

You can configure resources in two ways:

**Option 1: Specify individual resource fields**

```yaml config.yaml theme={"system"}
resources:
  accelerator: L4
  cpu: "4"
  memory: 16Gi
```

Baseten provisions the **smallest instance that meets the specified constraints**:

* cpu: "3" or "4" → Maps to a 4-core instance.
* cpu: "5" to "8" → Maps to an 8-core instance.

<Info>
  `Gi` in `resources.memory` refers to **Gibibytes**, which are slightly larger
  than **Gigabytes**.
</Info>

**Option 2: Specify an exact instance type**

An instance type is the full SKU name that uniquely identifies a specific hardware configuration. When you specify individual resource fields like `cpu` and `accelerator`, Baseten selects the smallest instance that meets your requirements. With `instance_type`, you specify exactly which instance you want—no guessing required.

Use `instance_type` when you:

* Know the exact hardware configuration you need.
* Want to ensure consistent instance selection across deployments.
* Are following a recommendation for a specific model (e.g., "use an L4 with 4 vCPUs and 16 GiB RAM").

```yaml config.yaml theme={"system"}
resources:
  instance_type: "L4:4x16"
```

The format encodes the hardware specs: `<GPU>:<vCPU>x<MEMORY>`. For example, `L4:4x16` means an L4 GPU with 4 vCPUs and 16 GiB of RAM. When `instance_type` is specified, other resource fields (`cpu`, `memory`, `accelerator`, `use_gpu`) are ignored.

### Updating resources in the Baseten UI

Once deployed, resource configurations can only be updated **through the Baseten UI**. Changing the instance type deploys a copy of the deployment using the specified instance type.

<Info>
  Like when running `truss push --watch`, the **development** deployment will be redeployed with the new specified instance type.
</Info>

For a list of available instance types, see the [instance type reference](/deployment/resources#instance-type-reference).

***

# Instance type reference

Specs and benchmarks for every Baseten instance type.

Choosing the right instance for model inference means balancing performance and cost. This page lists all available instance types on Baseten to help you deploy and serve models effectively.

## CPU-only instances

Cost-effective options for lighter workloads. No GPU.

* **Starts at**: \$0.00058/min
* **Best for**: Transformers pipelines, small QA models, text embeddings

| Instance | \$/min    | vCPU | RAM    |
| -------- | --------- | ---- | ------ |
| 1x2      | \$0.00058 | 1    | 2 GiB  |
| 1x4      | \$0.00086 | 1    | 4 GiB  |
| 2x8      | \$0.00173 | 2    | 8 GiB  |
| 4x16     | \$0.00346 | 4    | 16 GiB |
| 8x32     | \$0.00691 | 8    | 32 GiB |
| 16x64    | \$0.01382 | 16   | 64 GiB |

To select a CPU-only instance, use the format `CPU:<vCPU>x<MEMORY>` (e.g., `instance_type: "CPU:4x16"`).

**Example workloads:**

* `1x2`: Text classification (e.g., Truss quickstart)
* `4x16`: LayoutLM Document QA
* `4x16+`: Sentence Transformers embeddings on larger corpora

## GPU instances

Accelerated inference for LLMs, diffusion models, and Whisper.

| Instance       | \$/min    | vCPU | RAM      | GPU                    | VRAM    |
| -------------- | --------- | ---- | -------- | ---------------------- | ------- |
| T4x4x16        | \$0.01052 | 4    | 16 GiB   | NVIDIA T4              | 16 GiB  |
| T4x8x32        | \$0.01504 | 8    | 32 GiB   | NVIDIA T4              | 16 GiB  |
| T4x16x64       | \$0.02408 | 16   | 64 GiB   | NVIDIA T4              | 16 GiB  |
| L4x4x16        | \$0.01414 | 4    | 16 GiB   | NVIDIA L4              | 24 GiB  |
| L4:2x24x96     | \$0.04002 | 24   | 96 GiB   | 2 NVIDIA L4s           | 48 GiB  |
| L4:4x48x192    | \$0.08003 | 48   | 192 GiB  | 4 NVIDIA L4s           | 96 GiB  |
| A10Gx4x16      | \$0.02012 | 4    | 16 GiB   | NVIDIA A10G            | 24 GiB  |
| A10Gx8x32      | \$0.02424 | 8    | 32 GiB   | NVIDIA A10G            | 24 GiB  |
| A10Gx16x64     | \$0.03248 | 16   | 64 GiB   | NVIDIA A10G            | 24 GiB  |
| A10G:2x24x96   | \$0.05672 | 24   | 96 GiB   | 2 NVIDIA A10Gs         | 48 GiB  |
| A10G:4x48x192  | \$0.11344 | 48   | 192 GiB  | 4 NVIDIA A10Gs         | 96 GiB  |
| A10G:8x192x768 | \$0.32576 | 192  | 768 GiB  | 8 NVIDIA A10Gs         | 188 GiB |
| A100x12x144    | \$0.10240 | 12   | 144 GiB  | 1 NVIDIA A100          | 80 GiB  |
| A100:2x24x288  | \$0.20480 | 24   | 288 GiB  | 2 NVIDIA A100s         | 160 GiB |
| A100:3x36x432  | \$0.30720 | 36   | 432 GiB  | 3 NVIDIA A100s         | 240 GiB |
| A100:4x48x576  | \$0.40960 | 48   | 576 GiB  | 4 NVIDIA A100s         | 320 GiB |
| A100:5x60x720  | \$0.51200 | 60   | 720 GiB  | 5 NVIDIA A100s         | 400 GiB |
| A100:6x72x864  | \$0.61440 | 72   | 864 GiB  | 6 NVIDIA A100s         | 480 GiB |
| A100:7x84x1008 | \$0.71680 | 84   | 1008 GiB | 7 NVIDIA A100s         | 560 GiB |
| A100:8x96x1152 | \$0.81920 | 96   | 1152 GiB | 8 NVIDIA A100s         | 640 GiB |
| H100           | \$0.10833 | -    | -        | 1 NVIDIA H100          | 80 GiB  |
| H100:2         | \$0.21667 | -    | -        | 2 NVIDIA H100s         | 160 GiB |
| H100:4         | \$0.43333 | -    | -        | 4 NVIDIA H100s         | 320 GiB |
| H100:8         | \$0.86667 | -    | -        | 8 NVIDIA H100s         | 640 GiB |
| H100MIG        | \$0.06250 | -    | -        | Fractional NVIDIA H100 | 40 GiB  |

To select a GPU instance with `instance_type`:

* **Single GPU**: `<GPU>:<vCPU>x<MEMORY>` (e.g., `"L4:4x16"`).
* **Multi-GPU**: `<GPU>:<COUNT>x<vCPU>x<MEMORY>` (e.g., `"A100:2x24x288"`).
* **H100**: `H100` or `H100:<COUNT>` (e.g., `"H100:2"`).
* **Fractional H100**: `"H100_40GB"`.

## GPU details and workloads

### T4

Turing-series GPU

* 2,560 CUDA / 320 Tensor cores
* 16 GiB VRAM
* **Best for:** Whisper, small LLMs like StableLM 3B

### L4

Ada Lovelace-series GPU

* 7,680 CUDA / 240 Tensor cores
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
* **Best for**: Mixtral 8x7B, Llama 2 70B (2xH100), SDXL

### H100MIG

Fractional H100 (3/7 compute, ½ memory)

* 7,242 CUDA cores, 40 GiB VRAM
* 1.675 TB/s bandwidth
* **Best for**: Efficient LLM inference at lower cost than A100
