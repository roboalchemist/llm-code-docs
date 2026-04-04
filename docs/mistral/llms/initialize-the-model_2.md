# Initialize the model
llm = LLM(model="mistralai/Mistral-7B-Instruct-v0.3", dtype="bfloat16", max_model_len=20000, gpu_memory_utilization=0.9)

def run(prompt: str, temperature: float = 0.8, top_p: float = 0.75, top_k: int = 40, max_tokens: int = 256, frequency_penalty: int = 1):
  
    sampling_params = SamplingParams(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty
    )

    outputs = llm.generate([item.prompt], sampling_params)

    generated_text = []
    for output in outputs:
        generated_text.append(output.outputs[0].text)

    return {"result": generated_text}
```

## Run on the cloud

```bash
cerebrium deploy
```

You will see your application deploy, install pip packages and download the model. Once completed it will output a CURL request you can use to call your endpoint. Just remember to end
the url with the function you would like to call - in this case /run. 

```CURL
curl --location --request POST 'https://api.cortex.cerebrium.ai/v4/p-<YOUR PROJECT ID>/mistral-vllm/run' \
--header 'Authorization: Bearer <YOUR TOKEN HERE>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "prompt: "What is the capital city of France?"
}'
```

You should then get a message looking like this:

```json
{
  "run_id": "nZL6mD8q66u4lHTXcqmPCc6pxxFwn95IfqQvEix0gHaOH4gkHUdz1w==",
  "message": "Finished inference request with run_id: `nZL6mD8q66u4lHTXcqmPCc6pxxFwn95IfqQvEix0gHaOH4gkHUdz1w==`",
  "result": {
    "result": ["\nA: Paris"]
  },
  "status_code": 200,
  "run_time_ms": 151.24988555908203
}
```


[Deploy with Cloudflare Workers AI]
Source: https://docs.mistral.ai/docs/deployment/self-deployment/cloudflare

[Cloudflare](https://www.cloudflare.com/en-gb/) is a web performance and security company that provides content delivery network (CDN), DDoS protection, Internet security, and distributed domain name server services. Cloudflare launched Workers AI, which allows developers to run LLMs models powered by serverless GPUs on Cloudflare’s global network.

To learn more about Mistral models on Workers AI you can read the dedicated [Cloudflare documentation page](https://developers.cloudflare.com/workers-ai/models/mistral-7b-instruct-v0.1/).

## Set-up

To set-up Workers AI on Cloudflare, you need to create an account on the [Cloudflare dashboard](https://dash.cloudflare.com/), get your account ID, and generate a token with Workers AI permissions. You can then send a completion request:

<Tabs>
  <TabItem value="cloudflare-curl" label="curl" default>
  
  ```bash
  curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/mistral/mistral-7b-instruct-v0.1 \
    -X POST \
    -H "Authorization: Bearer {API_TOKEN}" \
    -d '{ "messages": [{ "role": "user", "content": "[INST] 2 + 2 ? [/INST]" }]}'
  ```
  </TabItem>
  <TabItem value="cloudflare-node" label="typescript">

  ```typescript
  async function run(model, prompt) {
    const messages = [
      { role: "user", content: prompt },
    ];

    const response = await fetch(
      `https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/${model}`,
      {
        headers: { Authorization: "Bearer {API_TOKEN}" },
        method: "POST",
        body: JSON.stringify({ messages }),
      }
    );
    const result = await response.json();
    return result;
  }

  run("@cf/mistral/mistral-7b-instruct-v0.1", "[INST] 2 + 2 ? [/INST]").then(
    (response) => {
      console.log(JSON.stringify(response));
    }
  );
  ```
  </TabItem>

  <TabItem value="cloudflare-python" label="python">
  
  ```python
  import requests

  API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/"
  headers = {"Authorization": "Bearer {API_TOKEN}"}

  def run(model, prompt):
    input = {
      "messages": [
        { "role": "user", "content": prompt }
      ]
    }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

  output = run("@cf/mistral/mistral-7b-instruct-v0.1", "[INST] 2 + 2 = ? [/INST]")
  print(output)
  ```
  </TabItem>
</Tabs>

Here is the output you should receive

```python
{'result': {'response': '2 + 2 = 4.'}, 'success': True, 'errors': [], 'messages': []}
```


[Self-deployment]
Source: https://docs.mistral.ai/docs/deployment/self-deployment/overview

Mistral AI models can be self-deployed on your own infrastructure through various
inference engines. We recommend using [vLLM](https://vllm.readthedocs.io/), a
highly-optimized Python-only serving framework which can expose an OpenAI-compatible
API.

Other inference engine alternatives include 
[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) and
[TGI](https://huggingface.co/docs/text-generation-inference/index).

You can also leverage specific tools to facilitate infrastructure management, such as 
[SkyPilot](https://skypilot.readthedocs.io) or [Cerebrium](https://www.cerebrium.ai).


[Deploy with SkyPilot]
Source: https://docs.mistral.ai/docs/deployment/self-deployment/skypilot

[SkyPilot](https://skypilot.readthedocs.io/en/latest/) is a framework for running LLMs, AI, and batch jobs on any cloud, offering maximum cost savings, highest GPU availability, and managed execution.

We provide an example SkyPilot config that deploys our models.

## SkyPilot Configuration

After [installing SkyPilot](https://skypilot.readthedocs.io/en/latest/getting-started/installation.html), you need to create a configuration file that tells SkyPilot how and where to deploy your inference server, using our pre-built docker container:
<Tabs>
  <TabItem value="mistral7b" label="Mistral-7B" default>

```yaml
resources: 
  cloud: ${CLOUD_PROVIDER}
  accelerators: A10G:1
  ports: 
    - 8000

