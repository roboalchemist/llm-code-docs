# Source: https://docs.salad.com/container-engine/reference/recipes/tgi.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Text Generation Inference (TGI) API Recipes

> Deploy large language models with Text Generation Inference (TGI) API on Salad Container Engine.

*Last Updated: July 9, 2025*

<Tip>Deploy from the [SaladCloud Portal](https://portal.salad.com).</Tip>

## Overview

Inference is powered by [Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference), a
toolkit for deploying and serving Large Language Models (LLMs) developed by Hugging Face. TGI provides optimized
inference for text generation models with features like continuous batching, tensor parallelism, and efficient memory
management.

Several models are available, including:

* [Qwen 2.5 VL 3B Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) - A 3 billion parameter vision-language
  model for multimodal understanding and generation tasks.
* [Qwen 2.5 VL 7B Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) - A 7 billion parameter vision-language
  model with enhanced capabilities for complex multimodal tasks.
* [Qwen 3 8B](https://huggingface.co/Qwen/Qwen3-8B) - An 8 billion parameter language model with improved performance
  and efficiency.
* [Llama 3.1 8B Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) - Meta's 8 billion parameter
  instruction-tuned model for conversational AI and text generation.
* [Mistral 7B 0.3 Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) - Mistral AI's 7 billion
  parameter instruction-tuned model optimized for chat and reasoning tasks.
* [Llama 3.2 11B Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) - Meta's 11 billion
  parameter vision-language model for multimodal understanding and generation.
* **Custom Model** - Deploy any
  [TGI-compatible model](https://huggingface.co/docs/text-generation-inference/supported_models) by providing the model
  name via environment variable.

## Example request

Submit chat completion requests to the `/v1/chat/completions` endpoint, and receive generated text in response.

```shell  theme={null}
curl -X POST https://vegetable-words-3e487ysdyhfkvjah.salad.cloud/v1/chat/completions \
-H "Content-Type: application/json" \
-H "Salad-Api-Key: <YOUR_API_KEY>" \
-d @request.json
```

```json request.json theme={null}
{
  "model": "tgi",
  "messages": [
    {
      "role": "user",
      "content": "Explain quantum computing in simple terms:"
    }
  ],
  "max_tokens": 200,
  "temperature": 0.7,
  "top_p": 0.95,
  "frequency_penalty": 0.1,
  "stream": false
}
```

You will get back a json response with the generated text:

```json  theme={null}
{
  "id": "chatcmpl-1234567890abcdef",
  "object": "chat.completion",
  "created": 1704067200,
  "model": "tgi",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Quantum computing is a revolutionary approach to computation that harnesses the principles of quantum mechanics..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 156,
    "total_tokens": 164
  }
}
```

## How To Use This Recipe

### Authentication

When deploying this recipe, you can optionally enable authentication in the container gateway. If you enable
authentication, all requests to your API will need to include your SaladCloud API key in the header `Salad-Api-Key`. See
the [documentation](/container-engine/how-to-guides/gateway/sending-requests) for more information about authentication.

### Replica Count

The recipe is configured for 3 replicas by default, and we recommend using at least 3 for testing, and at least 5 for
production workloads. SaladCloud's distributed GPU cloud is powered by idle gaming PCs around the world, in private
residences, gaming cafes, and esports arenas. A consequence of this unique infrastructure is that all nodes must be
considered interruptible without warning. If a 👨‍🍳 Chef (a compute host) decides they want to use their GPU to play a
video game, or their dog trips on the power cord, or their Wi-Fi goes out, the instance of your workload running on that
node will be interrupted, and a new instance will be allocated to a different node. This means you may want to slightly
over-provision the capacity you expect to need in order to have adequate coverage during node reallocations. Don't
worry, we only charge for instances that are actually running.

### Logging

SaladCloud offers a simple built-in method to view logs from the portal, to facilitate testing and development. For
production workloads, we highly recommend connecting an external logging source, such as Axiom. This can be done during
container group creation.

### Deploy It And Wait

When you deploy the recipe, SaladCloud will find the desired number of qualified nodes, and begin the process of
downloading the container image to the host machine. Depending on the preloaded model, the docker image can be quite
large (Up to 22GB), and it may take up to tens of minutes to download to some machines, depending on the network
conditions of that particular node. Remember, these are residential PCs with residential internet connections, and
performance will vary across different nodes.

Eventually, you will see instances enter the running state, and show a green checkmark in the "Ready" column, indicating
the workload is passing its readiness probe. Once at least 1 instance is running, the container group will be considered
running, but for production you will want to wait until an adequate number of nodes have become ready before moving
traffic over.

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-deploy.jpg?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=453f8f38b3c7ddc95051f3d5ae63c5f8" alt="" data-og-width="1233" width="1233" data-og-height="955" height="955" data-path="container-engine/images/tgi-deploy.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-deploy.jpg?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=f4229010a2dc225290e67020959ce79d 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-deploy.jpg?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=281f599a890e2667032f59c43511e7b7 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-deploy.jpg?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=e275483de8512c2c0345756b17518412 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-deploy.jpg?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=419aaf93a20daf0d0d4b64c65925693a 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-deploy.jpg?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=4184d12eab4c8e180b4ac8a2613fffc1 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/tgi-deploy.jpg?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=9583ebd2df8a48643460e9eddc41b359 2500w" />

You will find helpful links and information in the readme on the container group page once deployed.

## Source Code

[<Icon icon="github" size="24" /> Github Repository](https://github.com/SaladTechnologies/salad-recipes/tree/master/recipes/tgi)
