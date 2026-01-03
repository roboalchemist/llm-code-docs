# Source: https://docs.promptlayer.com/languages/integrations.md

# Integrations

PromptLayer works seamlessly with many popular LLM frameworks and abstractions.

Don't see the integration you are looking for? [Email us!](mailto:hello@promptlayer.com) 👋

## LangChain

Please read the [LangChain documentation page](/languages/langchain).

## LiteLLM

[LiteLLM](https://github.com/BerriAI/litellm) allows you to call any LLM API all using the OpenAI format. This is the easiest way to swap in and out new models and see which one works best for your prompts. Works with models such as Anthropic, HuggingFace, Cohere, PaLM, Replicate, Azure.

Please read the [LiteLLM documentation page](https://docs.litellm.ai/docs/observability/promptlayer_integration)

## LlamaIndex

[LlamaIndex](https://www.llamaindex.ai/) is a data framework for LLM-based applications. Read more about our integration on the [LlamaIndex documentation page](https://docs.llamaindex.ai/en/stable/module_guides/observability/observability.html#promptlayer)

## Hugging Face

PromptLayer supports integration with [Hugging Face](https://huggingface.co/models), allowing you to use any model available on Hugging Face within the platform. To set up:

1. Go to Settings
2. Navigate to the Hugging Face section
3. Click "Create New"

<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=9bf0067be9cc783f42e63359ed16c166" alt="huggingface" data-og-width="2886" width="2886" data-og-height="1300" height="1300" data-path="images/huggingface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=a0846f61c8c95117f5a43187fa3ac093 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=9ecf04cfe218079887dbe6a7b98b01e1 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=6c0befad5218c7d0bfed9b44bb6fc270 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=56a6fc5b33f3bde09ce50257d86613a2 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=f97ba93b301a482dd9246174ce3e604e 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=79360f2e1c50e6dfa5bb322638a45ec8 2500w" />
<img src="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface-add-model.png?fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=f37c03a31024c4be49ede72dfc6bcf51" alt="add model" data-og-width="1313" width="1313" data-og-height="1183" height="1183" data-path="images/huggingface-add-model.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface-add-model.png?w=280&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=d333da1208d67a80b90d8c41bec4d75d 280w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface-add-model.png?w=560&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=65d76172f0cdc5a88b788626abb7d714 560w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface-add-model.png?w=840&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=cd77a4cb29fd2eaa6ae4c6e7949c13cf 840w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface-add-model.png?w=1100&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=5890bcef07e9a8e2453b716fb6442025 1100w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface-add-model.png?w=1650&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=11fa5a526787e704931a58fdcf1fb486 1650w, https://mintcdn.com/promptlayer/4xCQDros0B-lHSut/images/huggingface-add-model.png?w=2500&fit=max&auto=format&n=4xCQDros0B-lHSut&q=85&s=551265b643f390dcec6b93c8717795ca 2500w" />

Once configured, you can use Hugging Face models throughout the platform, including:

* Prompt Registry
* Evaluations
* All other platform features

## Amazon Bedrock

PromptLayer supports integration with [Amazon Bedrock](https://aws.amazon.com/bedrock/), AWS's fully managed service for accessing foundation models. Amazon Bedrock provides access to models from leading AI companies including Anthropic, Cohere, Meta, and Amazon's own Titan models. To set up:

1. Go to Settings
2. Navigate to the Amazon Bedrock section
3. Enter your AWS Access Key ID
4. Enter your AWS Secret Access Key
5. Select your AWS Region (e.g., us-east-1, us-west-2)
6. Click "Save Bedrock Credentials"

Once configured, you can access a wide range of model families through Bedrock, including:

* **Anthropic Claude** models (Claude 3 Opus, Sonnet, Haiku, and Claude 2)
* **Amazon Titan** models (Titan Text, Titan Embeddings, Titan Image)
* **Meta Llama** models (Llama 2 and Llama 3 variants)
* **Cohere** models (Command and Embed)
* **Mistral AI** models (Mistral and Mixtral)
* And more as they become available on Bedrock

All Bedrock models are available throughout the platform, including:

* Prompt Registry for template management
* Evaluations for testing and comparison
* Playground for experimentation
* All other platform features

Note: Ensure your AWS IAM user has the necessary permissions to invoke Bedrock models in your selected region.

## Vertex AI

PromptLayer supports integration with [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai), allowing you to use both Google's foundation models and your own custom-deployed models.

### Standard Models

To set up Vertex AI for standard models:

1. Go to Settings
2. Navigate to the Vertex AI section
3. Enter your Vertex AI Project ID
4. Enter your Vertex AI Location (e.g., us-central1)
5. Attach your Vertex AI Security Credentials JSON file
6. Click "Save Vertex AI Credentials"

<img src="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/vertex-ai-configuration.png?fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=5a21ca46afe05f7828d87b75da6905e4" alt="vertex-ai-configuration" data-og-width="2226" width="2226" data-og-height="512" height="512" data-path="images/vertex-ai-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/vertex-ai-configuration.png?w=280&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=a6783f2041fce987d5a9b8763306cc17 280w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/vertex-ai-configuration.png?w=560&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=90695bafaf3cb2a5f3fdceb2236eef67 560w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/vertex-ai-configuration.png?w=840&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=89c53a65114ad20a9d18052f2e4bd508 840w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/vertex-ai-configuration.png?w=1100&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=200300a0cf126d85e0568ecaf5c9630c 1100w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/vertex-ai-configuration.png?w=1650&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=d2c0b8dfe5d4dde9e8360da4c015fb8b 1650w, https://mintcdn.com/promptlayer/v0RzaTvbzopITX7U/images/vertex-ai-configuration.png?w=2500&fit=max&auto=format&n=v0RzaTvbzopITX7U&q=85&s=51fdc283f403884ded72537003504469 2500w" />

Once configured, you can use Vertex AI foundation models including:

* Gemini models (gemini-pro, gemini-pro-vision, gemini-1.5-pro, etc.)
* Claude models (claude-3-sonnet, claude-3-haiku, claude-3-opus, etc.)
* PaLM models (text-bison, chat-bison, etc.)

### Custom Models

Vertex AI also supports deploying and using your own custom models. This allows you to:

* Deploy fine-tuned versions of foundation models
* Use models from Model Garden
* Deploy custom-trained models from your ML pipelines
* Access specialized domain-specific models

To use custom models:

1. Deploy your model to a Vertex AI endpoint in your project
2. In PromptLayer Settings, navigate to Custom Models
3. Click "Create Custom Model"
4. Select "Vertex AI" as the provider
5. Enter your model endpoint details:
   * **Endpoint ID**: The deployed model endpoint identifier
   * **Model Name**: The specific model version or identifier
   * **Display Name**: A friendly name for use in PromptLayer
6. Configure any model-specific parameters

Custom Vertex AI models are fully integrated with all platform features including Prompt Registry, Evaluations, and request tracking.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt