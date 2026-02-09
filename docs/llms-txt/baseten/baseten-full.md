# Baseten Documentation

Source: https://docs.baseten.co/llms-full.txt

---

# How Baseten works
Source: https://docs.baseten.co/concepts/howbasetenworks

Baseten is a platform for building, serving, and scaling AI models in production.

It supports multiple entry points depending on your workflow—whether you're deploying a dedicated model, calling an open-source LLM via our Model API, or training from scratch.

**At the core is the Baseten Inference Stack:** performant model engines on top of Inference optimized infrastructure. Instead of managing infrastructure, scaling policies, and performance optimization, you can focus on building and iterating on your AI-powered applications.

***

## Dedicated deployments

This is the primary workflow for teams deploying custom, open-source, or fine-tuned models with full control.

Baseten’s deployment stack is structured around four key pillars:

### Development

Package any model using Truss, our open-source framework for defining dependencies, hardware, and custom logic—no Docker required. For more advanced use cases, build compound inference systems using Chains, orchestrating multiple models, APIs, and processing steps.

<CardGroup>
  <Card title="Developing a model" href="/development/model">
    Package and deploy any AI/ML model as an API with Truss or a Custom Server.
  </Card>

  <Card title="Developing a Chain" href="/development/chain">
    Build multi-model workflows by chaining models, pre/post-processing, and
    business logic.
  </Card>
</CardGroup>

### Deployment

Deploy models to dedicated, autoscaling infrastructure. Use Environments for controlled versioning, rollouts, and promotion between staging and production. Support includes scale-to-zero, canary deploys, and structured model management.

<img />

### Inference

Serve synchronous, asynchronous, and streaming predictions with configurable execution controls. Optimize for latency, throughput, or cost depending on your application’s needs.

<img />

### Observability

Monitor model health and performance with real-time metrics, logs, and detailed request traces. Export data to observability tools like Datadog or Prometheus. Debug behavior with full visibility into inputs, outputs, and errors.

<img />

This full-stack infrastructure, from packaging to observability, is powered by the **Baseten Inference Stack**: performant model engines, cross-cloud availability, and seamless developer workflows.

***

## Model APIs

[Model APIs](/development/model-apis/overview) offer a fast, reliable path to production for LLM-powered features. Use OpenAI-compatible endpoints to call performant open-source models like Llama 4, DeepSeek, and Qwen, with support for structured outputs and tool calling.

If your code already works with OpenAI’s SDKs, it’ll work with Baseten—no wrappers or rewrites required.

***

## Training

[Baseten Training](/training/overview) provides scalable infrastructure for running containerized training jobs. Define your code, environment, and compute resources; manage checkpoints and logs; and transition seamlessly from training to deployment.

Organize work with TrainingProjects and track reproducible runs via TrainingJobs. Baseten supports any framework, from PyTorch to custom setups, with centralized artifact and job management.

***

## Summary

* Use [Dedicated Deployments](/development/concepts) to run and scale production-grade models with full control.
* Use [Model APIs](/development/model-apis/overview) to quickly build LLM-powered features without managing infrastructure.
* Use [Training](/training/overview) to run reproducible training jobs and productionize your own models.

Each product is built on the same core: reliable infrastructure, strong developer ergonomics, and a focus on operational excellence.


# Why Baseten
Source: https://docs.baseten.co/concepts/whybaseten

Baseten delivers fast, scalable AI/ML inference with enterprise-grade security and reliability—whether in our cloud or yours.

<img />

## Mission-critical inference

Built for high-performance workloads, our platform optimizes inference performance across modalities, from state-of-the-art transcription to blazing-fast LLMs.
Built-in autoscaling, model performance optimizations, and deep observability tools ensure efficiency without complexity.
Trusted by top ML teams serving their products to millions of users, Baseten accelerates time to market for AI-driven products by building on four key pillars of inference: performance, infrastructure, tooling, and expertise.

#### Model performance

Baseten’s model performance engineers apply the latest research and custom engine optimizations in production, so you get low latency and high throughput out of the box.
Production-grade support for critical features, like speculative decoding and LoRA swapping, is baked into our platform.

#### Cloud-native infrastructure

[Deploy](/deployment/concepts) and [scale models](/deployment/autoscaling) across clusters, regions, and clouds with five nines reliability.
We built all the orchestration and optimized the network routing to ensure global scalability without the operational complexity.

#### Model management tooling

Love your development ecosystem, with deep [observability](/observability/metrics) and easy-to-use tools for deploying, managing, and iterating on models in production.
Quickly serve open-source and custom models, ultra-low-latency compound AI systems, and custom Docker servers in our cloud or yours.

#### Forward deployed engineering

Baseten’s expert engineers work as an extension of your team, customizing deployments for your target performance, quality, and cost-efficiency metrics.
Get hands-on support with deep inference-specific expertise and 24/7 on-call availability.

#### Model training and finetuning, all in one platform

Baseten Training provides a fast, scalable, and flexible platform for training and finetuning models. Deploy checkpoints immediately with the click of a button to run end-to-end evals and seamlessly launch to production.


# Autoscaling
Source: https://docs.baseten.co/deployment/autoscaling

Autoscaling dynamically adjusts the number of active replicas to **handle variable traffic** while minimizing idle compute costs.

<img />

## Configuring autoscaling

Autoscaling settings are **per deployment** and are inherited when promoting a model to production unless overridden.

Configure autoscaling through:

* **UI** → Manage settings in your Baseten workspace.
* **API** → Use the **[autoscaling API](/reference/management-api/deployments/autoscaling)**.

### Replica scaling

Each deployment scales within a configured range of replicas:

* **Minimum replicas** → The lowest number of active replicas.
  * Default: `0` (scale to zero).
  * Maximum value: Cannot exceed the **maximum replica count**.
* **Maximum replicas** → The upper limit of active replicas.
  * Default: `1`.
  * Max: `10` by default (contact support to increase).

When first deployed, the model starts with `1` replica (or the **minimum count**, if higher). As traffic increases, additional replicas **scale up** until the **maximum count** is reached. When traffic decreases, replicas **scale down** to match demand.

***

## Autoscaler settings

The **autoscaler logic** is controlled by three key parameters:

* **Autoscaling window** → Time window for traffic analysis before scaling up/down. Default: 60 seconds.
* **Scale down delay** → Time before an unused replica is removed. Default: 900 seconds (15 minutes).
* **Concurrency target** → Number of requests a replica should handle before scaling. Default: 1 request.
* **Target Utilization Percentage** → Target percentage of filled concurrency slots. Default: 70%.

A **short autoscaling window** with a **longer scale-down delay** is recommended for **fast upscaling** while maintaining capacity during temporary dips.

The **target utilization percentage** determines the amount of headroom available. A higher number means less headroom and more
usage on each replica, where a lower number means more headroom and buffer for traffic spikes.

***

## Autoscaling behavior

### Scaling up

When the **average requests per active replica** exceed the **concurrency target** within the **autoscaling window**, more replicas are created until:

* The **concurrency target is met**, or
* The **maximum replica count** is reached.

Note here that the amount of headroom is determined by the **target utilization percentage**. For example, with a concurrency target of 10 requests and a
target utilization percentage of 70%, scaling will begin when the average requests per active replica exceeds 7.

### Scaling down

When traffic drops below the **concurrency target**, excess replicas are flagged for removal. The **scale-down delay** ensures that replicas are not removed prematurely:

* If traffic **spikes again before the delay ends**, replicas remain active.
* If the **minimum replica count** is reached, no further scaling down occurs.

***

## Scale to zero

If you're just testing your model or anticipate light and inconsistent traffic, scale to zero can save you substantial amounts of money.

Scale to zero means that when a deployed model is not receiving traffic, it scales down to zero replicas. When the model is called, Baseten spins up a new instance to serve model requests.

To turn on scale to zero, just set a deployment's minimum replica count to zero. Scale to zero is enabled by default in the standard autoscaling config.

<Note>
  Models that have not received any traffic for more than **two weeks** will be
  automatically deactivated. These models will need to be activated manually
  before they can serve requests again. For **production deployments this threshold
  is two months**.
</Note>

***

## Cold starts

A **cold start** is the time required to **initialize a new replica** when scaling up. Cold starts impact:

* **Scaled-to-zero deployments** → The first request must wait for a new replica to start.
* **Scaling events** → When traffic spikes and a deployment requires more replicas.

### Cold start optimizations

**Network accelerator**

Baseten speeds up model loading from **Hugging Face, CloudFront, S3, and OpenAI** using parallelized **byte-range downloads**, reducing cold start delays.

**Cold start pods**

Baseten pre-warms specialized **cold start pods** to accelerate loading times. These pods appear in logs as `[Coldboost]`.

```md Example coldboost log line theme={"system"}
Oct 09 9:20:25pm [Coldboost] Completed model.load() execution in 12650 ms
```

**Model Image streaming and optimization**

To further reduce initialization latency, Baseten uses **image streaming** to optimize container startup.

1. **Initial non-optimized image:**
   When a model is first deployed, a standard image is built without optimization. During this stage, the runtime monitors which parts of the image are accessed during startup and inference.

2. **Call graph–based optimization:**
   Baseten analyzes the model’s call graph to identify which layers, weights, and binaries are actually needed during initialization. This information drives creation of an **optimized image**.

3. **Prefetch and lazy fetch:**
   The optimized image is split into two content groups:
   * **Prefetched content:** Frequently accessed layers and dependencies are loaded eagerly at container start.
   * **Lazy-fetched content:** Less critical data is fetched on demand, reducing initial I/O overhead.

4. **Streaming-enabled image pull:**
   Images optimized through this process are streamed into the node filesystem during startup, allowing the model to begin loading before the entire image is downloaded.
   Pulling an optimized image appears in logs as:

   ```md Example streaming image pull log line theme={"system"}
   Successfully pulled streaming-enabled image in 15.851s. Image size: 32 GB.
   ```

***

## Autoscaling for development deployments

Development deployments have **fixed autoscaling constraints** to optimize for **live reload workflows**:

* **Min replicas:** `0`
* **Max replicas:** `1`
* **Autoscaling window:** `60 seconds`
* **Scale down delay:** `900 seconds (15 min)`
* **Concurrency target:** `1 request`

To enable full autoscaling, **promote the deployment and environment** like production.


# Concepts
Source: https://docs.baseten.co/deployment/concepts



Baseten provides a flexible and scalable infrastructure for deploying and managing machine learning models. This page introduces key concepts - [deployments](/deployment/deployments), [environments](/deployment/environments), [resources](/deployment/resources), and [autoscaling](/deployment/autoscaling) — that shape how models are served, tested, and optimized for performance and cost efficiency.

## Deployments

[Deployments](/deployment/deployments) define how models are served, scaled, and updated. They optimize resource use with autoscaling, scaling to zero, and controlled traffic shifts while ensuring minimal downtime. Deployments can be deactivated to pause resource usage or deleted permanently when no longer needed.

<img />

## Environments

[Environments](/deployment/environments) group deployments, providing stable endpoints and autoscaling to manage model release cycles. They enable structured testing, controlled rollouts, and seamless transitions between staging and production. Each environment maintains its own settings and metrics, ensuring reliable and scalable deployments.

<img />

## Resources

[Resources](/deployment/resources) define the hardware allocated to a model server, balancing performance and cost. Choosing the right instance type ensures efficient inference without unnecessary overhead. Resources can be set before deployment in Truss or adjusted later in the model dashboard to match workload demands.

<img />

## Autoscaling

[Autoscaling](/deployment/autoscaling) dynamically adjusts model resources to handle traffic fluctuations efficiently while minimizing costs. Deployments scale between a defined range of replicas based on demand, with settings for concurrency, scaling speed, and scale-to-zero for low-traffic models. Optimizations like network acceleration and cold start pods ensure fast response times even when scaling up from zero.

<img />


# Deployments
Source: https://docs.baseten.co/deployment/deployments

Deploy, manage, and scale machine learning models with Baseten

A **deployment** in Baseten is a **containerized instance of a model** that serves inference requests via an API endpoint. Deployments exist independently but can be **promoted to an environment** for structured access and scaling.

Every deployment is **automatically wrapped in a REST API**. Once deployed, models can be queried with a simple HTTP request:

```python theme={"system"}
import requests

resp = requests.post(
    "https://model-{modelID}.api.baseten.co/deployment/[{deploymentID}]/predict",
    headers={"Authorization": "Api-Key YOUR_API_KEY"},
    json={'text': 'Hello my name is {MASK}'},
)

print(resp.json())
```

[Learn more about running inference on your deployment](/inference/calling-your-model)

***

# Development deployment

A **development deployment** is a mutable instance designed for rapid iteration. It is always in the **development state** and cannot be renamed or detached from it.

Key characteristics:

* **Live reload** enables direct updates without redeployment.
* **Single replica, scales to zero** when idle to conserve compute resources.
* **No autoscaling or zero-downtime updates.**
* **Can be promoted** to create a persistent deployment.

Once promoted, the development deployment transitions to a **deployment** and can optionally be promoted to an environment.

***

# Environments and promotion

Environments provide **logical isolation** for managing deployments but are **not required** for a deployment to function. A deployment can be executed independently or promoted to an environment for controlled traffic allocation and scaling.

* The **production environment** exists by default.
* **Custom environments** (e.g., staging) can be created for specific workflows.
* **Promoting a deployment does not modify its behavior**, only its routing and lifecycle management.

## Canary deployments

Canary deployments support **incremental traffic shifting** to a new deployment, mitigating risk during rollouts.

* Traffic is routed in **10 evenly distributed stages** over a configurable time window.
* Traffic only begins to shift once the new deployment reaches the min replica count of the current production model.
* Autoscaling dynamically adjusts to real-time demand.
* Canary rollouts can be enabled or canceled via the UI or [REST API](/reference/management-api/environments/update-an-environments-settings).

***

# Managing Deployments

## Naming deployments

By default, deployments of a model are named `deployment-1`, `deployment-2`, and so forth sequentially. You can instead give deployments custom names via two methods:

1. While creating the deployment, using a [command line argument in truss push](/reference/sdk/truss#deploying-a-model).
2. After creating the deployment, in the model management page within your Baseten dashboard.

Renaming deployments is purely aesthetic and does not affect model management API paths, which work via model and deployment IDs.

## Deactivating a deployment

A deployment can be deactivated to suspend inference execution while preserving configuration.

* **Remains visible in the dashboard.**
* **Consumes no compute resources** but can be reactivated anytime.
* **API requests return a 404 error while deactivated.**

For demand-driven deployments, consider [autoscaling with scale to zero](/reference/management-api/deployments/autoscaling/updates-a-deployments-autoscaling-settings).

## Deleting deployments

Deployments can be **permanently deleted**, but production deployments must be replaced before deletion.

* **Deleted deployments are purged from the dashboard** but retained in usage logs.
* **All associated compute resources are released.**
* **API requests return a 404 error post-deletion.**

<Warning>
  Deletion is irreversible — use deactivation if retention is required.
</Warning>


# Environments
Source: https://docs.baseten.co/deployment/environments

Manage your model’s release cycles with environments.

Environments provide structured management for deployments, ensuring controlled rollouts, stable endpoints, and autoscaling. They help teams stage, test, and release models without affecting production traffic.

<img />

Deployments can be promoted to an environment (e.g., "staging") to validate outputs before moving to production, allowing for safer model iteration and evaluation.

***

## Using Environments to manage deployments

Environments support **structured validation** before promoting a deployment, including:

* **Automated tests and evaluations**
* **Manual testing in pre-production**
* **Gradual traffic shifts with canary deployments**
* **Shadow serving for real-world analysis**

Promoting a deployment ensures it inherits **environment-specific scaling and monitoring settings**, such as:

* **Dedicated API endpoint** → [Predict API Reference](/reference/inference-api/overview#predict-endpoints)
* **Autoscaling controls** → Scale behavior is managed per environment.
* **Traffic ramp-up** → Enable [canary rollouts](/deployment/deployments#canary-deployments).
* **Monitoring and metrics** → [Export environment metrics](/observability/export-metrics/overview).

A **production environment** operates like any other environment but has restrictions:

* **It cannot be deleted** unless the entire model is removed.
* **You cannot create additional environments named "production."**

***

## Creating custom environments

In addition to the standard **production** environment, you can create as many custom environments as needed. There are two ways to create a custom environment:

1. In the model management page on the Baseten dashboard.
2. Via the [create environment endpoint](/reference/management-api/environments/create-an-environment) in the model management API.

***

## Promoting deployments to environments

When a deployment is promoted, Baseten follows a **three-step process**:

1. A **new deployment** is created with a unique deployment ID.
2. The deployment **initializes resources** and becomes active.
3. The new deployment **replaces the existing deployment** in that environment.

* If there was **no previous deployment, default autoscaling settings** are applied.
* If a **previous deployment existed**, the new one **inherits autoscaling settings**, and the old deployment is **demoted and scales to zero**.

### Promoting a Published Deployment

If a **published deployment** (not a development deployment) is promoted:

* Its **autoscaling settings are updated** to match the environment.
* If **inactive**, it must be **activated** before promotion.

Previous deployments are **demoted but remain in the system**, retaining their **deployment ID and scaling behavior**.

***

## Deploying directly to an environment

You can **skip development stage** and deploy directly to an environment by specifying `--environment` in `truss push`:

```sh theme={"system"}
cd my_model/
truss push --environment {environment_name}
```

<Note>Only one active promotion per environment is allowed at a time.</Note>

***

## Accessing environments in your code

The **environment name** is available in `model.py` via the `environment` keyword argument:

```python theme={"system"}
def __init__(self, **kwargs):
    self._environment = kwargs["environment"]
```

To ensure the **environment variable remains updated**, enable\*\* "Re-deploy when promoting" \*\*in the UI or via the [REST API](/reference/management-api/environments/update-an-environments-settings). This guarantees the environment is fully initialized after a promotion.

***

## Deleting environments

Environments can be deleted, **except for production**. To remove a **production deployment**, first **promote another deployment to production** or delete the entire model.

* **Deleted environments are removed from the overview** but remain in billing history.
* **They do not consume resources** after deletion.
* **API requests to a deleted environment return a 404 error.**

<Warning>Deletion is permanent - consider deactivation instead.</Warning>


# Resources
Source: https://docs.baseten.co/deployment/resources

Manage and configure model resources

Every AI/ML model on Baseten runs on an **instance**, a dedicated set of hardware allocated to the model server. Selecting the right instance type ensures **optimal performance** while controlling **compute costs**.

* **Insufficient resources**: Slow inference or failures.
* **Excess resources**: Higher costs without added benefit.

<img />

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


# Binary IO
Source: https://docs.baseten.co/development/chain/binaryio

Performant serialization of numeric data

Numeric data or audio/video are most efficiently transmitted as bytes.

Other representations such as JSON or base64 encoding lose precision, add
significant parsing overhead and increase message sizes (e.g. \~33% increase
for base64 encoding).

Chains extends the JSON-centred pydantic ecosystem with two ways how you can
include binary data: numpy array support and raw bytes.

## Numpy `ndarray` support

<Tip>
  Once you have your data represented as a numpy array, you can easily (and
  often without copying) convert it to `torch`, `tensorflow` or other common
  numeric library's objects.
</Tip>

To include numpy arrays in a pydantic model, chains has a special field type
implementation `NumpyArrayField`. For example:

```python theme={"system"}
import numpy as np
import pydantic

from truss_chains import pydantic_numpy


class DataModel(pydantic.BaseModel):
    some_numbers: pydantic_numpy.NumpyArrayField
    other_field: str
    ...


numbers = np.random.random((3, 2))
data = DataModel(some_numbers=numbers, other_field="Example")
print(data)
# some_numbers=NumpyArrayField(shape=(3, 2), dtype=float64, data=[
#   [0.39595027 0.23837526]
#   [0.56714894 0.61244946]
#   [0.45821942 0.42464844]])
# other_field='Example'
```

`NumpyArrayField` is a wrapper around the actual numpy array. Inside your
python code, you can work with its `array` attribute:

```python theme={"system"}
data.some_numbers.array += 10
# some_numbers=NumpyArrayField(shape=(3, 2), dtype=float64, data=[
#   [10.39595027 10.23837526]
#   [10.56714894 10.61244946]
#   [10.45821942 10.42464844]])
# other_field='Example'
```

The interesting part is, how it serializes when making communicating between
Chainlets or with a client.
It can work in two modes: JSON and binary.

### Binary

As a JSON alternative that supports byte data, Chains uses `msgpack` (with
`msgpack_numpy`) to serialize the dict representation.

For Chainlet-Chainlet RPCs this is done automatically for you by enabling binary
mode of the dependency Chainlets, see
[all options](/reference/sdk/chains#truss-chains-depends):

```python theme={"system"}
import truss_chains as chains


class Worker(chains.ChainletBase):
    async def run_remote(self, data: DataModel) -> DataModel:
        data.some_numbers.array += 10
        return data


class Consumer(chains.ChainletBase):

    def __init__(self, worker=chains.depends(Worker, use_binary=True)):
        self._worker = worker

    async def run_remote(self):
        numbers = np.random.random((3, 2))
        data = DataModel(some_numbers=numbers, other_field="Example")
        result = await self._worker.run_remote(data)
```

Now the data is transmitted in a fast and compact way between Chainlets
which often gives performance increases.

### Binary client

If you want to send such data as input to a chain or parse binary output
from a chain, you have to add the `msgpack` serialization client-side:

```python theme={"system"}
import requests
import msgpack
import msgpack_numpy

msgpack_numpy.patch()  # Register hook for numpy.

# Dump to "python" dict and then to binary.
data_dict = data.model_dump(mode="python")
data_bytes = msgpack.dumps(data_dict)

# Set binary content type in request header.
headers = {
    "Content-Type": "application/octet-stream", "Authorization": ...
}

response = requests.post(url, data=data_bytes, headers=headers)
response_dict = msgpack.loads(response.content)
response_model = ResponseModel.model_validate(response_dict)
```

The steps of dumping from a pydantic model and validating the response dict
into a pydantic model can be skipped, if you prefer working with raw dicts
on the client.

<Tip>
  The implementation of `NumpyArrayField` only needs `pydantic`, no other Chains
  dependencies. So you can take that implementation code in isolation and
  integrate it in your client code.
</Tip>

<Warning>
  Some version combinations of `msgpack` and `msgpack_numpy` give errors, we
  know that `msgpack = ">=1.0.2"` and `msgpack-numpy = ">=0.4.8"` work.
</Warning>

### JSON

The JSON-schema to represent the array is a dict of `shape (tuple[int]), 
dtype (str), data_b64 (str)`. E.g.

```python theme={"system"}
print(data.model_dump_json())
'{"some_numbers":{"shape":[3,2],"dtype":"float64", "data_b64":"30d4/rnKJEAsvm...'
```

The base64 data corresponds to `np.ndarray.tobytes()`.

To get back to the array from the JSON string, use the model's
`model_validate_json` method.

As discussed in the beginning, this schema is not performant for numeric data
and only offered as a compatibility layer (JSON does not allow bytes) -
generally prefer the binary format.

# Simple `bytes` fields

It is possible to add a `bytes` field to a pydantic model used in a chain,
or as a plain argument to `run_remote`. This can be useful to include
non-numpy data formats such as images or audio/video snippets.

In this case, the "normal" JSON representation does not work and all
involved requests or Chainlet-Chainlet-invocations must use binary mode.

The same steps as for arrays [above](#binary-client) apply: construct dicts
with `bytes` values and keys corresponding to the `run_remote` argument
names or the field names in the pydantic model. Then use `msgpack` to
serialize and deserialize those dicts.

Don't forget to add `Content-type` headers and that `response.json()` will
not work.


# Concepts
Source: https://docs.baseten.co/development/chain/concepts

Glossary of Chains concepts and terminology

## Chainlet

A Chainlet is the basic building block of Chains. A Chainlet is a Python class
that specifies:

* A set of compute resources.
* A Python environment with software dependencies.
* A typed interface [
  `run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets)
  for other Chainlets to call.

This is the simplest possible Chainlet — only the
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets) method is
required — and we can layer in other concepts to create a more capable Chainlet.

```python theme={"system"}
import truss_chains as chains


class SayHello(chains.ChainletBase):

    async def run_remote(self, name: str) -> str:
        return f"Hello, {name}"
```

You can modularize your code by creating your own chainlet sub-classes,
refer to our [subclassing guide](/development/chain/subclassing).

### Remote configuration

Chainlets are meant for deployment as remote services. Each Chainlet specifies
its own requirements for compute hardware (CPU count, GPU type and count, etc)
and software dependencies (Python libraries or system packages). This
configuration is built into a Docker image automatically as part of the
deployment process.

When no configuration is provided, the Chainlet will be deployed on a basic
instance with one vCPU, 2GB of RAM, no GPU, and a standard set of Python and
system packages.

Configuration is set using the
[`remote_config`](/reference/sdk/chains#remote-configuration) class variable
within the Chainlet:

```python theme={"system"}
import truss_chains as chains


class MyChainlet(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            pip_requirements=["torch==2.3.0", ...]
        ),
        compute=chains.Compute(gpu="H100", ...),
        assets=chains.Assets(secret_keys=["hf_access_token"], ...),
    )
```

To select an exact instance type instead of specifying individual resource fields, use `instance_type`:

```python theme={"system"}
compute=chains.Compute(instance_type="H100:8x80")
```

When `instance_type` is specified, `cpu_count`, `memory`, and `gpu` fields are ignored.

See the
[remote configuration reference](/reference/sdk/chains#remote-configuration)
for a complete list of options.

### Initialization

Chainlets are implemented as classes because we often want to set up expensive
static resources once at startup and then re-use it with each invocation of the
Chainlet. For example, we only want to initialize an AI model and download its
weights once then re-use it every time we run inference.

We do this setup in `__init__()`, which is run exactly once when the Chainlet is
deployed or scaled up.

```python theme={"system"}
import truss_chains as chains


class PhiLLM(chains.ChainletBase):
    def __init__(self) -> None:
        import torch
        import transformers

        self._model = transformers.AutoModelForCausalLM.from_pretrained(
            PHI_HF_MODEL,
            torch_dtype=torch.float16,
            device_map="auto",
        )

        self._tokenizer = transformers.AutoTokenizer.from_pretrained(
            PHI_HF_MODEL,
        )
```

Chainlet initialization also has two important features: context and dependency
injection of other Chainlets, explained below.

#### Context (access information)

You can add
[
`DeploymentContext`](/reference/sdk/chains#class-truss-chains-deploymentcontext)
object as an optional argument to the `__init__`-method of a Chainlet.
This allows you to use secrets within your Chainlet, such as using
a `hf_access_token` to access a gated model on Hugging Face (note that when
using secrets, they also need to be added to the `assets`).

```python theme={"system"}
import truss_chains as chains


class MistralLLM(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        ...
    assets = chains.Assets(secret_keys=["hf_access_token"], ...),
    )

    def __init__(
        self,
        # Adding the `context` argument, allows us to access secrets
        context: chains.DeploymentContext = chains.depends_context(),
    ) -> None:
        import transformers

        # Using the secret from context to access a gated model on HF
        self._model = transformers.AutoModelForCausalLM.from_pretrained(
            "mistralai/Mistral-7B-Instruct-v0.2",
            use_auth_token=context.secrets["hf_access_token"],
        )
```

#### Depends (call other Chainlets)

The Chains framework uses the
[`chains.depends()`](/reference/sdk/chains#truss-chains-depends) function in
Chainlets' `__init__()` method to track the dependency relationship between
different Chainlets within a Chain.

This syntax, inspired by dependency injection, is used to translate local Python
function calls into calls to the remote Chainlets in production.

Once a dependency Chainlet is added with
[`chains.depends()`](/reference/sdk/chains#truss-chains-depends), its
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets) method can
call this dependency Chainlet, e.g. below `HelloAll` we can make calls to
`SayHello`:

```python theme={"system"}
import truss_chains as chains


class HelloAll(chains.ChainletBase):

    def __init__(self, say_hello_chainlet=chains.depends(SayHello)) -> None:
        self._say_hello = say_hello_chainlet

    async def run_remote(self, names: list[str]) -> str:
        output = []
        for name in names:
            output.append(self._say_hello.run_remote(name))
        return "\n".join(output)
```

## Run remote (chaining Chainlets)

The `run_remote()` method is run each time the Chainlet is called. It is the
sole public interface for the Chainlet (though you can have as many private
helper functions as you want) and its inputs and outputs must have type
annotations.

In `run_remote()` you implement the actual work of the Chainlet, such as model
inference or data chunking:

```python theme={"system"}
import truss_chains as chains


class PhiLLM(chains.ChainletBase):
    async def run_remote(self, messages: Messages) -> str:
        import torch

        model_inputs = await self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = await self._tokenizer(model_inputs, return_tensors="pt")
        input_ids = inputs["input_ids"].to("cuda")
        with torch.no_grad():
            outputs = await self._model.generate(
                input_ids=input_ids, **self._generate_args)
            output_text = await self._tokenizer.decode(
                outputs[0], skip_special_tokens=True)
        return output_text
```

We recommend implementing this as an `async` method and using async APIs for
doing all the work (e.g. downloads, vLLM or TRT inference).

It is possible to stream results back, see our
[streaming guide](/development/chain/streaming).

<Tip>
  If `run_remote()` makes calls to other Chainlets, e.g. invoking a dependency
  Chainlet for each element in a list, you can benefit from concurrent
  execution, by making the `run_remote()` an `async` method and starting the
  calls as concurrent tasks
  `asyncio.ensure_future(self._dep_chainlet.run_remote(...))`.
</Tip>

## Entrypoint

The entrypoint is called directly from the deployed Chain's API endpoint and
kicks off the entire chain. The entrypoint is also responsible for returning the
final result back to the client.

Using the
[`@chains.mark_entrypoint`](/reference/sdk/chains#truss-chains-mark-entrypoint)
decorator, one Chainlet within a file is set as the entrypoint to the chain.

```python theme={"system"}
@chains.mark_entrypoint
class HelloAll(chains.ChainletBase):
```

Optionally you can also set a Chain display name (not to be confused with
Chainlet display name) with this decorator:

```python theme={"system"}
@chains.mark_entrypoint("My Awesome Chain")
class HelloAll(chains.ChainletBase):
```

## I/O and `pydantic` data types

To make orchestrating multiple remotely deployed services possible, Chains
relies heavily on typed inputs and outputs. Values must be serialized to a safe
exchange format to be sent over the network.

The Chains framework uses the type annotations to infer how data should be
serialized and currently is restricted to types that are JSON compatible. Types
can be:

* Direct type annotations for simple types such as `int`, `float`,
  or `list[str]`.
* Pydantic models to define a schema for nested data structures or multiple
  arguments.

An example of pydantic input and output types for a Chainlet is given below:

```python theme={"system"}
import enum
import pydantic


class Modes(enum.Enum):
    MODE_0 = "MODE_0"
    MODE_1 = "MODE_1"


class SplitTextInput(pydantic.BaseModel):
    data: str
    num_partitions: int
    mode: Modes


class SplitTextOutput(pydantic.BaseModel):
    parts: list[str]
    part_lens: list[int]
```

Refer to the [pydantic docs](https://docs.pydantic.dev/latest/) for more
details on how
to define custom pydantic data models.

Also refer to the [guide](/development/chain/binaryio) about efficient integration
of binary and numeric data.

## Chains compared to Truss

<Accordion title="Tips for Truss users" icon="lightbulb">
  Chains is an alternate SDK for packaging and deploying AI models. It carries over many features and concepts from Truss and gives you access to the benefits of Baseten (resource provisioning, autoscaling, fast cold starts, etc), but it is not a 1-1 replacement for Truss.

  Here are some key differences:

  * Rather than running `truss init` and creating a Truss in a directory, a Chain
    is a single file, giving you more flexibility for implementing multi-step
    model inference. Create an example with `truss chains init`.
  * Configuration is done inline in typed Python code rather than in a
    `config.yaml` file.
  * While Chainlets are converted to Truss models when run on Baseten,
    `Chainlet != TrussModel`.

  Chains is designed for compatibility and incremental adoption, with a stub
  function for wrapping existing deployed models.
</Accordion>


# Deploy
Source: https://docs.baseten.co/development/chain/deploy

Deploy your Chain on Baseten

Deploying a Chain is an atomic action that deploys every Chainlet
within the Chain. Each Chainlet specifies its own remote
environment — hardware resources, Python and system dependencies, autoscaling
settings.

### Development

The default behavior for pushing a chain is to create a development deployment:

```sh theme={"system"}
truss chains push ./my_chain.py
```

Where `my_chain.py` contains the entrypoint Chainlet for your Chain.

Development deployments are intended for testing and can't scale past one
replica. Each time you make a development deployment, it overwrites the existing
development deployment.

Development deployments support rapid iteration with `watch` - see [above
guide](/development/chain/watch).

### 🆕 Environments

To deploy a Chain to an environment, run:

```sh theme={"system"}
truss chains push ./my_chain.py --environment {env_name}
```

Environments are intended for live traffic and have access to full
autoscaling settings. Each time you deploy to an environment, a new deployment is
created. Once the new deployment is live, it replaces the previous deployment,
which is relegated to the published deployments list.
[Learn more](/deployment/environments) about environments.


# Architecture and design
Source: https://docs.baseten.co/development/chain/design

How to structure your Chainlets

A Chain is composed of multiple connected Chainlets working together to perform
a task.

For example, the Chain in the diagram below takes a large audio file as input.
Then it splits it into smaller chunks, transcribes each chunk in parallel
(reducing the end-to-end latency), and finally aggregates and returns the
results.

<Frame>
  <img />
</Frame>

To build an efficient Chain, we recommend drafting your high level
structure as a flowchart or diagram. This can help you identifying
parallelizable units of work and steps that need different (model/hardware)
resources.

If one Chainlet creates many "sub-tasks" by calling other dependency
Chainlets (e.g. in a loop over partial work items),
these calls should be done as `aynscio`-tasks that run concurrently.
That way you get the most out of the parallelism that Chains offers. This
design pattern is extensively used in the
[audio transcription example](/examples/chains-audio-transcription).

<Warning>
  While using `asyncio` is essential for performance, it can also be tricky.
  Here are a few caveats to look out for:

  * Executing operations in an async function that block the event loop for
    more than a fraction of a second. This hinders the "flow" of processing
    requests concurrently and starting RPCs to other Chainlets. Ideally use
    native async APIs. Frameworks like vLLM or triton server offer such APIs,
    similarly file downloads can be made async and you might find
    [`AsyncBatcher`](https://github.com/hussein-awala/async-batcher) useful.
    If there is no async support, consider running blocking code in a
    thread/process pool (as an attribute of a Chainlet).
  * Creating async tasks (e.g. with `asyncio.ensure_future`) does not start
    the task *immediately*. In particular, when starting several tasks in a loop,
    `ensure_future` must be alternated with operations that yield to the event
    loop that, so the task can be started. If the loop is not `async for` or
    contains other `await` statements, a "dummy" await can be added, for example
    `await asyncio.sleep(0)`. This allows the tasks to be started concurrently.
</Warning>


# Engine-Builder LLM Models
Source: https://docs.baseten.co/development/chain/engine-builder-models

Engine-Builder LLM models are pre-trained models that are optimized for specific inference tasks.

Baseten's [Engine-Builder](/engines/engine-builder-llm/overview) enables the deployment of optimized model inference engines. Currently, it supports TensorRT-LLM. Truss Chains allows seamless integration of these engines into structured workflows. This guide provides a quick entry point for Chains users.

## LLama 7B Example

Use the `EngineBuilderLLMChainlet` baseclass to configure an LLM engine. The additional `engine_builder_config` field specifies model architecture, repository, and engine parameters and more, the full options are detailed in the [Engine-Builder configuration guide](/engines/engine-builder-llm/engine-builder-config).

```python theme={"system"}
import truss_chains as chains
from truss.base import trt_llm_config, truss_config

class Llama7BChainlet(chains.EngineBuilderLLMChainlet):
    remote_config = chains.RemoteConfig(
        compute=chains.Compute(gpu=truss_config.Accelerator.H100),
        assets=chains.Assets(secret_keys=["hf_access_token"]),
    )
    engine_builder_config = truss_config.TRTLLMConfiguration(
        build=trt_llm_config.TrussTRTLLMBuildConfiguration(
            base_model=trt_llm_config.TrussTRTLLMModel.LLAMA,
            checkpoint_repository=trt_llm_config.CheckpointRepository(
                source=trt_llm_config.CheckpointSource.HF,
                repo="meta-llama/Llama-3.1-8B-Instruct",
            ),
            max_batch_size=8,
            max_seq_len=4096,
            tensor_parallel_count=1,
        )
    )
```

## Differences from Standard Chainlets

* No `run_remote` implementation: Unlike regular Chainlets, `EngineBuilderLLMChainlet` does not require users to implement `run_remote()`. Instead, it automatically wires into the deployed engine’s API. All LLM Chainlets have the same function signature: `chains.EngineBuilderLLMInput` as input and a stream (`AsyncIterator`) of strings as output. Likewise `EngineBuilderLLMChainlet`s can only be used as dependencies, but not have dependencies themselves.
* No `run_local` ([guide](/development/chain/localdev)) and `watch` ([guide](/development/chain/watch)) Standard Chains support a local debugging mode and watch. However, when using `EngineBuilderLLMChainlet`, local execution is not available, and testing must be done after deployment.
  For a faster dev loop of the rest of your chain (everything except the engine builder chainlet) you can substitute those chainlets with stubs like you can do for an already deployed truss model \[[guide](/development/chain/stub)].

## Integrate the Engine-Builder Chainlet

After defining an `EngineBuilderLLMInput` like `Llama7BChainlet` above, you can use it as a dependency in other conventional chainlets:

```python theme={"system"}
from typing import AsyncIterator
import truss_chains as chains

@chains.mark_entrypoint
class TestController(chains.ChainletBase):
    """Example using the Engine-Builder Chainlet in another Chainlet."""

    def __init__(self, llm=chains.depends(Llama7BChainlet)) -> None:
        self._llm = llm

    async def run_remote(self, prompt: str) -> AsyncIterator[str]:
        messages = [{"role": "user", "content": prompt}]
        llm_input = chains.EngineBuilderLLMInput(messages=messages)
        async for chunk in self._llm.run_remote(llm_input):
            yield chunk
```


# Error Handling
Source: https://docs.baseten.co/development/chain/errorhandling

Understanding and handling Chains errors

Error handling in Chains follows the principle that the root cause "bubbles
up" until the entrypoint - which returns an error response. Similarly to how
python stack traces contain all the layers from where an exception was raised
up until the main function.

Consider the case of a Chain where the entrypoint calls `run_remote` of a
Chainlet named `TextToNum` and this in turn invokes `TextReplicator`. The
respective `run_remote` methods might also use other helper functions that
appear in the call stack.

Below is an example stack trace that shows how the root cause (a
`ValueError`) is propagated up to the entrypoint's `run_remote` method (this
is what you would see as an error log):

```
Chainlet-Traceback (most recent call last):
  File "/packages/itest_chain.py", line 132, in run_remote
    value = self._accumulate_parts(text_parts.parts)
  File "/packages/itest_chain.py", line 144, in _accumulate_parts
    value += self._text_to_num.run_remote(part)
ValueError: (showing chained remote errors, root error at the bottom)
├─ Error in dependency Chainlet `TextToNum`:
│   Chainlet-Traceback (most recent call last):
│     File "/packages/itest_chain.py", line 87, in run_remote
│       generated_text = self._replicator.run_remote(data)
│   ValueError: (showing chained remote errors, root error at the bottom)
│   ├─ Error in dependency Chainlet `TextReplicator`:
│   │   Chainlet-Traceback (most recent call last):
│   │     File "/packages/itest_chain.py", line 52, in run_remote
│   │       validate_data(data)
│   │     File "/packages/itest_chain.py", line 36, in validate_data
│   │       raise ValueError(f"This input is too long: {len(data)}.")
╰   ╰   ValueError: This input is too long: 100.
```

## Exception handling and retries

Above stack trace is what you see if you don't catch the exception. It is
possible to add error handling around each remote Chainlet invocation.

Chains tries to raise the same exception class on the *caller* Chainlet as was
raised in the *dependency* Chainlet.

* Builtin exceptions (e.g. `ValueError`) always work.
* Custom or third-party exceptions (e.g. from `torch`) can be only raised
  in the caller if they are included in the dependencies of the caller as
  well. If the exception class cannot be resolved, a
  `GenericRemoteException` is raised instead.

Note that the *message* of re-raised exceptions is the concatenation
of the original message and the formatted stack trace of the dependency
Chainlet.

In some cases it might make sense to simply retry a remote invocation (e.g.
if it failed due to some transient problems like networking or any "flaky"
parts). `depends` can be configured with additional
[options](/reference/sdk/chains#truss-chains-depends) for that.

Below example shows how you can add automatic retries and error handling for
the call to `TextReplicator` in `TextToNum`:

```python theme={"system"}
import truss_chains as chains


class TextToNum(chains.ChainletBase):

    def __init__(
        self,
        replicator: TextReplicator = chains.depends(TextReplicator, retries=3),
    ) -> None:
        self._replicator = replicator
    
    async def run_remote(self, data: ...):
        try:
            generated_text = await self._replicator.run_remote(data)
        except ValueError:
            ...  # Handle error.

```

## Stack filtering

The stack trace is intended to show the user implemented code in
`run_remote` (and user implemented helper functions). Under the
hood, the calls from one Chainlet to another go through an HTTP
connection, managed by the Chains framework. And each Chainlet itself is
run as a FastAPI server with several layers of request handling code "above".

In order to provide concise, readable stacks, all of this non-user code is
filtered out.


# Your first Chain
Source: https://docs.baseten.co/development/chain/getting-started

Build and deploy two example Chains

This quickstart guide contains instructions for creating two Chains:

1. A simple CPU-only “hello world”-Chain.
2. A Chain that implements Phi-3 Mini and uses it to write poems.

## Prerequisites

To use Chains, install a recent Truss version and ensure pydantic is v2:

```bash theme={"system"}
pip install --upgrade truss 'pydantic>=2.0.0'
```

<Accordion title="Help for setting up a clean development environment">
  Truss requires python `>=3.9,<3.15`. To set up a fresh development environment,
  you can use the following commands, creating a environment named `chains_env`
  using `pyenv`:

  ```bash theme={"system"}
  curl https://pyenv.run | bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  source ~/.bashrc
  pyenv install 3.11.0
  ENV_NAME="chains_env"
  pyenv virtualenv 3.11.0 $ENV_NAME
  pyenv activate $ENV_NAME
  pip install --upgrade truss 'pydantic>=2.0.0'
  ```
</Accordion>

To deploy Chains remotely, you also need a
[Baseten account](https://app.baseten.co/signup).
It is handy to export your API key to the current shell session or permanently in your `.bashrc`:

```bash ~/.bashrc theme={"system"}
export BASETEN_API_KEY="nPh8..."
```

## Example: Hello World

Chains are written in Python files. In your working directory,
create `hello_chain/hello.py`:

```sh theme={"system"}
mkdir hello_chain
cd hello_chain
touch hello.py
```

In the file, we'll specify a basic Chain. It has two Chainlets:

* `HelloWorld`, the entrypoint, which handles the input and output.
* `RandInt`, which generates a random integer. It is used a as a dependency
  by `HelloWorld`.

Via the entrypoint, the Chain takes a maximum value and returns the string "
Hello World!" repeated a
variable number of times.

```python hello.py theme={"system"}
import random
import truss_chains as chains


class RandInt(chains.ChainletBase):
    async def run_remote(self, max_value: int) -> int:
        return random.randint(1, max_value)


@chains.mark_entrypoint
class HelloWorld(chains.ChainletBase):
    def __init__(self, rand_int=chains.depends(RandInt, retries=3)) -> None:
        self._rand_int = rand_int

    async def run_remote(self, max_value: int) -> str:
        num_repetitions = await self._rand_int.run_remote(max_value)
        return "Hello World! " * num_repetitions
```

### The Chainlet class-contract

Exactly one Chainlet must be marked as the entrypoint with
the [`@chains.mark_entrypoint`](/reference/sdk/chains#truss-chains-mark-entrypoint)
decorator. This Chainlet is responsible for
handling public-facing input and output for the whole Chain in response to an
API call.

A Chainlet class has a single public method,
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets), which is
the API
endpoint for the entrypoint Chainlet and the function that other Chainlets can
use as a dependency. The
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets)
method must be fully type-annotated
with <Tooltip>primitive python
types</Tooltip>
or <Tooltip>[pydantic models](https://docs.pydantic.dev/latest/)</Tooltip>.

Chainlets cannot be <Tooltip>naively</Tooltip> instantiated. The only correct usages are:

1. Make one Chainlet depend on another one via the
   [`chains.depends()`](/reference/sdk/chains#truss-chains-depends) directive
   as an `__init__`-argument as shown above for the `RandInt` Chainlet.
2. In the [local debugging mode](/development/chain/localdev#test-a-chain-locally).

Beyond that, you can structure your code as you like, with private methods,
imports from other files, and so forth.

<Warning>
  Keep in mind that Chainlets are intended for distributed, replicated, remote
  execution, so using global variables, global state, and certain Python
  features like importing modules dynamically at runtime should be avoided as
  they may not work as intended.
</Warning>

### Deploy your Chain to Baseten

To deploy your Chain to Baseten, run:

```bash theme={"system"}
truss chains push hello.py
```

The deploy command results in an output like this:

```
                  ⛓️   HelloWorld - Chainlets  ⛓️
╭──────────────────────┬─────────────────────────┬─────────────╮
│ Status               │ Name                    │ Logs URL    │
├──────────────────────┼─────────────────────────┼─────────────┤
│  💚 ACTIVE           │ HelloWorld (entrypoint) │ https://... │
├──────────────────────┼─────────────────────────┼─────────────┤
│  💚 ACTIVE           │ RandInt (dep)           │ https://... │
╰──────────────────────┴─────────────────────────┴─────────────╯
Deployment succeeded.
You can run the chain with:
curl -X POST 'https://chain-.../run_remote' \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '<JSON_INPUT>'
```

Wait for the status to turn to `ACTIVE` and test invoking your Chain (replace
`$INVOCATION_URL` in below command):

```bash theme={"system"}
curl -X POST $INVOCATION_URL \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -d '{"max_value": 10}'
# "Hello World! Hello World! Hello World! "
```

## Example: Poetry with LLMs

Our second example also has two Chainlets, but is somewhat more complex and
realistic. The Chainlets are:

* `PoemGenerator`, the entrypoint, which handles the input and output and
  orchestrates calls to the LLM.
* `PhiLLM`, which runs inference on Phi-3 Mini.

This Chain takes a list of words and returns a poem about each word, written by
Phi-3. Here's the architecture:

<Frame>
  <img />
</Frame>

We build this Chain in a new working directory (if you are still inside
`hello_chain/`, go up one level with `cd ..` first):

```sh theme={"system"}
mkdir poetry_chain
cd poetry_chain
touch poems.py
```

<Tip>
  A similar end-to-end code example, using Mistral as an LLM, is available in
  the [examples
  repo](https://github.com/basetenlabs/model/tree/main/truss-chains/examples/mistral).
</Tip>

### Building the LLM Chainlet

The main difference between this Chain and the previous one is that we now have
an LLM that needs a GPU and more complex dependencies.

Copy the following code into `poems.py`:

```python poems.py theme={"system"}
import asyncio
from typing import List

import pydantic
import truss_chains as chains
from truss import truss_config

PHI_HF_MODEL = "microsoft/Phi-3-mini-4k-instruct"
# This configures to cache model weights from the hunggingface repo
# in the docker image that is used for deploying the Chainlet.
PHI_CACHE = truss_config.ModelRepo(
    repo_id=PHI_HF_MODEL, allow_patterns=["*.json", "*.safetensors", ".model"]
)


class Messages(pydantic.BaseModel):
    messages: List[dict[str, str]]


class PhiLLM(chains.ChainletBase):
    # `remote_config` defines the resources required for this chainlet.
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            # The phi model needs some extra python packages.
            pip_requirements=[
                "accelerate==0.30.1",
                "einops==0.8.0",
                "transformers==4.41.2",
                "torch==2.3.0",
            ]
        ),
        # The phi model needs a GPU and more CPUs.
        compute=chains.Compute(cpu_count=2, gpu="T4"),
        # Cache the model weights in the image
        assets=chains.Assets(cached=[PHI_CACHE]),
    )

    def __init__(self) -> None:
        # Note the imports of the *specific* python requirements are
        # pushed down to here. This code will only be executed on the
        # remotely deployed Chainlet, not in the local environment,
        # so we don't need to install these packages in the local
        # dev environment.
        import torch
        import transformers

        self._model = transformers.AutoModelForCausalLM.from_pretrained(
            PHI_HF_MODEL,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        self._tokenizer = transformers.AutoTokenizer.from_pretrained(
            PHI_HF_MODEL,
        )
        self._generate_args = {
            "max_new_tokens"      : 512,
            "temperature"         : 1.0,
            "top_p"               : 0.95,
            "top_k"               : 50,
            "repetition_penalty"  : 1.0,
            "no_repeat_ngram_size": 0,
            "use_cache"           : True,
            "do_sample"           : True,
            "eos_token_id"        : self._tokenizer.eos_token_id,
            "pad_token_id"        : self._tokenizer.pad_token_id,
        }

    async def run_remote(self, messages: Messages) -> str:
        import torch

        model_inputs = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self._tokenizer(model_inputs, return_tensors="pt")
        input_ids = inputs["input_ids"].to("cuda")
        with torch.no_grad():
            outputs = self._model.generate(
                input_ids=input_ids, **self._generate_args)
            output_text = self._tokenizer.decode(
                outputs[0], skip_special_tokens=True)
        return output_text
```

### Building the entrypoint

Now that we have an LLM, we can use it in a poem generator Chainlet. Add the
following code to `poems.py`:

```python poems.py theme={"system"}
import asyncio


@chains.mark_entrypoint
class PoemGenerator(chains.ChainletBase):
    def __init__(self, phi_llm: PhiLLM = chains.depends(PhiLLM)) -> None:
        self._phi_llm = phi_llm

    async def run_remote(self, words: list[str]) -> list[str]:
        tasks = []
        for word in words:
            messages = Messages(
                messages=[
                    {
                        "role"   : "system",
                        "content": (
                            "You are poet who writes short, "
                            "lighthearted, amusing poetry."
                        ),
                    },
                    {"role": "user", "content": f"Write a poem about {word}"},
                ]
            )
            tasks.append(
                asyncio.ensure_future(self._phi_llm.run_remote(messages)))
            await asyncio.sleep(0)  # Yield to event loop, to allow starting tasks.

        return list(await asyncio.gather(*tasks))
```

Note that we use `asyncio.ensure_future` around each RPC to the LLM chainlet.
This makes the current python process start these remote calls concurrently,
i.e. the next call is started before the previous one has finished and we can
minimize our overall runtime. In order to await the results of all calls,
`asyncio.gather` is used which gives us back normal python objects.
If the LLM is hit with many concurrent requests, it can auto-scale up (if
autoscaling is configured). More advanced LLM models have batching capabilities,
so for those even a single instance can serve concurrent request.

### Deploy your Chain to Baseten

To deploy your Chain to Baseten, run:

```bash theme={"system"}
truss chains push poems.py
```

Wait for the status to turn to `ACTIVE` and test invoking your Chain (replace
`$INVOCATION_URL` in below command):

```bash theme={"system"}
curl -X POST $INVOCATION_URL \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '{"words": ["bird", "plane", "superman"]}'
#[[
#"<s> [INST] Generate a poem about: bird [/INST] In the quiet hush of...</s>",
#"<s> [INST] Generate a poem about: plane [/INST] In the vast, boundless...</s>",
#"<s> [INST] Generate a poem about: superman [/INST] In the realm where...</s>"
#]]
```


# Invocation
Source: https://docs.baseten.co/development/chain/invocation

Call your deployed Chain

Once your Chain is deployed, you can call it via its API endpoint. Chains use
the same inference API as models:

* [Environment endpoint](/reference/inference-api/predict-endpoints/environments-run-remote)
* [Development endpoint](/reference/inference-api/predict-endpoints/development-run-remote)
* [Endpoint by ID](/reference/inference-api/predict-endpoints/deployment-run-remote)

Here's an example which calls the development deployment:

```python call_chain.py theme={"system"}
import requests
import os

# From the Chain overview page on Baseten
# E.g. "https://chain-<CHAIN_ID>.api.baseten.co/development/run_remote"
CHAIN_URL = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
# JSON keys and types match the `run_remote` method signature.
data = {...}

resp = requests.post(
    CHAIN_URL,
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data,
)

print(resp.json())
```

### How to pass chain input

The data schema of the inference request corresponds to the function
signature of [`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets)
in your entrypoint Chainlet.

For example, for the Hello Chain, `HelloAll.run_remote()`:

```python theme={"system"}
async def run_remote(self, names: list[str]) -> str:
```

You'd pass the following JSON payload:

```json theme={"system"}
{ "names": ["Marius", "Sid", "Bola"] }
```

I.e. the keys in the JSON record, match the argument names and values
match the types of`run_remote.`

### Async chain inference

Like Truss models, Chains support async invocation. The [guide for
models](/inference/async) applies largely - in particular for how to wrap the
input and set up the webhook to process results.

The following additional points are chains specific:

* Use chain-based URLS:
  * `https://chain-{chain}.api.baseten.co/production/async_run_remote`
  * `https://chain-{chain}.api.baseten.co/development/async_run_remote`
  * `https://chain-{chain}.api.baseten.co/deployment/{deployment}/async_run_remote`.
  * `https://chain-{chain}.api.baseten.co/environments/{env_name}/async_run_remote`.
* Only the entrypoint is invoked asynchronously. Internal Chainlet-Chainlet
  calls run synchronously.


# Local Development
Source: https://docs.baseten.co/development/chain/localdev

Iterating, Debugging, Testing, Mocking

Chains are designed for production in replicated remote deployments. But
alongside that production-ready power, we offer great local development and
deployment experiences.

<Accordion title="The 6 principles behind Chains">
  Chains exists to help you build multi-step, multi-model pipelines. The
  abstractions that Chains introduces are based on six opinionated principles:
  three for architecture and three for developer experience.

  **Architecture principles**

  <Steps>
    <Step title="Atomic components">
      Each step in the pipeline can set its own hardware requirements and
      software dependencies, separating GPU and CPU workloads.
    </Step>

    <Step title="Modular scaling">
      Each component has independent autoscaling parameters for targeted
      resource allocation, removing bottlenecks from your pipelines.
    </Step>

    <Step title="Maximum composability">
      Components specify a single public interface for flexible-but-safe
      composition and are reusable between projects
    </Step>
  </Steps>

  **Developer experience principles**

  <Steps>
    <Step title="Type safety and validation">
      Eliminate entire taxonomies of bugs by writing typed Python code and
      validating inputs, outputs, module initializations, function signatures,
      and even remote server configurations.
    </Step>

    <Step title="Local debugging">
      Seamless local testing and cloud deployments: test Chains locally with
      support for mocking the output of any step and simplify your cloud
      deployment loops by separating large model deployments from quick
      updates to glue code.
    </Step>

    <Step title="Incremental adoption">
      Use Chains to orchestrate existing model deployments, like pre-packaged
      models from Baseten’s model library, alongside new model pipelines built
      entirely within Chains.
    </Step>
  </Steps>
</Accordion>

Locally, a Chain is just Python files in a source tree. While that gives you a
lot of flexibility in how you structure your code, there are some constraints
and rules to follow to ensure successful distributed, remote execution in
production.

<Tip>
  The best thing you can do while developing locally with Chains is to run your
  code frequently, even if you do not have a  `__main__` section: the Chains
  framework runs various validations at
  <Tooltip>module initialization</Tooltip> to help
  you catch issues early.

  Additionally, running `mypy` and fixing reported type errors can help you
  find problems early in a rapid feedback loop, before attempting a (much
  slower) deployment.
</Tip>

<Tip>
  Complementary to the purely local development Chains also has a "watch" mode,
  like Truss, see the [watch guide](/development/chain/watch).
</Tip>

## Test a Chain locally

Let's revisit our "Hello World" Chain:

```python hello_chain/hello.py theme={"system"}
import asyncio
import truss_chains as chains


# This Chainlet does the work
class SayHello(chains.ChainletBase):

    async def run_remote(self, name: str) -> str:
        return f"Hello, {name}"


# This Chainlet orchestrates the work
@chains.mark_entrypoint
class HelloAll(chains.ChainletBase):

    def __init__(self, say_hello_chainlet=chains.depends(SayHello)) -> None:
        self._say_hello = say_hello_chainlet

    async def run_remote(self, names: list[str]) -> str:
        tasks = []
        for name in names:
            tasks.append(asyncio.ensure_future(
                self._say_hello.run_remote(name)))
        
        return "\n".join(await asyncio.gather(*tasks))


# Test the Chain locally
if __name__ == "__main__":
    with chains.run_local():
        hello_chain = HelloAll()
        result = asyncio.get_event_loop().run_until_complete(
            hello_chain.run_remote(["Marius", "Sid", "Bola"]))
        print(result)
```

When the `__main__()` module is run, local instances of the Chainlets are
created, allowing you to test functionality of your chain just by executing the
Python file:

```bash theme={"system"}
cd hello_chain
python hello.py
# Hello, Marius
# Hello, Sid
# Hello, Bola
```

## Mock execution of GPU Chainlets

Using `run_local()` to run your code locally requires that your development
environment have the compute resources and dependencies that each Chainlet
needs. But that often isn't possible when building with AI models.

Chains offers a workaround, mocking, to let you test the coordination and
business logic of your multi-step inference pipeline without worrying about
running the model locally.

The second example in the [getting started guide](/development/chain/getting-started)
implements a Truss Chain for generating poems with Phi-3.

This Chain has two Chainlets:

1. The `PhiLLM` Chainlet, which can run on NVIDIA GPUs such as the L4.
2. The `PoemGenerator` Chainlet, which easily runs on a CPU.

If you have an NVIDIA T4 under your desk, good for you. For the rest of us, we
can mock the `PhiLLM` Chainlet that is infeasible to run locally so that we can
quickly test the `PoemGenerator` Chainlet.

To do this, we define a mock Phi-3 model in our `__main__` module and give it
a [`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets) method that
produces a test output that matches the output type we expect from the real
Chainlet. Then, we inject an instance of this mock Chainlet into our Chain:

```python poems.py theme={"system"}
if __name__ == "__main__":
    class FakePhiLLM:
        async def run_remote(self, prompt: str) -> str:
            return f"Here's a poem about {prompt.split(" ")[-1]}"


    with chains.run_local():
        poem_generator = PoemGenerator(phi_llm=FakePhiLLM())
        result = asyncio.get_event_loop().run_until_complete(
            poem_generator.run_remote(words=["bird", "plane", "superman"]))
        print(result)
```

And run your Python file:

```bash theme={"system"}
python poems.py
# ['Here's a poem about bird', 'Here's a poem about plane', 'Here's a poem about superman']
```

### Typing of mocks

You may notice that the argument `phi_llm` expects a type `PhiLLM`, while we
pass an instance of `FakePhiLLM`. These aren't the same, which is formally a
type error.

However, this works at runtime because we constructed `FakePhiLLM` to
implement the same *protocol* as the real thing. We can make this explicit by
defining a `Protocol` as a type annotation:

```python theme={"system"}
from typing import Protocol


class PhiProtocol(Protocol):
    def run_remote(self, data: str) -> str:
        ...
```

and changing the argument type in `PoemGenerator`:

```python theme={"system"}
@chains.mark_entrypoint
class PoemGenerator(chains.ChainletBase):
    def __init__(self, phi_llm: PhiProtocol = chains.depends(PhiLLM)) -> None:
        self._phi_llm = phi_llm
```

This is a bit more work and not needed to execute the code, but it shows how
typing consistency can be achieved - if desired.


# Overview
Source: https://docs.baseten.co/development/chain/overview



Chains is a framework for building robust, performant multi-step and multi-model
inference pipelines and deploying them to production. It addresses the common
challenges of managing latency, cost and dependencies for complex workflows,
while leveraging Truss’ existing battle-tested performance, reliability and
developer toolkit.

<video />

# User Guides

Guides focus on specific features and use cases. Also refer to
[getting started](/development/chain/getting-started) and
[general concepts](/development/chain/concepts).

<CardGroup>
  <Card title="Design" icon="chart-network" href="/development/chain/design">
    How to structure your Chainlets, concurrency, file structure
  </Card>

  <Card title="Local Dev" icon="flask" href="/development/chain/localdev">
    Iterating, Debugging, Testing, Mocking
  </Card>

  <Card title="Deploy" icon="rocket" href="/development/chain/deploy">
    Deploy your Chain on Baseten
  </Card>

  <Card title="Invocation" icon="circle-play" href="/development/chain/invocation">
    Call your deployed Chain
  </Card>

  <Card title="Watch" icon="rotate" href="/development/chain/watch">
    Live-patch deployed code
  </Card>

  <Card title="Subclassing" icon="sitemap" href="/development/chain/subclassing">
    Modularize and re-use Chainlet implementations
  </Card>

  <Card title="Streaming" icon="wind" href="/development/chain/streaming">
    Streaming outputs, reducing latency, SSEs
  </Card>

  <Card title="Binary IO" icon="binary" href="/development/chain/binaryio">
    Performant serialization of numeric data
  </Card>

  <Card title="Error Propagation" icon="triangle-exclamation" href="/development/chain/errorhandling">
    Understanding and handling Chains errors
  </Card>

  <Card title="Truss Integration" icon="cube" href="/development/chain/stub">
    Integrate deployed Truss models with stubs
  </Card>
</CardGroup>

## From model to system

Some models are actually pipelines (e.g. invoking a LLM involves sequentially
tokenizing the input, predicting the next token, and then decoding the predicted
tokens). These pipelines generally make sense to bundle together in a monolithic
deployment because they have the same dependencies, require the same compute
resources, and have a robust ecosystem of tooling to improve efficiency and
performance in a single deployment.
Many other pipelines and systems do not share these properties. Some examples
include:

* Running multiple different models in sequence.
* Chunking/partitioning a set of files and concatenating/organizing results.
* Pulling inputs from or saving outputs to a database or vector store.

Each step in these workflows has different hardware requirements, software
dependencies, and scaling needs so it doesn’t make sense to bundle them in a
monolithic deployment. That’s where Chains comes in!

## Six principles behind Chains

Chains exists to help you build multi-step, multi-model pipelines. The
abstractions that Chains introduces are based on six opinionated principles:
three for architecture and three for developer experience.

**Architecture principles**

<Steps>
  <Step title="Atomic components">
    Each step in the pipeline can set its own hardware requirements and
    software dependencies, separating GPU and CPU workloads.
  </Step>

  <Step title="Modular scaling">
    Each component has independent autoscaling parameters for targeted
    resource allocation, removing bottlenecks from your pipelines.
  </Step>

  <Step title="Maximum composability">
    Components specify a single public interface for flexible-but-safe
    composition and are reusable between projects
  </Step>
</Steps>

**Developer experience principles**

<Steps>
  <Step title="Type safety and validation">
    Eliminate entire taxonomies of bugs by writing typed Python code and
    validating inputs, outputs, module initializations, function signatures,
    and even remote server configurations.
  </Step>

  <Step title="Local debugging">
    Seamless local testing and cloud deployments: test Chains locally with
    support for mocking the output of any step and simplify your cloud
    deployment loops by separating large model deployments from quick
    updates to glue code.
  </Step>

  <Step title="Incremental adoption">
    Use Chains to orchestrate existing model deployments, like pre-packaged
    models from Baseten’s model library, alongside new model pipelines built
    entirely within Chains.
  </Step>
</Steps>

## Hello World with Chains

Here’s a simple Chain that says “hello” to each person in a list of provided
names:

```python hello_chain/hello.py theme={"system"}
import asyncio
import truss_chains as chains


# This Chainlet does the work.
class SayHello(chains.ChainletBase):

    async def run_remote(self, name: str) -> str:
        return f"Hello, {name}"


# This Chainlet orchestrates the work.
@chains.mark_entrypoint
class HelloAll(chains.ChainletBase):

    def __init__(self, say_hello_chainlet=chains.depends(SayHello)) -> None:
        self._say_hello = say_hello_chainlet

    async def run_remote(self, names: list[str]) -> str:
        tasks = []
        for name in names:
            tasks.append(asyncio.ensure_future(
                self._say_hello.run_remote(name)))

        return "\n".join(await asyncio.gather(*tasks))
```

This is a toy example, but it shows how Chains can be used to separate
preprocessing steps like chunking from workload execution steps. If SayHello
were an LLM instead of a simple string template, we could do a much more complex
action for each person on the list.

## What to build with Chains

<AccordionGroup>
  <Accordion title="RAG: retrieval-augmented generation" icon="book">
    Connect to vector databases and augment LLM results with additional
    context information without introducing overhead to the model inference
    step.

    Try it yourself: [RAG Chain](/examples/chains-build-rag).
  </Accordion>

  <Accordion title="Chunked Audio Transcription and high-throughput pipelines" icon="forward-fast">
    Transcribe large audio files by splitting them into smaller chunks and
    processing them in parallel — we've used this approach to process 10-hour
    files in minutes.

    Try it yourself: [Audio Transcription Chain](/examples/chains-audio-transcription).
  </Accordion>

  <Accordion title="Efficient multi-model pipelines" icon="hand-holding-dollar">
    Build powerful experiences with optimal scaling in each step like:

    * AI phone calling (transcription + LLM + speech synthesis)
    * Multi-step image generation (SDXL + LoRAs + ControlNets)
    * Multimodal chat (LLM + vision + document parsing + audio)

    Since each stage runs on its hardware with independent auto-scaling,
    you can achieve better hardware utilization and save costs.
  </Accordion>
</AccordionGroup>

Get started by
[building and deploying your first chain](/development/chain/getting-started).


# Streaming
Source: https://docs.baseten.co/development/chain/streaming

Streaming outputs, reducing latency, SSEs

Streaming outputs is useful for returning partial results to the client, before
all data has been processed.

For example LLM text generation happens in incremental text chunks, so the
beginning of the reply can already be sent to the client before the whole
prediction is complete.
Similarly, transcribing audio to text happens in \~30 second chunks and the
first ones can be returned before all completed.

In general, this does not reduce the overall processing time (still the same
amount of work must be done), but the initial latency to get some response
can be reduced significantly.

In some cases it might even reduce overall time, when streaming results
internally in a Chain, allows to start subsequent processing steps sooner -
i.e. pipelining the operations in a more efficient way.

# Low-level streaming

Low-level, streaming works by sending byte chunks (unicode strings will be
implicitly encoded) via HTTP. The most primitive way of doing this in Chains
is by implementing `run_remote` as a bytes- or string-iterator, e.g.:

```python theme={"system"}
from typing import AsyncIterator
import truss_chains as chains


class Streamlet(chains.ChainletBase):

    async def run_remote(self, inputs: ...) -> AsyncIterator[str]:
        async for text_chunk in make_incremental_outputs(inputs):
            yield text_chunk
```

You are free to chose what data to represent in the byte/string chunks, it
could be raw text generated by an LLM, it could be JSON string, bytes or
anything else.

# Server-sent events (SSEs)

A possible choice is to generate chunks that comply with the
[specification](https://html.spec.whatwg.org/multipage/server-sent-events.html)
of server-sent events.

Concretely, sending JSON strings with `data`, `event` and potentially
other fields and content-type `text/event-stream` .

However, the SSE specification is not opinionated regarding what exactly is
encoded in `data` and what `event`-types exist - you have to make up your schema
that is useful for the client that consumes the data.

# Pydantic and Chainlet-Chainlet-streams

<Info>
  While above low-level streaming is stable, the following helper APIs for typed
  streaming are only stable for intra-Chain streaming.

  If you want to use them for end clients, please reach out to Baseten support,
  so we can discuss the stable solutions.
</Info>

Unlike above "raw" stream example, Chains takes the general opinion that
input and output types should be definite, so that divergence and type
errors can be avoided.

Just like you type-annotate Chainlet inputs and outputs in the non-streaming
case, and use pydantic to manage more complex data structures, we built
tooling to bring the same benefits to streaming.

## Headers and footers

This also helps to solve another challenge of streaming: you might want to
send data of different kinds at the beginning or end of a stream than in
the "main" part.

For example if you transcribe an audio file, you might want
to send many transcription segments in a stream and at the end send some
aggregate information such as duration, detected languages etc.

We model typed streaming like this:

* \[optionally] send a chunk that conforms to the schema of a `Header` pydantic
  model.
* Send 0 to N chunks each conforming to the schema of an `Item` pydantic
  model.
* \[optionally] send a chunk that conforms to the schema of a `Footer` pydantic
  model.

## APIs

### StreamTypes

To have a single source of truth for the types that can be shared between
the producing Chainlet and the consuming client (either a Chainlet in the
Chain or an external client), the chains framework uses a `StreamType`-object:

```python theme={"system"}
import pydantic
from truss_chains import streaming


class MyDataChunk(pydantic.BaseModel):
    words: list[str]


STREAM_TYPES = streaming.stream_types(
    MyDataChunk, header_type=..., footer_type=...)
```

Note that header and footer types are optional and can be left out:

```python theme={"system"}
STREAM_TYPES = streaming.stream_types(MyDataChunk)
```

### StreamWriter

Use the `STREAM_TYPES` to create a matching stream writer:

```python theme={"system"}
from typing import AsyncIterator
import pydantic
import truss_chains as chains
from truss_chains import streaming


class MyDataChunk(pydantic.BaseModel):
    words: list[str]


STREAM_TYPES = streaming.stream_types(MyDataChunk)


class Streamlet(chains.ChainletBase):

    async def run_remote(self, inputs: ...) -> AsyncIterator[bytes]:
        stream_writer = streaming.stream_writer(STREAM_TYPES)
        async for item in make_pydantic_items(inputs):
            yield stream_writer.yield_item(item)
```

If your stream types have header or footer types, corresponding
`yield_header` and `yield_footer` methods are available on the writer.

The writer serializes the pydantic data to `bytes`, so you can also
efficiently represent numeric data (see the
[binary IO guide](/development/chain/binaryio)).

### StreamReader

To consume the stream on either another Chainlet or in the external client, a
matching `StreamReader` is created form your `StreamTypes`. Besides the
types, you connect the reader to the bytes generator that you obtain from the
remote invocation of the streaming Chainlet:

```python theme={"system"}
import truss_chains as chains
from truss_chains import streaming


class Consumer(chains.ChainletBase):

    def __init__(self, streamlet=chains.depends(Streamlet)):
        self._streamlet = streamlet

    async def run_remote(self, data: ...):
        byte_stream = self._streamlet.run_remote(data)
        reader = streaming.stream_reader(STREAM_TYPES, byte_stream)
        chunks = []
        async for data in reader.read_items():
            chunks.append(data)
```

If you use headers or footers, the reader has async `read_header` and
`read_footer` methods.

<Info>
  Note that the stream can only be consumed once and you have to consume
  header, items and footer in order.
</Info>

<Tip>
  The implementation of `StreamReader` only needs `pydantic`, no other Chains
  dependencies. So you can take that implementation code in isolation and
  integrate it in your client code.
</Tip>


# Truss Integration
Source: https://docs.baseten.co/development/chain/stub

Integrate deployed Truss models with stubs

Chains can be combined with existing Truss models using Stubs.

A Stub acts as a substitute (client-side proxy) for a remotely deployed
dependency, either a Chainlet or a Truss model. The Stub performs the remote
invocations as if it were local by taking care of the transport layer,
authentication, data serialization and retries.

Stubs can be integrated into Chainlets by passing in a URL of the deployed
model. They also require
[`context`](/development/chain/concepts#context-access-information) to be initialized
(for authentication).

```python theme={"system"}
import truss_chains as chains


class LLMClient(chains.StubBase):

    async def run_remote(self, prompt: str) -> str:
        # Call the deployed model
        resp = await self.predict_async(inputs={
            "messages": [{"role": "user", "content": prompt}],
            "stream"  : False
        })
        # Return a string with the model output
        return resp["output"]


LLM_URL = ...
    
    
class MyChainlet(chains.ChainletBase):

    def __init__(
        self,
        context: chains.DeploymentContext = chains.depends_context(),
    ):
        self._llm = LLMClient.from_url(LLM_URL, context)
```

There are various ways how you can make a call to the other deployment:

* Input as JSON dict (like above) or pydantic model.
* Automatic parsing of the response into an pydantic model using the
  `output_model` argument.
* `predict_async` (recommended) or `predict_async`.
* Streaming responses using `predict_async_stream` which returns an async
  bytes iterator.
* Customized with `RPCOptions`.

See the
[StubBase reference](/reference/sdk/chains#class-truss-chains-stubbase)
for all APIS.


# Subclassing
Source: https://docs.baseten.co/development/chain/subclassing

Modularize and re-use Chainlet implementations

Sometimes you want to write one "main" implementation of a complicated inference
task, but then re-use it for similar variations. For example:

* Deploy it on different hardware and with different concurrency.
* Replace a dependency (e.g. silence detection in audio files) with a
  different implementation of that step - while keeping all other processing
  the same.
* Deploy the same inference flow, but exchange the model weights used. E.g. for
  a large and small version of an LLM or different model weights fine-tuned to\
  domains.
* Add an adapter to convert between a different input/output schema.

In all of those cases, you can create lightweight subclasses of your main
chainlet.

Below are some example code snippets - they can all be combined with each other!

### Example base class

```python theme={"system"}
import asyncio
import truss_chains as chains


class Preprocess2x(chains.ChainletBase):
    async def run_remote(self, number: int) -> int:
        return 2 * number


class MyBaseChainlet(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        compute=chains.Compute(cpu_count=1, memory="100Mi"),
        options=chains.ChainletOptions(enable_b10_tracing=True),
    )

    def __init__(self, preprocess=chains.depends(Preprocess2x)):
        self._preprocess = preprocess

    async def run_remote(self, number: int) -> float:
        return 1.0 / await self._preprocess.run_remote(number)


# Assert base behavior.
with chains.run_local():
    chainlet = MyBaseChainlet()
    result = asyncio.get_event_loop().run_until_complete(chainlet.run_remote(4))
    assert result == 1 / (4 * 2)
```

### Adapter for different I/O

The base class `MyBaseChainlet` works with integer inputs and returns floats. If
you want to reuse the computation, but provide an alternative interface (e.g.
for a different client with different request/response schema), you can create
a subclass which does the I/O conversion. The actual computation is delegated to
the base classes above.

```python theme={"system"}
class ChainletStringIO(MyBaseChainlet):
    async def run_remote(self, number: str) -> str:
        return str(await super().run_remote(int(number)))


# Assert new behavior.
with chains.run_local():
    chainlet_string_io = ChainletStringIO()
    result = asyncio.get_event_loop().run_until_complete(
        chainlet_string_io.run_remote("4"))
    assert result == "0.125"
```

### Chain with substituted dependency

The base class `MyBaseChainlet` uses preprocessing that doubles the input. If
you want to use a different variant of preprocessing - while keeping
`MyBaseChainlet.run_remote` and everything else as is - you can define a shallow
subclass of `MyBaseChainlet` where you use a different dependency
`Preprocess8x`, which multiplies by 8 instead of 2.

```python theme={"system"}
class Preprocess8x(chains.ChainletBase):
    async def run_remote(self, number: int) -> int:
        return 8 * number


class Chainlet8xPreprocess(MyBaseChainlet):
    def __init__(self, preprocess=chains.depends(Preprocess8x)):
        super().__init__(preprocess=preprocess)


# Assert new behavior.
with chains.run_local():
    chainlet_8x_preprocess = Chainlet8xPreprocess()
    result = asyncio.get_event_loop().run_until_complete(
        chainlet_8x_preprocess.run_remote(4))
    assert result == 1 / (4 * 8)
```

### Override remote config.

If you want to re-deploy a chain, but change some deployment options, e.g. run
on different hardware, you can create a subclass and override `remote_config`.

```python theme={"system"}
class Chainlet16Core(MyBaseChainlet):
    remote_config = chains.RemoteConfig(
        compute=chains.Compute(cpu_count=16, memory="100Mi"),
        options=chains.ChainletOptions(enable_b10_tracing=True),
    )

```

<Warning>
  Be aware that `remote_config` is a class variable. In the example above we
  created a completely new `RemoteConfig` value, because changing fields
  *inplace* would also affect the base class.

  If you want to share config between the base class and subclasses, you can
  define them in additional variables e.g. for the image:

  ```python theme={"system"}

  DOCKER_IMAGE = chains.DockerImage(pip_requirements=[...], ...)


  class MyBaseChainlet(chains.ChainletBase):
      remote_config = chains.RemoteConfig(docker_image=DOCKER_IMAGE, ...)


  class Chainlet16Core(MyBaseChainlet):
      remote_config = chains.RemoteConfig(docker_image=DOCKER_IMAGE, ...)
  ```
</Warning>


# Watch
Source: https://docs.baseten.co/development/chain/watch

Live-patch deployed code

The [watch command](/reference/cli/chains/chains-cli#watch) (`truss chains watch`) combines
the best of local development and full deployment. `watch` lets you run on an
exact copy of the production hardware and interface but gives you live code
patching that lets you test changes in seconds without creating a new
deployment.

To use `truss chains watch`:

1. Push a chain in development mode (i.e. `publish` and `promote` flags are
   false).
2. Run the watch command `truss chains watch SOURCE`. You can also add the
   `watch` option to the `push` command and combine both to a single step.
3. Each time you edit a file and save the changes, the watcher patches the
   remote deployments. Updating the deployments might take a moment, but is
   generally *much* faster than creating a new deployment.
4. You can call the chain with test data via `cURL` or the playground dialogue
   in the UI and observe the result and logs.
5. Iterate steps 3. and 4. until your chain behaves in the desired way.

### Selective Watch

Some large ML models might have a slow cycle time to reload (e.g. if the
weights are huge). For this case, we provide a "selective" watch option. For
example if your chain has such a heavy model Chainlet and other Chainlets
that contain only business logic, you can iterate on those, while not patching
and reloading the heavy model Chainlet.

<Warning>
  This feature is really useful for advanced use case, but must be used with
  caution.
  If you change the code of a Chainlet not watched, in particular I/O types,
  you get an inconsistent deployment.
</Warning>

Add the Chainlet names you want to watch as a comma separated list:

```shell theme={"system"}
truss chains watch ... --experimental-chainlet-names=ChainletA,ChainletB
```


# Concepts
Source: https://docs.baseten.co/development/concepts



Baseten provides two core development workflows: [developing a model with Truss](/development/model/) and orchestrating models with [Chains](/development/chain/). Both are building blocks for production-grade ML systems, but they solve different problems.

<CardGroup>
  <Card title="Developing a model with Truss" href="/development/model">
    Package and deploy any AI/ML model as an API with Truss or a Custom Server.
  </Card>

  <Card title="Developing a Chain" href="/development/chain">
    Orchestrate multiple models and logic, enabling complex inference workflows.
  </Card>
</CardGroup>

## Truss vs. Chains: When to use each

### Developing a model with Truss

[Truss](/development/model/overview) is the open-source package you use to turn any ML model into a production-ready API on Baseten - without needing to learn Docker or build custom infrastructure.

**Use Truss when:**

* **You’re deploying a single model.** Whether it’s a fine-tuned transformer, diffusion model, or traditional classifier, Truss helps you package it with code, configuration, and system requirements to deploy at scale.

* **You want flexibility across tools and frameworks.** Build with your preferred model frameworks (e.g. PyTorch, transformers, diffusers), inference engines (e.g. TensorRT-LLM, SGLang, vLLM), and serving technologies (like Triton) as well as [any package](/development/model/configuration) installable via `pip` or `apt`.

* **You need control over how your model runs.** Define pre- and post-processing, batching, logging, and custom inference logic. Truss gives you full access to environment settings and dependencies, versioned and deployable.

* **You want to keep development local and reproducible.** Develop locally in a containerized environment that mirrors production, test confidently, and ship your model without surprises.

### Orchestrating with Chains

[Chains](/development/chain/overview) are for building inference workflows that span multiple steps, models, or tools. You define a sequence of steps — like routing, transformation, or chaining outputs — and run them as a single unit.

**Use Chains when:**

* **You’re combining multiple models or tools.**
  For example, running a vector search + LLM pipeline, or combining OCR, classification, and validation steps.

* **You want visibility into intermediate steps.**
  Chains let you debug and monitor each part of the workflow, retry failed steps, and trace outputs with ease — something that’s much harder with a single model endpoint.

* **You’re using orchestration libraries like LangChain or LlamaIndex.**
  Chains integrate natively with these frameworks, while still allowing you to insert your own logic or wrap Truss models as steps.


# Deprecation
Source: https://docs.baseten.co/development/model-apis/deprecation

Baseten's deprecation policy for Model APIs

As open source models advance rapidly, Baseten prioritizes serving the highest quality models and deprecates specific Model APIs when stronger alternatives are available. When a model is selected for deprecation, Baseten follows this process:

1. **Announcement**
   * Deprecations are announced approximately two weeks before the deprecation date.
   * Documentation is updated to identify the model being deprecated and recommend a replacement.
   * Affected users are contacted via email.
2. **Transition**
   * The deprecated model remains fully functional until the deprecation date. You have approximately two weeks to transition using one of these options:
     1. Migrate to a dedicated deployment with the deprecated model weights. [Contact us](https://www.baseten.co/talk-to-us/deprecation-inquiry/) for assistance.
     2. Update your code to use an active model (a recommendation is provided in the deprecation announcement).
3. **Deprecation date**
   * The model ID for the deprecated model becomes inactive and returns an error for all requests.
   * A changelog notification is published with the recommended replacement.

## Planned deprecations

| Deprecation Date | Model                          | Recommended Replacement                            | Dedicated Available |
| :--------------- | :----------------------------- | :------------------------------------------------- | :-----------------: |
| 2026-2-06        | Qwen3 Coder 480B A35B Instruct | [GLM 4.7](https://www.baseten.co/library/glm-4-7/) |          ✅          |


# Model APIs
Source: https://docs.baseten.co/development/model-apis/overview

OpenAI-compatible endpoints for high-performance LLMs

*Model APIs* provide instant access to high-performance LLMs through OpenAI-compatible endpoints. Point your existing OpenAI SDK at Baseten's inference endpoint and start making calls—no model deployment required.

## Prerequisites

To use Model APIs, you need:

1. A [Baseten account](https://app.baseten.co/signup/)
2. An [API key](https://app.baseten.co/settings/api_keys)
3. The [OpenAI SDK](https://platform.openai.com/docs/libraries) for your language

## Supported models

Enable a model from the [Model APIs page](https://app.baseten.co/model-apis/create) in the Baseten dashboard.

| Model               | Slug                                  | Context |
| ------------------- | ------------------------------------- | ------- |
| OpenAI GPT OSS 120B | `openai/gpt-oss-120b`                 | 128k    |
| DeepSeek V3.2       | `deepseek-ai/DeepSeek-V3.2`           | 131k    |
| DeepSeek V3.1       | `deepseek-ai/DeepSeek-V3.1`           | 164k    |
| DeepSeek V3 0324    | `deepseek-ai/DeepSeek-V3-0324`        | 164k    |
| Kimi K2 Thinking    | `moonshotai/Kimi-K2-Thinking`         | 262k    |
| Kimi K2 0905        | `moonshotai/Kimi-K2-Instruct-0905`    | 128k    |
| Qwen3 Coder 480B    | `Qwen/Qwen3-Coder-480B-A35B-Instruct` | 262k    |
| GLM 4.7             | `zai-org/GLM-4.7`                     | 200k    |
| GLM 4.6             | `zai-org/GLM-4.6`                     | 200k    |

## Create a chat completion

<Tabs>
  <Tab title="Python">
    Initialize the OpenAI client with Baseten's base URL and your API key:

    ```python theme={"system"}
    from openai import OpenAI
    import os

    client = OpenAI(
        base_url="https://inference.baseten.co/v1",
        api_key=os.environ.get("BASETEN_API_KEY")
    )

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3.2",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain gradient descent in one sentence."}
        ]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    Initialize the OpenAI client with Baseten's base URL and your API key:

    ```jsx theme={"system"}
    import OpenAI from "openai";

    const client = new OpenAI({
        baseURL: "https://inference.baseten.co/v1",
        apiKey: process.env.BASETEN_API_KEY,
    });

    const response = await client.chat.completions.create({
        model: "deepseek-ai/DeepSeek-V3.2",
        messages: [
            { role: "system", content: "You are a helpful assistant." },
            { role: "user", content: "Explain gradient descent in one sentence." }
        ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="cURL">
    Send a POST request to the chat completions endpoint with your API key in the header:

    ```bash theme={"system"}
    curl https://inference.baseten.co/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Api-Key $BASETEN_API_KEY" \
      -d '{
        "model": "deepseek-ai/DeepSeek-V3.2",
        "messages": [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Explain gradient descent in one sentence."}
        ]
      }'
    ```
  </Tab>
</Tabs>

Replace the model slug with any model from the supported models table.

## Features

Model APIs support the full OpenAI Chat Completions API:

* **[Structured outputs](/engines/performance-concepts/structured-outputs)**: Generate JSON that conforms to a schema.
* **[Tool calling](/engines/performance-concepts/function-calling)**: Let the model call functions you define.
* **[Reasoning](/development/model-apis/reasoning)**: Control extended thinking for complex tasks.
* **Streaming**: Set `stream: true` to receive responses as server-sent events.

For the complete parameter reference, see the [Chat Completions API documentation](/reference/inference-api/chat-completions).

## Migrate from OpenAI

To migrate existing OpenAI code to Baseten, change three values:

1. Replace your API key with a [Baseten API key](https://app.baseten.co/settings/api_keys).
2. Change the base URL to `https://inference.baseten.co/v1`.
3. Update the model name to a Baseten model slug.

```python theme={"system"}
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://inference.baseten.co/v1",  # [!code ++]
    api_key=os.environ["BASETEN_API_KEY"]  # [!code ++]
)

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2",  # [!code ++]
    messages=[{"role": "user", "content": "Hello"}]
)
```

## Handle errors

Model APIs return standard HTTP error codes:

| Code | Meaning                                 |
| ---- | --------------------------------------- |
| 400  | Invalid request (check your parameters) |
| 401  | Invalid or missing API key              |
| 402  | Payment required                        |
| 404  | Model not found                         |
| 429  | Rate limit exceeded                     |
| 500  | Internal server error                   |

The response body contains details about the error and suggested resolutions.

## Next steps

<CardGroup>
  <Card title="Reasoning" icon="brain" href="/development/model-apis/reasoning">
    Control extended thinking for complex tasks
  </Card>

  <Card title="Rate limits" icon="gauge" href="/development/model-apis/rate-limits-and-budgets">
    Understand and configure rate limits
  </Card>

  <Card title="API reference" icon="code" href="/reference/inference-api/chat-completions">
    Complete parameter documentation
  </Card>

  <Card title="Structured outputs" icon="brackets-curly" href="/engines/performance-concepts/structured-outputs">
    Generate JSON that conforms to a schema
  </Card>
</CardGroup>


# Rate limits and budgets
Source: https://docs.baseten.co/development/model-apis/rate-limits-and-budgets

Rate limits and usage budgets for Model APIs

Baseten enforces two rate limits to ensure fair use and system stability:

* **Request rate limits**: Maximum API requests per minute.
* **Token rate limits**: Maximum tokens processed per minute (input + output combined).

Default limits vary by account status.

| Account                |                                         RPM |                                         TPM |
| :--------------------- | ------------------------------------------: | ------------------------------------------: |
| **Basic** (unverified) |                                          15 |                                     100,000 |
| **Basic** (verified)   |                                         120 |                                     500,000 |
| **Pro**                |                                         120 |                                   1,000,000 |
| **Enterprise**         | [Custom](https://www.baseten.co/talk-to-us) | [Custom](https://www.baseten.co/talk-to-us) |

<Warning>
  If you exceed these limits, the API returns a `429 Too Many Requests` error.
  To request a rate limit increase, [contact us](https://www.baseten.co/talk-to-us/increase-rate-limits/).
</Warning>

***

## Set budgets

Budgets let you control Model API usage and avoid unexpected costs. Budgets apply only to Model APIs, not dedicated deployments. Your team receives email notifications at 75%, 90%, and 100% of budget.

### Enforce budgets

Budgets can be enforced or non-enforced:

* **Enforced**: Requests are rejected when the budget is reached.
* **Not enforced**: You receive notifications but remain responsible for costs over the budget.


# Reasoning
Source: https://docs.baseten.co/development/model-apis/reasoning

Control extended thinking for reasoning-capable models

Some Model APIs support *extended thinking*, where the model reasons through a problem before producing a final answer. The reasoning process generates additional tokens that appear in a separate `reasoning_content` field, distinct from the final response.

## Supported models

| Model            | Slug                           | Reasoning          |
| ---------------- | ------------------------------ | ------------------ |
| DeepSeek V3.2    | `deepseek-ai/DeepSeek-V3.2`    | Enabled by default |
| DeepSeek V3.1    | `deepseek-ai/DeepSeek-V3.1`    | Enabled by default |
| DeepSeek V3 0324 | `deepseek-ai/DeepSeek-V3-0324` | Enabled by default |
| Kimi K2 Thinking | `moonshotai/Kimi-K2-Thinking`  | Always enabled     |
| GLM 4.7          | `zai-org/GLM-4.7`              | Enabled by default |
| GLM 4.6          | `zai-org/GLM-4.6`              | Enabled by default |

Models not listed here do not support reasoning.

## Control reasoning depth

The `reasoning_effort` parameter controls how thoroughly the model reasons through a problem.

| Value    | Behavior                                  |
| -------- | ----------------------------------------- |
| `low`    | Faster responses, less thorough reasoning |
| `medium` | Balanced (default)                        |
| `high`   | Slower responses, more thorough reasoning |

<Tabs>
  <Tab title="Python">
    Pass `reasoning_effort` through `extra_body` since it extends the standard OpenAI API:

    ```python theme={"system"}
    from openai import OpenAI
    import os

    client = OpenAI(
        base_url="https://inference.baseten.co/v1",
        api_key=os.environ.get("BASETEN_API_KEY")
    )

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3.2",
        messages=[
            {"role": "user", "content": "What is the sum of the first 100 prime numbers?"}
        ],
        extra_body={"reasoning_effort": "high"}  # [!code ++]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    Include `reasoning_effort` directly in the request options:

    ```jsx theme={"system"}
    import OpenAI from "openai";

    const client = new OpenAI({
        baseURL: "https://inference.baseten.co/v1",
        apiKey: process.env.BASETEN_API_KEY,
    });

    const response = await client.chat.completions.create({
        model: "deepseek-ai/DeepSeek-V3.2",
        messages: [
            { role: "user", content: "What is the sum of the first 100 prime numbers?" }
        ],
        reasoning_effort: "high"  // [!code ++]
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="cURL">
    Include `reasoning_effort` in the JSON request body:

    ```bash theme={"system"}
    curl https://inference.baseten.co/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Api-Key $BASETEN_API_KEY" \
      -d '{
        "model": "deepseek-ai/DeepSeek-V3.2",
        "messages": [{"role": "user", "content": "What is the sum of the first 100 prime numbers?"}],
        "reasoning_effort": "high"
      }'
    ```
  </Tab>
</Tabs>

## Parse the response

The model's thinking process appears in `reasoning_content`, separate from the final answer in `content`.

```json theme={"system"}
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "The sum of the first 100 prime numbers is 24,133.",
        "reasoning_content": "Let me work through this step by step. The first prime number is 2..."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 18,
    "completion_tokens": 245,
    "total_tokens": 263,
    "completion_tokens_details": {
      "reasoning_tokens": 198
    }
  }
}
```

The `reasoning_tokens` field in `completion_tokens_details` shows how many tokens the model used for reasoning. These tokens count toward your total usage and billing.

## Decide when to reason

Reasoning improves quality for tasks that benefit from step-by-step thinking: mathematical calculations, multi-step logic problems, code generation with complex requirements, and analysis requiring multiple considerations.

For straightforward tasks like simple Q\&A or text generation, reasoning adds latency and token cost without improving quality. In these cases, use a model without reasoning support or set `reasoning_effort` to `low`.


# b10cache 🆕
Source: https://docs.baseten.co/development/model/b10cache

Persist data across replicas or deployments

<Warning>
  ### Early Access

  Please contact our [support team](mailto:support@baseten.co) for access to b10cache.
</Warning>

Deployments sometimes have cache or other files that are useful to other replicas. Using `torch.compile` results in a cache that can speed up future `torch.compile` on the same function. This can speed up other replicas' cold start times.

**These files can be stored via b10cache**. b10cache is a volume mounted over the network onto each of your pods. There are two ways files can be stored:

#### 1. `/cache/org/`

This directory is shared, and can be written to or accessed by every pod you deploy. Simply move a file into here and it will be accessible.

#### 2. `/cache/model/`

This directory is shared by every pod within the scope of your deployment. This is excellent for keeping filesystems clean and limiting access.

<Danger>
  ### Not a persistent object storage

  While b10cache is very reliable, it should not be used as a persistent object storage or database. **It should be considered a cache** that can be shared by deployments, meaning there should always be a fallback plan if the b10cache path does not exist.
</Danger>

See two features built on b10cache:

1. [*model cache*](/development/model/model-cache)
2. [*torch compile cache*](/development/model/torch-compile-cache)


# Base Docker images
Source: https://docs.baseten.co/development/model/base-images

A guide to configuring a base image for your truss

Truss uses containerized environments to ensure consistent model execution across deployments. While the default Truss image works for most cases, you may need a custom base image to meet specific package or system requirements.

## Setting a base image in`config.yaml`

Specify a custom base image in `config.yaml`:

```yaml config.yaml theme={"system"}
base_image:
  image: <image_name:tag>
  python_executable_path: <path-to-python>
```

* `image`: The Docker image to use.
* `python_executable_path`: The path to the Python binary inside the container.

### Example: NVIDIA NeMo Model

Using a custom image to deploy [NVIDIA NeMo TitaNet](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/titanet_large) model:

```yaml config.yaml theme={"system"}
base_image:
  image: nvcr.io/nvidia/nemo:23.03
  python_executable_path: /usr/bin/python
apply_library_patches: true
requirements:
  - PySoundFile
resources:
  accelerator: T4
  cpu: 2500m
  memory: 4512Mi
  use_gpu: true
secrets: {}
system_packages:
  - python3.8-venv
```

## Using Private Base Images

If your base image is private, ensure that you have configured your model to use a [private registry](/development/model/private-registries)

## Creating a custom base image

You can build a new base image using Truss’s base images as a foundation. Available images are listed on [Docker Hub](https://hub.docker.com/r/baseten/truss-server-base/tags).

#### Example: Customizing a Truss Base Image

```Dockerfile Dockerfile theme={"system"}
FROM baseten/truss-server-base:3.11-gpu-v0.7.16
RUN pip uninstall cython -y
RUN pip install cython==0.29.30
```

#### Building & Pushing Your Custom Image

Ensure Docker is installed and running. Then, build, tag, and push your image:

```sh theme={"system"}
docker build -t my-custom-base-image:0.1 .
docker tag my-custom-base-image:0.1 your-docker-username/my-custom-base-image:0.1
docker push your-docker-username/my-custom-base-image:0.1
```


# Custom build commands
Source: https://docs.baseten.co/development/model/build-commands

How to run your own docker commands during the build stage

The `build_commands` feature allows you to **run custom Docker commands** during the **build stage**, enabling **advanced caching**, **dependency management**, **and environment setup**.

**Use Cases:**

* Clone GitHub repositories
* Install dependencies
* Create directories
* Pre-download model weights

## 1. Using Build Commands in `config.yaml`

Add `build_commands` to your `config.yaml`:

```yaml theme={"system"}
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

```yaml theme={"system"}
build_commands:
  - git clone https://github.com/comfyanonymous/ComfyUI.git
  - cd ComfyUI && mkdir ipadapter
  - cd ComfyUI && mkdir instantid
```

<Info>Useful for **large codebases** requiring additional structure.</Info>

## 3. Caching Model Weights Efficiently

<Warning>For large weights (10GB+), use `model_cache` or `external_data`.</Warning>

For smaller weights, **use** `wget` in `build_commands`:

```yaml theme={"system"}
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


# Your first model
Source: https://docs.baseten.co/development/model/build-your-first-model

Build and deploy your first model

This quickstart guide shows you how to build and deploy your first model,
using Baseten's Truss framework.

## Prerequisites

To use Truss, install a recent Truss version and ensure pydantic is v2:

```bash theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"}
pip install --upgrade truss 'pydantic>=2.0.0'
```

<Accordion title="Help for setting up a clean development environment">
  Truss requires python `>=3.9,<3.15`. To set up a fresh development environment,
  you can use the following commands, creating a environment named `truss_env`
  using `pyenv`:

  ```bash theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"}
  curl https://pyenv.run | bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  source ~/.bashrc
  pyenv install 3.11.0
  ENV_NAME="truss_env"
  pyenv virtualenv 3.11.0 $ENV_NAME
  pyenv activate $ENV_NAME
  pip install --upgrade truss 'pydantic>=2.0.0'
  ```
</Accordion>

To deploy Truss remotely, you also need a
[Baseten account](https://app.baseten.co/signup).
It is handy to export your API key to the current shell session or permanently in your `.bashrc`:

```bash ~/.bashrc theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"} theme={"system"}
export BASETEN_API_KEY="nPh8..."
```

## Initialize your model

Truss is a tool that helps you package your model code and configuration, and ship it to Baseten for deployment, testing, and scaling.

To create your first model, you can use the `truss init` command.

```bash theme={"system"}
$ truss init hello-world
? 📦 Name this model: HelloWorld
Truss HelloWorld was created in ~/hello-world
```

This will create a new directory called `hello-world` with the following files:

* `config.yaml` - A configuration file for your model.
* `model/model.py` - A Python file that contains your model code
* `packages/` - A folder to hold any dependencies your model needs
* `data/` - A folder to hold any data your model needs

For this example, we'll focus on the `config.yaml` file and the `model.py` file.

### `config.yaml`

The `config.yaml` file is used to configure dependencies, resources, and
other settings for your model.

Let's take a look at the contents:

```yaml config.yaml theme={"system"}
build_commands: []
environment_variables: {}
external_package_dirs: []
model_metadata: {}
model_name: HelloWorld
python_version: py311
requirements: []
resources:
  accelerator: null
  cpu: '1'
  memory: 2Gi
  use_gpu: false
secrets: {}
system_packages: []
```

Some key fields to note:

* `requirements`: This is a list of `pip` packages that will be installed when
  your model is deployed.
* `resources`: This is where you can specify the resources your model will use.
* `secrets`: This is where you can specify any secrets your model will need, such as
  HuggingFace API keys.

See the [Configuration](/development/model/configuration) page for more information on the `config.yaml` file.

### `model.py`

Next, let's take a look at the `model.py` file.

```python theme={"system"}
class Model:
    def __init__(self, **kwargs):
        pass

    def load(self):
        pass

    def predict(self, model_input):
        return model_input 
```

In Truss models, we expect users to provide a Python class with the following methods:

* `__init__`: This is the constructor.
* `load`: This is called at model startup, and should include any setup logic, such as weight downloading or initialization
* `predict`: This is the method that is called during inference.

## Deploy your model

To deploy your model for development with live reload, run:

```bash theme={"system"}
$ truss push --watch
```

This will deploy your model to Baseten as a development deployment with live reload enabled.

<Note>
  When no flag is specified, `truss push` defaults to a published deployment. Use `--watch` for development deployments with live reload support, or `--publish` explicitly for production-ready deployments.
</Note>

## Invoke your model

After deploying your model, you can invoke it with the invocation URL provided:

```bash theme={"system"}
$ curl -X POST https://model-{model-id}.api.baseten.co/development/predict \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -d '"some text"'
"some text"
```

## A Real Example

To show a slightly more complex example, let's deploy a text classification model
from HuggingFace!

In this example, we'll use the `transformers` library to load a pre-trained model,
from HuggingFace, and use it to classify the given text.

### `config.yaml`

To deploy this model, we need to add a few more dependencies to our `config.yaml` file.

```yaml config.yaml theme={"system"}
requirements:
  - transformers
  - torch
```

### `model.py`

Next, let's change our `model.py` file to use the `transformers` library to load the model,
and then use it to predict the sentiment of a given text.

```python model.py theme={"system"}
from transformers import pipeline

class Model:
    def __init__(self, **kwargs):
        pass

    def load(self):
        self._model = pipeline("text-classification")

    def predict(self, model_input):
        return self._model(model_input)
```

## Running inference

Similarly to our previous example, we can deploy this model using `truss push --watch`

```bash theme={"system"}
$ truss push --watch
```

And then invoke it using the invocation URL on Baseten.

```bash theme={"system"}
$ curl -X POST https://model-{model-id}.api.baseten.co/development/predict \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -d '{"text": "some text"}'
```

## Next steps

Now that you've deployed your first model, you can learn more about more
options for [configuring your model](/development/model/configuration),
and [implementing your model](/development/model/implementation).


# Python driven configuration for models 🆕
Source: https://docs.baseten.co/development/model/code-first-development

Use code-first development tools to streamline model production.

<Info> This feature is still in beta. </Info>

In addition to our normal YAML configuration, we support configuring your model using pure Python. This offers the following benefits:

* **Typed configuration via Python code** with IDE autocomplete, instead of a separate `yaml` configuration file
* **Simpler directory structure** that IDEs support for module resolution

In this guide, we go through deploying a simple Model using this new framework.

### Step 1: Initializing your project

We leverage traditional `truss init` functionality with a new flag to create the directory structure:

```bash theme={"system"}
truss init my-new-model --python-config
```

### Step 2: Write your model

To build a model with this new framework, we require two things:

* A class that inherits from `baseten.ModelBase`, which will serve as the entrypoint when invoking `/predict`
* A `predict` method with type hints

That’s it! The following is a contrived example of a complete model that will keep a running total of user provided input:

```python my_model.py theme={"system"}
import truss_chains as baseten


class RunningTotalCalculator(baseten.ModelBase):
    def __init__(self):
        self._running_total = 0

    async def predict(self, increment: int) -> int:
        self._running_total += increment
        return self._running_total
```

### Step 3: Deploy, patch, and publish your model

In order to deploy a development version of your new model with live reload, you can run:

```bash theme={"system"}
truss push my_model.py --watch
```

Please note that `push` (as well as all other commands below) will require that you pass the path to the file containing the model as the final argument.

This new workflow also supports patching, so you can quickly iterate during development without building new images every time.

```bash theme={"system"}
truss watch my_model.py
```

To deploy a production-ready version, use:

```bash theme={"system"}
truss push my_model.py --publish
```

### Model Configuration

Models can configure requirements for compute hardware (CPU count, GPU type and count, etc) and software dependencies (Python libraries or system packages) via the [`remote_config`](/reference/sdk/chains#remote-configuration) class variable within the model:

```python my_model.py theme={"system"}
class RunningTotalCalculator(baseten.ModelBase):
    remote_config: baseten.RemoteConfig = baseten.RemoteConfig(
        compute=baseten.Compute(cpu_count=4, memory="1Gi", gpu="T4", gpu_count=2)
    )

    ...
```

See the [remote configuration reference](/reference/sdk/chains#remote-configuration) for a complete list of options.

### Context (access information)

You can add [`DeploymentContext`](/reference/sdk/chains#class-truss-chains-deploymentcontext) object as an optional final argument to the **`__init__`**-method of a Model. This allows you to use secrets within your Model, but note that they’ll also need to be added to the **`assets`**.

We only expose secrets to the model that were explicitly requested in `assets` to comply with best security practices.

```python my_model.py theme={"system"}
class RunningTotalCalculator(baseten.ModelBase):
    remote_config: baseten.RemoteConfig = baseten.RemoteConfig(
        ...
        assets=baseten.Assets(secret_keys=["token"])
    )

    def __init__(self, context: baseten.DeploymentContext = baseten.depends_context()):
        ...
        self._token = context.secrets["token"]

```

### Packages

If you want to include modules in your model, you can easily create them from the root of the project:

```bash theme={"system"}
my-new-model/
    module_1/
	    submodule/
		    script.py
    module_2/
	    another_script.py
    my_model.py
```

With this file structure, you would import in `my_model.py` as follows:

```python my_model.py theme={"system"}
import truss_chains as baseten

from module_1.submodule import script
from module_2 import another_script

class RunningTotalCalculator(baseten.ModelBase):
    ....
```

### Known Limitations

* RemoteConfig does *not* support all the options exposed by the traditional `config.yaml`. If you’re excited about this new development experience but need a specific feature ported over, please reach out to us!
* This new framework does not support `preprocess` or `postprocess` hooks. We typically recommend inlining functionality from those functions if easy, or utilizing `chains` if the needs are more complex.


# Request concurrency
Source: https://docs.baseten.co/development/model/concurrency

A guide to setting concurrency for your model

Configuring concurrency optimizes **model performance**, balancing **throughput** and **latency**.

In Baseten and Truss, concurrency is managed at **two levels**:

1. **Concurrency Target** – Limits the number of requests **sent** to a single replica.
2. **Predict Concurrency** – Limits how many requests the predict function handles **inside the model container**.

## 1. Concurrency Target

* **Set in the Baseten UI** – Defines how many requests a single replica can process at once.
* **Triggers autoscaling** – If all replicas hit the concurrency target, additional replicas spin up.

**Example:**

* **Concurrency Target = 2, Single Replica**
* **5 requests arrive** → 2 are processed immediately, **3 are queued**.
* If max replicas aren't reached, **autoscaling spins up a new replica**.

## 2. Predict Concurrency

* **Set in** `config.yaml` – Controls how many requests can be **processed by** predict simultaneously.
* **Protects GPU resources** – Prevents multiple requests from overloading the GPU.

### Configuring Predict Concurrency

```yaml config.yaml theme={"system"}
model_name: "My model with concurrency limits"
runtime:
  predict_concurrency: 2  # Default is 1
```

### How It Works Inside a Model Pod

1. **Requests arrive** → All begin preprocessing (e.g., downloading images from S3).
2. **Predict runs on GPU** → Limited by `predict_concurrency`.
3. **Postprocessing begins** → Can run while other requests are still in inference.

## When to Use Predict Concurrency

* ✅ **Protect GPU resources** – Prevent multiple requests from degrading performance.
* ✅ **Allow parallel preprocessing/postprocessing** – I/O tasks can continue even when inference is blocked.

<Warning>Ensure `Concurrency Target` is set high enough to send enough requests to the container.</Warning>


# Configuration
Source: https://docs.baseten.co/development/model/configuration

How to configure your model.

ML models depend on external libraries, data files, and specific hardware configurations.

This guide shows you how to configure your model's dependencies and resources.

The `config.yaml` file defines your model's configuration. Common options include:

# Environment variables

To set environment variables in the model serving environment, use the `environment_variables` key:

```yaml config.yaml theme={"system"}
environment_variables:
  MY_ENV_VAR: my_value
```

# Python packages

Python packages can be specified in two ways in the `config.yaml` file:

1. `requirements`: A list of Python packages to install.
2. `requirements_file`: A requirements.txt file to install pip packages from.

To specify Python packages as a list, use the following:

```yaml config.yaml theme={"system"}
requirements:
  - package_name
  - package_name2
```

Pin package versions using the `==` operator:

```yaml config.yaml theme={"system"}
requirements:
  - package_name==1.0.0
  - package_name2==2.0.0
```

If you need more control over the installation process and want to use
different pip options or repositories, you can specify a `requirements_file`
instead.

```yaml config.yaml theme={"system"}
requirements_file: ./requirements.txt
```

# System packages

Truss also has support for installing apt-installable Debian packages. To add
system packages to your model serving environment, add the following to your
`config.yaml` file:

```yaml config.yaml theme={"system"}
system_packages:
  - package_name
  - package_name2
```

For example, to install Tesseract OCR:

```yaml config.yaml theme={"system"}
system_packages:
  - tesseract-ocr
```

# Resources

Specify hardware resources in the `resources` section.

**Option 1: Specify individual resource fields**

For a CPU model:

```yaml config.yaml theme={"system"}
resources:
  cpu: "1"
  memory: 2Gi
```

For a GPU model:

```yaml config.yaml theme={"system"}
resources:
  accelerator: "L4"
```

When you push your model, it will be assigned an instance type matching the
specifications required.

**Option 2: Specify an exact instance type**

```yaml config.yaml theme={"system"}
resources:
  instance_type: "L4:4x16"
```

Using `instance_type` lets you select an exact SKU. When specified, other resource fields are ignored.

See the [Resources](/deployment/resources) page for more information on
options available.

# Advanced configuration

There are numerous other options for configuring your model. See some
of the other guides:

* [Secrets](/development/model/secrets)
* [Data](/development/model/data-directory)
* [Custom Build Commands](/development/model/build-commands)
* [Base Docker Images](/development/model/base-images)
* [Custom Servers](/development/model/custom-server)
* [Custom Health Checks](/development/model/custom-health-checks)


# Custom health checks
Source: https://docs.baseten.co/development/model/custom-health-checks

Customize the health of your deployments.

**Why use custom health checks?**

* **Control traffic and restarts** by configuring failure thresholds to suit your needs.
* **Define replica health with custom logic** (e.g. fail after a certain number of 500s or a specific CUDA error).

By default, health checks run every 10 seconds to verify that each replica of
your deployment is running successfully and can receive requests. If a health
check fails for an extended period, one or both of the following actions may
occur:

* Traffic is immediately stopped from reaching the failing replica.
* The failing replica is restarted.

The thresholds for each of these actions are configurable.

## Understanding readiness vs. liveness

Baseten uses two types of Kubernetes health probes that run continuously after
your container starts:

**Readiness probe** answers "Can I handle requests right now?" When it fails,
Kubernetes stops sending traffic to the container but doesn't restart it. Use
this to prevent traffic during startup or temporary unavailability. The failure
threshold is controlled by `stop_traffic_threshold_seconds`.

**Liveness probe** answers "Am I healthy enough to keep running?" When it fails,
Kubernetes restarts the container. Use this to recover from deadlocks or hung
processes. The failure threshold is controlled by `restart_threshold_seconds`.

For most servers, using the same endpoint (like `/health`) for both probes is
sufficient. The key difference is the action taken: readiness controls traffic
routing, while liveness controls container lifecycle.

Both probes wait before starting checks to allow your server time to initialize.
Configure this delay with `restart_check_delay_seconds`.

Custom health checks can be implemented in two ways:

1. [**Configuring thresholds**](#configuring-health-checks) for when health check failures should stop traffic to or restart a replica.
2. [**Writing custom health check logic**](#writing-custom-health-checks) to define how replica health is determined.

## Configuring health checks

### Parameters

You can customize the behavior of health checks on your deployments by setting
the following parameters:

<ParamField type="integer">
  The duration that health checks must continuously fail before traffic to the failing replica is stopped.

  `stop_traffic_threshold_seconds` must be between `30` and `1800` seconds, inclusive.
</ParamField>

<ParamField type="integer">
  How long to wait before running health checks.

  `restart_check_delay_seconds` must be between `0` and `1800` seconds, inclusive.
</ParamField>

<ParamField type="integer">
  The duration that health checks must continuously fail before triggering a restart of the failing replica.

  `restart_threshold_seconds` must be between `30` and `1800` seconds, inclusive.

  <Note> The combined value of `restart_check_delay_seconds` and `restart_threshold_seconds` must not exceed `1800` seconds. </Note>
</ParamField>

### Model and custom server deployments

Configure health checks in your `config.yaml`.

```yaml config.yaml theme={"system"}
runtime:
  health_checks:
    restart_check_delay_seconds: 60 # Waits 60 seconds after deployment before starting health checks
    restart_threshold_seconds: 600 # Triggers a restart if health checks fail for 10 minutes
    stop_traffic_threshold_seconds: 300 # Stops traffic if health checks fail for 5 minutes
```

You can also specify custom health check endpoints for custom servers.
[See here](/development/model/custom-server#1-configuring-a-custom-server-in-config-yaml)
for more details.

### Chains

Use `remote_config` to configure health checks for your chainlet classes.

```python chain.py theme={"system"}
class CustomHealthChecks(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        options=chains.ChainletOptions(
            health_checks=truss_config.HealthChecks(
                restart_check_delay_seconds=30,     # Waits 30 seconds before starting health checks
                restart_threshold_seconds=600,      # Restart replicas after 10 minutes of failure
                stop_traffic_threshold_seconds=300, # Stop traffic after 5 minutes of failure
            )
        )
    )
```

## Writing custom health checks

You can write custom health checks in both **model deployments** and **chain
deployments**.

<Info>
  Custom health checks are currently not supported in development deployments.
</Info>

### Custom health checks in models

```python model.py theme={"system"}
class Model:
    def is_healthy(self) -> bool:
        # Add custom health check logic for your model here
		pass
```

### Custom health checks in chains

Health checks can be customized for each chainlet in your chain.

```python chain.py theme={"system"}
@chains.mark_entrypoint
class CustomHealthChecks(chains.ChainletBase):
    def is_healthy(self) -> bool:
        # Add custom health check logic for your chainlet here
        pass
```

## Health checks in action

### Identifying 5xx errors

You might create a custom health check to identify 5xx errors like the following:

```python model.py theme={"system"}
class Model:
    def __init__(self):
        ...
        self._is_healthy = True

    def load(self):
        # Perform load
        # Your custom health check won't run until after load completes
        ...

    def is_healthy(self):
        return self._is_healthy

    def predict(self, input):
        try:
            # Perform inference
            ...
        except Some5xxError:
            self._is_healthy = False
            raise
```

Custom health check failures are indicated by the following log:

```md Example health check failure log line theme={"system"}
Jan 27 10:36:03pm md2pg Health check failed.
```

Deployment restarts due to health check failures are indicated by the following log:

```md Example restart log line theme={"system"}
Jan 27 12:02:47pm zgbmb Model terminated unexpectedly. Exit code: 0, reason: Completed, restart count: 1
```

## FAQs

### Is there a rule of thumb for configuring thresholds for stopping traffic and restarting?

It depends on your health check implementation. If your health check relies on conditions that only change during inference (e.g., `_is_healthy` is set in `predict`), restarting before stopping traffic is generally better, as it allows recovery without disrupting traffic.

Stopping traffic first may be preferable if a failing replica is actively degrading performance or causing inference errors, as it prevents the failing replica from affecting the overall deployment while allowing time for debugging or recovery.

### When should I configure `restart_check_delay_seconds`?

Configure `restart_check_delay_seconds` to allow replicas sufficient time to initialize after deployment or a restart. This delay helps reduce unnecessary restarts, particularly for services with longer startup times.

### Why am I seeing two health check failure logs in my logs?

These refer to two separate health checks we run every 10 seconds:

* One to determine when to stop traffic to a replica.
* The other to determine when to restart a replica.

### Does stopped traffic or replica restarts affect autoscaling?

Yes, both can impact autoscaling. If traffic stops or replicas restart, the
remaining replicas handle more load. If the load exceeds the concurrency target
during the autoscaling window, additional replicas are spun up. Similarly, when
traffic stabilizes, excess replicas are scaled down after the scale down delay.
[See here](/deployment/autoscaling#autoscaling-behavior) for more details on
autoscaling.

### How does billing get affected?

You are billed for the uptime of your deployment. This includes the time a
replica is running, even if it is failing health checks, until it scales down.

### Will failing health checks cause my deployment to stay up forever?

No. If your deployment is configured with a scale down delay and the minimum
number of replicas is set to 0, the replicas will scale down once the model is
no longer receiving traffic for the duration of the scale down delay. This
applies even if the replicas are failing health checks.
[See here](/deployment/autoscaling#scale-to-zero) for more details on
autoscaling.

### What happens when my deployment is loading?

When your deployment is loading, your custom health check will not be running.
Once `load()` is completed, we'll start using your custom `is_healthy()` health
check.


# Deploy custom Docker images
Source: https://docs.baseten.co/development/model/custom-server

Deploy custom Docker images to run inference servers like vLLM, SGLang, Triton, or any containerized application.

When you write a `Model` class, Truss uses the
[Truss server base image](https://hub.docker.com/r/baseten/truss-server-base/tags)
by default. However, you can deploy pre-built containers.

In this guide, you will learn how to set the your configuration file to run a
custom Docker image and deploy it to Baseten using Truss.

## Configuration

To deploy a custom Docker image, set
[`base_image`](/reference/truss-configuration#base-image-image) to your image
and use the `docker_server` argument to specify how to run it.

```yaml config.yaml theme={"system"}
base_image:
  image: your-registry/your-image:latest
docker_server:
  start_command: your-server-start-command
  server_port: 8000
  predict_endpoint: /predict
  readiness_endpoint: /health
  liveness_endpoint: /health
```

* `image`: The Docker image to use.
* `start_command`: The command to start the server.
* `server_port`: The port to listen on.
* `predict_endpoint`: The endpoint to forward requests to.
* `readiness_endpoint`: The endpoint to check if the server is ready.
* `liveness_endpoint`: The endpoint to check if the server is alive.

<Warning>
  Port 8080 is reserved by Baseten's internal reverse proxy. If your server binds to port 8080, the deployment fails with `[Errno 98] address already in use`.
</Warning>

For the full list of fields, see the
[configuration reference](/reference/truss-configuration#docker_server).

<Accordion title="Endpoint mapping">
  While `predict_endpoint` maps your server's inference route to Baseten's
  `/predict` endpoint, you can access any route in your server using the
  [sync endpoint](/inference/calling-your-model#sync-api-endpoints).

  | Baseten endpoint                            | Maps to                       |
  | ------------------------------------------- | ----------------------------- |
  | `/environments/production/predict`          | Your `predict_endpoint` route |
  | `/environments/production/sync/{any/route}` | `/{any/route}` in your server |

  **Example:** If you set `predict_endpoint: /v1/chat/completions`:

  | Baseten endpoint                          | Maps to                |
  | ----------------------------------------- | ---------------------- |
  | `/environments/production/predict`        | `/v1/chat/completions` |
  | `/environments/production/sync/v1/models` | `/v1/models`           |
</Accordion>

## Deploy Ollama

This example deploys [Ollama](https://ollama.com/) with the TinyLlama model
using a custom Docker image. Ollama is a popular lightweight LLM inference
server, similar to vLLM or SGLang. TinyLlama is small enough to run on a CPU.

### 1. Create the config

Create a `config.yaml` file with the following configuration:

```yaml config.yaml theme={"system"}
model_name: ollama-tinyllama
base_image:
  image: python:3.11-slim
build_commands:
  - curl -fsSL https://ollama.com/install.sh | sh
docker_server:
  start_command: sh -c "ollama serve & sleep 5 && ollama pull tinyllama && wait"
  readiness_endpoint: /api/tags
  liveness_endpoint: /api/tags
  predict_endpoint: /api/generate
  server_port: 11434
resources:
  cpu: "4"
  memory: 8Gi
```

The `base_image` field specifies the Docker image to use as your starting
point, in this case a lightweight Python image. The `build_commands` section
installs Ollama into the container at build time. You can also use this to
install model weights or other dependencies.

The `start_command` launches the Ollama server, waits for it to initialize, and
then pulls the TinyLlama model.

The `readiness_endpoint` and `liveness_endpoint`
both point to `/api/tags`, which returns successfully when Ollama is running.
The `predict_endpoint` maps Baseten's `/predict` route to Ollama's
`/api/generate` endpoint.

Finally, declare your resource requirements. This example only needs 4 CPUs and
8GB of memory. For a complete list of resource options, see the
[Resources](/deployment/resources) page.

### 2. Deploy

To deploy the model, use the following:

```sh theme={"system"}
truss push --publish
```

This will build the Docker image and deploy it to Baseten.
Once the `readiness_endpoint` and `liveness_endpoint` are successful, the model will be ready to use.

### 3. Run inference

Ollama uses OpenAI API compatible endpoints to run inference and calls
`/api/generate` to generate text. Since you mapped the `/predict` route to
Ollama's `/api/generate` endpoint, you can run inference by calling the
`/predict` endpoint.

<Tabs>
  <Tab title="Truss CLI">
    To run inference with Truss, use the `predict` command:

    ```sh theme={"system"}
    truss predict -d '{"model": "tinyllama", "prompt": "Write a short story about a robot dreaming", "options": {"num_predict": 50}}'
    ```
  </Tab>

  <Tab title="cURL">
    To run inference with cURL, use the following command:

    ```sh theme={"system"}
    curl -s -X POST "https://model-MODEL_ID.api.baseten.co/development/predict" \
      -H "Authorization: Api-Key $BASETEN_API_KEY" \
      -d '{"model": "tinyllama", "prompt": "Write a short story about a robot dreaming", "options": {"num_predict": 50}}' \
      | jq -j '.response'
    ```
  </Tab>

  <Tab title="Python">
    To run inference with Python, use the following:

    ```python theme={"system"}
    import os
    import requests

    model_id = "MODEL_ID"
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    response = requests.post(
        f"https://model-{model_id}.api.baseten.co/development/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "model": "tinyllama",
            "prompt": "Write a short story about a robot dreaming",
            "options": {"num_predict": 50},
        },
    )
    print(response.json()["response"])
    ```
  </Tab>
</Tabs>

The following is an example of its response:

```output theme={"system"}
It was a dreary, grey day when the robots started to dream. 
They had been programmed to think like humans, but it wasn't until they began to dream that they realized just how far apart they actually were.
```

Congratulations! You have successfully deployed and ran inference on a custom Docker image.

## Next steps

* [Private registries](/development/model/private-registries) — Pull images from AWS ECR, Google Artifact Registry, or Docker Hub
* [Secrets](/development/model/secrets#custom-docker-images) — Access API keys and tokens in your container
* [WebSockets](/development/model/websockets#websocket-usage-with-custom-servers) — Enable WebSocket connections
* [vLLM](/examples/vllm), [SGLang](/examples/sglang), [TensorRT-LLM](/examples/tensorrt-llm) — Deploy LLMs with popular inference servers


# Data and storage
Source: https://docs.baseten.co/development/model/data-directory

Load model weights without Hugging Face or S3

Model files, such as weights, can be **large** (often **multiple GBs**). Truss supports **multiple ways** to load them efficiently:

* **Public Hugging Face models** (default)
* **Bundled directly in Truss**

### 1. Bundling model weights in Truss

Store model files **inside Truss** using the `data/` directory.

**Example: Stable Diffusion 2.1 Truss structure**

```pssql theme={"system"}
data/
    scheduler/
        scheduler_config.json
    text_encoder/
        config.json
        diffusion_pytorch_model.bin
    tokenizer/
        merges.txt
        tokenizer_config.json
        vocab.json
    unet/
        config.json
        diffusion_pytorch_model.bin
    vae/
        config.json
        diffusion_pytorch_model.bin
    model_index.json
```

**Access bundled files in `model.py`:**

```python theme={"system"}
class Model:
    def __init__(self, **kwargs):
        self._data_dir = kwargs["data_dir"]

    def load(self):
        self.model = StableDiffusionPipeline.from_pretrained(
            str(self._data_dir),
            revision="fp16",
            torch_dtype=torch.float16,
        ).to("cuda")
```

<Warning>
  Limitation: Large weights increase deployment size, making it slower. Consider
  cloud storage instead.
</Warning>

## 2. Loading private model weights from S3

If using **private S3 storage**, first **configure secure authentication**.

### Step 1: Define AWS secrets in `config.yaml`

```yaml theme={"system"}
secrets:
  aws_access_key_id: null
  aws_secret_access_key: null
  aws_region: null # e.g., us-east-1
  aws_bucket: null
```

<Warning>
  Do not store actual credentials here. Add them securely to [Baseten secrets
  manager](https://app.baseten.co/settings/secrets).
</Warning>

### Step 2: Authenticate with AWS in `model.py`

```python theme={"system"}
import boto3

def __init__(self, **kwargs):
    self._config = kwargs.get("config")
    secrets = kwargs.get("secrets")
    self.s3_client = boto3.client(
        "s3",
        aws_access_key_id=secrets["aws_access_key_id"],
        aws_secret_access_key=secrets["aws_secret_access_key"],
        region_name=secrets["aws_region"],
    )
    self.s3_bucket = secrets["aws_bucket"]
```

### Step 3: Deploy

Deploy for development:

```sh theme={"system"}
truss push --watch
```

Or deploy for production:

```sh theme={"system"}
truss push --publish
```


# Deploy and iterate
Source: https://docs.baseten.co/development/model/deploy-and-iterate

Deploy your model and quickly iterate on it.

In [Your First Model](/development/model/build-your-first-model), we walked through
how to deploy a basic model to Baseten. If you are trying to rapidly make changes
and iterate on your model, you'll notice that there is quite a bit of time between
running `truss push --publish` and when the changes are reflected on Baseten.

Also, a lot of models require special hardware that you may not immediately have
access to.

To solve this problem, we have a feature called **Truss Watch**, that allows you to
live reload your model as you work.

# Truss Watch

To make use of `truss watch`, start by deploying your model as a development deployment:

```bash theme={"system"}
$ truss push --watch
```

This will deploy a "development" version of your model with live reload enabled. The model
has a live reload server attached to it and supports hot reloading. To continue the hot reload
loop, simply run `truss watch` afterwards:

```bash theme={"system"}
$ truss watch
```

Now, if you make changes to your model, you'll see them reflected in the model logs!

You can now happily iterate on your model without having to go through the entire
build & deploy loop between each change.

# Ready for Production?

Once you've iterated on your model, and you're ready to deploy it to production,
you can use the `truss push --publish` command. This will deploy a "published"
version of your model

```bash theme={"system"}
truss push --publish
```

Note that development models have slightly worse performance, and have more
limited scaling properties, so it's highly recommended to not use these for
any production use case.


# Access model environments
Source: https://docs.baseten.co/development/model/environments

A guide to leveraging environments in your models

Model environments help configure behavior based on **deployment stage** (e.g., production vs. staging). You can access the environment details via `kwargs` in the `Model` class.

## 1. Retrieve Environment Variables

Access the environment in `__init__`:

```python theme={"system"}
def __init__(self, **kwargs):
    self._environment = kwargs["environment"]
```

## 2. Configure Behavior Based on Environment

Use environment variables in the `load` function:

```python theme={"system"}
def load(self):
    if self._environment.get("name") == "production":
        # Production setup
        self.setup_sentry()
        self.setup_logging(level="INFO")
        self.load_production_weights()
    else:
        # Default setup for staging or development deployments
        self.setup_logging(level="DEBUG")
        self.load_default_weights()
```

**Why use this?**

* **Customize logging levels**
* **Load environment-specific model weights**
* **Enable monitoring tools (e.g., Sentry)**


# gRPC 🆕
Source: https://docs.baseten.co/development/model/grpc

Invoke your model over gRPC.

## Overview

gRPC is a high-performance, open-source remote procedure call (RPC) framework that uses HTTP/2 for transport and Protocol Buffers for serialization. Unlike traditional HTTP APIs, gRPC provides strong type safety, high performance, and built-in support for streaming and bidirectional communication.

**Why use gRPC with Baseten?**

* **Type safety**: Protocol Buffers ensure strong typing and contract validation between client and server
* **Ecosystem integration**: Easily integrate Baseten with existing gRPC-based services
* **Streaming support**: Built-in support for server streaming, client streaming, and bidirectional streaming
* **Language interoperability**: Generate client libraries for multiple programming languages from a single `.proto` file

## gRPC on Baseten

gRPC support in Baseten is implemented using [Custom Servers](/development/model/custom-server). Unlike standard Truss models that use the `load()`, and `predict()` methods, gRPC models run their own server process that handles gRPC requests directly.

This approach gives developers full control over the gRPC server implementation.

For this to work, you must first package your gRPC server code into a Docker image.
Once that is done, you can set up your Truss `config.yaml` to configure your deployment
and push the server to Baseten.

## Setup

### Installation

1. **Install Truss:**
   ```bash theme={"system"}
   pip install --upgrade truss
   ```

2. **Install Protocol Buffer compiler:**
   ```bash theme={"system"}
   # On macOS
   brew install protobuf

   # On Ubuntu/Debian
   sudo apt-get install protobuf-compiler

   # On other systems, see: https://protobuf.dev/getting-started/
   ```

3. **Install gRPC tools:**
   ```bash theme={"system"}
   pip install grpcio-tools
   ```

### Protocol Buffer Definition

Your gRPC service starts with a `.proto` file that defines the service interface and message types. Create an `example.proto` file in your project root:

```protobuf example.proto theme={"system"}
syntax = "proto3";

package example;

// The greeting service definition
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name
message HelloRequest {
  string name = 1;
}

// The response message containing the greeting
message HelloReply {
  string message = 1;
}
```

#### Generate Protocol Buffer Code

Generate the Python code from your `.proto` file:

```bash theme={"system"}
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --proto_path . example.proto
```

This generates the necessary Python files (`example_pb2.py` and `example_pb2_grpc.py`) for your gRPC service. For more information about Protocol Buffers, see the [official documentation](https://protobuf.dev/).

### Model Implementation

Create your gRPC server implementation in a file called `model.py`. Here's a basic example:

```python model.py theme={"system"}
import grpc
from concurrent import futures
import time
import example_pb2
import example_pb2_grpc

from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_health.v1.health import HealthServicer


class GreeterServicer(example_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        response = example_pb2.HelloReply()
        response.message = f"Hello, {request.name}!"
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    example_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    # The gRPC health check service must be used in order for Baseten
    # to consider the gRPC server healthy.
    health_servicer = HealthServicer()
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    health_servicer.set(
        "example.GreeterService", health_pb2.HealthCheckResponse.SERVING
    )

    # Ensure the server runs on port 50051
    server.add_insecure_port("[::]:50051")

    server.start()
    print("gRPC server started on port 50051")

    # Keep the server running
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.stop(0)


if __name__ == "__main__":
    serve()
```

## Deployment

### Step 1: Create a Dockerfile

Since gRPC on Baseten requires a custom server setup, you'll need to create a `Dockerfile` that bundles your gRPC server code and dependencies. Here's a basic skeleton:

```dockerfile Dockerfile theme={"system"}
FROM debian:latest

RUN apt-get update && apt-get install -y \
    build-essential \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model.py ./model.py
COPY example_pb2.py example_pb2_grpc.py ./

EXPOSE 8080

CMD ["python", "model.py"]

```

Create a `requirements.txt` file with your gRPC dependencies:

```txt requirements.txt theme={"system"}
grpcio
grpcio-health-checking
grpcio-tools
protobuf
```

### Step 2: Build and Push Docker Image

Build and push your Docker image to a container registry:

```bash theme={"system"}
docker build -t your-registry/truss-grpc-demo:latest . --platform linux/amd64
docker push your-registry/truss-grpc-demo:latest
```

<Tip>
  Replace `your-registry` with your actual container registry (e.g., Docker Hub, Google Container Registry, AWS ECR). You can create a Docker Hub container registry by [following their documentation](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/#try-it-out).
</Tip>

### Step 3: Configure Your Truss

Update your `config.yaml` to use the custom Docker image and configure the gRPC server:

```yaml config.yaml theme={"system"}
model_name: "gRPC Model Example"
base_image:
  image: your-registry/truss-grpc-demo:latest
docker_server:
  start_command: python model.py
  # 50051 is the only supported server port.
  server_port: 50051
  # Note that the _endpoint fields are ignored for gRPC models.
  predict_endpoint: /
  readiness_endpoint: /
  liveness_endpoint: /
resources:
  accelerator: L4  # or your preferred GPU
  use_gpu: true
runtime:
  transport:
    kind: "grpc"
```

### Step 4: Deploy with Truss

Deploy your model using the Truss CLI. You need to use the `--promote` or `--publish` flags, since gRPC models aren't supported in the development environment.

```bash theme={"system"}
truss push --promote
```

For more detailed information about Truss deployment, see the [truss push documentation](/reference/cli/truss/push).

## Calling Your Model

### Using a gRPC Client

Once deployed, you can call your model using any gRPC client. Here's an example Python client:

```python client.py theme={"system"}
import grpc
import example_pb2
import example_pb2_grpc


def run():
    channel = grpc.secure_channel(
        "model-{MODEL_ID}.grpc.api.baseten.co:443",
        grpc.ssl_channel_credentials(),
    )

    stub = example_pb2_grpc.GreeterStub(channel)

    request = example_pb2.HelloRequest(name="World")

    metadata = [
        ("baseten-authorization", "Api-Key {API_KEY}"),
        ("baseten-model-id", "model-{MODEL_ID}"),
    ]

    response = stub.SayHello(request, metadata=metadata)
    print(response.message)


if __name__ == "__main__":
    run()


```

### Inference for specific environments and deployments

If you want to perform inference against a specific environment or deployment,
you can do so by adding headers to your gRPC calls:

**Target a specific environment:**

```python theme={"system"}
metadata = [
    ('authorization', 'Api-Key YOUR_API_KEY'),
    ('baseten-model-id', 'model-{YOUR_MODEL_ID}'),
    ('x-baseten-environment', 'staging'),
]
```

**Target a specific deployment ID:**

```python theme={"system"}
metadata = [
    ('authorization', 'Api-Key YOUR_API_KEY'),
    ('baseten-model-id', 'model-{YOUR_MODEL_ID}'),
    ('x-baseten-deployment', 'your-deployment-id'),
]
```

### Testing Your Deployment

Run your client to test the deployed model:

```bash theme={"system"}
python client.py
```

# Full Example

See this [Github repository](https://github.com/basetenlabs/truss-examples/tree/main/grpc) for a full example.

# Scaling and  Monitoring

## Scaling

While many gRPC requests follow the traditional request-response pattern, gRPC also supports
bidirectional streaming and long-lived connections. The implication of this is that
a single long-lived connection, even if no data is being sent, will count
against the concurrency target for the deployment.

## Promotion

Just like with HTTP, you can promote a gRPC deployment to an environment via the REST API or UI.

When promoting a gRPC deployment, new connections will be routed to the new deployment, but existing
connections will remain connected to the current deployment until a termination happens.
Depending on the length of the connection, this could result in old deployments taking longer to scale down
than for HTTP deployments.

# Monitoring

Just like with HTTP deployment, with gRPC, we offer metrics on the performance
of the deployment.

## Inference volume

Inference volume is tracked as the number of RPCs per minute. These
metrics are published *after* the request is complete.

See [gRPC status codes](https://grpc.io/docs/guides/status-codes/) for a full list
of codes.

## End-to-end response time

Measured at different percentiles (p50, p90, p95, p99):

End-to-end response time includes cold starts, queuing, and inference (excludes client-side latency). Reflects real-world performance.


# Implementation
Source: https://docs.baseten.co/development/model/implementation

How to implement your model.

In this section, we'll cover how to implement the actual logic for your model.

As was mentioned in [Your First Model](/development/model/build-your-first-model), the
logic for the model itself is specified in a `model/model.py` file. To recap, the simplest
directory structure for a model is:

```
model/
  model.py
config.yaml
```

It's expected that the `model.py` file contains a class with particular methods:

```python model.py theme={"system"}
class Model:
  def __init__(self):
    pass

  def load(self):
    pass

  def predict(self, input_data):
    pass
```

* The `__init__` method is used to initialize the `Model` class, and allows you to read
  in configuration parameters and other information.
* The `load` method is where you define the logic for initializing the model. This might
  include downloading model weights, or loading them onto a GPU.
* The `predict` method is where you define the logic for inference.

In the next sections, we'll cover each of these methods in more detail.

## **init**

As mentioned above, the `__init__` method is used to initialize the `Model` class, and allows you to
read in configuration parameters and runtime information.

The simplest signature for `__init__` is:

```python model.py theme={"system"}
def __init__(self):
  pass
```

If you need more information, however, you have the option to define your **init** method
such that it accepts the following parameters:

```python model.py theme={"system"}
def __init__(self, config: dict, data_dir: str, secrets: dict, environment: str):
  pass
```

* `config`: A dictionary containing the config.yaml for the model.
* `data_dir`: A string containing the path to the data directory for the model.
* `secrets`: A dictionary containing the secrets for the model. Note that at runtime,
  these will be populated with the actual values as stored on Baseten.
* `environment`: A string containing the environment for the model, if the model has been
  deployed to an environment.

You can then make use of these parameters in the rest of your model but saving these as
attributes:

```python model.py theme={"system"}
def __init__(self, config: dict, data_dir: str, secrets: dict, environment: str):
  self._config = config
  self._data_dir = data_dir
  self._secrets = secrets
  self._environment = environment
```

## load

The `load` method is where you define the logic for initializing the model. As
mentioned before, this might include downloading model weights or loading them
onto the GPU.

`load`, unlike the other method mentioned, does not accept any parameters:

```python model.py theme={"system"}
def load(self):
  pass
```

After deploying your model, the deployment will not be considered "Ready" until `load` has
completed successfully. Note that there is a **timeout of 30 minutes** for this, after which,
if `load` has not completed, the deployment will be marked as failed.

## predict

The `predict` method is where you define the logic for performing inference.

The simplest signature for `predict` is:

```python model.py theme={"system"}
def predict(self, input_data) -> str:
  return "Hello"
```

The return type of `predict` must be JSON-serializable, so it can be:

* `dict`
* `list`
* `str`

If you would like to return a more strictly typed object, you can return a
`Pydantic` object.

```python model.py theme={"system"}
from pydantic import BaseModel

class Result(BaseModel):
  value: str
```

You can then return an instance of this model from `predict`:

```python model.py theme={"system"}
def predict(self, input_data) -> Prediction:
  return Result(value="Hello")
```

### Streaming

In addition to supporting a single request/response cycle, Truss also supports streaming.

See the [Streaming](/development/model/streaming) guide for more information.

### Async vs. Sync

Note that the `predict` method is synchronous by default. However, if your model inference
depends on APIs require `asyncio`, `predict` can also be written as a coroutine.

```python model.py theme={"system"}
import asyncio

async def predict(self, input_data) -> dict:
    # Async logic here

    await asyncio.sleep(1)
    return {"value": "Hello"}
```

<Warning>
  If you are using `asyncio` in your `predict` method, be sure not to perform any blocking
  operations, such as a synchronous file download. This can result in degraded performance.
</Warning>


# Cached weights 🆕
Source: https://docs.baseten.co/development/model/model-cache

Accelerate cold starts and availability by prefetching and caching your weights.

<Tip>
  ### What is a "cold start"?

  "Cold start" is a term used to describe the time taken when a request is received when the model is scaled to 0 until it is ready to handle the first request. This process is a critical factor in allowing your deployments to be responsive to traffic while maintaining your SLAs and lowering your costs.
  To optimize cold starts, we will go over the following stategies: Downloading them in a background thread in Rust that runs during the module import, caching weights in a distributed filesystem, and moving weights into the docker image.

  In practice, this reduces the cold start for large models to just a few seconds. For example, Stable Diffusion XL can take a few minutes to boot up without caching. With caching, it takes just under 10 seconds.
</Tip>

## Enabling Caching + Prefetching for a Model

To enable caching, simply add `model_cache` to your `config.yaml` with a valid `repo_id`. The `model_cache` has a few key configurations:

* `repo_id` (required): The repo name from Hugging Face or bucket/container from GCS, S3, or Azure.
* `revision` (required for Hugging Face): The revision of the huggingface repo, such as the sha or branch name such as `refs/pr/1` or `main`. Not needed for GCS, S3, or Azure.
* `use_volume`: Boolean flag to determine if the weights are downloaded to the Baseten Distributed Filesystem at runtime (recommended) or bundled into the container image (legacy, not recommended).
* `volume_folder`: string, folder name under which the model weights appear. Setting it to `my-llama-model` will mount the repo to `/app/model_cache/my-llama-model` at runtime.
* `allow_patterns`: Only cache files that match specified patterns. Utilize Unix shell-style wildcards to denote these patterns.
* `ignore_patterns`: Conversely, you can also denote file patterns to ignore, hence streamlining the caching process.
* `runtime_secret_name`: The name of your secret containing the credentials for a private repository or bucket, such as a `hf_access_token` or `gcs_service_account`.
* `kind`: The storage provider type for the model weights.
  * `"hf"` (default): Hugging Face
  * `"gcs"`: Google Cloud Storage
  * `"s3"`: AWS S3
  * `"azure"`: Azure Blob Storage

Here is an example of a well written `model_cache` for Stable Diffusion XL. Note how it only pulls the model weights that it needs using `allow_patterns`.

```yaml config.yaml theme={"system"}
model_cache:
  - repo_id: madebyollin/sdxl-vae-fp16-fix
    revision: 207b116dae70ace3637169f1ddd2434b91b3a8cd
    use_volume: true
    volume_folder: sdxl-vae-fp16
    allow_patterns:
      - config.json
      - diffusion_pytorch_model.safetensors
  - repo_id: stabilityai/stable-diffusion-xl-base-1.0
    revision: 462165984030d82259a11f4367a4eed129e94a7b
    use_volume: true
    volume_folder: stable-diffusion-xl-base
    allow_patterns:
      - "*.json"
      - "*.fp16.safetensors"
      - sd_xl_base_1.0.safetensors
  - repo_id: stabilityai/stable-diffusion-xl-refiner-1.0
    revision: 5d4cfe854c9a9a87939ff3653551c2b3c99a4356
    use_volume: true
    volume_folder: stable-diffusion-xl-refiner
    allow_patterns:
      - "*.json"
      - "*.fp16.safetensors"
      - sd_xl_refiner_1.0.safetensors
```

Many Hugging Face repos have model weights in different formats (`.bin`, `.safetensors`, `.h5`, `.msgpack`, etc.). You only need one of these most of the time. To minimize cold starts, ensure that you only cache the weights you need.

<Tip>
  ### What is weight "pre-fetching"?

  With `model_cache`, weights are pre-fetched by downloading your weights ahead of time in a dedicated Rust thread.
  This means, you can perform all kinds of preparation work (importing libraries, jit compilation of torch/triton modules), until you need access to the files.
  In practice, executing statements like `import tensorrt_llm` typically take 10–15 seconds. By that point, the first 5–10GB of the weights will have already been downloaded.
</Tip>

To use the `model_cache` config with truss,  we require you to actively interact with the `lazy_data_resolver`.
Before using any of the downloaded files, you must call the `lazy_data_resolver.block_until_download_complete()`. This will block until all files in the `/app/model_cache` directory are downloaded & ready to use.
This call must be either part of your `__init__` or `load` implementation.

```python model.py theme={"system"}
# <- download is invoked before here.
import torch # this line usually takes 2-5 seconds.
import tensorrt_llm # this line usually takes 10-15 seconds
import onnxruntime # this line usually takes 5-10 seconds

class Model:
    """example usage of `model_cache` in truss"""
    def __init__(self, *args, **kwargs):
        # `lazy_data_resolver` is passed as keyword-argument in init
        self._lazy_data_resolver = kwargs["lazy_data_resolver"]

    def load(self):
        # work that does not require the download may be done beforehand
        random_vector = torch.randn(1000)
        # important to collect the download before using any incomplete data
        self._lazy_data_resolver.block_until_download_complete()
        # after the call, you may use the /app/model_cache directory and the contents
        torch.load(
            "/app/model_cache/stable-diffusion-xl-base/model.fp16.safetensors"
        )
```

## Private Repositories/Cloud Storage

### Private Hugging Face repositories 🤗

For any public Hugging Face repo, you don't need to do anything else. Adding the `model_cache` key with an appropriate `repo_id` should be enough.

However, if you want to deploy a model from a gated repo like [Llama 2](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get Hugging Face API Key">
    [Grab an API key](https://huggingface.co/settings/tokens) from Hugging Face with `read` access. Make sure you have access to the model you want to serve.
  </Step>

  <Step title="Add it to Baseten Secrets Manager">
    Paste your API key in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, such as `hf_access_token`. You can read more about secrets [here](/development/model/secrets).
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, add the secret key under `runtime_secret_name`:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: your-org/your-private-repo
      revision: main # refs/pr/1
      runtime_secret_name: hf_access_token
    ```

    Note: Once your truss is pushed, we resolve the sha behind your branch (main), and protect the deployment against changes on this branch.
  </Step>
</Steps>

If you run into any issues, run through all the steps above again and make sure you did not misspell the name of the repo or secret name, or paste an incorrect API key.

### Private GCS Buckets

If you want to deploy a model from a private GCS bucket to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get GCS Service Account Key">
    Create a [service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating) in your GCS account for the project which contains the model weights.
  </Step>

  <Step title="Add it to Baseten Secrets Manager">
    Paste the contents of the `service_account.json` in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, e.g. `gcs_service_account`. You can read more about secrets [here](/development/model/secrets).

    At a minimum, you should have these credentials:

    ```json gcs_service_account theme={"system"}
      {
        "private_key_id": "xxxxxxx",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMI",
        "client_email": "b10-some@xxx-example.iam.gserviceaccount.com"
      }
    ```
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, make sure to add the `runtime_secret_name` to your `model_cache` matching the above secret name:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: gs://your-private-bucket
      use_volume: true
      volume_folder: your-model-weights
      runtime_secret_name: gcs_service_account
      kind: "gcs"
      ignore_patterns: "*.protobuf"
    ```

    Note: S3/Azure/GCS Buckets are immutable. Once the truss is pushed, you may no longer delete or modify files as they are referenced as required files for a model startup.
  </Step>
</Steps>

It's easy to make a mistake in any of these steps. If you run into issues, you're encouraged to go through the steps again just in case. Please contact [Baseten support](mailto:support@baseten.co) if you continue to experience issues.

### Private S3 Buckets

If you want to deploy a model from a private S3 bucket to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get S3 credentials">
    [Get the your `access_key_id` and `secret_access_key`](https://aws.amazon.com/blogs/security/how-to-find-update-access-keys-password-mfa-aws-management-console/) in your AWS account for the bucket that contains the model weights.
  </Step>

  <Step title="Add them to Baseten Secrets Manager">
    Paste the following `json` in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, e.g. `aws_secret_json`. You can read more about secrets [here](/development/model/secrets).

    ```json aws_secret_json theme={"system"}
      {
        "access_key_id": "XXXXX",
        "secret_access_key": "xxxxx/xxxxxx",
        "region": "us-west-2"
      }
    ```
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, make sure to add the `runtime_secret_name` to your `model_cache` matching the above secret name:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: s3://your-bucket-west-2-name/path/to/model/
      use_volume: true
      volume_folder: your-model-weights # sync of s3 path/to/model/* to /app/model_cache/your-model-weights/*
      runtime_secret_name: aws_secret_json
      kind: "s3"
      ignore_patterns: "*.protobuf"
    ```

    Note: S3/Azure/GCS Buckets are immutable. Once the truss is pushed, you may no longer delete or modify files as they are referenced as required files for a model startup.
  </Step>
</Steps>

It's easy to make a mistake in any of these steps. If you run into issues, you're encouraged to go through the steps again just in case. Please contact [Baseten support](mailto:support@baseten.co) if you continue to experience issues.

### Private Azure Containers

If you want to deploy a model from a private Azure container to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get Azure credentials">
    [Get the your `account_key`](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-get-info?tabs=portal#get-a-connection-string-for-the-storage-account) in your Azure account with the container that has the model weights.
  </Step>

  <Step title="Add them to Baseten Secrets Manager">
    Paste the following `json` in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, e.g. `azure_secret_json`. You can read more about secrets [here](/development/model/secrets).

    ```json azure_secret_json theme={"system"}
      {
          "account_key": "xxxxx",
      }
    ```
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, make sure to add the `runtime_secret_name` to your `model_cache` matching the above secret name:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: az://your-private-container/path/to/model/
      use_volume: true
      volume_folder: your-model-weights
      runtime_secret_name: azure_secret_json
      kind: "azure"
      ignore_patterns: "*.protobuf"
    ```

    Note: S3/Azure/GCS Buckets are immutable. Once the truss is pushed, you may no longer delete or modify files as they are referenced as required files for a model startup.
  </Step>
</Steps>

It's easy to make a mistake in any of these steps. If you run into issues, you're encouraged to go through the steps again just in case. Please contact [Baseten support](mailto:support@baseten.co) if you continue to experience issues.

## `model_cache` within Chains

To use `model_cache` for [chains](/development/chain/getting-started) - use the `Assets` specifier. In the example below, we will download `llama-3.2-1B`.
As this model is a gated huggingface model, we are setting the mounting token as part of the assets `chains.Assets(..., secret_keys=["hf_access_token"])`.
The model is quite small - in many cases, we will be able to download the model while `from transformers import pipeline` and `import torch` are running.

```python chain_cache.py theme={"system"}
import random
import truss_chains as chains

try:
    # imports on global level for PoemGeneratorLM, to save time during the download.
    from transformers import pipeline
    import torch
except ImportError:
    # RandInt does not have these dependencies.
    pass

class RandInt(chains.ChainletBase):
    async def run_remote(self, max_value: int) -> int:
        return random.randint(1, max_value)

@chains.mark_entrypoint
class PoemGeneratorLM(chains.ChainletBase):
    from truss import truss_config
    LLAMA_CACHE = truss_config.ModelRepo(
        repo_id="meta-llama/Llama-3.2-1B-Instruct",
        revision="c4219cc9e642e492fd0219283fa3c674804bb8ed",
        use_volume=True,
        volume_folder="llama_mini",
        ignore_patterns=["*.pth", "*.onnx"]
    )
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            # The phi model needs some extra python packages.
            pip_requirements=[
                "transformers==4.48.0",
                "torch==2.6.0",
            ]
        ),
        compute=chains.Compute(
            gpu="L4"
        ),
        # The phi model needs a GPU and more CPUs.
        # compute=chains.Compute(cpu_count=2, gpu="T4"),
        # Cache the model weights in the image
        assets=chains.Assets(cached=[LLAMA_CACHE], secret_keys=["hf_access_token"]),
    )
    # <- Download happens before __init__ is called.
    def __init__(self, rand_int=chains.depends(RandInt, retries=3)) -> None:
        self._rand_int = rand_int
        print("loading cached llama_mini model")
        self.pipeline = pipeline(
            "text-generation",
            model=f"/app/model_cache/llama_mini",
        )

    async def run_remote(self, max_value: int = 3) -> str:
        num_repetitions = await self._rand_int.run_remote(max_value)
        print("writing poem with num_repetitions", num_repetitions)
        poem = str(self.pipeline(
            text_inputs="Write a beautiful and descriptive poem about the ocean. Focus on its vastness, movement, and colors.",
            max_new_tokens=150,
            do_sample=True,
            return_full_text=False,
            temperature=0.7,
            top_p=0.9,
        )[0]['generated_text'])
        return poem * num_repetitions
```

## `model_cache` for custom servers

If you are not using Python's `model.py` and [custom servers](/development/model/custom-server) such as [vllm](/examples/vllm), TEI or [sglang](/examples/sglang),
you are required to use the `truss-transfer-cli` command, to force population of the `/app/model_cache` location. The command will block until the weights are downloaded.

Here is an example for how to use text-embeddings-inference on a L4 to populate a jina embeddings model from huggingface into the model\_cache.

```yaml config.yaml theme={"system"}
base_image:
  image: baseten/text-embeddings-inference-mirror:89-1.6
docker_server:
  liveness_endpoint: /health
  predict_endpoint: /v1/embeddings
  readiness_endpoint: /health
  server_port: 7997
  # using `truss-transfer-cli` to download the weights to `cached_model`
  start_command: bash -c "truss-transfer-cli && text-embeddings-router --port 7997
    --model-id /app/model_cache/my_jina --max-client-batch-size 128 --max-concurrent-requests
    128 --max-batch-tokens 16384 --auto-truncate"
model_cache:
- repo_id: jinaai/jina-embeddings-v2-base-code
  revision: 516f4baf13dec4ddddda8631e019b5737c8bc250
  use_volume: true
  volume_folder: my_jina
  ignore_patterns: ["*.onnx"]
model_metadata:
  example_model_input:
    encoding_format: float
    input: text string
    model: model
model_name: TEI-jinaai-jina-embeddings-v2-base-code-truss-example
resources:
  accelerator: L4
```

## Optimizing cache hits and access time futher with b10cache enabled

<Warning>
  Requires `use_volume: true` and [b10cache](/development/model/b10cache) enabled. Without b10cache enabled, scaling the model with download the weights again.
</Warning>

To further reduce weights loading time, we can enable Baseten's Distributed Filesystem (b10cache) for your account.
You can validate that this is enabled for your account by viewing the logs of your deployment.

```
[2025-09-10 01:04:35] [INFO ] b10cache is enabled.
[2025-09-10 01:04:35] [INFO ] Symlink created successfully. Skipping download for /app/model_cache/cached_model/model.safetensors
```

<Tip>
  Once b10cache is active, we will skip downloads that are cached in the distributed filesystem of the region your deployment is running in.
  b10cache acts like a content delivery network: Initial cache misses are populating the filesystem, unused files are garbage collected 4 days after their last usage.
  Once b10cache is active, it will pull from the fastest source. If another pod is active on the same physical node, artifacts may be hot-cached, and shared among your deployments.
  Downloads are fully isolated from other organizations. Modifying downloaded artifacts inplace / without copy is not recommended.
</Tip>

If b10cache is not available for your account, we will provision the model\_cache with a optimized download from HuggingFace.co.
The download is parallellized, achieving typical download speeds of greater than 1GB/s on a 10Gbit ethernet connection.
If you want to enable b10cache, feel free to reach out to our support.


# Developing a Model on Baseten
Source: https://docs.baseten.co/development/model/overview

This page introduces the key concepts and workflow you'll use to package, configure, and iterate on models using Baseten's developer tooling.

Baseten makes it easy to go from a trained machine learning model to a fully-deployed, production-ready API. You'll use Truss—our open-source model packaging tool—to containerize your model code and configuration, and ship it to Baseten for deployment, testing, and scaling.

## What does it mean to develop a model?

In Baseten, developing a model means:

1. [Packaging your model code and weights](/development/model/implementation):
   Wrap your trained model into a structured project that includes your inference logic and dependencies.

2. [Configuring the model environment](/development/model/configuration):
   Define everything needed to run your model—from Python packages to system dependencies and secrets.

3. [Deploying and iterating quickly](/development/model/deploy-and-iterate):
   Push your model to Baseten in development mode and make live edits with instant feedback.

Once your model works the way you want, you can promote it to [production](/deployment/environments), ready for live traffic.

## Development flow on Baseten

Here's what the typical model development loop looks like:

1. **Initialize a new model project** using the Truss CLI.

2. **Add your model logic** to a Python class (model.py), specifying how to load and run inference.

3. **Configure dependencies** in a YAML or Python config.

4. **Deploy the model** in development mode using `truss push --watch`.

5. **Iterate fast** with `truss watch`—live-reload your dev deployment as you make changes.

6. **Test and tune** the model until it's production-ready.

7. **Promote the model** to production when you're ready to scale.

<Frame>
  <img />
</Frame>

<Note>
  **Note:** Truss runs your model in a standardized container without needing
  Docker installed locally. It also gives you a fast developer loop and a
  consistent way to configure and serve models.
</Note>

## What is Truss?

Truss is the tool you use to:

* **Scaffold a new model project**
* **Serve models locally or in the cloud**
* **Package your code, config, and model files**
* **Push to Baseten for deployment**

You can think of it as the developer toolkit for building and managing model servers—built specifically for machine learning workflows.

With Truss, you can create a containerized model server **without needing to learn Docker**, and define everything about how your model runs: Python and system packages, GPU settings, environment variables, and custom inference logic. It gives you a fast, reproducible dev loop—test changes locally or in a remote environment that mirrors production.

Truss is **flexible enough to support a wide range of ML stacks**, including:

* Model frameworks like PyTorch, transformers, and diffusers
* [Inference engines](/development/model/performance-optimization) like TensorRT-LLM, SGLang, vLLM
* Serving technologies like Triton
* Any package installable with `pip` or `apt`

We'll use Truss throughout this guide, but the focus will stay on **how you develop models**, not just how Truss works.

## From model to server: the key components

When you develop a model on Baseten, you define:

* A `Model` **class**: This is where your model is loaded, preprocessed, run, and the results returned.
* A **configuration file** (`config.yaml` or Python config): Defines the runtime environment, dependencies, and deployment settings.
* Optional **extra assets**, like model weights, secrets, or external packages.

These components together form a **Truss**, which is what you deploy to Baseten.

Truss simplifies and standardizes model packaging for seamless deployment. It encapsulates model code, dependencies, and configurations into a **portable, reproducible structure**, enabling efficient development, scaling, and optimization.

## Development vs. other deployments

The only special deployment is **development**.

* **Development deployment**
  Meant for iteration and testing. It supports [live-reloading](/development/model/deploy-and-iterate#truss-watch) for quick feedback loops and will only scale to **one replica**, no autoscaling.
* **All others deployments**
  Stable, autoscaled, and ready for live traffic but **don't support live-reloading**.

You'll use the dev deployment to build and test, then promote it to an environment like **staging** or **production** once you're satisfied.


# Performance optimization
Source: https://docs.baseten.co/development/model/performance-optimization

Optimize model latency, throughput, and cost with Baseten engines

Model performance means optimizing every layer of your model serving infrastructure to balance four goals:

1. **Latency**: How quickly does each user get output from the model?
2. **Throughput**: How many requests can the deployment handle at once?
3. **Cost**: How much does a standardized unit of work cost?
4. **Quality**: Does your model consistently deliver high-quality output after optimization?

## Performance engines

Baseten's performance-optimized engines deliver the best possible inference speed and efficiency:

### **[Engine-Builder-LLM](/engines/engine-builder-llm/overview)** - Dense Models

* **Best for**: Llama, Mistral, Qwen, and other causal language models
* **Features**: TensorRT-LLM optimization, lookahead decoding, quantization
* **Performance**: Lowest latency and highest throughput for dense models

### **[BIS-LLM](/engines/bis-llm/overview)** - MoE Models

* **Best for**: DeepSeek, Mixtral, and other mixture-of-experts models
* **Features**: V2 inference stack, expert routing, structured outputs
* **Performance**: Optimized for large-scale MoE inference

### **[BEI](/engines/bei/overview)** - Embedding Models

* **Best for**: Sentence transformers, rerankers, classification models
* **Features**: OpenAI-compatible, high-performance embeddings
* **Performance**: Fastest embedding inference with optimized batching

## Performance concepts

Detailed performance optimization guides are now organized in the **[Performance Concepts](/engines/performance-concepts/quantization-guide)** section:

* **[Quantization Guide](/engines/performance-concepts/quantization-guide)** - FP8/FP4 trade-offs and hardware requirements
* **[Structured Outputs](/engines/performance-concepts/structured-outputs)** - JSON schema validation and controlled generation
* **[Function Calling](/engines/performance-concepts/function-calling)** - Tool use and function selection
* **[Performance Client](/engines/performance-concepts/performance-client)** - High-throughput client library
* **[Deployment Guide](/engines/performance-concepts/deployment-from-training-and-s3)** - Training checkpoints and cloud storage

## ⚡ Quick performance wins

### **Quantization**

Reduce memory usage and improve speed with post-training quantization:

```yaml theme={"system"}
trt_llm:
  build:
    quantization_type: fp8  # 50% memory reduction
```

### **Lookahead Decoding**

Accelerate inference for predictable content (code, JSON):

```yaml theme={"system"}
trt_llm:
  build:
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 5
```

### **Performance Client**

Maximize client-side throughput with Rust-based client:

```bash theme={"system"}
pip install baseten-performance-client
```

## 🔧 Where to start

1. **Choose your engine**: [Engines overview](/engines)
2. **Configure your model**: Engine-specific configuration guides
3. **Optimize performance**: [Performance concepts](/engines/performance-concepts/quantization-guide)
4. **Deploy and monitor**: Use [performance client](/engines/performance-concepts/performance-client) for maximum throughput

***

**💡 Tip**: Start with the default engine configuration, then apply quantization and other optimizations based on your specific performance requirements.


# Private Docker registries
Source: https://docs.baseten.co/development/model/private-registries

A guide to configuring a private container registry for your truss

Truss uses containerized environments to ensure consistent model execution across deployments. When deploying a custom base image or a custom server from a private registry, you must grant Baseten access to download that image.

## AWS Elastic Cloud Registry (ECR)

AWS supports using either [service accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html), or [access tokens](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html#registry-auth-token) for short lived access for container registry authentication.

### AWS IAM Service accounts

To use an IAM service account for long-lived access, you can use the `AWS_IAM` authentication method in Truss.

1. Get an AWS\_ACCESS\_KEY\_ID and AWS\_SECRET\_ACCESS\_KEY from the AWS dashboard

2. Add these as [secrets](https://app.baseten.co/settings/secrets) in Baseten. These should be named `aws_access_key_id` and `aws_secret_access_key`
   respectively.

3. Choose the `AWS_IAM` authentication method when setting up your Truss. The `config.yaml` file should look something like this:

```
...
  base_image:
    image: <aws account id>.dkr.ecr.<region>.amazonaws.com/path/to/image
    docker_auth:
      auth_method: AWS_IAM
      registry: <aws account id>.dkr.ecr.<region>.amazonaws.com
  secrets:
    aws_access_key_id: null
    aws_secret_access_key: null
...
```

Note here that you need to specify the registry and image separately.

If you'd like to use different secret names besides the default, you can configure these using the
`aws_access_key_id_secret_name` and `aws_secret_access_key_secret_name` options
under `docker_auth`:

```
...
base_image:
  ...
  docker_auth:
    auth_method: AWS_IAM
    registry: <aws account id>.dkr.ecr.<region>.amazonaws.com
    aws_access_key_id_secret_name: custom_aws_access_key_secret
    aws_secret_access_key_secret_name: custom_aws_secret_key_secret
secrets:
  custom_aws_access_key_secret: null
  custom_aws_secret_key_secret: null

```

### Access Token

1. Get the a **Base64-encoded** secret:

```sh theme={"system"}
PASSWORD=`aws ecr get-login-password --region {us-east-1}`
echo -n "AWS:$PASSWORD" | base64
```

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `DOCKER_REGISTRY_{aws account id}.dkr.ecr.{us-east-1}.amazonaws.com` with the `Base64-encoded secret` as the value.

3. Add the secret name to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```yaml config.yaml theme={"system"}
secrets:
  DOCKER_REGISTRY_{aws account id}.dkr.ecr.{us-east-1}.amazonaws.com: null
```

## Google Cloud Artifact Registry

GCP supports using either [access tokens](https://cloud.google.com/artifact-registry/docs/docker/authentication#token) for short lived access or [service accounts](https://cloud.google.com/iam/docs/service-account-overview) for container registry authentication.

### Service Account

1. Get your [service account key](https://cloud.google.com/artifact-registry/docs/docker/authentication#json-key) as a JSON key blob.

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `gcp-service-account` (or similar) with the JSON key blob as the value.

3. Add the secret name that you used to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```yaml config.yaml theme={"system"}
secrets:
  gcp-service-account: null
```

4. Configure the `docker_auth` section of your `base_image:` to ensure that the service account authentication method will be used.

```
base_image:
  ...
  docker_auth:
    auth_method: GCP_SERVICE_ACCOUNT_JSON
    secret_name: gcp-service-account
    registry: {us-west2}-docker.pkg.dev
```

Note that here, `secret_name` should match the name of the secret that is contains the JSON key blob.

### Access Token

1. Get your [access token](https://cloud.google.com/artifact-registry/docs/docker/authentication#token)

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `DOCKER_REGISTRY_{us-west2}-docker.pkg.dev` with the `Base64-encoded secret` as the value.

3. Add the secret name to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```yaml config.yaml theme={"system"}
secrets:
  DOCKER_REGISTRY_{us-west2}-docker.pkg.dev: null
```

## Docker Hub

1. Get the a **Base64-encoded** secret:

```sh theme={"system"}
echo -n 'username:password' | base64
```

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `DOCKER_REGISTRY_https://index.docker.io/v1/` with the `Base64-encoded secret` as the value.

3. Add the secret name to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```
Name: DOCKER_REGISTRY_https://index.docker.io/v1/
Token: <Base64-encoded secret>
```

Then, this to `config.yaml`:

```yaml config.yaml theme={"system"}
secrets:
  DOCKER_REGISTRY_https://index.docker.io/v1/: null
```


# Using request objects / cancellation
Source: https://docs.baseten.co/development/model/requests

Get more control by directly using the request object.

Truss processes client requests by extracting and validating payloads. For **advanced use cases**, you can access the raw request object to:

* **Customize payload deserialization** (e.g., binary protocol buffers).
* **Handle disconnections and cancel long-running predictions.**

<Tip>You can mix request objects with standard inputs or use requests exclusively for performance optimization.</Tip>

## Using Request Objects in Truss

You can define request objects in `preprocess`, `predict`, and `postprocess`:

```python theme={"system"}
import fastapi

class Model:
    def preprocess(self, request: fastapi.Request):
        ...

    def predict(self, inputs, request: fastapi.Request):
        ...

    def postprocess(self, inputs, request: fastapi.Request):
        ...
```

### Rules for Using Requests

* The request must be **type-annotated** as `fastapi.Request`.
* If **only** requests are used, Truss **skips payload extraction** for better performance.
* If **both** request objects and standard inputs are used:
  * Request **must be the second argument**.
  * **Preprocessing transforms inputs**, but the request object remains unchanged.
  * `postprocess` cannot use only the request—it must receive the model’s output.
  * If `predict` only uses the request, `preprocess` cannot be used.

```python theme={"system"}
import fastapi, asyncio, logging

class Model:
    async def predict(self, inputs, request: fastapi.Request):
        await asyncio.sleep(1)
        if await request.is_disconnected():
            logging.warning("Cancelled before generation.")
            return  # Cancel request on the model engine here.

        for i in range(5):
            await asyncio.sleep(1.0)
            logging.warning(i)
            yield str(i)  # Streaming response
            if await request.is_disconnected():
                logging.warning("Cancelled during generation.")
                return  # Cancel request on the model engine here.
```

<Tip>You must implement request cancellation at the model level, which varies by framework.</Tip>

## Cancelling Requests in Specific Frameworks

### TRT-LLM (Polling-Based Cancellation)

For TensorRT-LLM, use `response_iterator.cancel()` to terminate streaming requests:

```python theme={"system"}
async for request_output in response_iterator:
    if await is_cancelled_fn():
        logging.info("Request cancelled. Cancelling Triton request.")
        response_iterator.cancel()
        return
```

<Note>See full example in [TensorRT-LLM Docs](https://developer.nvidia.com/tensorrt-llm).</Note>

### vLLM (Abort API)

For vLLM, use `engine.abort()` to stop processing:

```python theme={"system"}
async for request_output in results_generator:
    if await request.is_disconnected():
        await engine.abort(request_id)
        return
```

<Note>See full example in [vLLM Docs](https://docs.vllm.ai/en/latest/dev/engine/async_llm_engine.html#vllm.AsyncLLMEngine.generate).</Note>

## Unsupported Request Features

* **Streaming file uploads** – Use URLs instead of embedding large data in the request.
* **Client-side headers** – Most headers are stripped; include necessary metadata in the payload.


# Custom responses
Source: https://docs.baseten.co/development/model/responses

Get more control by directly creating the response object.

By default, Truss wraps prediction results into an HTTP response. For **advanced use cases**, you can create response objects manually to:

* **Control HTTP status codes.**
* **Use server-sent events (SSEs) for streaming responses.**

<Tip>You can return a response from predict or postprocess, but not both.</Tip>

## Returning Custom Response Objects

Any subclass of starlette.responses.Response is supported.

```python theme={"system"}
import fastapi

class Model:
    def predict(self, inputs) -> fastapi.Response:
        return fastapi.Response(...)
```

<Tip>If `predict` returns a response, `postprocess` cannot be used.</Tip>

## Example: Streaming with SSEs

For **server-sent events (SSEs)**, use `StreamingResponse`:

```python theme={"system"}
import time
from starlette.responses import StreamingResponse

class Model:
    def predict(self, model_input):
        def event_stream():
            while True:
                time.sleep(1)
                yield f"data: Server Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        return StreamingResponse(event_stream(), media_type="text/event-stream")
```

## Limitations

* **Response headers are not fully propagated** – include metadata in the response body.

<Info>
  Also see [Using Request Objects](/development/model/requests)
  for handling raw requests.
</Info>


# Secrets
Source: https://docs.baseten.co/development/model/secrets

Use secrets securely in your models

Truss allows you to securely manage API keys, access tokens, passwords, and other secrets without exposing them in code.

## Create a secret

<Tabs>
  <Tab title="Baseten UI">
    1. Go to [Secrets](https://app.baseten.co/settings/secrets) in your account settings.
    2. Enter the name and value of the secret, for example `hf_access_token` and `hf_...`.
    3. Select **Add secret**.
  </Tab>

  <Tab title="cURL">
    To create a secret with the API, use the following command:

    ```bash theme={"system"}
    curl --request POST \
      --url https://api.baseten.co/v1/secrets \
      --header "Authorization: Api-Key $BASETEN_API_KEY" \
      --data '{
        "name": "hf_access_token",
        "value": "hf_..."
      }'
    ```

    For more information, see the
    [Upsert a secret](/reference/management-api/secrets/upserts-a-secret) reference.
  </Tab>
</Tabs>

## Use secrets in your model

Once you've created a secret, declare it in your `config.yaml` and access it in your model code.

<Warning>
  Never store actual secret values in `config.yaml`. Use `null` as a placeholder.
  The secret in your `config.yaml` is a reference to the key in the secret manager.
</Warning>

Specify the reference to the secret in `config.yaml`:

```yaml config.yaml theme={"system"}
secrets:
  hf_access_token: null
```

Secrets are passed as keyword arguments to the `Model` class. To access them, store the secrets in `__init__`:

```python main.py theme={"system"}
def __init__(self, **kwargs):
    self._secrets = kwargs["secrets"]
```

Then use the secret in `load` or `predict` section of your model by accessing the secret using the key:

```python main.py theme={"system"}
def load(self):
    self._model = pipeline(
        "fill-mask",
        model="baseten/docs-example-gated-model",
        use_auth_token=self._secrets["hf_access_token"]
    )
```

## Use secrets in custom Docker images

When using [custom Docker images](/development/model/custom-server), Truss
injects secrets into your container at `/secrets/{secret_name}` instead of
passing them through `kwargs`.

You must specify the reference to the secret and then access it in your `start_command` or application code.

Specify the reference to the secret in `config.yaml`:

```yaml config.yaml theme={"system"}
secrets:
  hf_access_token: null
```

### Read secrets in your `start_command`

To read a secret in your `start_command`:

```yaml config.yaml theme={"system"}
docker_server:
  start_command: sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) my-server --port 8000"
```

### Read secrets in application code

To read a secret in application code:

```python main.py theme={"system"}
with open("/secrets/hf_access_token", "r") as f:
    hf_token = f.read().strip()
```


# Streaming output
Source: https://docs.baseten.co/development/model/streaming

Streaming Output for LLMs

Streaming output significantly reduces wait time for generative AI models by returning results as they are generated instead of waiting for the full response.

## Why streaming?

* ✅ **Faster response time** – Get initial results in under **1 second** instead of waiting **10+ seconds**.
* ✅ **Improved user experience** – Partial outputs are **immediately usable**.

This guide walks through **deploying Falcon 7B** with streaming enabled.

### 1. Initialize Truss

```sh theme={"system"}
truss init falcon-7b && cd falcon-7b
```

### 2: Implement Model (Non-Streaming)

This first version loads the Falcon 7B model **without** streaming:

```python model/model.py theme={"system"}
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from typing import Dict

CHECKPOINT = "tiiuae/falcon-7b-instruct"
DEFAULT_MAX_NEW_TOKENS = 150
DEFAULT_TOP_P = 0.95

class Model:
    def __init__(self, **kwargs) -> None:
        self.tokenizer = None
        self.model = None

    def load(self):
        self.tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)
        self.model = AutoModelForCausalLM.from_pretrained(
            CHECKPOINT, torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto"
        )

    def predict(self, request: Dict) -> Dict:
        prompt = request["prompt"]
        inputs = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True, padding=True)
        input_ids = inputs["input_ids"].to("cuda")
        generation_config = GenerationConfig(temperature=1, top_p=DEFAULT_TOP_P, top_k=40)

        with torch.no_grad():
            return self.model.generate(
                input_ids=input_ids,
                generation_config=generation_config,
                return_dict_in_generate=True,
                output_scores=True,
                pad_token_id=self.tokenizer.eos_token_id,
                max_new_tokens=DEFAULT_MAX_NEW_TOKENS,
            )
```

### 3. Add Streaming Support

To enable streaming, we:

* Use `TextIteratorStreamer` to stream tokens as they are generated.
* Run `generate()` in a **separate thread** to prevent blocking.
* Return a **generator** that streams results.

```python model/model.py theme={"system"}
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig, TextIteratorStreamer
from threading import Thread
from typing import Dict

CHECKPOINT = "tiiuae/falcon-7b-instruct"

class Model:
    def __init__(self, **kwargs) -> None:
        self.tokenizer = None
        self.model = None

    def load(self):
        self.tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)
        self.model = AutoModelForCausalLM.from_pretrained(
            CHECKPOINT, torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto"
        )

    def predict(self, request: Dict):
        prompt = request["prompt"]
        inputs = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True, padding=True)
        input_ids = inputs["input_ids"].to("cuda")

        streamer = TextIteratorStreamer(self.tokenizer)
        generation_config = GenerationConfig(temperature=1, top_p=0.95, top_k=40)

        def generate():
            self.model.generate(
                input_ids=input_ids,
                generation_config=generation_config,
                return_dict_in_generate=True,
                output_scores=True,
                pad_token_id=self.tokenizer.eos_token_id,
                max_new_tokens=150,
                streamer=streamer,
            )

        thread = Thread(target=generate)
        thread.start()

        def stream_output():
            for text in streamer:
                yield text
            thread.join()

        return stream_output()
```

### 4. Configure `config.yaml`

```yaml config.yaml theme={"system"}
model_name: falcon-streaming
requirements:
  - torch==2.0.1
  - peft==0.4.0
  - scipy==1.11.1
  - sentencepiece==0.1.99
  - accelerate==0.21.0
  - bitsandbytes==0.41.1
  - einops==0.6.1
  - transformers==4.31.0
resources:
  cpu: "4"
  memory: 16Gi
  use_gpu: true
  accelerator: L4
```

### 5. Deploy and invoke

Deploy the model for development:

```sh theme={"system"}
truss push --watch
```

Or deploy for production:

```sh theme={"system"}
truss push --publish
```

Invoke with:

```sh theme={"system"}
truss predict -d '{"prompt": "Tell me about falcons", "do_sample": true}'
```


# Torch compile caching 🆕
Source: https://docs.baseten.co/development/model/torch-compile-cache

Accelerate cold starts by loading in previous compilation artifacts.

<Warning>
  ### Requires [b10cache](/development/model/b10cache) enabled
</Warning>

## Overview

PyTorch's `torch.compile` feature offers significant performance improvements for inference workloads, reducing inference time by up to 40%. However, this optimization comes with a trade-off: the initial compilation process adds considerable latency to cold starts, as the model must be compiled before serving its first inference request.

This compilation overhead becomes particularly problematic in production environments where:

* Models frequently scale up and down based on demand
* New pods are regularly spawned to handle traffic spikes
* Each new instance must repeat the compilation process from scratch

## Solution

Persist compilation artifacts across deployments and pod restarts, by storing them in [b10cache](/development/model/b10cache). When a new pod starts up, it can load previously compiled artifacts instead of recompiling from scratch. The library gracefully handles large scale ups, managing race conditions and ensuring fault-tolerance in the shared b10cache.

In practice, this strategy slashes compilation latencies to just around 5-20 seconds, depending on the model.

***

## Implementation Options

There are two different deployment patterns that benefit from torch compile caching:

<Tip>
  * **Truss Models**: `model.py` calling `torch.compile` ([Jump to](#truss-models-model-py))
  * **vLLM Servers**: vLLM custom server ([Jump to](#vllm-servers-cli-tool))
</Tip>

***

## Truss Models (`model.py`)

### API Reference

We expose two API calls that return an `OperationStatus` object to help you control program flow based on the result.

<Accordion title="load_compile_cache()">
  If you have previously saved compilation cache for this model, load it to speed up the compilation for the model on this pod.

  **Returns:**

  * `OperationStatus.SUCCESS` → successful load
  * `OperationStatus.SKIPPED` → if torch compilation artifacts already exist on the pod
  * `OperationStatus.ERROR` → general catch-all errors
  * `OperationStatus.DOES_NOT_EXIST` → if no cache file was found
</Accordion>

<Accordion title="save_compile_cache()">
  Save your model's torch compilation cache for future use. This should be called after running prompts to warm up your model and trigger compilation.

  **Returns:**

  * `OperationStatus.SUCCESS` → successful save
  * `OperationStatus.SKIPPED` → skipped because compile cache already exists in shared directory
  * `OperationStatus.ERROR` → general catch-all errors
</Accordion>

### Implementation Example

Here is an example of compile caching for Flux, an image generation model. Note how we save the result of `load_compile_cache` to inform on whether to `save_compile_cache`.

#### Step 1: Update `config.yaml`

Under requirements, add `b10-transfer`:

```yaml theme={"system"}
requirements:
  - b10-transfer
```

#### Step 2: Update `model.py`

Import the library and use the two functions to speed up torch compilation time:

```python theme={"system"}
from b10_transfer import load_compile_cache, save_compile_cache, OperationStatus

class Model:
    def load(self):
        self.pipe = FluxPipeline.from_pretrained(
            self.model_name, torch_dtype=torch.bfloat16, token=self.hf_access_token
        ).to("cuda")

        # Try to load compile cache
        cache_loaded: OperationStatus = load_compile_cache()

        if cache_loaded == OperationStatus.ERROR:
            logging.info("Run in eager mode, skipping torch compile")
        else:
            logging.info("Compiling the model for performance optimization")
            self.pipe.transformer = torch.compile(
                self.pipe.transformer, mode="max-autotune-no-cudagraphs", dynamic=False
            )

            self.pipe.vae.decode = torch.compile(
                self.pipe.vae.decode, mode="max-autotune-no-cudagraphs", dynamic=False
            )

            seed = random.randint(0, MAX_SEED)
            generator = torch.Generator().manual_seed(seed)
            start_time = time.time()
            # Warmup the model with dummy prompts, also triggering compilation
            self.pipe(
                prompt="dummy prompt",
                prompt_2=None,
                guidance_scale=0.0,
                max_sequence_length=256,
                num_inference_steps=4,
                width=1024,
                height=1024,
                output_type="pil",
                generator=generator
            )

            end_time = time.time()

            logging.info(
                f"Warmup completed in {(end_time - start_time)} seconds. "
                "This is expected to take a few minutes on the first run."
            )

            if cache_loaded != OperationStatus.SUCCESS:
                # Save compile cache for future runs
                outcome: OperationStatus = save_compile_cache()
```

<Note>
  See the [full example](https://github.com/basetenlabs/truss-examples/tree/main/flux/schnell).
</Note>

***

## vLLM Servers (CLI Tool)

### Overview

This should be used whenever using compile options with vLLM. On vLLM V1, compiling is the default behavior. This command line tool spawns a process that is completely automatic—it loads the compile cache if you have saved it before, and if not, it will save the compile cache.

### Implementation

There are two changes to make in `config.yaml`:

#### Step 1: Add Requirements

Under requirements, add `b10-transfer`:

```yaml theme={"system"}
requirements:
  - b10-transfer
```

#### Step 2: Update Start Command

Under start command, add `b10-compile-cache &` right before the `vllm serve` call:

```yaml theme={"system"}
start_command: "... b10-compile-cache & vllm serve ..."
```

<Note>
  See the [full example](https://github.com/basetenlabs/truss-examples/tree/main/mistral/mistral-small-3.1).
</Note>

***

## Advanced Configuration

<Accordion title="Parameter Overrides">
  The torch compile caching library supports several environment variables for fine-tuning behavior in production environments:

  ### Cache Directory Configuration

  **`TORCHINDUCTOR_CACHE_DIR`** (optional)

  * **Default**: `/tmp/torchinductor_<username>`
  * **Description**: Directory where PyTorch stores compilation artifacts locally
  * **Allowed prefixes**: `/tmp/`, `/cache/`, `~/.cache`
  * **Usage**: Set this if you need to customize where torch compilation artifacts are stored on the local filesystem

  **`B10FS_CACHE_DIR`** (optional)

  * **Default**: Derived from b10cache mount point + `/compile_cache`
  * **Description**: Directory in b10cache where compilation artifacts are persisted across deployments
  * **Usage**: Typically doesn't need to be changed as it's automatically configured based on your b10cache setup

  **`LOCAL_WORK_DIR`** (optional)

  * **Default**: `/app`
  * **Description**: Local working directory for temporary operations
  * **Allowed prefixes**: `/app/`, `/tmp/`, `/cache/`

  ### Performance and Resource Limits

  **`MAX_CACHE_SIZE_MB`** (optional)

  * **Default**: `1024` (1GB)
  * **Cap**: Limited by `MAX_CACHE_SIZE_CAP_MB` for safety
  * **Description**: Maximum size of a single cache archive in megabytes
  * **Usage**: Increase for larger models with extensive compilation artifacts, decrease to save storage

  **`MAX_CONCURRENT_SAVES`** (optional)

  * **Default**: `50`
  * **Cap**: Limited by `MAX_CONCURRENT_SAVES_CAP` for safety
  * **Description**: Maximum number of concurrent save operations allowed
  * **Usage**: Tune based on your deployment's concurrency requirements and storage performance

  ### Cleanup and Maintenance

  **`CLEANUP_LOCK_TIMEOUT_SECONDS`** (optional)

  * **Default**: `30`
  * **Cap**: Limited by `LOCK_TIMEOUT_CAP_SECONDS`
  * **Description**: Timeout for cleaning up stale lock files, to prevent deadlocks. They may occur when a replica holding the lock crashes.
  * **Usage**: Decrease if you're experiencing deadlocks in high-load scenarios

  **`CLEANUP_INCOMPLETE_TIMEOUT_SECONDS`** (optional)

  * **Default**: `60`
  * **Cap**: Limited by `INCOMPLETE_TIMEOUT_CAP_SECONDS`
  * **Description**: Timeout for cleaning up incomplete cache files
  * **Usage**: Increase for slower storage systems or larger cache files

  ### Example Configuration

  ```yaml theme={"system"}
  # config.yaml
  environment_variables:
    MAX_CACHE_SIZE_MB: "2048"
    MAX_CONCURRENT_SAVES: "25"
    CLEANUP_LOCK_TIMEOUT_SECONDS: "45"
  ```

  <Note>
    Most users won't need to modify these settings. The defaults are optimized for typical production workloads. Only adjust these values if you're experiencing specific performance issues or have unusual deployment requirements.
  </Note>
</Accordion>

***

## Further Reading

To understand implementation details, read more [here](https://docs.pytorch.org/tutorials/recipes/torch_compile_caching_tutorial.html).


# WebSockets 🆕
Source: https://docs.baseten.co/development/model/websockets

Enable real-time, streaming, bidirectional communication using WebSockets for Truss models and Chainlets.

## Overview

WebSockets provide a persistent, full-duplex communication channel between clients and server-side models or chains. Full duplex means that chunks of data can be sent client→server and server→client simultaneously and repeatedly.

This guide covers how to implement WebSocket-based interactions for Truss models and Chains/Chainlets.

Unlike traditional request-response models, WebSockets allow continuous data exchange without reopening connections. This is useful for real-time applications, streaming responses, and maintaining lightweight interactions. Example applications could be real-time audio transcription, AI phone calls or agents with turn-based interactions. WebSockets are also useful for situations where you want to manage some state on the server-side, and you want requests that are part of the same "session" to always be routed to the replica that maintains that state.

## WebSocket Usage in Truss Models

In Truss models, WebSockets replace the conventional request/response flow: a single `websocket` method handles all processing and input/output communication goes through the WebSocket object (not arguments and return values). There are no separate `preprocess`, `predict`, and `postprocess` methods anymore, but you can still implement `load`.

1. **Initialize your Truss**:

```bash theme={"system"}
truss init websocket-model
```

For more detailed information about this command, refer to the [truss init documentation](reference/cli/truss/init).

2. Replace the `predict` method with a `websocket` method to your Truss in `model/model.py`. For example:

```python theme={"system"}
import fastapi

class Model:
    async def websocket(self, websocket: fastapi.WebSocket):
        try:
            while True:
                message = await websocket.receive_text()
                await websocket.send_text(f"WS obtained: {message}")
        except fastapi.WebSocketDisconnect:
            pass
```

3. Set `runtime.transport.kind=websocket` in `config.yaml`:

```yaml theme={"system"}
...
runtime:
  transport:
    kind: websocket
```

### Key Points

* Continuous message exchange occurs in a loop until client disconnection. You can also decide to close the connection server-side if a certain condition is reached
  * This is done by calling `websocket.close()`
* WebSockets enable bidirectional streaming, avoiding the need for multiple HTTP requests (or return values).
* You must not implement any of the traditional methods `predict`, `preprocess`, or `postprocess`.
* The WebSocket object passed to the `websocket` method has already accepted the connection, so you must not call `websocket.accept()` on it. You may close the connection though at the end of your processing. If you don’t close it explicitly, it will be closed after exiting your `websocket` method.

### Invocation

Using `websocat` ([get it](https://github.com/vi/websocat)), you can call the model like this:

```bash theme={"system"}
websocat -H="Authorization: Api-Key $BASETEN_API_KEY" \
   wss://model-{MODEL_ID}.api.baseten.co/environments/production/websocket
Hello # Your input.
WS obtained: Hello # Echoed from model.
# ctrl+c to close connection.
```

<Note>
  The path you use depends on which environment or deployment of the model you'd like to call.

  * Environment: `wss://model-{MODEL_ID}.api.baseten.co/environments/{ENVIRONMENT_NAME}/websocket`.
  * Deployment: `wss://model-{MODEL_ID}.api.baseten.co/deployment/{DEPLOYMENT_NAME}/websocket`.

  See [Reference](reference/inference-api/predict-endpoints/environments-websocket) for the full details.
</Note>

## WebSocket Usage in Chains/Chainlets

For Chains, WebSockets are wrapped in a reduced API object `WebSocketProtocol`. All processing happens in the `run_remote` method as usual. But inputs as well as outputs (or “return values”) are sent through the WebSocket object using async `send_{X}` and `receive_{X}` methods (there are variants for `text`, `bytes` and `json)`. As a convenience, there's also a `receive` method that can passthrough both `str` and `bytes` types.

### Implementation Example

```python theme={"system"}
import fastapi
import truss_chains as chains

class Dependency(chains.ChainletBase):
    async def run_remote(self, name: str) -> str:
        return f"Hello from dependency, {name}."

@chains.mark_entrypoint
class WSEntrypoint(chains.ChainletBase):
    def __init__(self, dependency=chains.depends(Dependency)):
        self._dependency = dependency

    async def run_remote(self, websocket: chains.WebSocketProtocol) -> None:
        try:
            while True:
                message = await websocket.receive_text()
                if message == "dep":
                    response = await self._dependency.run_remote("WSEntrypoint")
                else:
                    response = f"You said: {message}"
                await websocket.send_text(response)
        except fastapi.WebSocketDisconnect:
            print("Disconnected.")
```

### Key Points

* WebSocket interactions in Chains must follow `WebSocketProtocol` (it is essentially the same as `fastapi.Websocket`, but you cannot accept the connection, because inside the Chainlet, the connection will be already accepted).
* No other arguments are allowed in `run_remote()` when using WebSockets.
* The return type must be `None` (if you return data to the client, send it through the WebSocket itself).
* WebSockets can only be used only in the *entrypoint*, not in dependencies.
* Unlike for truss models it is not needed to explicitly set `runtime.transport.kind` .

### Invocation

Using `websocat` ([get it](https://github.com/vi/websocat)), you can call the chain like this:

```bash theme={"system"}
websocat -H="Authorization: Api-Key $BASETEN_API_KEY" \
   wss://chain-{CHAIN_ID}.api.baseten.co/environments/production/websocket
```

<Note>
  Similarly to models, WebSocket chains can also be invoked either via deployment or environment.

  See [Reference](/reference/inference-api/predict-endpoints/environments-websocket) for the full details.
</Note>

## WebSocket Usage with Custom Servers

You can deploy WebSocket servers using **custom Docker images** with the `docker_server` configuration. This approach is useful when you have an existing WebSocket server packaged in a Docker container or need specific runtime environments.

### Configuration

To deploy a WebSocket server using a custom Docker image, configure your `config.yaml` as follows:

```yaml config.yaml theme={"system"}
base_image:
  image: bryanzhang2/custom_ws:v0.0.4
docker_server:
  start_command: /app/server
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /v1/websocket
  server_port: 8081
model_name: custom_ws
runtime:
  transport:
    kind: "websocket"
```

### Key Configurations for WebSocket Custom Servers

* `predict_endpoint` (**required**) – The WebSocket endpoint path (e.g., `/v1/websocket`, `/ws`)
* `runtime.transport.kind` (**required**) – Must be set to `"websocket"`
* `start_command` (**required**) – Command to start your WebSocket server
* `readiness_endpoint` (**required**) – Health check endpoint for Kubernetes readiness probes
* `liveness_endpoint` (**required**) – Health check endpoint for Kubernetes liveness probes

### Invocation

Using `websocat`, you can connect to your custom WebSocket server:

```bash theme={"system"}
websocat -H="Authorization: Api-Key $BASETEN_API_KEY" \
   wss://model-{MODEL_ID}.api.baseten.co/environments/production/websocket
```

The WebSocket connection will be routed to your custom server's `predict_endpoint` path.

<Info>
  For more details on custom server deployment, see [Custom servers documentation](/development/model/custom-server).
</Info>

# Deployment and Concurrency Considerations

### Scheduling

The WebSocket scaling algorithm will schedule new WebSocket connections to the least-utilized replica until all replicas are at `maxConcurrency - 1` concurrent WebSocket  connections, at which point the total number of replicas will be incremented, until the `maxReplica` setting is hit.

Scale-down occurs when the number of replicas is greater than `minReplica` , and there are replicas with 0 concurrent connections. At this point, we begin scaling down idle replicas one-by-one.

Some other scheduling factors to consider when using WebSockets:

* Resource utilization: Standard HTTP requests are stateless and allow Baseten to optimize replica utilization and autoscaling. With WebSockets, long-lived connections are tied to specific replicas and count against your concurrency targets—even if underutilized. It's your responsibility to manage connection efficiency.
* Stateful complexity: WebSocket handlers often assume server-side state. This adds complexity around connection lifecycle management (e.g., handling unexpected disconnects, cleanup, reconnection logic).

### Lifetime guarantees

WebSockets are guaranteed to last a minimum of *1 hour*. In reality, a single WebSocket connection should be able to continue for much longer, but this is the guarantee that we provide in order to ensure that we can make changes to our system at a reasonable rate (including restarting and moving internal services as needed).

### Concurrency changes

When scaling concurrency down, existing WebSockets will be allowed to continue until they complete, even if it means that a replica indefinitely has a greater number of ongoing connections than the max concurrency setting.

For instance, suppose:

* You have a concurrency setting of 10, and currently have 10 websocket connections active on a replica.
* Then, you change the concurrency setting to 5.

In this case, Baseten will not force any of the ongoing connections to close as a result of the concurrency change. They will be allowed to continue and close naturally (unless the 1 hour minimum has passed, and an internal restart is required).

### Promotion

Just like with HTTP, you can promote a WebSocket model or chain to an environment via the REST API or UI.

When promoting a WebSocket model or chain, new connections will be routed to the new deployment, but existing
connections will remain connected to the current deployment until a termination happens.
Depending on the length of the connection, this could result in old deployments taking longer to scale down
than for HTTP deployments.

### Maximum message size

As a hard limit, we enforce a 100MiB maximum message size for any individual message sent over a websocket. This means that both clients and models are limited to 100MiB for *each* outgoing message, though *there is no overall limit on the cumulative data that can be sent over a websocket*.

# Monitoring

Just like with HTTP deployment, with WebSockets, we offer metrics on the performance
of the deployment.

## Inference volume

Inference volume is tracked as the number of connections per minute. These
metrics are published *after* the connection is closed, so these include the
status that the connection was closed with.

See [WebsSocket connection close codes](https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent/code) for a full list.

## End-to-end connection duration

Measured at different percentiles (p50, p90, p95, p99):

End-to-end connection duration is tracked as the duration of the connection. Just
like connections/minute, this is tracked after connections are closed.

## Connection input and output size

Measured at different percentiles (p50, p90, p95, p99):

* **Connection input size:** Bytes sent by the client to the server for the duration of the connection.
* **Connection output size:** Bytes sent by the client to the server for the duration of the connection.


# BEI-Bert
Source: https://docs.baseten.co/engines/bei/bei-bert

BERT-optimized embeddings with cold-start performance

BEI-Bert is a specialized variant of Baseten Embeddings Inference optimized for BERT-based model architectures. It provides superior cold-start performance and 16-bit precision for models that benefit from bidirectional attention patterns.

## When to use BEI-Bert

### Ideal use cases

**Model architectures:**

* **Sentence-transformers**: `sentence-transformers/all-MiniLM-L6-v2`
* **Jina models**: `jinaai/jina-embeddings-v2-base-en`, `jinaai/jina-embeddings-v2-base-code`
* **Nomic models**: `nomic-ai/nomic-embed-text-v1.5`, `nomic-ai/nomic-embed-code-v1.5`
* **BERT variants**: `FacebookAI/roberta-base`, `cardiffnlp/twitter-roberta-base`
* **Gemma3Bidirectional**: `google/embeddinggemma-300m`
* **ModernBERT**: `answerdotai/ModernBERT-base`
* **Qwen2Bidirectional**: `Alibaba-NLP/gte-Qwen2-7B-instruct`
* **QWen3Bidirectional** `voyageai/voyage-4-nano`
* **LLama3Bidrectional** `nvidia/llama-embed-nemotron-8b`

**Deployment scenarios:**

* **Cold-start sensitive applications**: Where first-request latency is critical
* **Small to medium models**: (under 4B parameters) where quantization isn't needed
* **High-accuracy requirements**: Where 16-bit precision is preferred
* **Bidirectional attention**: Models with bidirectional attention run best on this engine.

### BEI-Bert vs BEI comparison

| Feature      | BEI-Bert                             | BEI                               |
| ------------ | ------------------------------------ | --------------------------------- |
| Architecture | BERT-based (bidirectional)           | Causal (unidirectional)           |
| Precision    | FP16 (16-bit)                        | BF16/FP16/FP8/FP4 (quantized)     |
| Cold-start   | Optimized for fast initialization    | Standard startup                  |
| Quantization | Not supported                        | FP8/FP4 supported                 |
| Memory usage | Lower for small models               | Higher or equal                   |
| Throughput   | 600-900 embeddings/sec               | 800-1400 embeddings/sec           |
| Best for     | Small BERT models, accuracy-critical | Large models, throughput-critical |

## Recommended models (MTEB ranking)

### Top-tier embeddings

**High performance (rank 2-8):**

* `Alibaba-NLP/gte-Qwen2-7B-instruct` (7.61B): Bidirectional.
* `intfloat/multilingual-e5-large-instruct` (560M): Multilingual.
* `google/embeddinggemma-300m` (308M): Google's compact model.

**Mid-range performance (rank 15-35):**

* `Alibaba-NLP/gte-Qwen2-1.5B-instruct` (1.78B): Cost-effective.
* `Salesforce/SFR-Embedding-2_R` (7.11B): Salesforce model.
* `Snowflake/snowflake-arctic-embed-l-v2.0` (568M): Snowflake large.
* `Snowflake/snowflake-arctic-embed-m-v2.0` (305M): Snowflake medium.

**Efficient models (rank 52-103):**

* `WhereIsAI/UAE-Large-V1` (335M): UAE large model.
* `nomic-ai/nomic-embed-text-v1` (137M): Nomic original.
* `nomic-ai/nomic-embed-text-v1.5` (137M): Nomic improved.
* `sentence-transformers/all-mpnet-base-v2` (109M): MPNet base.

**Specialized models:**

* `nomic-ai/nomic-embed-text-v2-moe` (475M-A305M): Mixture of experts.
* `Alibaba-NLP/gte-large-en-v1.5` (434M): Alibaba large English.
* `answerdotai/ModernBERT-large` (396M): Modern BERT large.
* `jinaai/jina-embeddings-v2-base-en` (137M): Jina English.
* `jinaai/jina-embeddings-v2-base-code` (137M): Jina code.

### Re-ranking models

**Top re-rankers:**

* `BAAI/bge-reranker-large`: XLM-RoBERTa based.
* `BAAI/bge-reranker-base`: XLM-RoBERTa base.
* `Alibaba-NLP/gte-multilingual-reranker-base`: GTE multilingual.
* `Alibaba-NLP/gte-reranker-modernbert-base`: ModernBERT reranker.

### Classification models

**Sentiment analysis:**

* `SamLowe/roberta-base-go_emotions`: RoBERTa for emotions.

## Supported model families

### Popular Hugging Face models

Find supported models on Hugging Face:

* [Embedding Models](https://huggingface.co/models?pipeline_tag=feature-extraction\&other=text-embeddings-inference\&sort=trending)
* [Classification Models](https://huggingface.co/models?pipeline_tag=text-classification\&other=text-embeddings-inference\&sort=trending)

### Sentence-transformers

The most common BERT-based embedding models, optimized for semantic similarity.

**Popular models:**

* `sentence-transformers/all-MiniLM-L6-v2` (384D, 22M params)
* `sentence-transformers/all-mpnet-base-v2` (768D, 110M params)
* `sentence-transformers/multi-qa-mpnet-base-dot-v1` (768D, 110M params)

**Configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "sentence-transformers/all-MiniLM-L6-v2"
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
```

### Voyage and Nemotron Bidrectional LLMs

Large-decoder architectures with bidirectional attention like Qwen3 (`voyageai/voyage-4-nano`) or Llama3 (`nvidia/llama-embed-nemotron-8b`) can be deployed with BEi-bert.

**Configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "voyageai/voyage-4-nano"
      # rewrite of the config files for compatability (no custom code support)
      revision: "refs/pr/5"
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
```

### Jina AI embeddings

Jina's BERT-based models optimized for various domains including code.

**Popular models:**

* `jinaai/jina-embeddings-v2-base-en` (512D, 137M params)
* `jinaai/jina-embeddings-v2-base-code` (512D, 137M params)
* `jinaai/jina-embeddings-v2-base-es` (512D, 137M params)

**Configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "jinaai/jina-embeddings-v2-base-en"
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
```

### Nomic AI embeddings

Nomic's models with specialized training for text and code.

**Popular models:**

* `nomic-ai/nomic-embed-text-v1.5` (768D, 137M params)
* `nomic-ai/nomic-embed-code-v1.5` (768D, 137M params)

**Configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "nomic-ai/nomic-embed-text-v1.5"
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
```

### Alibaba GTE and Qwen models

Advanced multilingual models with instruction-tuning and long-context support.

**Popular models:**

* `Alibaba-NLP/gte-Qwen2-7B-instruct`: Top-ranked multilingual.
* `Alibaba-NLP/gte-Qwen2-1.5B-instruct`: Cost-effective alternative.
* `intfloat/multilingual-e5-large-instruct`: E5 multilingual variant.

**Configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "Alibaba-NLP/gte-Qwen2-7B-instruct"
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
```

## Configuration examples

### Cost-effective GTE-Qwen deployment

```yaml theme={"system"}
model_name: BEI-Bert-GTE-Qwen-1.5B
resources:
  accelerator: L4
  cpu: '1'
  memory: 15Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "Alibaba-NLP/gte-Qwen2-1.5B-instruct"
      revision: main
    max_num_tokens: 8192
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.85
    batch_scheduler_policy: guaranteed_no_evict
```

### Basic sentence-transformer deployment

```yaml theme={"system"}
model_name: BEI-Bert-MiniLM
resources:
  accelerator: L4
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "sentence-transformers/all-MiniLM-L6-v2"
      revision: main
    max_num_tokens: 8192
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

### Jina code embeddings deployment

```yaml theme={"system"}
model_name: BEI-Bert-Jina-Code
resources:
  accelerator: H100
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "jinaai/jina-embeddings-v2-base-code"
      revision: main
    max_num_tokens: 8192
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

### Nomic text embeddings with custom routing

```yaml theme={"system"}
model_name: BEI-Bert-Nomic-Text
resources:
  accelerator: L4
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "nomic-ai/nomic-embed-text-v1.5"
      revision: main
    max_num_tokens: 16384
    quantization_type: no_quant
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.85
    batch_scheduler_policy: guaranteed_no_evict
```

## Integration examples

### OpenAI client with Qwen3 instructions

```python theme={"system"}
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

response = client.embeddings.create(
    input="This is a test sentence for embedding.",
    model="not-required"
)

# Batch embedding with multiple documents
documents = [
    "Product documentation for software library",
    "User question about API usage",
    "Code snippet example"
]

response = client.embeddings.create(
    input=documents,
    model="not-required"
)

print(f"Embedding dimension: {len(response.data[0].embedding)}")
print(f"Processed {len(response.data)} embeddings")
```

### Baseten Performance Client

For maximum throughput with BEI-Bert:

```python theme={"system"}
from baseten_performance_client import PerformanceClient

client = PerformanceClient(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync"
)

# High-throughput batch processing
texts = [f"Sentence {i}" for i in range(1000)]
response = client.embed(
    input=texts,
    model="not-required",
    batch_size=8,
    max_concurrent_requests=16,
    timeout_s=300
)

print(f"Processed {len(response.numpy())} embeddings")
print(f"Embedding shape: {response.numpy().shape}")
```

### Direct API usage

```python theme={"system"}
import requests
import os
import json

headers = {
    "Authorization": f"Api-Key {os.environ['BASETEN_API_KEY']}",
    "Content-Type": "application/json"
}

data = {
    "input": ["Text to embed", "Another text"],
    "encoding_format": "float"
}

response = requests.post(
    "https://model-xxxxxx.api.baseten.co/environments/production/sync/v1/embeddings",
    headers=headers,
    json=data
)

result = response.json()
print(f"Embeddings: {len(result['data'])} embeddings generated")
```

## Best practices

### Model selection guide

Choose based on your primary constraint:

**Cost-effective (balanced performance/cost):**

* `Alibaba-NLP/gte-Qwen2-7B-instruct`: Instruction-tuned, ranked #1 for multilingual.
* `Alibaba-NLP/gte-Qwen2-1.5B-instruct`: 1/5 the size, still top-tier.
* `Snowflake/snowflake-arctic-embed-m-v2.0`: Multilingual-optimized, MRL support.

**Lightweight & fast (under 500M):**

* `google/embeddinggemma-300m`: 300M params, 100+ languages.
* `Snowflake/snowflake-arctic-embed-m-v2.0`: 305M, compression-friendly.
* `nomic-ai/nomic-embed-text-v1.5`: 137M, minimal latency.
* `sentence-transformers/all-MiniLM-L6-v2`: 22M, legacy standard.

**Specialized:**

* **Code:** `jinaai/jina-embeddings-v2-base-code`
* **Long sequences:** `Alibaba-NLP/gte-large-en-v1.5`
* **Re-ranking:** `BAAI/bge-reranker-large`, `Alibaba-NLP/gte-reranker-modernbert-base`

### Hardware optimization

**Cost-effective deployments:**

* L4 GPUs for models `<200M` parameters
* H100 GPUs for models 200-500M parameters
* Enable autoscaling for variable traffic

**Performance optimization:**

* Use `max_num_tokens: 8192` for most use cases
* Use `max_num_tokens: 16384` for long documents
* Tune `batch_scheduler_policy` based on traffic patterns

### Deployment strategies

**For development:**

* Start with smaller models (MiniLM)
* Use L4 GPUs for cost efficiency
* Enable detailed logging

**For production:**

* Use larger models (MPNet) for better quality
* Use H100 GPUs for better performance
* Implement monitoring and alerting

**For edge deployments:**

* Use smallest suitable models
* Optimize for cold-start performance
* Consider model size constraints

## Troubleshooting

### Common issues

**Slow cold-start times:**

* Ensure model is properly cached
* Consider using smaller models
* Check GPU memory availability

**Lower than expected throughput:**

* Verify `max_num_tokens` is appropriate
* Check `batch_scheduler_policy` settings
* Monitor GPU utilization

**Memory issues:**

* Reduce `max_num_tokens` if needed
* Use smaller models for available memory
* Monitor memory usage during deployment

### Performance tuning

**For lower latency:**

* Reduce `max_num_tokens`
* Use `batch_scheduler_policy: guaranteed_no_evict`
* Consider smaller models

**For higher throughput:**

* Increase `max_num_tokens` appropriately
* Use `batch_scheduler_policy: max_utilization`
* Optimize batch sizes in client code

**For cost optimization:**

* Use L4 GPUs when possible
* Choose appropriately sized models
* Implement efficient autoscaling

## Migration from other systems

### From sentence-transformers library

**Python code:**

```python theme={"system"}
# Before (sentence-transformers)
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

# After (BEI-Bert)
from openai import OpenAI
client = OpenAI(api_key=BASETEN_API_KEY, base_url=BASE_URL)
embeddings = client.embeddings.create(input=sentences, model="not-required")
```

### From other embedding services

BEI-Bert provides OpenAI-compatible endpoints:

1. **Update base URL**: Point to Baseten deployment
2. **Update API key**: Use Baseten API key
3. **Test compatibility**: Verify embedding dimensions and quality
4. **Optimize**: Tune batch sizes and concurrency for performance

## Further reading

* [BEI overview](/engines/bei/overview) - General BEI documentation
* [BEI reference config](/engines/bei/bei-reference) - Complete configuration options
* [Embedding examples](/examples/bei) - Concrete deployment examples
* [Performance client documentation](/engines/performance-concepts/performance-client) - Client Usage with Embeddings
* [Performance optimization](/development/model/performance-optimization) - General performance guidance


# Configuration reference
Source: https://docs.baseten.co/engines/bei/bei-reference

Complete reference config for BEI and BEI-Bert engines

This reference covers all configuration options for BEI and BEI-Bert deployments. All settings use the `trt_llm` section in `config.yaml`.

## Configuration structure

```yaml theme={"system"}
trt_llm:
  inference_stack: v1  # Always v1 for BEI
  build:
    base_model: encoder | encoder_bert
    checkpoint_repository: {...}
    max_num_tokens: 16384
    quantization_type: no_quant | fp8 | fp4 | fp4_kv
    quantization_config: {...}
    plugin_configuration: {...}
  runtime:
    webserver_default_route: /v1/embeddings | /rerank | /predict
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
```

## Build configuration

The `build` section configures model compilation and optimization settings.

<ParamField type="string">
  The base model architecture determines which BEI variant to use.

  **Options:**

  * `encoder`: BEI - for causal embedding models (Llama, Mistral, Qwen, Gemma)
  * `encoder_bert`: BEI-Bert - for BERT-based models (BERT, RoBERTa, Jina, Nomic)

  ```yaml theme={"system"}
  build:
    base_model: encoder
  ```
</ParamField>

<ParamField type="object">
  Specifies where to find the model checkpoint. Repository must follow the standard HuggingFace structure.

  **Source options:**

  * `HF`: Hugging Face Hub (default)
  * `GCS`: Google Cloud Storage
  * `S3`: AWS S3
  * `AZURE`: Azure Blob Storage
  * `REMOTE_URL`: HTTP URL to tar.gz file
  * `BASETEN_TRAINING`: Baseten Training checkpoints

  For detailed configuration options including training checkpoints and cloud storage setup, see [Deploy training and S3 checkpoints](/engines/performance-concepts/deployment-from-training-and-s3).

  ```yaml theme={"system"}
  checkpoint_repository:
    source: HF
    repo: "BAAI/bge-large-en-v1.5"
    revision: main
    runtime_secret_name: hf_access_token  # Optional, for private repos
  ```
</ParamField>

<ParamField type="number">
  Maximum number of tokens that can be processed in a single batch. BEI and BEI-Bert run without chunked-prefill for performance reasons. This limits the effective context length to the `max_position_embeddings` value.

  **Range:** 64 to 131072, must be multiple of 64. Use higher values (up to 131072) for long context models. Most models use 16384 as default.

  ```yaml theme={"system"}
  build:
    max_num_tokens: 16384
  ```
</ParamField>

<ParamField type="number">
  Not supported for BEI engines. Leave this value unset. BEI automatically sets it and truncates if context length is exceeded.
</ParamField>

<ParamField type="string">
  Specifies the quantization format for model weights. `FP8` quantization maintains accuracy within 1% of `FP16` for embedding models.

  **Options for BEI:**

  * `no_quant`: `FP16`/`BF16` precision
  * `fp8`: `FP8` weights + 16-bit KV cache
  * `fp4`: `FP4` weights + 16-bit KV cache (B200 only)
  * `fp4_mlp_only`: `FP4` MLP weights only (B200 only)

  **Options for BEI-Bert:**

  * `no_quant`: `FP16` precision (only option)

  For detailed quantization guidance, see [Quantization guide](/engines/performance-concepts/quantization-guide).

  ```yaml theme={"system"}
  build:
    quantization_type: fp8
  ```
</ParamField>

<ParamField type="object">
  Configuration for post-training quantization calibration.

  **Fields:**

  * `calib_size`: Size of calibration dataset (64-16384, multiple of 64)
  * `calib_dataset`: HuggingFace dataset for calibration
  * `calib_max_seq_length`: Maximum sequence length for calibration

  ```yaml theme={"system"}
  quantization_config:
    calib_size: 512
    calib_dataset: "cnn_dailymail"
    calib_max_seq_length: 1024
  ```
</ParamField>

<ParamField type="object">
  BEI automatically configures optimal TensorRT-LLM plugin settings. Manual configuration is not required or supported.

  **Automatic optimizations:**

  * XQA kernels for maximum throughput
  * Dynamic batching for optimal utilization
  * Memory-efficient attention mechanisms
  * Hardware-specific optimizations

  **Note:** Plugin configuration is only available for Engine-Builder-LLM engine.
</ParamField>

## Runtime configuration

The `runtime` section configures serving behavior.

<ParamField type="string">
  The default API endpoint for the deployment.

  **Options:**

  * `/v1/embeddings`: OpenAI-compatible embeddings endpoint
  * `/rerank`: Reranking endpoint
  * `/predict`: Classification/prediction endpoint

  BEI automatically detects embedding models and sets `/v1/embeddings`. Classification models default to `/predict`.

  ```yaml theme={"system"}
  runtime:
    webserver_default_route: /v1/embeddings
  ```
</ParamField>

<ParamField type="number">
  Not applicable to BEI engines. Only used for generative models.
</ParamField>

<ParamField type="boolean">
  Not applicable to BEI engines. Only used for generative models.
</ParamField>

<ParamField type="string">
  Not applicable to BEI engines. Only used for generative models.
</ParamField>

## HuggingFace Model Repository Structure

All model sources (S3, GCS, HuggingFace, or tar.gz) must follow the standard HuggingFace repository structure. Files must be in the root directory, similar to running:

```bash theme={"system"}
git clone https://huggingface.co/michaelfeil/bge-small-en-v1.5
```

### Model configuration

**config.json**

* `max_position_embeddings`: Limits maximum context size (content beyond this is truncated)
* `id2label`: Required dictionary mapping IDs to labels for classification models.
  * **Note**: Needs to have len of the shape of the last dense layer. Each dense output needs a `name` for the json response.
* `architecture`: Must be `ModelForSequenceClassification` or similar (cannot be `ForCausalLM`)
  * **Note**: Remote code execution is not supported; architecture is inferred automatically
* `torch_dtype`: Default inference dtype (BEI-Bert: always `fp16`, BEI: `float16`, `bfloat16`)
  * **Note**: We don't support `pre-quantized` loading, meaning your weights need to be `float16`, `bfloat16` or `float32` for all engines.
* `quant_config`: Not allowed, as no `pre-quantized` weights.

#### Model weights

**model.safetensors** (preferred)

* Or: `model.safetensors.index.json` + `model-xx-of-yy.safetensors` (sharded)
* **Note**: Convert to safetensors if you encounter issues with other formats

#### Tokenizer files

**tokenizer\_config.json** and **tokenizer.json**

* Must be "FAST" tokenizers compatible with Rust
* Typically cannot contain custom Python code, will be unread.

#### Embedding model files (sentence-transformers)

**1\_Pooling/config.json**

* Required for embedding models to define pooling strategy

**modules.json**

* Required for embedding models
* Shows available pooling layers and configurations

### Pooling layer support

| **Engine**   | **Classification Layers**  | **Pooling Types**                             | **Notes**                |
| ------------ | -------------------------- | --------------------------------------------- | ------------------------ |
| **BEI**      | 1 layer maximum            | Last token, first token                       | Limited pooling options  |
| **BEI-Bert** | Multiple layers or 1 layer | Last token, first token, mean, SPLADE pooling | Advanced pooling support |

## Complete configuration examples

### BEI with `FP8` quantization (embedding model)

```yaml theme={"system"}
model_name: BEI-BGE-Large-FP8
resources:
  accelerator: H100
  use_gpu: true
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-Embedding-8B"
      revision: main
    max_num_tokens: 16384
    quantization_type: fp8
    quantization_config:
      calib_size: 1536
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: false
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

### BEI-Bert for small BERT model

```yaml theme={"system"}
model_name: BEI-Bert-MiniLM-L6
resources:
  accelerator: L4
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "sentence-transformers/all-MiniLM-L6-v2"
      revision: main
    max_num_tokens: 8192
    quantization_type: no_quant
    plugin_configuration:  # Limited options for encoder models
      paged_kv_cache: false  # Disabled for encoder_bert
      use_paged_context_fmha: false
      use_fp8_context_fmha: false
  runtime:
    webserver_default_route: /v1/embeddings
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

### BEI for reranking model

```yaml theme={"system"}
model_name: BEI-BGE-Reranker
resources:
  accelerator: H100
  use_gpu: true
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      source: HF
      repo: "BAAI/bge-reranker-large"
      revision: main
    max_num_tokens: 16384
    quantization_type: fp8
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    webserver_default_route: /rerank
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

### BEI-Bert for classification model

```yaml theme={"system"}
model_name: BEI-Bert-Language-Detection
resources:
  accelerator: L4
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: HF
      repo: "papluca/xlm-roberta-base-language-detection"
      revision: main
    max_num_tokens: 8192
    quantization_type: no_quant
  runtime:
    webserver_default_route: /predict
    kv_cache_free_gpu_mem_fraction: 0.9
    batch_scheduler_policy: guaranteed_no_evict
```

## Validation and troubleshooting

### Common configuration errors

**Error:** `encoder does not have a kv-cache, therefore a kv specfic datatype is not valid`

* **Cause:** Using KV quantization (fp8\_kv, fp4\_kv) with encoder models
* **Fix:** Use `fp8` or `no_quant` instead

**Error:** `FP8 quantization is only supported on L4, H100, H200, B200`

* **Cause:** Using `FP8` quantization on unsupported GPU.
* **Fix:** Use H100 or newer GPU, or use `no_quant`.

**Error:** `FP4 quantization is only supported on B200`

* **Cause:** Using `FP4` quantization on unsupported GPU.
* **Fix:** Use B200 GPU or `FP8` quantization.

### Performance tuning

**For maximum throughput:**

* Use `max_num_tokens: 16384` for BEI.
* Enable `FP8` quantization on supported hardware.
* Use `batch_scheduler_policy: max_utilization` for high load.

**For lowest latency:**

* Use smaller `max_num_tokens` for your use case
* Use `batch_scheduler_policy: guaranteed_no_evict`
* Consider BEI-Bert for small models with cold-start optimization

**For cost optimization:**

* Use L4 GPUs with `FP8` quantization.
* Use BEI-Bert for small models.
* Tune `max_num_tokens` to your actual requirements.

## Migration from older configurations

If you're migrating from older BEI configurations:

1. **Update base\_model**: Change from specific model types to `encoder` or `encoder_bert`
2. **Add checkpoint\_repository**: Use the new structured repository configuration
3. **Review quantization**: Ensure quantization type matches hardware capabilities
4. **Update engine**: Add engine configuration for better performance

**Old configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    model_type: "bge"
    checkpoint_repo: "BAAI/bge-large-en-v1.5"
```

**New configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      source: HF
      repo: "BAAI/bge-large-en-v1.5"
    max_num_tokens: 16384
    quantization_type: fp8
  runtime:
    webserver_default_route: /v1/embeddings
```


# Overview
Source: https://docs.baseten.co/engines/bei/overview

Production-grade embeddings, reranking, and classification models

Baseten Embeddings Inference (BEI) is Baseten's solution for production-grade inference on embedding, classification, and reranking models using TensorRT-LLM. BEI delivers the lowest latency and highest throughput inference across any embedding solution.

## BEI vs BEI-Bert

BEI comes in two variants, each optimized for different model architectures:

<CardGroup>
  <Card title="BEI" href="#bei-features" icon="brain-circuit">
    Causal embedding models with quantization support and maximum throughput.
  </Card>

  <Card title="BEI-Bert" href="#bei-bert-features" icon="microchip">
    BERT-based models with cold-start optimization, 16-bit precision and bidirectional attention.
  </Card>
</CardGroup>

### BEI features

**Use BEI when:**

* Model uses causal architecture (Llama, Mistral, Qwen for embeddings)
* You need quantization support (FP8, FP4)
* Maximum throughput is required
* Models like BAAI/bge, Qwen3-Embedding, Salesforce/SFR-Embedding

**Benefits:**

* **Quantization Support**: FP8 and FP4 quantization for 2-4x speedup
* **Highest Throughput**: Up to 1400 client embeddings per second
* **XQA Kernels**: Optimized attention kernels for maximum performance
* **Dynamic Batching**: Automatic batch optimization for varying loads

**Supported Architectures:**

* `LlamaModel` (e.g., BAAI/bge-multilingual-gemma2)
* `MistralModel` (e.g., Salesforce/SFR-Embedding-Mistral)
* `Qwen2Model` (e.g., Qwen/Qwen3-Embedding-8B)
* `Gemma2Model` (e.g., Google/EmbeddingGemma)

### BEI-Bert features

**Use BEI-Bert when:**

* Model uses BERT-based architecture (sentence-transformers, jinaai, nomic-ai) or generic bidirectional attention models
* You need cold-start optimization for small models (`<4B` parameters)
* 16-bit precision is sufficient for your use case
* Model architectures like Jina-BERT, Nomic, or ModernBERT

**Benefits:**

* **Cold-Start Optimization**: Optimized for fast initialization and small models
* **16-bit Precision**: Models run in FP16 precision
* **BERT Architecture Support**: Specialized optimization for bidirectional models
* **Low Memory Footprint**: Efficient for smaller models and edge deployments

**Supported Architectures:**

* `BertModel` (e.g., sentence-transformers/all-MiniLM-L6-v2)
* `RobertaModel` (e.g., FacebookAI/roberta-base)
* `Jina-BERT` (e.g., jinaai/jina-embeddings-v2-base-en)
* `Nomic-BERT` (e.g., nomic-ai/nomic-embed-text-v1.5)
* `Alibaba-GTE` (e.g., Alibaba-NLP/gte-large-en-v1.5)
* `Llama Bidirectional` (e.g., nvidia/llama-embed-nemotron-8b)

## Model types and use cases

### Embedding models

Embedding models convert text into numerical representations for semantic search, clustering, and retrieval-augmented generation (RAG).

**Examples:**

* **BAAI/bge-large-en-v1.5**: General-purpose English embeddings
* **michaelfeil/Qwen3-Embedding-8B-auto**: Multilingual embeddings with quantization support
* **Salesforce/SFR-Embedding-Mistral**: Instruction-tuned embeddings

**Configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      source: HF
      repo: "BAAI/bge-large-en-v1.5"
    quantization_type: no_quant  # Supported for causal models
```

### Reranking models

Reranking models are actually classification models that score document relevance for search and retrieval tasks. They work by classifying query-document pairs as relevant or not relevant.

**How rerankers work:**

* Rerankers are sequence classification models (ending with `ForSequenceClassification`)
* They take a query and document as input and output a relevance score
* The "reranking" is accomplished by scoring multiple documents and ranking them by the classification score
* You can implement reranking by using the classification endpoint with proper prompt templates

**Recommended:**

* **BAAI/bge-reranker-v2-m3**: Great reranking model (279M params). Performs well in RAG systems where a first pass of vector retrieval surfaces dozens of snippets of data.
* **michaelfeil/Qwen3-Reranker-8B-seq**: Best multilingual and general-purpose reranker. **Note:** Needs to be used with the `webserver_default_route: /predict` setting.

**Configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      source: HF
      repo: "BAAI/bge-reranker-v2-m3"
    max_num_tokens: 16384
  runtime:
    webserver_default_route: /rerank
```

**Implementation:**
Use the `/predict` endpoint with proper prompt formatting for query-document pairs. The baseten-performance-client handles reranking template formatting automatically.

### Classification models

Classification models categorize text into predefined classes for tasks like sentiment analysis, content moderation, and language detection.

**Examples:**

* **papluca/xlm-roberta-base-language-detection**: Language identification
* **samlowe/roberta-base-go\_emotions**: Emotion classification
* **Reward Models**: RLHF reward model examples

**Configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      source: HF
      repo: "papluca/xlm-roberta-base-language-detection"
    quantization_type: no_quant  # BEI-Bert required for classification models
  runtime:
    webserver_default_route: /predict
```

## Performance and optimization

### Throughput benchmarks

For detailed performance benchmarks, see: [Run Qwen3 Embedding on NVIDIA Blackwell GPUs](https://www.baseten.co/blog/run-qwen3-embedding-on-nvidia-blackwell-gpus/#bei-provides-the-fastest-embeddings-inference-on-b200s)

| Framework | Precision | GPU  | Max Token/s Throughput | Max Request/s Throughput |
| --------- | --------- | ---- | ---------------------- | ------------------------ |
| TEI       | FP16      | H100 | 34,055                 | 824.25                   |
| BEI-Bert  | FP16      | H100 | 36,520                 | 841.05                   |
| vLLM      | BF16      | H100 | 36,625                 | 155.23                   |
| BEI       | BF16      | H100 | 47,549                 | 761.44                   |
| BEI       | FP8       | H100 | 77,107                 | 855.96                   |
| BEI       | FP8       | B200 | 121,443                | 1,310.52                 |

* **Token Throughput/s**: Measured on 500 tokens per request
* **Request Throughput/s**: Measured on 5 tokens per request

### Quantization impact

| **Quantization** | **Speed Improvement** | **Memory Reduction** | **Accuracy Impact** |
| ---------------- | --------------------- | -------------------- | ------------------- |
| FP16/BF16 vLLM   | Baseline              | None                 | None                |
| FP16/BF16 BEI    | 1.3x                  | None                 | None                |
| FP8 BEI          | 2x faster             | 50%                  | \~1%                |
| FP4 BEI          | 3.5x faster           | 75%                  | 1-2%                |

### Hardware requirements

| **GPU Type** | **BEI Support** | **BEI-Bert Support** | **Recommended For**        |
| ------------ | --------------- | -------------------- | -------------------------- |
| L4           | Full            | Full                 | Cost-effective deployments |
| A10G, A100   | Full            | Full                 | Legacy support             |
| T4           | No              | Full                 | Legacy support             |
| H100         | Full            | Full                 | Maximum performance        |
| B200         | Full            | Full                 | FP4 quantization           |

## OpenAI compatibility

BEI deployments are fully OpenAI compatible for embeddings:

```python theme={"system"}
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

embedding = client.embeddings.create(
    input=["Baseten Embeddings are fast.", "Embed this sentence!"],
    model="not-required"
)
```

### Baseten Performance Client

For maximum throughput, use the [Baseten Performance Client](/engines/performance-concepts/performance-client).

```python theme={"system"}
from baseten_performance_client import PerformanceClient

client = PerformanceClient(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync"
)

texts = ["Hello world", "Example text", "Another sample"]
response = client.embed(
    input=texts,
    model="my_model",
    batch_size=4,
    max_concurrent_requests=32,
    timeout_s=360
)
```

## Reference config

For complete configuration options, see the [BEI reference config](/engines/bei/bei-reference).

### Key configuration options

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder  # or encoder_bert for BEI-Bert
    checkpoint_repository:
      source: HF  # or GCS, S3, AZURE, REMOTE_URL
      repo: "model-repo-name"
      revision: main
      runtime_secret_name: hf_access_token
    max_num_tokens: 16384  # BEI automatically upgrades to 16384
    quantization_type: fp8  # or no_quant for BEI-Bert
  runtime:
    webserver_default_route: /v1/embeddings  # or /rerank, /predict
```

## Production best practices

### GPU selection guidelines

* **L4**: Best for models `<4B` parameters, cost-effective
* **H100**: Required for models 4B+ parameters or long context (>8K tokens)
* **H100\_40GB**: Use for models with memory constraints

### Build job optimization

```yaml theme={"system"}
# H100 builds (default)
trt_llm:
  build:
    num_builder_gpus: 2

# L4 builds (memory-constrained)
trt_llm:
  build:
    num_builder_gpus: 4
```

### Model-specific recommendations

**BERT-based models (BEI-Bert):**

* Use `encoder_bert` base model
* No quantization support (FP16/BF16 only)
* Best for models `<200M` parameters on L4

**ModernBERT and newer architectures:**

* Support longer contexts (up to 8192 tokens)
* Use H100 for models >1B parameters
* Consider memory requirements for long sequences

**Qwen embedding models:**

* Use regular FP8 quantization
* Support very long contexts (up to 131K tokens)
* Higher memory requirements for long sequences

### Token limit optimization

```yaml theme={"system"}
trt_llm:
  build:
    max_num_tokens: 16384  # Default, automatically set by BEI
    # Override for specific use cases:
    # max_num_tokens: 8192   # Standard embeddings
    # max_num_tokens: 131072  # Qwen long-context models
```

## Getting started

1. **Choose your variant**: BEI for causal models and quantization, BEI-Bert for BERT models
2. **Review configuration**: See [BEI reference config](/engines/bei/bei-reference)
3. **Deploy your model**: Use the configuration templates and examples
4. **Test integration**: Use OpenAI client or Performance Client for maximum throughput

## Examples and further reading

* [BEI-Bert examples](/engines/bei/bei-bert) - BERT-specific configurations
* [BEI reference config](/engines/bei/bei-reference) - Complete configuration options
* [Embedding examples](/examples/bei) - Concrete deployment examples
* [Performance client documentation](/engines/performance-concepts/performance-client) - Client Usage with Embeddings


# Gated features for BIS-LLM
Source: https://docs.baseten.co/engines/bis-llm/advanced-features

KV-aware routing, disaggregated serving, and other gated features

BIS-LLM provides features for large-scale deployments: KV cache optimization, disaggregated serving, and specialized inference strategies.

<Note>
  These advanced features are not fully self-serviceable. [Contact us](mailto:support@baseten.co) to enable them for your organization.
</Note>

## Available advanced features

### Routing and scaling

*KV-aware routing* and *disaggregated serving* optimize multi-replica deployments. KV-aware routing directs requests to replicas with the best cache hit potential, while disaggregated serving separates prefill and decode phases into independent clusters that scale separately. *Separate prefill and decode autoscaling* uses token-exact metrics to right-size each phase.

### MoE optimization

*WideEP* (expert parallelism) distributes experts across multiple GPUs for extremely large expert counts. These features work together to maximize hardware utilization on models like DeepSeek-V3 and Qwen3MoE.

### Attention and memory

*DP attention for MLA* (Multi-Head Latent Attention) compresses KV cache by projecting attention tensors into a compact latent space, *DP attention* helps to managed KV-Cache across GPU ranks, and tunes DeepSeek deployments for high throughput. *DeepSparseAttention* sparsifies the attention matrix based on token relevance. *Distributed KV storage* spreads KV cache across devices for long-context inference beyond single-device memory limits.

### Speculative decoding

*Speculative n-gram automata-based decoding* uses automata to predict tokens from n-gram patterns without full model computation. *Speculative MTP or Eagle3 decoding* uses draft-model approaches to predict and verify multiple future tokens.

### Kernel optimization

*Zero-overlap scheduling* overlaps computation and communication to hide latency. *Auto-tuned kernels* optimize kernel parameters for your specific hardware and model topology.

## KV-aware routing

KV-aware routing directs requests to replicas with the best chance of KV cache hits, routing based on cache availability and replica utilization.

KV-aware routing reduces inter-token latency by distributing load across replicas, improves time-to-first-token through cache hits on repeated queries, and increases global throughput through cache reuse.

## Disaggregated serving

Disaggregated serving separates prefill and decode phases into independent clusters, allowing each to scale and be optimized independently. This architecture is particularly valuable for large MoE models.

Disaggregated serving is available as a gated feature. [Contact us](mailto:support@baseten.co) to be paired with an engineer to discuss your needs.

Disaggregated serving enables independent scaling of prefill and decode resources, isolates time-critical TTFT metrics from throughput-focused phases, and optimizes costs by right-sizing each phase for its workload.

## Get started

### Choose the right configuration

**For advanced deployments** with large MoE models and planet-scale inference, [contact us](mailto:support@baseten.co).

**For standard deployments**:
Use the standard BIS-LLM configuration as documented in [BIS-LLM configuration](/engines/bis-llm/bis-llm-config).

## Model recommendations

### Models that benefit from advanced features

**Large MoE models:**

* DeepSeek-V3
* Qwen3MoE
* Kimi-K2
* GLM-4.7
* GPT-OSS

**Ideal use cases:**

* High-throughput API services
* Complex reasoning tasks
* Long-context applications, including agentic coding
* Planet-scale deployments

### When to use standard BIS-LLM or Engine-Builder-LLM

* Dense models under 70B parameters
* Standard MoE models under 30B parameters
* Development and testing environments
* Workloads with low KV cache hit rates

## Further reading

* [BIS-LLM overview](/engines/bis-llm/overview): Main engine documentation.
* [BIS-LLM reference config](/engines/bis-llm/bis-llm-config): Configuration options.
* [Structured outputs documentation](/engines/performance-concepts/structured-outputs): JSON schema validation.
* [Examples section](/examples/overview): Deployment examples.


# Reference Config (BIS-LLM)
Source: https://docs.baseten.co/engines/bis-llm/bis-llm-config

Complete reference config for V2 inference stack and MoE models

This reference provides complete configuration options for BIS-LLM (Baseten Inference Stack V2) engine. BIS-LLM uses the V2 inference stack with simplified configuration and enhanced features for MoE models and advanced use cases.

## Configuration structure

```yaml theme={"system"}
trt_llm:
  inference_stack: v2  # Always v2 for BIS-LLM
  build:
    checkpoint_repository: {...}
    quantization_type: no_quant | fp8 | fp4
    quantization_config: {...}
    num_builder_gpus: 1
    skip_build_result: false
  runtime:
    max_seq_len: 32768
    max_batch_size: 256
    max_num_tokens: 8192
    tensor_parallel_size: 1
    enable_chunked_prefill: true
    served_model_name: "model-name"
    patch_kwargs: {...}
```

## Build configuration

### `checkpoint_repository`

Specifies where to find the model checkpoint. Same structure as V1 but with V2-specific optimizations.

**Structure:**

```yaml theme={"system"}
checkpoint_repository:
  source: HF | GCS | S3 | AZURE | REMOTE_URL | BASETEN_TRAINING
  repo: "model-repository-name"
  revision: main  # Optional, only for HF
  runtime_secret_name: hf_access_token  # Optional, for private repos
```

For detailed configuration options including training checkpoints and cloud storage setup, see [Deploy training and S3 checkpoints](/engines/performance-concepts/deployment-from-training-and-s3).

### `quantization_type`

Quantization options for V2 inference stack (simplified from V1):

**Options:**

* `no_quant`: precision of the repo. This can be fp16 / bf16. Unique to BIS-LLM is that we also do support quantized checkpoints from nvidia-modelopt libraries.
* `fp8`: FP8 weights + 16-bit KV cache
* `fp4`: FP4 weights + 16-bit KV cache (B200 only)
* `fp4_mlp_only`: FP4 MLP layers only + 16-bit KV cache

For detailed quantization guidance including hardware requirements, calibration strategies, and model-specific recommendations, see [Quantization Guide](/engines/performance-concepts/quantization-guide).

### `quantization_config`

Configuration for post-training quantization calibration:

**Structure:**

```yaml theme={"system"}
quantization_config:
  calib_size: 1024
  calib_dataset: "cnn_dailymail"
  calib_max_seq_length: 2048
```

### `num_builder_gpus`

Number of GPUs to use during the build process.

**Default:** `1` (auto-detected from resources)\
**Range:** 1 to 8

**Example:**

```yaml theme={"system"}
build:
  num_builder_gpus: 4  # For large models or complex quantization
```

### `skip_build_result`

Skip the engine build step and use a pre-built model, that does not require any quantization.

**Default:** `false`\
**Use case:** When you have a pre-built engine from model cache

**Example:**

```yaml theme={"system"}
build:
  skip_build_result: true
```

## Engine configuration

### `max_seq_len`

Maximum sequence length (context) for single requests.

**Default:** `32768` (64K)\
**Range:** 1 to 1048576

**Example:**

```yaml theme={"system"}
runtime:
  max_seq_len: 131072  # 128K context
```

### `max_batch_size`

Maximum number of input sequences processed concurrently.

**Default:** `256`\
**Range:** 1 to 2048

**Example:**

```yaml theme={"system"}
runtime:
  max_batch_size: 128  # Lower for better latency
```

### `max_num_tokens`

Maximum number of batched input tokens after padding removal.

**Default:** `8192`\
**Range:** 64 to 131072

**Example:**

```yaml theme={"system"}
runtime:
  max_num_tokens: 16384  # Higher for better throughput
```

### `tensor_parallel_size`

Number of GPUs to use for tensor parallelism.

**Default:** `1` (auto-detected from resources)\
**Range:** 1 to 8

**Example:**

```yaml theme={"system"}
runtime:
  tensor_parallel_size: 4  # For large models
```

### `enable_chunked_prefill`

Enable chunked prefilling for long sequences.

**Default:** `true`

**Example:**

```yaml theme={"system"}
runtime:
  enable_chunked_prefill: true
```

### `served_model_name`

Model name returned in API responses.

**Default:** `None` (uses model name from config)

**Example:**

```yaml theme={"system"}
runtime:
   served_model_name: "gpt-oss-120b"
```

### `patch_kwargs`

Advanced configuration patches for V2 inference stack.

**Structure:**

```yaml theme={"system"}
patch_kwargs:
  custom_setting: "value"
  advanced_config:
    nested_setting: true
```

**Note:** This is a preview feature and may change in future versions.

## Complete configuration examples

### Qwen3-30B-A3B-Instruct-2507 MoE with FP4 on B200

```yaml theme={"system"}
model_name: Qwen3-30B-A3B-Instruct-2507-FP4
resources:
  accelerator: B200:1
  cpu: '4'
  memory: 40Gi
  use_gpu: true
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-Coder-30B-A3B-Instruct"
      revision: main
    quantization_type: fp4
    quantization_config:
      calib_size: 2048
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 4096
    num_builder_gpus: 1
  runtime:
    max_seq_len: 65536
    max_batch_size: 256
    max_num_tokens: 8192
    tensor_parallel_size: 1
    enable_chunked_prefill: true
    served_model_name: "Qwen3-30B-A3B-Instruct-2507"
```

### GPT-OSS 120B on B200:1 with no\_quant

**Note**: We have GPT-OSS much more optimized. The below example is functional, but you can sequeeze much more performance using `B200`, e.g. with Baseten's custom Eagle Heads.

```yaml theme={"system"}
model_name: gpt-oss-120b-b200
resources:
  accelerator: B200:1
  cpu: '4'
  memory: 40Gi
  use_gpu: true
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "openai/gpt-oss-120b"
      revision: main
      runtime_secret_name: hf_access_token
    quantization_type: no_quant
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 16384
    tensor_parallel_size: 1
    enable_chunked_prefill: true
    served_model_name: "gpt-oss-120b"
```

### DeepSeek V3

**Note**: We have DeepSeek V3 / V3.1 / V3.2 much more optimized. The below example is functional, but you can sequeeze much more performance using `B200:4`, e.g. with MTP Heads and disaggregated serving, or data-parallel attention.

```yaml theme={"system"}
model_name: nvidia/DeepSeek-V3.1-NVFP4
resources:
  accelerator: B200:4
  cpu: '8'
  memory: 80Gi
  use_gpu: true
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "nvidia/DeepSeek-V3.1-NVFP4"
      revision: main
      runtime_secret_name: hf_access_token
    quantization_type: no_quant # nvidia/DeepSeek-V3.1-NVFP4 is already modelopt compatible
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 16384
    tensor_parallel_size: 8
    enable_chunked_prefill: true
    served_model_name: "nvidia/DeepSeek-V3.1-NVFP4"
```

## V2 vs V1 configuration differences

### Simplified build configuration

**V1 build configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: decoder
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: fp8_kv
    tensor_parallel_count: 4
    plugin_configuration: {...}
    speculator: {...}
```

**V2 build configuration:**

```yaml theme={"system"}
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository: {...}
    quantization_type: fp8
    num_builder_gpus: 4
  runtime:
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 8192
    tensor_parallel_size: 4
```

### Key differences

1. **`inference_stack`**: Explicitly set to `v2`
2. **Simplified build options**: Many V1 options moved to engine
3. **No `base_model`**: Automatically detected from checkpoint
4. **No `plugin_configuration`**: Handled automatically
5. **No `speculator`**: Lookahead decoding requires FDE involement.
6. **Tensor parallel**: Moved to engine as `tensor_parallel_size`

## Validation and troubleshooting

### Common V2 configuration errors

**Error:** `Field trt_llm.build.base_model is not allowed to be set when using v2 inference stack`

* **Cause:** Setting `base_model` in V2 configuration
* **Fix:** Remove `base_model` field, V2 detects automatically

**Error:** `Field trt_llm.build.quantization_type is not allowed to be set when using v2 inference stack`

* **Cause:** Using unsupported quantization type
* **Fix:** Use supported quantization: `no_quant`, `fp8`, `fp4`, `fp4_mlp_only`, `fp4_kv`, `fp8_kv`

**Error:** `Field trt_llm.build.speculator is not allowed to be set when using v2 inference stack`

* **Cause:** Trying to use lookahead decoding in V2
* **Fix:** Use V1 stack for lookahead decoding, or V2 without speculation or reach out to us to use V2 with speculation.

## Migration from V1

### V1 to V2 migration

**V1 configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-4B"
    max_seq_len: 32768
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: fp8_kv
    tensor_parallel_count: 1
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
```

**V2 configuration:**

```yaml theme={"system"}
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-4B"
    quantization_type: fp8_kv
  runtime:
    max_seq_len: 32768
    max_batch_size: 256
    max_num_tokens: 8192
    tensor_parallel_size: 1
    enable_chunked_prefill: true
```

### Migration steps

1. **Add `inference_stack: v2`**
2. **Remove `base_model`** (auto-detected)
3. \*\*Move `max_seq_len`, `max_batch_size`, `max_num_tokens` to engine
4. **Change `tensor_parallel_count` to `tensor_parallel_size`**
5. **Remove `plugin_configuration`** (handled automatically)
6. **Update quantization type** (V2 has simplified options)
7. **Remove `speculator`** (not supported in V2)

## Hardware selection

**GPU recommendations for V2:**

* **B200**: Best for FP4 quantization and next-gen performance
* **H100**: Best for FP8 quantization and production workloads
* **Multi-GPU**: Required for large MoE models (>30B parameters)

**Configuration guidelines:**

| **Model Size** | **Recommended GPU** | **Quantization** | **Tensor Parallel** |
| -------------- | ------------------- | ---------------- | ------------------- |
| `<30B` MoE     | H100:2-4            | FP8              | 2-4                 |
| 30-100B MoE    | H100:4-8            | FP8              | 4-8                 |
| 100B+ MoE      | B200:4-8            | FP4              | 4-8                 |
| Dense >30B     | H100:2-4            | FP8              | 2-4                 |

## Further reading

* [BIS-LLM overview](/engines/bis-llm/overview) - Main engine documentation
* [Advanced features documentation](/engines/bis-llm/advanced-features) - Enterprise features and capabilities
* [Structured outputs for BIS-LLM](/engines/performance-concepts/structured-outputs) - Advanced JSON schema validation
* [Examples section](/examples/overview) - Concrete deployment examples


# Overview
Source: https://docs.baseten.co/engines/bis-llm/overview

Next-generation engine for MoE models with advanced optimizations

BIS-LLM (Baseten Inference Stack V2) is Baseten's next-generation engine for Mixture of Experts (MoE) models and advanced text generation use cases. Built on the V2 inference stack, it provides cutting-edge optimizations including KV-aware routing, disaggregated serving, expert parallel load balancing and DP attention.
Before you continue reading - we have enabled a small subset of features for customers - the primary way to deploy these large models is though Forward Deployed Engineers.

## Overview and use cases

BIS-LLM is designed for MoE models and scenarios requiring the most advanced inference optimizations.

### Ideal for:

**MoE model families:**

* **DeepSeek**: `deepseek-ai/DeepSeek-R1`, `deepseek-ai/DeepSeek-V3.1`, `deepseek-ai/DeepSeek-V3.2`
* **Qwen MoE**: `Qwen/Qwen3-30B-A3B`, `Qwen/Qwen3-Coder-480B-A35B-Instruct`
* **Kimi**: `moonshotai/Kimi-K2-Instruct`
* **GLM**: `zai-org/GLM-4.7`
* **LLama4**: `meta-llama/llama-4-maverick`
* **GPT-OSS**: Various open-source GPT variants

**Advanced use cases:**

* **High-performance inference**: FP4 quantization on GB200/B200 GPUs
* **Complex reasoning**: Advanced tool calling and structured outputs
* **Large-scale deployments**: Multi-node setups and distributed inference

## Forward Deployed Engineer Gated Features

We gated some more advanced features behind feature flags that we internally toggle.
They are not the easiest to use, and some are mutually exclusive - making them hard to maintain on our docs page.

The features below power some of the largest LLM deployments for the customer logos on our website and a couple of [world-records on GPUs](https://www.baseten.co/blog/how-we-made-the-fastest-gpt-oss-on-nvidia-gpus-60-percent-faster/).

For detailed information on each advanced feature, see [Gated Features for BIS-LLM](/engines/bis-llm/advanced-features).

## Architecture support

### MoE model support

BIS-LLM specifically optimizes for Mixture of Experts architectures:

**Primary MoE architectures:**

* `DeepseekV32ForCausalLM` - DeepSeek family
* `Qwen3MoEForCausalLM` - Qwen3 MoE family
* `KimiK2ForCausalLM` - Kimi K2 family
* `Glm4MoeForCausalLM` - GLM MoE variants
* `GPTOSS` - OpenAI GPT-OSS variants
* ...

### Dense model support

While optimized for MoE, BIS-LLM also supports dense models with advanced features:

**Benefits for dense models:**

* **GB200/B200 optimization**: Advanced GPU kernel optimization
* **FP4 quantization**: Next-generation quantization support
* **Enhanced memory management**: Improved KV cache handling

**When to use BIS-LLM for dense models:**

* Models >30B parameters requiring maximum performance
* Deployments on GB200/B200 GPUs with advanced quantization
* You tried out V1 and want to compare against V2
* You want to try V2 features like KV routing or Disaggregated Serving.
* Speculation on GB200/B200

### Advanced quantization

BIS-LLM supports next-generation quantization formats for maximum performance:

**Quantization options:**

* `no_quant`: FP16/BF16 precision, or automatically uses hf\_quant\_config.json from modelopt if available
* `fp8`: FP8 weights + 16-bit KV cache
* `fp4`: FP4 weights + 16-bit KV cache
* `fp8_kv`: FP8 weights + 8-bit synmetric kv cache
* `fp4_kv`: FP8 weights + 8-bit synmetric kv cache
* `fp4_mlp_only`: FP4 weights (mlp layers) + 16-bit kv-cache and attn computation

**B200 optimization:**

* **FP4 kernels**: Custom B200 kernels for maximum performance
* **Memory efficiency**: 75% memory reduction with FP4, some models like DeepSeekV3 strongly prefered on B200 due to kernel selection.
* **Speed improvement**: 4x-8x faster inference with minimal accuracy loss
* **Cascaded improvments**: More memory and faster inference leading to improved system performance, especially under high load.

**Example:**

```yaml theme={"system"}
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-30B-A3B"
    quantization_type: fp4  # B200 only
```

### Structured outputs and tool calling

Advanced JSON schema validation and function calling capabilities:

**Features:**

* **JSON schema validation**: Precise structured output generation
* **Function calling**: Advanced tool selection and execution
* **Multi-tool support**: Complex tool chains and reasoning
* **Schema inheritance**: Nested and complex schema support

**Example:**

```python theme={"system"}
from pydantic import BaseModel
from openai import OpenAI

class ResearchResult(BaseModel):
    topic: str
    findings: list[str]
    confidence: float
    sources: list[str]

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

response = client.beta.chat.completions.parse(
    model="not-required",
    messages=[
        {"role": "user", "content": "Analyze the latest AI research papers"}
    ],
    response_format=ResearchResult
)

result = response.choices[0].message.parsed
```

## Configuration examples

**Note**: The below examples are just functional examples -- advanced features are frequently changing. Please reach out how to best configure a specific or fine-tuned model, we are happy to help.

### GPT-OSS 120B deployment

```yaml theme={"system"}
model_name: gpt-oss-120b
resources:
  accelerator: H100:8  # 8 GPUs for large dense model
  cpu: '8'
  memory: 80Gi
  use_gpu: true
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "openai/gpt-oss-120b"
      revision: main
      runtime_secret_name: hf_access_token
    quantization_type: fp8
    num_builder_gpus: 8
  runtime:
    max_seq_len: 32768
    max_batch_size: 256
    max_num_tokens: 16384
    tensor_parallel_size: 8
    enable_chunked_prefill: true
    served_model_name: "gpt-oss-120b"
```

### Qwen3-30B-A3B-Instruct-2507 MoE with FP4 quantization

```yaml theme={"system"}
model_name: Qwen3-30B-A3B-Instruct-2507-FP4
resources:
  accelerator: B200:2
  cpu: '4'
  memory: 40Gi
  use_gpu: true
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-30B-A3B-Instruct-2507"
      revision: main
    quantization_type: fp4
    num_builder_gpus: 2
  runtime:
    max_seq_len: 65536
    max_batch_size: 128
    max_num_tokens: 8192
    tensor_parallel_size: 2
    enable_chunked_prefill: true
    served_model_name: "Qwen3-30B-A3B-Instruct-2507"
```

### Dense model with BIS-LLM V2

```yaml theme={"system"}
model_name: Llama-3.3-70B-V2
resources:
  accelerator: H100:4
  cpu: '4'
  memory: 40Gi
  use_gpu: true
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.3-70B-Instruct"
      revision: main
      runtime_secret_name: hf_access_token
    quantization_type: fp8
    num_builder_gpus: 4
  runtime:
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 8192
    tensor_parallel_size: 4
    enable_chunked_prefill: true
    served_model_name: "Llama-3.3-70B-Instruct"
```

## Integration examples

### OpenAI-compatible inference

```python theme={"system"}
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

# Standard chat completion 
response = client.chat.completions.create(
    model="not-required",
    messages=[
        {"role": "system", "content": "You are an advanced AI assistant."},
        {"role": "user", "content": "Explain the concept of mixture of experts in AI."}
    ],
    temperature=0.7,
    max_tokens=1000
)

print(response.choices[0].message.content)
```

### Advanced structured outputs

```python theme={"system"}
from pydantic import BaseModel
from openai import OpenAI

class ExpertAnalysis(BaseModel):
    routing_decision: str
    expert_utilization: dict[str, float]
    processing_time: float
    confidence_score: float

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

response = client.beta.chat.completions.parse(
    model="not-required",
    messages=[
        {"role": "user", "content": "Analyze the expert routing for this complex query"}
    ],
    response_format=ExpertAnalysis
)

analysis = response.choices[0].message.parsed
print(f"Routing decision: {analysis.routing_decision}")
print(f"Expert utilization: {analysis.expert_utilization}")
```

### Multi-tool function calling

```python theme={"system"}
client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "analyze_expert_routing",
            "description": "Analyze expert routing patterns",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "expert_count": {"type": "integer"}
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "optimize_performance",
            "description": "Optimize model performance",
            "parameters": {
                "type": "object",
                "properties": {
                    "target_tps": {"type": "number"},
                    "memory_budget": {"type": "integer"}
                }
            }
        }
    }
]

response = client.chat.completions.create(
    model="not-required",
    messages=[
        {"role": "user", "content": "Analyze and optimize the performance of this MoE model"}
    ],
    tools=tools
)

for tool_call in response.choices[0].message.tool_calls:
    print(f"Function: {tool_call.function.name}")
    print(f"Arguments: {tool_call.function.arguments}")
```

## Best practices

### Hardware selection

**GPU recommendations:**

* **B200**: Best for FP4 quantization and next-gen performance
* **H100**: Best for FP8 quantization and production workloads
* **Multi-GPU**: Required for large MoE models (>30B parameters)
* **Multi-Node**:

**Configuration guidelines:**

| **Model Size** | **Recommended GPU** | **Quantization** | **Tensor Parallel** |
| -------------- | ------------------- | ---------------- | ------------------- |
| `<30B` MoE     | H100:2-4            | FP8              | 2-4                 |
| 30-100B MoE    | H100:4-8            | FP8              | 4-8                 |
| 100B+ MoE      | B200:4-8            | FP4              | 4-8                 |
| Dense >30B     | H100:2-4            | FP8              | 2-4                 |

## Production best practices

### V2 inference stack optimization

#### Configuration differences from V1

```yaml theme={"system"}
# V2 (recommended for MoE and advanced models)
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "openai/gpt-oss-120b"
    quantization_type: fp8
  runtime:
    max_seq_len: 32768  # Set in engine for V2
    max_batch_size: 32
    tensor_parallel_size: 8  # Engine configuration
```

## Migration guide

### From Engine-Builder-LLM

**V1 configuration:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-32B"
    quantization_type: fp8_kv
    tensor_parallel_count: 8
```

**V2 configuration:**

```yaml theme={"system"}
trt_llm:
  inference_stack: v2
  build:
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen3-32B"
    quantization_type: fp8_kv
  runtime:
    tensor_parallel_size: 8
    enable_chunked_prefill: true
```

### Key differences

1. **`inference_stack`**: Explicitly set to `v2`
2. **Build configuration**: Simplified with fewer options
3. **Engine configuration**: Enhanced with V2-specific features
4. **Performance**: Better optimization for MoE models

## Further reading

* [BIS-LLM reference config](/engines/bis-llm/bis-llm-config) - Complete V2 configuration options
* [Advanced features documentation](/engines/bis-llm/advanced-features) - Enterprise features and capabilities
* [Structured outputs](/engines/performance-concepts/structured-outputs) - Advanced JSON schema validation
* [Examples section](/examples/overview) - Concrete deployment examples


# Custom engine builder
Source: https://docs.baseten.co/engines/engine-builder-llm/custom-engine-builder

Implement custom model.py for business logic, logging, and advanced inference patterns

Implement custom business logic, request handling, and inference patterns in `model.py` while maintaining TensorRT-LLM performance. Custom engine builder enables billing integration, request tracing, fan-out generation, and multi-response workflows.

## Overview

The custom engine builder lets you:

* **Implement business logic**: Billing, usage tracking, access control.
* **Add custom logging**: Request tracing, performance monitoring, audit trails.
* **Create advanced inference patterns**: Fan-out generation, custom chat templates.
* **Integrate external services**: APIs, databases, monitoring systems.
* **Optimize performance**: Concurrent processing, custom batching strategies.

## When to use custom engine builder

### Ideal use cases

**Business logic integration:**

* **Usage tracking**: Monitor token usage per customer/request.
* **Access control**: Implement custom authentication/authorization.
* **Rate limiting**: Custom rate limiting based on user tiers.
* **Audit logging**: Compliance and security requirements.

**Advanced inference patterns:**

* **Fan-out generation**: Generate multiple responses from one request.
* **Custom chat templates**: Domain-specific conversation formats.
* **Multi-response workflows**: Parallel processing of variations.
* **Conditional generation**: Business rule-based output modification.

**Performance and monitoring:**

* **Custom logging**: Request tracing, performance metrics.
* **Concurrent processing**: Parallel generation for improved throughput.
* **Usage analytics**: Track patterns and optimize accordingly.
* **Error handling**: Custom error responses and fallback logic.

## Implementation

### Fan-out generation example

Multi-generation fan-out generates multiple texts from a single request. Running them sequentially ensures the KV cache is created before subsequent generations.

```python model/model.py theme={"system"}
# model/model.py
import copy
import asyncio
from typing import Any, Dict, List, Optional, Tuple
from fastapi import HTTPException, Request
from starlette.responses import JSONResponse, StreamingResponse

Message = Dict[str, str]  # {"role": "...", "content": "..."}

class Model:
    def __init__(self, trt_llm, **kwargs) -> None:
        self._secrets = kwargs["secrets"]
        self._engine = trt_llm["engine"]

    async def predict(self, model_input: Dict[str, Any], request: Request) -> Any:
        # Validate request structure
        if not isinstance(model_input, dict):
            raise HTTPException(status_code=400, detail="Request body must be a JSON object.")

        # Enforce non-streaming for this example
        if bool(model_input.get("stream", False)):
            raise HTTPException(status_code=400, detail="stream=true is not supported here; set stream=false.")

        # Extract base messages and fan-out tasks
        prompt_key, base_messages = self._get_base_messages(model_input)
        n, suffix_tasks = self._parse_fanout(model_input)

        # Build reusable request (don't forward fan-out params to engine)
        base_req = copy.deepcopy(model_input)
        base_req.pop("suffix_messages", None)
        
        # Extract debug ID for logging/tracing
        debug_id = request.headers.get("X-Debug-ID", "")

        # Run sequential generations
        per_gen_payloads: List[Any] = []

        async def run_generation(i: int) -> Any:
            msgs_i = copy.deepcopy(base_messages)
            if suffix_tasks is not None:
                msgs_i.extend(suffix_tasks[i])
            base_req[prompt_key] = msgs_i
            
            # Debug logging
            if debug_id:
                print(f"Running generation {debug_id} {i} with messages: {msgs_i}")
            
            # Time the generation
            start_time = asyncio.get_event_loop().time()
            resp = await self._engine.chat_completions(request=request, model_input=base_req)
            end_time = asyncio.get_event_loop().time()
            
            # Debug logging
            if debug_id:
                duration = end_time - start_time
                print(f"Result Generation {debug_id} {i} response: {resp} (took {duration:.3f}s)")
            
            # Validate response type
            if isinstance(resp, StreamingResponse) or hasattr(resp, "body_iterator"):
                raise HTTPException(status_code=400, detail="Engine returned streaming but stream=false was requested.")

            return resp

        # Run first generation
        payload = await run_generation(0)
        per_gen_payloads.append(payload)
        
        # Run remaining generations concurrently
        if n > 1:
            results = await asyncio.gather(*(run_generation(i) for i in range(1, n)))
            per_gen_payloads.extend(results)

        # Convert to OpenAI-ish multi-choice response
        out = self._to_openai_choices(per_gen_payloads)
        return JSONResponse(content=out.model_dump())

    # Helper methods
    def _get_base_messages(self, model_input: Dict[str, Any]) -> Tuple[str, List[Message]]:
        """Extract and validate base messages from request."""
        if "prompt" in model_input:
            raise HTTPException(status_code=400, detail='Use "messages" instead of "prompt" for chat models.')
        if "messages" not in model_input:
            raise HTTPException(status_code=400, detail='Request must include "messages" field.')
        
        key = "messages"
        msgs = model_input.get(key)
        if not isinstance(msgs, list):
            raise HTTPException(status_code=400, detail=f'"{key}" must be a list of messages.')

        for m in msgs:
            if not isinstance(m, dict) or "role" not in m or "content" not in m:
                raise HTTPException(status_code=400, detail=f'Each item in "{key}" must have role+content.')
        
        return key, msgs

    def _parse_fanout(self, model_input: Dict[str, Any]) -> Tuple[int, Optional[List[List[Message]]]]:
        """Parse and validate fan-out configuration."""
        suffix = model_input.get("suffix_messages", None)

        if not isinstance(suffix, list) or any(not isinstance(t, list) for t in suffix):
            raise HTTPException(status_code=400, detail='"suffix_messages" must be a list of tasks (each task is a list of messages).')
        if len(suffix) < 1 or len(suffix) > 256:
            raise HTTPException(status_code=400, detail='"suffix_messages" must have between 1 and 256 tasks.')

        for task in suffix:
            for m in task:
                if not isinstance(m, dict) or "role" not in m or "content" not in m:
                    raise HTTPException(status_code=400, detail="Each suffix message must have role+content.")

        return len(suffix), suffix

    def _to_openai_choices(self, payloads: List[Any]) -> Any:
        """Convert multiple payloads to OpenAI-style choices."""
        base = payloads[0]

        if hasattr(base, "choices") and hasattr(base, "model_dump"):
            new_choices = []
            for i, p in enumerate(payloads):
                c0 = p.choices[0]
                # Ensure index matches OpenAI n semantics
                try:
                    c0.index = i
                except Exception:
                    c0 = c0.model_copy(update={"index": i})
                new_choices.append(c0)

                # Aggregate usage statistics
                base.usage.completion_tokens += p.usage.completion_tokens
                base.usage.prompt_tokens += p.usage.prompt_tokens
                base.usage.total_tokens += p.usage.total_tokens

            base.choices = new_choices
            return base

        raise HTTPException(status_code=500, detail=f"Unsupported engine response type for fanout. {type(base)}")
    
    async def chat_completions( # if you need to use /v1/completions use def completions(..)
        self,
        model_input: Dict[str, Any],
        request: Request,
    ) -> Any:
        # alias to predict, so that both /predict and (/sync)/v1/chat/completions work
        return await self.predict(model_input, request)
```

### Fan-out generation configuration

To deploy the above example, create a new directory, e.g. `fanout` and create a `fanout/model/model.py` file.

Then create the following `config.yaml` at `fanout/config.yaml`

```yaml config.yaml theme={"system"}
model_name: Multi-Generation-LLM
resources:
  accelerator: H100
  cpu: '2'
  memory: 20Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.1-8B-Instruct"
    quantization_type: fp8
  runtime:
    served_model_name: "Multi-Generation-LLM"
```

At last, push the model with `truss push --publish`.

## Limitations and considerations

### What custom engine builder cannot do

**Custom tokenization:**

* Cannot modify the underlying tokenizer implementation
* Cannot add custom vocabulary or special tokens
* Must use the model's native tokenization

**Model architecture changes:**

* Cannot modify the TensorRT-LLM engine structure
* Cannot change attention mechanisms or model layers
* Cannot add custom model components

### When to use standard engine instead

* Standard chat completions without special requirements
* No need for business logic integration

## Monitoring and debugging

### Request tracing

```python theme={"system"}
import uuid
import os
from contextlib import asynccontextmanager

class Model:
    def __init__(self, trt_llm, **kwargs):
        self._engine = trt_llm["engine"]
        self._trace_enabled = os.environ.get("enable_tracing", True)
        
    @asynccontextmanager
    async def _trace_request(self, request_id: str):
        """Context manager for request tracing."""
        if self._trace_enabled:
            print(f"[TRACE] Start: {request_id}")
            start_time = time.time()
        
        try:
            yield
        finally:
            if self._trace_enabled:
                duration = time.time() - start_time
                print(f"[TRACE] End: {request_id} (duration: {duration:.3f}s)")
                
    async def predict(self, model_input: Dict[str, Any], request: Request) -> Any:
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        
        async with self._trace_request(request_id):
            # Main logic here
            response = await self._engine.chat_completions(request=request, model_input=model_input)
            return response
```

## Further reading

* [Engine-Builder-LLM overview](/engines/engine-builder-llm/overview): Main engine documentation.
* [Engine-Builder-LLM configuration](/engines/engine-builder-llm/engine-builder-config): Complete reference config.
* [Examples section](/examples/overview): Deployment examples.
* [Chains documentation](/development/chain/overview): Multi-model workflows.


# Reference config (Engine-Builder-LLM)
Source: https://docs.baseten.co/engines/engine-builder-llm/engine-builder-config

Complete reference config for dense text generation models

This reference covers all build and runtime options for Engine-Builder-LLM deployments. All settings use the `trt_llm` section in `config.yaml`.

## Configuration structure

```yaml theme={"system"}
trt_llm:
  inference_stack: v1  # Always v1 for Engine-Builder-LLM
  build:
    base_model: decoder
    checkpoint_repository: {...}
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: no_quant | fp8 | fp8_kv | fp4 | fp4_kv | fp4_mlp_only
    quantization_config: {...}
    tensor_parallel_count: 1
    plugin_configuration: {...}
    speculator: {...}  # Optional for lookahead decoding
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "model-name"
    total_token_limit: 500000
```

## Build configuration

The `build` section configures model compilation and optimization settings.

<ParamField type="string">
  The base model architecture for your model checkpoint.

  **Options:**

  * `decoder`: For CausalLM models (Llama, Mistral, Qwen, Gemma, Phi)

  ```yaml theme={"system"}
  build:
    base_model: decoder
  ```
</ParamField>

<ParamField type="object">
  Specifies where to find the model checkpoint. Repository must be a valid Hugging Face model repository with the standard structure (config.json, tokenizer files, model weights).

  **Source options:**

  * `HF`: Hugging Face Hub (default)
  * `GCS`: Google Cloud Storage
  * `S3`: AWS S3
  * `AZURE`: Azure Blob Storage
  * `REMOTE_URL`: HTTP URL to tar.gz file
  * `BASETEN_TRAINING`: Baseten Training checkpoints

  For detailed configuration options including training checkpoints and cloud storage setup, see [Deploy training and S3 checkpoints](/engines/performance-concepts/deployment-from-training-and-s3).

  ```yaml theme={"system"}
  checkpoint_repository:
    source: HF
    repo: "meta-llama/Llama-3.3-70B-Instruct"
    revision: main
    runtime_secret_name: hf_access_token
  ```
</ParamField>

<ParamField type="number">
  Maximum sequence length (context) for single requests. Range: 1 to 1048576.

  ```yaml theme={"system"}
  build:
    max_seq_len: 131072  # 128K context
  ```
</ParamField>

<ParamField type="number">
  Maximum number of input sequences processed concurrently. Range: 1 to 2048.

  Unless lookahead decoding is enabled, this parameter has little effect on performance. Keep it at 256 for most cases.
  Recommended not to be set below 8 to keep performance dynamic for various problems.

  ```yaml theme={"system"}
  build:
    max_batch_size: 256
  ```
</ParamField>

<ParamField type="number">
  Maximum number of batched input tokens after padding removal in each batch. Range: 256 to 131072, must be multiple of 64.

  If `enable_chunked_prefill: false`, this also limits the `max_seq_len` that can be processed. Recommended: `8192` or `16384`.

  ```yaml theme={"system"}
  build:
    max_num_tokens: 16384
  ```
</ParamField>

<ParamField type="string">
  Specifies the quantization format for model weights.

  **Options:**

  * `no_quant`: `FP16`/`BF16` precision
  * `fp8`: `FP8` weights + 16-bit KV cache
  * `fp8_kv`: `FP8` weights + `FP8` KV cache
  * `fp4`: `FP4` weights + 16-bit KV cache (B200 only)
  * `fp4_kv`: `FP4` weights + `FP8` KV cache (B200 only)
  * `fp4_mlp_only`: `FP4` MLP only + 16-bit KV (B200 only)

  For detailed quantization guidance, see [Quantization Guide](/engines/performance-concepts/quantization-guide).

  ```yaml theme={"system"}
  build:
    quantization_type: fp8_kv
  ```
</ParamField>

<ParamField type="object">
  Configuration for post-training quantization calibration.

  **Fields:**

  * `calib_size`: Size of calibration dataset (64-16384, multiple of 64). Defines how many rows of the train split with text column to take.
  * `calib_dataset`: HuggingFace dataset for calibration. Dataset must have 'text' column (str type) for samples, or 'train' split as subsection.
  * `calib_max_seq_length`: Maximum sequence length for calibration.

  ```yaml theme={"system"}
  build:
    quantization_type: fp8
    quantization_config:
      calib_size: 1536
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 1024
  ```
</ParamField>

<ParamField type="number">
  Number of GPUs to use for tensor parallelism. Range: 1 to 8.

  ```yaml theme={"system"}
  build:
    tensor_parallel_count: 4  # For 70B+ models
  ```
</ParamField>

<ParamField type="object">
  TensorRT-LLM plugin configuration for performance optimization.

  **Fields:**

  * `paged_kv_cache`: Enable paged KV cache (recommended: true)
  * `use_paged_context_fmha`: Enable paged context FMHA (recommended: true)
  * `use_fp8_context_fmha`: Enable `FP8` context FMHA (requires `FP8_KV` quantization)

  ```yaml theme={"system"}
  build:
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true  # For FP8_KV quantization
  ```
</ParamField>

<ParamField type="object">
  Configuration for speculative decoding with lookahead. For detailed configuration, see [Lookahead decoding](/engines/engine-builder-llm/lookahead-decoding).

  **Fields:**

  * `speculative_decoding_mode`: `LOOKAHEAD_DECODING` (recommended)
  * `lookahead_windows_size`: Window size for speculation (1-8)
  * `lookahead_ngram_size`: N-gram size for patterns (1-16)
  * `lookahead_verification_set_size`: Verification buffer size (1-8)
  * `enable_b10_lookahead`: Enable Baseten's lookahead algorithm

  ```yaml theme={"system"}
  build:
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 3
      enable_b10_lookahead: true
  ```
</ParamField>

<ParamField type="number">
  Number of GPUs to use during the build job. Only set this if you encounter errors during the build job. It has no impact once the model reaches the deploying stage. If not set, equals `tensor_parallel_count`.

  ```yaml theme={"system"}
  build:
    num_builder_gpus: 2
  ```
</ParamField>

## Runtime configuration

The `runtime` section configures inference engine behavior.

<ParamField type="number">
  Fraction of GPU memory to reserve for KV cache. Range: 0.1 to 1.0.

  ```yaml theme={"system"}
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.85
  ```
</ParamField>

<ParamField type="boolean">
  Enable chunked prefilling for long sequences.

  ```yaml theme={"system"}
  runtime:
    enable_chunked_context: true
  ```
</ParamField>

<ParamField type="string">
  Policy for scheduling requests in batches.

  **Options:**

  * `max_utilization`: Maximize GPU utilization (may evict requests)
  * `guaranteed_no_evict`: Guarantee request completion (recommended)

  ```yaml theme={"system"}
  runtime:
    batch_scheduler_policy: guaranteed_no_evict
  ```
</ParamField>

<ParamField type="string">
  Model name returned in API responses.

  ```yaml theme={"system"}
  runtime:
    served_model_name: "Llama-3.3-70B-Instruct"
  ```
</ParamField>

<ParamField type="number">
  Maximum number of tokens that can be scheduled at once. Range: 1 to 1000000.

  ```yaml theme={"system"}
  runtime:
    total_token_limit: 1000000
  ```
</ParamField>

## Configuration examples

### Llama 3.3 70B

```yaml theme={"system"}
model_name: Llama-3.3-70B-Instruct
resources:
  accelerator: H100:4
  cpu: '4'
  memory: 40Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.3-70B-Instruct"
      revision: main
      runtime_secret_name: hf_access_token
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: fp8_kv
    tensor_parallel_count: 4
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Llama-3.3-70B-Instruct"
```

### Qwen 2.5 32B with lookahead decoding

```yaml theme={"system"}
model_name: Qwen-2.5-32B-Lookahead
resources:
  accelerator: H100:2
  cpu: '2'
  memory: 20Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-32B-Instruct"
      revision: main
    max_seq_len: 32768
    max_batch_size: 128
    max_num_tokens: 8192
    quantization_type: fp8_kv
    tensor_parallel_count: 2
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 3
      enable_b10_lookahead: true
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.85
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Qwen-2.5-32B-Instruct"
```

### Small model on L4

```yaml theme={"system"}
model_name: Llama-3.2-3B-Instruct
resources:
  accelerator: L4
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.2-3B-Instruct"
      revision: main
    max_seq_len: 8192
    max_batch_size: 256
    max_num_tokens: 4096
    quantization_type: fp8
    tensor_parallel_count: 1
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: false
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Llama-3.2-3B-Instruct"
```

### B200 with `FP4` quantization

```yaml theme={"system"}
model_name: Qwen-2.5-32B-FP4
resources:
  accelerator: B200
  cpu: '2'
  memory: 20Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-32B-Instruct"
      revision: main
    max_seq_len: 32768
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: fp4_kv
    tensor_parallel_count: 1
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Qwen-2.5-32B-Instruct"
```

## Validation and troubleshooting

### Common errors

**Error:** `FP8 quantization is only supported on L4, H100, H200, B200`

* **Cause:** Using `FP8` quantization on unsupported GPU.
* **Fix:** Use H100 or newer GPU, or use `no_quant`.

**Error:** `FP4 quantization is only supported on B200`

* **Cause:** Using `FP4` quantization on unsupported GPU.
* **Fix:** Use B200 GPU or `FP8` quantization.

**Error:** `Using fp8 context fmha requires fp8 kv, or fp4 with kv cache dtype`

* **Cause:** Mismatch between quantization and context FMHA settings.
* **Fix:** Use `fp8_kv` quantization or disable `use_fp8_context_fmha`.

**Error:** `Tensor parallelism and GPU count must be the same`

* **Cause:** Mismatch between `tensor_parallel_count` and GPU count.
* **Fix:** Ensure `tensor_parallel_count` matches `accelerator` count.

### Performance tuning

**For lowest latency:**

* Reduce `max_batch_size` and `max_num_tokens`.
* Use `batch_scheduler_policy: guaranteed_no_evict`.
* Consider smaller models or quantization.

**For highest throughput:**

* Increase `max_batch_size` and `max_num_tokens`.
* Use `batch_scheduler_policy: max_utilization`.
* Enable quantization on supported hardware.

**For cost optimization:**

* Use L4 GPUs with `FP8` quantization.
* Choose appropriately sized models.
* Tune `max_seq_len` to your actual requirements.

## Model repository structure

All model sources (S3, GCS, HuggingFace, or tar.gz) must follow the standard HuggingFace repository structure. Files must be in the root directory, similar to running:

```bash theme={"system"}
git clone https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct
```

### Required files

**Model configuration (`config.json`):**

* `max_position_embeddings`: Limits maximum context size (content beyond this is truncated).
* `vocab_size`: Vocabulary size for the model.
* `architectures`: Must include `LlamaForCausalLM`, `MistralForCausalLM`, or similar causal LM architectures. Custom code is typically not read.
* `torch_dtype`: Default inference dtype (`float16` or `bfloat16`). Cannot be a pre-quantized model.

**Model weights (`model.safetensors`):**

* Or: `model.safetensors.index.json` + `model-xx-of-yy.safetensors` (sharded).
* Convert to safetensors if you encounter issues with other formats.
* Cannot be a pre-quantized model. Model must be an `fp16`, `bf16`, or `fp32` checkpoint.

**Tokenizer files (`tokenizer_config.json` and `tokenizer.json`):**

* For maximum compatibility, use "FAST" tokenizers compatible with Rust.
* Cannot contain custom Python code.
* For chat completions: must contain `chat_template`, a Jinja2 template.

### Architecture support

| **Model family** | **Supported architectures**            | **Notes**                                           |
| ---------------- | -------------------------------------- | --------------------------------------------------- |
| **Llama**        | `LlamaForCausalLM`                     | Full support for Llama 3. For Llama 4, use BIS-LLM. |
| **Mistral**      | `MistralForCausalLM`                   | Including v0.3 and Small variants.                  |
| **Qwen**         | `Qwen2ForCausalLM`, `Qwen3ForCausalLM` | Including Qwen 2.5 and Qwen 3 series.               |
| **QwenMoE**      | `Qwen3MoEForCausalLM`                  | Specfic support for Qwen3MoE.                       |
| **Gemma**        | `GemmaForCausalLM`                     | Including Gemma 2 and Gemma 3 series, bf16 only.    |

## Best practices

### Model size and GPU selection

| **Model size** | **Recommended GPU** | **Quantization** | **Tensor parallel** |
| -------------- | ------------------- | ---------------- | ------------------- |
| `<8B`          | L4/H100             | `FP8_KV`         | 1                   |
| 8B-70B         | H100                | `FP8_KV`         | 1-2                 |
| 70B+           | H100/B200           | `FP8_KV`/`FP4`   | 4+                  |

### Production recommendations

* Use `quantization_type: fp8_kv` for best performance/accuracy balance.
* Set `max_batch_size` based on your expected traffic patterns.
* Enable `paged_kv_cache` and `use_paged_context_fmha` for optimal performance.

### Development recommendations

* Use `quantization_type: no_quant` for fastest iteration.
* Set smaller `max_seq_len` to reduce build time.
* Use `batch_scheduler_policy: guaranteed_no_evict` for predictable behavior.


# Speculative decoding guide
Source: https://docs.baseten.co/engines/engine-builder-llm/lookahead-decoding

Faster inference with speculative decoding for coding agents and text generation

Lookahead decoding is a speculative decoding technique that provides 2x-4x faster inference for suitable workloads by predicting future tokens using n-gram patterns. It's particularly effective for coding agents and content with predictable patterns.

## Overview

Lookahead decoding identifies n-gram patterns in the input context and past tokens, speculates on future tokens by generating candidate sequences, verifies predictions against the model's actual output, and accepts verified tokens in a single step.

The technique works with any model compatible with Engine-Builder-LLM. Baseten's B10 Lookahead implementation searches up to 10M past tokens for n-gram matches across language patterns.

## When to use lookahead decoding

Lookahead decoding excels at code generation where programming language syntax creates predictable patterns, and function signatures, variable names, and common idioms all benefit. It also accelerates prompt lookup scenarios where you provide example completions in the prompt, and general low-latency use cases where you can trade slightly decreased throughput for faster individual responses.

### Limitations

* Lookahead is supported on A10G, L4, A100, H100\_40GB, H200, and H100. Other GPUs may not be supported.
* During speculative decoding, sampling is disabled and temperature is set to 0.0.
* Speculative decoding does not affect output quality. The output depends only on model weights and prompt.
* Speculative decoding generates multiple tokens at a time. Structured output (xgrammar, outlines) with state-machine guarantees (enforced json via `response_format`) is not possible with `engine-builder-llm`.
* For few versions, chunked prefill is now allowed with lookahead decoding, we will dynamically disable chunked prefill in this case.

## Configuration

### Basic lookahead configuration

Add a `speculator` section to your build configuration:

```yaml theme={"system"}
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-7B-Instruct"
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 3
      enable_b10_lookahead: true
```

### Configuration parameters

**`speculative_decoding_mode`**: Set to `LOOKAHEAD_DECODING` to enable Baseten's lookahead decoding algorithm.

**`lookahead_ngram_size`**: Size of n-gram patterns for speculation. Range: 1-64, default: 8. Use `4` for simple patterns, `8` for general use (recommended), or `16-32` for complex, highly predictable patterns.

**`lookahead_verification_set_size`**: Size of verification buffer for speculation. Range: 1-8. Use `1` for high-confidence patterns, `3` for general use (recommended), or `5` for complex patterns requiring more verification.

**`lookahead_windows_size`**: Size of the speculation window. Range: 1-8. Set to the same value as `lookahead_verification_set_size`.

**`enable_b10_lookahead`**: Enable Baseten's optimized lookahead algorithm. Default: `true`. Recommenedation to keep it to `true`.

### Performance tuning

**For coding agents:** Use smaller window sizes with moderate n-gram sizes:

```yaml theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 1
  lookahead_ngram_size: 8
  lookahead_verification_set_size: 3
  enable_b10_lookahead: true
```

**For general text generation:** Use balanced window and n-gram sizes:

```yaml theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 3
  lookahead_ngram_size: 8
  lookahead_verification_set_size: 3
  enable_b10_lookahead: true
```

**For highly predictable content:** Use larger n-gram sizes with conservative verification:

```yaml theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 1
  lookahead_ngram_size: 32
  lookahead_verification_set_size: 1
  enable_b10_lookahead: true
```

## Performance impact

### Batch size considerations

Lookahead decoding performs best with smaller batch sizes. Set `max_batch_size` to 32 or 64, depending on your use case.

### Memory overhead

Lookahead decoding does not require additional GPU memory.

## Production best practices

### Recommended configurations

**Standard (general purpose):** Balanced settings for general-purpose text generation:

```yaml theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 3
  lookahead_ngram_size: 8
  lookahead_verification_set_size: 3
  enable_b10_lookahead: true
```

**Dynamic content (less predictable):**

Setting `enable_b10_lookahead: true` and `lookahead_windows_size: 1 + lookahead_verification_set_size: 1` will enable dynamic length speculation.
The speculated length will depend on the quality of the lookup match. By default we will speculate "a n-gram of k tokens for a k token suffix match".

```yaml theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 1
  lookahead_ngram_size: 32
  lookahead_verification_set_size: 1
  enable_b10_lookahead: true
```

**Code generation (highly predictable):** Code has predictable syntax patterns, so you can use larger windows:

```yaml theme={"system"}
speculator:
  speculative_decoding_mode: LOOKAHEAD_DECODING
  lookahead_windows_size: 7
  lookahead_ngram_size: 5
  lookahead_verification_set_size: 7
  enable_b10_lookahead: true
```

### Build configuration

Set `max_batch_size` to control batch size limits:

```yaml theme={"system"}
trt_llm:
  build:
    max_batch_size: 64  # Recommended for lookahead decoding
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      # ... other speculator config
```

### Engine optimization

* Use smaller batch sizes for maximum benefit (1-8 requests)
* Monitor memory overhead and adjust KV cache allocation
* Test with your specific workload for optimal parameters

## Examples

### Code generation example

Deploy a coding model with lookahead decoding on an H100:

```yaml theme={"system"}
model_name: Qwen-Coder-7B-Lookahead
resources:
  accelerator: H100
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-7B-Instruct"
    quantization_type: fp8
    max_batch_size: 64
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 1
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 1
      enable_b10_lookahead: true
  runtime:
    served_model_name: "Qwen-Coder-7B"
```

## Integration examples - Python code generation

Generate code using the chat completions API:

```python theme={"system"}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

# Generate Python function refactor with lookahead decoding
code = "python\ndef hello_world(name):\n    print(42)"

response = client.chat.completions.create(
    model="not-required",
    messages=[
        {
            "role": "system", 
            "content": "You are a Python programming assistant. Write clean, efficient code."
        },
        {
            "role": "user", # By providing the code anywhere in the prompt, the generation is much faster.
            "content": f"Please refactor the follwing function to have docstrings. {code}"
        }
    ],
    temperature=0.0,
    max_tokens=200
)

print(response.choices[0].message.content)
```

## Best practices

### Configuration optimization

For coding assistants, use `lookahead_windows_size: 1` with `lookahead_ngram_size: 8` and keep batch sizes under 16 for best performance. For structured content like yamls or xml, use `lookahead_windows_size: 1` with `lookahead_ngram_size: 8`, note that `"response_format"` enforcement is not available with Engine-Builder-LLM Lookeahead decoding. For general use, start with default settings (window=3, ngram=8) and adjust based on your content patterns.

### Performance monitoring

Track tokens/second with and without lookahead to measure speed improvement, verification accuracy to see how often speculations succeed, and memory usage to catch overhead. If speed improvement diminishes, reduce batch size. Adjust window size based on content predictability and ngram size based on verification accuracy.

### Troubleshooting

**Common issues:**

**Low speed improvement:**

* Check if content is suitable for lookahead decoding
* Reduce batch size for better performance
* Adjust window and ngram sizes

**Blackwell support**

* Lookahead is not fully supported in `Engine-Builder-LLM`, check [BIS-LLM overview](/engines/bis-llm/overview) for Blackwell support.

## Further reading

* [Engine-Builder-LLM overview](/engines/engine-builder-llm/overview): Main engine documentation.
* [Engine-Builder-LLM configuration](/engines/engine-builder-llm/engine-builder-config): Complete reference config.
* [Structured outputs documentation](/engines/performance-concepts/structured-outputs): JSON schema validation.
* [Examples section](/examples/speculative-decoding): Deployment examples.


# LoRA support
Source: https://docs.baseten.co/engines/engine-builder-llm/lora-support

Multi-LoRA adapters for Engine-Builder-LLM engine

Engine-Builder-LLM supports multi-LoRA deployments with runtime adapter switching. Share base model weights across fine-tuned variants and switch adapters without redeployment.

## Overview

Deploy multiple LoRA adapters on a single base model and switch between them at inference time. The engine shares base model weights across all adapters for memory efficiency.

## Configuration

### Basic LoRA configuration

```yaml theme={"system"}
model_name: Qwen2.5-Coder-LoRA
resources:
  accelerator: H100
  cpu: '2'
  memory: 20Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-Coder-1.5B-Instruct"
      revision: "2e1fd397ee46e1388853d2af2c993145b0f1098a"
    lora_adapters:
      lora1:
        repo: "ai-blond/Qwen-Qwen2.5-Coder-1.5B-Instruct-lora"
        revision: "9cde18d8ed964b0519fb481cca6acd936b2ca811"
        source: "HF"
    max_lora_rank: 16
    plugin_configuration:
      lora_plugin: "float16"
  runtime:
    served_model_name: "Qwen2.5-Coder-base"
```

## Limitations

* **Same rank and same modules**: For optimal performance and stability, the LoRA adapters for one deployment should be uniform. All target modules must be the same.
* **Build time availability**: The engine relies on numpy-style weights. These need to be pre-converted during deployment and distributed to each replica. For Engine-Builder-LLM, these repos must be known ahead of time.
* **Inference performance**: If you're using only one LoRA adapter, merging the adapter into the base weights provides better performance. Additional LoRA adapters add complexity to kernel selection and fundamentally increase flops.

## LoRA adapter configuration

### Adapter repository structure

LoRA adapters must follow the standard HuggingFace repository structure:

```
adapter-repo/
├── adapter_config.json
├── adapter_model.safetensors
└── README.md
```

### Required files

**adapter\_config.json**

```yaml theme={"system"}
  # same base model for all configs 
  "base_model_name_or_path": "Qwen/Qwen2.5-Coder-1.5B-Instruct", 
  # same target modules among all lora adapters 
  "target_modules": [
    "attn_q",
    "attn_k", 
    "attn_v",
    "attn_dense",
    "mlp_h_to_4h",
    "mlp_4h_to_h",
    "mlp_gate"
  ],
  # same rank among all lora adapters
  "r": 16
```

**model.lora\_weights.npy**

* NumPy array containing LoRA weight matrices
* Shape: `(num_layers, rank, hidden_size, hidden_size)`
* Must match the target modules specified in config

**model.lora\_config.npy**

* NumPy array containing LoRA configuration
* Includes scaling factors and other parameters
* Must match the adapter\_config.json specifications

## Build configuration options

### `lora_adapters`

Dictionary of LoRA adapters to load during build:

```yaml theme={"system"}
lora_adapters:
  adapter_name:
    repo: "username/model-name"
    revision: "main"
    source: "HF"  # or "GCS", "S3", "AZURE"
```

### `max_lora_rank`

Maximum LoRA rank for all adapters.

```yaml theme={"system"}
max_lora_rank: 16  # Default: 8
```

**Range**: 1 to 64, must be power of 2
**Recommended**: Set to exactly the rank `r` that you use for all adapters.

### `plugin_configuration`

LoRA plugin configuration:

```yaml theme={"system"}
plugin_configuration:
  lora_plugin: "float16" 
```

**Options:**

* `float16`: Reduced memory usage, slight accuracy impact.
* `float32`: Higher precision, much slower inference.

## Engine inference configuration

The model parameter in OpenAI-format requests selects which adapter to use. For the above example, valid model names are `Qwen2.5-Coder-base` or `lora1`.

This lets you select different adapters at runtime through the OpenAI client.

## Further reading

* [Engine-Builder-LLM overview](/engines/engine-builder-llm/overview): Main engine documentation.
* [Engine-Builder-LLM configuration](/engines/engine-builder-llm/engine-builder-config): Complete reference config.
* [Custom engine builder](/engines/engine-builder-llm/custom-engine-builder): Custom model.py implementation.
* [Quantization guide](/engines/performance-concepts/quantization-guide): Performance optimization.


# Overview
Source: https://docs.baseten.co/engines/engine-builder-llm/overview

Dense LLM text generation with lookahead decoding and structured outputs

Engine-Builder-LLM optimizes dense text generation models with [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM), delivering up to 4000 tokens/second for code generation with [lookahead decoding](/engines/engine-builder-llm/lookahead-decoding). The engine supports [structured outputs](/engines/performance-concepts/structured-outputs) for JSON schema validation.

## Use cases

**Model families:**

* **Llama**: `meta-llama/Llama-3.3-70B-Instruct`, `meta-llama/Llama-3.2-3B-Instruct`.
* **Qwen**: `Qwen/Qwen2.5-72B-Instruct`, `Qwen3/Qwen3-8B`, `Qwen/QwQ-32B-Preview`.
* **Mistral**: `mistralai/Mistral-7B-Instruct-v0.3`, `mistralai/Mistral-Small-24B-Instruct`.
* **DeepSeek**: `deepseek-ai/DeepSeek-R1-Distill-Llama-70B`.
* **Gemma 3**: `google/gemma-3-27b-it`, `google/gemma-3-12b-it`.
* **Microsoft**: `microsoft/Phi-4`.

Engine-Builder-LLM handles high-throughput dialogue systems, coding assistants with lookahead decoding, and content generation with structured outputs. The engine's speculative decoding accelerates code generation by 2-4x, making it ideal for coding agents and JSON-heavy workloads.

### LoRA support

Engine-Builder-LLM supports [multi-LoRA](/engines/engine-builder-llm/lora-support) deployments with engine adapter switching:

<CardGroup>
  <Card title="Multi-LoRA" href="/engines/engine-builder-llm/lora-support" icon="layers">
    Multiple adapters, engine switching, parameter-efficient fine-tuning
  </Card>

  <Card title="Quick start" href="/engines/engine-builder-llm/lora-support" icon="rocket-launch">
    Deploy LoRA adapters in minutes
  </Card>
</CardGroup>

### Structured outputs

Engine-Builder-LLM supports OpenAI-compatible structured outputs with JSON schema validation:

<CardGroup>
  <Card title="Features" href="/engines/performance-concepts/structured-outputs#engine-builder-llm" icon="check-circle">
    Full OpenAI compatibility, JSON schema validation, complex nested schemas
  </Card>

  <Card title="Quick start" href="/engines/performance-concepts/structured-outputs" icon="rocket-launch">
    Get started with structured outputs in minutes
  </Card>
</CardGroup>

### Key benefits

<CardGroup>
  <Card title="Low latency" icon="lightning-bolt">
    TensorRT-LLM compilation optimizes time-to-first-token.
  </Card>

  <Card title="High throughput" icon="rocket-launch">
    Batching and kernel optimization maximize tokens per second.
  </Card>

  <Card title="Lookahead decoding" icon="eye">
    Speculative decoding accelerates coding agents and predictable content.
  </Card>

  <Card title="Structured outputs" icon="shapes">
    JSON schema validation for controlled text generation.
  </Card>
</CardGroup>

## Architecture support

### Supported model types

Engine-Builder-LLM supports all causal language model architectures that end with `ForCausalLM`:

**Primary architectures:**

* `LlamaForCausalLM`: Llama family models.
* `Qwen2ForCausalLM`: Qwen family models.
* `MistralForCausalLM`: Mistral family models.
* `Gemma2ForCausalLM`: Gemma family models.
* `Phi3ForCausalLM`: Phi family models.

**Automatic detection:**

The engine automatically detects the model architecture from the checkpoint repository and applies appropriate optimizations.

### Model size support

| **Model Size** | **Single GPU** | **Tensor Parallel** | **Recommended GPU** |
| -------------- | -------------- | ------------------- | ------------------- |
| `<8B`          | L4, A10G, H100 | N/A                 | L4 (cost-effective) |
| 8B-70B         | H100           | TP1-TP2             | H100 (2 GPUs)       |
| 70B+           | H100 / B200    | TP4+                | H100 (4+ GPUs)      |

## Advanced features

### Lookahead decoding

Lookahead decoding accelerates inference for code generation, JSON output, and templated content by speculating on future tokens using n-gram patterns.

**Best for:**

* **Code generation**: Highly predictable patterns in code.
* **Structured content**: Reliable JSON, YAML, XML generation.
* **Mathematical expressions**: Predictable mathematical notation.
* **Template completion**: Filling in predictable templates.

Enable lookahead decoding by adding a `speculator` section:

```yaml theme={"system"}
trt_llm:
  build:
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 1
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 1
      enable_b10_lookahead: true
```

**Performance impact:**

* **Speed improvement**: Up to 2x faster for code and structured content.
* **Prompt lookup**: Up to 10x faster for prompt-lookup workloads like code apply, reaching 4000 tokens/s per request on Qwen-3-8B with a single H100.
* **Optimal batch size**: Less than 32 requests for best performance.

### Structured outputs

Generate text that conforms to JSON schemas for reliable data extraction and controlled generation.

**Use cases:**

* **Data extraction**: Extract structured information from unstructured text.
* **API response generation**: Generate JSON responses for APIs.
* **Configuration generation**: Create structured configuration files.
* **Content validation**: Ensure generated content meets specific criteria.

Structured outputs work out of the box with no extra configuration. Define a Pydantic schema:

```python theme={"system"}
import os
from pydantic import BaseModel
from openai import OpenAI

class User(BaseModel):
    name: str
    age: int
    email: str

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

response = client.beta.chat.completions.parse(
    model="not-required",
    messages=[
        {"role": "user", "content": "Extract user info from: John is 25 years old and his email is john@example.com"}
    ],
    response_format=User
)

user = response.choices[0].message.parsed
print(f"Name: {user.name}, Age: {user.age}, Email: {user.email}")
```

### Quantization options

Engine-Builder-LLM supports multiple [quantization](/engines/performance-concepts/quantization-guide) formats for different performance and accuracy trade-offs.

**Quantization types:**

* `no_quant`: `FP16`/`BF16` precision (baseline).
* `fp8`: `FP8` weights + 16-bit KV cache (2x speedup).
* `fp8_kv`: `FP8` weights + `FP8` KV cache (2.5x speedup).
* `fp4`: `FP4` weights + 16-bit KV cache (4x speedup, B200 only).
* `fp4_kv`: `FP4` weights + `FP8` KV cache (4.5x speedup, B200 only).
* `fp4_mlp_only`: `FP4` MLP only + 16-bit KV (3x speedup, B200 only).

**Hardware requirements:**

Hardware requirements vary by quantization type.

| **Quantization**                | **Minimum GPU**      | **Memory reduction** | **Speed improvement** |
| ------------------------------- | -------------------- | -------------------- | --------------------- |
| `no_quant`                      | A100                 | None                 | Baseline              |
| `fp8`                           | L4, H100, H200, B200 | 50%                  | 2x                    |
| `fp8_kv`                        | L4, H100, H200, B200 | 60%                  | 2.5x                  |
| `fp4`, `fp4_kv`, `fp4_mlp_only` | B200 only            | 75%                  | 3-4.5x                |

## Configuration examples

### Basic Llama 3.3 70B deployment

Llama 3.3 70B on H100 GPUs with `FP8` quantization:

```yaml theme={"system"}
model_name: Llama-3.3-70B-Instruct
resources:
  accelerator: H100:4  # 4 GPUs for 70B model
  cpu: '4'
  memory: 40Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.3-70B-Instruct"
      revision: main
      runtime_secret_name: hf_access_token
    max_seq_len: 131072
    max_batch_size: 256
    max_num_tokens: 8192
    quantization_type: fp8_kv
    tensor_parallel_count: 4
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true
    quantization_config:
      calib_size: 1024
      calib_dataset: "cnn_dailymail"
      calib_max_seq_length: 2048
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Llama-3.3-70B-Instruct"
```

### Qwen 2.5 32B with lookahead decoding

Qwen 2.5 32B with *speculative decoding* for faster inference. Read more on [lookahead decoding here](/engines/engine-builder-llm/lookahead-decoding.mdx)

```yaml theme={"system"}
model_name: Qwen-2.5-32B-Lookahead
resources:
  accelerator: H100:1
  cpu: '2'
  memory: 20Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-Coder-32B-Instruct"
      revision: main
    max_seq_len: 32768
    max_batch_size: 128
    max_num_tokens: 8192
    quantization_type: fp8 # no fp8_kv for qwen2.5 models
    tensor_parallel_count: 1
    num_builder_gpus: 2 # will be loaded in bf16 for quantization, will require `2x32Gb memory -> 2H100s
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 3
      enable_b10_lookahead: true
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: true
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.85
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Qwen-2.5-Coder-32B-Instruct"
```

### Small model for cost-effective deployment

Llama 3.2 3B on an L4 GPU for cost efficiency:

```yaml theme={"system"}
model_name: Llama-3.2-3B-Instruct
resources:
  accelerator: L4
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.2-3B-Instruct"
      revision: main
    max_seq_len: 8192
    max_batch_size: 256
    max_num_tokens: 4096
    quantization_type: fp8
    tensor_parallel_count: 1
    plugin_configuration:
      paged_kv_cache: true
      use_paged_context_fmha: true
      use_fp8_context_fmha: false
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.9
    enable_chunked_context: true
    batch_scheduler_policy: guaranteed_no_evict
    served_model_name: "Llama-3.2-3B-Instruct"
```

## Performance characteristics

### Latency and throughput factors

Performance depends on model size (smaller models respond faster), quantization (`FP8`/`FP4` reduces memory and improves throughput), lookahead decoding (effective for code and structured content), batch size (larger batches improve throughput at the cost of latency), and hardware (H100 and B200 GPUs deliver the best results).

### Memory usage considerations

**Memory optimization factors:**

* **Quantization**: `FP8` reduces memory by \~50%, `FP4` by \~75%.
* **Lookahead decoding**: Minimal additional memory overhead.
* **Tensor parallelism**: Distributes memory across multiple GPUs.
* **KV cache management**: Configurable memory allocation for context handling.

## Integration examples

### OpenAI-compatible inference

Engine-Builder-LLM deployments are OpenAI compatible, enabling use of the standard OpenAI SDK.

```python theme={"system"}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

# Standard chat completion
response = client.chat.completions.create(
    model="not-required",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)

# Streaming completion
for chunk in client.chat.completions.create(
    model="not-required",
    messages=[{"role": "user", "content": "Write a poem about AI"}],
    stream=True,
):
    print(chunk.choices[0].delta.content or "", end="")
```

Point `base_url` to your model's production endpoint. Find this URL in your Baseten dashboard after deployment. The `model` parameter can be any string since Baseten routes based on the URL, not this field. Set `stream=True` to receive tokens as they're generated.

Running this returns a chat completion response with the model's answer in `response.choices[0].message.content`, or streams chunks with partial content in `delta.content`.

### Performant Client Usage

For high-throughput batch processing, use the [Performance Client](/engines/performance-concepts/performance-client) which handles concurrent requests efficiently.

```python theme={"system"}
from baseten_performance_client import PerformanceClient

client = PerformanceClient(
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync", 
    api_key=os.environ['BASETEN_API_KEY']
)

# Batch chat completions with stream=False
payloads = [
    {
        "model": "model",
        "messages": [{"role": "user", "content": "Explain quantum computing"}],
        "stream": False,
        "max_tokens": 500
    },
    {
        "model": "model", 
        "messages": [{"role": "user", "content": "Write a poem about AI"}],
        "stream": False,
        "max_tokens": 300
    }
] * 10  # 20 total requests

response = client.batch_post(
    url_path="/v1/chat/completions",
    payloads=payloads,
)

# Access 20 responses
for i, resp in enumerate(response.data):
    print(f"Response {i+1}: {resp['choices'][0]['message']['content']}")
```

**Use cases:** Bulk content generation, Unlocked GIL during Request, batch data processing, performance benchmarking.

### Structured outputs

*Structured outputs* guarantee the response matches your Pydantic schema.

```python theme={"system"}
import os
from pydantic import BaseModel
from openai import OpenAI

class Task(BaseModel):
    title: str
    priority: str
    due_date: str
    description: str

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

response = client.beta.chat.completions.parse(
    model="not-required",
    messages=[
        {"role": "user", "content": "Create a task for: Review the quarterly report by next Friday"}
    ],
    response_format=Task
)

task = response.choices[0].message.parsed
print(f"Task: {task.title}")
print(f"Priority: {task.priority}")
```

Define your schema as a Pydantic model with typed fields. Pass it to `response_format` and use `beta.chat.completions.parse` instead of the regular `create` method.

The response includes a `parsed` attribute with your data already converted to a `Task` object, so no JSON parsing is needed.

### Function calling

*Function calling* lets the model invoke your functions with structured arguments. Define available tools, and the model returns function calls when appropriate.

```python theme={"system"}
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name, e.g., San Francisco"
                }
            },
            "required": ["location"]
        }
    }
}]

response = client.chat.completions.create(
    model="not-required",
    messages=[{"role": "user", "content": "What's the weather like in Boston?"}],
    tools=tools
)

tool_call = response.choices[0].message.tool_calls[0]
print(f"Function: {tool_call.function.name}")
print(f"Arguments: {tool_call.function.arguments}")
```

Define each tool with a `name`, `description`, and JSON schema for `parameters`. The description helps the model decide when to use the tool.

When the model chooses to call a function, `tool_calls` contains the function name and JSON-encoded arguments. Your code executes the function and optionally sends the result back for a final response.

## Best practices

### Model selection

**For cost-effective deployments:**

* Use models under 8B parameters on L4 GPUs, H100 or H100\_40GB.
* Consider quantization for memory efficiency.
* Implement autoscaling for variable traffic.

**For high-performance deployments:**

* Use H100 GPUs with `FP8` quantization.
* Enable lookahead decoding for code generation.
* Use tensor parallelism for large models.

**For coding assistants:**

* Use models trained on code (Qwen-Coder, CodeLlama).
* Enable lookahead decoding with window size 1 for maximum throughput.
* Consider smaller models for faster response times.

### Hardware optimization

**GPU selection:**

* **L4 or H100\_40GB**: Best for models under 15B parameters, cost-effective.
* **H100\_80GB**: Recommended for models 15-70B parameters for optimal performance.
* **H100**: Best for models 15-70B parameters, high performance.
* **B200**: Required for `FP4` quantization.

**Memory optimization:**

* Use quantization to reduce memory usage.
* Lower max\_seq\_len or enable chunked prefill.
* Monitor memory usage during deployment.

### Performance tuning

**For lowest latency:**

* Use smaller models when possible.
* Enable lookahead decoding for code generation.

**For highest throughput:**

* Use larger batch sizes.
* Enable `FP8`/`FP4` quantization.
* Use tensor parallelism for large models.

**For cost efficiency:**

* Use L4 GPUs with quantization.
* Implement efficient autoscaling.
* Choose appropriately sized models.

## Migration guide

### From other deployment systems

Coming from vLLM? Here's how the configuration maps:

```yaml theme={"system"}
# vLLM configuration (old)
model: "meta-llama/Llama-3.3-70B-Instruct"
tensor_parallel_size: 4
quantization: "fp8"

# Engine-Builder-LLM configuration (new)
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.3-70B-Instruct"
    quantization_type: fp8_kv
    tensor_parallel_count: 4
```

## Further reading

* [Engine-Builder-LLM reference config](/engines/engine-builder-llm/engine-builder-config): Complete configuration options.
* [Structured outputs](/engines/performance-concepts/structured-outputs): JSON schema validation and controlled generation.
* [Lookahead decoding guide](/engines/engine-builder-llm/lookahead-decoding): Advanced speculative decoding.
* [Custom engine builder](/engines/engine-builder-llm/custom-engine-builder): Custom model.py implementation.
* [Quantization guide](/engines/performance-concepts/quantization-guide): `FP8`/`FP4` trade-offs and hardware requirements.
* [TensorRT-LLM examples](/examples/tensorrt-llm): Concrete deployment examples.


# Overview
Source: https://docs.baseten.co/engines/index

Engine selection guide for embeddings, dense LLMs, and MoE models

Baseten engines optimize model inference for specific architectures using [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM). Select an engine based on your model type (embeddings, dense LLMs, or mixture-of-experts) to achieve the best latency and throughput.

## Engine ecosystem

<CardGroup>
  <Card title="BEI (Embeddings & Classification)" href="/engines/bei/overview" icon="brain-circuit">
    Embeddings, reranking, and classification models with up to 1400 embeddings/sec throughput.
  </Card>

  <Card title="Engine-Builder-LLM (Dense Models)" href="/engines/engine-builder-llm/overview" icon="microchip">
    Dense text generation models with [lookahead decoding](/engines/engine-builder-llm/lookahead-decoding), [structured outputs](/engines/performance-concepts/structured-outputs), and single node inference.
  </Card>

  <Card title="BIS-LLM (MoE & Advanced)" href="/engines/bis-llm/overview" icon="network">
    MoE models with [KV-aware routing](/engines/bis-llm/advanced-features#kv-aware-routing), [tool calling](/engines/performance-concepts/function-calling), and speculative decoding.
  </Card>

  <Card title="Specialized Deployments" href="#specialized-deployments" icon="server">
    Specialized engines for models like Whisper, Orpheus, or Flux, available as dedicated deployments rather than self-serviceable options.
  </Card>
</CardGroup>

## Engine selection

Select an engine based on your model's architecture and expected workload.

| Model type         | Architecture                  | Recommended engine | Key features                              | **Hardware**             |
| ------------------ | ----------------------------- | ------------------ | ----------------------------------------- | ------------------------ |
| **Dense LLM**      | CausalLM (text generation)    | Engine-Builder-LLM | Lookahead decoding, structured outputs    | H100, B200               |
| **MoE Models**     | Mixture of Experts            | BIS-LLM            | KV-aware routing, advanced quantization   | H100, B200               |
| **Large Models**   | 700B+ parameters              | BIS-LLM            | Distributed inference, `FP4` support      | H100, B200               |
| **Embeddings**     | BERT-based (bidirectional)    | BEI-Bert           | Cold-start optimization, 16-bit precision | T4, L4, A10G, H100, B200 |
| **Embeddings**     | Causal (Llama, Mistral, Qwen) | BEI                | `FP8` quantization, high throughput       | L4, A10G, H100, B200     |
| **Reranking**      | Cross-encoder architectures   | BEI / BEI-Bert     | Low latency, batch processing             | L4, A10G, H100, B200     |
| **Classification** | Sequence classification       | BEI / BEI-Bert     | High throughput, cached weights           | L4, A10G, H100, B200     |

### Feature availability

| Feature                              | BIS-LLM | Engine-Builder-LLM | BEI | BEI-Bert | Notes                                            |
| ------------------------------------ | ------- | ------------------ | --- | -------- | ------------------------------------------------ |
| **Quantization**                     | ✅       | ✅                  | ✅   | ❌        | BEI-Bert: `FP16`/`BF16` only                     |
| **KV quantization**                  | ✅       | ✅                  | ⚠️  | ⚠️       | `FP8_KV`, `FP4_KV` supported                     |
| **Speculative lookahead decoding**   | Gated   | ✅                  | ❌   | ❌        | n-gram based speculation                         |
| **Self-serviceable**                 | Gated/✅ | ✅                  | ✅   | ✅        | All engines self-service                         |
| **KV-routing**                       | Gated   | ❌                  | ❌   | ❌        | BIS-LLM only                                     |
| **Disaggregated serving**            | Gated   | ❌                  | ❌   | ❌        | BIS-LLM enterprise                               |
| **Tool calling & structured output** | ✅       | ✅                  | ❌   | ❌        | Function calling support                         |
| **Classification models**            | ❌       | ❌                  | ✅   | ✅        | Sequence classification                          |
| **Embedding models**                 | ❌       | ❌                  | ✅   | ✅        | Embedding generation                             |
| **Mixture-of-experts**               | ✅       | ⚠️ (Qwen3MoE only) | ❌   | ❌        | Mixture of Experts models like DeepSeek          |
| **MTP and Eagle 3 speculation**      | Gated   | ❌                  | ❌   | ❌        | Model-based speculation                          |
| **HTTP request cancellation**        | ✅       | ❌                  | ✅   | ✅        | Engine-Builder supports it within the first 10ms |
| **MultiModal Inputs**                | Gated   | ❌                  | ⚠️  | ❌        | Selected architectures only                      |

## Architecture recommendations

### BEI vs BEI-Bert (embeddings)

BEI-Bert optimizes BERT-based architectures (sentence-transformers, jinaai, nomic-ai) with fast cold-start performance and 16-bit precision. Choose BEI-Bert for bidirectional models under 4B parameters where cold-start latency matters. Jina-BERT, Nomic, and ModernBERT architectures all run well on this engine.

BEI handles causal embedding architectures (Llama, Mistral, Qwen) with `FP8`/`FP4` quantization support. Choose BEI when you need maximum throughput or want to run larger embedding models like BAAI/bge, Qwen3-Embedding, or Salesforce/SFR-Embedding with quantization.

### Engine-Builder-LLM vs BIS-LLM (text generation)

Engine-Builder-LLM serves dense models (non-MoE) with lookahead decoding and structured outputs. Choose it for Llama 3.3, Qwen-3, Qwen2.5, Mistral, or Gemma-3 when you need speculative decoding for coding agents or JSON schema validation.

BIS-LLM serves large MoE models with KV-aware routing and advanced tool calling. Choose it for DeepSeek-R1, Qwen3MoE, Kimi-K2, Llama-4, or GLM-4.7 when you need enterprise features like disaggregated serving or H100/B200 optimization.

## Performance benchmarks

Benchmark results depend on model size, GPU type, and quantization settings. The figures below represent typical performance on H100 GPUs.

### Embedding performance (BEI/BEI-Bert)

* **Throughput**: Up to 1400 client embeddings per second.
* **Latency**: Sub-millisecond response times.
* **Quantization**: `FP8`/`FP4` provides 2x speedup with less than 1% accuracy loss.

### Text generation performance (Engine-Builder-LLM/BIS-LLM)

* **Speculative decoding**: Faster inference for code and structured content through lookahead decoding.
* **Quantization**: Memory reduction and speed improvements with `FP8`/`FP4`.
* **Distributed inference**: Scalable deployment with tensor parallelism.

## Hardware requirements and optimization

*[Quantization](/engines/performance-concepts/quantization-guide)* reduces memory usage and improves inference speed.

| Quantization  | Minimum GPU | Recommended GPU | Memory reduction | Notes                                       |
| ------------- | ----------- | --------------- | ---------------- | ------------------------------------------- |
| `FP16`/`BF16` | A100        | H100            | None             | Baseline precision                          |
| `FP8`         | L4          | H100            | \~50%            | Good balance of performance and accuracy    |
| `FP8_KV`      | L4          | H100            | \~60%            | KV cache quantization for memory efficiency |
| `FP4`         | B200        | B200            | \~75%            | B200-only quantization                      |
| `FP4_KV`      | B200        | B200            | \~80%            | Maximum memory reduction                    |

<Note>
  Some models require specialized engines that are not self-serviceable:

  * **Whisper**: Audio transcription and speech recognition.
  * **Orpheus**: Audio generation.
</Note>

## Next steps

* [BEI documentation](/engines/bei/overview): Embeddings and classification.
* [Engine-Builder-LLM documentation](/engines/engine-builder-llm/overview): Dense text generation.
* [BIS-LLM documentation](/engines/bis-llm/overview): MoE and advanced features.

**Examples:**

* [BEI deployment guide](/examples/bei): Complete embedding model setup.
* [TensorRT-LLM examples](/examples/tensorrt-llm): Dense LLM deployment.
* [DeepSeek examples](/examples/models/deepseek/deepseek-r1): Large MoE deployment.


# Auto-Scaling Engines
Source: https://docs.baseten.co/engines/performance-concepts/autoscaling-engines

Performant auto-scaling custom tailored to Embedding and Generation Models on Baseten

# Auto-Scaling Engines

Beyond the [Introduction to autoscaling](/deployment/autoscaling), some adjustments specialized to models using dynamic batching are helpful.

Both BEI and Engine-Builder-LLM use **dynamic batching** to process parallel multiple requests. This increase in throughput comes at the cost of increased p50 latency.
Combining this feature with engine-specific autoscaling becomes a powerful tool for maintaining optimal performance across varying traffic patterns.

## BEI

BEI provides millisecond-range inference times and scales differently than other models. With too few replicas, backpressure can build up quickly.

**Key recommendations:**

* **Enable autoscaling** - BEI's millisecond-range inference and dynamic batching require autoscaling to handle variable traffic efficiently
* **Target utilization: 25%** - Low target provides headroom for traffic spikes and accommodates dynamic batching behavior
* **Concurrency: 96+ requests** - High concurrency allows maximum throughput. If unsure, start with 64 and 40% utilization and tune on live traffic.
* **Minimum concurrency: ≥8** - Never set below 8 for optimal performance

**Multi-payload routes** (`/rerank`, `/v1/embeddings`) can send multiple requests at once, challenging autoscaling based on concurrent requests. Use the [Performance client](/engines/performance-concepts/performance-client) for optimal scaling.

## Engine-Builder-LLM

Engine-Builder-LLM uses dynamic batching to maximize throughput, similar to BEI, but doesn't face the multi-payload challenge that BEI does with `/rerank` and `/v1/embeddings` routes.

**Key recommendations:**

* **Target utilization: 40-50%** - Lower than default to accommodate dynamic batching and provide headroom
* **Concurrency: 16-256 requests** - If unsure, start with 64 and 40% utilization and tune on live traffic.
* **Batch cases** - Use the Performance client for batch processing
* **Minimum concurrency: ≥8** - Never set below 8 for optimal performance
* **Lookahead works slightly better with lower batch-size** - Tune the concurrency to a same or slightly below `max_batch_size`, so that lookahead is aware that it can perform optimizations. This is partially also helpful for any `engine-builder-llm` engine, even if you're not using lookahead.

**Important**: Do not set concurrency above `max_batch_size` as it leads to on-replica queueing and negates the benefits of autoscaling.

General advice:
Tune the equilibrium on your live-traffic, cost, thoughput and latency targets. Your mean expected concurrency will be the concurrency\_target \* target\_utilization. Most engines are only provide marginal thoughput improvements when paired with 128 requests vs working on 256 requests at a time. Keeping a mean expected concurrency around 16-64 will allow for the best stability guarantees and proactive scaling descisions under variable traffic.

## Quick Reference

| **Setting**        | **BEI**      | **Engine-Builder-LLM** |
| ------------------ | ------------ | ---------------------- |
| Target utilization | 25%          | 40-50%                 |
| Concurrency        | 96+ (min ≥8) | 32-256                 |
| Batch size         | Flexible     | Flexible               |

## Further reading

* [BEI overview](/engines/bei/overview) - General BEI documentation
* [BEI reference config](/engines/bei/bei-reference) - Complete configuration options
* [Engine-Builder-LLM overview](/engines/engine-builder-llm/overview) - Generation model details
* [Embedding examples](/examples/bei) - Concrete deployment examples
* [Performance client documentation](/engines/performance-concepts/performance-client) - Client usage with embeddings
* [Quantization guide](/engines/performance-concepts/quantization-guide) - Hardware considerations
* [Performance optimization](/development/model/performance-optimization) - General performance guidance


# Deploy training and S3 checkpoints
Source: https://docs.baseten.co/engines/performance-concepts/deployment-from-training-and-s3

Deploy training checkpoints and cloud storage models with TensorRT-LLM optimization.

Deploy training checkpoints and cloud storage models with Engine-Builder-LLM, BEI, or BIS-LLM.

## Training checkpoint deployment

Deploy fine-tuned models from Baseten Training with Engine-Builder-LLM. Specify `BASETEN_TRAINING` as the source:

```yaml config.yaml theme={"system"}
model_name: My Fine-Tuned LLM
resources:
  accelerator: H100:1
  use_gpu: true
secrets:
  hf_access_token: null # do not set value here
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: BASETEN_TRAINING
      repo: YOUR_TRAINING_JOB_ID
      revision: checkpoint-100
```

**Key fields:**

* `base_model`: `decoder` for LLMs, `encoder`/`encoder_bert` for embeddings
* `source`: `BASETEN_TRAINING` for Baseten Training checkpoints
* `repo`: Your training job ID
* `revision`: Checkpoint folder name (e.g., `checkpoint-100`, `checkpoint-final`)

Find your checkpoint details with:

```sh theme={"system"}
truss train get_checkpoint_urls --job-id=YOUR_TRAINING_JOB_ID
```

### Encoder model requirements

To deploy a fine-tuned encoder model (embeddings, rerankers) from training checkpoints, use `encoder` or `encoder_bert` as the base model:

```yaml config.yaml theme={"system"}
model_name: My Fine-Tuned Embeddings
resources:
  accelerator: L4:1
  use_gpu: true
trt_llm:
  build:
    base_model: encoder_bert
    checkpoint_repository:
      source: BASETEN_TRAINING
      repo: YOUR_TRAINING_JOB_ID
      revision: checkpoint-final
  runtime:
    webserver_default_route: /v1/embeddings
```

Use `encoder_bert` for BERT-based models (sentence-transformers, classification, reranking). Use `encoder` for causal embedding models.

Encoder models have specific requirements:

* **No tensor parallelism**: Omit `tensor_parallel_count` or set it to `1`.
* **Fast tokenizer required**: Your checkpoint must include a `tokenizer.json` file. Models using only the legacy `vocab.txt` format are not supported.
* **Embedding model files**: For sentence-transformer models, include `modules.json` and `1_Pooling/config.json` in your checkpoint.

The `webserver_default_route` configures the inference endpoint. Options include `/v1/embeddings` for embeddings, `/rerank` for rerankers, and `/predict` for classification.

## Cloud storage deployment

Deploy models directly from S3, GCS, or Azure. Specify the storage source and bucket path:

```yaml config.yaml theme={"system"}
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: S3  # or GCS, AZURE, HF
      repo: s3://your-bucket/path/to/model/
```

**Storage sources:**

* `S3`: Amazon S3 buckets
* `GCS`: Google Cloud Storage
* `AZURE`: Azure Blob Storage
* `HF`: Hugging Face repositories

### Private storage setup

All runtimes use the same downloader system as [model\_cache](/development/model/model-cache). As a result, you configure the `runtime_secret_name` and `repo` identically across model\_cache and runtimes like Engine-Builder-LLM or BEI.

**Secret Setup:**

Add these JSON secrets to your [Baseten secrets manager](https://app.baseten.co/settings/secrets).
For more details, refer to the documentation in [model\_cache](/development/model/model-cache).

**S3:**

```json theme={"system"}
{
  "access_key_id": "XXXXX",
  "secret_access_key": "xxxxx/xxxxxx",
  "region": "us-west-2"
}
```

**GCS:**

```json theme={"system"}
{
  "private_key_id": "xxxxxxx",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMI",
  "client_email": "b10-some@xxx-example.iam.gserviceaccount.com"
}
```

**Azure:**

```json theme={"system"}
{
  "account_key": "xxxxx"
}
```

Reference the secret in your config:

```yaml theme={"system"}
secrets:
  aws_secret_json: "set token in baseten workspace"
trt_llm:
  build:
    checkpoint_repository:
      source: S3
      repo: s3://your-private-bucket/model
      runtime_secret_name: aws_secret_json
```

**For Baseten Training deployments:** These secrets are automatically mounted and available to your deployment.

## Further reading

* [Engine-Builder-LLM configuration](/engines/engine-builder-llm/engine-builder-config): Complete build and runtime options for LLMs.
* [BEI reference configuration](/engines/bei/bei-reference): Complete configuration for encoder models.
* [Model cache documentation](/development/model/model-cache): Caching strategies used by the engines.
* [Secrets management](/development/model/secrets): Configure credentials for private storage.


# Function calling
Source: https://docs.baseten.co/engines/performance-concepts/function-calling

Tool selection and structured function calls with LLMs

<Note>
  Function calling is supported by Baseten engines including [BIS-LLM](/engines/bis-llm/overview) and [Engine-Builder-LLM](/engines/engine-builder-llm/overview), as well as [Model APIs](/development/model-apis/overview) for instant access. It's also compatible with other inference frameworks like [vLLM](/examples/vllm) and [SGLang](/examples/sglang).
</Note>

## Overview

*Function calling* (also known as *tool calling*) lets a model **choose a tool and produce arguments** based on a user request.

**Important:** the model **does not execute** your Python function. Your application must:

1. run the tool, and
2. optionally send the tool’s output back to the model to produce a final, user-facing response.

This is a great fit for [chains](/development/chain/overview) and other orchestrators.

***

## How tool calling works

A typical tool-calling loop looks like:

1. **Send** the user message and a list of tools.
2. The model returns either normal text or one or more **tool calls** (name and JSON arguments).
3. **Execute** the tool calls in your application.
4. **Send tool output** back to the model.
5. Receive a **final response** or additional tool calls.

***

## 1. Define tools

Tools can be anything: API calls, database queries, internal scripts, etc.

Docstrings matter. Models use them to decide which tool to call and how to fill parameters:

```python theme={"system"}
def multiply(a: float, b: float):
    """Multiply two numbers.

    Args:
        a: The first number.
        b: The second number.
    """
    return a * b


def divide(a: float, b: float):
    """Divide two numbers.

    Args:
        a: The dividend.
        b: The divisor (must be non-zero).
    """
    return a / b


def add(a: float, b: float):
    """Add two numbers.

    Args:
        a: The first number.
        b: The second number.
    """
    return a + b


def subtract(a: float, b: float):
    """Subtract two numbers.

    Args:
        a: The number to subtract from.
        b: The number to subtract.
    """
    return a - b
```

### Tool-writing tips

Design small, single-purpose tools and document constraints in docstrings (units, allowed values, required fields). Treat model-provided arguments as untrusted input and validate before execution.

***

## 2. Serialize functions

Convert functions into JSON-schema tool definitions (OpenAI-compatible format):

```python theme={"system"}
from transformers.utils import get_json_schema

calculator_functions = {
    "multiply": multiply,
    "divide": divide,
    "add": add,
    "subtract": subtract,
}

tools = [get_json_schema(f) for f in calculator_functions.values()]
```

***

## 3. Call the model

Include the `tools` array in your request:

```python theme={"system"}
import requests

payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is 3.14 + 3.14?"},
    ],
    "tools": tools,
    "tool_choice": "auto",  # default
}

MODEL_ID = ""
BASETEN_API_KEY = ""

resp = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=payload,
)
```

***

## 4. Control tool selection

Set `tool_choice` to control how the model uses tools. With `auto` (default), the model may respond with text or tool calls. With `required`, the model must return at least one tool call. With `none`, the model returns plain text only. To force a specific tool:

```python theme={"system"}
"tool_choice": {"type": "function", "function": {"name": "subtract"}}
```

***

## 5. Parse and execute tool calls

Depending on the engine and model, tool calls are typically returned in an assistant message under `tool_calls`:

```python theme={"system"}
import json

data = resp.json()
message = data["choices"][0]["message"]

tool_calls = message.get("tool_calls") or []

for tool_call in tool_calls:
    name = tool_call["function"]["name"]
    args = json.loads(tool_call["function"]["arguments"])

    # Validate args in production.
    result = calculator_functions[name](**args)
    print(result)
```

### Full loop: send tool output back for a final answer

If you want the model to turn raw tool output into a user-facing response, append the assistant message and a tool response with the matching `tool_call_id`:

```python theme={"system"}
# Continue the conversation
messages = payload["messages"]
messages.append(message)  # assistant tool call message

# Example: respond to the first tool call
tool_call = tool_calls[0]
name = tool_call["function"]["name"]
args = json.loads(tool_call["function"]["arguments"])
result = calculator_functions[name](**args)

messages.append({
    "role": "tool",
    "tool_call_id": tool_call["id"],
    "content": json.dumps({"result": result}),
})

final_payload = {
    **payload,
    "messages": messages,
}

final_resp = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=final_payload,
)

print(final_resp.json()["choices"][0]["message"].get("content"))
```

***

## Practical tips

Use low temperature (0.0–0.3) for reliable tool selection and argument values. Add `enum` and `required` constraints in your JSON schema to guide model outputs. Consider parallel tool calls only if your model supports them. Always validate and sanitize inputs before calling real systems.

***

## Further reading

* [Chains](/development/chain/overview): Orchestrate multi-step workflows.
* [Custom engine builder](/engines/engine-builder-llm/custom-engine-builder): Advanced configuration options.


# Performance client
Source: https://docs.baseten.co/engines/performance-concepts/performance-client

High-performance client library for embeddings, reranking, classification, and generic batch requests

<Card title="View on GitHub" icon="github" href="https://github.com/basetenlabs/truss/tree/main/baseten-performance-client" />

Built in Rust and integrated with Python, Node.js, and native Rust, the *Performance Client* handles concurrent POST requests efficiently. It releases the Python GIL while executing requests, enabling simultaneous sync and async usage.

[Benchmarks](https://www.baseten.co/blog/your-client-code-matters-10x-higher-embedding-throughput-with-python-and-rust/) show the Performance Client reaches 1200+ requests per second per client.

Use it with **Baseten deployments** or **third-party providers** like OpenAI.

<img alt="benchmarks" />

***

## Install the client

<Tabs>
  <Tab title="Python">
    To install the Performance Client for Python, use pip:

    ```bash theme={"system"}
    pip install baseten_performance_client>=0.1.0
    ```
  </Tab>

  <Tab title="JavaScript">
    To install the Performance Client for JavaScript, use npm:

    ```bash theme={"system"}
    npm install baseten-performance-client
    ```
  </Tab>
</Tabs>

***

## Get started

<Tabs>
  <Tab title="Python">
    To initialize the Performance Client in Python, import the class and provide your base URL and API key:

    ```python theme={"system"}
    from baseten_performance_client import PerformanceClient

    client = PerformanceClient(
        base_url="https://model-YOUR_MODEL_ID.api.baseten.co/environments/production/sync",
        api_key="YOUR_API_KEY"
    )
    ```
  </Tab>

  <Tab title="JavaScript">
    To initialize the Performance Client with JavaScript, require the package and create a new instance:

    ```javascript theme={"system"}
    const { PerformanceClient } = require("baseten-performance-client");

    const client = new PerformanceClient(
      "https://model-YOUR_MODEL_ID.api.baseten.co/environments/production/sync",
      process.env.BASETEN_API_KEY
    );
    ```
  </Tab>
</Tabs>

The client also works with third-party providers like OpenAI by replacing the `base_url`.

### Advanced setup

Configure HTTP version selection and *connection pooling* for optimal performance.

<Tabs>
  <Tab title="Python">
    To configure HTTP version and connection pooling in Python, use the `http_version` parameter and `HttpClientWrapper`:

    ```python theme={"system"}
    from baseten_performance_client import PerformanceClient, HttpClientWrapper

    # HTTP/1.1 (default, better for high concurrency)
    client_http1 = PerformanceClient(BASE_URL, API_KEY, http_version=1)

    # HTTP/2 (not recommended on Baseten)
    client_http2 = PerformanceClient(BASE_URL, API_KEY, http_version=2)

    # Connection pooling for multiple clients
    wrapper = HttpClientWrapper(http_version=1)
    client1 = PerformanceClient(base_url="https://api1.example.com", client_wrapper=wrapper)
    client2 = PerformanceClient(base_url="https://api2.example.com", client_wrapper=wrapper)
    ```
  </Tab>

  <Tab title="JavaScript">
    To configure HTTP version and connection pooling with JavaScript, pass the version as the third argument and use `HttpClientWrapper`:

    ```javascript theme={"system"}
    const { PerformanceClient, HttpClientWrapper } = require('baseten-performance-client');

    // HTTP/1.1 (default, better for high concurrency)
    const clientHttp1 = new PerformanceClient(BASE_URL, API_KEY, 1);

    // HTTP/2
    const clientHttp2 = new PerformanceClient(BASE_URL, API_KEY, 2);

    // Connection pooling for multiple clients
    const wrapper = new HttpClientWrapper(1);
    const pooledClient1 = new PerformanceClient(BASE_URL_1, API_KEY, 1, wrapper);
    const pooledClient2 = new PerformanceClient(BASE_URL_2, API_KEY, 1, wrapper);
    ```
  </Tab>
</Tabs>

***

## Core features

### Embeddings

The client provides efficient embedding requests with configurable *batching*, concurrency, and latency optimizations. Compatible with [BEI](/engines/bei/overview).

<Tabs>
  <Tab title="Python">
    To generate embeddings with Python, configure a `RequestProcessingPreference` and call `client.embed()`:

    ```python theme={"system"}
    from baseten_performance_client import PerformanceClient, RequestProcessingPreference

    client = PerformanceClient(base_url=BASE_URL, api_key=API_KEY)
    texts = ["Hello world", "Example text", "Another sample"] * 10

    preference = RequestProcessingPreference(
        batch_size=16,
        max_concurrent_requests=256,
        max_chars_per_request=10000,
        hedge_delay=0.5,
        timeout_s=360,
        total_timeout_s=600,
        extra_headers={"x-custom-header": "value"}
    )

    response = client.embed(
        input=texts,
        model="my_model",
        preference=preference
    )

    print(f"Model used: {response.model}")
    print(f"Total tokens used: {response.usage.total_tokens}")
    print(f"Total time: {response.total_time:.4f}s")

    # Convert to numpy array (requires numpy)
    numpy_array = response.numpy()
    print(f"Embeddings shape: {numpy_array.shape}")
    ```

    For async usage, call `await client.async_embed(input=texts, model="my_model", preference=preference)`.
  </Tab>

  <Tab title="JavaScript">
    To generate embeddings with JavaScript, configure a `RequestProcessingPreference` and call `client.embed()`:

    ```javascript theme={"system"}
    const { PerformanceClient, RequestProcessingPreference } = require('baseten-performance-client');

    const client = new PerformanceClient(BASE_URL, API_KEY);
    const texts = ["Hello world", "Example text", "Another sample"];

    const preference = new RequestProcessingPreference(
        32,        // maxConcurrentRequests
        4,         // batchSize
        10000,     // maxCharsPerRequest
        360.0,     // timeoutS
        0.5        // hedgeDelay
    );

    const response = await client.embed(
        texts,                      // input
        "my_model",                 // model
        null,                       // encodingFormat
        null,                       // dimensions
        null,                       // user
        preference                  // preference parameter
    );

    console.log(`Model used: ${response.model}`);
    console.log(`Total tokens used: ${response.usage.total_tokens}`);
    console.log(`Total time: ${response.total_time.toFixed(4)}s`);
    ```
  </Tab>
</Tabs>

### Generic batch POST

Send HTTP requests to any URL with any JSON payload. Compatible with [Engine-Builder-LLM](/engines/engine-builder-llm/overview) and other models. Set `stream=False` for SSE endpoints.

<Tabs>
  <Tab title="Python">
    To send batch POST requests with Python, define your payloads and call `client.batch_post()`:

    ```python theme={"system"}
    from baseten_performance_client import PerformanceClient, RequestProcessingPreference

    client = PerformanceClient(base_url=BASE_URL, api_key=API_KEY)

    payloads = [
        {"model": "my_model", "prompt": "Batch request 1", "stream": False},
        {"model": "my_model", "prompt": "Batch request 2", "stream": False}
    ] * 10

    preference = RequestProcessingPreference(
        max_concurrent_requests=96,
        timeout_s=720,
        hedge_delay=0.5,
        extra_headers={"x-custom-header": "value"}
    )

    response = client.batch_post(
        url_path="/v1/completions",
        payloads=payloads,
        preference=preference,
        method="POST"
    )

    print(f"Total time: {response.total_time:.4f}s")
    ```

    Supported methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.

    For async usage, call `await client.async_batch_post(url_path, payloads, preference, method)`.
  </Tab>

  <Tab title="JavaScript">
    To send batch POST requests with JavaScript, define your payloads and call `client.batchPost()`:

    ```javascript theme={"system"}
    const { PerformanceClient, RequestProcessingPreference } = require('baseten-performance-client');

    const client = new PerformanceClient(BASE_URL, API_KEY);

    const payloads = [
      { model: "my_model", prompt: "Batch request 1", stream: false },
      { model: "my_model", prompt: "Batch request 2", stream: false }
    ];

    const preference = new RequestProcessingPreference(
        32,        // maxConcurrentRequests
        undefined, // batchSize
        undefined, // maxCharsPerRequest
        360.0,     // timeoutS
        0.5        // hedgeDelay
    );

    const response = await client.batchPost(
      "/v1/completions",
      payloads,
      preference,
      "POST"
    );

    console.log(`Total time: ${response.total_time.toFixed(4)}s`);
    ```
  </Tab>
</Tabs>

### Reranking

Rerank documents by relevance to a query. Compatible with [BEI](/engines/bei/overview), [BEI-Bert](/engines/bei/overview), and text-embeddings-inference reranking endpoints.

<Tabs>
  <Tab title="Python">
    To rerank documents with Python, provide a query and list of documents to `client.rerank()`:

    ```python theme={"system"}
    from baseten_performance_client import PerformanceClient, RequestProcessingPreference

    client = PerformanceClient(base_url=BASE_URL, api_key=API_KEY)

    query = "What is the best framework?"
    documents = ["Doc 1 text", "Doc 2 text", "Doc 3 text"]

    preference = RequestProcessingPreference(
        batch_size=16,
        max_concurrent_requests=32,
        timeout_s=360,
        max_chars_per_request=256000,
        hedge_delay=0.5,
        extra_headers={"x-rerank-header": "value"}
    )

    response = client.rerank(
        query=query,
        texts=documents,
        model="rerank-model",
        return_text=True,
        preference=preference
    )

    for res in response.data:
        print(f"Index: {res.index} Score: {res.score}")
    ```

    For async usage, call `await client.async_rerank(query, texts, model, return_text, preference)`.
  </Tab>

  <Tab title="JavaScript">
    To rerank documents with JavaScript, provide a query and list of documents to `client.rerank()`:

    ```javascript theme={"system"}
    const { PerformanceClient, RequestProcessingPreference } = require('baseten-performance-client');

    const client = new PerformanceClient(BASE_URL, API_KEY);

    const query = "What is the best framework?";
    const documents = ["Doc 1 text", "Doc 2 text", "Doc 3 text"];

    const preference = new RequestProcessingPreference(
        32,        // maxConcurrentRequests
        16,        // batchSize
        undefined, // maxCharsPerRequest
        360.0,     // timeoutS
        0.5        // hedgeDelay
    );

    const response = await client.rerank(query, documents, "rerank-model", true, preference);

    response.data.forEach(res => console.log(`Index: ${res.index} Score: ${res.score}`));
    ```
  </Tab>
</Tabs>

### Classification

Classify text inputs into categories. Compatible with [BEI](/engines/bei/overview) and text-embeddings-inference classification endpoints.

<Tabs>
  <Tab title="Python">
    To classify text with Python, provide a list of inputs to `client.classify()`:

    ```python theme={"system"}
    from baseten_performance_client import PerformanceClient, RequestProcessingPreference

    client = PerformanceClient(base_url=BASE_URL, api_key=API_KEY)

    texts_to_classify = [
        "This is great!",
        "I did not like it.",
        "Neutral experience."
    ]

    preference = RequestProcessingPreference(
        batch_size=16,
        max_concurrent_requests=32,
        timeout_s=360.0,
        max_chars_per_request=256000,
        hedge_delay=0.5,
        extra_headers={"x-classify-header": "value"}
    )

    response = client.classify(
        inputs=texts_to_classify,
        model="classification-model",
        preference=preference
    )

    for group in response.data:
        for result in group:
            print(f"Label: {result.label}, Score: {result.score}")
    ```

    For async usage, call `await client.async_classify(inputs, model, preference)`.
  </Tab>

  <Tab title="JavaScript">
    To classify text with JavaScript, provide a list of inputs to `client.classify()`:

    ```javascript theme={"system"}
    const { PerformanceClient, RequestProcessingPreference } = require('baseten-performance-client');

    const client = new PerformanceClient(BASE_URL, API_KEY);

    const texts = ["This is great!", "I did not like it.", "Neutral experience."];

    const preference = new RequestProcessingPreference(32, 16, undefined, 360.0, 0.5);
    const response = await client.classify(texts, "classification-model", preference);

    response.data.forEach(group => {
        group.forEach(result => console.log(`Label: ${result.label}, Score: ${result.score}`));
    });
    ```
  </Tab>
</Tabs>

***

## Advanced features

### Configure RequestProcessingPreference

The `RequestProcessingPreference` class provides unified configuration for all request processing parameters.

<Tabs>
  <Tab title="Python">
    To configure request processing in Python, create a `RequestProcessingPreference` instance:

    ```python theme={"system"}
    from baseten_performance_client import RequestProcessingPreference

    preference = RequestProcessingPreference(
        max_concurrent_requests=64,
        batch_size=32,
        timeout_s=30.0,
        hedge_delay=0.5,
        hedge_budget_pct=0.15,
        retry_budget_pct=0.08,
        total_timeout_s=300.0
    )
    ```
  </Tab>

  <Tab title="JavaScript">
    To configure request processing with JavaScript, create a `RequestProcessingPreference` instance:

    ```javascript theme={"system"}
    const { RequestProcessingPreference } = require('baseten-performance-client');

    const preference = new RequestProcessingPreference(
        64,        // maxConcurrentRequests
        32,        // batchSize
        undefined, // maxCharsPerRequest
        30.0,      // timeoutS
        0.5,       // hedgeDelay
        undefined, // totalTimeoutS
        0.15,      // hedgeBudgetPct
        0.08       // retryBudgetPct
    );
    ```
  </Tab>
</Tabs>

#### Parameter reference

| Parameter                 | Type  | Default | Range       | Description                                 |
| ------------------------- | ----- | ------- | ----------- | ------------------------------------------- |
| `max_concurrent_requests` | int   | 128     | 1-1024      | Maximum parallel requests                   |
| `batch_size`              | int   | 128     | 1-1024      | Items per batch                             |
| `timeout_s`               | float | 3600.0  | 1.0-7200.0  | Per-request timeout in seconds              |
| `hedge_delay`             | float | None    | 0.2-30.0    | *Hedge delay* in seconds (see below)        |
| `hedge_budget_pct`        | float | 0.10    | 0.0-3.0     | Percentage of requests allowed for hedging  |
| `retry_budget_pct`        | float | 0.05    | 0.0-3.0     | Percentage of requests allowed for retries  |
| `total_timeout_s`         | float | None    | ≥timeout\_s | Total operation timeout                     |
| `extra_headers`           | dict  | None    | -           | Custom headers to include with all requests |

*Hedge delay* sends duplicate requests after a specified delay to reduce p99 latency. After the delay, the request is cloned and raced against the original. The 429 and 5xx errors are always retried automatically.

### Select HTTP version

Choose between HTTP/1.1 and HTTP/2 for optimal performance. HTTP/1.1 is recommended for high concurrency workloads.

<Tabs>
  <Tab title="Python">
    To select the HTTP version in Python, use the `http_version` parameter:

    ```python theme={"system"}
    from baseten_performance_client import PerformanceClient

    # HTTP/1.1 (default, better for high concurrency)
    client_http1 = PerformanceClient(BASE_URL, API_KEY, http_version=1)

    # HTTP/2 (better for single requests)
    client_http2 = PerformanceClient(BASE_URL, API_KEY, http_version=2)
    ```
  </Tab>

  <Tab title="JavaScript">
    To select the HTTP version with JavaScript, pass the version as the third argument:

    ```javascript theme={"system"}
    const { PerformanceClient } = require('baseten-performance-client');

    // HTTP/1.1 (default, better for high concurrency)
    const clientHttp1 = new PerformanceClient(BASE_URL, API_KEY, 1);

    // HTTP/2 (better for single requests)
    const clientHttp2 = new PerformanceClient(BASE_URL, API_KEY, 2);
    ```
  </Tab>
</Tabs>

### Share connection pools

Share connection pools across multiple client instances to reduce overhead when connecting to multiple endpoints.

<Tabs>
  <Tab title="Python">
    To share a connection pool in Python, create an `HttpClientWrapper` and pass it to each client:

    ```python theme={"system"}
    from baseten_performance_client import PerformanceClient, HttpClientWrapper

    wrapper = HttpClientWrapper(http_version=1)

    client1 = PerformanceClient(base_url="https://api1.example.com", client_wrapper=wrapper)
    client2 = PerformanceClient(base_url="https://api2.example.com", client_wrapper=wrapper)
    ```
  </Tab>

  <Tab title="JavaScript">
    To share a connection pool with JavaScript, create an `HttpClientWrapper` and pass it to each client:

    ```javascript theme={"system"}
    const { PerformanceClient, HttpClientWrapper } = require('baseten-performance-client');

    const wrapper = new HttpClientWrapper(1);

    const client1 = new PerformanceClient(BASE_URL_1, API_KEY, 1, wrapper);
    const client2 = new PerformanceClient(BASE_URL_2, API_KEY, 1, wrapper);
    ```
  </Tab>
</Tabs>

### Cancel operations

Cancel long-running operations using `CancellationToken`. The token provides immediate cancellation, resource cleanup, Ctrl+C support, token sharing across operations, and status checking with `is_cancelled()`.

<Tabs>
  <Tab title="Python">
    To cancel operations in Python, create a `CancellationToken` and pass it to your preference:

    ```python theme={"system"}
    from baseten_performance_client import (
        PerformanceClient,
        CancellationToken,
        RequestProcessingPreference
    )
    import threading
    import time

    client = PerformanceClient(base_url=BASE_URL, api_key=API_KEY)

    cancel_token = CancellationToken()
    preference = RequestProcessingPreference(
        max_concurrent_requests=32,
        batch_size=16,
        timeout_s=360.0,
        cancel_token=cancel_token
    )

    def long_operation():
        try:
            response = client.embed(
                input=["large batch"] * 1000,
                model="embedding-model",
                preference=preference
            )
            print("Operation completed")
        except ValueError as e:
            if "cancelled" in str(e):
                print("Operation was cancelled")

    threading.Thread(target=long_operation).start()
    time.sleep(2)
    cancel_token.cancel()
    ```
  </Tab>

  <Tab title="JavaScript">
    To cancel operations with JavaScript, create a `CancellationToken` and pass it to your preference:

    ```javascript theme={"system"}
    const { PerformanceClient, CancellationToken, RequestProcessingPreference } = require('baseten-performance-client');

    const client = new PerformanceClient(BASE_URL, API_KEY);

    const cancelToken = new CancellationToken();
    const preference = new RequestProcessingPreference(
        32, 16, undefined, 360.0, undefined, undefined,
        undefined, undefined, undefined, undefined, cancelToken
    );

    const operation = client.embed(
        ["large batch"].concat(Array(1000).fill("sample")),
        "model",
        undefined,
        undefined,
        undefined,
        preference
    );

    setTimeout(() => cancelToken.cancel(), 2000);

    try {
        const response = await operation;
        console.log("Operation completed");
    } catch (error) {
        if (error.message.includes("cancelled")) {
            console.log("Operation was cancelled");
        }
    }
    ```
  </Tab>
</Tabs>

***

## Handle errors

The client raises standard exceptions for error conditions:

* **`HTTPError`**: Authentication failures (403), server errors (5xx), endpoint not found (404).
* **`Timeout`**: Request or total operation timeout based on `timeout_s` or `total_timeout_s`.
* **`ValueError`**: Invalid input parameters (empty input list, invalid batch size, inconsistent embedding dimensions).

<Tabs>
  <Tab title="Python">
    To handle errors in Python, catch the appropriate exception types:

    ```python theme={"system"}
    import requests
    from baseten_performance_client import PerformanceClient, RequestProcessingPreference

    client = PerformanceClient(base_url=BASE_URL, api_key=API_KEY)
    preference = RequestProcessingPreference(timeout_s=30.0)

    try:
        response = client.embed(input=["text"], model="model", preference=preference)
        print(f"Model used: {response.model}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}, status code: {e.response.status_code}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout error: {e}")
    except ValueError as e:
        print(f"Input error: {e}")
    ```
  </Tab>

  <Tab title="JavaScript">
    To handle errors with JavaScript, use a try-catch block and inspect the error object:

    ```javascript theme={"system"}
    const { PerformanceClient, RequestProcessingPreference } = require('baseten-performance-client');

    const client = new PerformanceClient(BASE_URL, API_KEY);
    const preference = new RequestProcessingPreference(32, 16, undefined, 30.0);

    try {
        const response = await client.embed(texts, "model", undefined, undefined, undefined, preference);
        console.log("Success:", response.model);
    } catch (error) {
        if (error.response) {
            console.log(`HTTP error: ${error.response.status}`);
        } else if (error.code === 'TIMEOUT') {
            console.log("Timeout error");
        } else {
            console.log(`Error: ${error.message}`);
        }
    }
    ```
  </Tab>
</Tabs>

***

## Configure the client

### Environment variables

* **`BASETEN_API_KEY`**: Your Baseten API key. Also checks `OPENAI_API_KEY` as fallback.
* **`PERFORMANCE_CLIENT_LOG_LEVEL`**: Logging level. Overrides `RUST_LOG`. Valid values: `trace`, `debug`, `info`, `warn`, `error`. Default: `warn`.
* **`PERFORMANCE_CLIENT_REQUEST_ID_PREFIX`**: Custom prefix for request IDs. Default: `perfclient`.

### Configure logging

To set the logging level, use the `PERFORMANCE_CLIENT_LOG_LEVEL` environment variable:

```bash theme={"system"}
PERFORMANCE_CLIENT_LOG_LEVEL=info python script.py
PERFORMANCE_CLIENT_LOG_LEVEL=debug cargo run
```

The `PERFORMANCE_CLIENT_LOG_LEVEL` variable takes precedence over `RUST_LOG`.

***

## Use with Rust

The Performance Client is also available as a native Rust library.

To use the Performance Client in Rust, add the dependencies and create a `PerformanceClientCore` instance:

```rust theme={"system"}
use baseten_performance_client_core::{PerformanceClientCore, ClientError};
use tokio;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("BASETEN_API_KEY").expect("BASETEN_API_KEY not set");
    let base_url = "https://model-YOUR_MODEL_ID.api.baseten.co/environments/production/sync";

    let client = PerformanceClientCore::new(base_url, Some(api_key), None, None);

    // Generate embeddings
    let texts = vec!["Hello world".to_string(), "Example text".to_string()];
    let embedding_response = client.embed(
        texts,
        "my_model".to_string(),
        Some(16),
        Some(32),
        Some(360.0),
        Some(256000),
        Some(0.5),
        Some(360.0),
    ).await?;

    println!("Model: {}", embedding_response.model);
    println!("Total tokens: {}", embedding_response.usage.total_tokens);

    // Send batch POST requests
    let payloads = vec![
        serde_json::json!({"model": "my_model", "input": ["Rust sample 1"]}),
        serde_json::json!({"model": "my_model", "input": ["Rust sample 2"]}),
    ];

    let batch_response = client.batch_post(
        "/v1/embeddings".to_string(),
        payloads,
        Some(32),
        Some(360.0),
        Some(0.5),
        Some(360.0),
        None,
    ).await?;

    println!("Batch POST total time: {:.4}s", batch_response.total_time);

    Ok(())
}
```

Add these dependencies to your `Cargo.toml`:

```toml theme={"system"}
[dependencies]
baseten_performance_client_core = "0.1.4"
tokio = { version = "1.0", features = ["full"] }
serde_json = "1.0"
```

***

## Further reading

* [GitHub: baseten-performance-client](https://github.com/basetenlabs/truss/tree/main/baseten-performance-client): Complete source code and additional examples.
* [Performance benchmarks blog](https://www.baseten.co/blog/your-client-code-matters-10x-higher-embedding-throughput-with-python-and-rust/): Detailed performance analysis and comparisons.


# Quantization guide
Source: https://docs.baseten.co/engines/performance-concepts/quantization-guide

FP8 and FP4 trade-offs and hardware requirements for all engines

*Quantization* trades precision for speed and memory efficiency. This guide covers Baseten's supported formats, hardware requirements, and model-specific recommendations.

## Quantization options

Quantization type availability depends on the engine and GPU.

### Engine support

| **Quantization** | [**BIS-LLM**](/engines/bis-llm/overview) | [**Engine-Builder-LLM**](/engines/engine-builder-llm/overview) | [**BEI**](/engines/bei/overview) |
| ---------------- | ---------------------------------------- | -------------------------------------------------------------- | -------------------------------- |
| `FP8`            | ✅                                        | ✅                                                              | ✅                                |
| `FP8_KV`         | ✅                                        | ✅                                                              | ⚠️                               |
| `FP4`            | ✅                                        | ✅                                                              | ⚠️                               |
| `FP4_KV`         | ✅                                        | ✅                                                              | ⚠️                               |
| `FP4_MLP_ONLY`   | ✅                                        | ✅                                                              | ✅                                |

### GPU support

| **GPU type** | `FP8` | `FP8_KV` | `FP4` | `FP4_KV` | `FP4_MLP_ONLY` |
| ------------ | ----- | -------- | ----- | -------- | -------------- |
| **L4**       | ✅     | ✅        | ❌     | ❌        | ❌              |
| **H100**     | ✅     | ✅        | ❌     | ❌        | ❌              |
| **H200**     | ✅     | ✅        | ❌     | ❌        | ❌              |
| **B200**     | ✅     | ✅        | ✅     | ✅        | ✅              |

## Model recommendations

Some model families have specific quantization requirements that affect accuracy.

### Qwen2 models

Qwen2 retains QKV projection bias (attention bias), while Qwen3, Llama3, Llama2, and most other models remove it. This makes Qwen2 sensitive to symmetric KV cache quantization, so `FP8_KV` causes quality degradation. Use regular `FP8` instead and increase calibration size to 1024 or greater for better accuracy.

### Llama models

Llama variants work well with `FP8_KV` and standard calibration sizes (1024-1536). For B200 deployments, use `FP4_MLP_ONLY` for the best balance of speed and quality.

### BEI models (embeddings)

Use `FP8` for embedding models for causal models. Skip quantization for smaller models since the overhead isn't worth the minimal benefit and Bert is not supported. BEI doesn't support `FP8_KV`.

## Calibration

Quantization requires calibration data to determine optimal scaling factors. Larger models generally need more calibration samples.

### Calibration datasets

The default dataset is `cnn_dailymail` (general news text). For specialized models, or fine-tunes specific to a chat template, use domain-specific datasets when available.
For using a custom dataset, reference the huggingface name under `calib_dataset`, and make sure the dataset has a `train` split with a `text`/`messages` column.

When using the `messages` column, we require the tokenizer of your model to have a `apply_chat_template()` function on which we can apply `apply_chat_template(row["messages"]) for row in rows`.
If you want to use a dataset without preprocessing, you can provide a `text` column.

For chat-based calibration with thinking , we open-sourced [`baseten/quant_calibration_dataset_v1`](https://huggingface.co/datasets/baseten/quant_calibration_dataset_v1), to showcase an example.

### Calibration configuration

```yaml theme={"system"}
quantization_config:
  calib_size: 768                    # Number of samples
  calib_dataset: "cnn_dailymail"      # Dataset name
  calib_max_seq_length: 1024          # Max sequence length
```

Increase `calib_size` for larger models. Use domain-specific datasets when available for better accuracy on specialized tasks.

## Hardware requirements

`FP4` quantization requires B200 GPUs. `FP8` runs on L4 and above.

| **Quantization** | **Minimum GPU** | **Recommended GPU** | **Memory reduction** |
| ---------------- | --------------- | ------------------- | -------------------- |
| `FP16`/`BF16`    | A100            | H100                | None                 |
| `FP8`            | L4              | H100                | \~50%                |
| `FP8_KV`         | L4              | H100                | \~60%                |
| `FP4`            | B200            | B200                | \~75%                |
| `FP4_KV`         | B200            | B200                | \~80%                |

### Configuration examples

**Engine-Builder-LLM:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: decoder
    quantization_type: fp8
    quantization_config:
      calib_size: 1024
```

**BIS-LLM:**

```yaml theme={"system"}
trt_llm:
  inference_stack: v2
  build:
    quantization_type: fp8
    quantization_config:
      calib_size: 1024
  runtime:
    max_seq_len: 32768
```

**BEI:**

```yaml theme={"system"}
trt_llm:
  build:
    base_model: encoder
    quantization_type: fp8
    max_num_tokens: 16384
```

Set `quantization_type` in the build section and add `quantization_config` to customize calibration. BIS-LLM uses `inference_stack: v2` while Engine-Builder-LLM uses `base_model: decoder`.

## Best practices

### When to use quantization

Use `FP8` for production deployments to achieve cost-effective scaling. For memory-constrained environments, `FP8_KV` or `FP4` variants provide additional memory reduction. Quantization becomes essential for models over 15B parameters where memory and cost savings are significant.

### When to avoid quantization

Skip quantization when maximum accuracy is critical. Use `FP16`/`BF16` instead. Small models under 8B parameters see minimal benefit from quantization. BEI-Bert models don't support quantization at all. During research and development, `FP16` provides faster iteration without calibration overhead.

### Optimization tips

Use calibration datasets that match your domain for best accuracy. Test quantized models with your specific data before production deployment. Monitor the accuracy vs. performance trade-off and consider your hardware constraints when selecting quantization type.

## Further reading

* [Engine-Builder-LLM configuration](/engines/engine-builder-llm/engine-builder-config): Dense model configuration.
* [BIS-LLM configuration](/engines/bis-llm/bis-llm-config): MoE model configuration.
* [BEI configuration](/engines/bei/bei-reference): Embedding model configuration.


# Structured outputs
Source: https://docs.baseten.co/engines/performance-concepts/structured-outputs

JSON schema validation and controlled text generation across all engines

Structured outputs let you generate text that conforms to specific JSON schemas, providing reliable data extraction and controlled text generation. This feature is supported by Baseten engines like [BIS-LLM](/engines/bis-llm/overview) and [Engine-Builder-LLM](/engines/engine-builder-llm/overview), as well as other inference frameworks like [vLLM](/examples/vllm) and [SGLang](/examples/sglang).

## Quick start

Structured outputs require two components: a Pydantic schema defining your expected output format, and an API call that enforces that schema.

### Define a schema

```python theme={"system"}
from pydantic import BaseModel

class Task(BaseModel):
    title: str
    priority: str  # "low", "medium", "high"
    due_date: str
    description: str
```

Each field requires a type annotation. The model's response will conform to these types exactly.

### Generate structured output

```python theme={"system"}
import os
from pydantic import BaseModel
from openai import OpenAI

class Task(BaseModel):
    title: str
    priority: str
    due_date: str
    description: str

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

response = client.beta.chat.completions.parse(
    model="not-required",
    messages=[
        {"role": "user", "content": "Create a task for: Review the quarterly report by next Friday"}
    ],
    response_format=Task
)

task = response.choices[0].message.parsed
print(f"Task: {task.title}")
print(f"Priority: {task.priority}")
```

Point `base_url` to your model's production endpoint. Pass your Pydantic class to `response_format` and use `beta.chat.completions.parse` instead of the regular `create` method.

The response includes a `parsed` attribute with your data already converted to a `Task` object, so no JSON parsing is needed.

## Engine support

Structured outputs are compatible with:

* **Engine-Builder-LLM**, except when Lookahead speculative decoding is configured.
* **BIS-LLM**: except for a few exceptions like overlap scheduler enabled.

### Model support

All Engine-Builder-LLM and BIS-LLM models support structured outputs out of the box with no additional configuration required.

## Best practices

### Schema design

* **Keep schemas simple**: 2-3 levels max nesting for best results.
* **Use basic types**: str, int, float, bool when possible.
* **Set defaults**: Provide reasonable default values for optional fields.
* **Descriptive names**: Use clear, descriptive field names.

### Prompt engineering

* **Low temperature**: Use 0.1-0.3 for consistent outputs.
* **Provide schema**: Dump the model schema and few-shot examples into context.
* **Provide context**: Give background for complex schemas.

## Further reading

* [Engine-Builder-LLM overview](/engines/engine-builder-llm/overview): Dense model documentation.
* [BIS-LLM overview](/engines/bis-llm/overview): MoE model documentation.
* [Quantization guide](/engines/performance-concepts/quantization-guide): `FP8`/`FP4` trade-offs.


# Embeddings with BEI
Source: https://docs.baseten.co/examples/bei

Serve embedding, reranking, and classification models

Baseten Embeddings Inference is Baseten's solution for production grade inference on embedding, classification and reranking models using TensorRT-LLM.

With Baseten Embeddings Inference you get the following benefits:

* Lowest-latency inference across any embedding solution (vLLM, SGlang, Infinity, TEI, Ollama)<sup>1</sup>
* Highest-throughput inference across any embedding solution (vLLM, SGlang, Infinity, TEI, Ollama) - thanks to XQA kernels, FP8 and dynamic batching.<sup>2</sup>
* High parallelism: up to 1400 client embeddings per second
* Cached model weights for fast vertical scaling and high availability - no Hugging Face hub dependency at runtime
* Ahead-of-time compilation, memory allocation and fp8 post-training quantization

### Getting started with embedding models:

Embedding models are LLMs without a lm\_head for language generation.
Typical architectures that are supported for embeddings are `LlamaModel`, `BertModel`, `RobertaModel` or `Gemma2Model`, and contain the safetensors, config, tokenizer and sentence-transformer config files.
A good example is the repo [BAAI/bge-multilingual-gemma2](https://huggingface.co/BAAI/bge-multilingual-gemma2).

To deploy a model for embeddings, set the following config in your local directory.

```yaml config.yaml theme={"system"}
model_name: BEI-Linq-Embed-Mistral
resources:
  accelerator: H100_40GB
  use_gpu: true
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      # for a different model, change the repo to e.g. to "Salesforce/SFR-Embedding-Mistral"
      # "BAAI/bge-en-icl" or "BAAI/bge-m3"
      repo: "Linq-AI-Research/Linq-Embed-Mistral"
      revision: main
      source: HF
    # only Llama, Mistral and Qwen Models support quantization.
    # others, use: "quantization_type: no_quant"
    quantization_type: fp8
```

With `config.yaml` in your local directory, you can deploy the model to Baseten.

```bash theme={"system"}
truss push --publish --promote
```

Deployed embedding models are OpenAI compatible without any additional settings.
You may use the client code below to consume the model.

```python theme={"system"}
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    # add the deployment URL
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

embedding = client.embeddings.create(
    input=["Baseten Embeddings are fast.", "Embed this sentence!"],
    model="not-required"
)
```

### Example deployment of a classification, reranking and classification models

Besides embedding models, BEI deploys high-throughput rerank and classification models.
You can identify suitable architectures by their `ForSequenceClassification` suffix in the huggingface repo.
The use-case for these models is either Reward Modeling, Reranking documents in RAG or tasks like content moderation.

```yaml theme={"system"}
model_name: BEI-mixedbread-rerank-large-v2-fp8
resources:
  accelerator: H100_40GB
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      repo: michaelfeil/mxbai-rerank-large-v2-seq
      revision: main
      source: HF
    # only Llama, Mistral and Qwen Models support quantization
    quantization_type: fp8
```

As OpenAI does not offer reranking or classification, we are sending a simple request to the endpoint.
Depending on the model, you might want to apply a specific prompt template first.

```python theme={"system"}
import requests
import os

headers = {
    f"Authorization": f"Api-Key {os.environ['BASETEN_API_KEY']}"
}

# model specific prompt for mixedbread's reranker v2.
prompt = (
  "<|endoftext|><|im_start|>system\nYou are Qwen, created by Alibaba Cloud. You are a helpful assistant.\n<|im_end|>\n<|im_start|>user\n"
  "query: {query} \ndocument: {doc} \nYou are a search relevance expert who evaluates how well documents match search queries. For each query-document pair, carefully analyze the semantic relationship between them, then provide your binary relevance judgment (0 for not relevant, 1 for relevant).\nRelevance:<|im_end|>\n<|im_start|>assistant\n"
).format(query="What is Baseten?",doc="Baseten is a fast inference provider.")

requests.post(
    headers=headers,
    url="https://model-xxxxxx.api.baseten.co/environments/production/sync/predict",
    json={
        "inputs": prompt,
        "raw_scores": True,
    }
)
```

### Benchmarks and Performance optimizations

Embedding models on BEI are fast, and offer currently the fastest implementation for embeddings across all open-source and closed-source providers.
The team behind the implementation are the authors of [infinity](https://github.com/michaelfeil/infinity).
We recommend using fp8 quantization for LLama, Mistral and Qwen2 models on L4 or newer (L4, H100, H200 and B200).
Quality difference between fp8 and bfloat16 is often negligible - embedding models often retentain of >99% cosine simalarity between both presisions,
and reranking models retain the ranking order - despite a difference in the retained output.
For more details, check out the [technical launch post](https://www.baseten.co/blog/how-we-built-high-throughput-embedding-inference-with-tensorrt-llm/).

<Frame>
  <img />
</Frame>

The team at Baseten has additional options for sharing cached model weights across replicas - for very fast horizontal scaling.
Please contact us to enable this option.

### Deploy custom or fine-tuned models on BEI:

We support the deployment of of the below models, as well all finetuned variants of these models (same architecture & customized weights).
The following repositories are supported - this list is not exhaustive.

| Model Repository                                                                                              | Architecture                        | Function            |
| ------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------- |
| [`Salesforce/SFR-Embedding-Mistral`](https://huggingface.co/Salesforce/SFR-Embedding-Mistral)                 | MistralModel                        | embedding           |
| [`BAAI/bge-m3`](https://huggingface.co/BAAI/bge-m3)                                                           | BertModel                           | embedding           |
| [`BAAI/bge-multilingual-gemma2`](https://huggingface.co/BAAI/bge-multilingual-gemma2)                         | Gemma2Model                         | embedding           |
| [`mixedbread-ai/mxbai-embed-large-v1`](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1)             | BertModel                           | embedding           |
| [`BAAI/bge-large-en-v1.5`](https://huggingface.co/BAAI/bge-large-en-v1.5)                                     | BertModel                           | embedding           |
| [`allenai/Llama-3.1-Tulu-3-8B-RM`](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM)                     | LlamaForSequenceClassification      | classifier          |
| [`ncbi/MedCPT-Cross-Encoder`](https://huggingface.co/ncbi/MedCPT-Cross-Encoder)                               | BertForSequenceClassification       | reranker/classifier |
| [`SamLowe/roberta-base-go_emotions`](https://huggingface.co/SamLowe/roberta-base-go_emotions)                 | XLMRobertaForSequenceClassification | classifier          |
| [`mixedbread/mxbai-rerank-large-v2-seq`](https://huggingface.co/michaelfeil/mxbai-rerank-large-v2-seq)        | Qwen2ForSequenceClassification      | reranker/classifier |
| [`BAAI/bge-en-icl`](https://huggingface.co/BAAI/bge-en-icl)                                                   | LlamaModel                          | embedding           |
| [`BAAI/bge-reranker-v2-m3`](https://huggingface.co/BAAI/bge-reranker-v2-m3)                                   | BertForSequenceClassification       | reranker/classifier |
| [`Skywork/Skywork-Reward-Llama-3.1-8B-v0.2`](https://huggingface.co/Skywork/Skywork-Reward-Llama-3.1-8B-v0.2) | LlamaForSequenceClassification      | classifier          |
| [`Snowflake/snowflake-arctic-embed-l`](https://huggingface.co/Snowflake/snowflake-arctic-embed-l)             | BertModel                           | embedding           |
| [`nomic-ai/nomic-embed-code`](https://huggingface.co/nomic-ai/nomic-embed-code)                               | Qwen2Model                          | embedding           |

<sup>1</sup> measured on H100-HBM3 (bert-large-335M, for BAAI/bge-en-icl: 9ms)
<sup>2</sup> measured on H100-HBM3 (leading model architecture on MTEB, MistralModel-7B)


# Transcribe audio with Chains
Source: https://docs.baseten.co/examples/chains-audio-transcription

Process hours of audio in seconds using efficient chunking, distributed inference, and optimized GPU resources.

<Card title="View example on GitHub" icon="github" href="https://github.com/basetenlabs/truss-examples/tree/main/chains-examples/docs/audio-transcription" />

This guide walks through building an audio transcription pipeline using Chains. You'll break down large media files, distribute transcription tasks across autoscaling deployments, and leverage high-performance GPUs for rapid inference.

# 1. Overview

This Chain enables fast, high-quality transcription by:

* **Partitioning** long files (10+ hours) into smaller segments.
* **Detecting silence** to optimize split points.
* **Parallelizing inference** across multiple GPU-backed deployments.
* **Batching requests** to maximize throughput.
* **Using range downloads** for efficient data streaming.
* Leveraging `asyncio` for concurrent execution.

# 2. Chain Structure

Transcription is divided into two processing layers:

1. **Macro chunks:** Large segments (\~300s) split from the source media file. These are processed in parallel to handle massive files efficiently.
2. **Micro chunks:** Smaller segments (\~5–30s) extracted from macro chunks and sent to the Whisper model for transcription.

# 3. Implementing the Chainlets

## `Transcribe` (Entrypoint Chainlet)

Handles transcription requests and dispatches tasks to worker Chainlets.

Function signature:

```python theme={"system"}
async def run_remote(
  self,
  media_url: str,
  params: data_types.TranscribeParams
) -> data_types.TranscribeOutput:
```

**Steps:**

* Validates that the media source supports **range downloads**.
* Uses **FFmpeg** to extract metadata and duration.
* Splits the file into **macro chunks**, optimizing split points at silent sections.
* Dispatches **macro chunk tasks** to the MacroChunkWorker for processing.
* Collects **micro chunk transcriptions**, merges results, and returns the final text.

**Example request:**

```bash theme={"system"}
curl -X POST $INVOCATION_URL \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '<JSON_INPUT>'
```

```json theme={"system"}
{
  "media_url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
  "params": {
    "micro_chunk_size_sec": 30,
    "macro_chunk_size_sec": 300
  }
}
```

## `MacroChunkWorker` (Processing Chainlet)

Processes **macro chunks** by:

* **Extracting** relevant time segments using **FFmpeg**.
* **Streaming audio** instead of downloading full files for low latency.
* **Splitting segments** at silent points.
* **Encoding** audio in base64 for efficient transfer.
* **Distributing micro chunks** to the Whisper model for transcription.

This Chainlet **runs in parallel** with multiple instances autoscaled dynamically.

## `WhisperModel` (Inference Model)

A separately deployed **Whisper** model Chainlet handles speech-to-text transcription.

* Deployed **independently** to allow fast iteration on business logic without redeploying the model.
* Used **across different Chains** or accessed directly as a standalone model.
* Supports **multiple environments** (e.g., dev, prod) using the same instance.

Whisper can also be deployed as a **standard Truss model**, separate from the Chain.

# 4. Optimizing Performance

Even for very large files, **processing time remains bounded** by parallel execution.

## Key performance tuning parameters:

* `micro_chunk_size_sec` → Balance GPU utilization and inference latency.
* `macro_chunk_size_sec` → Adjust chunk size for optimal parallelism.
* **Autoscaling settings** → Tune concurrency and replica counts for load balancing.

Example speedup:

```json theme={"system"}
{
  "input_duration_sec": 734.26,
  "processing_duration_sec": 82.42,
  "speedup": 8.9
}
```

# 5. Deploy and run the Chain

## Deploy WhisperModel first:

```bash theme={"system"}
truss chains push whisper_chainlet.py
```

Copy the **invocation URL** and update `WHISPER_URL` in `transcribe.py`.

## Deploy the transcription Chain:

```bash theme={"system"}
truss chains push transcribe.py
```

## Run transcription on a sample file:

```bash theme={"system"}
curl -X POST $INVOCATION_URL \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '<JSON_INPUT>'
```

***

# Next Steps

* Learn more about [Chains](/development/chain/overview).
* Optimize GPU **autoscaling** for peak efficiency.
* Extend the pipeline with **custom business logic**.


# RAG pipeline with Chains
Source: https://docs.baseten.co/examples/chains-build-rag

Build a RAG (retrieval-augmented generation) pipeline with  Chains

[Learn more about Chains](/development/chain/overview)

## Prerequisites

To use Chains, install a recent Truss version and ensure pydantic is v2:

```bash theme={"system"}
pip install --upgrade truss 'pydantic>=2.0.0'
```

<Accordion title="Help for setting up a clean development environment">
  Truss requires python `>=3.9,<3.15`. To set up a fresh development environment,
  you can use the following commands, creating a environment named `chains_env`
  using `pyenv`:

  ```bash theme={"system"}
  curl https://pyenv.run | bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  source ~/.bashrc
  pyenv install 3.11.0
  ENV_NAME="chains_env"
  pyenv virtualenv 3.11.0 $ENV_NAME
  pyenv activate $ENV_NAME
  pip install --upgrade truss 'pydantic>=2.0.0'
  ```
</Accordion>

To deploy Chains remotely, you also need a
[Baseten account](https://app.baseten.co/signup).
It is handy to export your API key to the current shell session or permanently in your `.bashrc`:

```bash ~/.bashrc theme={"system"}
export BASETEN_API_KEY="nPh8..."
```

If you want to run this example in
[local debugging mode](/development/chain/localdev#test-a-chain-locally), you'll also need to
install chromadb:

```shell theme={"system"}
pip install chromadb
```

The complete code used in this tutorial can also be found in the
[Chains examples repo](https://github.com/basetenlabs/models/tree/main/truss-chains/examples/rag).

# Overview

Retrieval-augmented generation (RAG) is a multi-model pipeline for generating
context-aware answers from LLMs.

There are a number of ways to build a RAG system. This tutorial shows a minimum
viable implementation with a basic vector store and retrieval function. It's
intended as a starting point to show how Chains helps you flexibly combine model
inference and business logic.

In this tutorial, we'll build a simple RAG pipeline for a hypothetical alumni
matching service for a university. The system:

1. Takes a bio with information about a new graduate
2. Uses a vector database to retrieve semantically similar bios of other alums
3. Uses an LLM to explain why the new graduate should meet the selected alums
4. Returns the writeup from the LLM

Let's dive in!

## Building the Chain

Create a file `rag.py` in a new directory with:

```sh theme={"system"}
mkdir rag
touch rag/rag.py
cd rag
```

Our RAG Chain is composed of three parts:

* `VectorStore`, a Chainlet that implements a vector database with a retrieval
  function.
* `LLMClient`, a Stub for connecting to a deployed LLM.
* `RAG`, the entrypoint Chainlet that orchestrates the RAG pipeline and
  has `VectorStore` and `LLMClient` as dependencies.

We'll examine these components one by one and then see how they all work
together.

### Vector store Chainlet

A real production RAG system would use a hosted vector database with a massive
number of stored embeddings. For this example, we're using a small local vector
store built with `chromadb` to stand in for a more complex system.

The Chainlet has three parts:

* [`remote_config`](/reference/sdk/chains#remote-configuration), which
  configures a Docker image on deployment with dependencies.
* `__init__()`, which runs once when the Chainlet is spun up, and creates the
  vector database with ten sample bios.
* [`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets), which runs
  each time the Chainlet is called and is the sole public interface for the
  Chainlet.

```python rag/rag.py theme={"system"}
import truss_chains as chains


# Create a Chainlet to serve as our vector database.
class VectorStore(chains.ChainletBase):
    # Add chromadb as a dependency for deployment.
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            pip_requirements=["chromadb"]
        )
    )
    # Runs once when the Chainlet is deployed or scaled up.
    def __init__(self):
        # Import Chainlet-specific dependencies in init, not at the top of
        # the file.
        import chromadb
        self._chroma_client = chromadb.EphemeralClient()
        self._collection = self._chroma_client.create_collection(name="bios")
        # Sample documents are hard-coded for your convenience
        documents = [
            "Angela Martinez is a tech entrepreneur based in San Francisco. As the founder and CEO of a successful AI startup, she is a leading figure in the tech community. Outside of work, Angela enjoys hiking the trails around the Bay Area and volunteering at local animal shelters.",
            "Ravi Patel resides in New York City, where he works as a financial analyst. Known for his keen insight into market trends, Ravi spends his weekends playing chess in Central Park and exploring the city's diverse culinary scene.",
            "Sara Kim is a digital marketing specialist living in San Francisco. She helps brands build their online presence with creative strategies. Outside of work, Sara is passionate about photography and enjoys hiking the trails around the Bay Area.",
            "David O'Connor calls New York City his home and works as a high school teacher. He is dedicated to inspiring the next generation through education. In his free time, David loves running along the Hudson River and participating in local theater productions.",
            "Lena Rossi is an architect based in San Francisco. She designs sustainable and innovative buildings that contribute to the city's skyline. When she's not working, Lena enjoys practicing yoga and exploring art galleries.",
            "Akio Tanaka lives in Tokyo and is a software developer specializing in mobile apps. Akio is an avid gamer and enjoys attending eSports tournaments. He also has a passion for cooking and often experiments with new recipes in his spare time.",
            "Maria Silva is a nurse residing in New York City. She is dedicated to providing compassionate care to her patients. Maria finds joy in gardening and often spends her weekends tending to her vibrant flower beds and vegetable garden.",
            "John Smith is a journalist based in San Francisco. He reports on international politics and has a knack for uncovering compelling stories. Outside of work, John is a history buff who enjoys visiting museums and historical sites.",
            "Aisha Mohammed lives in Tokyo and works as a graphic designer. She creates visually stunning graphics for a variety of clients. Aisha loves to paint and often showcases her artwork in local exhibitions.",
            "Carlos Mendes is an environmental engineer in San Francisco. He is passionate about developing sustainable solutions for urban areas. In his leisure time, Carlos enjoys surfing and participating in beach clean-up initiatives."
        ]
        # Add all documents to the database
        self._collection.add(
            documents=documents,
            ids=[f"id{n}" for n in range(len(documents))]
        )

    # Runs each time the Chainlet is called
    async def run_remote(self, query: str) -> list[str]:
        # This call to includes embedding the query string.
        results = self._collection.query(query_texts=[query], n_results=2)
        if results is None or not results:
            raise ValueError("No bios returned from the query")
        if not results["documents"] or not results["documents"][0]:
            raise ValueError("Bios are empty")
        return results["documents"][0]
```

### LLM inference stub

Now that we can retrieve relevant bios from the vector database, we need to pass
that information to an LLM to generate our final output.

Chains can integrate previously deployed models using a Stub. Like Chainlets,
Stubs implement
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets), but as a call
to the deployed model.

For our LLM, we'll use Phi-3 Mini Instruct, a small-but-mighty open source LLM.

<Card title="Deploy Phi-3 Mini Instruct 4k" icon="rocket" href="https://www.baseten.co/library/phi-3-mini-4k-instruct/">
  One-click model deployment from Baseten's model library.
</Card>

While the model is deploying, be sure to note down the models' invocation URL from
the model dashboard for use in the next step.

To use our deployed LLM in the RAG Chain, we define a Stub:

```python rag/rag.py theme={"system"}
class LLMClient(chains.StubBase):
    # Runs each time the Stub is called
    async def run_remote(self, new_bio: str, bios: list[str]) -> str:
        # Use the retrieved bios to augment the prompt -- here's the "A" in RAG!
        prompt = f"""You are matching alumni of a college to help them make connections. Explain why the person described first would want to meet the people selected from the matching database.
        Person you're matching: {new_bio}
        People from database: {" ".join(bios)}"""
        # Call the deployed model.
        resp = await self._remote.predict_async(json_payload={
            "messages": [{"role": "user", "content": prompt}],
            "stream"  : False
        })
        return resp["output"][len(prompt) :].strip()
```

### RAG entrypoint Chainlet

The entrypoint to a Chain is the Chainlet that specifies the public-facing input
and output of the Chain and orchestrates calls to dependencies.

The `__init__` function in this Chainlet takes two new arguments:

* Add dependencies to any Chainlet with
  [`chains.depends()`](/reference/sdk/chains#truss-chains-depends). Only
  Chainlets, not Stubs, need to be added in this fashion.
* Use
  [`chains.depends_context()`](/reference/sdk/chains#truss-chains-depends-context)
  to inject a context object at runtime. This context object is required to
  initialize the `LLMClient` stub.
* Visit your [baseten workspace](https://app.baseten.co/models) to find your
  the URL of the previously deployed Phi-3 model and insert if as value
  for `LLM_URL`.

```python rag/rag.py theme={"system"}
# Insert the URL from the previously deployed Phi-3 model.
LLM_URL = ...

@chains.mark_entrypoint
class RAG(chains.ChainletBase):

    # Runs once when the Chainlet is spun up
    def __init__(
        self,
        # Declare dependency chainlets.
        vector_store: VectorStore = chains.depends(VectorStore),
        context: chains.DeploymentContext = chains.depends_context(),
    ):
        self._vector_store = vector_store
        # The stub needs the context for setting up authentication.
        self._llm = LLMClient.from_url(LLM_URL, context)

    # Runs each time the Chain is called
    async def run_remote(self, new_bio: str) -> str:
        # Use the VectorStore Chainlet for context retrieval.
        bios = await self._vector_store.run_remote(new_bio)
        # Use the LLMClient Stub for augmented generation.
        contacts = await self._llm.run_remote(new_bio, bios)
        return contacts
```

## Testing locally

Because our Chain uses a Stub for the LLM call, we can run the whole Chain
locally without any GPU resources.

Before running the Chainlet, make sure to set your Baseten API key as an
environment variable `BASETEN_API_KEY`.

```python rag/rag.py theme={"system"}
if __name__ == "__main__":
    import os
    import asyncio

    with chains.run_local(
        # This secret is needed even locally, because part of this chain
        # calls the separately deployed Phi-3 model. Only the Chainlets
        # actually run locally.
        secrets={"baseten_chain_api_key": os.environ["BASETEN_API_KEY"]}
    ):
        rag_client = RAG()
        result = asyncio.get_event_loop().run_until_complete(
            rag_client.run_remote(
                """
                Sam just moved to Manhattan for his new job at a large bank.
                In college, he enjoyed building sets for student plays.
                """
            )
        )
        print(result)
```

We can run our Chain locally:

```sh theme={"system"}
python rag.py
```

After a few moments, we should get a recommendation for why Sam should meet the
alumni selected from the database.

## Deploying to production

Once we're satisfied with our Chain's local behavior, we can deploy it to
production on Baseten. To deploy the Chain, run:

```sh theme={"system"}
truss chains push rag.py
```

This will deploy our Chain as a development deployment. Once the Chain is
deployed, we can call it from its API endpoint.

You can do this in the console with cURL:

```sh theme={"system"}
curl -X POST 'https://chain-5wo86nn3.api.baseten.co/development/run_remote' \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '{"new_bio": "Sam just moved to Manhattan for his new job at a large bank.In college, he enjoyed building sets for student plays."}'
```

Alternatively, you can also integrate this in a Python application:

```python call_chain.py theme={"system"}
import requests
import os

# Insert the URL from the deployed rag chain. You can get it from the CLI
# output or the status page, e.g.
# "https://chain-6wgeygoq.api.baseten.co/production/run_remote".
RAG_CHAIN_URL = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

if not RAG_CHAIN_URL:
    raise ValueError("Please insert the URL for the RAG chain.")

resp = requests.post(
    RAG_CHAIN_URL,
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={"new_bio": new_bio},
)

print(resp.json())
```

When we're happy with the deployed Chain, we can promote it to production via
the UI or by running:

```sh theme={"system"}
truss chains push --promote rag.py
```

Once in production, the Chain will have access to full autoscaling settings.
Both the development and production deployments will scale to zero when not in
use.


# Deploy a ComfyUI project
Source: https://docs.baseten.co/examples/comfyui

Deploy your ComfyUI workflow as an API endpoint

<Card title="View example on GitHub" icon="github" href="https://github.com/basetenlabs/truss-examples/tree/main/comfyui-truss" />

In this example, we'll deploy an **anime style transfer** ComfyUI workflow using truss.
This example won't require any Python code, but there are a few pre-requisites in order to get started.

Pre-Requisites:

1. Convert your ComfyUI workflow to an **API compatible JSON format**. The regular JSON format that is used to export Comfy workflows will not work here.
2. Have a list of the models your workflow requires along with URLs to where each model can be downloaded

## Setup

Clone the truss-examples repository and navigate to the `comfyui-truss` directory

```bash theme={"system"}
git clone https://github.com/basetenlabs/truss-examples.git
cd truss-examples/comfyui-truss
```

This repository already contains all the files we need to deploy our ComfyUI workflow.
There are just two files we need to modify:

1. `config.yaml`
2. `data/comfy_ui_workflow.json`

## Setting up the `config.yaml`

```yaml theme={"system"}
build_commands:
- git clone https://github.com/comfyanonymous/ComfyUI.git
- cd ComfyUI && git checkout b1fd26fe9e55163f780bf9e5f56bf9bf5f035c93 && pip install -r requirements.txt
- cd ComfyUI/custom_nodes && git clone https://github.com/LykosAI/ComfyUI-Inference-Core-Nodes --recursive && cd ComfyUI-Inference-Core-Nodes && pip install -e .[cuda12]
- cd ComfyUI/custom_nodes && git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-Gemini --recursive && cd ComfyUI-Gemini && pip install -r requirements.txt
- cd ComfyUI/custom_nodes && git clone https://github.com/kijai/ComfyUI-Marigold --recursive && cd ComfyUI-Marigold && pip install -r requirements.txt
- cd ComfyUI/custom_nodes && git clone https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92 --recursive
- cd ComfyUI/custom_nodes && git clone https://github.com/Fannovel16/comfyui_controlnet_aux --recursive && cd comfyui_controlnet_aux && pip install -r requirements.txt
- cd ComfyUI/models/controlnet && wget -O control-lora-canny-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-canny-rank256.safetensors
- cd ComfyUI/models/controlnet && wget -O control-lora-depth-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors
- cd ComfyUI/models/checkpoints && wget -O dreamshaperXL_v21TurboDPMSDE.safetensors https://civitai.com/api/download/models/351306
- cd ComfyUI/models/loras && wget -O StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors https://huggingface.co/artificialguybr/StudioGhibli.Redmond-V2/resolve/main/StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors
environment_variables: {}
external_package_dirs: []
model_metadata: {}
model_name: Anime Style Transfer
python_version: py310
requirements:
  - websocket-client
  - accelerate
  - opencv-python
resources:
  accelerator: H100
  use_gpu: true
secrets: {}
system_packages:
  - wget
  - ffmpeg
  - libgl1-mesa-glx
```

The main part that needs to get filled out is under `build_commands`. Build commands are shell commands that get run during the build stage of the docker image.

In this example, the first two lines clone the ComfyUI repository and install the python requirements.
The latter commands install various custom nodes and models and place them in their respective directory within the ComfyUI repository.

## Modifying `data/comfy_ui_workflow.json`

The `comfy_ui_workflow.json` contains the entire ComfyUI workflow in an API compatible format. This is the workflow that will get executed by the ComfyUI server.

Here is the workflow we will be using for this example.

<Accordion title="Anime Style Transfer Workflow">
  ```json theme={"system"}
  {
      "1": {
        "inputs": {
          "ckpt_name": "dreamshaperXL_v21TurboDPMSDE.safetensors"
        },
        "class_type": "CheckpointLoaderSimple",
        "_meta": {
          "title": "Load Checkpoint"
        }
      },
      "3": {
        "inputs": {
          "image": "{{input_image}}",
          "upload": "image"
        },
        "class_type": "LoadImage",
        "_meta": {
          "title": "Load Image"
        }
      },
      "4": {
        "inputs": {
          "text": [
            "160",
            0
          ],
          "clip": [
            "154",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "12": {
        "inputs": {
          "strength": 0.8,
          "conditioning": [
            "131",
            0
          ],
          "control_net": [
            "13",
            0
          ],
          "image": [
            "71",
            0
          ]
        },
        "class_type": "ControlNetApply",
        "_meta": {
          "title": "Apply ControlNet"
        }
      },
      "13": {
        "inputs": {
          "control_net_name": "control-lora-canny-rank256.safetensors"
        },
        "class_type": "ControlNetLoader",
        "_meta": {
          "title": "Load ControlNet Model"
        }
      },
      "15": {
        "inputs": {
          "strength": 0.8,
          "conditioning": [
            "12",
            0
          ],
          "control_net": [
            "16",
            0
          ],
          "image": [
            "18",
            0
          ]
        },
        "class_type": "ControlNetApply",
        "_meta": {
          "title": "Apply ControlNet"
        }
      },
      "16": {
        "inputs": {
          "control_net_name": "control-lora-depth-rank256.safetensors"
        },
        "class_type": "ControlNetLoader",
        "_meta": {
          "title": "Load ControlNet Model"
        }
      },
      "18": {
        "inputs": {
          "seed": 995352869972963,
          "denoise_steps": 4,
          "n_repeat": 10,
          "regularizer_strength": 0.02,
          "reduction_method": "median",
          "max_iter": 5,
          "tol": 0.001,
          "invert": true,
          "keep_model_loaded": true,
          "n_repeat_batch_size": 2,
          "use_fp16": true,
          "scheduler": "LCMScheduler",
          "normalize": true,
          "model": "marigold-lcm-v1-0",
          "image": [
            "3",
            0
          ]
        },
        "class_type": "MarigoldDepthEstimation",
        "_meta": {
          "title": "MarigoldDepthEstimation"
        }
      },
      "19": {
        "inputs": {
          "images": [
            "71",
            0
          ]
        },
        "class_type": "PreviewImage",
        "_meta": {
          "title": "Preview Image"
        }
      },
      "20": {
        "inputs": {
          "images": [
            "18",
            0
          ]
        },
        "class_type": "PreviewImage",
        "_meta": {
          "title": "Preview Image"
        }
      },
      "21": {
        "inputs": {
          "seed": 358881677137626,
          "steps": 20,
          "cfg": 7,
          "sampler_name": "dpmpp_2m_sde",
          "scheduler": "karras",
          "denoise": 0.7000000000000001,
          "model": [
            "154",
            0
          ],
          "positive": [
            "15",
            0
          ],
          "negative": [
            "4",
            0
          ],
          "latent_image": [
            "25",
            0
          ]
        },
        "class_type": "KSampler",
        "_meta": {
          "title": "KSampler"
        }
      },
      "25": {
        "inputs": {
          "pixels": [
            "70",
            0
          ],
          "vae": [
            "1",
            2
          ]
        },
        "class_type": "VAEEncode",
        "_meta": {
          "title": "VAE Encode"
        }
      },
      "27": {
        "inputs": {
          "samples": [
            "21",
            0
          ],
          "vae": [
            "1",
            2
          ]
        },
        "class_type": "VAEDecode",
        "_meta": {
          "title": "VAE Decode"
        }
      },
      "70": {
        "inputs": {
          "upscale_method": "lanczos",
          "megapixels": 1,
          "image": [
            "3",
            0
          ]
        },
        "class_type": "ImageScaleToTotalPixels",
        "_meta": {
          "title": "ImageScaleToTotalPixels"
        }
      },
      "71": {
        "inputs": {
          "low_threshold": 50,
          "high_threshold": 150,
          "resolution": 1024,
          "image": [
            "3",
            0
          ]
        },
        "class_type": "CannyEdgePreprocessor",
        "_meta": {
          "title": "Canny Edge"
        }
      },
      "123": {
        "inputs": {
          "images": [
            "27",
            0
          ]
        },
        "class_type": "PreviewImage",
        "_meta": {
          "title": "Preview Image"
        }
      },
      "131": {
        "inputs": {
          "text": [
            "159",
            0
          ],
          "clip": [
            "154",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "152": {
        "inputs": {
          "text": "{{prompt}}"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text_1"
        }
      },
      "154": {
        "inputs": {
          "lora_name": "StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors",
          "strength_model": 0.6,
          "strength_clip": 1,
          "model": [
            "1",
            0
          ],
          "clip": [
            "1",
            1
          ]
        },
        "class_type": "LoraLoader",
        "_meta": {
          "title": "Load LoRA"
        }
      },
      "156": {
        "inputs": {
          "text_1": [
            "152",
            0
          ],
          "text_2": [
            "158",
            0
          ]
        },
        "class_type": "ConcatText_Zho",
        "_meta": {
          "title": "✨ConcatText_Zho"
        }
      },
      "157": {
        "inputs": {
          "text": "StdGBRedmAF,Studio Ghibli,"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text _2"
        }
      },
      "158": {
        "inputs": {
          "text": "looking at viewer, anime artwork, anime style, key visual, vibrant, studio anime, highly detailed"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text _O"
        }
      },
      "159": {
        "inputs": {
          "text_1": [
            "156",
            0
          ],
          "text_2": [
            "157",
            0
          ]
        },
        "class_type": "ConcatText_Zho",
        "_meta": {
          "title": "✨ConcatText_Zho"
        }
      },
      "160": {
        "inputs": {
          "text": "photo, deformed, black and white, realism, disfigured, low contrast"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text _O"
        }
      }
    }
  ```
</Accordion>

**Important:**
If you look at the JSON file above, you'll notice we have templatized a few items using the **`{{handlebars}}`** templating style.

If there are any inputs in your ComfyUI workflow that should be variables such as input prompts, images, etc, you should templatize them using the handlebars format.

In this example workflow, there are two inputs:  **`{{input_image}}`** and **`{{prompt}}`**

When making an API call to this workflow, we will be able to pass in any variable for these two inputs.

## Deploying the Workflow to Baseten

Once you have both your `config.yaml` and `data/comfy_ui_workflow.json` filled out we can deploy this workflow just like any other model on Baseten.

1. `pip install truss --upgrade`
2. `truss push --publish`

## Running Inference

When you deploy the truss, it will spin up a new deployment in your Baseten account. Each deployment will expose a REST API endpoint which we can use to call this workflow.

```python theme={"system"}
import requests
import os
import base64
from PIL import Image
from io import BytesIO

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
BASE64_PREAMBLE = "data:image/png;base64,"

def pil_to_b64(pil_img):
   buffered = BytesIO()
   pil_img.save(buffered, format="PNG")
   img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
   return img_str

def b64_to_pil(b64_str):
   return Image.open(BytesIO(base64.b64decode(b64_str.replace(BASE64_PREAMBLE, ""))))

values = {
 "prompt": "american Shorthair",
 "input_image": {"type": "image", "data": pil_to_b64(Image.open("/path/to/cat.png"))}
}

resp = requests.post(
   f"https://model-{model_id}.api.baseten.co/production/predict",
   headers={"Authorization": f"Api-Key {baseten_api_key}"},
   json={"workflow_values": values}
)

res = resp.json()
results = res.get("result")

for item in results:
   if item.get("format") == "png":
       data = item.get("data")
       img = b64_to_pil(data)
       img.save(f"pet-style-transfer-1.png")
```

If you recall, we templatized two variables in our workflow: `prompt` and `input_image`. In our API call we can specify the values for these two variables like so:

```json theme={"system"}
values = {
 "prompt": "Maltipoo",
 "input_image": {"type": "image", "data": pil_to_b64(Image.open("/path/to/dog.png"))}
}
```

If your workflow contains more variables, simply add them to the dictionary above.

The API call returns an image in the form of a base64 string, which we convert to a PNG image.

<Frame>
  <img />
</Frame>


# Deploy your first model
Source: https://docs.baseten.co/examples/deploy-your-first-model

Learn how to package and deploy an AI model as a production-ready API endpoint on Baseten.

Deploying a model to Baseten turns your model code into a production-ready API endpoint. You package your model with [Truss](https://pypi.org/project/truss/), push it to Baseten, and receive a URL you can call from any application.

This guide walks through deploying [Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct), a 3.8B parameter LLM, from local code to a production API. You'll create a Truss project, write model code, configure dependencies and GPU resources, deploy to Baseten, and call your model's API endpoint.

## Set up your environment

Before you begin, [sign up](https://app.baseten.co/signup) or [sign in](https://app.baseten.co/login) to Baseten.

### Install Truss

[Truss](https://pypi.org/project/truss/) is Baseten's model packaging framework. It handles containerization, dependencies, and deployment configuration.

<Note>
  Using a virtual environment is recommended to avoid dependency conflicts with other Python projects.
</Note>

<Tabs>
  <Tab title="uv (recommended)">
    [uv](https://docs.astral.sh/uv/) is a fast Python package manager. These commands create a virtual environment, activate it, and install Truss:

    ```sh theme={"system"}
    uv venv && source .venv/bin/activate
    uv pip install truss
    ```
  </Tab>

  <Tab title="pip (macOS/Linux)">
    These commands create a virtual environment, activate it, and install Truss:

    ```sh theme={"system"}
    python -m venv .venv && source .venv/bin/activate
    pip install --upgrade truss
    ```
  </Tab>

  <Tab title="pip (Windows)">
    These commands create a virtual environment, activate it, and install Truss:

    ```sh theme={"system"}
    python -m venv .venv && .venv\Scripts\activate
    pip install --upgrade truss
    ```
  </Tab>
</Tabs>

<Tip>
  New accounts include free credits; this guide should use less than \$1 in GPU
  costs.
</Tip>

***

## Create a Truss

A **Truss** packages your model into a deployable container with all dependencies and configurations.

Create a new Truss:

```sh theme={"system"}
truss init phi-3-mini && cd phi-3-mini
```

When prompted, give your Truss a name like `Phi 3 Mini`.

This command scaffolds a project with the following structure:

```
phi-3-mini/
  model/
    __init__.py
    model.py
  config.yaml
  data/
  packages/
```

The key files are:

* `model/model.py`: Your model code with `load()` and `predict()` methods.
* `config.yaml`: Dependencies, resources, and deployment settings.
* `data/`: Optional directory for data files bundled with your model.
* `packages/`: Optional directory for local Python packages.

Truss uses this structure to build and deploy your model automatically. You
define your model in `model.py` and your infrastructure in `config.yaml`, no
Dockerfiles or container management required.

***

## Implement model code

In this example, you'll implement the model code for
[Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct).
You'll use the `transformers` library to load the model and tokenizer and PyTorch to run inference.
Replace the contents of `model/model.py` with the following code:

```python model/model.py theme={"system"}
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class Model:
    def __init__(self, **kwargs):
        self._model = None
        self._tokenizer = None

    def load(self):
        self._model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct",
            device_map="cuda",
            torch_dtype="auto"
        )
        self._tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct"
        )

    def predict(self, request):
        messages = request.pop("messages")
        model_inputs = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self._tokenizer(model_inputs, return_tensors="pt").to("cuda")
        with torch.no_grad():
            outputs = self._model.generate(input_ids=inputs["input_ids"], max_length=256)
        return {"output": self._tokenizer.decode(outputs[0], skip_special_tokens=True)}
```

Truss models follow a three-method pattern that separates initialization from inference:

| Method     | When it's called                     | What to do here                                           |
| ---------- | ------------------------------------ | --------------------------------------------------------- |
| `__init__` | Once when the class is created       | Initialize variables, store configuration, set secrets    |
| `load`     | Once at startup, before any requests | Load model weights, tokenizers, and other heavy resources |
| `predict`  | On every API request                 | Process input, run inference, return response             |

**Why separate `load` from `__init__`?**

The `load` method runs during the container's cold start, before your model
receives traffic. This keeps expensive operations (like downloading
large model weights) out of the request path.

### Understand the request/response flow

The `predict` method receives `request`, a dictionary containing the JSON body
from the API call:

```python theme={"system"}
# API call with: {"messages": [{"role": "user", "content": "Hello"}]}
def predict(self, request):
    messages = request.pop("messages")  # Extract from request
    # ... run inference ...
    return {"output": result}  # Return dict becomes JSON response
```

Whatever dictionary you return becomes the API response. You control the input
parameters and output format.

### GPU and memory patterns

A few patterns in this code are common across GPU models:

* **`device_map="cuda"`**: Loads model weights directly to GPU.
* **`.to("cuda")`**: Moves input tensors to GPU for inference.
* **`torch.no_grad()`**: Disables gradient tracking to save memory (gradients aren't needed for inference).

***

## Configure dependencies and GPU

The `config.yaml` file defines your model's environment and compute resources.
This configuration determines how your container is built and what hardware it
runs on.

### Set Python version and dependencies

```yaml config.yaml theme={"system"}
python_version: py311
requirements:
  - six==1.17.0
  - accelerate==0.30.1
  - einops==0.8.0
  - transformers==4.41.2
  - torch==2.3.0
```

**Key configuration options:**

| Field             | Purpose                                  | Example                           |
| ----------------- | ---------------------------------------- | --------------------------------- |
| `python_version`  | Python version for your container        | `py39`, `py310`, `py311`, `py312` |
| `requirements`    | Python packages to install (pip format)  | `torch==2.3.0`                    |
| `system_packages` | System-level dependencies (apt packages) | `ffmpeg`, `libsm6`                |

For the complete list of configuration options, see the [Truss reference config](/reference/truss-configuration).

<Note>
  Always pin exact versions (e.g., `torch==2.3.0` not `torch>=2.0`). This
  ensures reproducible builds and your model behaves the same way every time it's
  deployed.
</Note>

### Allocate a GPU

The `resources` section specifies what hardware your model runs on:

```yaml config.yaml theme={"system"}
resources:
  accelerator: T4
  use_gpu: true
```

**Choosing the right GPU:** Match your GPU to your model's VRAM requirements. For Phi-3-mini (\~7.6GB), a T4 (16GB) provides headroom for inference.

| GPU  | VRAM    | Good for                                    |
| ---- | ------- | ------------------------------------------- |
| T4   | 16GB    | Small models, embeddings, fine-tuned models |
| L4   | 24GB    | Medium models (7B parameters)               |
| A10G | 24GB    | Medium models, image generation             |
| A100 | 40/80GB | Large models (13B-70B parameters)           |
| H100 | 80GB    | Very large models, high throughput          |

<Tip>
  **Estimating VRAM:** A rough rule is 2GB of VRAM per billion parameters for float16 models. A 7B model needs \~14GB VRAM minimum.
</Tip>

***

## Deploy the model

### Authenticate with Baseten

First, generate an API key from the [Baseten settings](https://app.baseten.co/settings/account/api_keys). Then log in:

```sh theme={"system"}
truss login
```

The expected output is:

```output theme={"system"}
💻 Let's add a Baseten remote!
🤫 Quietly paste your API_KEY:
```

Paste your API key when prompted. Truss saves your credentials for future deployments.

### Push your model to Baseten

For development with live reload:

```sh theme={"system"}
truss push --watch
```

The expected output is:

```output theme={"system"}
Deploying truss using T4x4x16 instance type.
✨ Model Phi 3 Mini was successfully pushed ✨

🪵  View logs for your deployment at https://app.baseten.co/models/abc1d2ef/logs/xyz123
```

<Note>
  When no flag is specified, `truss push` defaults to a published deployment. Use `--watch` for development deployments with live reload support.
</Note>

In this example, the logs URL contains two IDs:

* **Model ID**: The string after `/models/` (e.g., `abc1d2ef`) which you'll use this to call the model API.
* **Deployment ID**: The string after `/logs/` (e.g., `xyz123`) identifies this specific deployment.

You can also find your model ID in [your Baseten dashboard](https://app.baseten.co/models/) by clicking on your model.

***

## Call the model API

After the deployment is complete, you can call the model API:

<Tabs>
  <Tab title="Truss CLI">
    From your Truss project directory, run:

    ```sh theme={"system"}
    truss predict --data '{"messages": [{"role": "user", "content": "What is AGI?"}]}'
    ```

    The expected output is:

    ```output theme={"system"}
    Calling predict on development deployment...
    {
      "output": "AGI stands for Artificial General Intelligence..."
    }
    ```

    The Truss CLI uses your saved credentials and automatically targets the correct deployment.
  </Tab>

  <Tab title="cURL">
    Set your API key and replace `YOUR_MODEL_ID` with your model ID (e.g., `abc1d2ef`):

    ```sh theme={"system"}
    export BASETEN_API_KEY=YOUR_API_KEY

    curl -X POST https://model-YOUR_MODEL_ID.api.baseten.co/development/predict \
      -H "Authorization: Api-Key $BASETEN_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"messages": [{"role": "user", "content": "What is AGI?"}]}'
    ```

    The expected output is:

    ```output theme={"system"}
    {'output': 'AGI stands for Artificial General Intelligence...'}
    ```
  </Tab>

  <Tab title="Python">
    Set your API key as an environment variable, then replace `YOUR_MODEL_ID` with your model ID:

    ```sh theme={"system"}
    export BASETEN_API_KEY=YOUR_API_KEY
    ```

    ```python main.py theme={"system"}
    import requests
    import os

    model_id = "YOUR_MODEL_ID"  # Replace with your model ID (e.g., "abc1d2ef")
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    resp = requests.post(
        f"https://model-{model_id}.api.baseten.co/development/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "messages": [
                {"role": "user", "content": "What is AGI?"}
            ]
        }
    )

    print(resp.json())
    ```

    The expected output is:

    ```output theme={"system"}
    {'output': 'AGI stands for Artificial General Intelligence...'}
    ```
  </Tab>
</Tabs>

***

## Use live reload for development

To avoid long deploy times when testing changes, use **live reload**:

```sh theme={"system"}
truss watch
```

The expected output is:

```output theme={"system"}
🪵  View logs for your deployment at https://app.baseten.co/models/<model_id>/logs/<deployment_id>
🚰 Attempting to sync truss with remote
No changes observed, skipping patching.
👀 Watching for changes to truss...
```

When you save changes to `model.py`, Truss automatically patches the deployed model:

```output theme={"system"}
Changes detected, creating patch...
Created patch to update model code file: model/model.py
Model Phi 3 Mini patched successfully.
```

This saves time by patching only the updated code without rebuilding Docker containers or restarting the model server.

***

## Promote to production

Once you're happy with the model, deploy it to production:

```sh theme={"system"}
truss push --publish
```

This changes the API endpoint from `/development/predict` to `/production/predict`:

```sh theme={"system"}
curl -X POST https://model-YOUR_MODEL_ID.api.baseten.co/production/predict \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "What is AGI?"}]}'
```

<Tip>
  To call your production endpoint, you need your model ID. The output of `truss push --publish` includes a logs URL:

  ```output theme={"system"}
  🪵  View logs for your deployment at https://app.baseten.co/models/abc1d2ef/logs/xyz123
  ```

  Your model ID is the string after `/models/` (e.g., `abc1d2ef`). You can also find it in your [Baseten dashboard](https://app.baseten.co/models/).
</Tip>

***

## Next steps

Now that you've deployed your first model, continue learning:

* [Model serving with Truss](/development/model/overview): Configure dependencies, secrets, and resources.
* [Example implementations](https://github.com/basetenlabs/truss-examples): Deploy dozens of open source models.
* [Autoscaling settings](/deployment/autoscaling): Scale GPU replicas based on demand.


# Dockerized model
Source: https://docs.baseten.co/examples/docker

Deploy any model in a pre-built Docker container

<Card title="View on GitHub" icon="github" href="https://github.com/basetenlabs/truss-examples/tree/main/custom-server/infinity-embedding-server" />

In this example, we deploy a dockerized model for [infinity embedding server](https://github.com/michaelfeil/infinity), a high-throughput, low-latency REST API server for serving vector embeddings.

# Setting up the `config.yaml`

To deploy a dockerized model, all you need is a `config.yaml`. It specifies how to build your Docker image, start the server, and manage resources. Let’s break down each section.

## Base Image

Sets the foundational Docker image to a lightweight Python 3.11 environment.

```yaml config.yaml theme={"system"}
base_image:
  image: python:3.11-slim
```

## Docker Server Configuration

Configures the server's startup command, health check endpoints, prediction endpoint, and the port on which the server will run.

```yaml config.yaml theme={"system"}
docker_server:
  start_command: sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) infinity_emb v2 --batch-size 64 --model-id BAAI/bge-small-en-v1.5 --revision main"
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /embeddings
  server_port: 7997
```

## Build Commands (Optional)

Pre-downloads model weights during the build phase to ensure the model is ready at container startup.

```yaml config.yaml theme={"system"}
build_commands: # optional step to download the weights of the model into the image
  - sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) infinity_emb v2 --preload-only --no-model-warmup --model-id BAAI/bge-small-en-v1.5 --revision main"
```

## Configure resources

Note that we need an L4 to run this model.

```yaml config.yaml theme={"system"}
resources:
  accelerator: L4
  use_gpu: true
```

## Requirements

Lists the Python package dependencies required for the infinity embedding server.

```yaml config.yaml theme={"system"}
requirements:
  - infinity-emb[all]==0.0.72
```

## Runtime Settings

Sets the server to handle up to 40 concurrent inferences to manage load efficiently.

```yaml config.yaml theme={"system"}
runtime:
  predict_concurrency: 40
```

## Environment Variables

Defines essential environment variables including the Hugging Face access token, request batch size, queue size limit, and a flag to disable tracking.

```yaml config.yaml theme={"system"}
environment_variables:
  hf_access_token: null
  # constrain api to at most 256 sentences per request, for better load-balancing
  INFINITY_MAX_CLIENT_BATCH_SIZE: 256
  # constrain model to a max backpressure of INFINITY_MAX_CLIENT_BATCH_SIZE * predict_concurrency = 10241 requests
  INFINITY_QUEUE_SIZE: 10241
  DO_NOT_TRACK: 1
```

# Deploy dockerized model

Deploy the model like you would other Trusses, with:

```bash theme={"system"}
truss push infinity-embedding-server --publish
```


# Image generation
Source: https://docs.baseten.co/examples/image-generation

Building a text-to-image model with Flux Schnell

<Card title="View example on GitHub" icon="github" href="https://github.com/basetenlabs/truss-examples/tree/main/04-image-generation" />

In this example, we go through a Truss that serves a text-to-image model. We
use Flux Schnell, which is one of the highest performing text-to-image models out
there today.

# Set up imports and torch settings

In this example, we use the Hugging Face diffusers library to build our text-to-image model.

```python model/model.py theme={"system"}
import base64
import random
import logging
from io import BytesIO

import numpy as np
import torch
from diffusers import FluxPipeline
from PIL import Image

logging.basicConfig(level=logging.INFO)
MAX_SEED = np.iinfo(np.int32).max
```

# Define the `Model` class and load function

In the `load` function of the Truss, we implement logic involved in
downloading and setting up the model. For this model, we use the
`FluxPipeline` class in `diffusers` to instantiate our Flux pipeline,
and configure a number of relevant parameters.

See the [diffusers docs](https://huggingface.co/docs/diffusers/index) for details
on all of these parameters.

```python model/model.py theme={"system"}
class Model:
    def __init__(self, **kwargs):
        self.pipe = None
        self.repo_id = "black-forest-labs/FLUX.1-schnell"

    def load(self):
        self.pipe = FluxPipeline.from_pretrained(self.repo_id, torch_dtype=torch.bfloat16).to("cuda")
```

This is a utility function for converting a PIL image to base64.

```python model/model.py theme={"system"}
    def convert_to_b64(self, image: Image) -> str:
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_b64

```

# Define the predict function

The `predict` function contains the actual inference logic. The steps here are:

* Setting up the generation params. These include things like the prompt, image width, image height, number of inference steps, etc.
* Running the Diffusion Pipeline
* Convert the resulting image to base64 and return it

```python model/model.py theme={"system"}
    def predict(self, model_input):
        seed = model_input.get("seed")
        prompt = model_input.get("prompt")
        prompt2 = model_input.get("prompt2")
        max_sequence_length = model_input.get(
            "max_sequence_length", 256
        )  # 256 is max for FLUX.1-schnell
        guidance_scale = model_input.get(
            "guidance_scale", 0.0
        )  # 0.0 is the only value for FLUX.1-schnell
        num_inference_steps = model_input.get(
            "num_inference_steps", 4
        )  # schnell is timestep-distilled
        width = model_input.get("width", 1024)
        height = model_input.get("height", 1024)
        if not math.isclose(guidance_scale, 0.0):
            logging.warning(
                "FLUX.1-schnell does not support guidance_scale other than 0.0"
            )
            guidance_scale = 0.0
        if not seed:
            seed = random.randint(0, MAX_SEED)
        if len(prompt.split()) > max_sequence_length:
            logging.warning(
                "FLUX.1-schnell does not support prompts longer than 256 tokens, truncating"
            )
            tokens = prompt.split()
            prompt = " ".join(tokens[: min(len(tokens), max_sequence_length)])
        generator = torch.Generator().manual_seed(seed)

        image = self.pipe(
            prompt=prompt,
            guidance_scale=guidance_scale,
            max_sequence_length=max_sequence_length,
            num_inference_steps=num_inference_steps,
            width=width,
            height=height,
            output_type="pil",
            generator=generator,
        ).images[0]

        b64_results = self.convert_to_b64(image)
        return {"data": b64_results}

```

# Setting up the `config.yaml`

Running Flux Schnell requires a handful of Python libraries, including
`diffusers`, `transformers`, and others.

```yaml config.yaml theme={"system"}
external_package_dirs: []
model_cache:
  - repo_id: black-forest-labs/FLUX.1-schnell
    allow_patterns:
      - "*.json"
      - "*.safetensors"
    ignore_patterns:
      - "flux1-schnell.safetensors"
model_metadata:
  example_model_input: {"prompt": 'black forest gateau cake spelling out the words "FLUX SCHNELL", tasty, food photography, dynamic shot'}
model_name: Flux.1-schnell
python_version: py311
requirements:
  - git+https://github.com/huggingface/diffusers.git@v0.32.2
  - transformers
  - accelerate
  - sentencepiece
  - protobuf
resources:
  accelerator: H100_40GB
  use_gpu: true
secrets: {}
system_packages:
  - ffmpeg
  - libsm6
  - libxext6
```

## Configuring resources for Flux Schnell

Note that we need an H100 40GB GPU to run this model.

```yaml config.yaml theme={"system"}
resources:
  accelerator: H100_40GB
  use_gpu: true
secrets: {}
```

## System Packages

Running diffusers requires `ffmpeg` and a couple other system
packages.

```yaml config.yaml theme={"system"}
system_packages:
  - ffmpeg
  - libsm6
  - libxext6
```

## Enabling Caching

Flux Schnell is a large model, and downloading it could take several minutes. This means
that the cold start time for this model is long. We can solve that by using our build
caching feature. This moves the model download to the build stage of your model--
caching the model will take about 15 minutes initially but you will get \~20s cold starts
subsequently.

To enable caching, add the following to the config:

```yaml theme={"system"}
model_cache:
  - repo_id: black-forest-labs/FLUX.1-schnell
    allow_patterns:
      - "*.json"
      - "*.safetensors"
    ignore_patterns:
      - "flux1-schnell.safetensors"
```

# Deploy the model

Deploy the model like you would other Trusses, with:

```bash theme={"system"}
truss push flux/schnell --publish
```

# Run an inference

Use a Python script to call the model once its deployed and parse its response. We parse the resulting base64-encoded string output into an actual image file: `output_image.jpg`.

```python infer.py theme={"system"}
import httpx
import os
import base64
from PIL import Image
from io import BytesIO

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

# Function used to convert a base64 string to a PIL image
def b64_to_pil(b64_str):
    return Image.open(BytesIO(base64.b64decode(b64_str)))

data = {
  "prompt": 'red velvet cake spelling out the words "FLUX SCHNELL", tasty, food photography, dynamic shot'
}

# Call model endpoint
res = httpx.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Get output image
res = res.json()
output = res.get("data")

# Convert the base64 model output to an image
img = b64_to_pil(output)
img.save("output_image.jpg")
```


# Deepseek R1
Source: https://docs.baseten.co/examples/models/deepseek/deepseek-r1

A state-of-the-art 671B-parameter MoE LLM with o1-style reasoning licensed for commercial use

<DeepSeekIconCard title="Deploy Deepseek R1" href="https://www.baseten.co/talk-to-us/deepseek/" />

# Example usage

DeepSeek-R1 is optimized using SGLang and uses an OpenAI-compatible API endpoint.

## Input

```python theme={"system"}
import httpx
import os

MODEL_ID = "abcd1234"  # Replace this with your model ID
DEPLOYMENT_ID = "abcd1234"  # [Optional] Replace this with your deployment ID
API_KEY = os.environ["BASETEN_API_KEY"]

resp = httpx.post(
    f"https://model-{MODEL_ID}.api.baseten.co/environments/production/sync/v1/chat/completions",
    headers={"Authorization": f"Api-Key {API_KEY}"},
    json={
        "model": "deepseek_v3",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": "What weighs more, a pound of bricks or a pound of feathers?"},
        ],
        "max_tokens": 1024,
    },
    timeout=None
)

print(resp.json())
```

## Output

```json theme={"system"}
{
  "id": "8456fe51db3548789f199cfb8c8efd35",
  "object": "text_completion",
  "created": 1735236968,
  "model": "/models/deepseek_r1",
  "choices": [
    {
      "index": 0,
      "text": "Let's think through this step by step...",
      "logprobs": null,
      "finish_reason": "stop",
      "matched_stop": 1
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "total_tokens": 240,
    "completion_tokens": 226,
    "prompt_tokens_details": null
  }
}
```


# DeepSeek-R1 Qwen 7B
Source: https://docs.baseten.co/examples/models/deepseek/deepseek-r1-qwen-7b

Qwen 7B fine-tuned for CoT reasoning capabilities with DeepSeek R1

<DeepSeekIconCard title="Deploy DeepSeek-R1 Qwen 7B" href="https://app.baseten.co/deploy/deepseek-r1-qwen-7b" />

# Example usage

The fine-tuned version of Qwen is OpenAI compatible and can be called using the OpenAI client.

```python theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "user", "content": "Which weighs more, a pound of bricks or a pound of feathers?"},
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

# JSON output

```json theme={"system"}
["streaming", "output", "text"]
```


# Flux-Schnell
Source: https://docs.baseten.co/examples/models/flux/flux-schnell

Flux-Schnell is a state-of-the-art image generation model

<BFLIconCard title="Deploy Flux-Schnell" href="https://app.baseten.co/deploy/flux.1-schnell" />

## Example usage

The model accepts a `prompt` which is some text describing the image you want to generate. The output images tend to get better as you add more descriptive words to the prompt.

The output JSON object contains a key called `data` which represents the generated image as a base64 string.

### Input

```python theme={"system"}
import httpx
import os
import base64
from PIL import Image
from io import BytesIO
# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
# Function used to convert a base64 string to a PIL image
def b64_to_pil(b64_str):
    return Image.open(BytesIO(base64.b64decode(b64_str)))
data = {
  "prompt": 'red velvet cake spelling out the words "FLUX SCHNELL", tasty, food photography, dynamic shot'
}
# Call model endpoint
res = httpx.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)
# Get output image
res = res.json()
output = res.get("data")
# Convert the base64 model output to an image
img = b64_to_pil(output)
img.save("output_image.jpg")
```

### JSON output

```json theme={"system"}
{
  "output": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAA..."
}
```


# Gemma 3 27B IT
Source: https://docs.baseten.co/examples/models/gemma/gemma-3-27b-it

Instruct-tuned open model by Google with excellent ELO/size tradeoff and vision capabilities

<GoogleIconCard title="Deploy Gemma 3 27B IT" href="https://app.baseten.co/deploy/gemma_3_27b_it" />

# Example usage

Gemma 3 is an OpenAI-compatible model and can be called using the OpenAI SDK in any language.

```python theme={"system"}
from openai import OpenAI
import os

model_url = "" # Copy in from API pane in Baseten model dashboard

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url=model_url
)

# Chat completion
response_chat = client.chat.completions.create(
    model="",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://picsum.photos/id/237/200/300",
                },
            },
        ],
    }],
    temperature=0.3,
    max_tokens=512,
)
print(response_chat)
```

**JSON Output**

```json theme={"system"}
{
  "id": "143",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "[Model output here]",
        "role": "assistant",
        "audio": null,
        "function_call": null,
        "tool_calls": null
      }
    }
  ],
  "created": 1741224586,
  "model": "",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": null,
  "usage": {
    "completion_tokens": 145,
    "prompt_tokens": 38,
    "total_tokens": 183,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  }
}
```


# Kokoro
Source: https://docs.baseten.co/examples/models/kokoro/kokoro

Kokoro is a frontier TTS model for its size of 82 million parameters (text in/audio out).

<LibraryIconCard title="Deploy Kokoro" href="https://app.baseten.co/deploy/kokoro" />

## Example usage

Kokoro uses the following request and response format:

```
request:
{"text": "Hello", "voice": "af", "speed": 1.0}

text: str = defaults to "Hi, I'm kokoro"
voice: str = defaults to "af", available options: "af", "af_bella", "af_sarah", "am_adam", "am_michael", "bf_emma", "bf_isabella", "bm_george", "bm_lewis", "af_nicole", "af_sky"
speed: float = defaults to 1.0. The speed of the audio generated

response:
{"base64": "base64 encoded bytestring"}
```

```python theme={"system"}
import httpx
import base64

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

with httpx.Client() as client:
    # Make the API request
    resp = client.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {API_KEY}"},
        json={"text": "Hello world", "voice": "af", "speed": 1.0},
        timeout=None,
    )

# Get the base64 encoded audio
response_data = resp.json()
audio_base64 = response_data["base64"]

# Decode the base64 string
audio_bytes = base64.b64decode(audio_base64)

# Write to a WAV file
with open("output.wav", "wb") as f:
    f.write(audio_bytes)

print("Audio saved to output.wav")
```

**JSON Output**

```json theme={"system"}
null
```


# Llama 3.3 70B Instruct
Source: https://docs.baseten.co/examples/models/llama/llama-3.3-70B-instruct

Llama 3.3 70B Instruct is a large language model that is optimized for instruction following.

<MetaIconCard title="Deploy Llama 3.3 70B Instruct" href="https://app.baseten.co/deploy/llama-3-3-70b-instruct" />

# Example usage

Llama is OpenAI compatible and can be called using the OpenAI client.

```python theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What was the role of Llamas in the Inca empire?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

**JSON Output**

```json theme={"system"}
["streaming", "output", "text"]
```


# MARS6
Source: https://docs.baseten.co/examples/models/mars/MARS6

MARS6 is a frontier text-to-speech model by CAMB.AI with voice/prosody cloning capabilities in 10 languages. MARS6 must be licensed for commercial use, we can help!

<MarsIconCard title="Deploy MARS6" href="https://app.baseten.co/deploy/mars-6r-tts" />

## Example usage

This model requires at least four inputs:

1. `text`: The input text that needs to be spoken
2. `audio_ref`: An audio file containing the audio of a single person
3. `ref_text`: What is spoken in audio\_ref
4. `language`: The language code for the target language

The model will try to output an audio stream containing the speech in the reference audio's style. The output is by default an HTTP1.1 chunked encoding response of an encoded audio file using an ADTS AAC stream, but can be configured to stream using flac format, or to not stream at all and return the entire response as a base64 encoded flac file.

```
data = {"text": "The quick brown fox jumps over the lazy dog",
        "audio_ref": encoded_str,
        "ref_text": prompt_txt,
        "language": 'en-us', # Target language, in this case english.
        # "top_p": 0.7, # Optionally specify a top_p (default 0.7)
        # "temperature": 0.7, # Optionally specify a temperature (default 0.7)
        # "chunk_length": 200, # Optional text chunk length for splitting long pieces of input text. Default 200
        # "max_new_tokens": 0, # Optional limit on max number of new tokens, default is zero (unlimited)
        # "repetition_penalty": 1.5 # Optional rep penalty, default 1.5
}
```

## Input

```python theme={"system"}
import base64
import time
import torchaudio
import requests
import IPython.display as ipd
import librosa, librosa.display
import torch
import io
from torchaudio.io import StreamReader

# Step 1: set endpoint url and api key:
url = "<YOUR PREDICTION ENDPOINT>"
headers = {"Authorization": "Api-Key <YOUR API KEY>"}

# Step 2: pick reference audio to clone, encode it as base64
file_path = "ref_debug.flac"  # any valid audio filepath, ideally between 6s-90s.
wav, sr = librosa.load(file_path, sr=None, mono=True, offset=0, duration=5)
io_data = io.BytesIO()
torchaudio.save(io_data, torch.from_numpy(wav)[None], sample_rate=sr, format="wav")
io_data.seek(0)
encoded_data = base64.b64encode(io_data.read())
encoded_str = encoded_data.decode("utf-8")
# OPTIONAL: specify the transcript of the reference/prompt (slightly speeds up inference, and may make it sound a bit better).
prompt_txt = None  # if unspecified, can be left as None

# Step 3: define other inference settings:
data = {
    "text": "The quick brown fox jumps over the lazy dog",
    "audio_ref": encoded_str,
    "ref_text": prompt_txt,
    "language": "en-us",  # Target language, in this case english.
    # "top_p": 0.7, # Optionally specify a top_p (default 0.7)
    # "temperature": 0.7, # Optionally specify a temperature (default 0.7)
    # "chunk_length": 200, # Optional text chunk length for splitting long pieces of input text. Default 200
    # "max_new_tokens": 0, # Optional limit on max number of new tokens, default is zero (unlimited)
    # "repetition_penalty": 1.5 # Optional rep penalty, default 1.5
    # stream: bool = True # whether to stream the response back as an HTTP1.1 chunked encoding response, or run to completion and return the base64 encoded file.
    # stream_format: str = "adts" # 'adts' or 'flac' for stream format. Default 'adts'
}

st = time.time()


class UnseekableWrapper:
    def __init__(self, obj):
        self.obj = obj

    def read(self, n):
        return self.obj.read(n)


# Step 4: Send the POST request (note the first request might be a bit slow, but following requests should be fast)
response = requests.post(url, headers=headers, json=data, stream=True, timeout=300)
streamer = StreamReader(UnseekableWrapper(response.raw))
streamer.add_basic_audio_stream(
    11025, buffer_chunk_size=3, sample_rate=44100, num_channels=1
)

# Step 4.1: check the header format of the returned stream response
for i in range(streamer.num_src_streams):
    print(streamer.get_src_stream_info(i))

# Step 5: stream the response back and decode it on-the-fly
audio_samples = []
for chunks in streamer.stream():
    audio_chunk = chunks[0]
    audio_samples.append(
        audio_chunk._elem.squeeze()
    )  # this is now just a (T,) float waveform, however you can set your own output format bove.
    print(
        f"Playing audio chunk of size {audio_chunk._elem.squeeze().shape} at {time.time() - st:.2f}s."
    )
    # If you wish, you can also play each chunk as you receive it, e.g. using IPython:
    # ipd.display(ipd.Audio(audio_chunk._elem.squeeze().numpy(), rate=44100, autoplay=True))

# Step 6: concatenate all the audio chunks and play the full audio (if you didn't play them on the fly above)
final_full_audio = torch.concat(audio_samples, dim=0)  # (T,) float waveform @ 44.1kHz
# ipd.display(ipd.Audio(final_full_audio.numpy(), rate=44100))
```

## Output

```json theme={"system"}
{
    "reuslt": "base64 encoded audio data",\
}
```


# All MPNet Base V2
Source: https://docs.baseten.co/examples/models/microsoft/all-mpnet-base-v2

A text embedding model with a context window of 384 tokens and a dimensionality of 768 values.

<MicrosoftIconCard title="Deploy All MPNet Base V2" href="https://app.baseten.co/deploy/all-mpnet-base-v2" />

## Example usage

This model takes a list of strings and returns a list of embeddings, where each embedding is a list of 768 floating-point number representing the semantic text embedding of the associated string.

Strings can be up to 384 tokens in length (approximately 280 words). If the strings are longer, they'll be truncated before being run through the embedding model.

```python theme={"system"}
import requests
import os

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

data = {
    "text": ["I want to eat pasta", "I want to eat pizza"],
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Print the output of the model
print(res.json())
```

## JSON output

```json theme={"system"}
[
  [0.2593194842338562, "...", -1.4059709310531616],
  [0.11028853803873062, "...", -0.9492666125297546]
]
```


# Nomic Embed v1.5
Source: https://docs.baseten.co/examples/models/nomic/nomic-embed-v1-5

SOTA text embedding model with variable dimensionality — outperforms OpenAI text-embedding-ada-002 and text-embedding-3-small models.

<NomicIconCard title="Deploy Nomic Embed v1.5" href="https://app.baseten.co/deploy/nomic_embed_v1_5?_gl=1*dnaf1c*_gcl_au*MTYzMTk5MDI1OS4xNzM2NjM4OTMw" />

## Example usage

Nomic Embed v1.5 is a state of the art text embedding model with two special features:

* You can choose whether to optimize the embeddings for retrieval, search, clustering, or classification.
* You can trade off between cost and accuracy by choosing your own dimensionality thanks to Matryoshka Representation Learning.

Nomic Embed v1.5 takes the following parameters:

* `texts` the strings to embed.
* `task_type` the task to optimize the embedding for. Can be `search_document` (default), `search_query`, `clustering`, or `classification`.
* `dimensionality` the size of each output vector, any integer between `64` and `768` (default).

This code sample demonstrates embedding a set of sentences for retrieval with a dimensionality of 512.

```python theme={"system"}
import requests
import os

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

data = {
    "texts": ["I want to eat pasta", "I want to eat pizza"],
    "task_type": "search_document",
    "dimensionality": 512
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Print the output of the model
print(res.json())
```

## JSON output

```json theme={"system"}
[
  [-0.03811980411410332, "...", -0.023593541234731674],
  [-0.042617011815309525, "...", -0.0191882885992527]
]
```


# Overview
Source: https://docs.baseten.co/examples/models/overview

Browse our library of open source models that are ready to deploy behind an API endpoint in seconds.

## Featured models

<CardGroup>
  <DeepSeekIconCard title="DeepSeek R1" href="/examples/models/deepseek/deepseek-r1" />

  <OpenAIIconCard title="Whisper V3" href="/examples/models/whisper/whisper-v3-fastest" />

  <QwenIconCard title="Qwen 2.5 32B Coder Instruct" href="/examples/models/qwen/qwen-2-5-32b-coder-instruct" />

  <MetaIconCard title="Llama 3.3 70B Instruct" href="/examples/models/llama/llama-3.3-70B-instruct" />

  <BFLIconCard title="flux-schnell" href="/examples/models/flux/flux-schnell" />

  <GoogleIconCard title="Gemma 3 27B IT" href="/examples/models/gemma/gemma-3-27b-it" />

  <MarsIconCard title="MARS6" href="/examples/models/mars/MARS6" />
</CardGroup>


# Qwen-2-5-32B-Coder-Instruct
Source: https://docs.baseten.co/examples/models/qwen/qwen-2-5-32b-coder-instruct

Qwen 2.5 32B Coder is an OpenAI-compatible model and can be called using the OpenAI SDK in any language.

<QwenIconCard title="Deploy Qwen 2.5 32B Coder Instruct" href="https://app.baseten.co/deploy/qwen-2-5-32b-coder-instruct" />

## Example usage

```python theme={"system"}
from openai import OpenAI
import os

model_url = "" # Copy in from API pane in Baseten model dashboard

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url=model_url
)

# Chat completion
response_chat = client.chat.completions.create(
    model="",
    messages=[
        {"role": "user", "content": "Tell me a fun fact about Python."}
    ],
    temperature=0.3,
    max_tokens=100,
)
print(response_chat)
```

## JSON output

```json theme={"system"}
{
  "id": "143",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "[Model output here]",
        "role": "assistant",
        "audio": null,
        "function_call": null,
        "tool_calls": null
      }
    }
  ],
  "created": 1741224586,
  "model": "",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": null,
  "usage": {
    "completion_tokens": 145,
    "prompt_tokens": 38,
    "total_tokens": 183,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  }
}
```


# SDXL Lightning
Source: https://docs.baseten.co/examples/models/stable-diffusion/sdxl-lightning

A variant of Stable Diffusion XL that generates 1024x1024 px images in 4 UNet steps, enabling near real-time image creation.

<LightningIconCard title="Deploy SDXL Lightning" href="https://app.baseten.co/deploy/sdxl_lightning" />

# Example usage

The model accepts a single input, prompt, and returns a base64 string of the image as the key `result`.

This implementation uses the 4-step UNet checkpoint to balance speed and quality. You can [deploy your own version](https://github.com/basetenlabs/truss-examples/tree/main/stable-diffusion/sdxl-lightning) with either 2 steps for even faster results or 8 steps for even higher quality.

```python theme={"system"}
import base64
import requests
import os

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
BASE64_PREAMBLE = "data:image/png;base64,"

data = {
    "prompt": "a picture of a rhino wearing a suit",
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Get output image
res = res.json()
img_b64 = res.get("result")
img = base64.b64decode(img_b64)

# Save the base64 string to a PNG
img_file = open("sdxl-output-1.png", "wb")
img_file.write(img)
img_file.close()
os.system("open sdxl-output-1.png")
```

**JSON Output**

```json theme={"system"}
{
  "result": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAA..."
}
```


# Whisper V3
Source: https://docs.baseten.co/examples/models/whisper/whisper-v3-fastest

Whisper V3 is a fast and accurate speech recognition model.

<OpenAIIconCard title="Deploy Whisper V3" href="https://www.baseten.co/talk-to-us/?ref=model-library-whisper&model=the%20world%27s%20fastest%20Whisper%20inference" />

# Example usage

Transcribe audio files at up to a 400x real-time factor — that's 1 hour of audio in under 9 seconds. This setup requires meaningful production traffic to be cost-effective, but at scale it's at least 80% cheaper than OpenAI. [Get in touch with us](https://www.baseten.co/talk-to-us/?ref=model-library-whisper\&model=the%20world%27s%20fastest%20Whisper%20inference) and we'll work with you to deploy a transcription pipeline that's customized to match your needs.

For quick deployments of Whisper suitable for shorter audio files and lower traffic volume, you can deploy Whisper V3 and Whisper V3 Turbo directly from the model library.

```python theme={"system"}
import requests
import os

# Model ID for production deployment
model_id = ""
# Read secrets from environment variables
baseten_api_key = os.environ["BASETEN_API_KEY"]

# Call model endpoint
resp = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={
      "url": "https://www2.cs.uic.edu/~i101/SoundFiles/gettysburg10.wav",
    }
)

print(resp.content.decode("utf-8"))
```

**JSON Output**

```json theme={"system"}
{
  "segments": [
    {
      "start": 0,
      "end": 9.8,
      "text": "Four score and seven years ago, our fathers brought forth on this continent a new nation, conceived in liberty and dedicated to the proposition that all men are created equal."
    }
  ],
  "language_code": "en"
}
```


# Building with Baseten
Source: https://docs.baseten.co/examples/overview



These examples cover a variety of use cases on Baseten, from [deploying your first LLM](/examples/deploy-your-first-model) and [image generation](/examples/image-generation) to [transcription](/examples/chains-audio-transcription), [embeddings](/examples/bei), and [RAG pipelines](/examples/chains-build-rag). Whether you're optimizing inference with [TensorRT-LLM](/examples/tensorrt-llm) or deploying a model with [Truss](/development/model/overview), these guides help you build and scale efficiently.

## Choosing the right engine

Not sure which engine to use? Check out our [engine documentation](/engines) to:

* **Select the appropriate engine** for your model architecture (embeddings, dense LLMs, or MoE models)
* **Understand performance trade-offs** between different engine options
* **Configure advanced features** like quantization and speculative decoding
* **Optimize for your specific use case** with engine-specific guidance

## Featured examples

<CardGroup>
  <Card title="Deploy your first model" href="/examples/deploy-your-first-model" />

  <Card title="Fast LLMs with TensorRT-LLM" href="/examples/tensorrt-llm" />

  <Card title="Run any LLM with vLLM" href="/examples/vllm" />

  <Card title="Deploy LLMs with SGLang" href="/examples/sglang" />

  <Card title="Transcribe audio with a Chain" href="/examples/chains-audio-transcription" />

  <Card title="Embeddings with BEI" href="/examples/bei" />
</CardGroup>

## Model library

For a **quick start**, explore the [model library](/examples/models/overview) with prebuilt, ready to deploy in one click models like DeepSeek, Llama, and Qwen.

<CardGroup>
  <DeepSeekIconCard title="DeepSeek R1" href="/examples/models/deepseek/deepseek-r1" />

  <OpenAIIconCard title="Whisper V3" href="/examples/models/whisper/whisper-v3-fastest" />

  <QwenIconCard title="Qwen 2.5 32B Coder Instruct" href="/examples/models/qwen/qwen-2-5-32b-coder-instruct" />

  <MetaIconCard title="Llama 3.3 70B Instruct" href="/examples/models/llama/llama-3.3-70B-instruct" />

  <BFLIconCard title="flux-schnell" href="/examples/models/flux/flux-schnell" />

  <MarsIconCard title="MARS6" href="/examples/models/mars/MARS6" />
</CardGroup>

## Training

Train and fine-tune models with Baseten's scalable training infrastructure. From [fine-tuning large language models](/training/getting-started) to training custom models, our platform provides the tools and compute you need.

<CardGroup>
  <OpenAIIconCard title="GPT OSS 20B with LoRA" href="https://github.com/basetenlabs/ml-cookbook/tree/main/examples/oss-gpt-20b-axolotl/training" />

  <MetaIconCard title="Llama 3.1 8B SFT" href="https://github.com/basetenlabs/ml-cookbook/tree/main/examples/llama-8b-lora-unsloth/training" />

  <QwenIconCard title="Long Context Qwen3-30B" href="https://github.com/basetenlabs/ml-cookbook/tree/main/recipes/sft/long_context" />

  <QwenIconCard title="Coding with Qwen3-8B" href="https://github.com/basetenlabs/ml-cookbook/tree/main/recipes/rl/ocaml_sepcialist" />
</CardGroup>

Our training infrastructure supports popular frameworks including VERL, Megatron, and Unsloth, as well as models trained directly with Hugging Face Transformers.


# Deploy LLMs with SGLang
Source: https://docs.baseten.co/examples/sglang

Optimized inference for LLMs with SGLang

Another great option for inference is [SGLang](https://docs.sglang.ai/), which supports a wide range of models and performance optimizations. Besides TensorRT-LLM it is in many cases the state-of-the-art engine for serving LLMs.

## Example: Deploy Qwen 2.5 3B on an L4 via SGLang

This configuration serves [Qwen 2.5 3B](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) with SGLang on an L4 GPU. Running this model is fast and cheap, making it a good example for documentation, but the process of deploying it is very similar to larger models like [Llama 3.3 70B](/examples/models/llama/llama-3.3-70B-instruct).

## Setup

Before you deploy a model, you'll need three quick setup steps.

<Steps>
  <Step title="Create an API key for your Baseten account">
    Create an [API key](https://app.baseten.co/settings/api_keys) and save it as an environment variable:

    ```sh theme={"system"}
    export BASETEN_API_KEY="abcd.123456"
    ```
  </Step>

  <Step title="Add an access token for Hugging Face">
    Some models require that you accept terms and conditions on Hugging Face before deployment. To prevent issues:

    1. Accept the license for any gated models you wish to access, like [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct).
    2. Create a read-only [user access token](https://huggingface.co/docs/hub/en/security-tokens) from your Hugging Face account.
    3. Add the `hf_access_token` secret [to your Baseten workspace](https://app.baseten.co/settings/secrets).
  </Step>

  <Step title="Install Truss in your local development environment">
    Install the latest version of Truss, our open-source model packaging framework, as well as OpenAI's model inference SDK, with:

    ```sh theme={"system"}
    pip install --upgrade truss openai
    ```
  </Step>
</Steps>

## Configuration

Start with an empty configuration file.

```sh theme={"system"}
mkdir qwen-2-5-3b-engine
touch qwen-2-5-3b-engine/config.yaml
```

Below is an example for Qwen 2.5 3B. You can copy-paste it into the empty `config.yaml` we created above.

```yaml config.yaml theme={"system"}
model_metadata:
  example_model_input: # Loads sample request into Baseten playground
    messages:
      - role: system
        content: "You are a helpful assistant."
      - role: user
        content: "What does Tongyi Qianwen mean?"
    stream: true
    model: "baseten-sglang"
    max_tokens: 512
    temperature: 0.6
  tags:
    - openai-compatible
model_name: Qwen 2.5 3B SGLang
environment_variables:
  hf_access_token: null
base_image:
  image: lmsysorg/sglang:v0.4.4.post1-cu125
docker_server:
  start_command: sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) python3 -m sglang.launch_server --model-path Qwen/Qwen2.5-3B-Instruct --host 0.0.0.0 --port 8000"
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /v1/chat/completions
  server_port: 8000
resources:
  accelerator: L4
  use_gpu: true
runtime:
  predict_concurrency: 32
```

## Deployment

Pushing the model to Baseten kicks off a multi-stage deployment process.

```sh theme={"system"}
truss push qwen-2-5-3b-engine --publish
```

Upon deployment, check your terminal logs or Baseten account to find the URL for the model server.

## Inference

This model is OpenAI compatible and can be called using the OpenAI client.

```python call_model.py theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What does Tongyi Qianwen mean?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

That's it! You have successfully deployed and called a model using SGLang.


# Speculative Decoding Examples
Source: https://docs.baseten.co/examples/speculative-decoding

Lookahead decoding configurations for faster inference

Speculative decoding with [lookahead decoding](/engines/engine-builder-llm/lookahead-decoding) accelerates inference for predictable workloads using n-gram patterns.

## Quick start

```yaml theme={"system"}
trt_llm:
  build:
    speculator:
      enable_b10_lookahead: true
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 8
      lookahead_ngram_size: 1
      lookahead_verification_set_size: 1
```

## Engine compatibility

| Feature                | [Engine-Builder-LLM](/engines/engine-builder-llm/overview) | [BIS-LLM](/engines/bis-llm/overview) |
| ---------------------- | ---------------------------------------------------------- | ------------------------------------ |
| **Lookahead decoding** | ✅ Supported                                                | ✅ Gated Feature                      |
| **Structured outputs** | ❌ Incompatible                                             | ✅ Supported                          |
| **Tool calling**       | ❌ Incompatible                                             | ✅ Supported                          |
| **Eagle speculation**  | ❌ Not supported                                            | ✅ Gated Feature                      |

## Configuration examples

### Code generation (Qwen2.5-Coder)

```yaml theme={"system"}
model_name: Qwen2.5-Coder-7B-Lookahead
resources:
  accelerator: H100
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "Qwen/Qwen2.5-Coder-7B-Instruct"
    quantization_type: fp8_kv
    speculator:
      enable_b10_lookahead: true
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 8
      lookahead_verification_set_size: 3
```

### Large model (Llama-3.3-70B)

```yaml theme={"system"}
model_name: Llama-3.3-70B-Lookahead
resources:
  accelerator: H100:2
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      source: HF
      repo: "meta-llama/Llama-3.3-70B-Instruct"
    quantization_type: fp8_kv
    tensor_parallel_count: 2
    speculator:
      enable_b10_lookahead: true
      speculative_decoding_mode: LOOKAHEAD_DECODING
      lookahead_windows_size: 3
      lookahead_ngram_size: 5
      lookahead_verification_set_size: 3
```

## Parameter tuning

See [lookahead decoding documentation](/engines/engine-builder-llm/lookahead-decoding) for detailed parameter explanations.

**Quick guidelines:**

* **lookahead\_windows\_size**: 1-7 (set to 1 for predictable content, 3 or 5 for others.)
* **lookahead\_ngram\_size**: 4-32 (large for code, smaller for creative tasks)
* **lookahead\_verification\_set\_size**: Usually equal to lookahead\_windows\_size

## Use cases

| Use case                | lookahead\_windows\_size | lookahead\_ngram\_size | Why                            |
| ----------------------- | ------------------------ | ---------------------- | ------------------------------ |
| **Code generation**     | 7                        | 3                      | Code patterns, smaller n-grams |
| **free form JSON/YAML** | 5                        | 5                      | Balanced for structured data   |
| **Template completion** | 7-10                     | 5-7                    | Highly predictable content     |

## Limitations

❌ **Not compatible with:**

* [Structured outputs](/engines/performance-concepts/structured-outputs) - Use BIS-LLM instead
* [Function calling](/engines/performance-concepts/function-calling) - Use BIS-LLM instead
* BIS-LLM engine - V2 stack doesn't support lookahead that is self-serviceable.

## Further reading

* [Lookahead decoding guide](/engines/engine-builder-llm/lookahead-decoding) - Complete reference config
* [Engine-Builder-LLM overview](/engines/engine-builder-llm/overview) - Dense model engine
* [BIS-LLM overview](/engines/bis-llm/overview) - MoE engine with structured outputs
* [Quantization guide](/engines/performance-concepts/quantization-guide) - Performance optimization


# LLM with Streaming
Source: https://docs.baseten.co/examples/streaming

Building an LLM with streaming output

<Card title="View on GitHub" icon="github" href="https://github.com/basetenlabs/truss-examples/tree/main/qwen/qwen-7b-chat" />

In this example, we go through a Truss that serves the Qwen 7B Chat LLM, and streams the output to the client.

# Why Streaming?

For certain ML models, generations can take a long time. Especially with LLMs, a long output could take
10-20 seconds to generate. However, because LLMs generate tokens in sequence, useful output can be
made available to users sooner. To support this, in Truss, we support streaming output.

# Set up the imports

In this example, we use the HuggingFace transformers library to build a text generation model.

```python model/model.py theme={"system"}
from threading import Thread
from typing import Dict

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from transformers.generation import GenerationConfig
```

# Define the load function

In the `load` function of the Truss, we implement logic
involved in downloading the chat version of the Qwen 7B model and loading it into memory.

```python model/model.py theme={"system"}
class Model:
    def __init__(self, **kwargs):
        self.model = None
        self.tokenizer = None

    def load(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "Qwen/Qwen-7B-Chat", trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            "Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True
        ).eval()
```

# Define the preprocess function

In the `preprocess` function of the Truss, we set up a `generate_args` dictionary with some generation arguments from the inference request to be used in the `predict` function.

```python model/model.py theme={"system"}
    def preprocess(self, request: dict) -> dict:
        generate_args = {
            "max_new_tokens": request.get("max_new_tokens", 512),
            "temperature": request.get("temperature", 0.5),
            "top_p": request.get("top_p", 0.95),
            "top_k": request.get("top_k", 40),
            "repetition_penalty": 1.0,
            "no_repeat_ngram_size": 0,
            "use_cache": True,
            "do_sample": True,
            "eos_token_id": self.tokenizer.eos_token_id,
            "pad_token_id": self.tokenizer.pad_token_id,
        }
        request["generate_args"] = generate_args
        return request
```

# Define the predict function

In the `predict` function of the Truss, we implement the actual
inference logic.

The two main steps are:

* Tokenize the input
* Call the model's `generate` function if we're not streaming the output, otherwise call the `stream` helper function

```python model/model.py theme={"system"}
    def predict(self, request: Dict):
        stream = request.pop("stream", False)
        prompt = request.pop("prompt")
        generation_args = request.pop("generate_args")
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.cuda()

        if stream:
            return self.stream(input_ids, generation_args)

        with torch.no_grad():
            output = self.model.generate(inputs=input_ids, **generation_args)
            return self.tokenizer.decode(output[0])
```

## Define the `stream` helper function

In this helper function, we'll instantiate the `TextIteratorStreamer` object, which we'll later use for
returning the LLM output to users.

```python model/model.py theme={"system"}
    def stream(self, input_ids: list, generation_args: dict):
        streamer = TextIteratorStreamer(self.tokenizer)
```

When creating the generation parameters, ensure to pass the `streamer` object
that we created previously.

```python model/model.py theme={"system"}
        generation_config = GenerationConfig(**generation_args)
        generation_kwargs = {
            "input_ids": input_ids,
            "generation_config": generation_config,
            "return_dict_in_generate": True,
            "output_scores": True,
            "max_new_tokens": generation_args["max_new_tokens"],
            "streamer": streamer,
        }
```

Spawn a thread to run the generation, so that it does not block the main
thread.

```python model/model.py theme={"system"}
        with torch.no_grad():
            # Begin generation in a separate thread
            thread = Thread(target=self.model.generate, kwargs=generation_kwargs)
            thread.start()
```

In Truss, the way to achieve streaming output is to return a generator
that yields content. In this example, we yield the output of the `streamer`,
which produces output and yields it until the generation is complete.

We define this `inner` function to create our generator.

```python model/model.py theme={"system"}
            # Yield generated text as it becomes available
            def inner():
                for text in streamer:
                    yield text
                thread.join()
        return inner()
```

# Setting up the `config.yaml`

Running Qwen 7B requires torch, transformers,
and a few other related libraries.

```yaml config.yaml theme={"system"}
model_name: qwen-7b-chat
model_metadata:
  example_model_input:
    prompt: What is the meaning of life?
requirements:
  - accelerate==0.23.0
  - tiktoken==0.5.1
  - einops==0.6.1
  - scipy==1.11.3
  - transformers_stream_generator==0.0.4
  - peft==0.5.0
  - deepspeed==0.11.1
  - torch==2.0.1
  - transformers==4.32.0
```

## Configure resources for Qwen

We will use an L4 to run this model.

```yaml config.yaml theme={"system"}
resources:
  accelerator: L4
  cpu: "4"
  memory: 16Gi
  use_gpu: true
```

# Deploy Qwen 7B Chat

Deploy the model like you would other Trusses, with:

```bash theme={"system"}
truss push qwen-7b-chat --publish
```


# Fast LLMs with TensorRT-LLM
Source: https://docs.baseten.co/examples/tensorrt-llm

Optimize LLMs for low latency and high throughput

To get the best performance, we recommend using our [TensorRT-LLM Engine-Builder](/engines/engine-builder-llm/overview) when deploying LLMs. Models deployed with the Engine-Builder are [OpenAI compatible](/inference/calling-your-model), support [structured output](/engines/performance-concepts/structured-outputs) and [function calling](/engines/performance-concepts/function-calling), and offer deploy-time post-training quantization to FP8 with Hopper GPUs and NVFP4 with Blackwell GPUs.

The Engine-Builder supports LLMs from the following families, both foundation models and fine-tunes:

* Llama 3.0 and later (including DeepSeek-R1 distills)
* Qwen 2.5 and later (including Math, Coder, and DeepSeek-R1 distills)
* Mistral (all LLMs)

You can download preset Engine-Builder configs for common models from the [model library](/examples/models/overview).

<Note>
  The Engine-Builder does not support vision-language models like Llama 3.2 11B or Pixtral. For these models, we recommend [vLLM](/examples/vllm).
</Note>

## Example: Deploy Qwen 2.5 3B on an H100

This configuration builds an inference engine to serve [Qwen 2.5 3B](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) on an H100 GPU. Running this model is fast and cheap, making it a good example for documentation, but the process of deploying it is very similar to larger models like [Llama 3.3 70B](/examples/models/llama/llama-3.3-70B-instruct).

## Setup

Before you deploy a model, you'll need three quick setup steps.

<Steps>
  <Step title="Create an API key for your Baseten account">
    Create an [API key](https://app.baseten.co/settings/api_keys) and save it as an environment variable:

    ```sh theme={"system"}
    export BASETEN_API_KEY="abcd.123456"
    ```
  </Step>

  <Step title="Add an access token for Hugging Face">
    Some models require that you accept terms and conditions on Hugging Face before deployment. To prevent issues:

    1. Accept the license for any gated models you wish to access, like [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct).
    2. Create a read-only [user access token](https://huggingface.co/docs/hub/en/security-tokens) from your Hugging Face account.
    3. Add the `hf_access_token` secret [to your Baseten workspace](https://app.baseten.co/settings/secrets).
  </Step>

  <Step title="Install Truss in your local development environment">
    Install the latest version of Truss, our open-source model packaging framework, as well as OpenAI's model inference SDK, with:

    ```sh theme={"system"}
    pip install --upgrade truss openai
    ```
  </Step>
</Steps>

## Configuration

Start with an empty configuration file.

```sh theme={"system"}
mkdir qwen-2-5-3b-engine
touch qwen-2-5-3b-engine/config.yaml
```

This configuration file specifies model information and Engine-Builder arguments. You can find dozens of examples in the [model library](/examples/models/overview) as well as details on each config option in the [engine builder reference](/engines/engine-builder-llm/engine-builder-config).

Below is an example for Qwen 2.5 3B.

```yaml config.yaml theme={"system"}
model_metadata:
  example_model_input: # Loads sample request into Baseten playground
    messages:
        - role: system
        content: "You are a helpful assistant."
        - role: user
        content: "What does Tongyi Qianwen mean?"
    stream: true
    max_tokens: 512
    temperature: 0.6  # Check recommended temperature per model
  repo_id: Qwen/Qwen2.5-3B-Instruct
model_name: Qwen 2.5 3B Instruct
python_version: py39
resources: # Engine-Builder GPU cannot be changed post-deployment
  accelerator: H100
  use_gpu: true
secrets: {}
trt_llm:
  build:
    base_model: decoder 
    checkpoint_repository:
      repo: Qwen/Qwen2.5-3B-Instruct
      source: HF
    num_builder_gpus: 1
    quantization_type: no_quant # `fp8_kv` often recommended for large models
    max_seq_len: 32768 # option to very the max sequence length, e.g. 131072 for Llama models
    tensor_parallel_count: 1 # Set equal to number of GPUs
    plugin_configuration:
      use_paged_context_fmha: true
      use_fp8_context_fmha: false # Set to true when using `fp8_kv`
      paged_kv_cache: true
  runtime:
    batch_scheduler_policy: max_utilization
    enable_chunked_context: true
    request_default_max_tokens: 32768 # 131072 for Llama models
```

## Deployment

Pushing the model to Baseten kicks off a multi-stage build and deployment process.

```sh theme={"system"}
truss push qwen-2-5-3b-engine --publish
```

Upon deployment, check your terminal logs or Baseten account to find the URL for the model server.

## Inference

This model is OpenAI compatible and can be called using the OpenAI client.

```python theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What does Tongyi Qianwen mean?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

That's it! You have successfully deployed and called an LLM optimized with the TensorRT-LLM Engine-Builder. Check the [model library](/examples/models/overview) for more examples and the [engine builder reference](/engines/engine-builder-llm/engine-builder-config) for details on each config option.


# Text to speech
Source: https://docs.baseten.co/examples/text-to-speech

Building a text-to-speech model with Kokoro

<Card title="View example on GitHub" icon="github" href="https://github.com/basetenlabs/truss-examples/tree/main/kokoro" />

In this example, we go through a Truss that serves Kokoro, a frontier text-to-speech model.

# Set up imports

We import necessary libraries and enable Hugging Face file transfers. We also download the NLTK tokenizer data.

```python model/model.py theme={"system"}
import logging
import os

os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
import base64
import io
import sys
import time

import nltk
import numpy as np
import scipy.io.wavfile as wav
import torch
from huggingface_hub import snapshot_download
from nltk.tokenize import sent_tokenize

from models import build_model
from kokoro import generate

logger = logging.getLogger(__name__)

nltk.download("punkt")
```

# Downloading model weights

We need to prepare model weights by doing the following:

* Create a directory for the model data
* Download the Kokoro model from Hugging Face into the created model data directory
* Add the model data directory to the system path

```python model/model.py theme={"system"}
# Ensure data directory exists
os.makedirs("/app/data/Kokoro-82M", exist_ok=True)

# Download model
snapshot_download(
    repo_id="hexgrad/Kokoro-82M",
    repo_type="model",
    revision="c97b7bbc3e60f447383c79b2f94fee861ff156ac",
    local_dir="/app/data/Kokoro-82M",
    ignore_patterns=["*.onnx", "kokoro-v0_19.pth", "demo/"],
    max_workers=8,
)

# Add data_dir to the system path
sys.path.append("/app/data/Kokoro-82M")
```

# Define the `Model` class and `load` function

In the `load` function of the Truss, we download and set up the model. This `load` function handles setting up the device, loading the model weights, and loading the default voice. We also define the available voices.

```python model/model.py theme={"system"}
class Model:
    def __init__(self, **kwargs):
        self._data_dir = kwargs["data_dir"]
        self.model = None
        self.device = None
        self.default_voice = None
        self.voices = None
        return

    def load(self):
        logger.info("Starting setup...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {self.device}")

        # Load model
        logger.info("Loading model...")
        model_path = "/app/data/Kokoro-82M/fp16/kokoro-v0_19-half.pth"
        logger.info(f"Model path: {model_path}")
        if not os.path.exists(model_path):
            logger.info(f"Error: Model file not found at {model_path}")
            raise FileNotFoundError(f"Model file not found at {model_path}")

        try:
            self.model = build_model(model_path, self.device)
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.info(f"Error loading model: {str(e)}")
            raise

        # Load default voice
        logger.info("Loading default voice...")
        voice_path = "/app/data/Kokoro-82M/voices/af.pt"
        if not os.path.exists(voice_path):
            logger.info(f"Error: Voice file not found at {voice_path}")
            raise FileNotFoundError(f"Voice file not found at {voice_path}")

        try:
            self.default_voice = torch.load(voice_path).to(self.device)
            logger.info("Default voice loaded successfully")
        except Exception as e:
            logger.info(f"Error loading default voice: {str(e)}")
            raise

        # Dictionary of available voices
        self.voices = {
            "default": "af",
            "bella": "af_bella",
            "sarah": "af_sarah",
            "adam": "am_adam",
            "michael": "am_michael",
            "emma": "bf_emma",
            "isabella": "bf_isabella",
            "george": "bm_george",
            "lewis": "bm_lewis",
            "nicole": "af_nicole",
            "sky": "af_sky",
        }
        return
```

# Define the `predict` function

The `predict` function contains the actual inference logic. The steps here are:

* Process input text and handle voice selection
* Chunk text for long inputs
* Generate audio
* Convert resulting audio to base64 and return it

```python model/model.py theme={"system"}
    def predict(self, model_input):
        # Run model inference here
        start = time.time()
        text = str(model_input.get("text", "Hi, I'm kokoro"))
        voice = str(model_input.get("voice", "af"))
        speed = float(model_input.get("speed", 1.0))
        logger.info(
            f"Text has {len(text)} characters. Using voice {voice} and speed {speed}."
        )
        if voice != "af":
            voicepack = torch.load(f"/app/data/Kokoro-82M/voices/{voice}.pt").to(
                self.device
            )
        else:
            voicepack = self.default_voice

        if len(text) >= 400:
            logger.info("Text is longer than 400 characters, splitting into sentences.")
            wavs = []

            def group_sentences(text, max_length=400):
                sentences = sent_tokenize(text)

                # Split long sentences
                while max([len(sent) for sent in sentences]) > max_length:
                    max_sent = max(sentences, key=len)
                    sentences_before = sentences[: sentences.index(max_sent)]
                    sentences_after = sentences[sentences.index(max_sent) + 1 :]
                    new_sentences = [
                        s.strip() + "." for s in max_sent.split(".") if s.strip()
                    ]
                    sentences = sentences_before + new_sentences + sentences_after

                return sentences

            sentences = group_sentences(text)
            logger.info(f"Processing {len(sentences)} chunks. Starting generation...")

            for sent in sentences:
                if sent.strip():
                    audio, _ = generate(
                        self.model, sent.strip(), voicepack, lang=voice[0], speed=speed
                    )
                    # Remove potential artifacts at the end
                    audio = audio[:-2000] if len(audio) > 2000 else audio
                    wavs.append(audio)

            # Concatenate all audio chunks
            audio = np.concatenate(wavs)
        else:
            logger.info("No splitting needed. Generating audio...")
            audio, _ = generate(self.model, text, voicepack, lang=voice[0], speed=speed)

        # Write audio to in-memory buffer
        buffer = io.BytesIO()
        wav.write(buffer, 24000, audio)
        wav_bytes = buffer.getvalue()
        duration_seconds = len(audio) / 24000
        logger.info(
            f"Generation took {time.time()-start} seconds to generate {duration_seconds:.2f} seconds of audio"
        )
        return {"base64": base64.b64encode(wav_bytes).decode("utf-8")}
```

# Setting up the `config.yaml`

Running Kokoro requires a handful of Python libraries, including `torch`, `transformers`, and others.

```yaml config.yaml theme={"system"}
build_commands:
- python3 -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
environment_variables: {}
model_metadata:
  example_model_input: {"text": "Kokoro is a frontier TTS model for its size of 82 million parameters (text in/audio out). On 25 Dec 2024, Kokoro v0.19 weights were permissively released in full fp32 precision under an Apache 2.0 license. As of 2 Jan 2025, 10 unique Voicepacks have been released, and a .onnx version of v0.19 is available.In the weeks leading up to its release, Kokoro v0.19 was the #1🥇 ranked model in TTS Spaces Arena. Kokoro had achieved higher Elo in this single-voice Arena setting over other models, using fewer parameters and less data. Kokoro's ability to top this Elo ladder suggests that the scaling law (Elo vs compute/data/params) for traditional TTS models might have a steeper slope than previously expected.", "voice": "af", "speed": 1.0}
model_name: kokoro
python_version: py311
requirements:
- torch==2.5.1
- transformers==4.48.0
- scipy==1.15.1
- phonemizer==3.3.0
- nltk==3.9.1
- numpy
- huggingface_hub[hf_transfer]
- hf_transfer==0.1.9
- munch==4.0.0
resources:
  accelerator: T4
  use_gpu: true
runtime:
  predict_concurrency: 1
secrets: {}
system_packages:
- espeak-ng
```

## Configuring resources for Kokoro

Note that we need an T4 GPU to run this model.

```yaml config.yaml theme={"system"}
resources:
  accelerator: T4
  use_gpu: true
```

## System Packages

Running Kokoro requires `espeak-ng` to synthesize speech output.

```yaml config.yaml theme={"system"}
system_packages:
- espeak-ng
```

# Deploy the model

Deploy the model like you would other Trusses by running the following command:

```bash theme={"system"}
truss push kokoro --publish
```

# Run an inference

Use a Python script to call the deployed model and parse its response. In this example, the script sends text input to the model and saves the returned audio (decoded from base64) as a WAV file: `output.wav`.

```python infer.py theme={"system"}
import httpx
import base64

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

with httpx.Client() as client:
    # Make the API request
    resp = client.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={"text": "Hello world", "voice": "af", "speed": 1.0},
        timeout=None,
    )

# Get the base64 encoded audio
response_data = resp.json()
audio_base64 = response_data["base64"]

# Decode the base64 string
audio_bytes = base64.b64decode(audio_base64)

# Write to a WAV file
with open("output.wav", "wb") as f:
    f.write(audio_bytes)

print("Audio saved to output.wav")
```


# Run any LLM with vLLM
Source: https://docs.baseten.co/examples/vllm

Serve a wide range of models

Another great option for inference is [vLLM](https://docs.vllm.ai/), which supports a wide range of models and performance optimizations.

## Example: Deploy Qwen 2.5 3B on an L4

This configuration serves [Qwen 2.5 3B](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) with vLLM on an L4 GPU. Running this model is fast and cheap, making it a good example for documentation, but the process of deploying it is very similar to larger models like [Llama 3.3 70B](/examples/models/llama/llama-3.3-70B-instruct).

## Setup

Before you deploy a model, you'll need three quick setup steps.

<Steps>
  <Step title="Create an API key for your Baseten account">
    Create an [API key](https://app.baseten.co/settings/api_keys) and save it as an environment variable:

    ```sh theme={"system"}
    export BASETEN_API_KEY="abcd.123456"
    ```
  </Step>

  <Step title="Add an access token for Hugging Face">
    Some models require that you accept terms and conditions on HuggingFace before deployment. To prevent issues:

    1. Accept the license for any gated models you wish to access, like [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct).
    2. Create a read-only [user access token](https://huggingface.co/docs/hub/en/security-tokens) from your Hugging Face account.
    3. Add the `hf_access_token` secret [to your Baseten workspace](https://app.baseten.co/settings/secrets).
  </Step>

  <Step title="Install Truss in your local development environment">
    Install the latest version of Truss, our open-source model packaging framework, as well as OpenAI's model inference SDK, with:

    ```sh theme={"system"}
    pip install --upgrade truss openai
    ```
  </Step>
</Steps>

## Configuration

Start with an empty configuration file.

```sh theme={"system"}
mkdir qwen-2-5-3b-engine
touch qwen-2-5-3b-engine/config.yaml
```

Below is an example for Qwen 2.5 3B. You can copy-paste it into the empty `config.yaml` we created above.

```yaml config.yaml theme={"system"}
model_metadata:
  engine_args:
    model: Qwen/Qwen2.5-3B-Instruct
  example_model_input: # Loads sample request into Baseten playground
    messages:
        - role: system
          content: "You are a helpful assistant."
        - role: user
          content: "What does Tongyi Qianwen mean?"
    stream: true
    max_tokens: 512
    temperature: 0.6
base_image:
  image: vllm/vllm-openai:v0.7.3
docker_server:
  start_command: sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) vllm serve Qwen/Qwen2.5-3B-Instruct --enable-prefix-caching --enable-chunked-prefill"
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /v1/completions
  server_port: 8000
runtime:
  predict_concurrency: 256
resources:
  accelerator: L4
  use_gpu: true
environment_variables:
  hf_access_token: null
```

## Deployment

Pushing the model to Baseten kicks off a multi-stage deployment process.

```sh theme={"system"}
truss push qwen-2-5-3b-engine --publish
```

Upon deployment, check your terminal logs or Baseten account to find the URL for the model server.

## Inference

This model is OpenAI compatible and can be called using the OpenAI client.

```python call_model.py theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="Qwen/Qwen2.5-3B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What does Tongyi Qianwen mean?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

That's it! You have successfully deployed and called a model using vLLM.


# Async inference
Source: https://docs.baseten.co/inference/async

Run asynchronous inference on deployed models

Async inference is a *fire and forget* pattern for model requests. Instead of
waiting for a response, you receive a request ID immediately while inference
runs in the background. When complete, results are delivered to your webhook
endpoint.

<Note>
  Async requests work with any deployed model, no code changes are required.
  Requests can queue for up to 72 hours and run for up to 1 hour. Async inference is not
  compatible with streaming output.
</Note>

Use async inference for:

* **Long-running tasks** that would otherwise hit request timeouts.
* **Batch processing** where you don't need immediate responses.
* **Priority queuing** to serve VIP customers faster.

<Warning>
  Baseten does not store model outputs. If webhook delivery fails after all retries,
  your data is lost. See [Webhook delivery](#webhook-delivery) for mitigation
  strategies.
</Warning>

## Quick start

<Steps>
  <Step title="Set up a webhook endpoint">
    Create an HTTPS endpoint to receive results.
    Use [this Repl](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code) as a starting point, or deploy to any service that can receive POST requests.
  </Step>

  <Step title="Make an async request">
    Call your model's `/async_predict` endpoint with your webhook URL:

    ```python theme={"system"}
    import requests
    import os

    model_id = "YOUR_MODEL_ID"
    webhook_endpoint = "YOUR_WEBHOOK_ENDPOINT"
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    # Call the async_predict endpoint of the production deployment
    resp = requests.post(
        f"https://model-{model_id}.api.baseten.co/production/async_predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "model_input": {"prompt": "hello world!"},
            "webhook_endpoint": webhook_endpoint,
            # "priority": 0,
            # "max_time_in_queue_seconds": 600,
        },
    )

    print(resp.json())
    ```

    You'll receive a `request_id` immediately.
  </Step>

  <Step title="Receive results">
    When inference completes, Baseten sends a POST request to your webhook with the model output.
    See [Webhook payload](#webhook-payload) for the response format.
  </Step>
</Steps>

<Tip>
  **Chains** support async inference through `async_run_remote`.
  Inference requests to the entrypoint are queued, but internal Chainlet-to-Chainlet calls run synchronously.
</Tip>

## How async works

Async inference decouples request submission from processing, letting you queue work without waiting for results.

### Request lifecycle

When you submit an async request:

1. You call `/async_predict` and immediately receive a `request_id`.
2. Your request enters a queue managed by the Async Request Service.
3. A background worker picks up your request and calls your model's predict endpoint.
4. Your model runs inference and returns a response.
5. Baseten sends the response to your webhook URL using POST.

The `max_time_in_queue_seconds` parameter controls how long a request waits
before expiring. It defaults to 10 minutes but can extend to 72 hours.

### Autoscaling behavior

The async queue is decoupled from model scaling. Requests queue successfully
even when your model has zero replicas.

When your model is scaled to zero:

1. Your request enters the queue while the model has no running replicas.
2. The queue processor attempts to call your model, triggering the autoscaler.
3. Your request waits while the model cold-starts.
4. Once the model is ready, inference runs and completes.
5. Baseten delivers the result to your webhook.

If the model doesn't become ready within `max_time_in_queue_seconds`, the
request expires with status `EXPIRED`. Set this parameter to account for your
model's startup time. For models with long cold starts, consider keeping minimum
replicas running using
[autoscaling settings](/deployment/autoscaling).

### Async priority

Async requests are subject to two levels of priority: how they compete with sync
requests for model capacity, and how they're ordered relative to other async
requests in the queue.

#### Sync vs async concurrency

Sync and async requests share your model's concurrency pool, controlled by
`predict_concurrency` in your model configuration:

```yaml config.yaml theme={"system"}
runtime:
  predict_concurrency: 10
```

The `predict_concurrency` setting defines how many requests your model can
process simultaneously per replica. When both sync and async requests are in
flight, sync requests take priority. The queue processor monitors your model's
capacity and backs off when it receives 429 responses, ensuring sync traffic
isn't starved.

For example, if your model has `predict_concurrency=10` and 8 sync requests are
running, only 2 slots remain for async requests. The remaining async requests
stay queued until capacity frees up.

#### Async queue priority

Within the async queue itself, you can control processing order using the
`priority` parameter. This is useful for serving specific requests faster or
ensuring critical batch jobs run before lower-priority work.

```python theme={"system"}
import requests
import os

model_id = "YOUR_MODEL_ID"
webhook_endpoint = "YOUR_WEBHOOK_URL"
baseten_api_key = os.environ["BASETEN_API_KEY"]

resp = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/async_predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={
        "webhook_endpoint": webhook_endpoint,
        "model_input": {"prompt": "hello world!"},
        "priority": 0,
    },
)

print(resp.json())
```

The `priority` parameter accepts values 0, 1, or 2. Lower values indicate higher
priority: a request with `priority: 0` is processed before requests with
`priority: 1` or `priority: 2`. If you don't specify a priority, requests
default to priority 1.

Use priority 0 sparingly for truly urgent requests. If all requests are marked
priority 0, the prioritization has no effect.

## Webhooks

Baseten delivers async results to your webhook endpoint when inference completes.

### Request format

When inference completes, Baseten sends a POST request to your webhook with these headers and body:

```text theme={"system"}
POST /your-webhook-path HTTP/2.0
Content-Type: application/json
X-BASETEN-REQUEST-ID: 9876543210abcdef1234567890fedcba
X-BASETEN-SIGNATURE: v1=abc123...
```

The `X-BASETEN-REQUEST-ID` header contains the request ID for correlating webhooks with your original requests.
The `X-BASETEN-SIGNATURE` header is only included if a [webhook secret](#secure-webhooks) is configured.

<Note>
  Webhook endpoints must use HTTPS (except `localhost` for development). Baseten
  supports HTTP/2 and HTTP/1.1 connections.
</Note>

```json theme={"system"}
{
  "request_id": "9876543210abcdef1234567890fedcba",
  "model_id": "abc123",
  "deployment_id": "def456",
  "type": "async_request_completed",
  "time": "2024-04-30T01:01:08.883423Z",
  "data": { "output": "model response here" },
  "errors": []
}
```

The body contains the `request_id` matching your original `/async_predict`
response, along with `model_id` and `deployment_id` identifying which deployment
ran the request. The `data` field contains your model output, or `null` if an
error occurred. The `errors` array is empty on success, or contains error
objects on failure.

### Webhook delivery

<Warning>
  If all delivery attempts fail, your model output is permanently lost.
</Warning>

Baseten delivers webhooks on a best-effort basis with automatic retries:

| Setting         | Value                      |
| --------------- | -------------------------- |
| Total attempts  | 3 (1 initial + 2 retries). |
| Backoff         | 1 second, then 4 seconds.  |
| Timeout         | 10 seconds per attempt.    |
| Retryable codes | 500, 502, 503, 504.        |

**To prevent data loss:**

1. **Save outputs in your model.** Use the `postprocess()` function to write to
   cloud storage:

```python theme={"system"}
import json
import boto3

class Model:
  # ...
    def postprocess(self, model_output):
        s3 = boto3.client("s3")
        s3.put_object(
            Bucket="my-bucket",
            Key=f"outputs/{self.context.get('request_id')}.json",
            Body=json.dumps(model_output)
        )
        return model_output
```

This will process your model output and save it to your desired location.

The `postprocess` method runs after inference completes. Use
`self.context.get('request_id')` to access the async request ID for correlating
outputs with requests.

2. **Use a reliable endpoint.** Deploy your webhook to a highly available
   service like a cloud function or message queue.

### Secure webhooks

Create a webhook secret in the
[Secrets tab](https://app.baseten.co/settings/secrets) to verify requests are
from Baseten.

When configured, Baseten includes an `X-BASETEN-SIGNATURE` header:

```text theme={"system"}
X-BASETEN-SIGNATURE: v1=abc123...
```

To validate, compute an HMAC-SHA256 of the request body using your secret and compare:

```python theme={"system"}
import hashlib
import hmac

def verify_signature(body: bytes, signature: str, secret: str) -> bool:
    expected = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
    actual = signature.replace("v1=", "").split(",")[0]
    return hmac.compare_digest(expected, actual)
```

The function computes an HMAC-SHA256 hash of the raw request body using your
webhook secret. It extracts the signature value after `v1=` and uses
`compare_digest` for timing-safe comparison to prevent timing attacks.

Rotate secrets periodically. During rotation, both old and new secrets remain
valid for 24 hours.

## Manage requests

You can check the status of async requests or cancel them while they're queued.

### Check request status

To check the status of an async request, call the status endpoint with your request ID:

```python theme={"system"}
import requests
import os

model_id = "YOUR_MODEL_ID"
request_id = "YOUR_REQUEST_ID"
baseten_api_key = os.environ["BASETEN_API_KEY"]

resp = requests.get(
    f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
    headers={"Authorization": f"Api-Key {baseten_api_key}"}
)

print(resp.json())
```

Status is available for 1 hour after completion. See the
[status API reference](/reference/inference-api/status-endpoints/get-async-request-status)
for details.

| Status           | Description                                      |
| ---------------- | ------------------------------------------------ |
| `QUEUED`         | Waiting in queue.                                |
| `IN_PROGRESS`    | Currently processing.                            |
| `SUCCEEDED`      | Completed successfully.                          |
| `FAILED`         | Failed after retries.                            |
| `EXPIRED`        | Exceeded `max_time_in_queue_seconds`.            |
| `CANCELED`       | Canceled by user.                                |
| `WEBHOOK_FAILED` | Inference succeeded but webhook delivery failed. |

### Cancel a request

Only `QUEUED` requests can be canceled. To cancel a request, call the cancel
endpoint with your request ID:

```python theme={"system"}
import requests
import os

model_id = "YOUR_MODEL_ID"
request_id = "YOUR_REQUEST_ID"
baseten_api_key = os.environ["BASETEN_API_KEY"]

resp = requests.delete(
    f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
    headers={"Authorization": f"Api-Key {baseten_api_key}"}
)

print(resp.json())
```

For more information, see the [cancel async request API reference](/reference/inference-api/predict-endpoints/cancel-async-request).

## Error codes

When inference fails, the webhook payload returns an `errors` array:

```json theme={"system"}
{
  "errors": [{ "code": "MODEL_PREDICT_ERROR", "message": "Details here" }]
}
```

| Code                    | HTTP    | Description                     | Retried |
| ----------------------- | ------- | ------------------------------- | ------- |
| `MODEL_NOT_READY`       | 400     | Model is loading or starting.   | Yes     |
| `MODEL_DOES_NOT_EXIST`  | 404     | Model or deployment not found.  | No      |
| `MODEL_INVALID_INPUT`   | 422     | Invalid input format.           | No      |
| `MODEL_PREDICT_ERROR`   | 500     | Exception in `model.predict()`. | Yes     |
| `MODEL_UNAVAILABLE`     | 502/503 | Model crashed or scaling.       | Yes     |
| `MODEL_PREDICT_TIMEOUT` | 504     | Inference exceeded timeout.     | Yes     |

### Inference retries

When inference fails with a retryable error, Baseten automatically retries the
request using exponential backoff. Configure this behavior with
`inference_retry_config`:

```python theme={"system"}
import requests
import os

model_id = "YOUR_MODEL_ID"
webhook_endpoint = "YOUR_WEBHOOK_URL"
baseten_api_key = os.environ["BASETEN_API_KEY"]

resp = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/async_predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={
        "model_input": {"prompt": "hello world!"},
        "webhook_endpoint": webhook_endpoint,
        "inference_retry_config": {
            "max_attempts": 3,
            "initial_delay_ms": 1000,
            "max_delay_ms": 5000
        }
    },
)

print(resp.json())
```

| Parameter          | Range    | Default | Description                                      |
| ------------------ | -------- | ------- | ------------------------------------------------ |
| `max_attempts`     | 1-10     | 3       | Total inference attempts including the original. |
| `initial_delay_ms` | 0-10,000 | 1000    | Delay before the first retry (ms).               |
| `max_delay_ms`     | 0-60,000 | 5000    | Maximum delay between retries (ms).              |

Retries use exponential backoff with a multiplier of 2. With the default
configuration, delays progress as: 1s → 2s → 4s → 5s (capped at `max_delay_ms`).

Only requests that fail with retryable error codes (500, 502, 503, 504) are
retried. Non-retryable errors like invalid input (422) or model not found (404)
fail immediately.

<Note>
  Inference retries are distinct from [webhook delivery retries](#webhook-delivery).
  Inference retries happen when calling your model fails. Webhook retries happen
  when delivering results to your endpoint fails.
</Note>

## Rate limits

There are rate limits for the async predict endpoint and the status polling endpoint.
If you exceed these limits, you will receive a 429 status code.

| Endpoint                                     | Limit                               |
| -------------------------------------------- | ----------------------------------- |
| Predict endpoint requests (`/async_predict`) | 12,000 requests/minute (org-level). |
| Status polling                               | 20 requests/second.                 |
| Cancel request                               | 20 requests/second.                 |

Use webhooks instead of polling to avoid status endpoint limits. Contact
[support@baseten.co](mailto:support@baseten.co) to request increases.

## Observability

Async metrics are available on the
[Metrics tab](/observability/metrics#async-queue-metrics) of your model
dashboard:

* **Inference latency/volume**: includes async requests.
* **Time in async queue**: time spent in `QUEUED` state.
* **Async queue size**: number of queued requests.

<Frame>
  <img />
</Frame>

## Resources

For more information and resources, see the following:

<CardGroup>
  <Card title="Webhook starter code" icon="code" href="https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code">
    Fork this Repl to quickly set up a webhook endpoint for testing async inference.
  </Card>

  <Card title="Webhook secrets" icon="key" href="https://app.baseten.co/settings/secrets">
    Configure webhook secrets in your Baseten settings to secure webhook delivery.
  </Card>
</CardGroup>


# Call your model
Source: https://docs.baseten.co/inference/calling-your-model

Run inference on deployed models

Once deployed, your model is accessible through an [API endpoint](/reference/inference-api/overview). To make an inference request, you'll need:

* **Model ID**: Found in the Baseten dashboard or returned when you deploy.
* **[API key](/organization/api-keys)**: Authenticates your requests.
* **JSON-serializable model input**: The data your model expects.

## Authentication

Include your API key in the `Authorization` header:

```sh theme={"system"}
curl -X POST https://model-YOUR_MODEL_ID.api.baseten.co/environments/production/predict \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, world!"}'
```

In Python with requests:

```python theme={"system"}
import requests
import os

api_key = os.environ["BASETEN_API_KEY"]
model_id = "YOUR_MODEL_ID"

response = requests.post(
    f"https://model-{model_id}.api.baseten.co/environments/production/predict",
    headers={"Authorization": f"Api-Key {api_key}"},
    json={"prompt": "Hello, world!"},
)

print(response.json())
```

## Predict API endpoints

Baseten provides multiple endpoints for different inference modes:

* [`/predict`](/reference/inference-api/overview#predict-endpoints) – Standard synchronous inference.
* [`/async_predict`](/reference/inference-api/overview#predict-endpoints) – Asynchronous inference for long-running tasks.

Endpoints are available for environments and all deployments. See the [API reference](/reference/inference-api/overview) for details.

## Sync API endpoints

Custom servers support both `predict` endpoints as well as a special `sync` endpoint. By using the `sync` endpoint you are able to call different routes in your custom server.

```
https://model-{model-id}.api.baseten.co/environments/{production}/sync/{route}
```

Here are a few examples that show how the sync endpoint maps to the custom server's routes.

* `https://model-{model_id}.../sync/health` -> `/health`
* `https://model-{model_id}.../sync/items` -> `/items`
* `https://model-{model_id}.../sync/items/123` -> `/items/123`

## OpenAI SDK

When deploying a model with Engine-Builder, you will get an OpenAI compatible server. If you are already using one of the OpenAI SDKs, you will simply need to update the base url to your Baseten model URL and include your Baseten API Key.

```python theme={"system"}
import os
from openai import OpenAI

model_id = "abcdef" # TODO: replace with your model id
api_key = os.environ.get("BASETEN_API_KEY")
model_url = f"https://model-{model_id}.api.baseten.co/environments/production/sync/v1"

client = OpenAI(
    base_url=model_url,
    api_key=api_key,
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

## Alternative invocation methods

* **Truss CLI**: [`truss predict`](/reference/cli/truss/predict)
* **Model Dashboard**: "Playground" button in the Baseten UI


# Concepts
Source: https://docs.baseten.co/inference/concepts



<img />

Inference on Baseten is designed for flexibility, efficiency, and scalability. Models can be served [synchronously](/inference/calling-your-model), [asynchronously](/inference/async), or with [streaming](/inference/streaming) to meet different performance and latency needs.

* [Synchronously](/inference/calling-your-model) inference is ideal for low-latency, real-time responses.
* [Asynchronously](/inference/async) inference handles long-running tasks efficiently without blocking resources.
* [Streaming](/inference/streaming) inference delivers partial results as they become available for faster response times.

Baseten supports various input and output formats, including structured data, binary files, and function calls, making it adaptable to different workloads.


# Integrations
Source: https://docs.baseten.co/inference/integrations

Integrate your models with tools like LangChain, LiteLLM, and more.

<CardGroup>
  <Card title="Cline" icon="robot" href="https://www.baseten.co/blog/from-prompt-to-production-baseten-inference-in-your-ide-with-cline/">
    Use frontier open-source models like Kimi K2 Thinking, GLM 4.6, DeepSeek V3.2 inside your IDE with Baseten and Cline.
  </Card>

  <Card title="HumanLayer" icon="person" href="https://www.humanlayer.dev">
    Build agents with human-in-the-loop powered by Baseten LLMs and HumanLayer.
  </Card>

  <Card title="LlamaIndex" icon="horse" href="https://docs.llamaindex.ai/en/latest/api_reference/llms/baseten/">
    Use Baseten models within your RAG applications with LlamaIndex.
  </Card>

  <Card title="LangChain" icon="bird" href="https://docs.langchain.com/oss/python/integrations/providers/baseten">
    Use your Baseten models with LangChain V1.0 to build workflows and agents.
  </Card>

  <Card title="LiteLLM" icon="grapes" href="https://docs.litellm.ai/docs/providers/baseten">
    Use your Baseten models in LiteLLM projects.
  </Card>

  <Card title="LiveKit" icon="microphone-lines" href="https://docs.livekit.io/agents/integrations/tts/baseten/">
    Build real-time voice agents with TTS models hosted on Baseten.
  </Card>

  <Card title="Roo Code" icon="rabbit" href="https://docs.roocode.com/providers/baseten">
    Use frontier open-source models like Kimi K2 Thinking, GLM 4.6, DeepSeek V3.2 inside your IDE with Baseten and Roo Code.
  </Card>

  <Card title="Vercel" icon="computer" href="https://ai-sdk.dev/providers/ai-sdk-providers/baseten">
    Power your Next.js web apps using Baseten models through AI SDK v5.
  </Card>
</CardGroup>

<Card title="Build your own" icon="hammer" href="mailto:support@baseten.co">
  Want to integrate Baseten with your platform or project? Reach out to
  [support@baseten.co](mailto:support@baseten.co) and we'll help with building
  and marketing the integration.
</Card>


# Model I/O in binary
Source: https://docs.baseten.co/inference/output-format/binary

Decode and save binary model output

Baseten and Truss natively support model I/O in binary and use msgpack encoding for efficiency.

## Deploy a basic Truss for binary I/O

If you need a deployed model to try the invocation examples below, follow these steps to create and deploy a super basic Truss that accepts and returns binary data. The Truss performs no operations and is purely illustrative.

<Accordion title="Steps for deploying an example Truss">
  <Steps>
    <Step title="Create a Truss">
      To create a Truss, run:

      ```sh theme={"system"}
      truss init binary_test
      ```

      This creates a Truss in a new directory `binary_test`. By default, newly created Trusses implement an identity function that returns the exact input they are given.
    </Step>

    <Step title="Add logging">
      Optionally, modify `binary_test/model/model.py` to log that the data received is of type `bytes`:

      ```python binary_test/model/model.py theme={"system"}
      def predict(self, model_input):
          # Run model inference here
          print(f"Input type: {type(model_input['byte_data'])}")
          return model_input
      ```
    </Step>

    <Step title="Deploy the Truss">
      Deploy the Truss to Baseten for development:

      ```sh theme={"system"}
      truss push --watch
      ```

      Or for production:

      ```sh theme={"system"}
      truss push --publish
      ```
    </Step>
  </Steps>
</Accordion>

## Send raw bytes as model input

To send binary data as model input:

1. Set the `content-type` HTTP header to `application/octet-stream`
2. Use `msgpack` to encode the data or file
3. Make a POST request to the model

This code sample assumes you have a file `Gettysburg.mp3` in the current working directory. You can download the [11-second file from our CDN](https://cdn.baseten.co/docs/production/Gettysburg.mp3) or replace it with your own file.

```python call_model.py theme={"system"}
import os
import requests
import msgpack


model_id = "MODEL_ID"  # Replace this with your model ID
deployment = "development"  # `development`, `production`, or a deployment ID
baseten_api_key = os.environ["BASETEN_API_KEY"]
# Specify the URL to which you want to send the POST request
url = f"https://model-{model_id}.api.baseten.co/{deployment}/predict"
headers={
    "Authorization": f"Api-Key {baseten_api_key}",
    "content-type": "application/octet-stream",
}

with open('Gettysburg.mp3', 'rb') as file:
    response = requests.post(
        url,
        headers=headers,
        data=msgpack.packb({'byte_data': file.read()})
    )

print(response.status_code)
print(response.headers)
```

<Note>
  To support certain types like numpy and datetime values, you may need to
  extend client-side `msgpack` encoding with the same [encoder and decoder used
  by
  Truss](https://github.com/basetenlabs/truss/blob/main/truss/templates/shared/serialization.py).
</Note>

## Parse raw bytes from model output

To use the output of a non-streaming model response, decode the response content.

```python call_model.py theme={"system"}
# Continues `call_model.py` from above

binary_output = msgpack.unpackb(response.content)

# Change extension if not working with mp3 data
with open('output.mp3', 'wb') as file:
    file.write(binary_output["byte_data"])
```

## Streaming binary outputs

You can also stream output as binary. This is useful for sending large files or reading binary output as it is generated.

In the `model.py`, you must create a streaming output.

```python model/model.py theme={"system"}
# Replace the predict function in your Truss
def predict(self, model_input):
    import os

    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "tmpfile.txt")
    with open(file_path, mode="wb") as file:
            file.write(bytes(model_input["text"], encoding="utf-8"))

    def iterfile():
        # Get the directory of the current file
        current_dir = os.path.dirname(__file__)
        # Construct the full path to the .wav file
        file_path = os.path.join(current_dir, "tmpfile.txt")
        with open(file_path, mode="rb") as file_like:
            yield from file_like

    return iterfile()
```

Then, in your client, you can use streaming output directly without decoding.

```python stream_model.py theme={"system"}
import os
import requests
import json

model_id = "MODEL_ID"  # Replace this with your model ID
deployment = "development"  # `development`, `production`, or a deployment ID
baseten_api_key = os.environ["BASETEN_API_KEY"]
# Specify the URL to which you want to send the POST request
url = f"https://model-{model_id}.api.baseten.co/{deployment}/predict"
headers={
    "Authorization": f"Api-Key {baseten_api_key}",
}

s = requests.Session()
with s.post(
    # Endpoint for production deployment, see API reference for more
    f"https://model-{model_id}.api.baseten.co/{deployment}/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    data=json.dumps({"text": "Lorem Ipsum"}),
    # Include stream=True as an argument so the requests libray knows to stream
    stream=True,
) as response:
    for token in response.iter_content(1):
        print(token) # Prints bytes
```


# Model I/O with files
Source: https://docs.baseten.co/inference/output-format/files

Call models by passing a file or URL

Baseten supports a wide variety of file-based I/O approaches. These examples show our recommendations for working with files during model inference, whether local or remote, public or private, in the Truss or in your invocation code.

## Files as input

### Example: Send a file with JSON-serializable content

The Truss CLI has a `-f` flag to pass file input. If you're using the API endpoint via Python, get file contents with the standard `f.read()` function.

<CodeGroup>
  ```sh Truss CLI theme={"system"}
  truss predict -f input.json
  ```

  ```python Python script theme={"system"}
  import urllib3
  import json

  model_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  # Read input as JSON
  with open("input.json", "r") as f:
      data = json.loads(f.read())

  resp = urllib3.request(
      "POST",
      # Endpoint for production deployment, see API reference for more
      f"https://model-{model_id}.api.baseten.co/production/predict",
      headers={"Authorization": f"Api-Key {baseten_api_key}"},
      json=data
  )

  print(resp.json())
  ```
</CodeGroup>

### Example: Send a file with non-serializable content

The `-f` flag for `truss predict` only applies to JSON-serializable content. For other files, like the audio files required by [MusicGen Melody](https://www.baseten.co/library/musicgen-melody), the file content needs to be base64 encoded before it is sent.

```python theme={"system"}
import urllib3

model_id = ""
# Read secrets from environment variables
baseten_api_key = os.environ["BASETEN_API_KEY"]

# Open a local file
with open("mymelody.wav", "rb") as f: # mono wav file, 48khz sample rate
    # Convert file contents into JSON-serializable format
    encoded_data = base64.b64encode(f.read())
    encoded_str = encoded_data.decode("utf-8")
# Define the data payload
data = {"prompts": ["happy rock", "energetic EDM", "sad jazz"], "melody": encoded_str, "duration": 8}
# Make the POST request
response = requests.post(url, headers=headers, data=data)
resp = urllib3.request(
    "POST",
    # Endpoint for production deployment, see API reference for more
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)
data = resp.json()["data"]
# Save output to files
for idx, clip in enumerate(data):
    with open(f"clip_{idx}.wav", "wb") as f:
        f.write(base64.b64decode(clip))
```

### Example: Send a URL to a public file

Rather than encoding and serializing a file to send in the HTTP request, you can instead write a Truss that takes a URL as input and loads the content in the `preprocess()` function.

Here's an example from [Whisper in the model library](https://www.baseten.co/library/whisper-v3).

```python theme={"system"}
from tempfile import NamedTemporaryFile
import requests

# Get file content without blocking GPU
def preprocess(self, request):
    resp = requests.get(request["url"])
    return {"content": resp.content}

# Use file content in model inference
def predict(self, model_input):
    with NamedTemporaryFile() as fp:
        fp.write(model_input["content"])
        result = whisper.transcribe(
            self._model,
            fp.name,
            temperature=0,
            best_of=5,
            beam_size=5,
        )
        segments = [
            {"start": r["start"], "end": r["end"], "text": r["text"]}
            for r in result["segments"]
        ]
    return {
        "language": whisper.tokenizer.LANGUAGES[result["language"]],
        "segments": segments,
        "text": result["text"],
    }
```

## Files as output

### Example: Save model output to local file

When saving model output to a local file, there's nothing Baseten-specific about the code. Just use the standard `>` operator in bash or `file.write()` function in Python to save the model output.

<CodeGroup>
  ```sh Truss CLI theme={"system"}
  truss predict -d '"Model input!"' > output.json
  ```

  ```python Python script theme={"system"}
  import urllib3
  import json

  model_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  # Call model
  resp = urllib3.request(
      "POST",
      # Endpoint for production deployment, see API reference for more
      f"https://model-{model_id}.api.baseten.co/production/predict",
      headers={"Authorization": f"Api-Key {baseten_api_key}"},
      json=json.dumps("Model input!")
  )
  # Write results to file
  with open("output.json", "w") as f:
      f.write(resp.json())
  ```
</CodeGroup>

Output for some models, like image and audio generation models, may need to be decoded before you save it. See our [image generation example](/examples/image-generation) for how to parse base64 output.


# Streaming
Source: https://docs.baseten.co/inference/streaming

How to call a model that has a streaming-capable endpoint.

Any model could be packaged with support for streaming output, but it only makes sense to do so for models where:

* Generating a complete output takes a relatively long time.
* The first tokens of output are useful without the context of the rest of the output.
* Reducing the time to first token improves the user experience.

LLMs in chat applications are the perfect use case for streaming model output.

## Example: Streaming with Mistral

[Mistral 7B Instruct](https://www.baseten.co/library/mistral-7b-instruct) from Baseten's model library is a recent LLM with streaming support. Invocation should be the same for any other model library LLM as well as any Truss that follows the same standard.

[Deploy Mistral 7B Instruct](https://www.baseten.co/library/mistral-7b-instruct) or a similar LLM to run the following examples.

### Truss CLI

The Truss CLI has built-in support for streaming model output.

```sh theme={"system"}
truss predict -d '{"prompt": "What is the Mistral wind?", "stream": true}'
```

### API endpoint

When using a streaming endpoint with cURL, use the `--no-buffer` flag to stream output as it is received.

As with all cURL invocations, you'll need a model ID and API key.

```sh theme={"system"}
curl -X POST https://app.baseten.co/models/MODEL_ID/predict \
  -H 'Authorization: Api-Key YOUR_API_KEY' \
  -d '{"prompt": "What is the Mistral wind?", "stream": true}' \
  --no-buffer
```

### Python application

Let's take things a step further and look at how to integrate streaming output with a Python application.

```python theme={"system"}
import requests
import json
import os

# Model ID for production deployment
model_id = ""
# Read secrets from environment variables
baseten_api_key = os.environ["BASETEN_API_KEY"]

# Open session to enable streaming
s = requests.Session()
with s.post(
    # Endpoint for production deployment, see API reference for more
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    # Include "stream": True in the data dict so the model knows to stream
    data=json.dumps({
      "prompt": "What even is AGI?",
      "stream": True,
      "max_new_tokens": 4096
    }),
    # Include stream=True as an argument so the requests libray knows to stream
    stream=True,
) as resp:
    # Print the generated tokens as they get streamed
    for content in resp.iter_content():
        print(content.decode("utf-8"), end="", flush=True)
```


# Export to Datadog
Source: https://docs.baseten.co/observability/export-metrics/datadog

Export metrics from Baseten to Datadog

The Baseten metrics endpoint can be integrated with [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) by configuring a Prometheus receiver that scrapes the endpoint. This allows Baseten metrics to be pushed to a variety of popular exporters—see the [OpenTelemetry registry](https://opentelemetry.io/ecosystem/registry/?component=exporter) for a full list.

**Using OpenTelemetry Collector to push to Datadog**

```yaml config.yaml theme={"system"}
receivers:  
  # Configure a Prometheus receiver to scrape the Baseten metrics endpoint.
  prometheus:
    config:
      scrape_configs:
        - job_name: 'baseten'
          scrape_interval: 60s
          metrics_path: '/metrics'
          scheme: https
          authorization:
            type: "Api-Key"
            credentials: "{BASETEN_API_KEY}"
          static_configs:
            - targets: ['app.baseten.co']
processors:
  batch:
exporters:
  # Configure a Datadog exporter.
  datadog:
    api:
      key: "{DATADOG_API_KEY}"
service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [batch]
      exporters: [datadog]
```


# Export to Grafana Cloud
Source: https://docs.baseten.co/observability/export-metrics/grafana

Export metrics from Baseten to Grafana Cloud

The Baseten + Grafana Cloud integration enables you to get real-time inference metrics within your existing Grafana setup.

## Video tutorial

See below for step-by-step details from the video.

<iframe title="YouTube video player" />

## Set up the integration

For a visual guide, please follow along with the video above.

Open your Grafana Cloud account:

1. Navigate to "Home > Connections > Add new connection".
2. In the search bar, type `Metrics Endpoint` and select it.
3. Give your scrape job a name like `baseten_metrics_scrape`.
4. Set the scrape job URL to `https://app.baseten.co/metrics`.
5. Leave the scrape interval set to `Every minute`.
6. Select `Bearer` for authentication credentials.
7. In your Baseten account, generate a metrics-only workspace API key.
8. In Grafana, enter the Bearer Token as `Api-Key abcd.1234567890` where the latter value is replaced by your API key.
9. Use the "Test Connection" button to ensure everything is entered correctly.
10. Click "Save Scrape Job."
11. Click "Install."
12. In your integrations list, select your new export and go through the "Enable" flow shown on video.

Now, you can navigate to your Dashboards tab, where you will see your data! Please note that it can take a couple of minutes for data to arrive and only new data will be scraped, not historical metrics.

## Build a Grafana dashboard

Importing the data is a great first step, but you'll need a dashboard to properly visualize the incoming information.

We've prepared a basic dashboard to get you started, which you can import by:

1. Downloading `baseten_grafana_dashboard.json` from [this GitHub Gist](https://gist.github.com/philipkiely-baseten/9952e7592775ce1644944fb644ba2a9c).
2. Selecting "New > Import" from the dropdown in the top-right corner of the Dashboard page.
3. Dropping in the provided JSON file.

For visual reference in navigating the dashboard, please see the video above.


# Export to New Relic
Source: https://docs.baseten.co/observability/export-metrics/new-relic

Export metrics from Baseten to New Relic

Export Baseten metrics to New Relic by integrating with [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/). This involves configuring a Prometheus receiver that scrapes Baseten's metrics endpoint and configuring a New Relic exporter to send the metrics to your observability backend.

**Using OpenTelemetry Collector to push to New Relic**

```yaml config.yaml theme={"system"}
receivers:  
  # Configure a Prometheus receiver to scrape the Baseten metrics endpoint.
  prometheus:
    config:
      scrape_configs:
        - job_name: 'baseten'
          scrape_interval: 60s
          metrics_path: '/metrics'
          scheme: https
          authorization:
            type: "Api-Key"
            credentials: "{BASETEN_API_KEY}"
          static_configs:
            - targets: ['app.baseten.co']
processors:
  batch:
exporters:
  # Configure a New Relic exporter. Visit New Relic documentation to get your regional otlp endpoint.
  otlphttp/newrelic:
    endpoint: https://otlp.nr-data.net
    headers:
      api-key: "{NEW_RELIC_KEY}"
service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [batch]
      exporters: [otlphttp/newrelic]
```


# Overview
Source: https://docs.baseten.co/observability/export-metrics/overview

Export metrics from Baseten to your observability stack

Baseten provides a metrics endpoint in Prometheus format, allowing integration with observability tools like Prometheus, OpenTelemetry Collector, Datadog Agent, and Vector.

## Setting Up Metrics Scraping

<Steps>
  <Step title="Scrape endpoint: https://app.baseten.co/metrics" />

  <Step title="Authentication">
    Use the Authorization header with a [Baseten API key](https://app.baseten.co/settings/api_keys):

    ```json theme={"system"}
    {"Authorization": "Api-Key YOUR_API_KEY"}
    ```
  </Step>

  <Step title="Scrape interval ">
    Recommended 1-minute interval (metrics update every 30 seconds).
  </Step>
</Steps>

## Supported Integrations

Baseten metrics can be collected via [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) and exported to:

* [Prometheus](/observability/export-metrics/prometheus)
* [Datadog](/observability/export-metrics/datadog)
* [Grafana](/observability/export-metrics/grafana)
* [New Relic](/observability/export-metrics/new-relic)

For available metrics, see the [supported metrics reference](/observability/export-metrics/supported-metrics).

## Rate Limits

* **6 requests per minute per organization**
* Exceeding this limit results in **HTTP 429 (Too Many Requests)** responses.
* To stay within limits, use a **1-minute scrape interval**.


# Export to Prometheus
Source: https://docs.baseten.co/observability/export-metrics/prometheus

Export metrics from Baseten to Prometheus

To integrate with Prometheus, specify the Baseten metrics endpoint in a scrape config. For example:

```yaml prometheus.yml theme={"system"}
global:
  scrape_interval: 60s
scrape_configs:
  - job_name: 'baseten'
    metrics_path: '/metrics'
    authorization:
      type: "Api-Key"
      credentials: "{BASETEN_API_KEY}"
    static_configs:
      - targets: ['app.baseten.co']
    scheme: https
```

See the Prometheus docs for more details on [getting started](https://prometheus.io/docs/prometheus/latest/getting_started/) and [configuration options](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).


# Metrics support matrix
Source: https://docs.baseten.co/observability/export-metrics/supported-metrics

Which metrics can be exported

## `baseten_inference_requests_total`

Cumulative number of requests to the model.

Type: `counter`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The status code of the response.
</ParamField>

<ParamField type="label">
  Whether the request was an [async inference request](/inference/async).
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_end_to_end_response_time_seconds`

End-to-end response time in seconds.

Type: `histogram`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The status code of the response.
</ParamField>

<ParamField type="label">
  Whether the request was an [async inference request](/inference/async).
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_container_cpu_usage_seconds_total`

Cumulative CPU time consumed by the container in core-seconds.

Type: `counter`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The ID of the replica.
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_replicas_active`

Number of replicas ready to serve model requests.

Type: `gauge`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_replicas_starting`

Number of replicas starting up--i.e. either waiting for resources to be available or loading the model.

Type: `gauge`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_container_cpu_memory_working_set_bytes`

Working set memory usage of the container in bytes.

Type: `gauge`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The ID of the replica.
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_request_size_bytes`

Request size in bytes. Proxy for input tokens.

Type: `histogram`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The status code of the response.
</ParamField>

<ParamField type="label">
  Whether the request was an [async inference request](/inference/async).
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_response_size_bytes`

Response size in bytes. Proxy for generated tokens.

Type: `histogram`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The status code of the response.
</ParamField>

<ParamField type="label">
  Whether the request was an [async inference request](/inference/async).
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_time_to_first_byte_seconds`

Time to first byte/write in seconds. Proxy for time-to-first-token (TTFT).

Type: `histogram`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The status code of the response.
</ParamField>

<ParamField type="label">
  Whether the request was an [async inference request](/inference/async).
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_time_in_async_queue_seconds`

Time async requests spend queued before processing.

Type: `histogram`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_async_queue_size`

Number of queued async requests over time.

Type: `gauge`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_gpu_memory_used`

GPU memory used in MiB.

Type: `gauge`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The ID of the replica.
</ParamField>

<ParamField type="label">
  The ID of the GPU.
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_gpu_utilization`

GPU utilization as a percentage (between 0 and 100).

Type: `gauge`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The ID of the replica.
</ParamField>

<ParamField type="label">
  The ID of the GPU.
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_ongoing_websocket_connections`

Number of ongoing websocket connections.

Type: `gauge`

Labels:

<ParamField type="label">
  The ID of the model.
</ParamField>

<ParamField type="label">
  The name of the model.
</ParamField>

<ParamField type="label">
  The ID of the deployment.
</ParamField>

<ParamField type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>


# Status and health
Source: https://docs.baseten.co/observability/health

Every model deployment in your Baseten workspace has a status to represent its activity and health.

## Model statuses

**Healthy states:**

* **Active**: The deployment is active and available. It can be called with `truss predict` or from its API endpoints.
* **Scaled to zero**: The deployment is active but is not consuming resources. It will automatically start up when called, then scale back to zero after traffic ceases.
* **Starting up**: The deployment is starting up from a scaled to zero state after receiving a request.
* **Inactive**: The deployment is unavailable and is not consuming resources. It may be manually reactivated.

**Error states:**

* **Unhealthy**: The deployment is active but is in an unhealthy state due to errors while running, such as an external service it relies on going down or a problem in your Truss that prevents it from responding to requests.
* **Build failed**: The deployment is not active due to a Docker build failure.
* **Deployment failed**: The deployment is not active due to a model deployment failure.

## Fixing unhealthy deployments

If you have an unhealthy or failed deployment, check the model logs to see if there's any indication of what the problem is. You can try deactivating and reactivating your deployment to see if the issue goes away. In the case of an external service outage, you may need to wait for the service to come back up before your deployment works again. For issues inside your Truss, you'll need to diagnose your code to see what is making it unresponsive.


# Metrics
Source: https://docs.baseten.co/observability/metrics

Understand the load and performance of your model

The Metrics tab in the model dashboard provides deployment-specific insights into model load and performance. Use the dropdowns to filter by environment or deployment and time range.

<img />

## Inference volume

Tracks the request rate over time, segmented by HTTP status codes:

* `2xx`: 🟢 Successful requests
* `4xx`: 🟡 Client errors
* `5xx`: 🔴 Server errors (includes model prediction exceptions)

<Note>
  Note that for non-HTTP models and Chains (WebSockets and gRPC), the status codes will
  reflect the status codes for those protocols.
</Note>

***

## Response time

Measured at different percentiles (p50, p90, p95, p99):

* **End-to-end response time:** Includes cold starts, queuing, and inference (excludes client-side latency). Reflects real-world performance.
* **Inference time:** Covers only model execution, including pre/post-processing. Useful for optimizing single-replica performance.
* **Time to first byte:** Measures the time-to-first-byte time distribution, including any queueing and routing time. A proxy for TTFT.

***

## Request and response size

Measured at different percentiles (p50, p90, p95, p99):

* **Request size:** Tracks the request size distribution. A proxy for input tokens.
* **Response size:** Tracks the response size distribution. A proxy for generated tokens.

***

## Replicas

Tracks the number of **active** and **starting** replicas:

* **Starting:** Waiting for resources or loading the model.
* **Active:** Ready to serve requests.
* For development deployments, a replica is considered active while running the live reload server.

***

## CPU usage and memory

Displays resource utilization across replicas. Metrics are averaged and may not capture short spikes.

### Considerations:

* **High CPU/memory usage**: May degrade performance—consider upgrading to a larger instance type.
* **Low CPU/memory usage**: Possible overprovisioning—switch to a smaller instance to reduce costs.

***

## GPU usage and memory

Shows GPU utilization across replicas.

* **GPU usage**: Percentage of time a kernel function occupies the GPU.
* **GPU memory**: Total memory used.

### Considerations:

* **High GPU load**: Can slow inference—check response time metrics.
* **High memory usage**: May cause out-of-memory failures.
* **Low utilization**: May indicate overprovisioning—consider a smaller GPU.

***

## Async Queue Metrics

* **Time in Async Queue**: Time spent in the async queue before execution (p50, p90, p95, p99).
* **Async Queue Size**: Number of queued async requests.

### Considerations:

* Large queue size indicates requests are queued faster than they are processed.
* To improve async throughput, increase the max replicas or adjust autoscaling concurrency.


# Secure model inference
Source: https://docs.baseten.co/observability/security

Keeping your models safe and private

Baseten maintains [SOC 2 Type II certification](https://www.baseten.co/blog/soc-2-type-2) and [HIPAA compliance](https://www.baseten.co/blog/baseten-announces-hipaa-compliance), with robust security measures beyond compliance.

## Data privacy

Baseten does not store model inputs, outputs, or weights by default.

* **Model inputs/outputs**: Inputs for [async inference](/inference/async) are temporarily stored until processed. Outputs are never stored.
* **Model weights**: Loaded dynamically from sources like Hugging Face, GCS, or S3, moving directly to GPU memory.
  * Users can enable caching via Truss. Cached weights can be permanently deleted on request.
* **Postgres data tables**: Existing users may store data in Baseten’s hosted Postgres tables, which can be deleted anytime.

Baseten’s network accelerator optimizes model downloads. [Contact support](mailto:support@baseten.co) to disable it.

## Workload security

Inference workloads are isolated to protect users and Baseten’s infrastructure.

* **Container security**:
  * No GPUs are shared across users.
  * Security tooling: Falco (Sysdig), Gatekeeper (Pod Security Policies).
  * Minimal privileges for workloads and nodes to limit incident impact.
* **Network security**:
  * Each customer has a dedicated Kubernetes namespace.
  * Isolation enforced via [Calico](https://docs.tigera.io/calico/latest/about).
  * Nodes run in a private subnet with firewall protections.
* **Pentesting**:
  * Extended pentesting by [RunSybil](https://www.runsybil.com/) (ex-OpenAI and CrowdStrike experts).
  * Malicious model deployments tested in a dedicated prod-like environment.

## Self-hosted model inference

Baseten offers single-tenant environments and self-hosted deployments. The cloud version is recommended for ease of setup, cost efficiency, and elastic GPU access.

For self-hosting, [contact support](mailto:support@baseten.co).


# Tracing
Source: https://docs.baseten.co/observability/tracing

Investigate the prediction flow in detail

Baseten’s Truss server includes built-in [OpenTelemetry](https://opentelemetry.io/) (OTEL) instrumentation, with support for custom tracing.

Tracing helps diagnose performance bottlenecks but introduces minor overhead, so it is **disabled by default**.

## Exporting builtin trace data to Honeycomb

1. **Create a Honeycomb API** key and add it to[ Baseten secrets](https://app.baseten.co/settings/secrets).
2. **Update** `config.yaml` for the target model:

```yaml config.yaml theme={"system"}
environment_variables:
  HONEYCOMB_DATASET: your_dataset_name
runtime:
  enable_tracing_data: true
secrets:
  HONEYCOMB_API_KEY: '***'
```

3. **Send requests with tracing**

* Provide traceparent headers for distributed tracing.
* If omitted, Baseten generates random trace IDs.

## Adding custom OTEL instrumentation

To define custom spans and events, integrate OTEL directly:

```python model.py theme={"system"}
import time
from typing import Any, Generator

import opentelemetry.exporter.otlp.proto.http.trace_exporter as oltp_exporter
import opentelemetry.sdk.resources as resources
import opentelemetry.sdk.trace as sdk_trace
import opentelemetry.sdk.trace.export as trace_export
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider

trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({resources.SERVICE_NAME: "UserModel"}))
)
tracer = trace.get_tracer(__name__)
trace_provider = trace.get_tracer_provider()


class Model:
    def __init__(self, **kwargs) -> None:
        honeycomb_api_key = kwargs["secrets"]["HONEYCOMB_API_KEY"]
        honeycomb_exporter = oltp_exporter.OTLPSpanExporter(
            endpoint="https://api.honeycomb.io/v1/traces",
            headers={
                "x-honeycomb-team"   : honeycomb_api_key,
                "x-honeycomb-dataset": "marius_testing_user",
            },
        )
        honeycomb_processor = sdk_trace.export.BatchSpanProcessor(honeycomb_exporter)
        trace_provider.add_span_processor(honeycomb_processor)

    @tracer.start_as_current_span("load_model")
    def load(self):
        ...

    def preprocess(self, model_input):
        with tracer.start_as_current_span("preprocess"):
            ...
            return model_input

    @tracer.start_as_current_span("predict")
    def predict(self, model_input: Any) -> Generator[str, None, None]:
        with tracer.start_as_current_span("start-predict") as span:
            def inner():
                time.sleep(0.01)
                for i in range(5):
                    span.add_event("yield")
                    yield str(i)

            return inner()
```

Baseten’s built-in tracing **does not interfere** with user-defined OTEL implementations.


# Billing and usage
Source: https://docs.baseten.co/observability/usage

Manage payments and track overall Baseten usage

The [billing and usage dashboard](https://app.baseten.co/settings/billing) provides a breakdown of model usage and costs, updated hourly. Usage is tracked per deployment, and any available credits are automatically applied to your bill.

## Billing

### Credits

* New workspaces receive free credits for testing and deployment.
* If credits run out and no payment method is set, models will be deactivated until a payment method is added.

### Payment method

* Payment details can be added or updated on the [billing page](https://app.baseten.co/settings/billing).
* Payment information is securely stored with our payment processor, not Baseten.

On the [billing page](https://app.baseten.co/settings/billing), you can set and update your payment method. Your payment information, including credit card numbers and bank information, is always stored securely with our payments processor and not by Baseten directly.

### Invoice history

* View past invoices and payments in the billing dashboard.
* For questions, [contact support](mailto:support@baseten.co).

***

## Usage and billing FAQs

For full details, see our [pricing page](https://www.baseten.co/pricing/), but here are answers to some common questions:

### How exactly is usage calculated?

* Usage is billed per minute while a model is deploying, scaling, or serving requests.
* Costs are based on the [instance type](/deployment/resources#choosing-the-right-instance-type) used.

### How often are payments due?

* Initially, charges occur when usage **exceeds \$50** or at the **end of the month**, whichever comes first.
* After a history of successful payments, billing occurs **monthly**.

### Do you offer volume discounts?

* Volume discounts are available on the **Pro plan**. [Contact support](mailto:support@baseten.co) for details.

### Do you offer education and non-profit discounts?

* Yes, discounts are available for educational and nonprofit ML projects. [Contact support](mailto:support@baseten.co) to apply.


# Access control
Source: https://docs.baseten.co/organization/access

Manage access to your Baseten organization with role-based access control.

Baseten uses role-based access control (RBAC) to manage organization access.
Every organization member has one of two roles.

| Permission               | Admin | Member |
| :----------------------- | ----- | ------ |
| Manage members           | ✅     | ❌      |
| Manage billing           | ✅     | ❌      |
| Deploy models and Chains | ✅     | ✅      |
| Call models              | ✅     | ✅      |

**Admins** have full control over the organization, including member management and billing.
**Members** can deploy and call models but cannot manage organization settings or other users.

<Note>
  If your organization uses multiple teams, see [Teams](/organization/teams) for information about team-level roles and permissions.
</Note>


# API keys
Source: https://docs.baseten.co/organization/api-keys

Authenticate requests to Baseten for deployment, inference, and management.

API keys authenticate your requests to Baseten. You need an API key to:

* Deploy models, Chains, and training projects with the Truss CLI.
* Call model endpoints for inference.
* Use the management API.

## API key types

Baseten supports two types of API keys:

**Personal API keys** are tied to your user account. Actions performed with a personal key are attributed to you. Use personal keys for local development and testing.

**Team API keys** are not tied to an individual user. When your organization has [teams](/organization/teams) enabled, team keys can be scoped to a specific team. Team keys can have different permission levels:

* **Full access** - Deploy models, call endpoints, and manage resources.
* **Inference only** - Call model endpoints but cannot deploy or manage.
* **Metrics only** - Export metrics but cannot deploy or call models.

Use team keys for CI/CD pipelines, production applications, and shared automation.

<Note>
  If your organization uses [teams](/organization/teams), Team Admins can create team API keys scoped to their team. See [Teams](/organization/teams) for more information.
</Note>

## Create an API key

To create an API key:

1. Navigate to [API keys](https://app.baseten.co/settings/api_keys) in your account settings.
2. Select **Create API key**.
3. Choose **Personal** or **Team** key type.
4. Enter a name for the key (lowercase letters, numbers, and hyphens only).
5. For team keys, select the permission level.
6. Select **Next**.

Copy the key immediately, you won't be able to view it again.

## Use API keys with the CLI

The first time you run `truss push`, the CLI prompts you for your API key and saves it to `~/.trussrc`:

```
$ truss push --watch
💻 Let's add a Baseten remote!
🤫 Quietly paste your API_KEY:
💾 Remote config `baseten` saved to `~/.trussrc`.
```

To manually configure or update your API key, edit `~/.trussrc`:

```sh theme={"system"}
[baseten]
remote_provider = baseten
api_key = YOUR_API_KEY
```

## Use API keys with endpoints

To call model endpoints with your API key, see [Call your model](/inference/calling-your-model).

## Manage API keys

The [API keys page](https://app.baseten.co/settings/api_keys) shows all your keys with their creation date and last used timestamp. Use this information to identify unused keys.

To rename a key, select the pencil icon next to the key name.

To rotate a key, create a new key, update your applications to use it, then revoke the old key.

To revoke a key, select the trash icon next to the key. Revoked keys cannot be restored.

You can also manage API keys programmatically with the [REST API](/reference/management-api/api-keys/creates-an-api-key).

### Security recommendations

* Store API keys in environment variables or secret managers, not in code.
* Never commit API keys to version control.
* Use team keys with minimal permissions for production applications.
* Rotate keys periodically and revoke unused keys.


# Organization settings
Source: https://docs.baseten.co/organization/overview

Manage your Baseten organization's access, security, and resources.

* **[Access control](/organization/access)**: Manage roles and permissions.
* **[Teams](/organization/teams)**: Segment resources across multiple teams (Enterprise).
* **[API keys](/organization/api-keys)**: Authenticate requests for deployment, inference, and management.
* **[Secrets](/organization/secrets)**: Store and access sensitive credentials in deployed models.
* **[Restricted environments](/organization/restricted-environments)**: Control environment access.


# Restricted environments
Source: https://docs.baseten.co/organization/restricted-environments

Control access to sensitive environments like production with environment-level permissions.

Restricted environments let organization Admins lock down specific environments so that
only designated users can modify settings and configurations.
Use restricted environments to prevent unauthorized changes to critical
environments like production.

For more information on user roles, see
[Access control](/organization/access) and
[Environments](/deployment/environments).

## How restricted environments work

By default, environments are unrestricted, meaning any organization member can modify
deployments, autoscaling settings, and other configurations.
When you mark an environment as restricted, only users you explicitly grant access can
make changes.

Restricted environments apply across all models and Chains in your organization.
For example, if you restrict an environment named `production`, that restriction applies to
every model and chain's production environment, not just one specific model or chain.

<Note>
  If your organization uses [teams](/organization/teams), restricted environments are scoped to individual teams.
  Team Admins can create and manage restricted environments for their team.
</Note>

### Permissions by access level

| Action                                 | With access | Without access |
| :------------------------------------- | ----------- | -------------- |
| View environment and configuration     | ✅           | ✅ (read-only)  |
| View metrics                           | ✅           | ✅ (read-only)  |
| Call inference on models and chains    | ✅           | ✅              |
| View logs                              | ✅           | ✅              |
| Modify deployment settings             | ✅           | ❌              |
| Change autoscaling configurations      | ✅           | ❌              |
| Promote deployments to the environment | ✅           | ❌              |
| Manage environment-specific settings   | ✅           | ❌              |

Users without access see a grayed-out UI for restricted actions.
They retain full read access and can still call inference endpoints.

## Managing restricted environments

Only organization **Admins** can create or modify restricted environments.
Members (non-admin users) can only create unrestricted environments and cannot change
environment restrictions.

### From the environments page

1. Navigate to **Settings** and then choose **Environments**.
2. Select an existing environment to modify, or select **Create environment** to create a new one.
3. Set the access level to **Restricted**.
4. Add users by searching by name or by email.
5. Select **Save changes** or **Create environment**.

### From a model or chain

1. Go to your model or chain's management page.
2. Select an existing environment to modify, or select **Add environment** then **Create environment** to create a new one.
3. Set the access level to **Restricted**.
4. Add users by searching by name or by email.
5. Select **Save changes** or **Create environment**.

<Note>
  Only admins can create restricted environments, and all admins have implicit
  access to every restricted environment. If an admin is later demoted to a member
  role, they lose this implicit access and can be removed from the environment
  like any other member.
</Note>

## API behavior

Restricted environments apply the same permission checks to
[API](/reference/management-api/environments/create-an-environment) and
[truss CLI](/reference/cli/truss/push) operations as the UI. API keys inherit
the permissions of their associated user.

If you attempt to modify a restricted environment using an API key associated with a
user without access, you'll receive a `403 Forbidden` error.

This includes operations like:

* Promoting deployments through the
  [promote endpoint](/reference/management-api/deployments/promote/promotes-a-deployment-to-an-environment).

* Updating autoscaling settings through the
  [autoscaling endpoint](/reference/management-api/deployments/autoscaling/updates-a-deployments-autoscaling-settings).

* Modifying environment configurations through the
  [update environment endpoint](/reference/management-api/environments/update-an-environments-settings).

Users without access can still call inference endpoints, as restrictions only apply to
management operations.


# Secrets
Source: https://docs.baseten.co/organization/secrets

Store and access sensitive credentials in your deployed models.

Secrets store sensitive credentials like API keys, access tokens, and passwords that your models need at runtime.
Secrets are encrypted and injected into your model's environment when it runs.

<Note>
  If your organization uses [teams](/organization/teams), secrets are scoped to individual teams.
  Models, Chains, and training projects deployed to a team can only access that team's secrets.
</Note>

## Create a secret

To create a secret:

1. Navigate to the **Secrets** tab in your settings. If your organization uses [teams](/organization/teams), navigate to the team's settings page.
2. Enter a name for the secret.
3. Enter the secret value.
4. Select **Add secret**.

Secret names follow these rules:

* Non-alphanumeric characters are normalized (for example, `hf_access_token` and `hf-access-token` are treated as the same name).
* Editing a secret's value overwrites the previous value.
* Changes take effect immediately for all deployments using the secret.

## Use secrets in your model

To use secrets in your Truss model, see [Secrets](/development/model/secrets).

## Security recommendations

* Create secrets through the Baseten dashboard, not in code.
* Use descriptive names that indicate the secret's purpose.
* Rotate secrets periodically by updating the value in the dashboard.
* Delete unused secrets to reduce exposure risk.


# Teams 🆕
Source: https://docs.baseten.co/organization/teams

Organize your organization into multiple teams with isolated resources and granular access control.

Teams let you segment your Baseten organization into multiple isolated
groups, each with its own resources, members, and access controls. Use teams to
separate environments by function, project, or access level.

<Note>
  Teams are available for organizations on our Enterprise tier.
  [Contact us](mailto:support@baseten.co) to enable teams for your
  organization.
</Note>

## How teams work

Every organization has a **default team** that contains all existing resources.
In the single-team world, you work within this default team without seeing any
team-specific UI.

When teams are enabled, Organization Admins can create additional teams within the
organization. Each team operates as an isolated unit with its own:

* Models, Chains, and training projects
* Secrets
* Team-level API keys
* Restricted environments
* Team members and roles

Billing remains at the organization level. All teams within an organization
share the same billing account and usage tracking.

## Roles and permissions

Teams introduce a two-level role hierarchy:

* Organization roles
* Team roles

### Organization roles

Organization-level roles determine what a user can do across the entire organization:

| Permission                  | Admin | Member |
| :-------------------------- | ----- | ------ |
| Manage billing              | ✅     | ❌      |
| Manage teams                | ✅     | ❌      |
| Manage organization members | ✅     | ❌      |
| View all teams              | ✅     | ❌      |

Organization Admins have implicit admin-level access to all teams and all restricted environments.

### Team roles

Team-level roles determine what a user can do within a specific team:

| Permission                                   | Team Admin | Team Member |
| :------------------------------------------- | ---------- | ----------- |
| Manage team members                          | ✅          | ❌           |
| Create restricted environments               | ✅          | ❌           |
| Create team API keys                         | ✅          | ❌           |
| Deploy models, Chains, and training projects | ✅          | ✅           |
| Call models                                  | ✅          | ✅           |
| View team resources                          | ✅          | ✅           |

A user can have different roles in different teams. For example, a data scientist might be a Team Admin for the Research team where they run experiments, while having Team Member access to the Inference team to deploy trained models.

## Manage teams

Organization Admins can create and delete teams. Team Admins can manage membership within their teams.

### Create a team

To create a team:

1. From the left navigation, select the dropdown next to the team name and select **Create new team**.
2. Enter a team name and optionally select an icon.
3. Choose **Create team**.

The default team cannot be deleted, but you can rename it.

### Invite members to a team

To invite a new member and add them to teams:

1. Navigate to **Organization settings** and select the **Members** tab.
2. Select **Invite member**.
3. Enter the member's email address.
4. Select the organization role: **Admin** or **Member**.
5. Select the teams to add them to.
6. For each team, set their team role: **Team Admin** or **Team Member**.
7. Select **Invite member**.

The invited user receives an email to join the organization and is automatically added to the selected teams with the specified roles.

To add an existing organization member to a team, navigate to the team's settings page, select the **Members** tab, and add them from there.

### Remove a member

To remove a member from the organization:

1. Navigate to **Organization settings** and select the **Members** tab.
2. Find the member you want to remove.
3. Select the trash icon next to their name.

Removing a member from the organization removes them from all teams.

To remove a member from a specific team without removing them from the organization, navigate to the team's settings page, select the **Members** tab, and remove them from there.

### Change a member's role

To change a member's organization or team roles:

1. Navigate to **Organization settings** and select the **Members** tab.
2. Select the pencil icon next to the member's name.
3. Update their organization role or team assignments as needed.
4. Select **Save changes**.

You can also change a member's team role from the team's settings page by navigating to the **Members** tab.

### Switch between teams

Use the team selector in the navigation to switch between teams.
The team selector displays all teams you have access to.
Selecting a team filters the view to show only that team's resources and settings.

## Team-scoped resources

### Secrets

Secrets are scoped to individual teams.
Each team maintains its own set of secrets, and models deployed to a team can only access that team's secrets.

To manage secrets for a team:

1. Switch to the team using the team selector in the navigation.
2. Navigate to **Settings** and select **Secrets**.
3. Add or modify secrets for that team.

For more information, see [Best practices for secrets](/organization/secrets).

### API keys

API keys can be personal or team-scoped:

* **Personal API keys** are tied to your user account and provide access to resources across all teams you belong to. Use personal keys for local development and testing.
* **Team API keys** are scoped to a single team and can only access that team's resources. Use team keys for automation and production deployments. Only Team Admins and organization Admins can create team API keys.

To create a team API key:

1. Navigate to **Settings** and select **API Keys**.
2. Select **Create API Key**.
3. Choose the team to scope the key to.
4. Name the key and select **Create**.

For more information, see [Best practices for API keys](/organization/api-keys).

### Restricted environments

Restricted environments work at the team level. When you create a restricted
environment, it applies to all models and Chains within that team.

For more information, see
[Restricted environments](/organization/restricted-environments).

## Deploy to a team

To deploy to a team, you can use the Truss CLI or the UI.

### Use the Truss CLI

To deploy a model to a specific team, use the `--team` flag with `truss push`. For development:

```sh theme={"system"}
truss push --watch --team your-team-name
```

Or for production:

```sh theme={"system"}
truss push --publish --team your-team-name
```

If you omit the `--team` flag, Truss infers the target team using the following logic:

1. If you belong to only one team, Truss deploys to that team.
2. If a model with the same name exists in only one of your accessible teams, Truss deploys to that team.
3. If there is ambiguity (for example, the same model name exists in multiple teams), Truss prompts you to select a team.

### Use the UI

The team selector determines which team a model belongs to when you create or deploy through the Baseten console.
To deploy to a specific team, switch to that team before creating or deploying resources.

## Considerations

### Model APIs

Model APIs are only available in the default team.
You cannot create or access Model APIs from other teams.

### Billing

Billing is managed at the organization level.
There is no team-level billing breakdown or budget controls.
All usage across teams is aggregated in the organization's billing dashboard, which is visible only to organization Admins.

### Resource naming

Model and Chain names must be unique within a team.
The same name can exist in different teams, but this may require explicit team specification when using the Truss CLI.

## Migrate to multiple teams

When teams are enabled for your organization, all existing resources remain in the default team.
You can then create additional teams and organize resources based on your needs.

Common team structures include:

* **By organizational structure**: Create teams for distinct departments or groups within your organization using Baseten. The recommended way to manage environments on Baseten is with [deployment environments](/deployment/environments), since this allows for centralized management, promotion workflows, and varying levels of access control.
* **By function**: Separate teams for different projects or use cases (for example, a training team and an inference team).
* **By access level**: Separate teams based on who should have access to modify production resources.

There is no single correct way to structure teams.
Consider your organization's access control needs, how you want to isolate secrets and credentials, and how different groups within your organization work with Baseten.

To move a model or Chain to a different team, redeploy it while switched to the target team. The original resource in the default team can then be deleted if no longer needed.


# Documentation
Source: https://docs.baseten.co/overview

Baseten is a platform for deploying and serving AI models performantly, scalably, and cost-efficiently.

<div />

<div>
  <h1>
    Build with Baseten
  </h1>

  <div>
    Baseten is a platform for deploying and serving AI models performantly,
    scalably, and cost-efficiently.
  </div>

  <CardGroup>
    <Card title="Quick start" href="/quickstart">
      Choose from common AI/ML usecases and modalities to get started on Baseten quickly.
    </Card>

    <Card title="How Baseten works" href="/concepts/howbasetenworks">
      Baseten makes it easy to deploy, serve, and scale AI models so you can focus on building, not infrastructure.
    </Card>
  </CardGroup>

  <div>
    <h2>
      Baseten is an inference and training platform that lets you:
    </h2>

    #### Deploy dedicated models with full control

    * [Package any model for production](/development/model/overview): Define dependencies, hardware, and custom code without needing to learn Docker. Build with your preferred frameworks (e.g., PyTorch, transformers, diffusers), [inference engines](/development/model/performance-optimization) (e.g., TensorRT-LLM, SGLang, vLLM), and serving tools (e.g., Triton) as well as [any package](/development/model/configuration) installable via `pip` or `apt`.

    * [Build complex AI systems](/development/chain/overview): Orchestrate multi-step workflows with [Chains](/development/chain/overview), combining models, business logic, and external APIs.

    * [Deploy with confidence](/deployment/concepts): [Autoscale](/deployment/autoscaling) models, manage [environments](/deployment/environments), and roll out updates with zero-downtime deployments.

    * [Run high-performance inference](/inference/concepts): Serve [synchronous](/inference/calling-your-model), [asynchronous](/inference/async), and [streaming](/inference/streaming) predictions with low-latency execution controls.

    * [Monitor and optimize in production](/observability/metrics): Monitor performance, debug issues, and [export metrics](/observability/export-metrics/overview) with built-in observability tooling.

    #### Start fast with model APIs

    * [Try model APIs](/development/model-apis/overview): Model APIs provide a fast path to production with reliable, high-performance inference. Use OpenAI-compatible endpoints to integrate models like Llama, DeepSeek, and Qwen, with built-in support for structured outputs and tool calling.

    #### Pre-train and fine-tune models

    * [Run training jobs on scalable infrastructure](/training/overview): Launch containerized training jobs with configurable environments, compute (CPU/GPU), and resource scaling. Supports any training framework via a framework-agnostic API.

    * [Manage artifacts and streamline workflows](/training/management): Track experiments, organize training runs, and handle large artifacts like checkpoints and logs. Seamlessly transition from training to deployment within the Baseten ecosystem.
  </div>

  <h1>
    Resources
  </h1>

  <CardGroup>
    <Card title="Examples" href="/examples/overview">
      From deploying AI models to optimizing inference and scaling ML models.
    </Card>

    <Card title="Model library" href="/examples/models/overview">
      Prebuilt, ready to deploy in one click models like DeepSeek, Llama, and
      Qwen.
    </Card>

    <Card title="Explore API reference" href="/reference/overview#api-reference">
      API reference for calling deployed models, Chains or managing models and
      your workspace.
    </Card>
  </CardGroup>
</div>


# Quick start
Source: https://docs.baseten.co/quickstart



<Steps>
  <Step title="What modality are you working with?">
    Choose from common modalities like LLMs, transcription, and image generation to get started quickly.

    <CardGroup>
      <Card title="LLMs" href="/quickstart/large-language-models">
        Build and deploy large language models
      </Card>

      <Card title="Transcription" href="/quickstart/transcription">
        Transcribe audio and video
      </Card>

      <Card title="Image generation" href="/quickstart/image-generation">
        Rapidly generate images
      </Card>

      <Card title="Text to speech" href="/quickstart/text-to-speech">
        Build humanlike experiences
      </Card>

      <Card title="Compound AI" href="/quickstart/compound-ai">
        Build real-time AI-native applications
      </Card>

      <Card title="Embeddings" href="/quickstart/embeddings">
        Process millions of data points
      </Card>

      <Card title="Custom models" href="/quickstart/custom-models">
        Deploy any model
      </Card>
    </CardGroup>
  </Step>

  <Step title="Select a model or guide to get started...">
    Choose a use case or modality above first...
  </Step>
</Steps>


# Chains CLI reference
Source: https://docs.baseten.co/reference/cli/chains/chains-cli

Deploy, manage, and develop Chains using the Truss CLI.

```sh theme={"system"}
truss chains [OPTIONS] COMMAND [ARGS]...
```

| Command           | Description                |
| ----------------- | -------------------------- |
| [`init`](#init)   | Initialize a Chain project |
| [`push`](#push)   | Deploy a Chain             |
| [`watch`](#watch) | Live reload development    |

***

## `init`

Initialize a Chain project.

```sh theme={"system"}
truss chains init [OPTIONS] [DIRECTORY]
```

* `DIRECTORY` (optional): Path to a new or empty directory for the Chain. Defaults to the current directory if omitted.

**Options:**

* `--log` `[humanfriendly | INFO | DEBUG]`: Set log verbosity.
* `--help`: Show this message and exit.

**Example:**

To create a new Chain project in a directory called `my-chain`, use the following:

```sh theme={"system"}
truss chains init my-chain
```

***

## `push`

Deploy a Chain.

```sh theme={"system"}
truss chains push [OPTIONS] SOURCE [ENTRYPOINT]
```

* `SOURCE`: Path to a Python file that contains the entrypoint chainlet.
* `ENTRYPOINT` (optional): Class name of the entrypoint chainlet. If omitted, the chainlet tagged with `@chains.mark_entrypoint` is used.

**Options:**

* `--name` (TEXT): Custom name for the Chain (defaults to entrypoint name).
* `--publish / --no-publish`: Create chainlets as a published deployment.
* `--promote / --no-promote`: Promote newly deployed chainlets into production.
* `--environment` (TEXT): Deploy chainlets into a particular environment.
* `--wait / --no-wait`: Wait until all chainlets are ready (or deployment failed).
* `--watch / --no-watch`: Watch the Chains source code and apply live patches. Using this option waits for the Chain to be deployed (the `--wait` flag is applied) before starting to watch for changes. This option requires the deployment to be a development deployment.
* `--experimental-chainlet-names` (TEXT): Run `watch`, but only apply patches to specified chainlets. The option is a comma-separated list of chainlet (display) names. This option can give faster dev loops, but also lead to inconsistent deployments. Use with caution and refer to [docs](/development/chain/watch).
* `--dryrun`: Produce only generated files, but don't deploy anything.
* `--remote` (TEXT): Name of the remote in .trussrc to push to.
* `--team` (TEXT): Name of the team to deploy to. If not specified, Truss infers the team or prompts for selection.
* `--log` `[humanfriendly|I|INFO|D|DEBUG]`: Customize logging.
* `--help`: Show this message and exit.

<Note>
  The `--team` flag is only available if your organization has teams enabled. [Contact us](mailto:support@baseten.co) to enable teams, or see [Teams](/organization/teams) for more information.
</Note>

**Example:**

To deploy a Chain as a development deployment, use the following:

```sh theme={"system"}
truss chains push my_chain.py
```

To deploy and promote to production, use the following:

```sh theme={"system"}
truss chains push my_chain.py --publish --promote
```

To deploy to a specific team, use the following:

```sh theme={"system"}
truss chains push my_chain.py --team my-team-name
```

***

## `watch`

Live reload development.

```sh theme={"system"}
truss chains watch [OPTIONS] SOURCE [ENTRYPOINT]
```

* `SOURCE`: Path to a Python file containing the entrypoint chainlet.
* `ENTRYPOINT` (optional): Class name of the entrypoint chainlet. If omitted, the chainlet tagged with `@chains.mark_entrypoint` is used.

**Options:**

* `--name` (TEXT): Name of the Chain to be deployed. If not given, the entrypoint name is used.
* `--remote` (TEXT): Name of the remote in .trussrc to push to.
* `--team` (TEXT): Name of the team to deploy to. If not specified, Truss infers the team or prompts for selection.

<Note>
  The `--team` flag is only available if your organization has teams enabled. [Contact us](mailto:support@baseten.co) to enable teams, or see [Teams](/organization/teams) for more information.
</Note>

* `--experimental-chainlet-names` (TEXT): Run `watch`, but only apply patches to specified chainlets. The option is a comma-separated list of chainlet (display) names. This option can give faster dev loops, but also lead to inconsistent deployments. Use with caution and refer to [docs](/development/chain/watch).
* `--log` `[humanfriendly|W|WARNING|I|INFO|D|DEBUG]`: Customize logging.
* `--help`: Show this message and exit.

**Example:**

To watch a Chain for live reload during development, use the following:

```sh theme={"system"}
truss chains watch my_chain.py
```


# Truss CLI overview
Source: https://docs.baseten.co/reference/cli/index

Install and configure the Truss CLI for deploying models, chains, and training jobs.

The `truss` CLI is your primary interface for everything from packaging and
deploying AI models to building and orchestrating multi-step chains to launching and
managing training jobs.

Use the following commands to manage your models, chains, and training jobs:

* **Models**: Package and deploy individual model servers.
* **Chains**: Build and deploy multi-step inference pipelines.
* **Training**: Launch and manage training jobs.

<Accordion title="Install the Truss CLI">
  To use Truss, install a recent Truss version and ensure pydantic is v2:

  ```bash theme={"system"}
  pip install --upgrade truss 'pydantic>=2.0.0'
  ```

  <Accordion title="Help for setting up a clean development environment">
    Truss requires python `>=3.9,<3.15`. To set up a fresh development environment,
    you can use the following commands, creating a environment named `truss_env`
    using `pyenv`:

    ```bash theme={"system"}
    curl https://pyenv.run | bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc
    source ~/.bashrc
    pyenv install 3.11.0
    ENV_NAME="truss_env"
    pyenv virtualenv 3.11.0 $ENV_NAME
    pyenv activate $ENV_NAME
    pip install --upgrade truss 'pydantic>=2.0.0'
    ```
  </Accordion>

  To deploy Truss remotely, you also need a
  [Baseten account](https://app.baseten.co/signup).
  It is handy to export your API key to the current shell session or permanently in your `.bashrc`:

  ```bash ~/.bashrc theme={"system"}
  export BASETEN_API_KEY="nPh8..."
  ```
</Accordion>

## CLI structure

The `truss` CLI organizes commands by workflow:

```
truss [OPTIONS] COMMAND [ARGS]...
```

### Model commands

Use these commands to package, deploy, and iterate on individual models.

| Command                                               | Description                       |
| ----------------------------------------------------- | --------------------------------- |
| [`truss login`](/reference/cli/truss/login)           | Authenticate with Baseten         |
| [`truss init`](/reference/cli/truss/init)             | Create a new Truss project        |
| [`truss push`](/reference/cli/truss/push)             | Deploy a model to Baseten         |
| [`truss watch`](/reference/cli/truss/watch)           | Live reload during development    |
| [`truss predict`](/reference/cli/truss/predict)       | Call the packaged model           |
| [`truss model-logs`](/reference/cli/truss/model-logs) | Fetch logs for the packaged model |

### Chain commands

Use these commands to build multi-model pipelines with shared dependencies.

| Command                                                        | Description                    |
| -------------------------------------------------------------- | ------------------------------ |
| [`truss chains init`](/reference/cli/chains/chains-cli#init)   | Initialize a new Chain project |
| [`truss chains push`](/reference/cli/chains/chains-cli#push)   | Deploy a Chain to Baseten      |
| [`truss chains watch`](/reference/cli/chains/chains-cli#watch) | Live reload Chain development  |

### Training commands

Use these commands to launch, monitor, and manage training jobs.

| Command                                                         | Description                     |
| --------------------------------------------------------------- | ------------------------------- |
| [`truss train init`](/reference/cli/training/training-cli#init) | Initialize a training project   |
| [`truss train push`](/reference/cli/training/training-cli#push) | Deploy and run a training job   |
| [`truss train logs`](/reference/cli/training/training-cli#logs) | Stream logs from a training job |
| [`truss train view`](/reference/cli/training/training-cli#view) | List and inspect training jobs  |

## Authentication

After installing Truss, authenticate with Baseten using either method:

**Option 1: Environment variable (recommended for CI/CD)**

```sh theme={"system"}
export BASETEN_API_KEY="YOUR_API_KEY"
```

**Option 2: Interactive login**

```sh theme={"system"}
truss login
```

This opens a browser window to authenticate and stores your credentials locally.

## Next steps

<CardGroup>
  <Card title="Deploy your first model" icon="rocket" href="/examples/deploy-your-first-model">
    Package and deploy a model in minutes.
  </Card>

  <Card title="Build a Chain" icon="link" href="/development/chain/getting-started">
    Create multi-step inference pipelines.
  </Card>

  <Card title="Launch a training job" icon="dumbbell" href="/training/getting-started">
    Fine-tune models on Baseten infrastructure.
  </Card>

  <Card title="Truss configuration" icon="gear" href="/reference/truss-configuration">
    Configure dependencies, resources, and more.
  </Card>
</CardGroup>


# Training CLI reference
Source: https://docs.baseten.co/reference/cli/training/training-cli

Deploy, manage, and monitor training jobs using the Truss CLI.

The `truss train` command provides subcommands for managing the full training job lifecycle.

```sh theme={"system"}
truss train [COMMAND] [OPTIONS]
```

### Universal options

The following options are available for all `truss train` commands:

* `--help`: Show help message and exit.
* `--non-interactive`: Disable interactive prompts (for CI/automated environments).
* `--remote TEXT`: Name of the remote in `.trussrc`.

***

## init

Initialize a training project from templates or create an empty project.

```sh theme={"system"}
truss train init [OPTIONS]
```

### Options

<ParamField type="string">
  Template name or comma-separated list of templates to initialize. See the [ML Cookbook](https://github.com/basetenlabs/ml-cookbook) for available examples.
</ParamField>

<ParamField type="string">
  Directory to initialize the project in. Defaults to current directory.
</ParamField>

<ParamField>
  List all available example templates.
</ParamField>

### Examples

Initialize a project from a template:

```sh theme={"system"}
truss train init --examples llama-8b-lora-unsloth
```

Initialize multiple templates:

```sh theme={"system"}
truss train init --examples llama-8b-lora-unsloth,qwen3-8b-lora-dpo-trl
```

List available templates:

```sh theme={"system"}
truss train init --list-examples
```

Create an empty training project:

```sh theme={"system"}
truss train init
```

***

## push

Submit and run a training job.

```sh theme={"system"}
truss train push [OPTIONS] CONFIG
```

### Arguments

<ParamField type="string">
  Path to the training configuration file (e.g., `config.py`).
</ParamField>

### Options

<ParamField>
  Stream status and logs after submitting the job.
</ParamField>

<ParamField type="string">
  Name for the training job.
</ParamField>

<ParamField type="string">
  Team name for the training project. If not specified, Truss infers the team or prompts for selection.
</ParamField>

<Note>
  The `--team` flag is only available if your organization has teams enabled. [Contact us](mailto:support@baseten.co) to enable teams, or see [Teams](/organization/teams) for more information.
</Note>

### Examples

Submit a training job:

```sh theme={"system"}
truss train push config.py
```

Submit and stream logs:

```sh theme={"system"}
truss train push config.py --tail
```

Submit to a specific team:

```sh theme={"system"}
truss train push config.py --team my-team-name
```

Submit with a custom job name:

```sh theme={"system"}
truss train push config.py --job-name fine-tune-v1
```

***

## logs

Fetch and stream logs from a training job.

```sh theme={"system"}
truss train logs [OPTIONS]
```

### Options

<ParamField type="string">
  Job ID to fetch logs from.
</ParamField>

<ParamField type="string">
  Project name or project ID.
</ParamField>

<ParamField type="string">
  Project ID.
</ParamField>

<ParamField>
  Continuously stream new logs.
</ParamField>

### Examples

Stream logs for a specific job:

```sh theme={"system"}
truss train logs --job-id abc123 --tail
```

View logs for a job without streaming:

```sh theme={"system"}
truss train logs --job-id abc123
```

***

## metrics

View real-time metrics for a training job including CPU, GPU, and storage usage.

```sh theme={"system"}
truss train metrics [OPTIONS]
```

### Options

<ParamField type="string">
  Job ID to fetch metrics from.
</ParamField>

<ParamField type="string">
  Project name or project ID.
</ParamField>

<ParamField type="string">
  Project ID.
</ParamField>

### Examples

View metrics for a specific job:

```sh theme={"system"}
truss train metrics --job-id abc123
```

***

## view

List training projects and jobs, or view details for a specific job.

```sh theme={"system"}
truss train view [OPTIONS]
```

### Options

<ParamField type="string">
  View details for a specific training job.
</ParamField>

<ParamField type="string">
  View jobs for a specific project (name or ID).
</ParamField>

<ParamField type="string">
  View jobs for a specific project ID.
</ParamField>

### Examples

List all training projects:

```sh theme={"system"}
truss train view
```

View jobs in a specific project:

```sh theme={"system"}
truss train view --project my-project
```

View details for a specific job:

```sh theme={"system"}
truss train view --job-id abc123
```

***

## stop

Stop a running training job.

```sh theme={"system"}
truss train stop [OPTIONS]
```

### Options

<ParamField type="string">
  Job ID to stop.
</ParamField>

<ParamField type="string">
  Project name or project ID.
</ParamField>

<ParamField type="string">
  Project ID.
</ParamField>

<ParamField>
  Stop all running jobs. Prompts for confirmation.
</ParamField>

### Examples

Stop a specific job:

```sh theme={"system"}
truss train stop --job-id abc123
```

Stop all running jobs:

```sh theme={"system"}
truss train stop --all
```

***

## recreate

Recreate an existing training job with the same configuration.

```sh theme={"system"}
truss train recreate [OPTIONS]
```

### Options

<ParamField type="string">
  Job ID of the training job to recreate. If not provided, defaults to the last created job.
</ParamField>

<ParamField>
  Stream status and logs after recreating the job.
</ParamField>

### Examples

Recreate a specific job:

```sh theme={"system"}
truss train recreate --job-id abc123
```

Recreate and stream logs:

```sh theme={"system"}
truss train recreate --job-id abc123 --tail
```

***

## download

Download training job artifacts to your local machine.

```sh theme={"system"}
truss train download [OPTIONS]
```

### Options

<ParamField type="string">
  Job ID to download artifacts from.
</ParamField>

<ParamField type="path">
  Directory to download files to. Defaults to current directory.
</ParamField>

<ParamField>
  Keep the compressed archive without extracting.
</ParamField>

### Examples

Download artifacts to current directory:

```sh theme={"system"}
truss train download --job-id abc123
```

Download to a specific directory:

```sh theme={"system"}
truss train download --job-id abc123 --target-directory ./downloads
```

Download without extracting:

```sh theme={"system"}
truss train download --job-id abc123 --no-unzip
```

***

## deploy\_checkpoints

Deploy a trained model checkpoint to Baseten's inference platform.

```sh theme={"system"}
truss train deploy_checkpoints [OPTIONS]
```

### Options

<ParamField type="string">
  Job ID containing the checkpoints to deploy.
</ParamField>

<ParamField type="string">
  Project name or project ID.
</ParamField>

<ParamField type="string">
  Project ID.
</ParamField>

<ParamField type="string">
  Path to a Python file defining a `DeployCheckpointsConfig`.
</ParamField>

<ParamField>
  Generate a Truss config without deploying. Useful for previewing the deployment configuration.
</ParamField>

<ParamField type="string">
  Path to output the generated Truss config. Defaults to `truss_configs/<model_version_name>_<model_version_id>`.
</ParamField>

### Examples

Deploy checkpoints interactively:

```sh theme={"system"}
truss train deploy_checkpoints
```

Deploy checkpoints from a specific job:

```sh theme={"system"}
truss train deploy_checkpoints --job-id abc123
```

Preview deployment without deploying:

```sh theme={"system"}
truss train deploy_checkpoints --job-id abc123 --dry-run
```

***

## get\_checkpoint\_urls

Get presigned URLs for checkpoint artifacts.

```sh theme={"system"}
truss train get_checkpoint_urls [OPTIONS]
```

### Options

<ParamField type="string">
  Job ID containing the checkpoints.
</ParamField>

### Examples

Get checkpoint URLs for a job:

```sh theme={"system"}
truss train get_checkpoint_urls --job-id abc123
```

***

## cache summarize

View a summary of the training cache for a project.

```sh theme={"system"}
truss train cache summarize [OPTIONS] PROJECT
```

### Arguments

<ParamField type="string">
  Project name or project ID.
</ParamField>

### Options

<ParamField type="string">
  Sort files by column. Options: `filepath`, `size`, `modified`, `type`, `permissions`.
</ParamField>

<ParamField type="string">
  Sort order: `asc` (ascending) or `desc` (descending).
</ParamField>

<ParamField type="string">
  Output format: `cli-table` (default), `csv`, or `json`.
</ParamField>

### Examples

View cache summary:

```sh theme={"system"}
truss train cache summarize my-project
```

Sort by size descending:

```sh theme={"system"}
truss train cache summarize my-project --sort size --order desc
```

Export as JSON:

```sh theme={"system"}
truss train cache summarize my-project --output-format json
```

***

## Ignore files and folders

Create a `.truss_ignore` file in your project root to exclude files from upload. Uses `.gitignore` syntax.

```plaintext .truss_ignore theme={"system"}
# Python cache files
__pycache__/
*.pyc
*.pyo
*.pyd

# Type checking
.mypy_cache/

# Testing
.pytest_cache/

# Large data files
data/
*.bin
```


# truss cleanup
Source: https://docs.baseten.co/reference/cli/truss/cleanup

Clean up Truss data.

```sh theme={"system"}
truss cleanup [OPTIONS]
```

Clears temporary directories created by Truss for operations like building Docker images. Use this to free up disk space.

**Example:**

To clean up temporary Truss data, use the following:

```sh theme={"system"}
truss cleanup
```


# truss configure
Source: https://docs.baseten.co/reference/cli/truss/configure

Configure Truss settings.

```sh theme={"system"}
truss configure [OPTIONS]
```

Configures Truss settings interactively. Use this command to set up or modify your local Truss configuration.

**Example:**

To configure Truss settings interactively, use the following:

```sh theme={"system"}
truss configure
```

You should see a configuration file that you can edit, for example:

```yaml ~/.trussrc theme={"system"}
[baseten]
remote_provider = baseten
api_key = YOUR_API_KEY
remote_url = https://app.baseten.co
```


# truss container
Source: https://docs.baseten.co/reference/cli/truss/container

Run and manage Truss containers locally.

```sh theme={"system"}
truss container [OPTIONS] COMMAND [ARGS]...
```

Manage Docker containers for your Truss.

***

## `kill`

Kill containers related to a specific Truss.

```sh theme={"system"}
truss container kill [OPTIONS] [TARGET_DIRECTORY]
```

### Arguments

<ParamField type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To kill containers for the current Truss, use the following:

```sh theme={"system"}
truss container kill
```

***

## `kill-all`

Kill all Truss containers that are not manually persisted.

```sh theme={"system"}
truss container kill-all [OPTIONS]
```

**Example:**

To kill all Truss containers, use the following:

```sh theme={"system"}
truss container kill-all
```

***

## `logs`

Get logs from a running Truss container.

```sh theme={"system"}
truss container logs [OPTIONS] [TARGET_DIRECTORY]
```

### Arguments

<ParamField type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To view logs from the current Truss container, use the following:

```sh theme={"system"}
truss container logs
```


# truss image
Source: https://docs.baseten.co/reference/cli/truss/image

Build and manage Truss Docker images.

```sh theme={"system"}
truss image [OPTIONS] COMMAND [ARGS]...
```

Build and manage Docker images for your Truss.

***

## `build`

Build the Docker image for a Truss.

```sh theme={"system"}
truss image build [OPTIONS] [TARGET_DIRECTORY] [BUILD_DIR]
```

### Options

<ParamField type="TEXT">
  Docker image tag.
</ParamField>

### Arguments

<ParamField type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

<ParamField type="TEXT">
  Image context directory. If not provided, a temp directory is created.
</ParamField>

**Example:**

To build a Docker image for your Truss, use the following:

```sh theme={"system"}
truss image build
```

To build with a custom tag, use the following:

```sh theme={"system"}
truss image build --tag my-model:v1
```

***

## `build-context`

Create a Docker build context for a Truss without building the image.

```sh theme={"system"}
truss image build-context [OPTIONS] BUILD_DIR [TARGET_DIRECTORY]
```

### Arguments

<ParamField type="TEXT">
  Directory where image context is created.
</ParamField>

<ParamField type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To create a build context in a specific directory, use the following:

```sh theme={"system"}
truss image build-context ./build-context
```

***

## `run`

Run the Docker image for a Truss locally.

```sh theme={"system"}
truss image run [OPTIONS] [TARGET_DIRECTORY] [BUILD_DIR]
```

### Options

<ParamField type="TEXT">
  Docker image tag to run.
</ParamField>

<ParamField type="INTEGER">
  Local port to expose the model on.
</ParamField>

<ParamField>
  Attach to the container process.
</ParamField>

### Arguments

<ParamField type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

<ParamField type="TEXT">
  Image context directory. If not provided, a temp directory is created.
</ParamField>

**Example:**

To build and run a Truss locally, use the following:

```sh theme={"system"}
truss image run
```

To run on a specific port, use the following:

```sh theme={"system"}
truss image run --port 8080
```

To run in attached mode, use the following:

```sh theme={"system"}
truss image run --attach
```


# truss init
Source: https://docs.baseten.co/reference/cli/truss/init

Create a new Truss project.

```sh theme={"system"}
truss init [OPTIONS] TARGET_DIRECTORY
```

Creates a new Truss project in the specified directory with the standard file structure.

### Options

<ParamField type="TrussServer | TRT_LLM">
  Server type to create. Default: `TrussServer`.
</ParamField>

<ParamField type="TEXT">
  The value assigned to `model_name` in `config.yaml`.
</ParamField>

### Arguments

<ParamField type="TEXT">
  Directory where the Truss project is created.
</ParamField>

**Example:**

To create a new Truss project, use the following:

```sh theme={"system"}
truss init my-model
```

To create a Truss with a custom name, use the following:

```sh theme={"system"}
truss init --name "My Model" my-model
```

To create a Truss with TRT\_LLM backend, use the following:

```sh theme={"system"}
truss init --backend TRT_LLM my-trt-model
```


# truss login
Source: https://docs.baseten.co/reference/cli/truss/login

Authenticate with Baseten.

```sh theme={"system"}
truss login [OPTIONS]
```

Authenticates with Baseten, storing the API key in the local configuration file.

If used with no options, runs in interactive mode. Otherwise, the API key can be passed as an option.

### Options

<ParamField type="TEXT">
  Baseten API key. If provided, the command runs in non-interactive mode.
</ParamField>

**Example:**

To authenticate interactively, use the following:

```sh theme={"system"}
truss login
```

To authenticate with your API key, use the following:

```sh theme={"system"}
truss login --api-key YOUR_API_KEY
```


# truss model-logs
Source: https://docs.baseten.co/reference/cli/truss/model-logs

Fetch logs for a deployed model.

```sh theme={"system"}
truss model-logs [OPTIONS]
```

Fetches logs for a deployed model. Use this command to debug issues or monitor model behavior in production.

### Options

<ParamField type="TEXT">
  The ID of the model to fetch logs from.
</ParamField>

<ParamField type="TEXT">
  The ID of the deployment to fetch logs from.
</ParamField>

<ParamField>
  Tail for ongoing logs. Streams new log entries as they arrive.
</ParamField>

<ParamField type="TEXT">
  Name of the remote in .trussrc to fetch logs from.
</ParamField>

**Example:**

To fetch logs for a specific deployment, use the following:

```sh theme={"system"}
truss model-logs --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID
```

To stream logs in real-time, use the following:

```sh theme={"system"}
truss model-logs --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID --tail
```


# Truss CLI reference
Source: https://docs.baseten.co/reference/cli/truss/overview

Deploy, manage, and develop models using the Truss CLI.

```sh theme={"system"}
truss [OPTIONS] COMMAND [ARGS]...
```

**Options:**

<ParamField>
  Show the version and exit.
</ParamField>

<ParamField type="[humanfriendly|w|warning|i|info|d|debug]">
  Customize logging verbosity.
</ParamField>

<ParamField>
  Disable interactive prompts. Use in CI or automated execution contexts.
</ParamField>

<ParamField>
  Show help message and exit.
</ParamField>

### Main commands

| Command                                         | Description                       |
| ----------------------------------------------- | --------------------------------- |
| [`init`](/reference/cli/truss/init)             | Create a new Truss project        |
| [`push`](/reference/cli/truss/push)             | Deploy a model to Baseten         |
| [`watch`](/reference/cli/truss/watch)           | Live reload during development    |
| [`predict`](/reference/cli/truss/predict)       | Call the packaged model           |
| [`model-logs`](/reference/cli/truss/model-logs) | Fetch logs for the packaged model |

### Advanced commands

| Command                                       | Description                             |
| --------------------------------------------- | --------------------------------------- |
| [`image`](/reference/cli/truss/image)         | Build and manage Truss Docker images    |
| [`container`](/reference/cli/truss/container) | Run and manage Truss containers locally |
| [`cleanup`](/reference/cli/truss/cleanup)     | Clean up Truss data                     |

### Other commands

| Command                                         | Description                                  |
| ----------------------------------------------- | -------------------------------------------- |
| [`login`](/reference/cli/truss/login)           | Authenticate with Baseten                    |
| [`configure`](/reference/cli/truss/configure)   | Configure Truss settings                     |
| [`run-python`](/reference/cli/truss/run-python) | Run a Python script in the Truss environment |
| [`whoami`](/reference/cli/truss/whoami)         | Show user information and exit               |

<Note>
  All commands support `--help` to display usage information.
</Note>


# truss predict
Source: https://docs.baseten.co/reference/cli/truss/predict

Call the packaged model.

```sh theme={"system"}
truss predict [OPTIONS] [TARGET_DIRECTORY]
```

Calls the packaged model with the provided input data. Use this to test your model locally or remotely.

### Options

<ParamField type="TEXT">
  JSON string representing the request payload.
</ParamField>

<ParamField type="PATH">
  Path to a JSON file containing the request payload.
</ParamField>

<ParamField type="TEXT">
  Name of the remote in .trussrc to invoke.
</ParamField>

<ParamField type="TEXT">
  ID of the model to invoke.
</ParamField>

<ParamField type="TEXT">
  ID of the model version to invoke.
</ParamField>

<ParamField>
  Invoke the published (production) deployment.
</ParamField>

### Arguments

<ParamField type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To call a model with inline JSON data, use the following:

```sh theme={"system"}
truss predict -d '{"prompt": "What is the meaning of life?"}'
```

To call a model using a JSON file, use the following:

```sh theme={"system"}
truss predict -f request.json
```

To call the production deployment, use the following:

```sh theme={"system"}
truss predict --published -d '{"prompt": "Hello, world!"}'
```


# truss push
Source: https://docs.baseten.co/reference/cli/truss/push

Deploy a model to Baseten.

```sh theme={"system"}
truss push [OPTIONS] [TARGET_DIRECTORY]
```

Deploys a Truss to Baseten. By default, creates a published deployment.

<Note>
  Use `--watch` for development deployments with live reload support. Use `--publish` to explicitly create a published deployment.
</Note>

### Options

<ParamField type="TEXT">
  Name of the remote in .trussrc to push to.
</ParamField>

<ParamField>
  Push as a development deployment with live reload enabled. Use this for rapid iteration during development.
</ParamField>

<ParamField>
  Push as a published deployment. If no production deployment exists, promote to production after deploy completes.
</ParamField>

<ParamField>
  Push as a published deployment and promote to production, even if a production deployment already exists.
</ParamField>

<ParamField type="TEXT">
  Push as a published deployment and promote into the specified environment.
</ParamField>

<ParamField>
  Preserve the previous production deployment's autoscaling settings. Can only be used with `--promote`.
</ParamField>

<ParamField type="TEXT">
  Name of the model.
</ParamField>

<ParamField type="TEXT">
  Name of the deployment. Can only be used with `--publish` or `--environment`. Must contain only alphanumeric, `.`, `-` or `_` characters.
</ParamField>

<ParamField>
  Wait for deployment to complete before returning. Returns non-zero exit code if deploy or build fails.
</ParamField>

<ParamField type="INTEGER">
  Maximum time to wait for deployment in seconds.
</ParamField>

<ParamField type="TEXT">
  Name of the team to deploy to. If not specified, Truss infers the team based on your team membership and existing models, or prompts for selection when ambiguous.
</ParamField>

<Note>
  The `--team` flag is only available if your organization has teams enabled. [Contact us](mailto:support@baseten.co) to enable teams, or see [Teams](/organization/teams) for more information.
</Note>

### Arguments

<ParamField type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To deploy a development deployment with live reload from the current directory, use the following:

```sh theme={"system"}
truss push --watch
```

To deploy a published deployment, use the following:

```sh theme={"system"}
truss push --publish
```

To deploy and promote to production, use the following:

```sh theme={"system"}
truss push --publish --promote
```

To deploy to a specific environment, use the following:

```sh theme={"system"}
truss push --environment staging
```

To deploy with a custom deployment name, use the following:

```sh theme={"system"}
truss push --publish --deployment-name my-model_v1.0
```

To deploy to a specific team, use the following:

```sh theme={"system"}
truss push --publish --team my-team-name
```


# truss run-python
Source: https://docs.baseten.co/reference/cli/truss/run-python

Run a Python script in the Truss environment.

```sh theme={"system"}
truss run-python [OPTIONS] SCRIPT [TARGET_DIRECTORY]
```

Runs a Python script in the same environment as your Truss. This builds a Docker
image matching your Truss environment, mounts the script, and executes it. Use
this to test scripts with the same dependencies your model uses.

### Arguments

<ParamField type="PATH">
  Path to the Python script to run.
</ParamField>

<ParamField type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To run a script in the Truss environment, use the following:

```sh theme={"system"}
truss run-python test_script.py
```

To run a script with a specific Truss directory, use the following:

```sh theme={"system"}
truss run-python test_script.py /path/to/my-truss
```


# truss watch
Source: https://docs.baseten.co/reference/cli/truss/watch

Live reload during development.

```sh theme={"system"}
truss watch [OPTIONS] [TARGET_DIRECTORY]
```

Watches for source code changes and applies live patches to a development deployment. This enables rapid iteration without redeploying.

### Options

<ParamField type="TEXT">
  Name of the remote in .trussrc to patch changes to.
</ParamField>

<ParamField type="TEXT">
  Name of the team to deploy to. If not specified, Truss infers the team or prompts for selection.

  <Note>
    The `--team` flag is only available if your organization has teams enabled. [Contact us](mailto:support@baseten.co) to enable teams, or see [Teams](/organization/teams) for more information.
  </Note>
</ParamField>

<ParamField>
  Automatically open remote logs tab.
</ParamField>

### Arguments

<ParamField type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To watch for changes in the current directory, use the following:

```sh theme={"system"}
truss watch
```

To watch a specific Truss directory, use the following:

```sh theme={"system"}
truss watch /path/to/my-truss
```

To watch and automatically open logs, use the following:

```sh theme={"system"}
truss watch --logs
```


# truss whoami
Source: https://docs.baseten.co/reference/cli/truss/whoami

Show user information.

```sh theme={"system"}
truss whoami [OPTIONS]
```

Shows the currently authenticated user information and exits. Use this command to verify your authentication status.

### Options

<ParamField type="TEXT">
  Name of the remote in .trussrc to check.
</ParamField>

**Example:**

To check the current authenticated user, use the following:

```sh theme={"system"}
truss whoami
```


# Chat Completions
Source: https://docs.baseten.co/reference/inference-api/chat-completions

reference/inference-api/llm-openapi-spec.json post /v1/chat/completions
Creates a chat completion for the provided conversation. This endpoint is fully compatible with the OpenAI Chat Completions API, allowing you to use standard OpenAI SDKs by changing only the base URL and API key.

<Tip>
  Download the [OpenAPI schema](/reference/inference-api/llm-openapi-spec.json) for code generation and client libraries.
</Tip>

[Model APIs](https://app.baseten.co/model-apis/create) provide instant access to high-performance open-source LLMs through an OpenAI-compatible endpoint.

## Replace OpenAI with Baseten

Switching from OpenAI to Baseten takes two changes: the base URL and API key.

<Tabs>
  <Tab title="Python">
    To switch to Baseten with the Python SDK, change `base_url` and `api_key` when initializing the client:

    ```python theme={"system"}
    from openai import OpenAI
    import os

    client = OpenAI(
        base_url="https://inference.baseten.co/v1",
        api_key=os.environ["BASETEN_API_KEY"],
    )

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3.1",
        messages=[{"role": "user", "content": "Hello!"}],
    )
    ```
  </Tab>

  <Tab title="JavaScript">
    To switch to Baseten with the JavaScript SDK, change `baseURL` and `apiKey` when initializing the client:

    ```javascript theme={"system"}
    import OpenAI from "openai";

    const client = new OpenAI({
        baseURL: "https://inference.baseten.co/v1",
        apiKey: process.env.BASETEN_API_KEY,
    });

    const response = await client.chat.completions.create({
        model: "deepseek-ai/DeepSeek-V3.1",
        messages: [{ role: "user", content: "Hello!" }],
    });
    ```
  </Tab>

  <Tab title="cURL">
    To call Baseten with cURL, send a POST request to `inference.baseten.co` with your API key:

    ```bash theme={"system"}
    curl https://inference.baseten.co/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Api-Key $BASETEN_API_KEY" \
      -d '{
        "model": "deepseek-ai/DeepSeek-V3.1",
        "messages": [{"role": "user", "content": "Hello!"}]
      }'
    ```
  </Tab>
</Tabs>

Deploy a [Model API](https://app.baseten.co/model-apis/create) to get started.

<Info>
  For detailed usage guides including structured outputs and tool calling, see [Using Model APIs](/development/model-apis/overview).
</Info>


# Overview
Source: https://docs.baseten.co/reference/inference-api/overview

The inference API is used to call deployed models and chains.

Each deployment has a dedicated subdomain on `api.baseten.co` for optimized routing.

**For models**, the endpoints follow this format:

```
https://model-{model_id}.api.baseten.co/{deployment_type_or_id}/{endpoint}
```

**For chains**, the endpoints follow this format:

```
https://chain-{chain_id}.api.baseten.co/{deployment_type_or_id}/{endpoint}
```

**Where:**

* `model_id` – The model's alphanumeric ID (found in your model dashboard).
* `chain_id` – The chain's alphanumeric ID (found in your chain dashboard).
* `deployment_type_or_id` – Either `development`, `production`, or a specific deployment’s alphanumeric ID.
* `endpoint` – The API action, such as `predict`.

For long-running tasks, the inference API supports [asynchronous inference](/inference/async) with priority queuing.

## Predict endpoints

<Tabs>
  <Tab title="Models">
    | Method      | Endpoint                                                                                                           | Description                                                                                                 |
    | :---------- | :----------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
    | `POST`      | [`/environments/{env_name}/predict`](/reference/inference-api/predict-endpoints/environments-predict)              | Call an **environment**                                                                                     |
    | `POST`      | [`/development/predict`](/reference/inference-api/predict-endpoints/development-predict)                           | Call the **development deployment**                                                                         |
    | `POST`      | [`/deployment/{deployment_id}/predict`](/reference/inference-api/predict-endpoints/deployment-predict)             | Call any **deployment**                                                                                     |
    | `POST`      | [`/environments/{env_name}/async_predict`](/reference/inference-api/predict-endpoints/environments-async-predict)  | For [Async inference](/inference/async), call the deployment associated with the specified **environment**. |
    | `POST`      | [`/development/async_predict`](/reference/inference-api/predict-endpoints/development-async-predict)               | For [Async inference](/inference/async), call the **development deployment**.                               |
    | `POST`      | [`/deployment/{deployment_id}/async_predict`](/reference/inference-api/predict-endpoints/deployment-async-predict) | For [Async inference](/inference/async), call any published **deployment** of your model.                   |
    | `WEBSOCKET` | [`/environments/{env_name}/websocket`](/reference/inference-api/predict-endpoints/environments-websocket)          | For WebSockets, connect to an **environment**.                                                              |
    | `WEBSOCKET` | [`/development/websocket`](/reference/inference-api/predict-endpoints/development-websocket)                       | For WebSockets, connect to the **development deployment**.                                                  |
    | `WEBSOCKET` | [`/deployment/{deployment_id}/websocket`](/reference/inference-api/predict-endpoints/deployment-websocket)         | For WebSockets, connect to a **deployment**.                                                                |
  </Tab>

  <Tab title="Chains">
    | Method      | Endpoint                                                                                                                 | Description                                                                                                       |
    | :---------- | :----------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
    | `POST`      | [`/environments/{env_name}/run_remote`](/reference/inference-api/predict-endpoints/environments-run-remote)              | Call a Chain **environment**                                                                                      |
    | `POST`      | [`/development/run_remote`](/reference/inference-api/predict-endpoints/development-run-remote)                           | Call a Chain **development deployment**                                                                           |
    | `POST`      | [`/deployment/{deployment_id}/run_remote`](/reference/inference-api/predict-endpoints/deployment-run-remote)             | Call a Chain **deployment**                                                                                       |
    | `POST`      | [`/environments/{env_name}/async_run_remote`](/reference/inference-api/predict-endpoints/environments-async-run-remote)  | For [Async inference](/inference/async), call the Chain deployment associated with the specified **environment**. |
    | `POST`      | [`/development/async_run_remote`](/reference/inference-api/predict-endpoints/development-async-run-remote)               | For [Async inference](/inference/async), call a Chain **development deployment**.                                 |
    | `POST`      | [`/deployment/{deployment_id}/async_run_remote`](/reference/inference-api/predict-endpoints/deployment-async-run-remote) | For [Async inference](/inference/async), call any published Chain **deployment**.                                 |
    | `WEBSOCKET` | [`/environments/{env_name}/websocket`](/reference/inference-api/predict-endpoints/environments-websocket)                | For WebSockets, connect to an **environment**.                                                                    |
    | `WEBSOCKET` | [`/development/websocket`](/reference/inference-api/predict-endpoints/development-websocket)                             | For WebSockets, connect to the **development deployment**.                                                        |
    | `WEBSOCKET` | [`/deployment/{deployment_id}/websocket`](/reference/inference-api/predict-endpoints/deployment-websocket)               | For WebSockets, connect to a **deployment**.                                                                      |
  </Tab>
</Tabs>

## Async status endpoints

| Method | Endpoint                                                                                                                        | Description                                                                               |
| :----- | :------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------- |
| `GET`  | [`/async_request/{request_id}`](/reference/inference-api/status-endpoints/get-async-request-status)                             | Get the **status** of an **async request**.                                               |
| `DEL`  | [`/async_request/{request_id}`](/reference/inference-api/predict-endpoints/cancel-async-request)                                | **Cancel** an async request.                                                              |
| `GET`  | [`/environments/{env_name}/async_queue_status`](/reference/inference-api/status-endpoints/environments-get-async-queue-status)  | Get the **async queue status** for a model associated with the **specified environment**. |
| `GET`  | [`/development/async_queue_status`](/reference/inference-api/status-endpoints/development-get-async-queue-status)               | Get the **status** of a **development deployment’s** async queue.                         |
| `GET`  | [`/deployment/{deployment_id}/async_queue_status`](/reference/inference-api/status-endpoints/deployment-get-async-queue-status) | Get the **status** of a **deployment’s** async queue.                                     |

## Wake endpoints

| Method | Endpoint                                                                            | Description                                        |
| :----- | :---------------------------------------------------------------------------------- | :------------------------------------------------- |
| `POST` | [`/production/wake`](/reference/inference-api/wake/production-wake)                 | Wake the **production environment** of your model. |
| `POST` | [`/development/wake`](/reference/inference-api/wake/development-wake)               | Wake the **development deployment** of your model. |
| `POST` | [`/deployment/{deployment_id}/wake`](/reference/inference-api/wake/deployment-wake) | Wake any **deployment** of your model.             |


# Async cancel request
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/cancel-async-request

DELETE https://model-{model_id}.api.baseten.co/async_request/{request_id}
Use this endpoint to cancel a queued async request.

Only `QUEUED` requests may be canceled.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField type="string">
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField type="string">
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

<ParamField type="string">
  The ID of the async request.
</ParamField>

### Headers

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<ResponseField name="request_id" type="string">
  The ID of the async request.
</ResponseField>

<ResponseField name="canceled" type="boolean">
  Whether the request was canceled.
</ResponseField>

<ResponseField name="message" type="string">
  Additional details about whether the request was canceled.
</ResponseField>

### Rate limits

Calls to the cancel async request status endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

<RequestExample>
  ```python Python (Model) theme={"system"}
  import requests
  import os

  model_id = ""
  request_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.delete(
  f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
  headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```python Python (Chain) theme={"system"}
  import requests
  import os

  chain_id = ""
  request_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.delete(
  f"https://chain-{chain_id}.api.baseten.co/async_request/{request_id}",
  headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>


# Async deployment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-async-predict

POST https://model-{model_id}.api.baseten.co/deployment/{deployment-id}/async_predict
Use this endpoint to call any [published deployment](/deploy/lifecycle) of your model.

### Parameters

<ParamField type="string">
  The ID of the model you want to call.
</ParamField>

<ParamField type="string">
  The ID of the specific deployment you want to call.
</ParamField>

### Headers

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

There is a 256 KiB size limit to `/async_predict` request payloads.

<ParamField type="json">
  JSON-serializable model input.
</ParamField>

<ParamField type="string">
  <Note> Baseten **does not** store model outputs. If `webhook_endpoint` is empty, your model must save prediction outputs so they can be accessed later. </Note>

  URL of the webhook endpoint. We require that webhook endpoints use HTTPS. Both HTTP/2 and HTTP/1.1 protocols are supported.
</ParamField>

<ParamField type="integer">
  Priority of the request. A lower value corresponds to a higher priority (e.g. requests with priority 0 are scheduled before requests of priority 1).

  `priority` is between 0 and 2, inclusive.
</ParamField>

<ParamField type="integer">
  Maximum time a request will spend in the queue before expiring.

  `max_time_in_queue_seconds` must be between 10 seconds and 72 hours, inclusive.
</ParamField>

<ParamField type="json">
  Exponential backoff parameters used to retry the model predict request.

  <Expandable>
    <ParamField type="integer">
      Number of predict request attempts.

      `max_attempts` must be between 1 and 10, inclusive.
    </ParamField>

    <ParamField type="integer">
      Minimum time between retries in milliseconds.

      `initial_delay_ms` must be between 0 and 10,000 milliseconds, inclusive.
    </ParamField>

    <ParamField type="integer">
      Maximum time between retries in milliseconds.

      `max_delay_ms` must be between 0 and 60,000 milliseconds, inclusive.
    </ParamField>
  </Expandable>
</ParamField>

### Response

<ResponseField name="request_id" type="string">
  The ID of the async request.
</ResponseField>

### Rate limits

Two types of rate limits apply when making async requests:

* Calls to the `/async_predict` endpoint are limited to **200 requests per second**.

* Each organization is limited to **50,000 `QUEUED` or `IN_PROGRESS` async requests**, summed across all deployments.

If either limit is exceeded, subsequent `/async_predict` requests will receive a 429 status code.

To avoid hitting these rate limits, we advise:

* Implementing a backpressure mechanism, such as calling `/async_predict` with exponential backoff in response to 429 errors.
* Monitoring the [async queue size metric](/observability/metrics#async-queue-metrics). If your model is accumulating a backlog of requests, consider increasing the number of requests your model can process at once by increasing the number of max replicas or the concurrency target in your autoscaling settings.

<RequestExample>
  ```python Python theme={"system"}
  import requests
  import os

  model_id = ""
  deployment_id = ""
  webhook_endpoint = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.post(
  f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={
  "model_input": {"prompt": "hello world!"},
  "webhook_endpoint": webhook_endpoint # Optional fields for priority, max_time_in_queue_seconds, etc
  },
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl --request POST \
    --url https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict \
    --header "Authorization: Api-Key $BASETEN_API_KEY" \
    --data '{
    "model_input": {"prompt": "hello world!"},
    "webhook_endpoint": "https://my_webhook.com/webhook",
    "priority": 1,
    "max_time_in_queue_seconds": 100,
    "inference_retry_config": {
      "max_attempts": 3,
      "initial_delay_ms": 1000,
      "max_delay_ms": 5000
    }
  }'
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({
        model_input: { prompt: "hello world!" },
        webhook_endpoint: "https://my_webhook.com/webhook",
        priority: 1,
        max_time_in_queue_seconds: 100,
        inference_retry_config: {
          max_attempts: 3,
          initial_delay_ms: 1000,
          max_delay_ms: 5000,
        },
      }),
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>


# Async chains deployment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-async-run-remote

POST https://chain-{chain_id}.api.baseten.co/deployment/{deployment-id}/async_run_remote

Use this endpoint to call any [deployment](/deployment/deployments) of your
chain asynchronously.

```sh theme={"system"}
https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/async_run_remote
```

### Parameters

<ParamField type="string">
  The ID of the chain you want to call.
</ParamField>

<ParamField type="string">
  The ID of the specific deployment you want to call.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField type="json">
  JSON-serializable chain input. The input schema corresponds to the signature
  of the entrypoint's `run_remote` method. I.e. The top-level keys are the
  argument names. The values are the corresponding JSON representation of the
  types.
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  chain_id = ""
  deployment_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://chain
  -{chain_id}.api.baseten.co/deployment/{deployment_id}/async_run_remote",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable chain input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/async_run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/async_run_remote",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>


# Deployment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-predict

POST https://model-{model_id}.api.baseten.co/deployment/{deployment-id}/predict

Use this endpoint to call any [published deployment](/deployment/deployments) of your model.

```sh theme={"system"}
https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/predict
```

### Parameters

<ParamField type="string">
  The ID of the model you want to call.
</ParamField>

<ParamField type="string">
  The ID of the specific deployment you want to call.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField type="json">
  JSON-serializable model input.
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  model_id = ""
  deployment_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable model input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/predict \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable model input
  ```

  ```sh Truss theme={"system"}
  truss predict --model-version DEPLOYMENT_ID -d '{}' # JSON-serializable model input
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable model input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // JSON-serializable output varies by model theme={"system"}
  {}
  ```
</ResponseExample>


# Chains deployment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-run-remote

POST https://chain-{chain_id}.api.baseten.co/deployment/{deployment-id}/run_remote

Use this endpoint to call any [deployment](/deployment/deployments) of your
chain.

```sh theme={"system"}
https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/run_remote
```

### Parameters

<ParamField type="string">
  The ID of the chain you want to call.
</ParamField>

<ParamField type="string">
  The ID of the specific deployment you want to call.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField type="json">
  JSON-serializable chain input. The input schema corresponds to the signature
  of the entrypoint's `run_remote` method. I.e. The top-level keys are the
  argument names. The values are the corresponding JSON representation of the
  types.
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  chain_id = ""
  deployment_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://chain
  -{chain_id}.api.baseten.co/deployment/{deployment_id}/run_remote",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable chain input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/run_remote",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // JSON-serializable output varies by chain theme={"system"}
  {}
  ```
</ResponseExample>


# Websocket deployment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-websocket

WEBSOCKET wss://{entity}-{entity_id}.api.baseten.co/deployment/{deployment_id}/websocket

Use this endpoint to connect via WebSockets to a specific deployment.

Note that `entity` here could be either `model` or `chain`, depending on whether you using Baseten models or Chains.

```sh theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/deployment/{deployment_id}/websocket"
```

See [WebSockets](/development/model/websockets) for more details.

### Parameters

<ParamField type="string">
  The type of entity you want to connect to. Either `model` or `chain`.
</ParamField>

<ParamField type="string">
  The ID of the model or chain you want to connect to.
</ParamField>

<ParamField type="string">
  The ID of the deployment you want to connect to.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Api-Key YOUR_API_KEY' \
      wss://{entity}-{model_id}.api.baseten.co/deployment/{deployment_id}/websocket
  ```
</RequestExample>


# Async development
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-async-predict

POST https://model-{model_id}.api.baseten.co/development/async_predict
Use this endpoint to call the [development deployment](/deploy/lifecycle) of your model asynchronously.

### Parameters

<ParamField type="string">
  The ID of the model you want to call.
</ParamField>

### Headers

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

There is a 256 KiB size limit to `/async_predict` request payloads.

<ParamField type="json">
  JSON-serializable model input.
</ParamField>

<ParamField type="string">
  <Note> Baseten **does not** store model outputs. If `webhook_endpoint` is empty, your model must save prediction outputs so they can be accessed later. </Note>

  URL of the webhook endpoint. We require that webhook endpoints use HTTPS. Both HTTP/2 and HTTP/1.1 protocols are supported.
</ParamField>

<ParamField type="integer">
  Priority of the request. A lower value corresponds to a higher priority (e.g. requests with priority 0 are scheduled before requests of priority 1).

  `priority` is between 0 and 2, inclusive.
</ParamField>

<ParamField type="integer">
  Maximum time a request will spend in the queue before expiring.

  `max_time_in_queue_seconds` must be between 10 seconds and 72 hours, inclusive.
</ParamField>

<ParamField type="json">
  Exponential backoff parameters used to retry the model predict request.

  <Expandable>
    <ParamField type="integer">
      Number of predict request attempts.

      `max_attempts` must be between 1 and 10, inclusive.
    </ParamField>

    <ParamField type="integer">
      Minimum time between retries in milliseconds.

      `initial_delay_ms` must be between 0 and 10,000 milliseconds, inclusive.
    </ParamField>

    <ParamField type="integer">
      Maximum time between retries in milliseconds.

      `max_delay_ms` must be between 0 and 60,000 milliseconds, inclusive.
    </ParamField>
  </Expandable>
</ParamField>

### Response

<ResponseField name="request_id" type="string">
  The ID of the async request.
</ResponseField>

### Rate limits

Two types of rate limits apply when making async requests:

* Calls to the `/async_predict` endpoint are limited to **200 requests per second**.

* Each organization is limited to **50,000 `QUEUED` or `IN_PROGRESS` async requests**, summed across all deployments.

If either limit is exceeded, subsequent `/async_predict` requests will receive a 429 status code.

To avoid hitting these rate limits, we advise:

* Implementing a backpressure mechanism, such as calling `/async_predict` with exponential backoff in response to 429 errors.
* Monitoring the [async queue size metric](/observability/metrics#async-queue-metrics). If your model is accumulating a backlog of requests, consider increasing the number of requests your model can process at once by increasing the number of max replicas or the concurrency target in your autoscaling settings.

<RequestExample>
  ```python Python theme={"system"}
  import requests
  import os

  model_id = ""
  webhook_endpoint = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.post(
  f"https://model-{model_id}.api.baseten.co/development/async_predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={
  "model_input": {"prompt": "hello world!"},
  "webhook_endpoint": webhook_endpoint # Optional fields for priority, max_time_in_queue_seconds, etc
  },
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl --request POST \
    --url https://model-{model_id}.api.baseten.co/development/async_predict \
    --header "Authorization: Api-Key $BASETEN_API_KEY" \
    --data '{
    "model_input": {"prompt": "hello world!"},
    "webhook_endpoint": "https://my_webhook.com/webhook",
    "priority": 1,
    "max_time_in_queue_seconds": 100,
    "inference_retry_config": {
      "max_attempts": 3,
      "initial_delay_ms": 1000,
      "max_delay_ms": 5000
    }
  }'
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/development/async_predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({
        model_input: { prompt: "hello world!" },
        webhook_endpoint: "https://my_webhook.com/webhook",
        priority: 1,
        max_time_in_queue_seconds: 100,
        inference_retry_config: {
          max_attempts: 3,
          initial_delay_ms: 1000,
          max_delay_ms: 5000,
        },
      }),
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>


# Async chains development
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-async-run-remote

POST https://chain-{chain_id}.api.baseten.co/development/async_run_remote

Use this endpoint to call the [development deployment](/development/chain/deploy#development) of
your chain asynchronously.

```sh theme={"system"}
https://chain-{chain_id}.api.baseten.co/development/async_run_remote
```

### Parameters

<ParamField type="string">
  The ID of the chain you want to call.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField type="json">
  JSON-serializable chain input. The input schema corresponds to the
  signature of the entrypoint's `run_remote` method. I.e. The top-level keys
  are the argument names. The values are the corresponding JSON representation of
  the types.
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  chain_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://chain-{chain_id}.api.baseten.co/development/async_run_remote",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable chain input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/development/async_run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require('node-fetch');

  const resp = await fetch(
    'https://chain-{chain_id}.api.baseten.co/development/async_run_remote',
    {
      method: 'POST',
      headers: { Authorization: 'Api-Key YOUR_API_KEY' },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>


# Development
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-predict

POST https://model-{model_id}.api.baseten.co/development/predict

Use this endpoint to call the [development deployment](/deployment/deployments) of your model.

```sh theme={"system"}
https://model-{model_id}.api.baseten.co/development/predict
```

### Parameters

<ParamField type="string">
  The ID of the model you want to call.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField type="json">
  JSON-serializable model input.
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  model_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/development/predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable model input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/development/predict \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable model input
  ```

  ```sh Truss theme={"system"}
  truss predict --model-version DEPLOYMENT_ID -d '{}' # JSON-serializable model input
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/development/predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable model input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // JSON-serializable output varies by model theme={"system"}
  {}
  ```
</ResponseExample>


# Chains development
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-run-remote

POST https://chain-{chain_id}.api.baseten.co/development/run_remote

Use this endpoint to call the [development deployment](/development/chain/deploy#development) of
your chain.

```sh theme={"system"}
https://chain-{chain_id}.api.baseten.co/development/run_remote
```

### Parameters

<ParamField type="string">
  The ID of the chain you want to call.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField type="json">
  JSON-serializable chain input. The input schema corresponds to the
  signature of the entrypoint's `run_remote` method. I.e. The top-level keys
  are the argument names. The values are the corresponding JSON representation of
  the types.
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  chain_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://chain-{chain_id}.api.baseten.co/development/run_remote",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable chain input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/development/run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require('node-fetch');

  const resp = await fetch(
    'https://chain-{chain_id}.api.baseten.co/development/run_remote',
    {
      method: 'POST',
      headers: { Authorization: 'Api-Key YOUR_API_KEY' },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response theme={"system"}
  // JSON-serializable output varies by chain
  {}
  ```
</ResponseExample>


# Websocket development
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-websocket

WEBSOCKET wss://{entity}-{entity_id}.api.baseten.co/development/websocket

Use this endpoint to connect via WebSockets to the development deployment of a model or chain.

```sh theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/development/websocket"
```

See [WebSockets](/development/model/websockets) for more details.

### Parameters

<ParamField type="string">
  The type of entity you want to connect to. Either `model` or `chain`.
</ParamField>

<ParamField type="string">
  The ID of the model or chain you want to connect to.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Api-Key YOUR_API_KEY' \
      wss://{entity}-{entity_id}.api.baseten.co/development/websocket
  ```
</RequestExample>


# Async environment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-async-predict

POST https://model-{model_id}.api.baseten.co/environments/{env_name}/async_predict
Use this endpoint to call the model associated with the specified environment asynchronously.

### Parameters

<ParamField type="string">
  The ID of the model you want to call.
</ParamField>

<ParamField type="string">
  The name of the model's environment you want to call.
</ParamField>

### Headers

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

There is a 256 KiB size limit to `/async_predict` request payloads.

<ParamField type="json">
  JSON-serializable model input.
</ParamField>

<ParamField type="string">
  <Note> Baseten **does not** store model outputs. If `webhook_endpoint` is empty, your model must save prediction outputs so they can be accessed later. </Note>

  URL of the webhook endpoint. We require that webhook endpoints use HTTPS. Both HTTP/2 and HTTP/1.1 protocols are supported.
</ParamField>

<ParamField type="integer">
  Priority of the request. A lower value corresponds to a higher priority (e.g. requests with priority 0 are scheduled before requests of priority 1).

  `priority` is between 0 and 2, inclusive.
</ParamField>

<ParamField type="integer">
  Maximum time a request will spend in the queue before expiring.

  `max_time_in_queue_seconds` must be between 10 seconds and 72 hours, inclusive.
</ParamField>

<ParamField type="json">
  Exponential backoff parameters used to retry the model predict request.

  <Expandable>
    <ParamField type="integer">
      Number of predict request attempts.

      `max_attempts` must be between 1 and 10, inclusive.
    </ParamField>

    <ParamField type="integer">
      Minimum time between retries in milliseconds.

      `initial_delay_ms` must be between 0 and 10,000 milliseconds, inclusive.
    </ParamField>

    <ParamField type="integer">
      Maximum time between retries in milliseconds.

      `max_delay_ms` must be between 0 and 60,000 milliseconds, inclusive.
    </ParamField>
  </Expandable>
</ParamField>

### Response

<ResponseField name="request_id" type="string">
  The ID of the async request.
</ResponseField>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>

### Rate limits

Two types of rate limits apply when making async requests:

* Calls to the `/async_predict` endpoint are limited to **200 requests per second**.

* Each organization is limited to **50,000 `QUEUED` or `IN_PROGRESS` async requests**, summed across all deployments.

If either limit is exceeded, subsequent `/async_predict` requests will receive a 429 status code.

To avoid hitting these rate limits, we advise:

* Implementing a backpressure mechanism, such as calling `/async_predict` with exponential backoff in response to 429 errors.
* Monitoring the [async queue size metric](/observability/metrics#async-queue-metrics). If your model is accumulating a backlog of requests, consider increasing the number of requests your model can process at once by increasing the number of max replicas or the concurrency target in your autoscaling settings.


# Async chains environment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-async-run-remote

POST https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_run_remote
Use this endpoint to call the deployment associated with the specified environment asynchronously.

```sh theme={"system"}
https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_run_remote"
```

### Parameters

<ParamField type="string">
  The ID of the chain you want to call.
</ParamField>

<ParamField type="string">
  The name of the chain's environment you want to call.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField type="json">
  JSON-serializable chain input. The input schema corresponds to the
  signature of the entrypoint's `run_remote` method. I.e. The top-level keys
  are the argument names. The values are the corresponding JSON representation of
  the types.
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  chain_id = ""
  env_name = "staging"
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
      "POST",
      f"https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_run_remote",
      headers={"Authorization": f"Api-Key {baseten_api_key}"},
      json={}, # JSON-serializable chain input
  )

  print(resp.json())
  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require('node-fetch');

  const resp = await fetch(
    'https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_run_remote',
    {
      method: 'POST',
      headers: { Authorization: 'Api-Key YOUR_API_KEY' },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>


# Environment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-predict

POST https://model-{model_id}.api.baseten.co/environments/{env_name}/predict

Use this endpoint to call the deployment associated with the specified [environment](/deployment/environments).

```sh theme={"system"}
https://model-{model_id}.api.baseten.co/environments/{env_name}/predict
```

### Parameters

<ParamField type="string">
  The ID of the model you want to call.
</ParamField>

<ParamField type="string">
  The name of the model's environment you want to call.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField type="json">
  JSON-serializable model input.
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  model_id = ""
  env_name = "staging"

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/environments/{env_name}/predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable model input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/environments/{env_name}/predict \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable model input
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/environments/{env_name}/predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable model input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // JSON-serializable output varies by model theme={"system"}
  {}
  ```
</ResponseExample>


# Chains environment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-run-remote

POST https://chain-{chain_id}.api.baseten.co/environments/{env_name}/run_remote
Use this endpoint to call the deployment associated with the specified environment.

```sh theme={"system"}
https://chain-{chain}.api.baseten.co/environments/{env_name}/run_remote"
```

### Parameters

<ParamField type="string">
  The ID of the chain you want to call.
</ParamField>

<ParamField type="string">
  The name of the chain's environment you want to call.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField type="json">
  JSON-serializable chain input. The input schema corresponds to the
  signature of the entrypoint's `run_remote` method. I.e. The top-level keys
  are the argument names. The values are the corresponding JSON representation of
  the types.
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  chain_id = ""
  env_name = "staging"
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
      "POST",
      f"https://chain-{chain_id}.api.baseten.co/environments/{env_name}/run_remote",
      headers={"Authorization": f"Api-Key {baseten_api_key}"},
      json={}, # JSON-serializable chain input
  )

  print(resp.json())
  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/environments/{env_name}/run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require('node-fetch');

  const resp = await fetch(
    'https://chain-{chain_id}.api.baseten.co/environments/{env_name}/run_remote',
    {
      method: 'POST',
      headers: { Authorization: 'Api-Key YOUR_API_KEY' },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response theme={"system"}
  // JSON-serializable output varies by chain
  {}
  ```
</ResponseExample>


# Websocket environment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-websocket

WEBSOCKET wss://{entity}-{entity_id}.api.baseten.co/environments/{env_name}/websocket

Use this endpoint to connect via WebSockets to the deployment associated with the specified [environment](/deployment/environments).

Note that `entity` here could be either `model` or `chain`, depending on whether you using Baseten models or Chains.

```sh theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/environments/{env_name}/websocket"
```

See [WebSockets](/development/model/websockets) for more details.

### Parameters

<ParamField type="string">
  The type of entity you want to connect to. Either `model` or `chain`.
</ParamField>

<ParamField type="string">
  The ID of the model or chain you want to connect to.
</ParamField>

<ParamField type="string">
  The name of the environment you want to connect to.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Api-Key YOUR_API_KEY' \
      wss://{entity}-{model_id}.api.baseten.co/environments/{env_name}/websocket
  ```
</RequestExample>


# Async deployment
Source: https://docs.baseten.co/reference/inference-api/status-endpoints/deployment-get-async-queue-status

GET https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_queue_status
Use this endpoint to get the status of a published deployment's async queue.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField type="string">
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField type="string">
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

<ParamField type="string">
  The ID of the deployment.
</ParamField>

### Headers

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<ResponseField name="model_id" type="string">
  The ID of the model.
</ResponseField>

<ResponseField name="deployment_id" type="string">
  The ID of the deployment.
</ResponseField>

<ResponseField name="num_queued_requests" type="integer">
  The number of requests in the deployment's async queue with `QUEUED` status (i.e. awaiting processing by the model).
</ResponseField>

<ResponseField name="num_in_progress_requests" type="integer">
  The number of requests in the deployment's async queue with `IN_PROGRESS` status (i.e. currently being processed by the model).
</ResponseField>

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "model_id": "<string>",
    "deployment_id": "<string>",
    "num_queued_requests": 12,
    "num_in_progress_requests": 3
  }
  ```
</ResponseExample>

### Rate limits

Calls to the `/async_queue_status` endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

To gracefully handle hitting this rate limit, we advise implementing a backpressure mechanism, such as calling `/async_queue_status` with exponential backoff in response to 429 errors.

<RequestExample>
  ```py Model theme={"system"}
  import requests
  import os

  model_id = ""
  deployment_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```py Chain theme={"system"}
  import requests
  import os

  chain_id = ""
  deployment_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>


# Async development
Source: https://docs.baseten.co/reference/inference-api/status-endpoints/development-get-async-queue-status

GET https://model-{model_id}.api.baseten.co/development/async_queue_status
Use this endpoint to get the status of a development deployment's async queue.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField type="string">
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField type="string">
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

### Headers

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<ResponseField name="model_id" type="string">
  The ID of the model.
</ResponseField>

<ResponseField name="deployment_id" type="string">
  The ID of the deployment.
</ResponseField>

<ResponseField name="num_queued_requests" type="integer">
  The number of requests in the deployment's async queue with `QUEUED` status (i.e. awaiting processing by the model).
</ResponseField>

<ResponseField name="num_in_progress_requests" type="integer">
  The number of requests in the deployment's async queue with `IN_PROGRESS` status (i.e. currently being processed by the model).
</ResponseField>

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "model_id": "<string>",
    "deployment_id": "<string>",
    "num_queued_requests": 12,
    "num_in_progress_requests": 3
  }
  ```
</ResponseExample>

### Rate limits

Calls to the `/async_queue_status` endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

To gracefully handle hitting this rate limit, we advise implementing a backpressure mechanism, such as calling `/async_queue_status` with exponential backoff in response to 429 errors.

<RequestExample>
  ```py Model theme={"system"}
  import requests
  import os

  model_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://model-{model_id}.api.baseten.co/development/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```py Chain theme={"system"}
  import requests
  import os

  chain_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://chain-{chain_id}.api.baseten.co/development/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>


# Async environment
Source: https://docs.baseten.co/reference/inference-api/status-endpoints/environments-get-async-queue-status

GET https://model-{model_id}.api.baseten.co/environments/{env_name}/async_queue_status
Use this endpoint to get the async queue status for a model associated with the specified environment.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField type="string">
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField type="string">
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

<ParamField type="string">
  The name of the environment.
</ParamField>

### Headers

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<ResponseField name="model_id" type="string">
  The ID of the model.
</ResponseField>

<ResponseField name="deployment_id" type="string">
  The ID of the deployment.
</ResponseField>

<ResponseField name="num_queued_requests" type="integer">
  The number of requests in the deployment's async queue with `QUEUED` status (i.e. awaiting processing by the model).
</ResponseField>

<ResponseField name="num_in_progress_requests" type="integer">
  The number of requests in the deployment's async queue with `IN_PROGRESS` status (i.e. currently being processed by the model).
</ResponseField>

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "model_id": "<string>",
    "deployment_id": "<string>",
    "num_queued_requests": 12,
    "num_in_progress_requests": 3
  }
  ```
</ResponseExample>

### Rate limits

Calls to the `/async_queue_status` endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

To gracefully handle hitting this rate limit, we advise implementing a backpressure mechanism, such as calling `/async_queue_status` with exponential backoff in response to 429 errors.

<RequestExample>
  ```py Model theme={"system"}
  import requests
  import os

  model_id = ""
  env_name = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://model-{model_id}.api.baseten.co/environments/{env_name}/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```py Chain theme={"system"}
  import requests
  import os

  chain_id = ""
  env_name = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>


# Async request
Source: https://docs.baseten.co/reference/inference-api/status-endpoints/get-async-request-status

GET https://model-{model_id}.api.baseten.co/async_request/{request_id}
Use this endpoint to get the status of an async request.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField type="string">
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField type="string">
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

<ParamField type="string">
  The ID of the async request.
</ParamField>

### Headers

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<Tabs>
  <Tab title="Model">
    <ResponseField name="request_id" type="string">
      The ID of the async request.
    </ResponseField>

    <ResponseField name="model_id" type="string">
      The ID of the model that executed the request.
    </ResponseField>

    <ResponseField name="deployment_id" type="string">
      The ID of the deployment that executed the request.
    </ResponseField>

    <ResponseField name="status" type="string">
      An enum representing the status of the request.

      Available options: `QUEUED`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `EXPIRED`, `CANCELED`, `WEBHOOK_FAILED`
    </ResponseField>

    <ResponseField name="webhook_status" type="string">
      An enum representing the status of sending the predict result to the provided webhook.

      Available options: `PENDING`, `SUCCEEDED`, `FAILED`, `CANCELED`, `NO_WEBHOOK_PROVIDED`
    </ResponseField>

    <ResponseField name="created_at" type="string">
      The time in UTC at which the async request was created.
    </ResponseField>

    <ResponseField name="status_at" type="string">
      The time in UTC at which the async request's status was updated.
    </ResponseField>

    <ResponseField name="errors" type="object[]">
      Any errors that occurred in processing the async request. Empty if no errors occurred.

      <Expandable>
        <ResponseField name="code" type="string">
          An enum representing the type of error that occurred.

          Available options: `MODEL_PREDICT_ERROR`, `MODEL_PREDICT_TIMEOUT`, `MODEL_NOT_READY`, `MODEL_DOES_NOT_EXIST`, `MODEL_UNAVAILABLE`, `MODEL_INVALID_INPUT`, `ASYNC_REQUEST_NOT_SUPPORTED`, `INTERNAL_SERVER_ERROR`
        </ResponseField>

        <ResponseField name="message" type="string">
          A message containing details of the error that occurred.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>

  <Tab title="Chain">
    <ResponseField name="request_id" type="string">
      The ID of the async request.
    </ResponseField>

    <ResponseField name="chain_id" type="string">
      The ID of the chain that executed the request.
    </ResponseField>

    <ResponseField name="deployment_id" type="string">
      The ID of the deployment that executed the request.
    </ResponseField>

    <ResponseField name="status" type="string">
      An enum representing the status of the request.

      Available options: `QUEUED`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `EXPIRED`, `CANCELED`, `WEBHOOK_FAILED`
    </ResponseField>

    <ResponseField name="webhook_status" type="string">
      An enum representing the status of sending the predict result to the provided webhook.

      Available options: `PENDING`, `SUCCEEDED`, `FAILED`, `CANCELED`, `NO_WEBHOOK_PROVIDED`
    </ResponseField>

    <ResponseField name="created_at" type="string">
      The time in UTC at which the async request was created.
    </ResponseField>

    <ResponseField name="status_at" type="string">
      The time in UTC at which the async request's status was updated.
    </ResponseField>

    <ResponseField name="errors" type="object[]">
      Any errors that occurred in processing the async request. Empty if no errors occurred.

      <Expandable>
        <ResponseField name="code" type="string">
          An enum representing the type of error that occurred.

          Available options: `MODEL_PREDICT_ERROR`, `MODEL_PREDICT_TIMEOUT`, `MODEL_NOT_READY`, `MODEL_DOES_NOT_EXIST`, `MODEL_UNAVAILABLE`, `MODEL_INVALID_INPUT`, `ASYNC_REQUEST_NOT_SUPPORTED`, `INTERNAL_SERVER_ERROR`
        </ResponseField>

        <ResponseField name="message" type="string">
          A message containing details of the error that occurred.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>
</Tabs>

<ResponseExample>
  ```json 200 (Model) theme={"system"}
  {
    "request_id": "<string>",
    "model_id": "<string>",
    "deployment_id": "<string>",
    "status": "<string>",
    "webhook_status": "<string>",
    "created_at": "<string>",
    "status_at": "<string>",
    "errors": [
      {
        "code": "<string>",
        "message": "<string>"
      }
    ]
  }
  ```

  ```json 200 (Chain) theme={"system"}
  {
    "request_id": "<string>",
    "chain_id": "<string>",
    "deployment_id": "<string>",
    "status": "<string>",
    "webhook_status": "<string>",
    "created_at": "<string>",
    "status_at": "<string>",
    "errors": [
      {
        "code": "<string>",
        "message": "<string>"
      }
    ]
  }
  ```
</ResponseExample>

### Rate limits

Calls to the get async request status endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

To avoid hitting this rate limit, we recommend [configuring a webhook endpoint](/inference/async#configuring-the-webhook-endpoint) to receive async predict results instead of frequently polling this endpoint for async request statuses.

<RequestExample>
  ```python Python (Model) theme={"system"}
  import requests
  import os

  model_id = ""
  request_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```python Python (Chain) theme={"system"}
  import requests
  import os

  chain_id = ""
  request_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://chain-{chain_id}.api.baseten.co/async_request/{request_id}",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>


# Deployment
Source: https://docs.baseten.co/reference/inference-api/wake/deployment-wake

POST https://model-{model_id}.api.baseten.co/deployment/{deployment-id}/wake

Use this endpoint to wake any scaled-to-zero [deployment](/deployment/deployments) of your model.

```sh theme={"system"}
https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/wake
```

### Parameters

<ParamField type="string">
  The ID of the model you want to wake.
</ParamField>

<ParamField type="string">
  The ID of the specific deployment you want to wake.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  model_id = ""
  deployment_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/wake",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/wake \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/wake",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // Returns a 202 response code theme={"system"}
  {}
  ```
</ResponseExample>


# Development
Source: https://docs.baseten.co/reference/inference-api/wake/development-wake

POST https://model-{model_id}.api.baseten.co/development/wake

Use this endpoint to wake the [development deployment](/deployment/deployments#development-deployment) of your model if it is scaled to zero.

```sh theme={"system"}
https://model-{model_id}.api.baseten.co/development/wake
```

### Parameters

<ParamField type="string">
  The ID of the model you want to wake.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  model_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/development/wake",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/development/wake \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/development/wake",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // Returns a 202 response code theme={"system"}
  {}
  ```
</ResponseExample>


# Production
Source: https://docs.baseten.co/reference/inference-api/wake/production-wake

POST https://model-{model_id}.api.baseten.co/production/wake

Use this endpoint to wake the [production environment](/deployment/deployments#environments-and-promotion) of your model if it is scaled to zero.

```sh theme={"system"}
https://model-{model_id}.api.baseten.co/production/wake
```

### Parameters

<ParamField type="string">
  The ID of the model you want to wake.
</ParamField>

<ParamField type="string">
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```python Python theme={"system"}
  import urllib3
  import os

  model_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/production/wake",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/production/wake \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
  ```

  ```javascript Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/production/wake",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // Returns a 202 response code theme={"system"}
  {}
  ```
</ResponseExample>


# Create an API key
Source: https://docs.baseten.co/reference/management-api/api-keys/creates-an-api-key

post /v1/api_keys
Creates an API key with the provided name and type. The API key is returned in the response.



# Delete an API key
Source: https://docs.baseten.co/reference/management-api/api-keys/delete-an-api-key

delete /v1/api_keys/{api_key_prefix}
Deletes an API key by prefix and returns info about the API key.



# Get all API keys
Source: https://docs.baseten.co/reference/management-api/api-keys/lists-the-users-api-keys

get /v1/api_keys
Lists all API keys your account has access to.

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "name": "my-api-key", 
    "type": "PERSONAL"
  }
  ```
</ResponseExample>


# Delete chains
Source: https://docs.baseten.co/reference/management-api/chains/deletes-a-chain-by-id

delete /v1/chains/{chain_id}



# By ID
Source: https://docs.baseten.co/reference/management-api/chains/gets-a-chain-by-id

get /v1/chains/{chain_id}



# All chains
Source: https://docs.baseten.co/reference/management-api/chains/gets-all-chains

get /v1/chains



# Any deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/activate/activates-a-deployment

post /v1/models/{model_id}/deployments/{deployment_id}/activate
Activates an inactive deployment and returns the activation status.



# Activate environment deployment
Source: https://docs.baseten.co/reference/management-api/deployments/activate/activates-a-deployment-associated-with-an-environment

post /v1/models/{model_id}/environments/{env_name}/activate
Activates an inactive deployment associated with an environment and returns the activation status.



# Development deployment
Source: https://docs.baseten.co/reference/management-api/deployments/activate/activates-a-development-deployment

post /v1/models/{model_id}/deployments/development/activate
Activates an inactive development deployment and returns the activation status.



# Update chainlet environment's autoscaling settings
Source: https://docs.baseten.co/reference/management-api/deployments/autoscaling/update-a-chainlet-environments-autoscaling-settings

patch /v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/autoscaling_settings
Updates a chainlet environment's autoscaling settings and returns the updated chainlet environment settings.



# Any model deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/autoscaling/updates-a-deployments-autoscaling-settings

patch /v1/models/{model_id}/deployments/{deployment_id}/autoscaling_settings
Updates a deployment's autoscaling settings and returns the update status.

<Note>
  To update autoscaling settings at the environment level, use the [update environment settings](/reference/management-api/environments/update-an-environments-settings) endpoint.
</Note>


# Development model deployment
Source: https://docs.baseten.co/reference/management-api/deployments/autoscaling/updates-a-development-deployments-autoscaling-settings

patch /v1/models/{model_id}/deployments/development/autoscaling_settings
Updates a development deployment's autoscaling settings and returns the update status.

<Note>
  To update autoscaling settings at the environment level, use the [update environment settings](/reference/management-api/environments/update-an-environments-settings) endpoint.
</Note>


# Any deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/deactivate/deactivates-a-deployment

post /v1/models/{model_id}/deployments/{deployment_id}/deactivate
Deactivates a deployment and returns the deactivation status.



# Deactivate environment deployment
Source: https://docs.baseten.co/reference/management-api/deployments/deactivate/deactivates-a-deployment-associated-with-an-environment

post /v1/models/{model_id}/environments/{env_name}/deactivate
Deactivates a deployment associated with an environment and returns the deactivation status.



# Development deployment
Source: https://docs.baseten.co/reference/management-api/deployments/deactivate/deactivates-a-development-deployment

post /v1/models/{model_id}/deployments/development/deactivate
Deactivates a development deployment and returns the deactivation status.



# Delete chain deployment
Source: https://docs.baseten.co/reference/management-api/deployments/deletes-a-chain-deployment-by-id

delete /v1/chains/{chain_id}/deployments/{chain_deployment_id}



# Delete model deployments
Source: https://docs.baseten.co/reference/management-api/deployments/deletes-a-models-deployment-by-id

delete /v1/models/{model_id}/deployments/{deployment_id}
Deletes a model's deployment by ID and returns the tombstone of the deployment.



# Any chain deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/gets-a-chain-deployment-by-id

get /v1/chains/{chain_id}/deployments/{chain_deployment_id}



# Any model deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/gets-a-models-deployment-by-id

get /v1/models/{model_id}/deployments/{deployment_id}
Gets a model's deployment by ID and returns the deployment.



# Development model deployment
Source: https://docs.baseten.co/reference/management-api/deployments/gets-a-models-development-deployment

get /v1/models/{model_id}/deployments/development
Gets a model's development deployment and returns the deployment.



# Production model deployment
Source: https://docs.baseten.co/reference/management-api/deployments/gets-a-models-production-deployment

get /v1/models/{model_id}/deployments/production
Gets a model's production deployment and returns the deployment.



# Get all chain deployments
Source: https://docs.baseten.co/reference/management-api/deployments/gets-all-chain-deployments

get /v1/chains/{chain_id}/deployments



# Get all model deployments
Source: https://docs.baseten.co/reference/management-api/deployments/gets-all-deployments-of-a-model

get /v1/models/{model_id}/deployments



# Cancel model promotion
Source: https://docs.baseten.co/reference/management-api/deployments/promote/cancel-promotion

post /v1/models/{model_id}/environments/{env_name}/cancel_promotion
Cancels an ongoing promotion to an environment and returns the cancellation status.

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "status": "CANCELED",
    "message": "Promotion to production was successfully canceled."
  }
  ```

  ```json 400 theme={"system"}
  {
    "code": "VALIDATION_ERROR",
    "message": "Environment production has no in progress promotion."
  }
  ```
</ResponseExample>


# Promote to chain environment
Source: https://docs.baseten.co/reference/management-api/deployments/promote/promotes-a-chain-deployment-to-an-environment

post /v1/chains/{chain_id}/environments/{env_name}/promote
Promotes an existing chain deployment to an environment and returns the promoted chain deployment.



# Promote to model environment
Source: https://docs.baseten.co/reference/management-api/deployments/promote/promotes-a-deployment-to-an-environment

post /v1/models/{model_id}/environments/{env_name}/promote
Promotes an existing deployment to an environment and returns the promoted deployment.



# Any model deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/promote/promotes-a-deployment-to-production

post /v1/models/{model_id}/deployments/{deployment_id}/promote
Promotes an existing deployment to production and returns the same deployment.



# Development model deployment
Source: https://docs.baseten.co/reference/management-api/deployments/promote/promotes-a-development-deployment-to-production

post /v1/models/{model_id}/deployments/development/promote
Creates a new production deployment from the development deployment, the currently building deployment is returned.



# Create Chain environment
Source: https://docs.baseten.co/reference/management-api/environments/create-a-chain-environment

post /v1/chains/{chain_id}/environments
Create a chain environment. Returns the resulting environment.



# Create environment
Source: https://docs.baseten.co/reference/management-api/environments/create-an-environment

post /v1/models/{model_id}/environments
Creates an environment for the specified model and returns the environment.



# Get Chain environment
Source: https://docs.baseten.co/reference/management-api/environments/get-a-chain-environments-details

get /v1/chains/{chain_id}/environments/{env_name}
Gets a chain environment's details and returns the chain environment.



# Get all Chain environments
Source: https://docs.baseten.co/reference/management-api/environments/get-all-chain-environments

get /v1/chains/{chain_id}/environments
Gets all chain environments for a given chain



# Get all environments
Source: https://docs.baseten.co/reference/management-api/environments/get-all-environments

get /v1/models/{model_id}/environments
Gets all environments for a given model



# Get environment
Source: https://docs.baseten.co/reference/management-api/environments/get-an-environments-details

get /v1/models/{model_id}/environments/{env_name}
Gets an environment's details and returns the environment.



# Update Chain environment
Source: https://docs.baseten.co/reference/management-api/environments/update-a-chain-environments-settings

patch /v1/chains/{chain_id}/environments/{env_name}
Update a chain environment's settings and returns the chain environment.



# Update chainlet environment's instance type
Source: https://docs.baseten.co/reference/management-api/environments/update-a-chainlet-environments-instance-type-settings

post /v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/instance_types/update
Updates a chainlet environment's instance type settings. The chainlet environment setting must exist. When updated, a new chain deployment is created and deployed. It is promoted to the chain environment according to promotion settings on the environment.



# Update model environment
Source: https://docs.baseten.co/reference/management-api/environments/update-an-environments-settings

patch /v1/models/{model_id}/environments/{env_name}
Updates an environment's settings and returns the updated environment.



# All instance types
Source: https://docs.baseten.co/reference/management-api/instance-types/gets-all-instance-types

get /v1/instance_types



# Instance type prices
Source: https://docs.baseten.co/reference/management-api/instance-types/gets-instance-type-prices

get /v1/instance_type_prices



# Delete models
Source: https://docs.baseten.co/reference/management-api/models/deletes-a-model-by-id

delete /v1/models/{model_id}



# By ID
Source: https://docs.baseten.co/reference/management-api/models/gets-a-model-by-id

get /v1/models/{model_id}



# All models
Source: https://docs.baseten.co/reference/management-api/models/gets-all-models

get /v1/models



# Overview
Source: https://docs.baseten.co/reference/management-api/overview

The management API is used to manage models and deployments. It supports monitoring, CI/CD, and automation at both the model and workspace levels.

## Model endpoints

| Method | Endpoint                                                                          | Description      |
| :----- | :-------------------------------------------------------------------------------- | :--------------- |
| `GET`  | [`/v1/models`](/reference/management-api/models/gets-all-models)                  | Get all models   |
| `GET`  | [`/v1/models/{model_id}`](/reference/management-api/models/gets-a-model-by-id)    | Get models by ID |
| `DEL`  | [`/v1/models/{model_id}`](/reference/management-api/models/deletes-a-model-by-id) | Delete models    |

## Chain endpoints

| Method | Endpoint                                                                          | Description          |
| :----- | :-------------------------------------------------------------------------------- | :------------------- |
| `GET`  | [`/v1/chains`](/reference/management-api/chains/gets-all-chains)                  | Get all Chains       |
| `GET`  | [`/v1/chains/{chain_id}`](/reference/management-api/chains/gets-a-chain-by-id)    | Get all Chains by ID |
| `DEL`  | [`/v1/chains/{chain_id}`](/reference/management-api/chains/deletes-a-chain-by-id) | Delete Chains        |

## Deployment endpoints

<Tabs>
  <Tab title="Models">
    ### Activate a model deployment

    | Method | Endpoint                                                                                                                                                         | Description                 |
    | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
    | `POST` | [`/v1/models/{model_id}/environments/{env_name}/activate`](/reference/management-api/deployments/activate/activates-a-deployment-associated-with-an-environment) | **Activate** an environment |
    | `POST` | [`/v1/models/{model_id}/deployments/development/activate`](/reference/management-api/deployments/activate/activates-a-development-deployment)                    | **Activate** development    |
    | `POST` | [`/v1/models/{model_id}/deployments/{deployment_id}/activate`](/reference/management-api/deployments/activate/activates-a-deployment)                            | **Activate** a deployment   |

    ### Deactivate a model deployment

    | Method | Endpoint                                                                                                                                                               | Description                   |
    | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
    | `POST` | [`/v1/models/{model_id}/environments/{env_name}/deactivate`](/reference/management-api/deployments/deactivate/deactivates-a-deployment-associated-with-an-environment) | **Deactivate** an environment |
    | `POST` | [`/v1/models/{model_id}/deployments/development/deactivate`](/reference/management-api/deployments/deactivate/deactivates-a-development-deployment)                    | **Deactivate** development    |
    | `POST` | [`/v1/models/{model_id}/deployments/{deployment_id}/deactivate`](/reference/management-api/deployments/deactivate/deactivates-a-deployment)                            | **Deactivate** a deployment   |

    ### Promote a model deployment

    | Method | Endpoint                                                                                                                                                 | Description                              |
    | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------- |
    | `POST` | [`/v1/models/{model_id}/environments/{env_name}/promote`](/reference/management-api/deployments/promote/promotes-a-deployment-to-an-environment)         | **Promote** to model **environment**     |
    | `POST` | [`/v1/models/{model_id}/environments/{env_name}/cancel_promotion`](/reference/management-api/deployments/promote/cancel-promotion)                       | **Cancel** a promotion to an environment |
    | `POST` | [`/v1/models/{model_id}/deployments/development/promote`](/reference/management-api/deployments/promote/promotes-a-development-deployment-to-production) | **Promote** development deployment       |
    | `POST` | [`/v1/models/{model_id}/deployments/{deployment_id}/promote`](/reference/management-api/deployments/promote/promotes-a-deployment-to-production)         | **Promote** any deployment               |

    ### Autoscaling

    | Method  | Endpoint                                                                                                                                                       | Description                                     |
    | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------- |
    | `PATCH` | [`.../deployments/development/autoscaling_settings`](/reference/management-api/deployments/autoscaling/updates-a-development-deployments-autoscaling-settings) | Updates **development's autoscaling** settings  |
    | `PATCH` | [`.../deployments/{deployment_id}/autoscaling_settings`](/reference/management-api/deployments/autoscaling/updates-a-deployments-autoscaling-settings)         | Updates a **deployment's autoscaling** settings |

    ### Manage deployment endpoints

    | Method | Endpoint                                                                                                                       | Description                  |
    | :----- | :----------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
    | `GET`  | [`/v1/models/{model_id}/deployments`](/reference/management-api/deployments/gets-all-deployments-of-a-model)                   | Get all model deployments    |
    | `GET`  | [`/v1/models/{model_id}/deployments/production`](/reference/management-api/deployments/gets-a-models-production-deployment)    | Production model deployment  |
    | `GET`  | [`/v1/models/{model_id}/deployments/development`](/reference/management-api/deployments/gets-a-models-development-deployment)  | Development model deployment |
    | `GET`  | [`/v1/models/{model_id}/deployments/{deployment_id}`](/reference/management-api/deployments/gets-a-models-deployment-by-id)    | Any model deployment by ID   |
    | `DEL`  | [`/v1/models/{model_id}/deployments/{deployment_id}`](/reference/management-api/deployments/deletes-a-models-deployment-by-id) | Delete model deployments     |
  </Tab>

  <Tab title="Chains">
    ### Promote a Chain deployment

    | Method | Endpoint                                                                                                                                               | Description                  |
    | :----- | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
    | `POST` | [`/v1/chains/{chain_id}/environments/{env_name}/promote`](/reference/management-api/deployments/promote/promotes-a-chain-deployment-to-an-environment) | Promote to chain environment |

    ### Autoscaling

    | Method  | Endpoint                                                                                                                                              | Description                                            |
    | :------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
    | `PATCH` | [`.../chainlet_settings/autoscaling_settings`](/reference/management-api/deployments/autoscaling/update-a-chainlet-environments-autoscaling-settings) | **Update chainlet** environment's autoscaling settings |

    ### Manage Chain deployments

    | Method | Endpoint                                                                                                                            | Description                  |
    | :----- | :---------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
    | `GET`  | [`/v1/chains/{chain_id}/deployments`](/reference/management-api/deployments/gets-all-chain-deployments)                             | Get all chain deployments    |
    | `GET`  | [`/v1/chains/{chain_id}/deployments/{chain_deployment_id}`](/reference/management-api/deployments/gets-a-chain-deployment-by-id)    | Any chain deployment by ID   |
    | `DEL`  | [`/v1/chains/{chain_id}/deployments/{chain_deployment_id}`](/reference/management-api/deployments/deletes-a-chain-deployment-by-id) | **Delete** chain deployments |
  </Tab>
</Tabs>

## Environment endpoints

<Tabs>
  <Tab title="Models">
    | Method  | Endpoint                                                                                                                  | Description                |
    | :------ | :------------------------------------------------------------------------------------------------------------------------ | :------------------------- |
    | `POST`  | [`/v1/models/{model_id}/environments`](/reference/management-api/environments/create-an-environment)                      | Create environment         |
    | `GET`   | [`/v1/models/{model_id}/environments`](/reference/management-api/environments/get-all-environments)                       | Get all environments       |
    | `GET`   | [`/v1/models/{model_id}/environments/{env_name}`](/reference/management-api/environments/get-an-environments-details)     | Get an environment details |
    | `PATCH` | [`/v1/models/{model_id}/environments/{env_name}`](/reference/management-api/environments/update-an-environments-settings) | Update model environment   |
  </Tab>

  <Tab title="Chains">
    | Method  | Endpoint                                                                                                                                                                                | Description                                 |
    | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------ |
    | `POST`  | [`/v1/chains/{chain_id}/environments`](/reference/management-api/environments/create-a-chain-environment)                                                                               | Create chain environment                    |
    | `GET`   | [`/v1/chains/{chain_id}/environments`](/reference/management-api/environments/get-all-chain-environments)                                                                               | Get all chain environments                  |
    | `GET`   | [`/v1/chains/{chain_id}/environments/{env_name}`](/reference/management-api/environments/get-a-chain-environments-details)                                                              | Get a chain environment                     |
    | `PATCH` | [`/v1/chains/{chain_id}/environments/{env_name}`](/reference/management-api/environments/update-a-chain-environments-settings)                                                          | Update chain environment                    |
    | `POST`  | [`/v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/instance_types/update`](/reference/management-api/environments/update-a-chainlet-environments-instance-type-settings) | Update chainlet environment's instance type |
  </Tab>
</Tabs>

## Instance type endpoints

| Method | Endpoint                                                                                         | Description              |
| :----- | :----------------------------------------------------------------------------------------------- | :----------------------- |
| `GET`  | [`/v1/instance_types`](/reference/management-api/instance-types/gets-all-instance-types)         | Get all instance types   |
| `GET`  | [`/v1/instance_type_prices`](/reference/management-api/instance-types/gets-instance-type-prices) | Get instance type prices |

## Team endpoints

| Method | Endpoint                                                       | Description   |
| :----- | :------------------------------------------------------------- | :------------ |
| `GET`  | [`/v1/teams`](/reference/management-api/teams/lists-all-teams) | Get all teams |

## Secret endpoints

| Method | Endpoint                                                                               | Description                    |
| :----- | :------------------------------------------------------------------------------------- | :----------------------------- |
| `GET`  | [`/v1/secrets`](/reference/management-api/secrets/gets-all-secrets)                    | Get all secrets                |
| `POST` | [`/v1/secrets`](/reference/management-api/secrets/upserts-a-secret)                    | Create or update a secret      |
| `GET`  | [`/v1/teams/{team_id}/secrets`](/reference/management-api/teams/gets-all-team-secrets) | Get all team secrets           |
| `POST` | [`/v1/teams/{team_id}/secrets`](/reference/management-api/teams/upserts-a-team-secret) | Create or update a team secret |

## API Key endpoints

| Method   | Endpoint                                                                                 | Description           |
| :------- | :--------------------------------------------------------------------------------------- | :-------------------- |
| `GET`    | [`/v1/api_keys`](/reference/management-api/api-keys/lists-the-users-api-keys)            | Get all API keys      |
| `POST`   | [`/v1/api_keys`](/reference/management-api/api-keys/creates-an-api-key)                  | Create an API key     |
| `DELETE` | [`/v1/api_keys/{api_key_prefix}`](/reference/management-api/api-keys/delete-an-api-key)  | Delete an API key     |
| `POST`   | [`/v1/teams/{team_id}/api_keys`](/reference/management-api/teams/creates-a-team-api-key) | Create a team API key |

## Training endpoints

| Method | Endpoint                                                                                                                                           | Description                     |
| :----- | :------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------ |
| `POST` | [`/v1/teams/{team_id}/training_projects`](/reference/management-api/teams/creates-a-team-training-project)                                         | Create a team training project  |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs`](/reference/training-api/list-training-jobs)                                                   | Get all training jobs           |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}`](/reference/training-api/get-training-job)                                   | Get training job by ID          |
| `POST` | [`/v1/training_jobs/search`](/reference/training-api/search-training-jobs)                                                                         | Search training jobs            |
| `POST` | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/stop`](/reference/training-api/stop-training-job)                             | Stop a training job             |
| `POST` | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/recreate`](/reference/training-api/recreate-training-job)                     | Recreate a training job         |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoints`](/reference/training-api/get-training-job-checkpoints)           | Get training job checkpoints    |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files`](/reference/training-api/get-training-job-checkpoint-files) | Get checkpoint files            |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs`](/reference/training-api/get-training-job-logs)                         | Get training job logs           |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics`](/reference/training-api/get-training-job-metrics)                   | Get training job metrics        |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/download`](/reference/training-api/download-training-job)                     | Download training job artifacts |


# Get all secrets
Source: https://docs.baseten.co/reference/management-api/secrets/gets-all-secrets

get /v1/secrets



# Upsert a secret
Source: https://docs.baseten.co/reference/management-api/secrets/upserts-a-secret

post /v1/secrets
Creates a new secret or updates an existing secret if one with the provided name already exists. The name and creation date of the created or updated secret is returned.



# Create a team API key
Source: https://docs.baseten.co/reference/management-api/teams/creates-a-team-api-key

post /v1/teams/{team_id}/api_keys
Creates a team API key with the provided name and type. The API key is returned in the response.



# Create a team training project
Source: https://docs.baseten.co/reference/management-api/teams/creates-a-team-training-project

post /v1/teams/{team_id}/training_projects
Upserts a training project with the specified metadata for a team.



# Get all team secrets
Source: https://docs.baseten.co/reference/management-api/teams/gets-all-team-secrets

get /v1/teams/{team_id}/secrets



# List all teams
Source: https://docs.baseten.co/reference/management-api/teams/lists-all-teams

get /v1/teams
Returns a list of all teams the authenticated user has access to.



# Upsert a team secret
Source: https://docs.baseten.co/reference/management-api/teams/upserts-a-team-secret

post /v1/teams/{team_id}/secrets
Creates a new secret or updates an existing secret if one with the provided name already exists. The name and creation date of the created or updated secret is returned. This secret belongs to the specified team



# Reference documentation
Source: https://docs.baseten.co/reference/overview

For deploying, managing, and interacting with machine learning models on Baseten.

This reference section documents our API, CLI, and Python SDK—whether you're deploying models, managing inference chains, or calling endpoints in production.

## API Reference

Baseten provides two sets of API endpoints:

<CardGroup>
  <Card title="Inference API" href="/reference/inference-api/overview">
    For calling deployed models and chains.
  </Card>

  <Card title="Management API" href="/reference/management-api/overview">
    For managing models, workspaces, and training jobs.
  </Card>
</CardGroup>

## CLI Reference

The CLI provides a command-line interface for managing deployments, running local inference, and configuring Truss models.

* [Truss CLI reference](/reference/cli/truss/overview) – Commands for initializing, deploying, and managing models.
* [Chains CLI reference](/reference/cli/chains/chains-cli) – Commands for orchestrating multi-model workflows.
* [Training CLI reference](/reference/cli/training/training-cli) – Commands for managing training jobs.

***

## SDK Reference

The Python SDK provides an abstraction for deploying models, managing deployments, and interacting with models via code.

* [Truss SDK reference](/reference/sdk/truss) – Deploy and interact with Truss models using Python.
* [Chains SDK reference](/reference/sdk/chains) – Build and manage inference chains programmatically.
* [Training SDK reference](/reference/sdk/training) – Deploy and interact with trained models using Python.


# Chains SDK Reference
Source: https://docs.baseten.co/reference/sdk/chains

Python SDK Reference for Chains

# Chainlet classes

APIs for creating user-defined Chainlets.

### *class* `truss_chains.ChainletBase`

Base class for all chainlets.

Inheriting from this class adds validations to make sure subclasses adhere to the
chainlet pattern and facilitates remote chainlet deployment.

Refer to [the docs](/development/chain/getting-started) and this
[example chainlet](https://github.com/basetenlabs/truss/blob/main/truss-chains/truss_chains/reference_code/reference_chainlet.py)
for more guidance on how to create subclasses.

### *class* `truss_chains.ModelBase`

Base class for all standalone models.

Inheriting from this class adds validations to make sure subclasses adhere to the
truss model pattern.

### *class* `truss_chains.EngineBuilderLLMChainlet`

#### *method final async* run\_remote(llm\_input)

**Parameters:**

| Name        | Type                    | Description                |
| ----------- | ----------------------- | -------------------------- |
| `llm_input` | *EngineBuilderLLMInput* | OpenAI compatible request. |

* **Returns:**
  *AsyncIterator*\[str]

### *function* `truss_chains.depends`

Sets a “symbolic marker” to indicate to the framework that a chainlet is a
dependency of another chainlet. The return value of `depends` is intended to be
used as a default argument in a chainlet’s `__init__`-method.
When deploying a chain remotely, a corresponding stub to the remote is injected in
its place. In [`run_local`](#function-truss-chains-run-local) mode an instance
of a local chainlet is injected.

Refer to [the docs](/development/chain/getting-started) and this
[example chainlet](https://github.com/basetenlabs/truss/blob/main/truss-chains/truss_chains/reference_code/reference_chainlet.py)
for more guidance on how make one chainlet depend on another chainlet.

<Warning>
  Despite the type annotation, this does *not* immediately provide a
  chainlet instance. Only when deploying remotely or using `run_local` a
  chainlet instance is provided.
</Warning>

**Parameters:**

| Name                | Type                                                      | Default | Description                                                                                                                                                                                                                                                                                |
| ------------------- | --------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `chainlet_cls`      | *Type\[[ChainletBase](#class-truss-chains-chainletbase)]* |         | The chainlet class of the dependency.                                                                                                                                                                                                                                                      |
| `retries`           | *int*                                                     | `1`     | The number of times to retry the remote chainlet in case of failures (e.g. due to transient network issues). For streaming, retries are only made if the request fails before streaming any results back. Failures mid-stream not retried.                                                 |
| `timeout_sec`       | *float*                                                   | `600.0` | Timeout for the HTTP request to this chainlet.                                                                                                                                                                                                                                             |
| `use_binary`        | *bool*                                                    | `False` | Whether to send data in binary format. This can give a parsing speedup and message size reduction (\~25%) for numpy arrays. Use `NumpyArrayField` as a field type on pydantic models for integration and set this option to `True`. For simple text data, there is no significant benefit. |
| `concurrency_limit` | *int*                                                     | `300`   | The maximum number of concurrent requests to send to the remote chainlet. Excessive requests will be queued and a warning will be shown. Try to design your algorithm in a way that spreads requests evenly over time so that this the default value can be used.                          |

* **Returns:**
  A “symbolic marker” to be used as a default argument in a chainlet’s
  initializer.

### *function* `truss_chains.depends_context`

Sets a “symbolic marker” for injecting a context object at runtime.

Refer to [the docs](/development/chain/getting-started) and this
[example chainlet](https://github.com/basetenlabs/truss/blob/main/truss-chains/truss_chains/reference_code/reference_chainlet.py)
for more guidance on the `__init__`-signature of chainlets.

<Warning>
  Despite the type annotation, this does *not* immediately provide a
  context instance. Only when deploying remotely or using `run_local` a
  context instance is provided.
</Warning>

* **Returns:**
  A “symbolic marker” to be used as a default argument in a chainlet’s
  initializer.

### *class* `truss_chains.DeploymentContext`

Bases: `pydantic.BaseModel`

Bundles config values and resources needed to instantiate Chainlets.

The context can optionally be added as a trailing argument in a Chainlet’s
`__init__` method and then used to set up the chainlet (e.g. using a secret as
an access token for downloading model weights).

**Parameters:**

| Name                  | Type                                                                                       | Default | Description                                                                                                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `chainlet_to_service` | *Mapping\[str,[DeployedServiceDescriptor](#class-truss-chains-deployedservicedescriptor)]* |         | A mapping from chainlet names to service descriptors. This is used to create RPC sessions to dependency chainlets. It contains only the chainlet services that are dependencies of the current chainlet. |
| `secrets`             | *Mapping\[str,str]*                                                                        |         | A mapping from secret names to secret values. It contains only the secrets that are listed in `remote_config.assets.secret_keys` of the current chainlet.                                                |
| `data_dir`            | *Path\|None*                                                                               | `None`  | The directory where the chainlet can store and access data, e.g. for downloading model weights.                                                                                                          |
| `environment`         | *[Environment](#class-truss-chains-environment)\|None*                                     | `None`  | The environment that the chainlet is deployed in. None if the chainlet is not associated with an environment.                                                                                            |

#### *method* get\_baseten\_api\_key()

* **Returns:**
  str

#### *method* get\_service\_descriptor(chainlet\_name)

**Parameters:**

| Name            | Type  | Description               |
| --------------- | ----- | ------------------------- |
| `chainlet_name` | *str* | The name of the chainlet. |

* **Returns:**
  [*DeployedServiceDescriptor*](#class-truss-chains-deployedservicedescriptor)

### *class* `truss_chains.Environment`

Bases: `pydantic.BaseModel`

The environment the chainlet is deployed in.

* **Parameters:**
  **name** (*str*) – The name of the environment.

### *class* `truss_chains.ChainletOptions`

Bases: `pydantic.BaseModel`

**Parameters:**

| Name                     | Type                                                  | Default                                  | Description                                                                                                                                                                                                                                                   |
| ------------------------ | ----------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enable_b10_tracing`     | *bool*                                                | `False`                                  | enables baseten-internal trace data collection. This helps baseten engineers better analyze chain performance in case of issues. It is independent of a potentially user-configured tracing instrumentation. Turning this on, could add performance overhead. |
| `enable_debug_logs`      | *bool*                                                | `False`                                  | Sets log level to debug in deployed server.                                                                                                                                                                                                                   |
| `env_variables`          | *Mapping\[str,str]*                                   | `{}`                                     | static environment variables available to the deployed chainlet.                                                                                                                                                                                              |
| `health_checks`          | *HealthChecks*                                        | `truss.base.truss_config.HealthChecks()` | Configures health checks for the chainlet. See [guide](https://docs.baseten.co/truss/guides/custom-health-checks#chains).                                                                                                                                     |
| `metadata`               | *JsonValue\|None*                                     | `None`                                   | Arbitrary JSON object to describe chainlet.                                                                                                                                                                                                                   |
| `streaming_read_timeout` | *int*                                                 | `60`                                     | Amount of time (in seconds) between each streamed chunk before a timeout is triggered.                                                                                                                                                                        |
| `transport`              | *Union\[HTTPOptions\|WebsocketOptions\|GRPCOptions]'* | `None`                                   | Allows to customize certain transport protocols, e.g. websocket pings.                                                                                                                                                                                        |

### *class* `truss_chains.RPCOptions`

Bases: `pydantic.BaseModel`

Options to customize RPCs to dependency chainlets.

**Parameters:**

| Name                | Type    | Default | Description                                                                                                                                                                                                                                                                                |
| ------------------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `retries`           | *int*   | `1`     | The number of times to retry the remote chainlet in case of failures (e.g. due to transient network issues). For streaming, retries are only made if the request fails before streaming any results back. Failures mid-stream not retried.                                                 |
| `timeout_sec`       | *float* | `600.0` | Timeout for the HTTP request to this chainlet.                                                                                                                                                                                                                                             |
| `use_binary`        | *bool*  | `False` | Whether to send data in binary format. This can give a parsing speedup and message size reduction (\~25%) for numpy arrays. Use `NumpyArrayField` as a field type on pydantic models for integration and set this option to `True`. For simple text data, there is no significant benefit. |
| `concurrency_limit` | *int*   | `300`   | The maximum number of concurrent requests to send to the remote chainlet. Excessive requests will be queued and a warning will be shown. Try to design your algorithm in a way that spreads requests evenly over time so that this the default value can be used.                          |

### *function* `truss_chains.mark_entrypoint`

Decorator to mark a chainlet as the entrypoint of a chain.

This decorator can be applied to *one* chainlet in a source file and then the
CLI push command simplifies: only the file, not the class within, must be specified.

Optionally a display name for the Chain (not the Chainlet) can be set (effectively
giving a custom default value for the `name` arg of the CLI push command).

Example usage:

```python theme={"system"}
import truss_chains as chains

@chains.mark_entrypoint
class MyChainlet(ChainletBase):
    ...

# OR with custom Chain name.
@chains.mark_entrypoint("My Chain Name")
class MyChainlet(ChainletBase):
    ...
```

# Remote Configuration

These data structures specify for each chainlet how it gets deployed remotely, e.g. dependencies and compute resources.

### *class* `truss_chains.RemoteConfig`

Bases: `pydantic.BaseModel`

Bundles config values needed to deploy a chainlet remotely.

This is specified as a class variable for each chainlet class, e.g.:

```python theme={"system"}
import truss_chains as chains


class MyChainlet(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            pip_requirements=["torch==2.0.1", ...]
        ),
        compute=chains.Compute(cpu_count=2, gpu="A10G", ...),
        assets=chains.Assets(secret_keys=["hf_access_token"], ...),
    )
```

**Parameters:**

| Name           | Type                                                     | Default                          |
| -------------- | -------------------------------------------------------- | -------------------------------- |
| `docker_image` | *[DockerImage](#class-truss-chains-dockerimage)*         | `truss_chains.DockerImage()`     |
| `compute`      | *[Compute](#class-truss-chains-compute)*                 | `truss_chains.Compute()`         |
| `assets`       | *[Assets](#class-truss-chains-assets)*                   | `truss_chains.Assets()`          |
| `name`         | *str\|None*                                              | `None`                           |
| `options`      | *[ChainletOptions](#class-truss-chains-chainletoptions)* | `truss_chains.ChainletOptions()` |

### *class* `truss_chains.DockerImage`

Bases: `pydantic.BaseModel`

Configures the docker image in which a remoted chainlet is deployed.

<Note>
  Any paths are relative to the source file where `DockerImage` is
  defined and must be created with the helper function \[`make_abs_path_here`]
  (#function-truss-chains-make-abs-path-here).
  This allows you for example organize chainlets in different (potentially nested)
  modules and keep their requirement files right next their python source files.
</Note>

**Parameters:**

| Name                            | Type                                                                                               | Default                       | Description                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `base_image`                    | *[BasetenImage](#class-truss-chains-basetenimage)\|[CustomImage](#class-truss-chains-customimage)* | `truss_chains.BasetenImage()` | The base image used by the chainlet. Other dependencies and assets are included as additional layers on top of that image. You can choose a Baseten default image for a supported python version (e.g. `BasetenImage.PY311`), this will also include GPU drivers if needed, or provide a custom image (e.g. `CustomImage(image="python:3.11-slim")`).                                      |
| `pip_requirements_file`         | *AbsPath\|None*                                                                                    | `None`                        | Path to a file containing pip requirements. The file content is naively concatenated with `pip_requirements`.                                                                                                                                                                                                                                                                              |
| `pip_requirements`              | *list\[str]*                                                                                       | `[]`                          | A list of pip requirements to install.  The items are naively concatenated with the content of the `pip_requirements_file`.                                                                                                                                                                                                                                                                |
| `apt_requirements`              | *list\[str]*                                                                                       | `[]`                          | A list of apt requirements to install.                                                                                                                                                                                                                                                                                                                                                     |
| `data_dir`                      | *AbsPath\|None*                                                                                    | `None`                        | Data from this directory is copied into the docker image and accessible to the remote chainlet at runtime.                                                                                                                                                                                                                                                                                 |
| `external_package_dirs`         | *list\[AbsPath]\|None*                                                                             | `None`                        | A list of directories containing additional python packages outside the chain’s workspace dir, e.g. a shared library. This code is copied into the docker image and importable at runtime.                                                                                                                                                                                                 |
| `truss_server_version_override` | *str\|None*                                                                                        | `None`                        | By default, deployed Chainlets use the truss server implementation corresponding to the truss version of the user’s CLI. To use a specific version, e.g. pinning it for exact reproducibility, the version can be overridden here. Valid versions correspond to truss releases on PyPi: [https://pypi.org/project/truss/#history](https://pypi.org/project/truss/#history), e.g. “0.9.80”. |

### *class* `truss_chains.BasetenImage`

Bases: `Enum`

Default images, curated by baseten, for different python versions. If a Chainlet
uses GPUs, drivers will be included in the image.

| Enum Member | Value   |
| ----------- | ------- |
| `PY39`      | *py39*  |
| `PY310`     | *py310* |
| `PY311`     | *py311* |
| `PY312`     | *py312* |
| `PY313`     | *py313* |
| `PY314`     | *py314* |

### *class* `truss_chains.CustomImage`

Bases: `pydantic.BaseModel`

Configures the usage of a custom image hosted on dockerhub.

**Parameters:**

| Name                     | Type                       | Default | Description                                                                                            |
| ------------------------ | -------------------------- | ------- | ------------------------------------------------------------------------------------------------------ |
| `image`                  | *str*                      |         | Reference to image on dockerhub.                                                                       |
| `python_executable_path` | *str\|None*                | `None`  | Absolute path to python executable (if default `python` is ambiguous).                                 |
| `docker_auth`            | *DockerAuthSettings\|None* | `None`  | See [corresponding truss config](/development/model/base-images#example%3A-docker-hub-authentication). |

### *class* `truss_chains.Compute`

Specifies which compute resources a chainlet has in the *remote* deployment.

<Note>
  Not all combinations can be exactly satisfied by available hardware, in some
  cases more powerful machine types are chosen to make sure requirements are met
  or over-provisioned. Refer to the
  [baseten instance reference](https://docs.baseten.co/deployment/resources).
</Note>

**Parameters:**

| Name                  | Type                          | Default | Description                                                                                                     |
| --------------------- | ----------------------------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| `cpu_count`           | *int*                         | `1`     | Minimum number of CPUs to allocate.                                                                             |
| `memory`              | *str*                         | `'2Gi'` | Minimum memory to allocate, e.g. “2Gi” (2 gibibytes).                                                           |
| `gpu`                 | *str\|Accelerator\|None*      | `None`  | GPU accelerator type, e.g. “A10G”, “A100”, refer to the [truss config](/deployment/resources) for more choices. |
| `gpu_count`           | *int*                         | `1`     | Number of GPUs to allocate.                                                                                     |
| `predict_concurrency` | *int\|Literal\['cpu\_count']* | `1`     | Number of concurrent requests a single replica of a deployed chainlet handles.                                  |

Concurrency concepts are explained in [this guide](/development/model/concurrency#2-predict-concurrency).
It is important to understand the difference between predict\_concurrency and
the concurrency target (used for autoscaling, i.e. adding or removing replicas).
Furthermore, the `predict_concurrency` of a single instance is implemented in
two ways:

* Via python’s `asyncio`, if `run_remote` is an async def. This
  requires that `run_remote` yields to the event loop.
* With a threadpool if it’s a synchronous function. This requires
  that the threads don’t have significant CPU load (due to the GIL).

### *class* `truss_chains.Assets`

Specifies which assets a chainlet can access in the remote deployment.

For example, model weight caching can be used like this:

```python theme={"system"}
import truss_chains as chains
from truss.base import truss_config

mistral_cache = truss_config.ModelRepo(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    allow_patterns=["*.json", "*.safetensors", ".model"]
)
chains.Assets(cached=[mistral_cache], ...)
```

**Parameters:**

| Name            | Type                          | Default | Description                                                                                                                                                     |
| --------------- | ----------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cached`        | *Iterable\[ModelRepo]*        | `()`    | One or more `truss_config.ModelRepo` objects.                                                                                                                   |
| `secret_keys`   | *Iterable\[str]*              | `()`    | Names of secrets stored on baseten, that the chainlet should have access to. You can manage secrets on baseten [here](https://app.baseten.co/settings/secrets). |
| `external_data` | *Iterable\[ExternalDataItem]* | `()`    | Data to be downloaded from public URLs and made available in the deployment (via `context.data_dir`).                                                           |

# Core

General framework and helper functions.

### *function* `truss_chains.push`

Deploys a chain remotely (with all dependent chainlets).

**Parameters:**

| Name                    | Type                             | Default     | Description                                                                                                                                                  |
| ----------------------- | -------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `entrypoint`            | *Type\[ChainletT]*               |             | The chainlet class that serves as the entrypoint to the chain.                                                                                               |
| `chain_name`            | *str*                            |             | The name of the chain.                                                                                                                                       |
| `publish`               | *bool*                           | `True`      | Whether to publish the chain as a published deployment (it is a draft deployment otherwise)                                                                  |
| `promote`               | *bool*                           | `True`      | Whether to promote the chain to be the production deployment (this implies publishing as well).                                                              |
| `only_generate_trusses` | *bool*                           | `False`     | Used for debugging purposes. If set to True, only the the underlying truss models for the chainlets are generated in `/tmp/.chains_generated`.               |
| `remote`                | *str*                            | `'baseten'` | name of a remote config in .trussrc. If not provided, it will be inquired.                                                                                   |
| `environment`           | *str\|None*                      | `None`      | The name of an environment to promote deployment into.                                                                                                       |
| `progress_bar`          | *Type\[progress.Progress]\|None* | `None`      | Optional rich.progress.Progress if output is desired.                                                                                                        |
| `include_git_info`      | *bool*                           | `False`     | Whether to attach git versioning info (sha, branch, tag) to deployments made from within a git repo. If set to True in .trussrc, it will always be attached. |

* **Returns:**
  [*ChainService*](#class-truss-chains-remote-chainservice): A chain service
  handle to the deployed chain.

### *class* `truss_chains.deployment.deployment_client.ChainService`

Handle for a deployed chain.

A `ChainService` is created and returned when using `push`. It
bundles the individual services for each chainlet in the chain, and provides
utilities to query their status, invoke the entrypoint etc.

#### *method* get\_info()

Queries the statuses of all chainlets in the chain.

* **Returns:**
  List of `DeployedChainlet`, `(name, is_entrypoint, status, logs_url)`
  for each chainlet.

#### *property* name *: str*

#### *method* run\_remote(json)

Invokes the entrypoint with JSON data.

**Parameters:**

| Name   | Type        | Description                  |
| ------ | ----------- | ---------------------------- |
| `json` | *JSON dict* | Input data to the entrypoint |

* **Returns:**
  The JSON response.

#### *property* run\_remote\_url *: str*

URL to invoke the entrypoint.

#### *property* status\_page\_url *: str*

Link to status page on Baseten.

### *function* `truss_chains.make_abs_path_here`

Helper to specify file paths relative to the *immediately calling* module.

E.g. in you have a project structure like this:

```default theme={"system"}
root/
    chain.py
    common_requirements.text
    sub_package/
        chainlet.py
        chainlet_requirements.txt
```

You can now in `root/sub_package/chainlet.py` point to the requirements
file like this:

```python theme={"system"}
shared = make_abs_path_here("../common_requirements.text")
specific = make_abs_path_here("chainlet_requirements.text")
```

<Warning>
  This helper uses the directory of the immediately calling module as an
  absolute reference point for resolving the file location. Therefore,
  you MUST NOT wrap the instantiation of `make_abs_path_here` into a
  function (e.g. applying decorators) or use dynamic code execution.

  Ok:

  ```python theme={"system"}
  def foo(path: AbsPath):
      abs_path = path.abs_path


  foo(make_abs_path_here("./somewhere"))
  ```

  Not Ok:

  ```python theme={"system"}
  def foo(path: str):
      dangerous_value = make_abs_path_here(path).abs_path


  foo("./somewhere")
  ```
</Warning>

**Parameters:**

| Name        | Type  | Description                |
| ----------- | ----- | -------------------------- |
| `file_path` | *str* | Absolute or relative path. |

* **Returns:**
  *AbsPath*

### *function* `truss_chains.run_local`

Context manager local debug execution of a chain.

The arguments only need to be provided if the chainlets explicitly access any the
corresponding fields of [`DeploymentContext`](#class-truss-chains-deploymentcontext).

**Parameters:**

| Name                  | Type                                                                                       | Default | Description                                                    |
| --------------------- | ------------------------------------------------------------------------------------------ | ------- | -------------------------------------------------------------- |
| `secrets`             | *Mapping\[str,str]\|None*                                                                  | `None`  | A dict of secrets keys and values to provide to the chainlets. |
| `data_dir`            | *Path\|str\|None*                                                                          | `None`  | Path to a directory with data files.                           |
| `chainlet_to_service` | *Mapping\[str,[DeployedServiceDescriptor](#class-truss-chains-deployedservicedescriptor)]* | `None`  | A dict of chainlet names to service descriptors.               |

Example usage (as trailing main section in a chain file):

```python theme={"system"}
import os
import truss_chains as chains


class HelloWorld(chains.ChainletBase):
    ...


if __name__ == "__main__":
    with chains.run_local(
        secrets={"some_token": os.environ["SOME_TOKEN"]},
        chainlet_to_service={
            "SomeChainlet": chains.DeployedServiceDescriptor(
                name="SomeChainlet",
                display_name="SomeChainlet",
                predict_url="https://...",
                options=chains.RPCOptions(),
            )
        },
    ):
        hello_world_chain = HelloWorld()
        result = hello_world_chain.run_remote(max_value=5)

    print(result)
```

Refer to the [local debugging guide](/development/chain/localdev)
for more details.

### *class* `truss_chains.DeployedServiceDescriptor`

Bases: `pydantic.BaseModel`

Bundles values to establish an RPC session to a dependency chainlet,
specifically with `StubBase`.

**Parameters:**

| Name           | Type                                           | Default |
| -------------- | ---------------------------------------------- | ------- |
| `name`         | *str*                                          |         |
| `display_name` | *str*                                          |         |
| `options`      | *[RPCOptions](#class-truss-chains-rpcoptions)* |         |
| `predict_url`  | *str\|None*                                    | `None`  |
| `internal_url` | *InternalURL*                                  | `None`  |

### *class* `truss_chains.StubBase`

Bases: `BasetenSession`, `ABC`

Base class for stubs that invoke remote chainlets.

Extends `BasetenSession` with methods for data serialization, de-serialization
and invoking other endpoints.

It is used internally for RPCs to dependency chainlets, but it can also be used
in user-code for wrapping a deployed truss model into the Chains framework. It
flexibly supports JSON and pydantic inputs and output. Example usage:

```python theme={"system"}
import pydantic
import truss_chains as chains


class WhisperOutput(pydantic.BaseModel):
    ...


class DeployedWhisper(chains.StubBase):
    # Input JSON, output JSON.
    async def run_remote(self, audio_b64: str) -> Any:
        return await self.predict_async(
            inputs={"audio": audio_b64})
        # resp == {"text": ..., "language": ...}

    # OR Input JSON, output pydantic model.
    async def run_remote(self, audio_b64: str) -> WhisperOutput:
        return await self.predict_async(
            inputs={"audio": audio_b64}, output_model=WhisperOutput)

    # OR Input and output are pydantic models.
    async def run_remote(self, data: WhisperInput) -> WhisperOutput:
        return await self.predict_async(data, output_model=WhisperOutput)


class MyChainlet(chains.ChainletBase):

    def __init__(self, ..., context=chains.depends_context()):
        ...
        self._whisper = DeployedWhisper.from_url(
            WHISPER_URL,
            context,
            options=chains.RPCOptions(retries=3),
        )

    async def run_remote(self, ...):
       await self._whisper.run_remote(...)
```

**Parameters:**

| Name                 | Type                                                                          | Description                               |
| -------------------- | ----------------------------------------------------------------------------- | ----------------------------------------- |
| `service_descriptor` | *[DeployedServiceDescriptor](#class-truss-chains-deployedservicedescriptor)]* | Contains the URL and other configuration. |
| `api_key`            | *str*                                                                         | A baseten API key to authorize requests.  |

#### *classmethod* from\_url(predict\_url, context\_or\_api\_key, options=None)

Factory method, convenient to be used in chainlet’s `__init__`-method.

**Parameters:**

| Name                 | Type                                                         | Description                                                                          |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `predict_url`        | *str*                                                        | URL to predict endpoint of another chain / truss model.                              |
| `context_or_api_key` | *[DeploymentContext](#class-truss-chains-deploymentcontext)* | Deployment context object, obtained in the chainlet’s `__init__` or Baseten API key. |
| `options`            | *[RPCOptions](#class-truss-chains-rpcoptions)*               | RPC options, e.g. retries.                                                           |

#### Invocation Methods

* `async predict_async(inputs: PydanticModel, output_model: Type[PydanticModel]) → PydanticModel`
* `async predict_async(inputs: JSON, output_model: Type[PydanticModel]) →
   PydanticModel`
* `async predict_async(inputs: JSON) → JSON`
* `async predict_async_stream(inputs: PydanticModel | JSON) -> AsyncIterator[bytes]`

Deprecated synchronous methods:

* `predict_sync(inputs: PydanticModel, output_model: Type[PydanticModel]) → PydanticModel`
* `predict_sync(inputs: JSON, output_model: Type[PydanticModel]) → PydanticModel`
* `predict_sync(inputs: JSON) → JSON`

### *class* `truss_chains.RemoteErrorDetail`

Bases: `pydantic.BaseModel`

When a remote chainlet raises an exception, this pydantic model contains
information about the error and stack trace and is included in JSON form in the
error response.

**Parameters:**

| Name                    | Type                |
| ----------------------- | ------------------- |
| `exception_cls_name`    | *str*               |
| `exception_module_name` | *str\|None*         |
| `exception_message`     | *str*               |
| `user_stack_trace`      | *list\[StackFrame]* |

#### *method* format()

Format the error for printing, similar to how Python formats exceptions
with stack traces.

* **Returns:**
  str

### *class* `truss_chains.GenericRemoteException`

Bases: `Exception`

Raised when calling a remote chainlet results in an error and it is not possible
to re-raise the same exception that was raise remotely in the caller.


# Training SDK
Source: https://docs.baseten.co/reference/sdk/training

Configure and manage training jobs with Baseten's training SDK.

## Installation

The training SDK is included with Truss:

<Tabs>
  <Tab title="uv (recommended)">
    [uv](https://docs.astral.sh/uv/) is a fast Python package manager:

    ```sh theme={"system"}
    uv pip install truss
    ```
  </Tab>

  <Tab title="pip (macOS/Linux)">
    ```sh theme={"system"}
    pip install --upgrade truss
    ```
  </Tab>

  <Tab title="pip (Windows)">
    ```sh theme={"system"}
    pip install --upgrade truss
    ```
  </Tab>
</Tabs>

Import classes from `truss_train`:

```python theme={"system"}
from truss_train import definitions
```

***

## Programmatic job submission

### push

Submits a training job programmatically from Python code. Use this when you need to:

* Build an API endpoint that receives training requests.
* Dynamically configure training jobs based on user input.
* Integrate training into your application workflow.

<Note>
  Before using `push()`, authenticate with `truss login` or ensure your Baseten API key is configured.
  See [CLI authentication](/reference/cli/truss/login).
</Note>

```python theme={"system"}
from truss_train.public_api import push

def push(
    config: Path,            # Path to config.py defining the training project
    remote: str = "baseten"  # Remote provider (defaults to "baseten")
) -> dict
```

The function returns a dictionary containing the created training project and job:

```python theme={"system"}
{
    "training_project": TrainingProject,
    "training_job": TrainingJob,
}
```

**Example:**

To submit a training job programmatically, create a `config.py` file and call `push`:

```python theme={"system"}
from pathlib import Path
from truss_train.public_api import push

result = push(config=Path("./training/config.py"))

print(f"Project ID: {result['training_project']['id']}")
print(f"Job ID: {result['training_job']['id']}")
```

For dynamic job configuration, write runtime parameters to a file before calling `push`:

```python theme={"system"}
import json
import shutil
import tempfile
from pathlib import Path

from truss_train.public_api import push


def submit_training_job(dataset_id: str, model_id: str) -> dict:
    """Submit a training job with dynamic configuration."""
    template_dir = Path("./training_template")

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)

        # Copy training template
        shutil.copytree(template_dir, tmp_path, dirs_exist_ok=True)

        # Write runtime configuration
        runtime_config = {
            "dataset_id": dataset_id,
            "model_id": model_id,
        }
        (tmp_path / "runtime_config.json").write_text(
            json.dumps(runtime_config, indent=2)
        )

        # Submit the job
        return push(config=tmp_path / "config.py")


result = submit_training_job(
    dataset_id="HuggingFaceH4/Multilingual-Thinking",
    model_id="meta-llama/Llama-3.1-8B",
)
```

Your `config.py` can read the runtime configuration at import time:

```python theme={"system"}
import json
from pathlib import Path

from truss.base import truss_config
from truss_train import definitions

# Read dynamic configuration
config_path = Path(__file__).parent / "runtime_config.json"
runtime_config = json.loads(config_path.read_text())

training_runtime = definitions.Runtime(
    start_commands=["python train.py"],
    environment_variables={
        "MODEL_ID": runtime_config["model_id"],
        "DATASET_ID": runtime_config["dataset_id"],
        "HF_TOKEN": definitions.SecretReference(name="hf_access_token"),
    },
    checkpointing_config=definitions.CheckpointingConfig(enabled=True),
)

training_compute = definitions.Compute(
    accelerator=truss_config.AcceleratorSpec(
        accelerator=truss_config.Accelerator.H100,
        count=2,
    ),
)

training_job = definitions.TrainingJob(
    image=definitions.Image(base_image="pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime"),
    compute=training_compute,
    runtime=training_runtime,
)

training_project = definitions.TrainingProject(
    name=runtime_config.get("project_name", "dynamic-training"),
    job=training_job,
)
```

**After submitting:**

Once a job is submitted, use the Training API to monitor progress:

* [Get job status](/reference/training-api/get-training-job).
* [Get job logs](/reference/training-api/get-training-job-logs).
* [Get job metrics](/reference/training-api/get-training-job-metrics).
* [List checkpoints](/reference/training-api/get-training-job-checkpoints).

For a complete working example, see the [programmatic training API recipe](https://github.com/basetenlabs/ml-cookbook/tree/main/recipes/programmatic-training-api).

***

## TrainingProject

Organizes training jobs and provides project-level configuration.

```python theme={"system"}
class TrainingProject:
    name: str                        # Project name (required)
    job: TrainingJob                 # Training job configuration (required)
    team_name: Optional[str] = None  # Team that owns this project
```

**Example:**

```python theme={"system"}
from truss_train import definitions

project = definitions.TrainingProject(
    name="llm-fine-tuning",
    job=training_job,
    team_name="my-team"  # Optional
)
```

## TrainingJob

Defines a complete training job configuration.

```python theme={"system"}
class TrainingJob:
    image: Image                     # Container image configuration (required)
    compute: Compute = Compute()     # Compute resource configuration
    runtime: Runtime = Runtime()     # Runtime environment configuration
    name: Optional[str] = None       # Job name
```

**Example:**

```python theme={"system"}
from truss_train import definitions
from truss.base import truss_config

training_job = definitions.TrainingJob(
    name="fine-tune-v1",
    image=definitions.Image(base_image="pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime"),
    compute=definitions.Compute(
        accelerator=truss_config.AcceleratorSpec(
            accelerator=truss_config.Accelerator.H100,
            count=4
        )
    ),
    runtime=definitions.Runtime(
        start_commands=["chmod +x ./run.sh && ./run.sh"],
        checkpointing_config=definitions.CheckpointingConfig(enabled=True),
        cache_config=definitions.CacheConfig(enabled=True),
    )
)
```

## Image

Specifies the container image for the training environment.

```python theme={"system"}
class Image:
    base_image: str                          # Docker image to use (required)
    docker_auth: Optional[DockerAuth] = None # Authentication for private images
```

**Example:**

```python theme={"system"}
image = definitions.Image(
    base_image="pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime"
)
```

### DockerAuth

Configures authentication for private Docker registries. Store secrets in your [Baseten workspace](/organization/secrets).

```python theme={"system"}
class DockerAuth:
    auth_method: truss_config.DockerAuthType                                   # Authentication method
    registry: str                                                              # Docker registry URL
    aws_iam_docker_auth: Optional[AWSIAMDockerAuth] = None                     # AWS ECR auth
    gcp_service_account_json_docker_auth: Optional[GCPServiceAccountJSONDockerAuth] = None  # GCP auth
```

#### AWSIAMDockerAuth

Authenticates with AWS ECR using IAM credentials.

```python theme={"system"}
class AWSIAMDockerAuth:
    access_key_secret_ref: SecretReference          # AWS access key ID
    secret_access_key_secret_ref: SecretReference   # AWS secret access key
```

**Example:**

```python theme={"system"}
from truss.base import truss_config

image = definitions.Image(
    base_image="123456789.dkr.ecr.us-east-1.amazonaws.com/my-image:latest",
    docker_auth=definitions.DockerAuth(
        auth_method=truss_config.DockerAuthType.AWS_IAM,
        registry="123456789.dkr.ecr.us-east-1.amazonaws.com",
        aws_iam_docker_auth=definitions.AWSIAMDockerAuth(
            access_key_secret_ref=definitions.SecretReference(name="aws_access_key"),
            secret_access_key_secret_ref=definitions.SecretReference(name="aws_secret_key")
        )
    )
)
```

#### GCPServiceAccountJSONDockerAuth

Authenticates with Google Container Registry using service account JSON.

```python theme={"system"}
class GCPServiceAccountJSONDockerAuth:
    service_account_json_secret_ref: SecretReference  # GCP service account JSON
```

**Example:**

```python theme={"system"}
from truss.base import truss_config

image = definitions.Image(
    base_image="gcr.io/my-project/my-image:latest",
    docker_auth=definitions.DockerAuth(
        auth_method=truss_config.DockerAuthType.GCP_SERVICE_ACCOUNT_JSON,
        registry="gcr.io",
        gcp_service_account_json_docker_auth=definitions.GCPServiceAccountJSONDockerAuth(
            service_account_json_secret_ref=definitions.SecretReference(name="gcp_service_account_json")
        )
    )
)
```

## Compute

Specifies compute resources for training jobs.

```python theme={"system"}
class Compute:
    node_count: int = 1                              # Number of nodes for distributed training
    cpu_count: int = 1                               # Number of CPU cores
    memory: str = "2Gi"                              # Memory allocation
    accelerator: Optional[AcceleratorSpec] = None    # GPU configuration
```

**Example:**

```python theme={"system"}
from truss.base import truss_config

compute = definitions.Compute(
    node_count=2,
    cpu_count=8,
    memory="64Gi",
    accelerator=truss_config.AcceleratorSpec(
        accelerator=truss_config.Accelerator.H100,
        count=4
    )
)
```

### AcceleratorSpec

Configures GPU resources.

```python theme={"system"}
class AcceleratorSpec:
    accelerator: Optional[Accelerator] = None  # GPU type
    count: int = 1                             # Number of GPUs
```

### Accelerator

Supported GPU types for training jobs.

| Value       | Description        |
| ----------- | ------------------ |
| `T4`        | NVIDIA T4          |
| `L4`        | NVIDIA L4          |
| `A10G`      | NVIDIA A10G        |
| `V100`      | NVIDIA V100        |
| `A100`      | NVIDIA A100 (80GB) |
| `A100_40GB` | NVIDIA A100 (40GB) |
| `H100`      | NVIDIA H100 (80GB) |
| `H100_40GB` | NVIDIA H100 (40GB) |
| `H200`      | NVIDIA H200        |
| `B200`      | NVIDIA B200        |

## Runtime

Defines the runtime environment for training jobs.

```python theme={"system"}
class Runtime:
    start_commands: List[str] = []                                       # Commands to run at job start
    environment_variables: Dict[str, Union[str, SecretReference]] = {}   # Environment variables
    checkpointing_config: CheckpointingConfig = CheckpointingConfig()    # Checkpointing settings
    cache_config: Optional[CacheConfig] = None                           # Cache settings
    load_checkpoint_config: Optional[LoadCheckpointConfig] = None        # Load checkpoints from previous jobs
```

<Note>
  The `enable_cache` field is deprecated. Use `cache_config` with `enabled=True` instead.
</Note>

**Example:**

```python theme={"system"}
runtime = definitions.Runtime(
    start_commands=["chmod +x ./run.sh && ./run.sh"],
    environment_variables={
        "BATCH_SIZE": "32",
        "WANDB_API_KEY": definitions.SecretReference(name="wandb_api_key"),
        "HF_TOKEN": definitions.SecretReference(name="hf_access_token"),
    },
    checkpointing_config=definitions.CheckpointingConfig(enabled=True),
    cache_config=definitions.CacheConfig(enabled=True),
)
```

### SecretReference

Securely references secrets stored in your [Baseten workspace](/organization/secrets).

```python theme={"system"}
class SecretReference:
    name: str  # Name of the secret in your workspace
```

**Example:**

```python theme={"system"}
secret_ref = definitions.SecretReference(name="wandb_api_key")
```

### CheckpointingConfig

Configures model checkpointing behavior during training. When enabled, Baseten exports `$BT_CHECKPOINT_DIR` in your job's environment. Save your model to this directory to preserve checkpoints for deployment.

```python theme={"system"}
class CheckpointingConfig:
    enabled: bool = False                      # Enable checkpointing
    checkpoint_path: Optional[str] = None      # Custom checkpoint directory path
    volume_size_gib: Optional[int] = None      # Custom checkpoint volume size
```

**Example:**

```python theme={"system"}
checkpointing = definitions.CheckpointingConfig(
    enabled=True,
    volume_size_gib=500  # 500 GiB checkpoint storage
)
```

### CacheConfig

Configures caching for training jobs. The cache persists data between jobs within a project or team.

```python theme={"system"}
class CacheConfig:
    enabled: bool = False                 # Enable caching
    enable_legacy_hf_mount: bool = False  # Enable legacy Hugging Face cache mount
    require_cache_affinity: bool = True   # Prefer nodes with cached data
    mount_base_path: str = "/root/.cache" # Base path for cache mounts
```

When enabled, Baseten provides two cache directories.

| Environment Variable    | Description                                |
| ----------------------- | ------------------------------------------ |
| `$BT_PROJECT_CACHE_DIR` | Shared across jobs within the same project |
| `$BT_TEAM_CACHE_DIR`    | Shared across jobs within the same team    |

**Example:**

```python theme={"system"}
cache = definitions.CacheConfig(
    enabled=True,
    require_cache_affinity=True
)
```

### LoadCheckpointConfig

Configures loading checkpoints from previous training jobs to resume training.

```python theme={"system"}
class LoadCheckpointConfig:
    enabled: bool = False                    # Enable checkpoint loading
    checkpoints: List[BasetenCheckpoint]     # Checkpoints to load
    download_folder: str = "/tmp/loaded_checkpoints"  # Where to download checkpoints
```

**Example:**

```python theme={"system"}
load_config = definitions.LoadCheckpointConfig(
    enabled=True,
    download_folder="/tmp/loaded_checkpoints",
    checkpoints=[
        definitions.BasetenCheckpoint.from_latest_checkpoint(project_name="my-project"),
        definitions.BasetenCheckpoint.from_named_checkpoint(
            checkpoint_name="checkpoint-24",
            job_id="abc123"
        )
    ]
)
```

### BasetenCheckpoint

Factory class for referencing checkpoints from previous training jobs.

#### from\_latest\_checkpoint

Load the most recent checkpoint from a project or job.

```python theme={"system"}
BasetenCheckpoint.from_latest_checkpoint(
    project_name: Optional[str] = None,  # Project name
    job_id: Optional[str] = None         # Job ID
)
```

At least one of `project_name` or `job_id` is required.

#### from\_named\_checkpoint

Load a specific checkpoint by name.

```python theme={"system"}
BasetenCheckpoint.from_named_checkpoint(
    checkpoint_name: str,  # Checkpoint name (required)
    job_id: str            # Job ID (required)
)
```

**Example:**

```python theme={"system"}
# Load most recent checkpoint from a project
latest = definitions.BasetenCheckpoint.from_latest_checkpoint(
    project_name="my-fine-tuning-project"
)

# Load specific checkpoint
specific = definitions.BasetenCheckpoint.from_named_checkpoint(
    checkpoint_name="checkpoint-100",
    job_id="abc123"
)

# Use in LoadCheckpointConfig
runtime = definitions.Runtime(
    start_commands=["python train.py"],
    load_checkpoint_config=definitions.LoadCheckpointConfig(
        enabled=True,
        checkpoints=[latest, specific]
    )
)
```

## Environment variables

Baseten automatically provides environment variables in your training job's environment.

### Standard variables

| Variable                   | Description                     | Example                         |
| -------------------------- | ------------------------------- | ------------------------------- |
| `BT_TRAINING_JOB_ID`       | Training job ID                 | `"gvpql31"`                     |
| `BT_TRAINING_PROJECT_ID`   | Training project ID             | `"aghi527"`                     |
| `BT_TRAINING_JOB_NAME`     | Training job name               | `"gpt-oss-20b-lora"`            |
| `BT_TRAINING_PROJECT_NAME` | Training project name           | `"gpt-oss-finetunes"`           |
| `BT_NUM_GPUS`              | Number of GPUs per node         | `"4"`                           |
| `BT_CHECKPOINT_DIR`        | Checkpoint save directory       | `"/mnt/ckpts"`                  |
| `BT_LOAD_CHECKPOINT_DIR`   | Loaded checkpoints directory    | `"/tmp/loaded_checkpoints"`     |
| `BT_PROJECT_CACHE_DIR`     | Project-level cache directory   | `"/root/.cache/user_artifacts"` |
| `BT_TEAM_CACHE_DIR`        | Team-level cache directory      | `"/root/.cache/team_artifacts"` |
| `BT_RW_CACHE_DIR`          | Base read-write cache directory | `"/root/.cache"`                |
| `BT_RETRY_COUNT`           | Job retry attempt count         | `"0"`                           |

### Multi-node variables

For distributed training across multiple nodes:

| Variable         | Description                   | Example      |
| ---------------- | ----------------------------- | ------------ |
| `BT_GROUP_SIZE`  | Number of nodes in deployment | `"2"`        |
| `BT_LEADER_ADDR` | Leader node address           | `"10.0.0.1"` |
| `BT_NODE_RANK`   | Node rank (0 for leader)      | `"0"`        |

Any standard port number (e.g., `29500`) works for distributed training.

***

## Deploy checkpoints

Deploy trained model checkpoints to Baseten's inference platform.

### Deploy with CLI wizard

Deploy checkpoints interactively with the CLI wizard:

```bash theme={"system"}
truss train deploy_checkpoints --job-id <job_id>
```

The wizard guides you through selecting checkpoints and configuring deployment. Baseten automatically recognizes checkpoints for full fine-tunes and LoRAs for LLMs and Whisper models.

<Note>
  FSDP checkpoints aren't supported by `deploy_checkpoints` and must be manually configured in the Truss config.
</Note>

<Note>
  For optimized inference with TensorRT-LLM, see [Deploy checkpoints with Engine Builder](/engines/performance-concepts/deployment-from-training-and-s3).
</Note>

### Deploy with static configuration

Create a Python config file for repeatable deployments:

```bash theme={"system"}
truss train deploy_checkpoints --config <path_to_config_file>
```

## DeployCheckpointsConfig

Specifies configuration for deploying trained model checkpoints.

```python theme={"system"}
class DeployCheckpointsConfig:
    checkpoint_details: Optional[CheckpointList] = None          # Checkpoints to deploy
    model_name: Optional[str] = None                             # Name for the deployed model
    runtime: Optional[DeployCheckpointsRuntime] = None           # Runtime configuration
    compute: Optional[Compute] = None                            # Compute resources
```

**Example:**

```python theme={"system"}
from truss_train import definitions
from truss.base import truss_config

deploy_config = definitions.DeployCheckpointsConfig(
    model_name="fine-tuned-llm",
    checkpoint_details=definitions.CheckpointList(
        base_model_id="meta-llama/Llama-3.1-8B-Instruct",
        checkpoints=[
            definitions.LoRACheckpoint(
                training_job_id="gvpql31",
                checkpoint_name="checkpoint-100",
                lora_details=definitions.LoRADetails(rank=16)
            )
        ]
    ),
    compute=definitions.Compute(
        accelerator=truss_config.AcceleratorSpec(
            accelerator=truss_config.Accelerator.H100,
            count=1
        )
    )
)
```

### DeployCheckpointsRuntime

Configures the runtime environment for deployed checkpoints.

```python theme={"system"}
class DeployCheckpointsRuntime:
    environment_variables: Dict[str, Union[str, SecretReference]] = {}
```

### CheckpointList

Manages a collection of checkpoints for deployment.

```python theme={"system"}
class CheckpointList:
    download_folder: str = "/tmp/training_checkpoints"  # Download location
    base_model_id: Optional[str] = None                 # Base model identifier
    checkpoints: List[Checkpoint] = []                  # List of checkpoints
```

### Checkpoint types

Baseten supports two checkpoint types based on model weight format.

#### FullCheckpoint

For full model fine-tunes.

```python theme={"system"}
class FullCheckpoint:
    training_job_id: str                                # Training job ID (required)
    checkpoint_name: str                                # Checkpoint name (required)
    model_weight_format: ModelWeightsFormat = "full"    # Auto-set
```

#### LoRACheckpoint

For LoRA adapter weights.

```python theme={"system"}
class LoRACheckpoint:
    training_job_id: str                                # Training job ID (required)
    checkpoint_name: str                                # Checkpoint name (required)
    model_weight_format: ModelWeightsFormat = "lora"    # Auto-set
    lora_details: LoRADetails = LoRADetails()           # LoRA configuration
```

### LoRADetails

Configuration for LoRA adapters.

```python theme={"system"}
class LoRADetails:
    rank: int = 16  # LoRA rank
```

**Valid ranks:** 8, 16, 32, 64, 128, 256, 320, 512.

### ModelWeightsFormat

Enum for checkpoint weight formats.

| Value  | Description          |
| ------ | -------------------- |
| `lora` | LoRA adapter weights |
| `full` | Full model weights   |


# Truss SDK Reference
Source: https://docs.baseten.co/reference/sdk/truss

Python SDK for deploying and managing models with Truss.

## Authentication

### `truss.login(api_key: str) → None`

Authenticates with Baseten using an API key.

**Parameters:**

| Name      | Type  | Description      |
| --------- | ----- | ---------------- |
| `api_key` | *str* | Baseten API Key. |

***

## Deploying a Model

### `truss.push(target_directory: str, **kwargs) → ModelDeployment`

Deploys a **Truss** model to Baseten.

**Parameters:**

| Name                                      | Type             | Description                                                                                                              |
| ----------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `target_directory`                        | *str*            | Path to the Truss directory to push.                                                                                     |
| `remote`                                  | *Optional\[str]* | Name of the remote in `.trussrc` to push to.                                                                             |
| `model_name`                              | *Optional\[str]* | Override the model name in `config.yaml`.                                                                                |
| `publish`                                 | *bool*           | Deploy as **published**. If no production deployment exists, promote it to production.                                   |
| `promote`                                 | *bool*           | Deploy as **published** and promote to production, even if a production deployment exists.                               |
| `preserve_previous_production_deployment` | *bool*           | Preserve the previous production deployment's **autoscaling settings** (only with `promote`).                            |
| `trusted`                                 | *bool*           | Grants **access to secrets** on the remote host.                                                                         |
| `deployment_name`                         | *Optional\[str]* | Custom deployment name (must contain only alphanumeric, `.`, `-`, or `_` characters). (Requires `publish` or `promote`.) |

**Returns:** [ModelDeployment](#class-truss-api-definitions-modeldeployment) – An object representing the deployed model.

***

## Model Deployment Object

### *class* `truss.api.definitions.ModelDeployment`

Represents a deployed model (returned by `truss.push()`).

**Attributes**

`model_id` → `str`: Unique ID of the deployed model.
`model_deployment_id` → `str`:Unique ID of the model deployment.

**Methods**

`wait_for_active()` → bool
Waits for the deployment to become **active**.

**Returns**: `True` when deployment is ready.
**Raises**: An error if deployment fails.


# Create training project
Source: https://docs.baseten.co/reference/training-api/create-training-project

post /v1/training_projects
Upserts a training project with the specified metadata.



# Download training job source code
Source: https://docs.baseten.co/reference/training-api/download-training-job

get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/download
Get the uploaded training job as a S3 Artifact



# Get training job
Source: https://docs.baseten.co/reference/training-api/get-training-job

get /v1/training_projects/{training_project_id}/jobs/{training_job_id}
Get the details of an existing training job.



# Get training job checkpoint files
Source: https://docs.baseten.co/reference/training-api/get-training-job-checkpoint-files

get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files
Get presigned URLs for all checkpoint files for a training job.



# List training job checkpoints
Source: https://docs.baseten.co/reference/training-api/get-training-job-checkpoints

get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoints
Get the checkpoints for a training job.



# Get training job logs
Source: https://docs.baseten.co/reference/training-api/get-training-job-logs

post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs
Get the logs for a training job with the provided filters.



# Get training job metrics
Source: https://docs.baseten.co/reference/training-api/get-training-job-metrics

post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics
Get the metrics for a training job.



# List training projects
Source: https://docs.baseten.co/reference/training-api/get-training-projects

get /v1/training_projects
List all training projects for the organization.



# List training jobs
Source: https://docs.baseten.co/reference/training-api/list-training-jobs

get /v1/training_projects/{training_project_id}/jobs
List all training jobs for the training project.



# Overview
Source: https://docs.baseten.co/reference/training-api/overview

The Training API enables programmatic management of Baseten Training resources.

The Training API allows you to manage training projects, jobs, and related resources through a RESTful interface. This API is used to:

* Monitor training job metrics and logs
* Manage training jobs
* Manage checkpoints and artifacts

## Authentication

All Training API requests require authentication using an API key:

```bash theme={"system"}
Authorization: Api-Key YOUR_API_KEY
```

## Base URL

All Training API endpoints are relative to:

```
https://api.baseten.co/v1
```

## Available Endpoints

### Training Projects

| Method | Endpoint                                                                | Description                   |
| ------ | ----------------------------------------------------------------------- | ----------------------------- |
| `GET`  | [`/training_projects`](/reference/training-api/get-training-projects)   | List all training projects    |
| `POST` | [`/training_projects`](/reference/training-api/create-training-project) | Create a new training project |

### Training Jobs

**Note: Creating Training Jobs via REST API is not supported at this time.**

The following endpoints have the relative base path: `/training_projects/{training_project_id}/jobs`

| Method | Endpoint                                                                                              | Description                       |
| ------ | ----------------------------------------------------------------------------------------------------- | --------------------------------- |
| `GET`  | [`.../`](/reference/training-api/list-training-jobs)                                                  | List all jobs in a project        |
| `GET`  | [`.../{training_job_id}`](/reference/training-api/get-training-job)                                   | Get a specific training job       |
| `POST` | [`.../{training_job_id}/stop`](/reference/training-api/stop-training-job)                             | Stop a training job               |
| `POST` | [`.../{training_job_id}/recreate`](/reference/training-api/recreate-training-job)                     | Recreate a training job           |
| `POST` | [`.../{training_job_id}/logs`](/reference/training-api/get-training-job-logs)                         | Get training job logs             |
| `POST` | [`.../{training_job_id}/metrics`](/reference/training-api/get-training-job-metrics)                   | Get training job metrics          |
| `GET`  | [`.../{training_job_id}/checkpoints`](/reference/training-api/get-training-job-checkpoints)           | List job checkpoints              |
| `GET`  | [`.../{training_job_id}/checkpoint_files`](/reference/training-api/get-training-job-checkpoint-files) | Get training job checkpoint files |
| `GET`  | [`.../{training_job_id}/download`](/reference/training-api/download-training-job)                     | Download training job artifacts   |

Search endpoint:

| Method | Endpoint                                                                | Description                     |
| ------ | ----------------------------------------------------------------------- | ------------------------------- |
| `POST` | [`/training_jobs/search`](/reference/training-api/search-training-jobs) | Search across all training jobs |


# Recreate training job
Source: https://docs.baseten.co/reference/training-api/recreate-training-job

post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/recreate
Create a new training job with the same configuration as an existing training job.



# Search training jobs
Source: https://docs.baseten.co/reference/training-api/search-training-jobs

post /v1/training_jobs/search
Search training jobs for the organization.



# Stop training job
Source: https://docs.baseten.co/reference/training-api/stop-training-job

post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/stop
Stops a training job.



# Truss configuration
Source: https://docs.baseten.co/reference/truss-configuration

Set your model resources, dependencies, and more

The `config.yaml` file defines how your model runs on Baseten: its dependencies,
compute resources, secrets, and runtime behavior. You specify what your model
needs; Baseten handles the infrastructure.

Every Truss includes a `config.yaml` in its root directory. Configuration is
optional, every value has a sensible default.

Common configuration tasks include:

* [Allocate GPU and memory](#resources): compute resources for your instance.
* [Declare environment variables](#environment-variables): environment variables for your model.
* [Configure concurrency](#runtime): parallel request handling.
* [Use a custom Docker image](#base-image): deploy pre-built inference servers.

<Accordion title="YAML syntax">
  If you're new to YAML, here's a quick primer.
  The default config uses `[]` for empty lists and `{}` for empty dictionaries.
  When adding values, the syntax changes to indented lines:

  ```yaml theme={"system"}
  # Empty
  requirements: []
  secrets: {}

  # With values
  requirements:
    - torch
    - transformers
  secrets:
    hf_access_token: null
  ```
</Accordion>

## Example

The following example shows a config file for a GPU-accelerated text generation model:

```yaml config.yaml theme={"system"}
model_name: my-llm
description: A text generation model.
requirements:
  - torch
  - transformers
  - accelerate
resources:
  cpu: "4"
  memory: 16Gi
  accelerator: L4
secrets:
  hf_access_token: null
```

For more examples, see the
[truss-examples](https://github.com/basetenlabs/truss-examples) repository.

## Reference

<Snippet />


# Baseten platform status
Source: https://docs.baseten.co/status/status

Current operational status of Baseten's services.

This page automatically refreshes with real-time data from our status monitoring system.

<div>
  <div>
    <div>
      <Icon icon="circle-check" />
    </div>

    <div>All systems are operational.</div>
  </div>

  <CardGroup>
    <Card title="Model Inference" icon="circle-check" href="https://status.baseten.co/">
      <div>Normal</div>
    </Card>

    <Card title="Management API" icon="circle-check" href="https://status.baseten.co/">
      <div>Normal</div>
    </Card>

    <Card title="Web Application" icon="circle-check" href="https://status.baseten.co/">
      <div>Normal</div>
    </Card>
  </CardGroup>
</div>

<div>
  <span>Last updated: Loading...</span>
</div>


# Basics
Source: https://docs.baseten.co/training/concepts/basics

Learn how to get up and running on Baseten Training

This page covers the essential building blocks of Baseten Training. These are
the core concepts you'll need to understand to effectively organize and execute
your training workflows.

## How Baseten Training works

Baseten Training jobs can be launched from any terminal. Training jobs are created from within a directory, and when created, that directory is packaged up and can be pushed up to Baseten.

This allows you to define your Baseten training config, scripts, code, and any other dependencies within the folder.

Within the folder, we require you to include a Baseten training config file such as `config.py`. The `config.py` includes a list of `run_commands`, which can be anything from running a Python file (`python train.py`) to a bash script (`chmod +x run.sh && ./run.sh`).

<Tip>
  If you're looking to upload more than 1GB of files, we strongly suggest
  uploading your data to an object store and including a download command before
  running your training code. To avoid duplicate downloads, check out our
  documentation on the [cache](/training/concepts/cache).
</Tip>

## Setting up your workspace

If you'd like to start from one of our existing recipes, you can check out one of the following examples:

**Simple CPU job with raw PyTorch:**

```bash theme={"system"}
truss train init --examples mnist-pytorch
```

**More complex example that trains GPT-OSS-20b:**

```bash theme={"system"}
truss train init --examples oss-gpt-20b-axolotl
```

Your `config.py` contains all infrastructure configuration for your job, which we will cover below.

Your `run.sh` is invoked by the command that runs when the job first begins. Here you can install any Python dependencies not already included in your Docker image, and begin the execution of your code either by calling a Python file with your training code or a launch command.

## Organizing your work with `TrainingProject`s

A `TrainingProject` is a lightweight organization tool to help you group different `TrainingJob`s together.

While there a few technical details to consider, your team can use `TrainingProject`s to facilitate collaboration and organization.

## Running a `TrainingJob`

Once you have a `TrainingProject`, the actual work of training a model happens within a **`TrainingJob`**. Each `TrainingJob` represents a single, complete execution of your training script with a specific configuration.

* **What it is:** A `TrainingJob` is the fundamental unit of execution. It bundles together:
  * Your training code.
  * A base `image`.
  * The `compute` resources needed to run the job.
  * The `runtime` configurations like startup commands and environment variables.
* **Why use it:** Each job is a self-contained, reproducible experiment. If you want to try training your model with a different learning rate, more GPUs, or a slightly modified script, you can create new `TrainingJob`s while knowing that previous ones have been persisted on Baseten.
* **Lifecycle:** A job goes through various stages, from being created (`TRAINING_JOB_CREATED`), to resources being set up (`TRAINING_JOB_DEPLOYING`), to actively running your script (`TRAINING_JOB_RUNNING`), and finally to a terminal state like `TRAINING_JOB_COMPLETED`. More details on the job lifecycle can be found on the [Lifecycle](/training/lifecycle) page.

## Compute resources

The `Compute` configuration defines the computational resources your training job will use. This includes:

* **GPU specifications** - Choose from various GPU types based on your model's requirements
* **CPU and memory** - Configure the amount of CPU and RAM allocated to your job
* **Node count** - For single-node or multi-node training setups

Baseten Training supports H100, H200, and A10G GPUs. Choose your GPU type based
on your model's memory requirements and performance needs.

## Base images

Baseten provides pre-configured base images that include common ML frameworks and dependencies. These images are optimized for training workloads and include:

* Popular ML frameworks (PyTorch, VERL, Megatron, Axolotl, etc.)
* GPU drivers and CUDA support
* Common data science libraries

You can also use [custom or private images](/development/model/private-registries) if you have specific requirements.

## Securely integrate with external services with `SecretReference`

Successfully training a model often requires many tools and services. Baseten provides **`SecretReference`** for secure handling of secrets.

* **How to use it:** Store your secret (e.g., an API key for Weights & Biases) in your Baseten workspace with a specific name. In your job's configuration (e.g., environment variables), you refer to this secret by its name using `SecretReference`. The actual secret value is never exposed in your code.
* **How it works:** Baseten injects the secret value at runtime under the environment variable name that you specify.

```python theme={"system"}
from truss_train import definitions

runtime = definitions.Runtime(
    # ... other runtime options
    environment_variables={
        "HF_TOKEN": definitions.SecretReference(name="hf_access_token"),
    },
)
```

## Running inference on trained models

The journey from training to a usable model in Baseten typically follows this path:

1. A `TrainingJob` with checkpointing enabled, produces one or more model artifacts.
2. You run `truss train deploy_checkpoint` to deploy a model from your most recent training job. You can read more about this at [Serving Trained Models](/training/deployment).
3. Once deployed, your model will be available for inference via API. See more at [Calling Your Model](/inference/calling-your-model).

## Next steps: advanced topics

Now that you understand the basics of Baseten Training, explore these advanced topics to optimize your training workflows:

* **[Cache](/training/concepts/cache)** - Speed up your training iterations by persisting data between jobs and avoiding expensive downloads
* **[Checkpointing](/training/concepts/checkpointing)** - Manage model checkpoints seamlessly and avoid disk errors during training
* **[Multinode Training](/training/concepts/multinode)** - Scale your training across multiple nodes with high-speed infiniband networking


# Cache
Source: https://docs.baseten.co/training/concepts/cache

Learn how to use the training cache to speed up your training iterations by persisting data between jobs.

The training cache enables you to persist data between training jobs. This can significantly improve iteration speed by skipping expensive downloads and data transformations.

## How to Use the Training Cache

Set the cache configuration in your `Runtime`:

```python theme={"system"}
from truss_train import definitions

training_runtime = definitions.Runtime(
    # ... other configuration options
    cache_config=definitions.CacheConfig(enabled=True)
)
```

## Cache Directory

By default, the cache will be mounted in two locations

* `/root/.cache/user_artifacts`, which can be accessed via the [`$BT_PROJECT_CACHE_DIR`](/reference/sdk/training#baseten-provided-environment-variables) environment variable. This cache is shared by all jobs in a project.
* `/root/.cache/team_artifacts`, which can be accessed via the [`$BT_TEAM_CACHE_DIR`](/reference/sdk/training#baseten-provided-environment-variables) environment variable. This cache is shared by all jobs for a team.

## Hugging Face Cache Mount

You can mount your cache to the Hugging Face cache directory by setting `HF_HOME` to one of the provided mount points plus `/huggingface`. For example, you can set `HF_HOME=$BT_PROJECT_CACHE_DIR/huggingface` to use the project cache directory.

However, there are considerable technical pitfalls when trying to read from the cache with multiple processes, as Huggingface doesn't work well with distributed filesystems. To help enable this use case, ensure your dataset processors or process count is set to 1 to minimize the number of concurrent readers.

## Seeding Your Data and Models

For multi-gpu training, you should ensure that your data is seeded before running multi-process training jobs. You can do this by separating out a data loading script and a training script.
For a 400 GB HF Dataset, you can expect to save *nearly an hour* of compute time for each job - data download and preparation have been done already!

## Cache Management

You can inspect the contents of the cache through CLI with `truss train cache summarize <project_name or project_id>`. This visibility into what's in the cache can help you verify your code is working as expected, and additionally manage files and artifacts you no longer need.

<Warning>
  When you delete a project, all data in the project's training cache (`$BT_PROJECT_CACHE_DIR`) is permanently deleted with no archival or recovery option. See [Management](/training/management) for details.
</Warning>


# Checkpointing
Source: https://docs.baseten.co/training/concepts/checkpointing

Learn how to use Baseten's checkpointing feature to manage model checkpoints and avoid disk errors during training.

With checkpointing enabled, you can manage your model checkpoints seamlessly and avoid common training issues.

## Benefits of Checkpointing

* **Avoid catastrophic out of disk errors**: We mount additional storage at the checkpointing directory to help avoid out of disk errors during your training run.
* **Maximize GPU utilization**: When checkpointing is enabled, any data written to the checkpointing directory will be uploaded to the cloud by a separate process, allowing you to maximize GPU time spent training.
* **Seamless checkpoint management**: Checkpoints are automatically uploaded to cloud storage for easy access and management.

## Enabling Checkpointing

To enable checkpointing, add a `CheckpointingConfig` to the `Runtime` and set `enabled` to `True`:

```python theme={"system"}
from truss_train import definitions

training_runtime = definitions.Runtime(
    # ... other configuration options
    checkpointing_config=definitions.CheckpointingConfig(enabled=True)
)
```

## Using the Checkpoint Directory

Baseten will automatically export the [`$BT_CHECKPOINT_DIR`](/reference/sdk/training#baseten-provided-environment-variables) environment variable in your job's environment.

<Danger>
  **Write your checkpoints to the `$BT_CHECKPOINT_DIR` directory so Baseten can automatically backup and preserve them.**
</Danger>

## Serving Checkpoints

Once your training is complete, you can serve your model checkpoints using Baseten's serving infrastructure. Learn more about [serving checkpoints](/training/deployment).

<Warning>
  When you delete a job or project, all undeployed checkpoints are permanently deleted with no archival or recovery option. Deployed checkpoints aren't affected. See [Management](/training/management) for details.
</Warning>


# Multinode Training
Source: https://docs.baseten.co/training/concepts/multinode

Learn how to configure and run multinode training jobs with Baseten Training.

Baseten Training supports multinode training via infiniband for distributed training across multiple nodes.

## Configuring Multinode Training

To deploy a multinode training job:

* Configure the `Compute` resource in your `TrainingJob` by setting the `node_count` to the number of nodes you'd like to use (e.g. 2).

```python theme={"system"}
from truss_train import definitions

compute = definitions.Compute(
    node_count=2,  # Use 2 nodes for multinode training
    # ... other compute configuration options
)
```

## Environment Variables

Make sure you've properly integrated with the [Baseten provided environment variables](/reference/sdk/training#baseten-provided-environment-variables) for distributed training.

## Network Configuration

Baseten provides high-speed infiniband networking between nodes to ensure efficient communication during distributed training. This enables:

* Fast gradient synchronization
* Efficient parameter updates
* Low-latency communication between nodes

## Checkpointing in Multinode Training

Checkpointing behavior varies across training frameworks in multinode setups. One common pattern is to use the shared cache directory that all nodes can access:

```bash theme={"system"}
# Use shared volume with job name for checkpointing
ckpt_dir="${BT_PROJECT_CACHE_DIR}/${BT_TRAINING_JOB_NAME}"
```

Then ensure you write to `ckpt_dir`. This ensures all nodes write to the same checkpoint location. For comprehensive framework-specific examples and patterns, see the [Training Cookbook](https://github.com/basetenlabs/ml-cookbook).
Keep in mind that these checkpoints will not be backed up by Baseten since they are not stored in \$BT\_CHECKPOINT\_DIR. Make sure to copy them there at some point to ensure they are preserved.

## Common Practices

When setting up multinode training:

1. **Data Loading**: Ensure your data loading is properly distributed across nodes
2. **Seeding**: Use consistent seeding across all nodes for reproducible results
3. **Monitoring**: Monitor training metrics across all nodes to ensure balanced training


# Serving your trained model
Source: https://docs.baseten.co/training/deployment

How to deploy checkpoints from Baseten Training jobs as usable models.

Baseten Training seamlessly integrates with Baseten's model deployment capabilities. Once your `TrainingJob` has produced model checkpoints, you can deploy them as fully operational model endpoints.

**This feature works with HuggingFace compatible LLMs**, allowing you to easily deploy fine-tuned language models directly from your training checkpoints with a single command.

<Note>
  For optimized inference performance with TensorRT-LLM, BEI and Baseten Inference Stack, see [Deploy checkpoints with Engine Builder](/engines/performance-concepts/deployment-from-training-and-s3).
</Note>

To leverage deploying checkpoints, first ensure you have a `TrainingJob` that's running with a `checkpointing_config` enabled.

```python theme={"system"}
runtime = definitions.Runtime(
    start_commands=[
        "/bin/sh -c './run.sh'",
    ],
    checkpointing_config=definitions.CheckpointingConfig(
        enabled=True,
    ),
)
```

In your training code or configuration, ensure that your checkpoints are being written to the checkpointing directory, which can be referenced via [`$BT_CHECKPOINT_DIR`](/reference/sdk/training#baseten-provided-environment-variables).
The contents of this directory are uploaded to Baseten's storage and made immediately available for deployment.
*(You can optionally specify a `checkpoint_path` in your `checkpointing_config` if you prefer to write to a specific directory).* The default location is "/tmp/training\_checkpoints".

To deploy your checkpoint(s) as a `Deployment`, you can:

### CLI Deployment

```bash theme={"system"}
truss train deploy_checkpoints [OPTIONS]
```

**Options:**

* `--job-id` (TEXT): Job ID to deploy checkpoints from. If not specified, deploys from the most recent training job.

This will deploy the most recent checkpoint from your training job as an inference endpoint.

### UI Deployment

You can also deploy checkpoints directly from the Baseten UI by pressing the dropdown menu on your completed training job and selecting "Deploy" on your selected checkpoint.

### Advanced CLI Deployment

You can also:

* run `truss train deploy_checkpoints [--job-id <job_id>]` and follow the setup wizard.
* define an instance of a `DeployCheckpointsConfig` class (this is helpful for small changes that aren't provided by the wizard) and run `truss train deploy_checkpoints --config <path_to_config_file>`.

<Note>
  Currently, the `deploy_checkpoints` command only supports LoRA and Full Fine Tune for Single Node LLM Training jobs.
</Note>

When `deploy_checkpoints` is run, `truss` will construct a deployment `config.yml` and store it on disk in a temporary directory. If you'd like to preserve or modify the resulting deployment config, you can copy paste it
into a permanent directory and customize it as needed.

This file defines the source of truth for the deployment and can be deployed independently via `truss push`. See [deployments](../deployment/deployments) for more details.

After successful deployment, your model will be deployed on Baseten, where you can run inference requests and evaluate performance. See [Calling Your Model](/inference/calling-your-model) for more details.

To download the files you saved to the checkpointing directory or understand the file structure, you can run `truss train get_checkpoint_urls [--job-id=<job_id>]` to get a JSON file containing presigned URLs for each training job.

The JSON file contains the following structure:

```json theme={"system"}
{
  "timestamp": "2025-06-23T13:44:16.485905+00:00",
  "job": {
    "id": "03yv1l3",
    "created_at": "2025-06-18T14:30:30.480Z",
    "current_status": "TRAINING_JOB_COMPLETED",
    "error_message": null,
    "instance_type": {
			"id": "H100:2x8x176x968",
			"name": "H100:2x8x176x968 - 2 Nodes of 8 H100 GPUs, 640 GiB VRAM, 176 vCPUs, 968 GiB RAM",
			"memory_limit_mib": 967512,
			"millicpu_limit": 176000,
			"gpu_count": 8,
			"gpu_type": "H100",
			"gpu_memory_limit_mib": 655360
		},
    "updated_at": "2025-06-18T14:30:30.510Z",
    "training_project_id": "lqz9o34",
    "training_project": {
      "id": "lqz9o34",
      "name": "checkpointing"
    }
  },
  "checkpoint_artifacts": [
    {
      "url": "https://bt-training-eqwnwwp-f815d6cd-19bf-4589-bfcb-da76cd8432c0.s3.amazonaws.com/training_projects/lqz9o34/jobs/03yv1l3/rank-0/checkpoint-24/tokenizer_config.json?AWSAccessKeyId=AKIARLZO4BEQO4Q2A5NH&Signature=0vdzJf0686wNE1d9bm4%2Bw9ik5lY%3D&Expires=1751291056",
      "relative_file_name": "checkpoint-24/tokenizer_config.json",
      "node_rank": 0
    }
    ...
  ]
}
```

**Important notes about the presigned URLs:**

* The presigned URLs expire after **7 days** from generation
* These URLs are primarily intended for **evaluation and testing purposes**, not for long-term inference deployments
* For production deployments, consider copying the checkpoint files to your Truss model directory and downloading them in the model's `load()` function

## Complex and Custom Use Cases

* Custom Model Architectures
* Weights Sharded Across Nodes (Contact Baseten for help implementing this)

Examine the structure of your files with `truss train get_checkpoint_urls --job-id=<your-training-job-id>`. If a file looks like this:

```json theme={"system"}
{
  "url": "https://bt-training-eqwnwwp-f815d6cd-19bf-4589-bfcb-da76cd8432c0.s3.amazonaws.com/training_projects/lqz9o34/jobs/03yv1l3/rank-4/checkpoint-10/weights.safetensors?AWSAccessKeyId=AKIARLZO4BEQO4Q2A5NH&Signature=0vdzJf0686wNE1d9bm4%2Bw9ik5lY%3D&Expires=1751291056",
  "relative_file_name": "checkpoint-10/weights.safetensors",
  "node_rank": 4
}
```

In your Truss configuration, add a section like this: Wildcards `*` match to an arbitrary number of chars while `?` matches to one.

```yaml theme={"system"}
training_checkpoints:
  download_folder: /tmp/training_checkpoints
  artifact_references:
    - training_job_id: <your-training-job-id>
      paths:
        - rank-*/checkpoint-10/ # Pull in all the files for checkpoint-10 across all nodes
```

When your model pod starts up, you can read the file from the path `/tmp/training_checkpoints/rank-[node-rank]/[relative_file_name]`. For the example above, the file can be read from:

```
/tmp/training_checkpoints/<your-training-job-id>/rank-4/checkpoint-10/weights.safetensors
```


# Get started
Source: https://docs.baseten.co/training/getting-started

Run your first training job and deploy it to production.

Learn to fine-tune a model on Baseten, monitor your training job, and deploy the result as an endpoint.

## Prerequisites

Before you begin, ensure you have:

* **Baseten account**: Sign up at [app.baseten.co](https://app.baseten.co/).
* **Truss**: Install Truss:

  <Tabs>
    <Tab title="uv (recommended)">
      [uv](https://docs.astral.sh/uv/) is a fast Python package manager.

      ```bash theme={"system"}
      uv venv && source .venv/bin/activate
      uv pip install truss
      ```
    </Tab>

    <Tab title="pip (macOS/Linux)">
      ```bash theme={"system"}
      python -m venv .venv && source .venv/bin/activate
      pip install --upgrade truss
      ```
    </Tab>

    <Tab title="pip (Windows)">
      ```bash theme={"system"}
      python -m venv .venv && .venv\Scripts\activate
      pip install --upgrade truss
      ```
    </Tab>
  </Tabs>

<Tip>
  You can add keys like `hf_access_token` or `wandb_api_key` in
  [Baseten Secrets](/organization/secrets) to access gated models on Hugging Face
  or track experiment metrics in Weights & Biases.
</Tip>

## Create your training project

To create a new training project, use the `truss train init` command.

```bash theme={"system"}
truss train init --examples oss-gpt-20b-axolotl
cd oss-gpt-20b-axolotl
```

Baseten provides starter templates for common frameworks like Axolotl, Unsloth, and TRL.
Browse the [ML Cookbook](https://github.com/basetenlabs/ml-cookbook) for more examples.

Skip to [Submit your training job](#submit-your-training-job) if you're using the template.

### Write your configuration file

Define your training job in a Python configuration file, typically named `config.py`.
This file specifies your [`TrainingProject`](/reference/sdk/training#trainingproject) and [`TrainingJob`](/reference/sdk/training#trainingjob). The configuration uses classes like [`Image`](/reference/sdk/training#image), [`Compute`](/reference/sdk/training#compute), [`Runtime`](/reference/sdk/training#runtime), and [`SecretReference`](/reference/sdk/training#secretreference):

```python config.py theme={"system"}
from truss_train import (
    TrainingProject,
    TrainingJob,
    Image,
    Compute,
    Runtime,
    SecretReference,
    CacheConfig,
    CheckpointingConfig,
)
from truss.base.truss_config import AcceleratorSpec

# Base image with your training dependencies (use any Docker image)
BASE_IMAGE = "pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime"

# Runtime configuration
training_runtime = Runtime(
    start_commands=[
        "chmod +x ./run.sh && ./run.sh",
    ],
    environment_variables={
        # "HF_TOKEN": SecretReference(name="hf_access_token"),
        # "WANDB_API_KEY": SecretReference(name="wandb_api_key"),
    },
    cache_config=CacheConfig(enabled=True),
    checkpointing_config=CheckpointingConfig(enabled=True),
)

# Compute resources
training_compute = Compute(
    accelerator=AcceleratorSpec(accelerator="H100", count=2),
)

# Training job definition
training_job = TrainingJob(
    image=Image(base_image=BASE_IMAGE),
    compute=training_compute,
    runtime=training_runtime,
)

# Project groups related training jobs together
training_project = TrainingProject(
    name="LoRA Training Job - gpt-oss-20b",
    job=training_job
)
```

This example uses the `pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime` base image. You can use other base images to support your framework:

| Framework | Base image                                                                              |
| --------- | --------------------------------------------------------------------------------------- |
| PyTorch   | `pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime`                                         |
| Axolotl   | `axolotlai/axolotl:main-20250811-py3.11-cu126-2.7.1`                                    |
| Unsloth   | `unsloth/unsloth:2025.10.9-pt2.8.0-cu12.8-updates-fixes`                                |
| VeRL      | `verlai/verl:verl0.3.0.post1`                                                           |
| Megatron  | `baseten/megatron:py3.11.11-cuda12.8.1-torch2.8.0-fa2.8.1-megatron0.14.1-msswift3.10.3` |

For information on using private images, see the [Training SDK reference](/reference/sdk/training#dockerauth).

To configure your project, you should set:

* **Local artifacts**: Place scripts (`train.py`, `run.sh`), config files, and data in the same directory as `config.py`. Truss packages everything and uploads it to the container's working directory.
* **Ignore files**: Create a `.truss_ignore` file to exclude files from upload, using `.gitignore` syntax. For more information, see the [Training reference](/reference/cli/training/training-cli#ignoring-files-and-folders).
* **Secrets**: Store secrets in your [Baseten workspace](/organization/secrets) and reference them with [`SecretReference`](/reference/sdk/training#secretreference).

### Create your training scripts

Baseten Training is framework-agnostic.
Typically, you use a `run.sh` script to install dependencies and launch training.
For example:

```bash run.sh theme={"system"}
#!/bin/bash
set -eux

# Install dependencies
pip install "trl>=0.20.0" "peft>=0.17.0" "transformers>=4.55.0"

# Run training
python3 train.py
```

Here's a corresponding `train.py`:

```python train.py theme={"system"}
import os
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Mxfp4Config
import torch
from peft import LoraConfig, get_peft_model
from trl import SFTConfig, SFTTrainer

MODEL_ID = "openai/gpt-oss-20b"
DATASET_ID = "HuggingFaceH4/Multilingual-Thinking"

# Load dataset and tokenizer
dataset = load_dataset(DATASET_ID, split="train")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

# Load model with quantization
quantization_config = Mxfp4Config(dequantize=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    attn_implementation="eager",
    torch_dtype=torch.bfloat16,
    quantization_config=quantization_config,
    use_cache=False,
    device_map="auto",
)

# Configure LoRA
peft_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules="all-linear",
    target_parameters=[
        "7.mlp.experts.gate_up_proj",
        "7.mlp.experts.down_proj",
        "15.mlp.experts.gate_up_proj",
        "15.mlp.experts.down_proj",
        "23.mlp.experts.gate_up_proj",
        "23.mlp.experts.down_proj",
    ],
)
peft_model = get_peft_model(model, peft_config)
peft_model.print_trainable_parameters()

# Training configuration
training_args = SFTConfig(
    learning_rate=2e-4,
    gradient_checkpointing=True,
    num_train_epochs=1,
    logging_steps=1,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    max_length=2048,
    warmup_ratio=0.03,
    lr_scheduler_type="cosine_with_min_lr",
    lr_scheduler_kwargs={"min_lr_rate": 0.1},
    output_dir=os.getenv("BT_CHECKPOINT_DIR", "./checkpoints"),
)

# Train
trainer = SFTTrainer(
    model=peft_model,
    args=training_args,
    train_dataset=dataset,
    processing_class=tokenizer,
)
trainer.train()

# Save to checkpoint directory for deployment
trainer.save_model(training_args.output_dir)
```

<Important>
  Save your trained model to `$BT_CHECKPOINT_DIR` so Baseten can automatically back up and preserve your checkpoints for deployment.
  Baseten automatically sets this environment variable when you enable checkpointing in your configuration.
</Important>

## Submit your training job

With your `config.py` and training scripts ready, submit the job:

```bash theme={"system"}
truss train push config.py
```

This command parses your `config.py` file, packages local files in the directory
alongside `config.py`, creates or updates the `TrainingProject`, and submits the
`TrainingJob`.

On successful submission, you'll see:

```output theme={"system"}
✨ Training job successfully created!
🪵 View logs for your job via 'truss train logs --job-id <job_id> --tail'
🔍 View metrics for your job via 'truss train metrics --job-id <job_id>'
🌐 View job in the UI: https://app.baseten.co/training/<project_id>/logs/<job_id>
```

Copy the `job_id` from this output to use in the monitoring commands below.

## Monitor your training job

Use the job ID from the submission output to monitor your training job:

```bash theme={"system"}
truss train logs --job-id <job_id> --tail
```

You can also view logs, metrics, and job status in the [Baseten dashboard](https://app.baseten.co/training/).

See [Monitor and manage jobs](/training/management) for detailed monitoring commands including metrics, job status, and stopping jobs.

## Deploy your trained model

Once you see the model saved successfully in your logs, you're ready to deploy.
For example, you might see:

```output theme={"system"}
[2026-01-01 12:00:00] [INFO] Model successfully saved to /workspace/checkpoints
Job has exited. Syncing checkpoints...
```

<Tabs>
  <Tab title="CLI">
    Deploy your fine-tuned model directly to Baseten's inference platform:

    ```bash theme={"system"}
    truss train deploy_checkpoints
    ```

    The interactive wizard guides you through deployment:

    ```output theme={"system"}
    Fetching checkpoints for training job <job_id>...
    ? Use spacebar to select/deselect checkpoints to deploy.
      ○ .
    ❯ ○ checkpoint-15

    ? Enter the model name for your deployment: my-fine-tuned-model
    ? Select the GPU type to use for deployment: A100
    ? Select the number of A100 GPUs to use for deployment: 2
    ? Enter the huggingface secret name: hf_access_token

    Successfully created model version: deployment-1
    Model version ID: <model_version_id>
    ```
  </Tab>

  <Tab title="Dashboard">
    Deploy from the [Baseten dashboard](https://app.baseten.co/training/):

    1. Select your training job.
    2. Open the **Checkpoints** tab and choose a checkpoint.
    3. Click **Deploy** and configure your model name, instance type, and scaling settings.
  </Tab>
</Tabs>

### Test your deployment

After deployment, call your model using the OpenAI-compatible chat format:

<Tabs>
  <Tab title="CLI">
    ```bash theme={"system"}
    truss predict --model <model-id> --data '{"model": "<checkpoint-name>", "messages": [{"role": "user", "content": "Hello!"}]}'
    ```
  </Tab>

  <Tab title="Python">
    ```python theme={"system"}
    import baseten

    model = baseten.deployed_model_id("<model-id>")
    response = model.predict({
        "model": "<checkpoint-name>",
        "messages": [{"role": "user", "content": "Hello!"}]
    })
    print(response)
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={"system"}
    curl -X POST https://model-<id>.api.baseten.co/v1/predict \
      -H "Authorization: Api-Key $BASETEN_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"model": "<checkpoint-name>", "messages": [{"role": "user", "content": "Hello!"}]}'
    ```
  </Tab>
</Tabs>

### Training framework examples

| Framework    | Example                                                                                                      | Description            |
| ------------ | ------------------------------------------------------------------------------------------------------------ | ---------------------- |
| **TRL**      | [oss-gpt-20b-lora-trl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/oss-gpt-20b-lora-trl)   | LoRA fine-tuning       |
| **TRL**      | [qwen3-8b-lora-dpo-trl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-8b-lora-dpo-trl) | DPO training           |
| **Axolotl**  | [oss-gpt-20b-axolotl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/oss-gpt-20b-axolotl)     | Axolotl fine-tuning    |
| **Axolotl**  | [gemma-27b-axolotl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/gemma-27b-axolotl)         | Multi-node fine-tuning |
| **Unsloth**  | [llama-8b-lora-unsloth](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/llama-8b-lora-unsloth) | Fast LoRA fine-tuning  |
| **VeRL**     | [qwen3-8b-fft-verl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-8b-fft-verl)         | RL with custom rewards |
| **MS-Swift** | [glm-4-7-msswift](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/glm-4-7-msswift)             | GLM-4 fine-tuning      |
| **MS-Swift** | [qwen3-235b-mswift](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-235b-mswift)         | Large model training   |

See the [ML Cookbook](https://github.com/basetenlabs/ml-cookbook) for all examples and [advanced recipes](https://github.com/basetenlabs/ml-cookbook/tree/main/recipes).


# Lifecycle
Source: https://docs.baseten.co/training/lifecycle

Understanding the different states and transitions in a Baseten training job's lifecycle.

A training job in Baseten progresses through several states from creation to completion. Understanding these states helps you monitor and manage your training jobs effectively.

## Job states

| State                        | Description                                                                                                                 | Active | Terminal |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ------ | -------- |
| `TRAINING_JOB_CREATED`       | Initial state when a job is first created. Baseten has received the training configuration and persisted it to our records. | ✅      |          |
| `TRAINING_JOB_DEPLOYING`     | Baseten is deploying the job, including provisioning compute resources and installing dependencies.                         | ✅      |          |
| `TRAINING_JOB_RUNNING`       | The training code is actively executing.                                                                                    | ✅      |          |
| `TRAINING_JOB_COMPLETED`     | The job has successfully finished execution. Any checkpoints or artifacts have been saved and uploaded.                     |        | ✅        |
| `TRAINING_JOB_DEPLOY_FAILED` | The job failed to deploy. This is likely due to a bad image or a resource allocation issue.                                 |        | ✅        |
| `TRAINING_JOB_FAILED`        | The job encountered an error and could not complete successfully. Check the logs for error details.                         |        | ✅        |
| `TRAINING_JOB_STOPPED`       | The job was manually stopped by a user.                                                                                     |        | ✅        |

## State transitions

Jobs typically progress through states in the following order:

1. `TRAINING_JOB_CREATED` → `TRAINING_JOB_DEPLOYING`: Automatic transition once resources are allocated
2. `TRAINING_JOB_DEPLOYING` → `TRAINING_JOB_RUNNING`: Automatic transition once environment setup is complete
3. `TRAINING_JOB_RUNNING` → `TRAINING_JOB_COMPLETED`: Automatic transition upon successful completion

A job may enter `TRAINING_JOB_FAILED` from any state if an error occurs. Similarly, `TRAINING_JOB_STOPPED` can be entered from any active state (`DEPLOYING` or `RUNNING`) when manually stopped.

You can monitor these state transitions using the CLI command:

```bash theme={"system"}
truss train view # shows all active jobs
truss train view --job-id <your_job_id> # shows a specific job
```

Or track a specific job's progress with:

```bash theme={"system"}
truss train logs --job-id <your_job_id> --tail
```


# Loading Checkpoints
Source: https://docs.baseten.co/training/loading

Resume training from existing checkpoints to continue where you left off

Checkpoint loading lets you resume training from previously saved model states. When enabled, Baseten automatically downloads your specified checkpoints to the training environment before your training code starts.

**Use cases:**

* Resume failed training jobs
* Incremental training and fine-tuning

## Accessing Downloaded Checkpoints

Checkpoints are available through the `BT_LOAD_CHECKPOINT_DIR` environment variable. For single-node training, they're located in `BT_LOAD_CHECKPOINT_DIR/rank-0/`.

<Note>
  Checkpoint restoration currently does not support loading weights that are sharded across multiple nodes.
</Note>

## Checkpoint Reference

Create references to checkpoints using the `BasetenCheckpoint` factory:

### From Latest

```python theme={"system"}
# Load the latest checkpoint from a project 
BasetenCheckpoint.from_latest_checkpoint(project_name="my-training-project")  

# Load the latest checkpoint from a previous job  
BasetenCheckpoint.from_latest_checkpoint(job_id="gvpql31")
```

**Parameters:**

* `project_name`: Load the latest checkpoint from the most recent job in this project
* `job_id`: Load the latest checkpoint from this specific job
* Both parameters: Load the latest checkpoint from that specific job in that project

### From Named

```python theme={"system"}
# Pin your starting point to a specific checkpoint
BasetenCheckpoint.from_named_checkpoint(checkpoint_name="checkpoint-20", job_id="gvpql31")
```

**Parameters:**

* `checkpoint_name`: The name of the specific checkpoint to load
* `job_id`: The job that contains the named checkpoint
* Both parameters: Load the named checkpoint from that specific job in that project

## Configuration Examples

Here are practical examples of how to configure checkpoint loading in your training jobs:

### From Latest

```python theme={"system"}
# Latest checkpoint from project
load_config = LoadCheckpointConfig(
    enabled=True,
    checkpoints=[
        BasetenCheckpoint.from_latest_checkpoint(project_name="gpt-finetuning")
    ]
)

# Latest checkpoint from specific job
load_config = LoadCheckpointConfig(
    enabled=True,
    checkpoints=[
        BasetenCheckpoint.from_latest_checkpoint(job_id="gvpql31")
    ]
)
```

### From Named

```python theme={"system"}
# Specific named checkpoint
load_config = LoadCheckpointConfig(
    enabled=True,
    checkpoints=[
        BasetenCheckpoint.from_named_checkpoint(
            checkpoint_name="checkpoint-20",
            job_id="gvpql31"
        )
    ]
)

# Named checkpoint with custom download location
load_config = LoadCheckpointConfig(
    enabled=True,
    download_folder="/tmp/my_checkpoints",
    checkpoints=[
        BasetenCheckpoint.from_named_checkpoint(
            checkpoint_name="checkpoint-20",
            job_id="rwnojdq"
        )
    ]
)
```

**Configuration parameters for :**

* `enabled`: Set to `True` to enable checkpoint loading
* `checkpoints`: List containing checkpoint references
* `download_folder`: Optional custom download location (defaults to `/tmp/loaded_checkpoints`)

## Complete TrainingJob Setup

```python theme={"system"}
from truss_train import LoadCheckpointConfig, BasetenCheckpoint, CheckpointingConfig, TrainingJob, Image, Runtime, TrainingProject
from truss_train.definitions import CacheConfig

# Configure checkpoint loading
load_checkpoint_config = LoadCheckpointConfig(
    enabled=True,
    download_folder="/tmp/loaded_checkpoints",
    checkpoints=[
        BasetenCheckpoint.from_latest_checkpoint(job_id="previous_job_id")
    ]
)

# Configure checkpointing for saving new checkpoints
checkpointing_config = CheckpointingConfig(
    enabled=True,
    checkpoint_path="/tmp/training_checkpoints"
)

# Create TrainingJob
job = TrainingJob(
    image=Image(base_image="your-base-image"),
    runtime=Runtime(
        checkpointing_config=checkpointing_config,
        load_checkpoint_config=load_checkpoint_config,
        start_commands=["chmod +x ./run.sh && ./run.sh"],
        cache_config=CacheConfig(enabled=True)
    ),
)

project = TrainingProject(name="my-training-project", job=job)
```

## Using Checkpoints in Your Training Code

Access loaded checkpoints using the `BT_LOAD_CHECKPOINT_DIR` environment variable:

```python theme={"system"}
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
from transformers.trainer_utils import get_last_checkpoint
import os

def train():
    checkpoint_dir = os.environ.get("BT_LOAD_CHECKPOINT_DIR")
    last_checkpoint = None

    if checkpoint_dir:
        last_checkpoint = get_last_checkpoint(checkpoint_dir)
        if last_checkpoint:
            print(f"✅ Resuming from checkpoint: {last_checkpoint}")
            model = AutoModelForSequenceClassification.from_pretrained(last_checkpoint)
            tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir)
        else:
            print("⚠️ No checkpoint found, starting from scratch")
            model = AutoModelForSequenceClassification.from_pretrained("your-base-model")
            tokenizer = AutoTokenizer.from_pretrained("your-base-model")
    else:
        print("ℹ️ No checkpoint loading configured")
        model = AutoModelForSequenceClassification.from_pretrained("your-base-model")
        tokenizer = AutoTokenizer.from_pretrained("your-base-model")

    training_args = TrainingArguments(
        output_dir=os.environ.get("BT_CHECKPOINT_DIR", "/tmp/training_checkpoints"),
        save_strategy="steps",
        save_steps=1000,
        load_best_model_at_end=True,
    )

    trainer = Trainer(model=model, args=training_args)
    trainer.train(resume_from_checkpoint=last_checkpoint)
```


# Management
Source: https://docs.baseten.co/training/management

How to monitor, manage, and interact with your Baseten Training projects and jobs.

Once you have submitted training jobs, Baseten provides tools to manage your `TrainingProject`s and individual `TrainingJob`s. You can use the [CLI](/reference/cli/training/training-cli) or the [API](/reference/training-api/overview) to manage your jobs.

## `TrainingProject` management

* **Listing Projects:** To view all your training projects:
  ```bash theme={"system"}
  truss train view
  ```
  This command will list all `TrainingProject`s you have access to, typically showing their names and IDs. Additionally, this command will show all active jobs.

* **Viewing Jobs within a Project:** To see all jobs associated with a specific project, use its `project` (obtained when creating the project or from `truss train view`):
  ```bash theme={"system"}
  truss train view --project <project_id or project_name>
  ```

* **Deleting a `TrainingProject`:** To delete a training project from the Baseten dashboard:

  1. Select the training project you want to delete.
  2. Type the project name (for example, `demo/qwen3-0.6b`) to confirm.
  3. Select **Delete**.

  <Warning>
    When you delete a project, the following data is permanently deleted with no archival or recovery option:

    * All undeployed [checkpoints](/training/concepts/checkpointing) from every job in the project
    * All data in the project's [training cache](/training/concepts/cache) (`$BT_PROJECT_CACHE_DIR`)

    Checkpoints that have been [deployed](/training/deployment) aren't affected.
  </Warning>

## `TrainingJob` management

After submitting a job with `truss train push config.py`, you receive a `project_id` and `job_id`.

* **Listing Jobs:** As shown above, you can list all jobs within a project using:
  ```bash theme={"system"}
  truss train view --project <project_id or project_name>
  ```
  This will typically show job IDs, statuses, creation times, etc.

* **Checking Status and Retrieving Logs:** To view the logs for a specific job, you can tail them in real-time or fetch existing logs.
  * To view logs for the most recently submitted job in the current context (e.g., if you just pushed a job from your current terminal directory):
    ```bash theme={"system"}
    truss train logs --tail
    ```
  * To view logs for a specific job using its `job-id`:
    ```bash theme={"system"}
    truss train logs --job-id <your_job_id> [--tail]
    ```
    Add `--tail` to follow the logs live.

* **Understanding Job Statuses:**
  The `truss train view` and `truss train logs` commands will help you track which status a job is in. For more on the job lifecycle, see the [Lifecycle](/training/lifecycle) page.

* **Stopping a `TrainingJob`:** If you need to stop a running job, use the `stop` command with the job's project ID and job ID:
  ```bash theme={"system"}
  truss train stop --job-id <your_job_id>
  truss train stop --all # Stops all active jobs; Will prompt the user for confirmation.
  ```
  This will transition the job to the `TRAINING_JOB_STOPPED` state.

* **Deleting a `TrainingJob`:** To delete a training job from the Baseten dashboard:

  1. Select the project containing the job.
  2. Select the job you want to delete.
  3. Type the job name (for example, `job-2`) to confirm.
  4. Select **Delete**.

  <Warning>
    When you delete a job, all undeployed checkpoints are deleted permanently. There's no archival or recovery option. Checkpoints that have been [deployed](/training/deployment) aren't affected.
  </Warning>

* **Understanding Job Outputs & Checkpoints:**
  * The primary outputs of a successful `TrainingJob` are model **checkpoints** (if checkpointing is enabled and configured).
  * These checkpoints are stored by Baseten. Refer to the [Checkpointing section in Core Concepts](/training/concepts#checkpointing) for how `CheckpointingConfig` works.
  * When you are ready to [deploy a model](/training/deployment), you will specify which checkpoints to use. The `model_name` you assign during deployment (via `DeployCheckpointsConfig`) becomes the identifier for this trained model version derived from your specific job's checkpoints.
  * You can see the available checkpoints for a job via the [Training API](/reference/training-api/get-training-job-checkpoints).


# Training on Baseten
Source: https://docs.baseten.co/training/overview

Own your intelligence and train custom models with our developer-first training infrastructure.

Baseten provides a flexible training platform that enables you to bring your own training scripts, utilize the latest training techniques, and fine tune the newest models.

Train models and serve them in production, all on one platform. Baseten automatically stores your checkpoints during training and makes them ready for deployment. No downloading weights, no re-uploading, no separate infrastructure. Your fine-tuned model goes from checkpoint to production endpoint in a single command.

```bash theme={"system"}
# Train your model
truss train push config.py

# Deploy from the checkpoint
truss train deploy_checkpoints --job-id <job_id>
```

## Train and serve on one platform

The train-to-serve workflow is seamless:

1. **Set up your training project:** Bring any framework or start with a template.
2. **Configure your training job:** Define compute, runtime, and checkpointing settings.
3. **Run on managed infrastructure:** Use H100, H200, or A10G GPUs—single-node or multi-node.
4. **Checkpoints sync automatically:** Baseten stores checkpoints as training progresses.
5. **Deploy your fine-tuned model:** Go from checkpoint to production endpoint in one command.

No infrastructure management. No manual file transfers. Bring any framework—Axolotl, TRL, VeRL, Megatron, or your own training code—and your trained model serves traffic within minutes of training completion.

## Supported frameworks

Baseten Training is framework-agnostic. Use whatever framework fits your workflow.

| Framework | Best for                                         | Example                                                                                                                |
| --------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Axolotl   | Configuration-driven fine-tuning with LoRA/QLoRA | [oss-gpt-20b-axolotl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/oss-gpt-20b-axolotl)               |
| TRL       | SFT, DPO, and GRPO with Hugging Face             | [oss-gpt-20b-lora-trl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/oss-gpt-20b-lora-trl)             |
| Unsloth   | Fast single-GPU LoRA training                    | [llama-8b-lora-unsloth](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/llama-8b-lora-unsloth)           |
| VeRL      | Reinforcement learning with custom rewards       | [qwen3-8b-lora-verl](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-8b-lora-verl)                 |
| MS-Swift  | Long-context and multilingual training           | [qwen3-30b-mswift-multinode](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/qwen3-30b-mswift-multinode) |

Browse the [ML Cookbook](https://github.com/basetenlabs/ml-cookbook) for more examples including multi-node training with FSDP and DeepSpeed.

## Key features

### Checkpoint management

Checkpoints sync automatically to Baseten storage during training. You can:

* **Deploy** any checkpoint as a production endpoint with [`truss train deploy_checkpoints`](/training/deployment).
* **Download** checkpoints for local evaluation and analysis.
* **Resume** from any checkpoint if a job fails or you want to train further.

Learn more about [checkpointing](/training/concepts/checkpointing).

### Persistent caching

Speed up training iterations by caching models, datasets, and preprocessed data between jobs. The cache persists across training runs, so you don't re-download 70B models every time.

Learn more about the [training cache](/training/concepts/cache).

### Multi-node training

Scale training across multiple GPU nodes with InfiniBand networking. Baseten handles node orchestration, communication setup, and environment variables—you just set `node_count` in your configuration.

Learn more about [multi-node training](/training/concepts/multinode).

### Interactive development with rSSH

Debug training jobs interactively with SSH-like access to your training environment. Rapidly experiment, inspect state, and iterate without losing reproducibility.

[Contact us](https://www.baseten.co/talk-to-us/) to learn more about rSSH.

## Next steps

<CardGroup>
  <Card title="Get started" icon="rocket" href="/training/getting-started">
    Run your first training job and deploy the result.
  </Card>

  <Card title="ML Cookbook" icon="book" href="https://github.com/basetenlabs/ml-cookbook">
    Production-ready examples for various frameworks and models.
  </Card>
</CardGroup>

## Reference

* [CLI reference](/reference/cli/training/training-cli)
* [SDK reference](/reference/sdk/training)
* [API reference](/reference/training-api/overview)


# Deployments
Source: https://docs.baseten.co/troubleshooting/deployments

Troubleshoot common problems during model deployment

## Issue: `truss push` can't find `config.yaml`

```sh theme={"system"}
[Errno 2] No such file or directory: '/Users/philipkiely/Code/demo_docs/config.yaml'
```

### Fix: set correct target directory

The directory `truss push` is looking at is not a Truss. Make sure you're giving `truss push` access to the correct directory by:

* Running `truss push --watch` or `truss push --publish` from the directory containing the Truss. You should see the file `config.yaml` when you run `ls` in your working directory.
* Or passing the target directory as an argument, such as `truss push /path/to/my-truss --watch`.

## Issue: unexpected failure during model build

During the model build step, there can be unexpected failures from temporary circumstances. An example is a network error while downloading model weights from Hugging Face or installing a Python package from PyPi.

### Fix: restart deploy from Baseten UI

First, check your model logs to determine the exact cause of the error. If it's an error during model download, package installation, or similar, you can try restarting the deploy from the model dashboard in your workspace.


# Inference
Source: https://docs.baseten.co/troubleshooting/inference

Troubleshoot common problems during model inference

## Model I/O issues

### Error: JSONDecodeError

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

This error means you're attempting to pass a model input that is not JSON-serializable. For example, you might have left out the double quotes required for a valid string:

```sh theme={"system"}
truss predict -d 'This is not a string' # Wrong
truss predict -d '"This is a string"'   # Correct
```

## Model version issues

### Error: No OracleVersion matches the given query

```
<Server response: {
    'errors': [{
        'message': 'No OracleVersion matches the given query.',
        'locations': [{'line': 3, 'column': 13}],
        'path': ['model_version']
    }],
    'data': {'model_version': None}
}>
```

Make sure that the model ID or deployment ID you're passing is correct and that the associated model has not been deleted.

Additionally, make sure you're using the correct endpoint:

* [Production environment endpoint](/reference/inference-api/predict-endpoints/environments-predict).
* [Development deployment endpoint](/reference/inference-api/predict-endpoints/development-predict).
* [Deployment endpoint](/reference/inference-api/predict-endpoints/deployment-predict).

## Authentication issues

### Error: Service provider not found

```
ValueError: Service provider example-service-provider not found in ~/.trussrc
```

This error means your `~/.trussrc` is incomplete or incorrect. It should be formatted as follows:

```
[baseten]
remote_provider = baseten
api_key = YOUR.API_KEY
remote_url = https://app.baseten.co
```

### Error: You have to log in to perform the request

```
<Server response: {
    'errors': [{
        'message': 'You have to log in to perform the request',
        'locations': [{'line': 3, 'column': 13}],
        'path': ['model_version'],
        'extensions': {'code': 'UNAUTHENTICATED_ACCESS'}
    }],
    'data': {'model_version': None}
}>
```

This error occurs on `truss predict` when the API key in `~/.trussrc` for a given host is missing or incorrect. To fix it, update your API key in the `~/.trussrc` file.

### Error: Please check the API key you provided

```
{
        "error": "please check the api-key you provided"
}
```

This error occurs when using `curl` or similar to call the model via its API endpoint when the API key passed in the request header is not valid. Make sure you're using a valid API key then try again.


