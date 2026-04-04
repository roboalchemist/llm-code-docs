# Source: https://docs.fireworks.ai/tools-sdks/python-client/sdk-basics.md

# Build SDK Basics

<Warning>
  This SDK documentation applies to version [0.19.20](https://pypi.org/project/fireworks-ai/0.19.20/) and earlier. The Build SDK will be deprecated and replaced with version 1.0.0 of the SDK (see our [changelog](/updates/changelog#2025-11-12) for more details). Please migrate to the new SDK when it becomes available.
</Warning>

## Why use the Build SDK?

The Fireworks Build SDK gives you a declarative way to work with Fireworks resources like deployments, fine-tuning jobs, and datasets. We've designed it to handle all the infrastructure complexity for you, letting you focus on building your application. Instead of using the web UI, CLI, or raw API calls, you can manage everything through simple Python code with smart, logical defaults without sacrificing control and customizability.

The principles of the SDK are the following:

* **Object-oriented:** Fireworks primitives are represented as Python objects. You can access their capabilities and properties through methods and attributes.

* **Declarative:** You can describe your desired state and the SDK will handle reconcilliation.

* **Smart defaults:** The SDK will infer the most logical defaults for you, prioritizing development speed and lowest cost. Here are some examples:
  * The SDK will automatically use a serverless deployment for models that are available serverlessly unless you specify otherwise.
  * When creating deployments, the SDK will also enable scale-to-zero with the shortest possible scale-down window.
  * If the SDK determines that a resource already exists by matching its signature (see below), it will re-use the existing resource instead of creating a new one.

* **Customizable:** Although we enable smart defaults, you still have full access to the configuration parameters for any Fireworks resource

<Note>
  The Build SDK is currently in beta and not all functionality may be supported. Please reach out to [dhuang@fireworks.ai](mailto:dhuang@fireworks.ai) to report any issues or feedback.
</Note>

## The `LLM()` class

Running a model on Fireworks is as simple as instantiating the `LLM` class and
calling a single function. Here's an example of how to instantiate the latest
[Llama 4 Maverick model](https://fireworks.ai/models/fireworks/llama4-maverick-instruct-basic) using the Build SDK.

```python main.py {3} theme={null}
from fireworks import LLM

llm = LLM(model="llama4-maverick-instruct-basic", deployment_type="serverless")

response = llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(response.choices[0].message.content)
```

You can send various parameters to the `LLM()` constructor to take full advantage of all of Fireworks' customization options.

```python main.py {2-8} theme={null}
llm = LLM(
  model="qwen2p5-72b-instruct",
  id="my-deployment-id",
  deployment_type="on-demand",
  precision="FP8",
  accelerator_type="NVIDIA_H100_80GB",
  draft_model="qwen2p5-0p5b-instruct",
  draft_token_count=4,
  min_replica_count=1,
) 

# Apply deployment configuration to Fireworks
llm.apply()

response = llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(response.choices[0].message.content)
```

## Fine-tuning a model

You can fine-tune a model by creating a `Dataset` object and then calling the `.create_supervised_fine_tuning_job()` method on the `LLM` object.

```python main.py theme={null}
from fireworks import Dataset, LLM

dataset = Dataset.from_file("my-dataset.jsonl")

base_model = LLM(model="qwen2p5-7b-instruct", id="my-base-deployment-id", deployment_type="on-demand")

job = base_model.create_supervised_fine_tuning_job(
    "my-fine-tuning-job",
    dataset,
)
job.wait_for_completion()
fine_tuned_model=job.output_llm
```

Datasets are files in JSONL format, where each line represents a complete JSON-formatted training example following the Chat Completions API format. See [fine-tuning a model](../../fine-tuning/fine-tuning-models#step-2%3A-prepare-the-dataset) for an example. Once you have training examples prepared, you can create a `Dataset` object and upload the dataset to Fireworks by using `from_file()`, `from_string()`, or `from_list()`, and pass it to the `.create_supervised_fine_tuning_job()` method on the `LLM` object as we did above.

## Debug mode

Sometimes, it can be helpful to see the log of actions that the SDK is taking behind the scenes. You can enable debug mode by setting the `FIREWORKS_SDK_DEBUG=True` environment variable.

## Key concepts

### Resource types

The SDK supports the following resource types:

* `LLM` - Represents a model running on a deployment
* `Dataset` - Represents a dataset used to create a fine-tuning job
* `SupervisedFineTuningJob` - Represents a fine-tuning job

### Deployment type selection

The SDK tries to be parsimonious with the way it deploys resources. We provide two types of deployment options on Fireworks:

* `serverless` hosting is enabled for some commonly-used state of the art models. The pricing for these models is per-token, i.e. you only pay for the tokens you use, and subject to rate limits.
* `on-demand` hosting is enabled for all other models. The pricing for these models is per GPU-second. This hosting is required for models that are not available serverlessly or workloads that exceed serverless rate limits.

For non-finetuned models, you can always specify the deployment type of `LLM()` by passing either `"serverless"` or `"on-demand"` as the `deployment_type` parameter to the constructor. If the model is not available for the deployment type you selected, the SDK will throw an error. The SDK can also decide the best deployment strategy on your behalf, just pass `deployment_type="auto"`. If the model is available serverlessly, the SDK will use serverless hosting, otherwise the SDK will create an on-demand deployment.

<Note>
  When using `deployment_type="on-demand"` or `deployment_type="on-demand-lora"`, you must call `.apply()` to apply the deployment configuration to Fireworks. This is not required for serverless deployments. When using `deployment_type="auto"`, the SDK will automatically handle deployment creation, but if it falls back to on-demand deployment, you may need to call `.apply()` explicitly. If you do not call `.apply()`, you are expected to set up the deployment through the deployment page at [https://app.fireworks.ai/dashboard/deployments](https://app.fireworks.ai/dashboard/deployments).
</Note>

<Warning>
  Be careful with the `deployment_type` parameter, especially for `"auto"` and `"on-demand"` deployments. While the SDK will try to make the most cost effective choice for you and put sensible autoscaling policies in place, it is possible to unintentionally create many deployments that lead to unwanted spend, especially when working with non-serverless models.
</Warning>

<Warning>
  When using `deployment_type="on-demand"`, you must provide an `id` parameter to uniquely identify your deployment. This is required to prevent accidental creation of multiple deployments.
</Warning>

For finetuned (LoRA) models, passing `deployment_type="serverless" ` will try to deploy the finetuned model to serverless hosting, `deployment_type="on-demand"` will create an on-demand deployment of your base model and merge in your LoRA weights, `deployment_type="on-demand-lora"` will create an on-demand deployment with Multi-LoRA enabled, and `deployment_type="auto"` will try to use `serverless` if available, otherwise fall back to `on-demand-lora`.

#### Deploying Fine-tuned Models with On-Demand

When deploying a fine-tuned model using `deployment_type="on-demand"`, you need to provide:

* `model` - Your fine-tuned model ID (e.g., `"accounts/your-account/models/your-fine-tuned-model-id"`)
* `id` - A unique deployment identifier (can be any simple string like `"my-fine-tuned-deployment"`)

```python  theme={null}
# Deploy a fine-tuned model with on-demand deployment
fine_tuned_llm = LLM(
    model="accounts/your-account/models/your-fine-tuned-model-id",
    deployment_type="on-demand",
    id="my-fine-tuned-deployment"  # Simple string ID
)

# Apply deployment configuration to Fireworks
fine_tuned_llm.apply()

# Track deployment in web dashboard
print(f"Track at: {fine_tuned_llm.deployment_url}")
```

<Note>
  The `id` parameter can be any simple string - it does not need to follow the format `"accounts/account_id/deployments/model_id"`.
</Note>

### Resource signatures

Each resource has a signature, which is the set of properties that are used to identify the resource. The SDK will use the signature to determine if a resource already exists and can be re-used.

| Resource                  | Signature                   |
| ------------------------- | --------------------------- |
| `LLM`                     | `id`                        |
| `Dataset`                 | `hash(data)` and `filename` |
| `SupervisedFineTuningJob` | `name` and `model`          |

For `LLM` resources, the resource signature is based on the `id` parameter. When using `deployment_type="on-demand"`, you must provide a unique `id` to identify your deployment.

For `Dataset` resources, the resource signature is derived from the `filename` of your dataset (if created via `from_file()`) and the hash of the data itself.

For `SupervisedFineTuningJob` resources, you are required to pass a `name` when creating the resource.

### Resource management

The SDK also tries to be parsimonious with the *number* of resources it creates. Before creating a resource, the SDK will first check if a resource with the same signature already exists. If so, the SDK will re-use the existing resource instead of creating a new one. This could mean updating the resource with new configuration parameters, or re-using the existing resource.

A new resource will be created in the following cases for each resource type:

| Resource                  | Created by SDK if...                                                               |
| ------------------------- | ---------------------------------------------------------------------------------- |
| `LLM`                     | You pass a unique `id` to the constructor                                          |
| `Dataset`                 | You change the `filename` of the data or modify the data itself                    |
| `SupervisedFineTuningJob` | You pass a unique `name` when creating the fine-tuning job or use a unique `model` |
