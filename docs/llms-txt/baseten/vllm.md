# Source: https://docs.baseten.co/examples/vllm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Run any LLM with vLLM

> Serve a wide range of models

Another great option for inference is [vLLM](https://docs.vllm.ai/), which supports a wide range of models and performance optimizations.

## Example: Deploy Qwen 2.5 3B on an L4

This configuration serves [Qwen 2.5 3B](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct) with vLLM on an L4 GPU. Running this model is fast and cheap, making it a good example for documentation, but the process of deploying it is very similar to larger models like [Llama 3.3 70B](/examples/models/llama/llama-3.3-70B-instruct).

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
    Some models require that you accept terms and conditions on HuggingFace before deployment. To prevent issues:

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

```sh  theme={"system"}
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