run: |
  docker run --gpus all -p 8000:8000 ghcr.io/mistralai/mistral-src/vllm:latest \
                   --host 0.0.0.0 \
                   --model mistralai/Mistral-7B-Instruct-v0.2 \
                   --tensor-parallel-size 1
```

  </TabItem>
  <TabItem value="mixtral8x7b" label="Mixtral-8X7B">

```yaml
resources: 
  cloud: ${CLOUD_PROVIDER}
  accelerators: A100-80GB:2
  ports: 
    - 8000

run: |
  docker run --gpus all -p 8000:8000 ghcr.io/mistralai/mistral-src/vllm:latest \
                   --host 0.0.0.0 \
                   --model mistralai/Mixtral-8x7B-Instruct-v0.1 \
                   --tensor-parallel-size 2
```

  </TabItem>
  <TabItem value="mixtral8x22b" label="Mixtral-8X22B">

```yaml
resources: 
  cloud: ${CLOUD_PROVIDER}
  accelerators: A100-80GB:4
  ports: 
    - 8000

run: |
  docker run --gpus all -p 8000:8000 ghcr.io/mistralai/mistral-src/vllm:latest \
                   --host 0.0.0.0 \
                   --model mistralai/Mixtral-8x22B-Instruct-v0.1 \
                   --tensor-parallel-size 4
```

  </TabItem>
</Tabs>
Once these environment variables are set, you can use `sky launch` to launch the inference 
server with the appropriate model name, for example with `mistral-7b`:

```bash
sky launch -c mistral-7b mistral-7b-v0.1.yaml --region us-east-1
```

:::caution

When deployed that way, the model will be accessible to the whole world. You **must** secure it, either by exposing it exclusively on your private network (change the `--host` Docker option for that), by adding a load-balancer with an authentication mechanism in front of it, or by configuring your instance networking properly.

:::

### Test it out!

To easily retrieve the IP address of the deployed `mistral-7b` cluster you can use:

```bash
sky status --ip mistral-7b
```

You can then use curl to send a completion request:

```
IP=$(sky status --ip cluster-name)

curl http://$IP:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
      "model": "mistralai/Mistral-7B-v0.1",
      "prompt": "My favourite condiment is",
      "max_tokens": 25
  }'
```


## Usage Quotas

Many cloud providers require you to explicitly request access to powerful GPU instances. Read [SkyPilot's guide](https://skypilot.readthedocs.io/en/latest/cloud-setup/quota.html) on how to do this.


[Text Generation Inference]
Source: https://docs.mistral.ai/docs/deployment/self-deployment/tgi

Text Generation Inference (TGI) is a toolkit for deploying and serving Large Language Models (LLMs). TGI enables high-performance text generation for the most popular open-access LLMs. Among other features, it has quantization, tensor parallelism, token streaming, continuous batching, flash attention, guidance, and more.

The easiest way of getting started with TGI is using the official Docker container.

## Deploying

<Tabs>
  <TabItem value="mistral7b" label="Mistral-7B" default>

```bash
model=mistralai/Mistral-7B-Instruct-v0.3
```

  </TabItem>
  <TabItem value="mixtral8x7b" label="Mixtral-8X7B">

```bash
model=mistralai/Mixtral-8x22B-Instruct-v0.1
```

  </TabItem>
  <TabItem value="mixtral8x22b" label="Mixtral-8X22B">

```bash
model=mistralai/Mixtral-8x22B-Instruct-v0.1
```

  </TabItem>
</Tabs>

```bash
volume=$PWD/data # share a volume with the Docker container to avoid downloading weights every run
docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data  \
    -e HUGGING_FACE_HUB_TOKEN=$HUGGING_FACE_HUB_TOKEN \
    ghcr.io/huggingface/text-generation-inference:2.0.3 \
    --model-id $model
```

This will spawn a TGI instance exposing an OpenAI-like API, as documented in the [API section](/api).  

Make sure to set the `HUGGING_FACE_HUB_TOKEN` environment variable to your [Hugging Face user access token](https://huggingface.co/docs/hub/security-tokens). To use Mistral models, you must first visit the corresponding model page and fill out the small form. You then automatically get access to the model.

If the model does not fit in your GPU, you can also use quantization methods (AWQ, GPTQ, etc.). You can find all TGI launch options at [their documentation](https://huggingface.co/docs/text-generation-inference/en/basic_tutorials/launcher). 

## Using the API


### With chat-compatible endpoint

TGI supports the [Messages API](https://huggingface.co/docs/text-generation-inference/en/messages_api) which is compatible with Mistral and OpenAI Chat Completion API.

<Tabs>
  <TabItem value="mistralclient" label="Using MistralClient" default>

```python
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage