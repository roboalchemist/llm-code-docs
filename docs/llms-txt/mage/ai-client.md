# Source: https://docs.mage.ai/ai/ai-client.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.mage.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Clients

> Use and enable different AI clients.

## AI Client

You now have the option to select from various AI clients to harness
[the capabilities of Mage AI](https://docs.mage.ai/guides/ai/overview), as detailed in the
Mage AI capabilities documentation. Currently, we offer support for OpenAI and Hugging Face,
with the promise of additional AI clients being added in the future.

## Use Hugging Face Client

### Setup

#### Hugging Face Inference Endpoint

In order to utilize the Hugging Face AI Client, it is necessary to establish a Hugging Face inference endpoint.
You can set it up following [this guide](https://huggingface.co/inference-endpoints).

This process is quite straightforward. It entails

* selecting the specific model you wish to use,
* determining the hosting environment (AWS or Azure),
* specifying the geographical region,
* choosing the type of GPU.

For your convenience and based on our testing, we recommend using the
"mistralai/Mistral-7B-Instruct-v0.1" model.

Once the Inference endpoint is operational, it will provide you with an API URL and a corresponding
token for establishing a secure connection.

#### Mage Project Setup

Within your Mage project's metadata YAML configuration, please include the subsequent "ai\_config" section:

```
ai_config:
  mode: 'hugging_face'
  open_ai_config:
    openai_api_key: key
  hugging_face_config:
    huggingface_api: api_url
    huggingface_inference_api_token: api_token
```

The "mode" parameter determines your selection of the AI client to be employed.
It can be specified as either "open\_ai" or "hugging\_face," with the default value being set to "open\_ai."

"hugging\_face\_config" as a mandatory configuration if you choose to use the hugging face client.
This configuration includes the two essential elements obtained from the Hugging Face inference
endpoint, namely, the API and Token.

You are ready to go once the "ai\_config" is setup. At this point,
you can fully leverage Mage AI's capabilities, such as generating blocks
with text description, automatically write comments for your functions, etc.

## How to add a new AI Client

You may find it necessary to employ an AI client other than those offered by OpenAI and Hugging Face.
Additionally, you might wish to make direct calls to your Language Model (LLM).
This can be accomplished by enabling a new AI client for your specific needs.

This is an [example PR](https://github.com/mage-ai/mage-ai/pull/3850).

### Create new AI config

Create a dedicated configuration to save the params required to connect to LLM in the [config.py](https://github.com/mage-ai/mage-ai/blob/92c372b24e08148863d799d9afcdd44483c11c89/mage_ai/orchestration/ai/config.py#L19).
For instance, when using the Hugging Face client, the LLM is hosted within the
inference endpoint, mandating both the API and Token for invoking the service
for inference. In the OpenAI client, the OpenAI key is required to facilitate model inference.

### Create dedicated AI Client

Inherit the [AIClient interface](https://github.com/mage-ai/mage-ai/blob/master/mage_ai/ai/ai_client.py)
and implements the two required functions: “inference\_with\_prompt” and “find\_block\_params”.

* Inference\_with\_prompt function does the LLM model inference.
  It takes the prompt template, required variables being used in the prompt and
  return the inference result.
* Find\_block\_params function does a multi classification based on code description
  to generate required types including block\_type, pipeline\_type, language,
  action type and data source.

You can read your configuration in the Setup function and initialize the client
to talk to your service.

### Enable in llm\_pipeline\_wizard

The last action to take is modifying the Setup function within "[mage\_ai/ai/llm\_pipeline\_wizard.py](https://github.com/mage-ai/mage-ai/blob/92c372b24e08148863d799d9afcdd44483c11c89/mage_ai/ai/llm_pipeline_wizard.py#L195)"
to introduce a new mode of your client and initialize your AI client.


Built with [Mintlify](https://mintlify.com).