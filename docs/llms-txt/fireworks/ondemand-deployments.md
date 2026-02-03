# Source: https://docs.fireworks.ai/guides/ondemand-deployments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployments

> Configure and manage on-demand deployments on dedicated GPUs

<Info>
  **New to deployments?** Start with our [Deployments Quickstart](/getting-started/ondemand-quickstart) to deploy and query your first model in minutes, then return here to learn about configuration options.
</Info>

On-demand deployments give you dedicated GPUs for your models, providing several advantages over serverless:

* **Better performance** – Lower latency, higher throughput, and predictable performance unaffected by other users
* **No hard rate limits** – Only limited by your deployment's capacity
* **Cost-effective at scale** – Cheaper under high utilization. Unlike serverless models (billed per token), on-demand deployments are [billed by GPU-second](https://fireworks.ai/pricing).
* **Broader model selection** – Access models not available on serverless
* **Custom models** – Upload your own models (for supported architectures) from Hugging Face or elsewhere

Need higher GPU quotas or want to reserve capacity? [Contact us](https://fireworks.ai/contact).

## Creating & querying deployments

**Create a deployment:**

```bash  theme={null}
# This command returns your accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID> - save it for querying
firectl deployment create accounts/fireworks/models/<MODEL_NAME> --wait
```

See [Deployment shapes](#deployment-shapes) below to optimize for speed, throughput, or cost.

**Query your deployment:**

After creating a deployment, query it using this format:

```
accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>
```

<Tip>
  You can find your deployment name anytime with `firectl deployment list` and `firectl deployment get <DEPLOYMENT_ID>`.
</Tip>

**Example:**

```
accounts/alice/deployments/12345678
```

### Code examples

<Tabs>
  <Tab title="Python (Fireworks SDK)">
    ```python  theme={null}
    from fireworks import Fireworks

    client = Fireworks()

    response = client.chat.completions.create(
      model="accounts/fireworks/models/gpt-oss-120b#<DEPLOYMENT_NAME>",
      messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    ```python  theme={null}
    import os
    from openai import OpenAI

    client = OpenAI(
        api_key=os.environ.get("FIREWORKS_API_KEY"),
        base_url="https://api.fireworks.ai/inference/v1"
    )

    response = client.chat.completions.create(
        model="accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
        messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```javascript  theme={null}
    import OpenAI from "openai";

    const client = new OpenAI({
      apiKey: process.env.FIREWORKS_API_KEY,
      baseURL: "https://api.fireworks.ai/inference/v1",
    });

    const response = await client.chat.completions.create({
      model: "accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
      messages: [
        {
          role: "user",
          content: "Explain quantum computing in simple terms",
        },
      ],
    });

    console.log(response.choices[0].message.content);
    ```
  </Tab>

  <Tab title="curl">
    ```bash  theme={null}
    curl https://api.fireworks.ai/inference/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $FIREWORKS_API_KEY" \
      -d '{
        "model": "accounts/<ACCOUNT_ID>/deployments/<DEPLOYMENT_ID>",
        "messages": [
          {
            "role": "user",
            "content": "Explain quantum computing in simple terms"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

## Deployment shapes

Deployment shapes are the primary way to configure deployments. They're pre-configured templates optimized for speed, cost, or efficiency, including hardware, quantization, and other [performance factors](/faq/deployment/performance/optimization#performance-factors).

* **Fast** – Low latency for interactive workloads
* **Throughput** – Cost-per-token at scale for high-volume workloads
* **Minimal** – Lowest cost for testing or light workloads

**Usage:**

```bash  theme={null}
# List available shapes
firectl deployment-shape-version list --base-model <model-id>

# Create with a shape (shorthand)
firectl deployment create accounts/fireworks/models/deepseek-v3 --deployment-shape throughput

# Create with full shape ID
firectl deployment create accounts/fireworks/models/llama-v3p3-70b-instruct \
  --deployment-shape accounts/fireworks/deploymentShapes/llama-v3p3-70b-instruct-fast

# View shape details
firectl deployment-shape-version get <full-deployment-shape-version-id>
```

<Tip>
  Need even better performance with tailored optimizations? [Contact our team](https://fireworks.ai/contact).
</Tip>

## Managing & configuring deployments

### Basic management

```bash  theme={null}
# List all deployments
firectl deployment list

# Check deployment status
firectl deployment get <DEPLOYMENT_ID>

# Delete a deployment
firectl deployment delete <DEPLOYMENT_ID>
```

<Note>
  By default, deployments scale to zero if unused for 1 hour. Deployments with min replicas set to 0 are automatically deleted after 7 days of no traffic.
</Note>

<Warning>
  When a deployment is scaled to zero, requests return a `503` error immediately while the deployment scales up. Your application should implement retry logic to handle this. See [Scaling from zero behavior](/deployments/autoscaling#scaling-from-zero-behavior) for implementation details.
</Warning>

### GPU hardware

Choose GPU type with `--accelerator-type`:

* `NVIDIA_A100_80GB`
* `NVIDIA_H100_80GB`
* `NVIDIA_H200_141GB`

GPU availability varies by [region](/deployments/regions). See [Hardware selection guide→](https://docs.fireworks.ai/faq/deployment/ondemand/hardware-options#hardware-selection)

### Autoscaling

Control replica counts, scale timing, and load targets for your deployment.

See the [Autoscaling guide](/deployments/autoscaling) for configuration options.

### Multiple GPUs per replica

Use multiple GPUs to improve latency and throughput:

```bash  theme={null}
firectl deployment create <MODEL_NAME> --accelerator-count 2
```

More GPUs = faster generation. Note that scaling is sub-linear (2x GPUs ≠ 2x performance).

## Advanced

* **[Speculative decoding](/deployments/speculative-decoding)** - Speed up text generation using draft models or n-gram speculation
* **[Quantization](/models/quantization)** - Reduce model precision (e.g., FP16 to FP8) to improve speeds and reduce costs by 30-50%
* **[Performance benchmarking](/deployments/benchmarking)** - Measure and optimize your deployment's performance with load testing
* **[Managing default deployments](/deployments/managing-default-deployments)** - Control which deployment handles queries when using just the model name
* **[Publishing deployments](/deployments/publishing-deployments)** - Make your deployment accessible to other Fireworks users

## Next steps

<CardGroup cols={3}>
  <Card title="Autoscaling" href="/deployments/autoscaling" icon="arrows-up-down">
    Configure autoscaling for optimal cost and performance
  </Card>

  <Card title="Upload custom models" href="/models/uploading-custom-models" icon="cloud-arrow-up">
    Deploy your own models from Hugging Face
  </Card>

  <Card title="Quantization" href="/models/quantization" icon="compress">
    Reduce costs with model quantization
  </Card>

  <Card title="Regions" href="/deployments/regions" icon="earth-americas">
    Choose deployment regions for optimal latency
  </Card>

  <Card title="Reserved capacity" href="/deployments/reservations" icon="calendar-check">
    Purchase reserved GPUs for guaranteed capacity
  </Card>

  <Card title="Fine-tuning" href="/fine-tuning/finetuning-intro" icon="wand-magic-sparkles">
    Fine-tune models for your specific use case
  </Card>
</CardGroup>
