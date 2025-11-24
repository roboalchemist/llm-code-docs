# Source: https://docs.fireworks.ai/tools-sdks/python-client/sdk-reference.md

# Reference

<Warning>
  This SDK documentation applies to version [0.19.20](https://pypi.org/project/fireworks-ai/0.19.20/) and earlier. The Build SDK will be deprecated and replaced with version 1.0.0 of the SDK (see our [changelog](/updates/changelog#2025-11-12) for more details). Please migrate to the new SDK when it becomes available.
</Warning>

# Resource types

The SDK currently supports four types of resources: `LLM`, `Dataset`, `SupervisedFineTuningJob`, and `BatchInferenceJob`.

## LLM

```python  theme={null}
class LLM()
```

**Properties:**

* `deployment_name` *str* - The full name of the deployment (e.g., `accounts/my-account/deployments/my-custom-deployment`)
* `deployment_display_name` *str* - The display name of the deployment, defaults to the filename where the LLM was instantiated unless otherwise specified
* `deployment_url` *str* - The URL to view the deployment in the Fireworks dashboard
* `temperature` *float* - The temperature for generation
* `model` *str* - The model associated with this LLM (e.g., `accounts/fireworks/models/llama-v3p2-3b-instruct`)
* `base_deployment_name` *str* - If a LoRA addon, the deployment name of the base model deployment
* `peft_base_model` *str* - If this is a LoRA addon, the base model identifier (e.g., `accounts/fireworks/models/llama-v3p2-3b-instruct`)
* `addons_enabled` *bool* - Whether LoRA addons are enabled for this LLM
* `model_id` *str* - The identifier used under the hood to query this model (e.g., `accounts/my-account/deployedModels/my-deployed-model-abcdefg`)
* `deployment_id` *str* - The deployment ID (e.g., `my-custom-deployment`)
* `base_deployment_id` *str* - The base deployment ID for LoRA addons
* `perf_metrics_in_response` *bool* - Whether performance metrics are included in responses

### Instantiation

The `LLM(*args, **kwargs)` class constructor initializes a new LLM instance.

```python  theme={null}
from fireworks import LLM
from datetime import timedelta

# Basic usage with required parameters
llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="auto"
)

# Advanced usage with optional parameters
llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="on-demand",
    id="my-custom-deployment",
    accelerator_type="NVIDIA_H100_80GB",
    min_replica_count=1,
    max_replica_count=3,
    scale_up_window=timedelta(seconds=30),
    scale_down_window=timedelta(minutes=10),
    enable_metrics=True
)

# Apply deployment configuration to Fireworks
llm.apply()

# Deploy a fine-tuned model with on-demand deployment
fine_tuned_llm = LLM(
    model="accounts/your-account/models/your-fine-tuned-model-id",
    deployment_type="on-demand",
    id="my-fine-tuned-deployment"  # Simple string identifier
)

# Apply deployment configuration to Fireworks
fine_tuned_llm.apply()

# Deploy fine-tuned model using multi-LoRA (sharing base deployment)
base_model = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="on-demand",
    id="shared-base-deployment",
    enable_addons=True
)

# Apply base deployment configuration to Fireworks
base_model.apply()

fine_tuned_with_lora = LLM(
    model="accounts/your-account/models/your-fine-tuned-model-id",
    deployment_type="on-demand-lora",
    base_id=base_model.deployment_id
)

# Apply LoRA deployment configuration to Fireworks
fine_tuned_with_lora.apply()
```

#### Required Arguments

* `model` *str* - The model identifier to use (e.g., `accounts/fireworks/models/llama-v3p2-3b-instruct`)
* `deployment_type` *str* - The type of deployment to use. Must be one of:
  * `"serverless"`: Uses Fireworks' shared serverless infrastructure
  * `"on-demand"`: Uses dedicated resources for your deployment
  * `"auto"`: Automatically selects the most cost-effective option (recommended for experimentation)
  * `"on-demand-lora"`: For LoRA addons that require dedicated resources

#### Optional Arguments

**Deployment Configuration**

* `id` *str, optional* - Deployment ID to identify the deployment. Required when deployment\_type is "on-demand". Can be any simple string (e.g., `"my-deployment"`) - does not need to follow the format `"accounts/account_id/deployments/model_id"`.
* `deployment_display_name` *str, optional* - Display name for the deployment. Defaults to the filename where the LLM was instantiated. If a deployment with the same display name and model already exists, the SDK will try and re-use it.
* `base_id` *str, optional* - Base deployment ID for LoRA addons. Required when deployment\_type is "on-demand-lora".

**Authentication & API**

* `api_key` *str, optional* - Your Fireworks API key
* `base_url` *str, optional* - Base URL for API calls. Defaults to "[https://api.fireworks.ai/inference/v1](https://api.fireworks.ai/inference/v1)"
* `max_retries` *int, optional* - Maximum number of retry attempts. Defaults to 10

**Scaling Configuration**

* `scale_up_window` *timedelta, optional* - Time to wait before scaling up after increased load. Defaults to 1 second
* `scale_down_window` *timedelta, optional* - Time to wait before scaling down after decreased load. Defaults to 1 minute
* `scale_to_zero_window` *timedelta, optional* - Time of inactivity before scaling to zero. Defaults to 5 minutes

**Hardware & Performance**

* `accelerator_type` *str, optional* - Type of GPU accelerator to use
* `region` *str, optional* - Region for deployment
* `multi_region` *str, optional* - Multi-region configuration
* `min_replica_count` *int, optional* - Minimum number of replicas
* `max_replica_count` *int, optional* - Maximum number of replicas
* `replica_count` *int, optional* - Fixed number of replicas
* `accelerator_count` *int, optional* - Number of accelerators per replica
* `precision` *str, optional* - Model precision (e.g., "FP16", "FP8")
* `world_size` *int, optional* - World size for distributed training
* `generator_count` *int, optional* - Number of generators
* `disaggregated_prefill_count` *int, optional* - Number of disaggregated prefill instances
* `disaggregated_prefill_world_size` *int, optional* - World size for disaggregated prefill
* `max_batch_size` *int, optional* - Maximum batch size for inference
* `max_peft_batch_size` *int, optional* - Maximum batch size for PEFT operations
* `kv_cache_memory_pct` *int, optional* - Percentage of memory for KV cache

**Advanced Features**

* `enable_addons` *bool, optional* - Enable LoRA addons support
* `live_merge` *bool, optional* - Enable live merging
* `draft_token_count` *int, optional* - Number of tokens to generate per step for speculative decoding
* `draft_model` *str, optional* - Model to use for speculative decoding
* `ngram_speculation_length` *int, optional* - Length of previous input sequence for N-gram speculation
* `long_prompt_optimized` *bool, optional* - Optimize for long prompts
* `temperature` *float, optional* - Sampling temperature for generation
* `num_peft_device_cached` *int, optional* - Number of PEFT devices to cache

**Monitoring & Metrics**

* `enable_metrics` *bool, optional* - Enable metrics collection. Currently supports time to last token for non-streaming requests.
* `perf_metrics_in_response` *bool, optional* - Include performance metrics in API responses

**Additional Configuration**

* `description` *str, optional* - Description of the deployment
* `annotations` *dict\[str, str], optional* - Annotations for the deployment
* `cluster` *str, optional* - Cluster identifier
* `enable_session_affinity` *bool, optional* - Enable session affinity
* `direct_route_api_keys` *list\[str], optional* - List of API keys for direct routing
* `direct_route_type` *str, optional* - Type of direct routing
* `direct_route_handle` *str, optional* - Direct route handle

### `apply(wait: bool = True)`

Ensures the deployment is ready and returns the deployment. Like Terraform apply, this will ensure the deployment is ready.

```python  theme={null}
llm.apply(wait=True)
```

### `create_supervised_fine_tuning_job()`

Creates a new supervised fine-tuning job and blocks until it is ready. See the [SupervisedFineTuningJob](#supervisedfinetuningjob) section for details on the parameters.

**Returns:**

* An instance of `SupervisedFineTuningJob`.

```python  theme={null}
job = llm.create_supervised_fine_tuning_job(
    display_name="my-fine-tuning-job",
    dataset_or_id=dataset,
    epochs=3,
    learning_rate=1e-5
)
```

### `reinforcement_step()`

Performs a reinforcement learning step for training. This method creates a new model checkpoint by fine-tuning the current model on the provided dataset with reinforcement learning.

**Arguments:**

* `dataset` *Dataset* - The dataset containing training examples with rewards
* `output_model` *str* - The name of the output model to create
* `lora_rank` *int, optional* - Rank for LoRA fine-tuning. Defaults to 16
* `learning_rate` *float, optional* - Learning rate for training. Defaults to 0.0001
* `max_context_length` *int, optional* - Maximum context length for the model. Defaults to 8192
* `epochs` *int, optional* - Number of training epochs. Defaults to 1
* `batch_size` *int, optional* - Batch size for training. Defaults to 32768
* `accelerator_count` *int, optional* - Number of accelerators to use for training. Defaults to 1
* `accelerator_type` *str, optional* - Type of GPU accelerator to use for training. Supported values: `"NVIDIA_A100_80GB"`, `"NVIDIA_H100_80GB"`, `"NVIDIA_H200_141GB"`. Defaults to `"NVIDIA_A100_80GB"`

<Note>
  When running on a trained LoRA (i.e., when using a model that is already a LoRA fine-tuned checkpoint), the training parameters (`lora_rank`, `learning_rate`, `max_context_length`, `epochs`, `batch_size`) must always be the same as those used in the original LoRA training. Changing these parameters when continuing training from a LoRA checkpoint is not supported and will result in an error.
</Note>

**Returns:**

* An instance of [`ReinforcementStep`](/tools-sdks/python-client/sdk-reference#reinforcementstep) representing the training job

**Note:** The output model name must not already exist. If a model with the same name exists, a `ValueError` will be raised.

```python  theme={null}
# Perform a reinforcement learning step
job = llm.reinforcement_step(
    dataset=dataset,
    output_model="my-improved-model-v1",
    epochs=1,
    learning_rate=1e-5,
    accelerator_count=2,
    accelerator_type="NVIDIA_H100_80GB"
)

# Wait for completion
while not job.is_completed:
    job.raise_if_bad_state()
    time.sleep(1)
    job = job.get()
    if job is None:
        raise Exception("Job was deleted while waiting for completion")

# The new model is now available at job.output_model
```

### `delete_deployment(ignore_checks: bool = False, wait: bool = True)`

Deletes the deployment associated with this LLM instance if one exists.

**Arguments:**

* `ignore_checks` *bool, optional* - Whether to ignore safety checks. Defaults to False.
* `wait` *bool, optional* - Whether to wait for deletion to complete. Defaults to True.

```python  theme={null}
llm.delete_deployment(ignore_checks=True)
```

### `get_time_to_last_token_mean()`

Returns the mean time to last token for non-streaming requests. If no metrics are available, returns None.

**Returns:**

* A float representing the mean time to last token, or None if no metrics are available.

```python  theme={null}
time_to_last_token_mean = llm.get_time_to_last_token_mean()
```

### `with_deployment_type()`

Returns a new LLM instance with the specified deployment type.

**Arguments:**

* `deployment_type` *str* - The deployment type to use ("serverless", "on-demand", "auto", or "on-demand-lora")

**Returns:**

* A new `LLM` instance with the specified deployment type

```python  theme={null}
# Create a new LLM with different deployment type
serverless_llm = llm.with_deployment_type("serverless")
on_demand_llm = llm.with_deployment_type("on-demand")
```

### `with_temperature()`

Returns a new LLM instance with the specified temperature.

**Arguments:**

* `temperature` *float* - The temperature for generation

**Returns:**

* A new `LLM` instance with the specified temperature

```python  theme={null}
# Create a new LLM with different temperature
creative_llm = llm.with_temperature(1.0)
deterministic_llm = llm.with_temperature(0.0)
```

### `with_perf_metrics_in_response()`

Returns a new LLM instance with the specified performance metrics setting.

**Arguments:**

* `perf_metrics_in_response` *bool* - Whether to include performance metrics in responses

**Returns:**

* A new `LLM` instance with the specified performance metrics setting

```python  theme={null}
# Create a new LLM with performance metrics enabled
llm_with_metrics = llm.with_perf_metrics_in_response(True)
```

### `scale_to_zero()`

Sends a request to scale the deployment to 0 replicas but does not wait for it to complete.

**Returns:**

* The deployment object, or None if no deployment exists

```python  theme={null}
deployment = llm.scale_to_zero()
```

### `scale_to_1_replica()`

Scales the deployment to at least 1 replica.

```python  theme={null}
llm.scale_to_1_replica()
```

### `get_deployment()`

Returns the deployment associated with this LLM instance, or None if no deployment exists.

**Returns:**

* The deployment object, or None if no deployment exists

```python  theme={null}
deployment = llm.get_deployment()
```

### `is_peft_addon()`

Checks if this LLM is a PEFT (Parameter-Efficient Fine-Tuning) addon.

**Returns:**

* True if this LLM is a PEFT addon, False otherwise

```python  theme={null}
is_peft = llm.is_peft_addon()
```

### `list_models()`

Lists all models available to your account.

**Returns:**

* A list of model objects

```python  theme={null}
models = llm.list_models()
```

### `get_model()`

Gets the model object for this LLM's model.

**Returns:**

* The model object, or None if the model doesn't exist

```python  theme={null}
model = llm.get_model()
```

### `is_available_on_serverless()`

Checks if the model is available on serverless infrastructure.

**Returns:**

* True if the model is available on serverless, False otherwise

```python  theme={null}
is_serverless = llm.is_available_on_serverless()
```

### `model_id()`

Returns the model ID, which is the model name plus the deployment name if it exists. This is used for the "model" arg when calling the model.

**Returns:**

* The model ID string

```python  theme={null}
model_id = llm.model_id()
```

### `supports_serverless_lora()`

Checks if the model supports serverless LoRA deployment.

**Returns:**

* True if the model supports serverless LoRA, False otherwise

```python  theme={null}
supports_lora = llm.supports_serverless_lora()
```

### `list_fireworks_models()`

Lists all models available on the Fireworks account.

**Returns:**

* A list of model objects from the Fireworks account

```python  theme={null}
fireworks_models = llm.list_fireworks_models()
```

### `is_model_on_fireworks_account()`

Checks if the model is on the Fireworks account.

**Arguments:**

* `model` *str* - The model identifier to check

**Returns:**

* The model object if it exists on the Fireworks account, None otherwise

```python  theme={null}
model_obj = llm.is_model_on_fireworks_account("accounts/fireworks/models/llama-v3p2-3b-instruct")
```

### `is_model_available_on_serverless()`

Checks if a specific model is available on serverless infrastructure.

**Arguments:**

* `model` *str* - The model identifier to check

**Returns:**

* True if the model is available on serverless, False otherwise

```python  theme={null}
is_serverless = llm.is_model_available_on_serverless("accounts/fireworks/models/llama-v3p2-3b-instruct")
```

### `is_model_deployed_on_serverless_account()`

Checks if a model is deployed on a serverless-enabled account.

**Arguments:**

* `model` *SyncModel* - The model object to check

**Returns:**

* True if the model is deployed on a supported serverless account, False otherwise

```python  theme={null}
model_obj = llm.get_model()
if model_obj:
    is_deployed = llm.is_model_deployed_on_serverless_account(model_obj)
```

### `completions.create()` and `completions.acreate()`

Creates a text completion using the LLM. These methods are OpenAI compatible and follow the same interface as described in the [OpenAI Completions API](https://platform.openai.com/docs/api-reference/completions/create). Use `create()` for synchronous calls and `acreate()` for asynchronous calls.

**Arguments:**

* `prompt` *str* - The prompt to complete
* `stream` *bool, optional* - Whether to stream the response. Defaults to False
* `images` *list\[str], optional* - List of image URLs for multimodal models
* `max_tokens` *int, optional* - The maximum number of tokens to generate
* `logprobs` *int, optional* - Number of log probabilities to return
* `echo` *bool, optional* - Whether to echo the prompt in the response
* `temperature` *float, optional* - Sampling temperature between 0 and 2. If not provided, uses the LLM's default temperature
* `top_p` *float, optional* - Nucleus sampling parameter
* `top_k` *int, optional* - Top-k sampling parameter (must be between 0 and 100)
* `frequency_penalty` *float, optional* - Frequency penalty for repetition
* `presence_penalty` *float, optional* - Presence penalty for repetition
* `repetition_penalty` *float, optional* - Repetition penalty
* `reasoning_effort` *str, optional* - How much effort the model should put into reasoning
* `mirostat_lr` *float, optional* - Mirostat learning rate
* `mirostat_target` *float, optional* - Mirostat target entropy
* `n` *int, optional* - Number of completions to generate
* `ignore_eos` *bool, optional* - Whether to ignore end-of-sequence tokens
* `stop` *str or list\[str], optional* - Stop sequences
* `response_format` *dict, optional* - An object specifying the format that the model must output
* `context_length_exceeded_behavior` *str, optional* - How to handle context length exceeded
* `user` *str, optional* - User identifier
* `extra_headers` *dict, optional* - Additional headers to include in the request
* `**kwargs` - Additional parameters supported by the OpenAI API

**Returns:**

* `Completion` when `stream=False` (default)
* `Generator[Completion, None, None]` when `stream=True` (sync version)
* `AsyncGenerator[Completion, None]` when `stream=True` (async version)

```python  theme={null}
import asyncio
from fireworks import LLM

llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="auto"
)

# Synchronous usage
response = llm.completions.create(
    prompt="Hello, world!"
)
print(response.choices[0].text)

# Synchronous streaming
for chunk in llm.completions.create(
    prompt="Tell me a story",
    stream=True
):
    if chunk.choices[0].text:
        print(chunk.choices[0].text, end="")

# Asynchronous usage
async def main():
    response = await llm.completions.acreate(
        prompt="Hello, world!"
    )
    print(response.choices[0].text)

    # Async streaming
    async for chunk in llm.completions.acreate(
        prompt="Tell me a story",
        stream=True
    ):
        if chunk.choices[0].text:
            print(chunk.choices[0].text, end="")

asyncio.run(main())
```

### `chat.completions.create()` and `chat.completions.acreate()`

Creates a chat completion using the LLM. These methods are OpenAI compatible and follow the same interface as described in the [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat/create). Use `create()` for synchronous calls and `acreate()` for asynchronous calls.

**Note:** The Fireworks chat completions API includes additional request and response fields beyond the standard OpenAI API. See the [Fireworks Chat Completions API reference](/api-reference/post-chatcompletions) for the complete set of available parameters and response fields.

**Arguments:**

* `messages` *list* - A list of messages comprising the conversation so far
* `stream` *bool, optional* - Whether to stream the response. Defaults to False
* `response_format` *dict, optional* - An object specifying the format that the model must output
* `reasoning_effort` *str, optional* - How much effort the model should put into reasoning
* `max_tokens` *int, optional* - The maximum number of tokens to generate
* `temperature` *float, optional* - Sampling temperature between 0 and 2. If not provided, uses the LLM's default temperature. Note that temperature can also be set once during LLM instantiation if preferred
* `tools` *list, optional* - A list of tools the model may call
* `extra_headers` *dict, optional* - Additional headers to include in the request
* `**kwargs` - Additional parameters supported by the OpenAI API

**Returns:**

* `ChatCompletion` when `stream=False` (default)
* `Generator[ChatCompletionChunk, None, None]` when `stream=True` (sync version)
* `AsyncGenerator[ChatCompletionChunk, None]` when `stream=True` (async version)

For details on the `ChatCompletion` object structure, see the [OpenAI Chat Completion Object documentation](https://platform.openai.com/docs/api-reference/chat/object). For the `ChatCompletionChunk` object structure used in streaming, see the [OpenAI Chat Streaming documentation](https://platform.openai.com/docs/api-reference/chat-streaming/streaming).

```python  theme={null}
import asyncio
from fireworks import LLM

llm = LLM(
    model="accounts/fireworks/models/llama-v3p2-3b-instruct",
    deployment_type="auto"
)

# Synchronous usage
response = llm.chat.completions.create(
    messages=[
        {"role": "user", "content": "Hello, world!"}
    ]
)
print(response.choices[0].message.content)

# Synchronous streaming
for chunk in llm.chat.completions.create(
    messages=[
        {"role": "user", "content": "Tell me a story"}
    ],
    stream=True
):
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")

# Asynchronous usage
async def main():
    response = await llm.chat.completions.acreate(
        messages=[
            {"role": "user", "content": "Hello, world!"}
        ]
    )
    print(response.choices[0].message.content)

    # Async streaming
    async for chunk in await llm.chat.completions.acreate(
        messages=[
            {"role": "user", "content": "Tell me a story"}
        ],
        stream=True
    ):
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")

asyncio.run(main())
```

## Dataset

The `Dataset` class provides a convenient way to manage datasets for fine-tuning on Fireworks. It offers smart features like automatic naming and uploading of datasets. You do not instantiate a `Dataset` object directly. Instead, you create a `Dataset` object by using one of the class methods below.

**Properties:**

* `name` *str* - The full name of the dataset (e.g., `accounts/my-account/datasets/dataset-12345-my-data`)
* `id` *str* - The dataset identifier (e.g., `dataset-12345-my-data`)
* `url` *str* - The URL to view the dataset in the Fireworks dashboard

### `from_list()`

```python  theme={null}
@classmethod
from_list(data: list)
```

Creates a Dataset from a list of training examples. Each example should be compatible with OpenAI's chat completion format.

```python  theme={null}
from fireworks import Dataset

# Create dataset from a list of examples
examples = [
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"},
            {"role": "assistant", "content": "Paris."}
        ]
    }
]
dataset = Dataset.from_list(examples)
```

### `from_file()`

```python  theme={null}
@classmethod
from_file(path: str)
```

Creates a Dataset from a local JSONL file. The file should contain training examples in OpenAI's chat completion format.

```python  theme={null}
from fireworks import Dataset

# Create dataset from a JSONL file
dataset = Dataset.from_file("path/to/training_data.jsonl")
```

### `from_string()`

```python  theme={null}
@classmethod
from_string(data: str)
```

Creates a Dataset from a string containing JSONL-formatted training examples.

```python  theme={null}
from fireworks import Dataset

# Create dataset from a JSONL string
jsonl_data = """
{"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there!"}]}
{"messages": [{"role": "user", "content": "What is 1+1?"}, {"role": "assistant", "content": "2"}]}
"""
dataset = Dataset.from_string(jsonl_data)
```

### `from_id()`

```python  theme={null}
@classmethod
from_id(id: str)
```

Creates a Dataset from an existing dataset ID on Fireworks.

```python  theme={null}
from fireworks import Dataset

# Create dataset from existing ID
dataset = Dataset.from_id("existing-dataset-id")
```

### `sync()`

Uploads the dataset to Fireworks if it doesn't already exist. This method automatically:

1. Checks if a dataset with the same content hash already exists
2. If it exists, skips the upload to avoid duplicates
3. If it doesn't exist, creates and uploads the dataset to Fireworks
4. Validates the dataset after upload

```python  theme={null}
from fireworks import Dataset

# Create dataset and sync it to Fireworks
dataset = Dataset.from_file("path/to/training_data.jsonl")
dataset.sync()

# The dataset is now available on Fireworks and ready for fine-tuning
```

### `delete()`

Deletes the dataset from Fireworks.

```python  theme={null}
dataset = Dataset.from_file("path/to/training_data.jsonl")
dataset.delete()
```

### `head(n: int = 5, as_dataset: bool = False)`

Returns the first n rows of the dataset.

**Arguments:**

* `n` *int, optional* - Number of rows to return. Defaults to 5.
* `as_dataset` *bool, optional* - If True, return a Dataset object; if False, return a list. Defaults to False.

**Returns:**

* *list or Dataset* - List of dictionaries if as\_dataset=False, Dataset object if as\_dataset=True

```python  theme={null}
# Get first 5 rows as a list
first_5_rows = dataset.head(5)

# Get first 10 rows as a new dataset
first_10_dataset = dataset.head(10, as_dataset=True)
```

### `create_evaluation_job(reward_function: Callable, samples: Optional[int] = None)`

Creates an evaluation job using a reward function for this dataset.

**Arguments:**

* `reward_function` *Callable* - A callable decorated with @reward\_function
* `samples` *int, optional* - Optional number of samples to evaluate (creates a subset dataset)

**Returns:**

* *EvaluationJob* - The created evaluation job

```python  theme={null}
from fireworks import reward_function

@reward_function
def my_reward_function(response, context):
    # Your reward logic here
    return 1.0

evaluation_job = dataset.create_evaluation_job(my_reward_function, samples=100)
```

### `preview_evaluator(reward_function: Callable, samples: Optional[int] = None)`

Previews the evaluator for the dataset.

**Arguments:**

* `reward_function` *Callable* - A callable decorated with @reward\_function
* `samples` *int, optional* - Optional number of samples to preview

**Returns:**

* *SyncPreviewEvaluatorResponse* - Preview response from the evaluator

```python  theme={null}
preview_response = dataset.preview_evaluator(my_reward_function, samples=10)
```

### Data Format

The Dataset class expects data in OpenAI's chat completion format. Each training example should be a JSON object with a `messages` array containing message objects. Each message object should have:

* `role`: One of `"system"`, `"user"`, or `"assistant"`
* `content`: The message content as a string

Example format:

```json  theme={null}
{
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "Paris."}
    ]
}
```

## SupervisedFineTuningJob

The `SupervisedFineTuningJob` class manages fine-tuning jobs on Fireworks. It provides a convenient interface for creating, monitoring, and managing fine-tuning jobs.

```python  theme={null}
class SupervisedFineTuningJob()
```

**Properties:**

* `output_model` *str* - The identifier of the output model (e.g., `accounts/my-account/models/my-finetuned-model`)
* `output_llm` *LLM* - An LLM instance associated with the output model
* `id` *str* - The job ID
* `display_name` *str* - The display name of the job
* `name` *str* - The full name of the job
* `url` *str* - The URL to view the job in the Fireworks dashboard

### Instantiation

You do not need to directly instantiate a `SupervisedFineTuningJob` object. Instead, you should use the `.create_supervised_fine_tuning_job()` method on the `LLM` object and pass in the following required and optional arguments.

#### Required Arguments

* `display_name` *str* - A unique name for the fine-tuning job. Must only contain lowercase a-z, 0-9, and hyphen (-).
* `dataset_or_id` *Union\[Dataset, str]* - The dataset to use for fine-tuning, either as a Dataset object or dataset ID

#### Optional Arguments

**Training Configuration**

* `epochs` *int, optional* - Number of training epochs
* `learning_rate` *float, optional* - Learning rate for training
* `lora_rank` *int, optional* - Rank for LoRA fine-tuning
* `jinja_template` *str, optional* - Template for formatting training examples
* `early_stop` *bool, optional* - Whether to enable early stopping
* `max_context_length` *int, optional* - Maximum context length for the model
* `base_model_weight_precision` *str, optional* - Precision for base model weights
* `batch_size` *int, optional* - Batch size for training

**Hardware Configuration**

* `accelerator_type` *str, optional* - Type of GPU accelerator to use
* `accelerator_count` *int, optional* - Number of accelerators to use
* `is_turbo` *bool, optional* - Whether to use turbo mode for faster training
* `region` *str, optional* - Region for deployment
* `nodes` *int, optional* - Number of nodes to use

**Evaluation & Monitoring**

* `evaluation_dataset` *str, optional* - Dataset ID to use for evaluation
* `eval_auto_carveout` *bool, optional* - Whether to automatically carve out evaluation data
* `wandb_config` *WandbConfig, optional* - Configuration for Weights & Biases integration

**Job Management**

* `output_model` *str, optional* - The name of the output model to create. If not provided, it will be the same as the display\_name argument.

### `sync()`

Creates the job if it doesn't exist, otherwise returns the existing job. If previous job failed, deletes it and creates a new one.

**Returns:**

* *SupervisedFineTuningJob* - The synced job object

```python  theme={null}
job = job.sync()
```

### `wait_for_completion()`

Polls the job status until it is complete and returns the job object.

**Returns:**

* *SupervisedFineTuningJob* - The completed job object

```python  theme={null}
job = job.wait_for_completion()
```

### `await_for_completion()`

Asynchronously polls the job status until it is complete and returns the job object.

**Returns:**

* *SupervisedFineTuningJob* - The completed job object

```python  theme={null}
job = await job.await_for_completion()
```

### `delete()`

Deletes the job.

```python  theme={null}
job.delete()
```

### `adelete()`

Asynchronously deletes the job.

```python  theme={null}
await job.adelete()
```

## ReinforcementStep

The `ReinforcementStep` class represents a reinforcement learning training step.
It provides methods to monitor and manage the training process.

```python  theme={null}
class ReinforcementStep()
```

**Properties:**

* `state` *str* - The current state of the training job (e.g., "JOB\_STATE\_RUNNING", "JOB\_STATE\_COMPLETED")
* `output_model` *str* - The identifier of the output model (e.g., `accounts/my-account/models/my-improved-model`)
* `is_completed` *bool* - Whether the training job has completed successfully

### `get()`

Retrieves the current state of the training job from the server.

**Returns:**

* A `ReinforcementStep` object with updated state, or `None` if the job no longer exists

```python  theme={null}
# Get updated job status
updated_job = job.get()
if updated_job is None:
    print("Job was deleted")
else:
    print(f"Job state: {updated_job.state}")
```

### `raise_if_bad_state()`

Raises a `RuntimeError` if the job is in a failed, cancelled, or otherwise bad state. This is useful for error handling during training.

**Raises:**

* `RuntimeError` - If the job is in a bad state (failed, cancelled, expired, etc.)

```python  theme={null}
# Check for bad states during training
try:
    job.raise_if_bad_state()
except RuntimeError as e:
    print(f"Training failed: {e}")
```

### Usage Example

```python  theme={null}
import time
from fireworks import LLM, Dataset

# Create base model
llm = LLM(
    model="qwen2p5-7b-instruct",
    deployment_type="on-demand",
    id="my-base-deployment",
    enable_addons=True
)

# Apply deployment configuration to Fireworks
llm.apply()

# Generate rollouts and create dataset
# (This would be your rollout generation logic)
dataset = Dataset.from_list([
    {
        "samples": [
            {
                "messages": [
                    {"role": "user", "content": "What is 2+2?"},
                    {"role": "assistant", "content": "4"}
                ],
                "evals": {"score": 1.0}
            }
        ]
    }
])
dataset.sync()

# Perform reinforcement learning step
job = llm.reinforcement_step(
    dataset=dataset,
    output_model="my-improved-model-v1",
    epochs=1
)

# Monitor training progress
while not job.is_completed:
    job.raise_if_bad_state()
    print(f"Training state: {job.state}")
    time.sleep(10)
    job = job.get()
    if job is None:
        raise Exception("Job was deleted while waiting for completion")

print(f"Training completed! New model: {job.output_model}")

# Use the improved model
improved_llm = LLM(
    model=job.output_model,
    deployment_type="on-demand-lora",
    base_id=llm.deployment_id
)
improved_llm.apply()
```

### Iterative Reinforcement Learning Workflow

The `reinforcement_step` method is designed to support iterative reinforcement learning workflows. Here's a complete example showing how to perform multiple reinforcement learning steps:

```python  theme={null}
import asyncio
import time
import random
from fireworks import LLM, Dataset

# Initialize base model
base_model = LLM(
    model="qwen2p5-7b-instruct",
    deployment_type="on-demand",
    id="my-base-deployment",
    enable_addons=True  # Enable LoRA addons to only use one deployment for all steps
)

# Apply deployment configuration to Fireworks
base_model.apply()

# Number of reinforcement learning steps
num_steps = 5

# Iterative reinforcement learning loop
async def run_reinforcement_learning():
    for step in range(num_steps):
        print(f"Starting reinforcement learning step {step + 1}/{num_steps}")
        
        # Create deployment for current model snapshot
        if step == 0:
            # Use base model for first step
            model_snapshot = base_model
        else:
            # Use the improved model from previous step
            model_snapshot = LLM(
                model=f"accounts/my-account/models/my-improved-model-v{step}",
                deployment_type="on-demand-lora",
                base_id=base_model.deployment_id
            )
        
        # Ensure deployment is ready
        model_snapshot.apply()
        
        # Generate rollouts and rewards (your custom logic here)
        # This is where you would:
        # 1. Generate rollouts by calling the deployment's inference endpoint
        # 2. Evaluate responses and compute rewards locally
        dataset_rows = await generate_rollouts_and_rewards(
            model_snapshot,
            num_prompts=10,
            num_generations_per_prompt=8,
            concurrency=100
        )
        
        # Create dataset from dataset rows
        dataset = Dataset.from_list(dataset_rows)
        dataset.sync()
        
        # Perform reinforcement learning step
        job = model_snapshot.reinforcement_step(
            dataset=dataset,
            output_model=f"my-improved-model-v{step + 1}",
            epochs=1,
            learning_rate=1e-5,
            accelerator_count=1,
            accelerator_type="NVIDIA_A100_80GB"
        )
        
        # Wait for training completion
        while not job.is_completed:
            job.raise_if_bad_state()
            print(f"Training state: {job.state}")
            time.sleep(10)
            job = job.get()
            if job is None:
                raise Exception("Job was deleted while waiting for completion")
        
        print(f"Step {step + 1} completed! New model: {job.output_model}")
        
        # Clean up dataset
        dataset.delete()

    print("Reinforcement learning complete!")

# Run the async reinforcement learning workflow
asyncio.run(run_reinforcement_learning())

# Example rollout generation function with concurrent generation
async def generate_rollouts_and_rewards(llm, num_prompts=10, num_generations_per_prompt=8, concurrency=100):
    """
    Generate rollouts and compute rewards for the given model using concurrent generation.
    Each sample contains multiple generations for Policy Optimization.
    """
    semaphore = asyncio.Semaphore(concurrency)
    
    async def generate_single_response(prompt_id, generation_id):
        """Generate a single response for a given prompt."""
        async with semaphore:
            messages = [
                {"role": "user", "content": f"What is {prompt_id} + {prompt_id}?"}
            ]
            
            response = await llm.chat.completions.acreate(
                messages=messages,
                max_tokens=50,
                temperature=1.5,  # Higher temperature for more diverse responses
                n=1  # Generate one response at a time
            )
            
            assistant_message = response.choices[0].message.content
            
            # Compute reward for this generation
            if str(prompt_id + prompt_id) in assistant_message:
                reward = 1.0  # Correct answer
            else:
                reward = 0.0  # Incorrect answer
            
            return {
                "prompt_id": prompt_id,
                "generation_id": generation_id,
                "messages": messages + [{"role": "assistant", "content": assistant_message}],
                "evals": {"score": reward}
            }
    
    # Create all generation tasks concurrently
    coros = []
    for prompt_id in range(num_prompts):
        for generation_id in range(num_generations_per_prompt):
            coro = generate_single_response(prompt_id, generation_id)
            coros.append(coro)
    
    # Execute all generations concurrently
    print(f"Starting {len(coros)} concurrent generations...")
    num_completed = 0
    results = []
    
    for coro in asyncio.as_completed(coros):
        result = await coro
        results.append(result)
        num_completed += 1
        if num_completed % 10 == 0:
            print(f"Completed {num_completed}/{len(coros)} generations")
    
    # Group results by prompt_id to create dataset rows
    dataset_rows = []
    for prompt_id in range(num_prompts):
        prompt_generations = [r for r in results if r["prompt_id"] == prompt_id]
        sample_generations = [
            {
                "messages": gen["messages"],
                "evals": gen["evals"]
            }
            for gen in prompt_generations
        ]
        dataset_rows.append({
            "samples": sample_generations
        })
    
    return dataset_rows
```

This workflow demonstrates the iterative nature of reinforcement learning, where each step:

1. Uses the current model snapshot to generate rollouts
2. For each prompt, generates multiple responses (required for Policy Optimization)
3. Evaluates each response and computes rewards
4. Creates a dataset with the rollouts and rewards (each sample contains multiple generations)
5. Performs a reinforcement learning step to create an improved model

<Note>
  Each sample in the dataset must contain multiple trajectories for the same prompt. This is required for policy optimization to work.
</Note>

## BatchInferenceJob

The `BatchInferenceJob` class provides a convenient way to manage batch inference jobs on Fireworks. It allows you to perform bulk asynchronous inference on large datasets, reducing costs by up to 50%.

```python  theme={null}
class BatchInferenceJob()
```

**Properties:**

* `name` *str* - The full name of the batch inference job (e.g., `accounts/my-account/batchInferenceJobs/test-job-123`)
* `id` *str* - The job identifier (e.g., `test-job-123`)
* `model` *str* - The model used for inference
* `input_dataset_id` *str* - The input dataset identifier
* `output_dataset_id` *str* - The output dataset identifier
* `state` *str* - The current state of the job
* `created_by` *str* - Email of the user who created the job
* `create_time` *str* - Creation timestamp
* `update_time` *str* - Last update timestamp

### `create()`

```python  theme={null}
@staticmethod
create(
    model: str,
    input_dataset_id: str,
    output_dataset_id: Optional[str] = None,
    job_id: Optional[str] = None,
    display_name: Optional[str] = None,
    inference_parameters: Optional[dict] = None,
    api_key: Optional[str] = None,
) -> BatchInferenceJob
```

Creates a new batch inference job.

**Arguments:**

* `model` *str* - The model to use for inference (e.g., `llama-v3p1-8b-instruct` or `accounts/fireworks/models/llama-v3p1-8b-instruct`)
* `input_dataset_id` *str* - The input dataset ID containing JSONL formatted requests
* `output_dataset_id` *str, optional* - The output dataset ID. If not provided, one will be auto-generated
* `job_id` *str, optional* - The job ID. If not provided, one will be auto-generated
* `display_name` *str, optional* - Display name for the job
* `inference_parameters` *dict, optional* - Dict of inference parameters:
  * `max_tokens` *int* - Maximum number of tokens to generate
  * `temperature` *float* - Sampling temperature (0-2)
  * `top_p` *float* - Top-p sampling parameter
  * `top_k` *int* - Top-k sampling parameter
  * `n` *int* - Number of completions per request
  * `extra_body` *str* - Additional parameters as JSON string
* `api_key` *str, optional* - The API key to use

**Returns:**

* A `BatchInferenceJob` object

```python  theme={null}
from fireworks import BatchInferenceJob

# Create a batch inference job
job = BatchInferenceJob.create(
    model="llama-v3p1-8b-instruct",
    input_dataset_id="my-input-dataset",
    output_dataset_id="my-output-dataset",
    job_id="my-batch-job",
    display_name="My Batch Processing Job",
    inference_parameters={
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.9
    }
)
```

### `get()`

```python  theme={null}
@staticmethod
get(job_id: str, account: str, api_key: Optional[str] = None) -> Optional[BatchInferenceJob]
```

Retrieves a batch inference job by its ID.

**Arguments:**

* `job_id` *str* - The job ID or full resource name
* `account` *str* - Account ID
* `api_key` *str, optional* - The API key to use

**Returns:**

* A `BatchInferenceJob` object if found, `None` otherwise

```python  theme={null}
# Get an existing batch inference job
job = BatchInferenceJob.get(
    job_id="my-batch-job",
    account="my-account"
)

if job:
    print(f"Job state: {job.state}")
    print(f"Created by: {job.created_by}")
```

### `list()`

```python  theme={null}
@staticmethod
list(
    account: str,
    api_key: Optional[str] = None,
    page_size: int = 50
) -> list[BatchInferenceJob]
```

Lists batch inference jobs in an account.

**Arguments:**

* `account` *str* - Account ID
* `api_key` *str, optional* - The API key to use
* `page_size` *int, optional* - Number of jobs to return per page. Defaults to 50

**Returns:**

* A list of `BatchInferenceJob` objects

```python  theme={null}
# List all batch inference jobs
jobs = BatchInferenceJob.list(account="my-account")

for job in jobs:
    print(f"Job: {job.id}, State: {job.state}, Model: {job.model}")
```

### `delete()`

```python  theme={null}
@staticmethod
delete(job_id: str, account: str, api_key: Optional[str] = None) -> None
```

Deletes a batch inference job.

**Arguments:**

* `job_id` *str* - The job ID or full resource name
* `account` *str* - Account ID
* `api_key` *str, optional* - The API key to use

```python  theme={null}
# Delete a batch inference job
BatchInferenceJob.delete(
    job_id="my-batch-job",
    account="my-account"
)
```

### `to_dict()`

```python  theme={null}
@staticmethod
to_dict(proto: BatchInferenceJob) -> dict
```

Converts a batch inference job proto to a friendly dictionary representation.

**Arguments:**

* `proto` *BatchInferenceJob* - The batch inference job proto object

**Returns:**

* A dictionary with human-readable field values

```python  theme={null}
# Convert job to dictionary for easy viewing
job = BatchInferenceJob.get("my-batch-job", "my-account")
if job:
    job_dict = BatchInferenceJob.to_dict(job)
    print(job_dict)
    # Output:
    # {
    #     'name': 'accounts/my-account/batchInferenceJobs/my-batch-job',
    #     'display_name': 'My Batch Job',
    #     'model': 'accounts/fireworks/models/llama-v3p1-8b-instruct',
    #     'state': 'JOB_STATE_COMPLETED',
    #     'create_time': '2024-01-01 08:00:00 UTC',
    #     'inference_parameters': {'max_tokens': 1024, 'temperature': 0.7}
    # }
```
