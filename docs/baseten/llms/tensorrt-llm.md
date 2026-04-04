# Source: https://docs.baseten.co/examples/tensorrt-llm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Fast LLMs with TensorRT-LLM

> Optimize LLMs for low latency and high throughput

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

    ```sh  theme={"system"}
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

    ```sh  theme={"system"}
    pip install --upgrade truss openai
    ```
  </Step>
</Steps>

## Configuration

Start with an empty configuration file.

```sh  theme={"system"}
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

```sh  theme={"system"}
truss push qwen-2-5-3b-engine --publish
```

Upon deployment, check your terminal logs or Baseten account to find the URL for the model server.

## Inference

This model is OpenAI compatible and can be called using the OpenAI client.

```python  theme={"system"}
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
