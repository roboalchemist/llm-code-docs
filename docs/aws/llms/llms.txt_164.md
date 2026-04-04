# Source: https://docs.aws.amazon.com/bedrock/latest/userguide/llms.txt

# Amazon Bedrock User Guide

> User Guide for the Amazon Bedrock service.

- [Overview](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Quickstart](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html)
- [AWS Glossary](https://docs.aws.amazon.com/bedrock/latest/userguide/glossary.html)

## [Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models.html)

### [Availability & Compatibility](https://docs.aws.amazon.com/bedrock/latest/userguide/model-availability-compatibility.html)

View model availability across AWS Regions and compatibility with Amazon Bedrock APIs and endpoints.

- [API compatibility](https://docs.aws.amazon.com/bedrock/latest/userguide/models-api-compatibility.html): Amazon Bedrock supports three families of runtime APIs, each designed for different integration patterns and use cases.
- [Endpoint availability](https://docs.aws.amazon.com/bedrock/latest/userguide/models-endpoint-availability.html): Amazon Bedrock supports two endpoints: bedrock-runtime and bedrock-mantle.
- [Regional availability](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html): Amazon Bedrock gives you three options so you can match the routing behavior of your inference calls to the scale, compliance, and cost requirements of your workload.

### [Detailed model information](https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models-reference.html)

A foundation model is an Artificial Intelligence model with a large number of parameters and trained on a massive amount of diverse data.

- [Get model information](https://docs.aws.amazon.com/bedrock/latest/userguide/models-get-info.html): In the Amazon Bedrock console, you can find overarching information about Amazon Bedrock foundation model providers and the models they provide in the Providers and Base models sections.
- [Supported models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html): The table below lists information for foundation models supported by Amazon Bedrock.
- [Model support by Region](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html): This section shows model compatibility with different AWS Regions.
- [Feature support by Region](https://docs.aws.amazon.com/bedrock/latest/userguide/features-regions.html): This section shows Amazon Bedrock feature compatibility for different AWS Regions.
- [Model support by feature](https://docs.aws.amazon.com/bedrock/latest/userguide/models-features.html): This section shows model compatibility with different features in Amazon Bedrock.

### [Model inference parameters and responses](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html)

Learn about the request parameters and response fields for each of the models that Amazon Bedrock supports.

- [Amazon Nova models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-nova.html): Amazon Nova multimodal understanding models are available for use for inferencing through the Invoke API (InvokeModel, InvokeModelWithResponseStream) and the Converse API (Converse and ConverseStream).

### [Amazon Titan models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan.html)

Learn about Amazon Titan models in Amazon Bedrock, including text generation, image generation, and embedding models with their request parameters and response fields.

- [Amazon Titan Text models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-text.html): The Amazon Titan Text models support the following inference parameters.
- [Amazon Titan Image Generator G1 models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-image.html): The Amazon Titan Image Generator G1 V1 and Titan Image Generator G1 V2 models support the following inference parameters and model responses when carrying out model inference.
- [Amazon Titan Embeddings G1 - Text](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-text.html): Titan Embeddings G1 - Text does not support the use of inference parameters.
- [Amazon Titan Multimodal Embeddings G1](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-titan-embed-mm.html): This section provides request and response body formats and code examples for using Amazon Titan Multimodal Embeddings G1.

### [AnthropicÂ Claude models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-claude.html)

This section describes the request parameters and response fields for AnthropicÂ Claude models.

- [AnthropicÂ Claude Text Completions API](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-text-completion.html): This section provides inference parameters and code examples for using Anthropic Claude models with the Text Completions API.

### [AnthropicÂ Claude Messages API](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages.html)

This section provides inference parameters and code examples for using the Anthropic Claude Messages API.

- [Tool use](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-tool-use.html): Learn how to use Anthropic Claude models with tools to enhance responses and automate tasks through API integration.
- [Extended thinking](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html): Learn how to use Anthropic Claude's extended thinking capabilities for complex reasoning tasks, with step-by-step thought processes and enhanced problem-solving abilities.
- [Adaptive thinking](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-adaptive-thinking.html): Learn how to use Anthropic Claude's adaptive thinking capabilities, which dynamically decides when and how much to think based on request complexity.
- [Thinking encryption](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-thinking-encryption.html): Full thinking content is encrypted and returned in the signature field.
- [Differences in thinking across model versions](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-thinking-differences.html): Understand the key differences in extended thinking capabilities between Anthropic Claude 3.7 Sonnet and Claude 4 models, including output format and redaction handling.
- [Compaction](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-compaction.html): Learn how to use Anthropic Claude's compaction feature to automatically summarize context in long-running conversations and agentic workflows.
- [Structured Outputs](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-structured-outputs.html): Learn about structured outputs support for Anthropic Claude models.
- [Request and Response](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-request-response.html): The request body is passed in the body field of a request to InvokeModel or InvokeModelWithResponseStream.
- [Code examples](https://docs.aws.amazon.com/bedrock/latest/userguide/api-inference-examples-claude-messages-code-examples.html): The following code examples show how to use the messages API.
- [Supported models](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-supported-models.html): You can use the Messages API with the following Anthropic Claude models.

### [AI21 Labs models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-ai21.html)

This section describes the request parameters and response fields for AI21 Labs models.

- [AI21 LabsÂ Jurassic-2 models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-jurassic2.html): This section provides inference parameters and a code example for using AI21 Labs AI21 Labs Jurassic-2 models.
- [AI21 Labs Jamba models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-jamba.html): This section provides inference parameters and a code example for using AI21 Labs Jamba models.

### [Cohere models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-cohere.html)

This section describes the request parameters and response fields for Cohere models.

- [CohereÂ Command models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-cohere-command.html): Learn about Cohere Command models in Amazon Bedrock, including request parameters, response fields, and how to make inference calls for text generation.

### [CohereÂ Embed and Cohere Embed v4 models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-embed.html)

You make inference requests to an Embed model with InvokeModel You need the model ID for the model that you want to use.

- [Cohere Embed v4](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-embed-v4.html): Cohere Embed v4 is a multimodal embedding model that supports both text and image inputs.
- [Cohere Embed v3](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-embed-v3.html)
- [CohereÂ Command R and Command R+ models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-cohere-command-r-plus.html): Learn how to use Cohere Command R and Command R+ models for inference requests with detailed parameter options and response handling.
- [DeepSeek models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-deepseek.html): DeepSeekâs R1 and V3.1 models are text-to-text models available for use for inferencing through the Invoke API (InvokeModel, InvokeModelWithResponseStream) and the Converse API (Converse and ConverseStream).
- [Luma AI models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-luma.html): Learn about Luma AI models in Amazon Bedrock, including request parameters, response fields, and how to make inference calls for text-to-video generation.
- [MetaÂ Llama models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-meta.html): This section describes the request parameters and response fields for MetaÂ Llama models.

### [Mistral AI models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-mistral.html)

This section describes the request parameters and response fields for Mistral AI models.

- [Mistral AI text completion](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-mistral-text-completion.html): Learn how to use Mistral AI models in Amazon Bedrock for text completion, including request parameters, response fields, and formatting prompts for optimal results.
- [Mistral AI chat completion](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-mistral-chat-completion.html): The Mistral AI chat completion API lets create conversational applications.
- [Mistral AI Large (24.07) parameters and inference](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-mistral-large-2407.html): The Mistral AI chat completion API lets you create conversational applications.
- [Pixtral Large (25.02) parameters and inference](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-mistral-pixtral-large.html): Learn about Mistral AI Pixtral Large (25.02), a multimodal model combining image understanding with text processing capabilities for document analysis and interpretation.
- [OpenAI models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-openai.html): OpenAI offers the following open-weight models:

### [Stability AI models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-stability-diffusion.html)

Learn about Stability AI models in Amazon Bedrock, including Stable Diffusion XL, Stable Image Core, and Stable Image Ultra for text-to-image and image-to-image generation.

- [Stable Image Ultra](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-diffusion-stable-ultra-text-image-request-response.html): The request body is passed in the body field of a request to InvokeModel operation.
- [Stable Diffusion 3.5 Large](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-diffusion-3-5-large.html): The Stable Diffusion 3.5 Large model uses 8 billion parameters and supports 1 megapixel resolution output for text-to-image and image-to-image generation.
- [Stable Image Core](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-diffusion-stable-image-core-text-image-request-response.html): The request body is passed in the body field of a request to InvokeModel.
- [Stability AI Image Services](https://docs.aws.amazon.com/bedrock/latest/userguide/stable-image-services.html): You can use Stability AI Image Services with Amazon Bedrock to access thirteen specialized image editing tools designed to accelerate professional creative workflows.

### [TwelveLabs models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-twelvelabs.html)

Learn about TwelveLabs models in Amazon Bedrock, including video understanding and embedding models with their request parameters and response fields.

- [TwelveLabs Pegasus 1.2](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-pegasus.html): The TwelveLabs Pegasus 1.2 model provides comprehensive video understanding and analysis capabilities.
- [TwelveLabs Marengo Embed 2.7](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-marengo.html): The TwelveLabs Marengo Embed 2.7 model generates embeddings from video, text, audio, or image inputs.
- [TwelveLabs Marengo Embed 3.0](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-marengo-3.html): The TwelveLabs Marengo Embed 3.0 model generates enhanced embeddings from video, text, audio, or image inputs.

### [Writer AI Palmyra models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-writer-palmyra.html)

This section describes the request parameters and response fields for Writer AI models.

- [Writer Palmyra X4](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-palmyra-x4.html): Writer Palmyra X4 is a model with a context window of up to 128,000 tokens.
- [Writer Palmyra X5](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-palmyra-x5.html): Writer Palmyra X5 includes a suite of enterprise-ready capabilities, including advanced reasoning, tool-calling, LLM delegation, built-in RAG, code generation, structured outputs, multi-modality, and multi-lingual support.
- [Model lifecycle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html): Learn how the model lifecycle works with Amazon Bedrock.

### [Request access to models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)

Learn how to add, manage, and remove model access to Amazon Bedrock base and custom models.

- [Subscribe from Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-product-ids.html): See a list of product ID condition keys to control access to some Amazon Bedrock serverless foundation models.

### [Manage subscriptions with License Manager](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements.html)

Learn how to centrally manage third-party Bedrock model subscriptions and distribute access across your AWS Organization.

- [Workflow overview](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-workflow.html): Step 1 - Subscribe: Subscribe to a third-party Bedrock serverless model through AWS Marketplace (either via auto-enablement or private offer).
- [Key concepts](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-key-concepts.html)
- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-prerequisites.html): Before you can use managed entitlements for Amazon Bedrock, you must complete the following prerequisites.
- [Setup](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-setup.html): Complete the following setup steps once for your AWS Organization.
- [Subscribing](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-subscribing.html): Before you can distribute licenses, you must first subscribe to a Bedrock model through AWS Marketplace.
- [Distributing licenses](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-distributing.html): After you have subscribed to a third-party Bedrock model and verified that a license has been created, you can create grants to distribute access to other accounts in your organization.
- [Accepting and activating grants](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-accepting.html): After a grant has been distributed to a member account, the grant must be accepted and activated before the third-party Bedrock model can be used.
- [Using models](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-using-models.html): Once a grant has been activated in your account, you can invoke the third-party Bedrock model using the Amazon Bedrock console, AWS CLI, or AWS SDKs.
- [Managing grants](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-managing.html): After creating grants, you may need to modify, deactivate, or delete them based on changing organizational needs.
- [API Reference](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-api.html): This section provides comprehensive API documentation for programmatically managing Managed Entitlements for Bedrock.
- [Troubleshooting](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-troubleshooting.html): This section provides solutions to common issues you may encounter when using Managed Entitlements for Amazon Bedrock.
- [FAQ](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-faq.html)

### [Reranker models](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html)

Learn how to use reranker models in Amazon Bedrock to improve the relevance of query responses.

- [Supported Regions/models](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank-supported.html): Learn which AWS Regions and models Amazon Bedrock supports for reranking.
- [Permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank-prereq.html): Learn about the permissions that you need for reranking in Amazon Bedrock.
- [Use a reranker model](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank-use.html): Learn how to use a reranker model in Amazon Bedrock.

### [Amazon Titan models](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-models.html)

Learn about Amazon Titan foundation models, their capabilities, and how to use them for text generation, image creation, and embeddings in Amazon Bedrock.

- [Text Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html): Amazon Titan Embeddings models include Amazon Titan Text Embeddings V2 and Titan Text Embeddings G1 model.
- [Multimodal Embeddings G1](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-multiemb-models.html): Amazon Titan Foundation Models are pre-trained on large datasets, making them powerful, general-purpose models.
- [Image Generator G1](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-image-models.html): Amazon Titan Image Generator G1 is an image generation model that enables users to generate and edit images in versatile ways.


## [Build](https://docs.aws.amazon.com/bedrock/latest/userguide/build.html)

- [APIs](https://docs.aws.amazon.com/bedrock/latest/userguide/apis.html): Inference APIs supported
- [Endpoints](https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.html): Amazon Bedrock supports various endpoints depending on whether you want to perform control plane operators or inference operations.
- [Projects](https://docs.aws.amazon.com/bedrock/latest/userguide/projects.html): Amazon Bedrock Projects API provides application-level isolation for your generative AI workloads using OpenAI-compatible APIs.

### [API keys](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html)

Learn how to quickly start using the Amazon Bedrock API by authenticating with Amazon Bedrock API keys.

- [How it works](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-how.html): Learn how Amazon Bedrock API keys work to simplify authentication and authorization for making API calls, including short-term and long-term key options.
- [Supported Regions/SDKs](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-supported.html): Learn what Regions support Amazon Bedrock API keys.
- [Generate an API key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-generate.html): Generate and configure API keys in Amazon Bedrock to authenticate your API requests.
- [Use an API key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-use.html): Use an Amazon Bedrock API key to authenticate your API requests.
- [Modify permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-modify.html): Learn how to modify permissions for Amazon Bedrock API keys by managing IAM policies.
- [Compromised keys](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-revoke.html): Learn how to revoke permissions for Amazon Bedrock API keys.
- [Control permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-permissions.html): Learn how to control permissions for generation and use of Amazon Bedrock API keys.

### [Inference: Generate responses](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html)

Learn how to use foundation models in Amazon Bedrock to generate text, images, and embeddings from your prompts.

- [Different inference methods](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-methods.html): You can directly run model inference in the following ways:
- [How inference works](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-how.html): Learn how model inference works in Amazon Bedrock.
- [Inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html): Learn how to control and customize foundation model outputs by adjusting inference parameters like temperature, top_p, and max_tokens in Amazon Bedrock.
- [Supported Regions and models](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-supported.html): Learn about the Regions and models with which you can run model inference.
- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-prereq.html): Learn about the requirements and setup needed before using Amazon Bedrock foundation models for inference, including model access and permissions.
- [Responses using Console](https://docs.aws.amazon.com/bedrock/latest/userguide/playgrounds.html): Learn how to use Amazon Bedrock playgrounds to experiment with foundation models, test prompts, and generate text and image responses in the console.
- [Inference reasoning](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-reasoning.html): Learn how to improve foundation model accuracy and transparency by using chain of thought reasoning to break down complex tasks into simpler steps.
- [Latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html): Learn how to reduce response times and improve user experience by using latency-optimized inference for Amazon Bedrock foundation models.
- [Inference using OpenAI APIs](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html): Learn how to use OpenAI compatible API operations with Amazon Bedrock to generate responses from foundation models.

### [Inference using Bedrock APIs](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-api.html)

Learn how to programmatically interact with Amazon Bedrock foundation models using API operations to generate text, images, and embeddings for your applications.

- [Submit a single prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-invoke.html): You run inference on a single prompt by using the InvokeModel and InvokeModelWithResponseStream API operations and specifying a model.
- [Use the OpenAI Chat Completions API](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-chat-completions.html): You can run model inference using the OpenAI Create chat completion API with Amazon Bedrock models.

### [Carry out a conversation with Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html)

Learn how to build conversational AI applications using the Amazon Bedrock Converse API to manage multi-turn dialogues with foundation models.

- [Supported models and model features](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-supported-models-features.html): The Converse API supports the following Amazon Bedrock models and model features.
- [Using the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html): To use the Converse API, you call the Converse or ConverseStream operations to send messages to a model.
- [Converse API examples](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-examples.html): The following examples show you how to use the Converse and ConverseStream operations.
- [API restrictions](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-api-restrictions.html): The following restrictions apply to the InvokeModel, InvokeModelWithResponseStream, Converse, and ConverseStream operations.
- [Structured Outputs](https://docs.aws.amazon.com/bedrock/latest/userguide/structured-output.html): Structured outputs is a capability in Amazon Bedrock that ensures model responses conform to user-defined JSON schemas and tool definitions, reducing the need for custom parsing and validation mechanisms in production AI deployments.
- [Computer use](https://docs.aws.amazon.com/bedrock/latest/userguide/computer-use.html): Shows how to call a tool (function) with Amazon Bedrock Tool Use (Function Calling).
- [Tool use](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html): Shows how to call a tool (function) with Amazon Bedrock Tool Use (Function Calling).


## [Model customization](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html)

### [Supervised fine-tuning](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html)

With Amazon Bedrock, you can train a foundation model to improve performance on specific tasks (known as fine-tuning).

- [Prepare data for fine-tuning your models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html): Learn how to prepare training datasets for different types of models and customization approaches in Amazon Bedrock.
- [Fine-tune Amazon Nova models](https://docs.aws.amazon.com/bedrock/latest/userguide/nova-2-sft-data-prep.html): Amazon Nova 2.0 SFT data uses the same Converse API format as Amazon Nova 1.0, with the addition of optional reasoning content fields.
- [Custom model hyperparameters](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html): Learn about the hyperparameters available for customizing foundation models in Amazon Bedrock, including settings for learning rate, batch size, and epochs.
- [Submit a model fine-tuning job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-submit.html): You can create a custom model by using fine-tuning in the Amazon Bedrock console or API.

### [Reinforcement fine-tuning](https://docs.aws.amazon.com/bedrock/latest/userguide/reinforcement-fine-tuning.html)

Learn how to use reinforcement fine-tuning to improve foundation model performance through feedback signals.

### [Fine-tune Amazon Nova models](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-nova-models.html)

Learn how to use reinforcement fine-tuning to customize Amazon Nova models for your specific use cases.

- [Access and security](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-access-security.html): Learn about the additional permissions required for reinforcement fine-tuning operations for Amazon Nova models.
- [Prepare data](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-prepare-data.html): Learn how to prepare training data for reinforcement fine-tuning Amazon Nova models.
- [Setting up reward functions](https://docs.aws.amazon.com/bedrock/latest/userguide/reward-functions.html): Reward functions evaluate response quality and provide feedback signals for model training.
- [Create fine-tuning jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-submit-job.html): Learn how to create and submit a reinforcement fine-tuning job using the console or API, and how to monitor the job's progress, and gather metrics.

### [Fine-tune open-weight models using OpenAI APIs](https://docs.aws.amazon.com/bedrock/latest/userguide/fine-tuning-openai-apis.html)

Learn how to use OpenAI compatible API operations with Amazon Bedrock to create and manage reinforcement fine-tuning jobs.

- [Access and security](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-open-weight-access-security.html): Learn about the additional permissions required for reinforcement fine-tuning operations for OpenAI open-weight models.
- [Prepare data](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-prepare-data-open-weight.html): Learn how to prepare training data for reinforcement fine-tuning open-weight models.
- [Setting up reward functions](https://docs.aws.amazon.com/bedrock/latest/userguide/reward-functions-open-weight.html): Reward functions evaluate response quality and provide feedback signals for model training.
- [Create fine-tuning jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/fine-tuning-openai-job-create.html): The OpenAI-compatible fine-tuning job APIs allow you to create, monitor, and manage fine-tuning jobs.
- [Evaluate your RFT model](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-evaluate-model.html): Learn how to evaluate your reinforcement fine-tuned model using multiple assessment methods.

### [Distillation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-distillation.html)

Learn how to use distilled models for your use case in Amazon Bedrock.

- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/prequisites-model-distillation.html): Learn about the prerequisites and foundation models you can choose for teacher and student models for model distillation.
- [Prepare data](https://docs.aws.amazon.com/bedrock/latest/userguide/distillation-prepare-datasets.html): Learn about how to prepare a dataset for model distillation with Amazon Bedrock.
- [Submit a model distillation job](https://docs.aws.amazon.com/bedrock/latest/userguide/submit-model-distillation-job.html): You can perform model distillation through the Amazon Bedrock console or by sending a CreateModelCustomizationJob request with an Amazon Bedrock control plane endpoint.
- [Clone a distillation job](https://docs.aws.amazon.com/bedrock/latest/userguide/clone-model-distillation-job.html): Learn how to clone an Amazon Bedrock distillation job.

### [Custom model import](https://docs.aws.amazon.com/bedrock/latest/userguide/import-pre-trained-model.html)

You can create a custom model in Amazon Bedrock by importing a model you customized in other environments, such as Amazon SageMaker AI.

### [Custom model import: Import pretrained open-source models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html)

You can create a custom model in Amazon Bedrock by using the Amazon Bedrock Custom Model Import feature to import Foundation Models that you have customized in other environments, such as Amazon SageMaker AI.

### [Prerequisites for importing model](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-import-prereq.html)

Learn the prerequisites that you must fulfill before you can import a model to Amazon Bedrock.

- [(Optional) Protect custom model import jobs using a VPC](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-custom-model-import.html): Learn about using virtual private clouds to protect your custom model import jobs.
- [Submit a model import job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model-job.html): You import a model into Amazon Bedrock by submitting a model import job in the Amazon Bedrock console, using the API, using the AWS CLI or using AWS SDK.

### [Invoke your imported model](https://docs.aws.amazon.com/bedrock/latest/userguide/invoke-imported-model.html)

Learn about invoking the newly imported model and about configuring retries

- [Advanced API features for imported models](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-import-advanced-features.html): Learn about advanced capabilities including structured outputs, vision support, log probabilities, and tool calling
- [Custom chat templates and tokenizers](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-chat-templates-tokenizers.html): Learn how to import and use custom chat templates and tokenizers with your imported models to ensure proper message formatting and tokenization.
- [Calculate the cost of running a custom model](https://docs.aws.amazon.com/bedrock/latest/userguide/import-model-calculate-cost.html): Learn about how to calculate the cost of running a model that you import into Amazon Bedrock

### [Code samples for custom model import](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-import-code-samples.html)

The following code samples show how to set up permissions, create a custom model import job, view the details of your import jobs and imported models, and delete imported model.

- [Converse API code samples for custom model import](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-import-code-samples-converse.html): If you're importing a Mistral, Llama, or Qwen type instruct model and you want to use the Converse or the ConverseStream API, make sure to include the chat_template for the model type you are importing in the tokenizer_config.json.

### [Import a SageMaker AI-trained Amazon Nova model](https://docs.aws.amazon.com/bedrock/latest/userguide/import-with-create-custom-model.html)

Create a new custom model in Amazon Bedrock from an existing SageMaker AI-trained Amazon Nova model stored in Amazon S3.

- [Create a custom model](https://docs.aws.amazon.com/bedrock/latest/userguide/create-custom-model-sdks.html): Use Amazon Bedrock APIs to create a new custom model in Amazon Bedrock from an existing SageMaker AI-trained Amazon Nova model stored in Amazon S3.

### [Manage customized models](https://docs.aws.amazon.com/bedrock/latest/userguide/manage-customized-models.html)

After creating a customized model through fine-tuning, reinforcement fine-tuning, distillation, or import, you can manage the model throughout its lifecycle.

- [Model customization access and security](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-job-access-security.html): Learn how to secure your Amazon Bedrock model customization jobs and artifacts.
- [Monitor your model customization job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-monitor.html): Learn how to track the progress and status of your model customization job.
- [Analyze model customization job results](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-analyze.html): Learn how to analyze the results and performance metrics of your completed model customization job.
- [Stop a model customization job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-stop.html): Learn how to stop a model customization job that is in progress.
- [View details about a custom model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-view.html): Learn how to get information about a custom model or list information about all your custom models.

### [Set up inference for a custom model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html)

Learn how to set up inference for custom models.

- [Purchase Provisioned Throughput for a custom model](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-use-pt.html): Learn how to use a custom model with Provisioned Throughput.
- [Deploy a custom model for on-demand inference](https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-custom-model-on-demand.html): Learn how to deploy your custom model for on-demand inference with Amazon Bedrock.

### [Share a model for another account to use](https://docs.aws.amazon.com/bedrock/latest/userguide/share-model.html)

Learn how to share a model with another account.

- [Supported Regions and models](https://docs.aws.amazon.com/bedrock/latest/userguide/share-model-support.html): The following list provides links to general information about Regional and model support in Amazon Bedrock:
- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/share-model-prereq.html): Learn how to set up permissions for sharing models with other accounts.
- [Share a model with another account](https://docs.aws.amazon.com/bedrock/latest/userguide/share-model-share.html): Learn how to share a model with another account.
- [View information about shared models](https://docs.aws.amazon.com/bedrock/latest/userguide/share-model-view.html): Learn how to view information about models that you've shared with other accounts.
- [Update access to a shared model](https://docs.aws.amazon.com/bedrock/latest/userguide/share-model-edit.html): Learn how to update access to models that you've shared with other accounts.
- [Revoke access to a shared model](https://docs.aws.amazon.com/bedrock/latest/userguide/share-model-revoke.html): Learn how to revoke access to a model that you've shared with another account.

### [Copy a model to use in a Region](https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html)

Learn how to copy a model to a Region.

- [Supported Regions and models](https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model-support.html): The following list provides links to general information about Regional and model support in Amazon Bedrock:
- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model-prereq.html): Learn how to set up permissions for copying models.
- [Copy a model to a Region](https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model-copy.html): Learn how to copy a model to a Region so that it can be used.
- [View information about model copy jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model-job-view.html): Learn how to view information about model copy jobs that you've submitted.
- [Delete a custom model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-delete.html): Learn how to delete a custom model.
- [Code samples](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-code-samples.html): The following code samples show how to prepare a basic dataset, set up permissions, create a custom model, view the output files, purchase throughput for the model, and run inference on the model.
- [Troubleshooting model customization issues](https://docs.aws.amazon.com/bedrock/latest/userguide/fine-tuning-troubleshooting.html): This section summarizes errors that you might encounter and what to check if you do.


## [Security, Guardrails, and Observability](https://docs.aws.amazon.com/bedrock/latest/userguide/security.html)

### [Security](https://docs.aws.amazon.com/bedrock/latest/userguide/security-overview.html)

Learn about security features and best practices for Amazon Bedrock.

### [Data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon Bedrock.

### [Data encryption](https://docs.aws.amazon.com/bedrock/latest/userguide/data-encryption.html)

Amazon Bedrock uses encryption to protect data at rest and data in transit.

- [Encryption of custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-custom-job.html): Amazon Bedrock uses your training data with the CreateModelCustomizationJob action, or with the console, to create a custom model which is a fine tuned version of an Amazon Bedrock foundational model.

### [Encryption of imported custom models](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-import-model.html)

Amazon Bedrock supports creating custom models through two methods that both use the same encryption approach.

- [Using customer managed key (CMK)](https://docs.aws.amazon.com/bedrock/latest/userguide/import-model-using-cmk.html): If you are planning to use customer managed key to encrypt your custom imported model, complete the following steps:
- [Monitoring your encryption keys for the Amazon Bedrock service](https://docs.aws.amazon.com/bedrock/latest/userguide/import-model-monitor-encryption-keys.html): When you use an AWS KMS customer managed key with your Amazon Bedrock resources, you can use AWS CloudTrail or Amazon CloudWatch Logs to track requests that Amazon Bedrock sends to AWS KMS.
- [Encryption in Amazon Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-bda.html): Amazon Bedrock Data Automation (BDA) uses encryption to protect your data at rest.

### [Encryption of agent resources](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-agents-new.html)

Encryption of data at rest by default helps reduce the operational overhead and complexity involved in protecting sensitive data.

### [Encryption of agent resources with customer managed keys (CMK)](https://docs.aws.amazon.com/bedrock/latest/userguide/cmk-agent-resources.html)

You can at any time create a customer managed key to encrypt your agentâs information using the following agent information provided when building your agent.

- [Encrypt agent sessions with customer managed key (CMK)](https://docs.aws.amazon.com/bedrock/latest/userguide/ltm-permissions.html): If you've enabled memory for your agent and if you encrypt agent sessions with a customer managed key, you must configure the following key policy and the calling identity IAM permissions to configure your customer managed key.
- [Preventative security best practice for agents](https://docs.aws.amazon.com/bedrock/latest/userguide/security-best-practice-agents.html): The following best practices for Amazon Bedrock service can help prevent security incidents:
- [Encryption of agent resources for agents created before January 22, 2025](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-agents.html)
- [Encryption of flow resources](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-flows.html): Amazon Bedrock encrypts your data at rest.
- [Encryption of knowledge base resources](https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-kb.html): Amazon Bedrock encrypts resources related to your knowledge bases.

### [Protect your data using a Amazon VPC](https://docs.aws.amazon.com/bedrock/latest/userguide/usingVPC.html)

Learn about virtual private clouds (VPCs) and AWS PrivateLink interface VPC endpoints.

- [Use AWS PrivateLink to create a private connection](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html): You can use an AWS PrivateLink to create a private connection between your VPC and Amazon Bedrock.
- [(Example) Restrict data access to your S3 data](https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-s3.html): Learn how to restrict data access to your S3 data such that only your VPC can access it.

### [Identity and access management](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html)

How to authenticate requests and manage access your Amazon Bedrock resources.

- [How Amazon Bedrock works with IAM](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Bedrock, learn what IAM features are available to use with Amazon Bedrock.

### [Identity-based policy examples](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html)

By default, users and roles don't have permission to create or modify Amazon Bedrock resources.

- [Amazon Bedrock Agents examples](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples-agent.html): Select a topic to see example IAM policies that you can attach to an IAM role to provision permissions for actions in .
- [Managing IAM policies on Projects](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-projects.html): Amazon Bedrock Projects support direct IAM policy attachment, allowing you to manage access control at the project resource level.
- [AWS managed policies](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Bedrock and recent changes to those policies.

### [Service roles](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-sr.html)

Amazon Bedrock uses IAM service roles for some features to let Amazon Bedrock carry out tasks on your behalf.

- [Batch inference service role](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html): To use a custom service role for batch inference instead of the one Amazon Bedrock automatically creates for you in the AWS Management Console, create an IAM role and attach the following permissions by following the steps at Creating a role to delegate permissions to an AWS service.
- [Model customization service role](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-iam-role.html): To use a custom role for model customization instead of the one Amazon Bedrock automatically creates, create an IAM role and attach the following permissions by following the steps at Creating a role to delegate permissions to an AWS service.
- [Model import service role](https://docs.aws.amazon.com/bedrock/latest/userguide/model-import-iam-role.html): To use a custom role for model import create an IAM service role and attach the following permissions.
- [Agents service role](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-permissions.html): To use a custom service role for agents instead of the one Amazon Bedrock automatically creates, create an IAM role and attach the following permissions by following the steps at Creating a role to delegate permissions to an AWS service.
- [Knowledge base service role](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-permissions.html): To use a custom role for a knowledge base instead of the one Amazon Bedrock automatically creates, create an IAM role and attach the following permissions by following the steps at Creating a role to delegate permissions to an AWS service.
- [Amazon Bedrock Flows service role](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html): To create and manage a flow in Amazon Bedrock, you must use a service role with the necessary permissions outlined on this page.

### [Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security-service-roles.html)

To create a model evaluation job, you must specify a service role.

- [Automatic model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/automatic-service-roles.html): To create an automatic model evaluation job, you must specify a service role.
- [Model evaluation jobs that use humans](https://docs.aws.amazon.com/bedrock/latest/userguide/model-eval-service-roles.html): To create a model evaluation job that uses human evaluators, you must specify two service roles.
- [Service role: Model as Judge](https://docs.aws.amazon.com/bedrock/latest/userguide/judge-service-roles.html): Learn more about the service role requirements for setting up a model evaluation job that uses a LLM as judge
- [Knowledge base evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/rag-eval-service-roles.html): To create a knowledge base evaluation job, you must specify a service role.
- [Configure access to S3 buckets](https://docs.aws.amazon.com/bedrock/latest/userguide/s3-bucket-access.html): Configure access to Amazon S3 buckets.
- [Troubleshooting](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Bedrock and IAM.
- [Cross-account access to Amazon S3 bucket for custom model import job](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-account-access-cmi.html): Configure cross-account access to Amazon S3 bucket for custom model import job
- [Compliance validation](https://docs.aws.amazon.com/bedrock/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Incident response](https://docs.aws.amazon.com/bedrock/latest/userguide/security-incident-response.html): Security is the highest priority at AWS.
- [Resilience](https://docs.aws.amazon.com/bedrock/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific Amazon Bedrock features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/bedrock/latest/userguide/infrastructure-security.html): Learn how Amazon Bedrock isolates service traffic.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [Configuration and vulnerability analysis in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/vulnerability-analysis-and-management.html): Configuration and IT controls are a shared responsibility between AWS and you, our customer.
- [Abuse detection](https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html): Learn about Amazon Bedrock automated abuse detection mechanisms that help prevent misuse and identify potential violations of acceptable use policies.
- [Prompt injection security](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-injection.html): As per the AWS Shared Responsibility Model, AWS is responsible for securing the underlying cloud infrastructure, including the hardware, software, networking, and facilities that run AWS services.

### [Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)

Learn how to reduce and protect from harmful information being sent to end-users.

- [Overview](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html): Guardrails helps block harmful content using word and image filters, policies, and contextual grounding checks.
- [Supported Regions/models](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-supported.html): Learn about AWS Region and model support for Amazon Bedrock Guardrails.
- [Safeguard tiers for guardrails policies](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tiers.html): Amazon Bedrock Guardrails provides safeguard tiers for specific policies.
- [Supported languages](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-supported-languages.html): Learn which languages are supported by Amazon Bedrock Guardrails.
- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prereq.html): Learn the prerequisites for using Amazon Bedrock Guardrails and what you should prepare to create a guardrail.

### [Set up permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-permissions.html)

Learn how to configure the necessary IAM permissions and roles to create, manage, and use Amazon Bedrock guardrails for content filtering.

- [Permissions for Automated Reasoning policies](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrail-automated-reasoning-permissions.html): Learn what IAM permissions you need to use Automated Reasoning policies with the ApplyGuardrail API.
- [Permissions for Automated Reasoning with agents](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrail-automated-reasoning-agent-permissions.html): Learn what additional IAM permissions you need to use Automated Reasoning policies with Amazon Bedrock agents.
- [(Optional) Permissions for encrypting a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-permissions-kms.html): You encrypt your guardrails with customer managed AWS KMS keys.
- [Enforce specific guardrails during inference](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-permissions-id.html): You can enforce the use of a specific guardrail for model inference by including the bedrock:GuardrailIdentifier condition key in your IAM policy.
- [Permissions for using cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrail-profiles-permissions.html): Learn what IAM permissions you need to use cross-Region guardrail inference with Amazon Bedrock.
- [Using resource-based policies for guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-resource-based-policies.html): Learn how to use resource-based policies to control access to Guardrails resources across accounts and organizations.

### [Create your guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html)

Learn about the different filters and blockers of a guardrail in Amazon Bedrock

### [Configure content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters-overview.html)

With Amazon Bedrock Guardrails, you can configure content filters to block model prompts and responses in natural language for text and images containing harmful content.

- [Content filters (text)](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html): Amazon Bedrock Guardrails supports content filters to help detect and filter harmful user inputs and model-generated outputs in natural language as well as code-related content in Standard tier.
- [Content filters (images)](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-mmfilter.html): Learn how to use Amazon Bedrock guardrails to detect and filter harmful image content in multimodal AI applications.
- [Prompt attacks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html): Learn how prompt attacks work and the different types of prompt attacks.
- [Add denied topics](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-denied-topics.html): You can specify a set of denied topics in a guardrail that are undesirable in the context of your generative AI application.
- [Add word filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-word-filters.html): Amazon Bedrock Guardrails has word filters that you can use to block words and phrases (exact match) in input prompts and model responses.
- [Add sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html): Amazon Bedrock Guardrails helps detect sensitive information, such as personally identifiable information (PII), in input prompts or model responses using sensitive information filters.
- [Add contextual grounding checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html): Amazon Bedrock Guardrails supports contextual grounding checks to detect and filter hallucinations in model responses when a reference source and a user query is provided.
- [Options for handling harmful content](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-harmful-content-handling-options.html): Learn about options for handling harmful content detected by Amazon Bedrock Guardrails.

### [What are Automated Reasoning checks?](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html)

Learn how Automated Reasoning checks in Amazon Bedrock Guardrails use mathematical verification to detect hallucinations, highlight unstated assumptions, and provide explanations for why accurate statements are correct.

- [Automated Reasoning checks concepts](https://docs.aws.amazon.com/bedrock/latest/userguide/automated-reasoning-checks-concepts.html): Understand the core concepts behind Automated Reasoning checks in Amazon Bedrock Guardrails, including policies, rules, variables, custom types, findings, translation, and confidence thresholds.
- [Create your Automated Reasoning policy](https://docs.aws.amazon.com/bedrock/latest/userguide/create-automated-reasoning-policy.html): Learn how to create an Automated Reasoning policy for Amazon Bedrock Guardrails, from preparing your source document through reviewing the extracted policy.
- [Policy best practices](https://docs.aws.amazon.com/bedrock/latest/userguide/automated-reasoning-policy-best-practices.html): Best practices for writing effective Automated Reasoning policies, including rule structure, variable descriptions, naming conventions, and common anti-patterns to avoid.
- [Test an Automated Reasoning policy](https://docs.aws.amazon.com/bedrock/latest/userguide/test-automated-reasoning-policy.html): Learn how to test your Automated Reasoning policy using generated scenarios and QnA tests, run tests, and interpret the results before deploying to production.
- [Troubleshoot and refine your policy](https://docs.aws.amazon.com/bedrock/latest/userguide/address-failed-automated-reasoning-tests.html): Learn how to diagnose and fix issues when your Automated Reasoning policy tests fail, including a systematic debugging workflow, translation fixes, rule fixes, annotations, and the quality report.
- [Use Kiro CLI with an Automated Reasoning policy](https://docs.aws.amazon.com/bedrock/latest/userguide/kiro-cli-automated-reasoning-policy.html): Learn how to use Kiro CLI to create, inspect, test, and refine Automated Reasoning policies using an interactive chat interface.
- [Deploy your Automated Reasoning policy](https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-automated-reasoning-policy.html): Learn how to save a version of your Automated Reasoning policy, add it to a guardrail, automate deployment with CloudFormation, and integrate policy deployment into CI/CD pipelines.
- [Integrate Automated Reasoning checks](https://docs.aws.amazon.com/bedrock/latest/userguide/integrate-automated-reasoning-checks.html): Learn how to use Automated Reasoning checks at runtime to validate LLM responses, interpret findings programmatically, rewrite invalid responses using AR feedback, ask clarifying questions, and build an audit trail.
- [Code domain support](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-code-domain.html): Guardrails now detect and filter harmful content across both natural-language and code-related inputs and outputs.

### [Cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html)

Learn how to improve guardrail performance by distributing inference requests across multiple AWS Regions.

- [Supported Regions for cross-Region guardrail inference](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region-support.html): Cross-Region inference with Amazon Bedrock Guardrails lets you seamlessly manage unplanned traffic bursts by utilizing compute across different AWS Regions for your guardrail policy evaluations.
- [Cross-account safeguards](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html): Learn how to automatically apply safety controls at an AWS account level and at an AWS Organizations level for all model invocations with Amazon Bedrock using guardrails enforcements.
- [Test your guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-test.html): Learn how to evaluate and validate your Amazon Bedrock guardrail configurations to ensure they properly filter harmful content before deployment.
- [View information about your guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-view.html): Learn how to access and review details about your Amazon Bedrock guardrails, including configurations, versions, and deployment status.
- [Modify your guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-edit.html): Learn how to update and refine your Amazon Bedrock guardrail configurations to improve content filtering effectiveness and adapt to changing requirements.
- [Delete your guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-delete.html): Learn how to safely remove Amazon Bedrock guardrails that are no longer needed while ensuring proper cleanup of associated resources.

### [Deploy your guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-deploy.html)

Learn how to deploy your Amazon Bedrock guardrails to production environments and integrate them with foundation models and applications.

- [Create a version of a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-versions-create.html): To create a version of a guardrail, choose the tab for your preferred method, and then follow the steps:
- [View information about guardrail versions](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-versions-view.html): To view information about a version or versions of a guardrail, select one of the tabs below and follow the steps indicated:
- [Delete a guardrail version](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-versions-delete.html): To learn how to delete a version of a guardrail, select one of the tabs below and follow the steps indicated:

### [Guardrails use cases](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use.html)

Learn how to apply Amazon Bedrock guardrails to different use cases and integrate them with foundation models, agents, and flows.

### [Use with inference operations](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-input-tagging-base-inference.html)

You can use guardrails with the base inference operations, InvokeModel and InvokeModelWithResponseStream (streaming).

- [Apply tags to user input](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tagging.html): Input tags allow you to mark specific content within the input text that you want to be processed by guardrails.
- [Streaming responses](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html): The InvokeModelWithResponseStream API returns data in a streaming format.
- [Include a guardrail with Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-converse-api.html): Learn how to integrate Amazon Bedrock guardrails with the Converse API to filter content in conversational AI applications.
- [Use the ApplyGuardrail API in your application](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html): Learn how to implement content filtering in your applications by using the Amazon Bedrock ApplyGuardrail API independently of model inference.

### [Observability](https://docs.aws.amazon.com/bedrock/latest/userguide/observability.html)

Learn how to monitor, tag, and manage Amazon Bedrock resources.

### [Monitoring](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html)

Learn how to monitor the health and performance of all parts of your Amazon Bedrock application.

- [Monitor models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html): You can use model invocation logging to collect invocation logs, model input data, and model output data for all invocations in your AWS account used in Amazon Bedrock in a Region.
- [Monitor knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-bases-logging.html): Amazon Bedrock supports a monitoring system to help you understand the execution of any data ingestion jobs for your knowledge bases.
- [Monitor Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-guardrails-cw-metrics.html): The following table describes runtime metrics provided by Amazon Bedrock Guardrails that you can monitor with Amazon CloudWatch metrics.
- [Monitor Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-agents-cw-metrics.html): The following table describes runtime metrics provided by Amazon Bedrock Agents that you can monitor with Amazon CloudWatch Metrics.

### [Monitor event changes](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-eventbridge.html)

Learn how to monitor job state changes with Amazon EventBridge

- [How EventBridge for Amazon Bedrock works](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-eventbridge-how-it-works.html): Learn how EventBridge works for EventBridge.
- [[Example] Create a rule to handle Amazon Bedrock state change events](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-eventbridge-create-rule-ex.html): The example in this topic demonstrates how to set up notification of Amazon Bedrock state change events by guiding you through configuring an Amazon Simple Notification Service topic, subscribing to the topic, and creating a rule in Amazon EventBridge to notify you of an Amazon Bedrock state change through the topic.
- [Monitor APIs](https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html): Learn about logging Amazon Bedrock API calls with AWS CloudTrail.
- [Tagging resources](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html): Learn how to tag and organize your resources in Amazon Bedrock.

### [Provisioning & Orchestration](https://docs.aws.amazon.com/bedrock/latest/userguide/provisioning-orchestration.html)

Learn how to provision and manage Amazon Bedrock resources using infrastructure as code.

### [CloudFormation](https://docs.aws.amazon.com/bedrock/latest/userguide/creating-resources-with-cloudformation.html)

Learn how to create and manage Amazon Bedrock resources using AWS CloudFormation templates for automated infrastructure deployment.

- [Managing Projects with AWS CloudFormation](https://docs.aws.amazon.com/bedrock/latest/userguide/cloudformation-projects.html): Amazon Bedrock is integrated with AWS CloudFormation, allowing you to define and manage Projects as part of your infrastructure templates.


## [Capacity, Limits, and Cost Optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html)

- [Reserved, Standard, Priority, and Flex tiers](https://docs.aws.amazon.com/bedrock/latest/userguide/service-tiers-inference.html): Learn how to optimize performance and cost by using service tiers for Amazon Bedrock foundation models.

### [Batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)

Learn how to run inference on multiple prompts asynchronously.

- [Supported Regions and models](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-supported.html): Learn about the Regions and models that support batch inference

### [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-prereq.html)

To perform batch inference, you must fulfill the following prerequisites:

- [Set up data](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html): You must add your batch inference data to an S3 location that you'll choose or specify when submitting a model invocation job.
- [Permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-permissions.html): To carry out batch inference, you must set up permissions for the following IAM identities:
- [[Optional] Set up a VPC](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc.html): Learn about using virtual private clouds to protect your batch inference data.
- [Create a job](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-create.html): After you've set up an Amazon S3 bucket with files for running model inference, you can create a batch inference job.
- [Monitor jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-monitor.html): Learn how to view information about a batch inference job
- [Stop a job](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-stop.html): Learn how to stop a batch inference job
- [View the results of a job](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-results.html): After a batch inference job is Completed, you can extract the results of the batch inference job from the files in the Amazon S3 bucket that you specified during creation of the job.
- [Code example](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-example.html): The code example in this chapter shows how to create a batch inference job, view information about it, and stop it.
- [Use the OpenAI Batch API](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-openai-batch.html): You can run a batch inference job using the OpenAI Create batch API with Amazon Bedrock OpenAI models.

### [Cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)

Learn how to use cross-Region inference to increase throughput of your model requests.

- [Geographic cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html): Geographic cross-Region inference keeps data processing within specified geographic boundaries (US, EU, APAC, etc.) while providing higher throughput than single-region inference.
- [Global cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html): Global cross-Region inference extends cross-Region inference beyond geographic boundaries, enabling the routing of inference requests to supported commercial AWS Regions worldwide, optimizing available resources and enabling higher model throughput.

### [Inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html)

Learn how you can track model invocation metrics and costs and increase your throughput with cross-Region inference using inference profiles.

- [Supported Regions and models](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html): Learn about the Regions and models supported for inference profiles.
- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-prereq.html): Learn about the prerequisites that you must fulfill to use inference profiles.
- [Create an application inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-create.html): Learn how to create an application inference profile.
- [Modify the tags for an application inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-modify.html): Learn how to add, remove, and modify tags for an application inference profile.
- [View information about an inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-view.html): Learn how to view information about inference profiles that you can use.
- [Use an inference profile in model invocation](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-use.html): Learn how to use an inference profile when running inference.
- [Delete an application inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-delete.html): Learn how to delete an inference profile.

### [Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)

Learn how to purchase and use Provisioned Throughput for Amazon Bedrock custom and base models.

- [Supported Regions and models](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-supported.html): Learn about Regional, model, and feature support for Provisioned Throughput.
- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-prereq.html): Before you can purchase and manage Provisioned Throughput, you need to fulfill the following prerequisites:
- [Purchase a Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-purchase.html): Learn how to purchase Provisioned Throughput for Amazon Bedrock custom and base models.
- [View information about a Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-info.html): Learn how to view information about a Provisioned Throughput.
- [Modify a Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-edit.html): Learn how to modify a Provisioned Throughput.
- [Use a Provisioned Throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-use.html): After you purchase a Provisioned Throughput, you can use it with the following features:
- [Delete a Provisioned Throughput or cancel auto renew](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-delete.html): Learn how to delete a Provisioned Throughput or disable auto-renewal.
- [Code examples](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-thru-code-examples.html): See code examples for purchasing and managing a Provisioned Throughput in Amazon Bedrock.

### [Quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html)

Learn about the service quotas and limits for Amazon Bedrock resources, API operations, and model usage to optimize your application performance.

- [How tokens are counted](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas-token-burndown.html): Learn how to calculate the token burndown rate for Amazon Bedrock.
- [Count tokens to monitor usage and cost](https://docs.aws.amazon.com/bedrock/latest/userguide/count-tokens.html): Learn how to count the number of tokens in your input before sending for inference.
- [Request an increase for Amazon Bedrock quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas-increase.html): Learn how to request an increase for Amazon Bedrock quotas.
- [Prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html): Learn about how to use the prompt caching feature in Amazon Bedrock to get faster model responses and reduce inference costs.


## [Additional Capabilities](https://docs.aws.amazon.com/bedrock/latest/userguide/additional-capabilities.html)

### [Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)

Learn about how to use Amazon Bedrock to automate processing of images, audio, video, and documents

### [How Bedrock Data Automation works](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-how-it-works.html)

Introduction to BDA concepts such as output types, projects and blueprints.

### [Bedrock Data Automation projects](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-projects.html)

Introduction to Projects for grouping outputs and customizing Standard Outputs

- [Splitting documents while using projects](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-document-splitting.html): Amazon Bedrock Data Automation (BDA) supports splitting documents when using the Amazon Bedrock API.
- [Disabling modalities and routing file types](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-routing-enablement.html): Learn more about routing and enablement
- [Cross Region support required for Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-cris.html): Learn about cross Region support and ARNs supported by Bedrock.

### [Standard output in Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-standard-output.html)

Learn about standard output for different data types in BDA

- [Documents](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-output-documents.html): Learn about Document standard output options
- [Images](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-ouput-image.html): Learn about standard output for images in BDA
- [Videos](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-ouput-video.html): Learn about Video standard output for BDA
- [Audio](https://docs.aws.amazon.com/bedrock/latest/userguide/audio-processing.html): Learn about Audio standard output in BDA

### [Custom output and blueprints](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-custom-output-idp.html)

Learn about custom output, how blueprints work, and ways to create blueprints for processing

- [Blueprints](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-blueprint-info.html): Learn about blueprints and see an in depth walkthrough of one.

### [Creating blueprints](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-idp.html)

Learn about creating blueprints in general, and for specific data types.

### [Creating Blueprints for Documents](https://docs.aws.amazon.com/bedrock/latest/userguide/idp-cases.html)

Learn about indvidual document processing cases with BDA

- [Create Blueprints for Classification](https://docs.aws.amazon.com/bedrock/latest/userguide/idp-cases-classification.html): Learn about creating blueprints to classify documents into catagories
- [Creating Blueprints for Extraction](https://docs.aws.amazon.com/bedrock/latest/userguide/idp-cases-extraction.html): Learn about extracting specific information from blueprints using BDA
- [Create Blueprints for Normalization](https://docs.aws.amazon.com/bedrock/latest/userguide/idp-cases-normalization.html): Learn about using BDA to normalize information such as dates and times.
- [Create Blueprints for Transformation](https://docs.aws.amazon.com/bedrock/latest/userguide/idp-cases-transformation.html): Learn about using blueprints to change data into more usable forms
- [Create Blueprints for Validation](https://docs.aws.amazon.com/bedrock/latest/userguide/idp-cases-validation.html): Learn about using blueprints to validate certain key information
- [Creating blueprints for images](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-idp-images.html): Amazon Bedrock Data Automation (BDA) allows you to create custom blueprints for image modalities.
- [Creating blueprints for audio](https://docs.aws.amazon.com/bedrock/latest/userguide/creating-blueprint-audio.html): Learn about creating audio blueprints for processing
- [Creating blueprints for video](https://docs.aws.amazon.com/bedrock/latest/userguide/creating-blueprint-video.html): Learn about creating video blueprints for processing
- [Optimize your blueprints with ground truth](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-optimize-blueprint-info.html): You can improve blueprint accuracy by providing example content assets with the correct expected results.
- [Using the Bedrock Data Automation Console](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-blueprints-console.html): In Amazon Bedrock Data Automation (BDA), two major artifacts are used when processing information.
- [Using the Bedrock Data Automation API](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-using-api.html): The Amazon Bedrock Data Automation (BDA) feature provides a streamlined API workflow for processing your data.
- [Tagging Inferences and Resources in Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-tagging.html): Learn about tagging in BDA
- [Prerequisites for using Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-limits.html): Files for BDA need to meet certain requirements in order to be processed.

### [Using Amazon Bedrock Data Automation CLI](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-cli-guide.html)

Learn how to use the AWS Command Line Interface (CLI) to create and manage Amazon Bedrock Data Automation projects, blueprints, and process documents.

- [Blueprint Operations CLI](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-blueprint-operations.html): Learn how to create, view, edit, and delete Blueprints using the AWS Command Line Interface (AWS CLI).

### [Processing through CLI](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-document-processing-cli.html)

Learn how to process documents, images, audio, and video files using the AWS CLI with Amazon Bedrock Data Automation.

- [Processing use cases](https://docs.aws.amazon.com/bedrock/latest/userguide/bda-document-processing-examples.html): Examples of processing different types of media using BDA.

### [Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)

Learn about knowledge bases in Amazon Bedrock for Retrieval Augmented Generation (RAG) using your own data.

### [How knowledge bases work](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-it-works.html)

Learn how Retrieval Augmented Generation (RAG) for Amazon Bedrock works.

- [Turning data into a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-data.html): Learn about the role of data sources in Amazon Bedrock Knowledge Bases.
- [Retrieving information from data sources](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html): After setting up a knowledge base, you can set up your application to query the data sources in it.

### [Customizing your knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-customization.html)

Learn how to customize how your data source is ingested into a knowledge base.

- [Content chunking](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html): When ingesting your data, Amazon Bedrock first splits your documents or content into manageable chunks for efficient data retrieval.
- [Parsing options](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html): Parsing refers to the understanding and extraction of content from raw data.
- [Use a Lambda function for data ingestion](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-custom-transformation.html): You have the ability to define a custom transformation Lambda function to inject your own logic into the knowledge base ingestion process.
- [Include metadata in a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-metadata.html): When ingesting CSV (comma separate values) files, you have the ability to have the knowledge base treat certain columns as content fields versus metadata fields.
- [Supported models and Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html): Use vector embedding and generative AI models with Amazon Bedrock knowledge bases and selects your Region.
- [Chat with your document with zero setup](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-chatdoc.html): Learn how to test play an Amazon Bedrock knowledge base without the need to configure a knowledge base.
- [Set up permissions to create and manage knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-prereq-permissions-general.html): For a user or role to perform actions related to Amazon Bedrock Knowledge Bases, you must attach policies to it that grant permissions to perform the actions.

### [Build a knowledge base by connecting to a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build.html)

Learn how to build a knowledge base by connecting it to a data store.

### [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-prereq.html)

Learn the required prerequisites before you can create an Amazon Bedrock knowledge base.

- [Prerequisites for your knowledge base data](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html): Learn the required prerequisites before you can use your data for your knowledge base.
- [Prerequisites for using your vector store](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html): Learn the required prerequisites before you can use your own vector store for your Amazon Bedrock knowledge base.

### [Prerequisites for OpenSearch Managed Clusters](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-osm-permissions-prereq.html)

This section shows you how to configure permissions if you're creating your own vector database with Amazon OpenSearch Service Managed Clusters.

- [Configuring resource-based policies for OpenSearch Managed clusters](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-osm-permissions-slr-rbp.html): When creating your knowledge base, you can either create your own custom role or let Amazon Bedrock create one for you.
- [Configuring OpenSearch permissions with fine-grained access control](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-osm-permissions-console-fgap.html): While optional, we strongly recommend that you enable fine-grained access control for your OpenSearch domain.

### [Create a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html)

Learn how to create an Amazon Bedrock knowledge base by connecting it to a data source.

### [Connect a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/data-source-connectors.html)

Learn how to create a data source connector to connect to and crawl your data for an Amazon Bedrock knowledge base.

- [Amazon S3](https://docs.aws.amazon.com/bedrock/latest/userguide/s3-data-source-connector.html): Learn how to connect to Amazon S3 to ingest your content for Amazon Bedrock knowledge bases.
- [Confluence](https://docs.aws.amazon.com/bedrock/latest/userguide/confluence-data-source-connector.html): Learn how to connect to Atlassian Confluence to ingest your content for Amazon Bedrock knowledge bases.
- [Microsoft SharePoint](https://docs.aws.amazon.com/bedrock/latest/userguide/sharepoint-data-source-connector.html): Learn how to connect to Microsoft SharePoint to ingest your content for Amazon Bedrock knowledge bases.
- [Salesforce](https://docs.aws.amazon.com/bedrock/latest/userguide/salesforce-data-source-connector.html): Learn how to connect to Salesforce to ingest your content for Amazon Bedrock knowledge bases.
- [Web Crawler](https://docs.aws.amazon.com/bedrock/latest/userguide/webcrawl-data-source-connector.html): Learn how to crawl web pages to ingest web content for Amazon Bedrock knowledge bases.
- [Custom](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-data-source-connector.html): Learn how to connect to a custom data source to ingest your content for Amazon Bedrock knowledge bases.
- [Customize ingestion for a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-customize-ingestion.html): You can customize vector ingestion when connecting a data source in the AWS Management Console or by modifying the value of the vectorIngestionConfiguration field when sending a CreateDataSource request.
- [Set up security configurations for your knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-create-security.html): Learn how to set up data access and network access policies for your knowledge base.
- [Sync a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-sync-ingest.html): Learn how to sync your data source and ingest your data into your knowledge base.

### [Ingest changes directly into a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion.html)

Learn how to use the KnowledgeBaseDocuments API operations to modify and ingest documents directly.

- [Prerequisites for direct ingestion](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion-prereq.html): To use direct ingestion, an IAM role must have permissions to use the KnowledgeBaseDocs API operations.
- [Ingest documents directly into a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion-add.html): Learn how to add and ingest documents directly.
- [View information about documents in your data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion-view.html): Learn how to view information about documents in your data source.
- [Delete documents from a knowledge base directly](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-direct-ingestion-delete.html): Learn how to delete directly.
- [View information about a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-ds-info.html): Learn how to view important information about a data source for an Amazon Bedrock knowledge base, such as the current settings and sync history.
- [Modify a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-ds-update.html): Learn how to change, edit, modify, or update a data source for an Amazon Bedrock knowledge base.
- [Delete a data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-ds-delete.html): Learn how to remove or delete a data source from an Amazon Bedrock knowledge base.

### [Build a knowledge base for multimodal content](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal.html)

Learn how to build, configure, and query knowledge bases with images, audio, and video content.

- [Choosing your processing approach](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal-choose-approach.html): Amazon Bedrock Knowledge Bases offers two approaches for processing multimodal content: Nova Multimodal Embeddings for visual similarity searches, and Bedrock Data Automation (BDA) for text-based processing of multimedia content.
- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal-prerequisites.html): Learn the required prerequisites before you can create a multimodal knowledge base.
- [Create a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal-create.html): You can create multimodal knowledge bases using either the console or API.
- [Add data sources and ingest](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal-add-data-source-and-ingest.html): After creating your knowledge base, add data sources containing your multimodal content and start ingestion jobs to process and index the content.
- [Test and query knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal-test-and-query.html): After ingesting your multimodal content, you can test and query your knowledge base using the console or API.
- [Troubleshooting](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-multimodal-troubleshooting.html): This section provides guidance for resolving common issues encountered when working with multimodal knowledge bases.

### [Build a knowledge base by connecting to a structured data store](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html)

Learn how to build a knowledge base by connecting it to a structured data store.

- [Set up query engine and configure permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-prereq-structured.html): Learn the required prerequisites for setting up your query engine and accessing underlying data store before creating an Amazon Bedrock knowledge base.
- [Create a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-structured-create.html): Learn how to create an Amazon Bedrock knowledge base by connecting it to a structured data store.
- [Sync a structured data store](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-data-source-structured-sync-ingest.html): Learn how to sync your structured data store and ingest your data into your knowledge base.

### [Build a knowledge base with an Amazon Kendra GenAI index](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-kendra-genai-index.html)

Learn how to build a knowledge base by connecting it to an Amazon Kendra GenAI index.

- [Create a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-kendra-genai-index-create.html): Learn how to create a knowledge base in Amazon Bedrock by connecting it to an Amazon Kendra GenAI index.

### [Build a knowledge base with Amazon Neptune Analytics graphs](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-graphs.html)

Learn how to build a knowledge base with graphs from Amazon Neptune Analytics

- [Create a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-graphs-build.html): GraphRAG is fully integrated into Amazon Bedrock Knowledge Bases and uses Amazon Neptune Analytics for graph and vector storage.

### [Test your knowledge base with queries and responses](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-test.html)

Learn how to test an Amazon Bedrock knowledge base in with queries and generated AI responses.

- [Query a knowledge base and retrieve data](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve.html): Learn how to query an Amazon Bedrock knowledge base and return data from it.
- [Query a knowledge base and generate responses](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html): Learn how to query an Amazon Bedrock knowledge base and generate AI responses based on the retrieved data.
- [Generate a query for structured data](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-generate-query.html): Learn how to generate a query for structured data.
- [Query a knowledge base connected to an Amazon Kendra GenAI index](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-kendra.html): Learn how to query a knowledge base connected to an Amazon Kendra GenAI index.
- [Query a knowledge base connected to an Amazon Neptune Analytics graph](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-neptune.html): Learn how to query a knowledge base connected to a Neptune Analytics graph.
- [Configure and customize queries and responses](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html): Learn about the query and response configurations for custom retrieval and response generation with Amazon Bedrock knowledge bases.
- [Configure responses for reasoning models](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-configure-reasoning.html): Learn how to use reasoning models with Amazon Bedrock Knowledge Bases and their considerations.
- [Deploy your knowledge base for your application](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-deploy.html): Learn how to deploy an Amazon Bedrock knowledge base to use for your generative AI application.
- [View information about a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-info.html): Learn how to view important information about an Amazon Bedrock knowledge base, such as the current settings and status.
- [Modify a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-update.html): Learn how to change, edit, modify, or update an Amazon Bedrock knowledge base.
- [Delete a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-delete.html): Learn how to remove or delete an Amazon Bedrock knowledge base.

### [Evaluate models](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)

Learn how to evaluate the performance and effectiveness of Amazon Bedrock resources, such as models and knowledge bases.

- [Supported Regions and models](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-support.html): The following table shows the models that support model evaluation:

### [Automatic model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-automatic.html)

Learn more about how to create your first automatic model evaluation job in Amazon Bedrock

- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-automatic.html): Learn more abouty creating your first automatic model evaluation job

### [Model evaluation task types](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-tasks.html)

Learn more about the available evaluation tasks in Amazon Bedrock.

- [General text generation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-tasks-general-text.html): General text generation is a task used by applications that include chatbots.
- [Text summarization](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-tasks-text-summary.html): Text summarization is used for tasks including creating summaries of news, legal documents, academic papers, content previews, and content curation.
- [Question and answer](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-tasks-question-answer.html): Question and answer is used for tasks including generating automatic help-desk responses, information retrieval, and e-learning.
- [Text classification](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-text-classification.html): Text classification is used to categorize text into pre-defined categories.
- [Prompt datasets](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-prompt-datasets.html): Learn more about using prompt datasets in model evaluation jobs
- [Create job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-create.html): Learn more about starting an automatic model evaluation job
- [List job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-list.html): Learn more how to see a list of your current automatic model evaluation jobs
- [Stop job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-stop.html): Learn more about how to stop a model evaluation job
- [Delete job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-delete.html): Learn how to remove model evaluation jobs that are no longer needed from your Amazon Bedrock account.

### [Human-based model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-human.html)

Learn how to set up and create model evaluation jobs that use human workers to assess foundation model performance in Amazon Bedrock.

- [Creating your first model evaluation that uses human workers](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-human.html): Learn more abouty creating your first model evaluation job that uses human workers
- [Custom prompt datasets (human)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-prompt-datasets-custom-human.html): Learn about requirements for custom prompt datasets in model evaluation jobs that use human workers
- [Create a model evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-create-human.html): The following examples show how to create a model evaluation job that uses human workers.
- [List model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-list-human.html): Learn more how to see a list of your current model evaluation jobs that use human workers
- [Stop job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-human-management-stop.html): Learn more about how to stop a model evaluation job
- [Delete job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-human-delete.html): Learn how to remove human-based model evaluation jobs from your Amazon Bedrock account when they are no longer needed.
- [Manage a work team for human evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/human-worker-evaluations.html): Learn how to create and manage human evaluation teams to assess foundation model performance in Amazon Bedrock.

### [LLM as a judge model evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)

Learn how to use foundation models as judges to evaluate the performance of other models in Amazon Bedrock evaluation jobs.

- [Prompt datasets](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-prompt-datasets-judge.html): Learn about requirements for custom prompt datasets in model evaluation job that uses a model as judge

### [Evaluation metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html)

Learn more about the metrics Amazon Bedrock evaluations use to score model performance.

### [Built-in metric prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt.html)

Learn more about the prompts used by evaluator models to score, and explain your model's responses.

- [Amazon Nova Pro](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt-nova.html): Prompts used with Amazon Nova Pro.
- [AnthropicÂ Claude 3.5 Sonnet](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt-claude-sonnet.html): Prompts used with Anthropic Claude 3.5 Sonnet.
- [AnthropicÂ Claude 3.5 Sonnet v2](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt-claude-sonnet35v2.html): Prompts used with Anthropic Claude 3.5 Sonnet v2.
- [AnthropicÂ Claude 3.7 Sonnet](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt-claude-sonnet37.html): Prompts used with Anthropic Claude 3.7 Sonnet.
- [AnthropicÂ Claude 3 Haiku](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt-haiku.html): Prompts used with AnthropicÂ Claude 3 Haiku.
- [AnthropicÂ Claude 3.5 Haiku](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt-haiku35.html): Prompts used with AnthropicÂ Claude 3.5 Haiku.
- [MetaÂ Llama 3.1 70B Instruct](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt-llama.html): Prompts used with MetaÂ Llama 3.1 70B Instruct.
- [Mistral Large](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt-mistral.html): Prompts used with Mistral Large.
- [Custom metric prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html): Learn about requirements and best practices for creating custom metric prompts

### [Create a job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-judge-create.html)

Create model evaluation jobs that uses a model as judge

- [Create a job with built-in metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-built-in-metrics.html): Learn more about using built-in metrics for Amazon Bedrock evaluations use to score model performance.
- [Create a job with custom metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-create-job.html): Learn more about using custom metrics for Amazon Bedrock evaluations use to score model performance.
- [List jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-judge-list.html): Learn more how to see a list of your current model evaluation jobs that use a model as judge
- [Stop a job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-judge-management-stop.html): Learn more about how to stop a model evaluation job

### [RAG evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html)

Learn how to use RAG evaluations to help choose the best retrieval and response generation for your application.

### [Prompt datasets](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-prompt.html)

Learn more about the prompt and ground truth dataset required for RAG evaluations.

- [Retrieve only](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-prompt-retrieve.html): Learn more about the prompt and ground truth dataset required for knowledge base evaluations.
- [Retrieve and generate](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-prompt-retrieve-generate.html): Learn more about the prompt and ground truth dataset required for RAG evaluations.

### [Evaluation metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-metrics.html)

Learn more about the metrics used for RAG evaluations.

### [Evaluator prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-eval-prompt.html)

Learn more about the prompts used in a knowledge base evaluation job

- [Amazon Nova Pro](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-kb-prompt-kb-nova.html): Prompts used with Amazon Nova Pro
- [AnthropicÂ Claude 3.5 Sonnet](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-kb-prompt-kb-sonnet-35.html): Prompts used with Anthropic Claude 3.5 Sonnet
- [AnthropicÂ Claude 3.5 Sonnet v2](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-kb-prompt-kb-sonnet-35v2.html): Prompts used with Anthropic Claude 3.5 Sonnet v2
- [AnthropicÂ Claude 3.7 Sonnet](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-kb-prompt-kb-sonnet-37.html): Prompts used with Anthropic Claude 3.7 Sonnet
- [AnthropicÂ Claude 3 Haiku](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-kb-haiku.html): Prompts used with Anthropic Claude 3 Haiku.
- [AnthropicÂ Claude 3.5 Haiku](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-kb-haiku35.html): Prompts used with Anthropic Claude 3.5 Haiku.
- [Meta Llama 3.1 70B Instruct](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-kb-llama.html): Prompts used with Meta Llama 3.1 70B Instruct
- [Mistral Large 1 (24.02)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-kb-prompt-kb-mistral.html): Prompts used with Mistral Large 1 (24.02)
- [Custom metric prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-evaluation-custom-metrics-prompt-formats.html): Learn about requirements and best practices for creating custom metric prompts

### [Create job](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create.html)

Learn more about how to create an evaluation job to evaluate an Amazon Bedrock knowledge base.

- [Retrieve only](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-ro.html): Learn more about how to create a retrieve-only evaluation job to evaluate an Amazon Bedrock knowledge base.
- [Retrieve only with custom metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-ro-custom.html): Learn more about how to create a retrieve-only evaluation job to evaluate an Amazon Bedrock knowledge base.
- [Retrieve and generate](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-randg.html): Learn more about how to create a retrieve-and-generate evaluation job to evaluate an Amazon Bedrock knowledge base.
- [Retrieve and generate with custom metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-create-randg-custom.html): Learn more about how to create a retrieve-and-generate evaluation job to evaluate an Amazon Bedrock knowledge base.
- [List job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-jobs-management-kb-list.html): Learn more how to see a list of your current evaluation job that use a Amazon Bedrock Knowledge Bases
- [Stop job](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-stop.html): Learn how to stop a RAG evaluation job that is in progress in Amazon Bedrock.
- [Delete job](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-delete.html): Learn more about how to delete an Amazon Bedrock knowledge base evaluation job.

### [Reports and metrics for knowledge base evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-report.html)

Learn more about the dashboard report and metrics to help you evaluate an Amazon Bedrock knowledge base.

- [Results: RAG evaluations using LLMs](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html): Learn more about the dashboard report and metrics for Amazon Bedrock knowledge base evaluations that use LLMs.
- [CORS requirements](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security-cors.html): Learn about the CORS configuration requirements for Amazon S3 buckets used with Amazon Bedrock model evaluation jobs.

### [Reports and metrics for model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report.html)

Learn more about how the reports and metrics of model evaluation jobs are saved, and how to view them

- [Review metrics for an automated model evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report-programmatic.html): You can review the metrics presented in a report for an automatic model evaluation job using the Amazon Bedrock console.
- [Review a human model evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report-human-customer.html): You can review the data for human evaluation presented in a report using the Amazon Bedrock console.
- [Understand Amazon S3 output from a model evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report-s3.html): The output from a model evaluation job is saved in the Amazon S3 bucket you specified when you created the model evaluation job.

### [Data management and encryption in Amazon Bedrock evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-data-management.html)

Learn how Amazon Bedrock manages and encrypts data during model evaluation jobs to maintain security and privacy.

- [Key policy requirements](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security-kms.html): Every AWS KMS key must have exactly one key policy.
- [IAM policy requirements](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security-data.html): Amazon Bedrock uses the following IAM and AWS KMS permissions to use your AWS KMS key to decrypt your files and access them.
- [Data encryption for knowledge base evaluation jobs](https://docs.aws.amazon.com/bedrock/latest/userguide/rag-evaluation-security-data.html): During a knowledge base evaluation job, Amazon Bedrock makes a temporary copy of your data.
- [Management events](https://docs.aws.amazon.com/bedrock/latest/userguide/cloudtrail-events-in-model-evaluations.html): Learn about AWS CloudTrail management events generated during Amazon Bedrock model evaluation jobs for auditing and monitoring.

### [Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html)

Learn about how to create and store prompts in a library in Amazon Bedrock.

- [Supported Regions and models](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-supported.html): Learn about Regional and model support for Prompt management.
- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-prereq.html): Learn about prerequisites for prompt management.
- [Create a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html): Learn about how to create prompts using Prompt management in Amazon Bedrock.
- [View information about prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-view.html): Learn about how to view information about prompts using Prompt management in Amazon Bedrock.
- [Modify a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-modify.html): Learn about how to modify prompts using Prompt management in Amazon Bedrock.
- [Test a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-test.html): Learn about how to test prompts using Prompt management in Amazon Bedrock.
- [Optimize a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html): Learn how to optimize prompts in Amazon Bedrock.

### [Deploy to your application using versions](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-deploy.html)

Learn about how to deploy prompts using Prompt management in Amazon Bedrock by creating and managing versions of them.

- [Create a version](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-version-create.html): Learn about how to create a version of a prompt using Prompt management in Amazon Bedrock.
- [View information about versions](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-version-view.html): Learn about how to view information about a version of a prompt using Prompt management in Amazon Bedrock.
- [Compare versions](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-version-compare.html): Learn about how to compare versions of a prompt using Prompt management in Amazon Bedrock.
- [Delete a version](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-version-delete.html): Learn about how to delete a version of a prompt using Prompt management in Amazon Bedrock.
- [Delete a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-delete.html): Learn about how to delete prompts using Prompt management in Amazon Bedrock.
- [Run code samples](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-code-ex.html): Run some code samples to test out Prompt management capabilities.

### [Agents: Automate tasks](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)

Learn about how to set up conversational agents using Amazon Bedrock

- [How Amazon Bedrock Agents work](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-how.html)
- [Supported Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-supported.html): Learn about Regional and model support for Amazon Bedrock Agents.

### [Tutorial: Building a simple agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial.html)

Learn how to create and configure an Amazon Bedrock agent using the AWS Management Console.

- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial-prereq.html): Requirements needed before starting the Amazon Bedrock agent tutorial.
- [Step 1: Create a Lambda function](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial-step1.html): Set up a Lambda function that will provide date and time information to your agent.
- [Step 2: Create an Amazon Bedrock agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial-step2.html): Create your first Amazon Bedrock agent and prepare it for development.
- [Step 3: Test the agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial-step3.html): Test your agent by sending prompts and observing how it responds with date and time information.
- [Step 4: Deploy the agent with an alias](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial-step4.html): Create a version of your agent and deploy it with an alias to make it available for use.
- [Step 5: Call the agent from Python code](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial-step5.html): In this step, you'll learn how to programmatically interact with your agent using the AWS SDK for Python (Boto).
- [Step 6: Clean up resources](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial-step6.html): Remove the resources created during this tutorial to avoid incurring unnecessary charges.
- [Additional resources](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial-resources.html): Links to additional documentation and resources related to Amazon Bedrock agents.

### [Build and modify agents for your application](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-build-modify.html)

Learn how to build and modify an agent with Amazon Bedrock to help your customers perform tasks.

- [Configure your agent using conversational builder](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create-cb.html): Conversational builder is an interactive assistant that helps in configuring an agent for you.

### [Configure an inline agent at runtime](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create-inline.html)

Learn how to configure an agent dynamically at runtime

- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/inline-agent-prereq.html): Complete the prerequisites for invoking an inline agent
- [Invoke an inline agent](https://docs.aws.amazon.com/bedrock/latest/userguide/inline-agent-invoke.html): Learn how to configure an agent dynamically at runtime

### [Create and configure agent manually](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create.html)

- [Prerequisites for creating an agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-prereq.html): Learn about the prerequisites to fulfill before you creating an agent in Amazon Bedrock.
- [View information about an agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-view.html): Learn how to view information about an agent in Amazon Bedrock.
- [Modify an agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-edit.html): Learn how to modify an agent in Amazon Bedrock.
- [Delete an agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-delete.html): Learn how to delete an agent in Amazon Bedrock.

### [Use action groups to define actions for your agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html)

Learn about how to create an action group for your agent in Amazon Bedrock.

### [Define actions in the action group](https://docs.aws.amazon.com/bedrock/latest/userguide/action-define.html)

You can define action groups in one of the following ways (you can use different methods for different action groups):

- [Define function details](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-function.html): Learn how to write function details for action groups in your Amazon Bedrock agent.
- [Define OpenAPI schemas](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html): Learn how to write API schemas for action groups in your Amazon Bedrock agent.

### [Handle fulfillment of the action](https://docs.aws.amazon.com/bedrock/latest/userguide/action-handle.html)

When you configure the action group, you also select one of the following options for the agent to pass the information and parameters that it receives from the user:

- [Configure Lambda functions](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html): Learn how to write Lambda functions for your Amazon Bedrock agent.
- [Return control to the agent developer](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html): Learn how to return control to the agent developer by sending the information that your Amazon Bedrock agent elicits from the user in an InvokeAgent response.
- [Get user confirmation before invoking action](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-userconfirmation.html): Learn how to safeguard ,your application from malicious prompt injections.
- [Add an action group to your agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-add.html): After setting up the OpenAPI schema and Lambda function for your action group, you can create the action group.
- [View information about an action group](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-view.html): Learn how to view information about an action group in Amazon Bedrock.
- [Modify an action group](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-edit.html): Learn how to edit an action group in Amazon Bedrock.
- [Delete an action group](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-delete.html): Learn how to delete an action group in Amazon Bedrock.

### [Use multi-agent collaboration for complex tasks](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html)

Learn how to build a multi-agent collaboration team.

- [Supported Regions and models for multi-agent collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/multi-agents-supported.html): Supported models
- [Create multi-agent collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/create-multi-agent-collaboration.html): Creating a multi-agent collaboration comprises of the following steps:
- [Disassociate collaborator agent](https://docs.aws.amazon.com/bedrock/latest/userguide/disassociate-collaborator-agent.html): You can disassociate one or more collaborator agents from the supervisor agent in the Amazon Bedrock console, using the APIs, using the AWS CLI, or by using the AWS SDK.
- [Disable a multi-agent collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/disable-multi-agents-collaboration.html): You can disable multi-agent collaboration at any time.

### [Configure agent to request information from user](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-user-input.html)

Learn how to configure user input for your agent Amazon Bedrock.

- [Enable user input](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-enable-user-input.html): learn how to enable user input for your agent Amazon Bedrock.
- [Disable user input](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-disable-user-input.html): Learn how to disable user input in Amazon Bedrock.

### [Augment response generation for your agent with knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-kb-add.html)

Learn how to associate a knowledge base with your agent in Amazon Bedrock.

- [View information about an agent-knowledge base association](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-kb-view.html): Learn how to view information about an agent-knowledge base in Amazon Bedrock.
- [Modify an agent-knowledge base association](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-kb-edit.html): Learn how to edit an agent-knowledge base association in Amazon Bedrock.
- [Disassociate a knowledge base from an agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-kb-delete.html): Learn how to disassociate a knowledge base from an agent in Amazon Bedrock.

### [Retain conversational context using memory](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory.html)

Learn how to use memory for your agent in Amazon Bedrock.

- [Enable agent memory](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-configure-memory.html): Learn how to configure memory for your agent in Amazon Bedrock.
- [View memory sessions](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory-view.html): Learn how to view sessions stored in the memory in Amazon Bedrock agent.
- [Delete session summaries](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory-delete.html): Learn how to delete session summaries
- [Disable agent memory](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory-disable.html): Learn how to disable memory for your Amazon Bedrock agent.
- [Enable memory summarization log delivery](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory-log-delivery-enable.html): To enable logging for your Amazon Bedrock agent alias, use the PutDeliverySource CloudWatch API.

### [Generate, run, and test code with code interpretation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-code-interpretation.html)

Learn how to use code interpretation to generate and test your code in Amazon Bedrock.

- [Enable code interpretation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-enable-code-interpretation.html): learn how to enable code interpretation to generate and test your code in Amazon Bedrock.
- [Test code interpretation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test-code-interpretation.html): Test code interpretation in Amazon Bedrock.
- [Disable code interpretation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-disable-code-interpretation.html): Learn how to disable code interpretation in Amazon Bedrock.
- [Implement safeguards for your application](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-guardrail.html): To implement safeguards and prevent unwanted behavior from model responses or user messages, associate a guardrail with your agent.
- [Provision additional throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-pt.html): To increase the rate and number of tokens that the agent can process during model inference, associate a Provisioned Throughput that you've purchased for the model that your agent is using.

### [Configure an agent to use computer use tools](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-computer-use.html)

Configure an Amazon Bedrock Agent to complete tasks with computer use tools

- [Specify the computer use tools for the agent in an action group](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-computer-use-create-action-group.html): Specify the computer use tools for the agent in an action group.
- [Handle computer use tool requests from agents in conversations](https://docs.aws.amazon.com/bedrock/latest/userguide/agent-computer-use-handle-tools.html): Learn how to handle computer use tool from agents in conversations.

### [Test and troubleshoot agent behavior](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html)

Learn how to test your Amazon Bedrock agent.

### [Track agent's step-by-step reasoning process using trace](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)

Learn how to trace your agent's step-by-step reasoning.

- [View the trace](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-view.html): The following describes how to view the trace.

### [Customize agent for your use case](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-customize.html)

Learn how to customize your Amazon Bedrock agent.

### [Customize agent orchestration](https://docs.aws.amazon.com/bedrock/latest/userguide/orch-strategy.html)

Learn how to customize agent orchestration.

### [Enhance your agent's accuracy using advanced prompt templates](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html)

Learn how to modify base templates to better customize your agent's behavior.

- [Advanced prompt templates](https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts-templates.html): Learn how to modify the prompt templates.
- [Configure advanced prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/configure-advanced-prompts.html): You can configure advanced prompts in either the AWS Management Console or through the API.
- [Use placeholder variables in prompt templates](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-placeholders.html): You can use placeholder variables in agent prompt templates.
- [Write a custom parser Lambda function](https://docs.aws.amazon.com/bedrock/latest/userguide/lambda-parser.html): Each prompt template includes a parser Lambda function.
- [Customize your agent's behavior with custom orchestration](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-custom-orchestration.html): Learn how to create custom orchestration strategy for your agent
- [Control agent session context](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html): Learn how to use session attributes and prompt session attributes to provide context for your agents.
- [Optimize performance for agents using a single knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-optimize-performance.html): Learn how to optimize Amazon Bedrock agents that use a single knowledge base.
- [Working with models not yet optimized](https://docs.aws.amazon.com/bedrock/latest/userguide/working-with-models-not-yet-optimized.html): Learn how to use unoptimized Amazon Bedrock Agents

### [Deploy and use an agent in your application](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-deploy.html)

Learn how to create versions of your Amazon Bedrock agent and to create aliases to point to those versions.

### [Deploy an agent](https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent.html)

When you first create an Amazon Bedrock agent, you have a working draft version (DRAFT) and a test alias (TSTALIASID) that points to the working draft version.

- [Create an alias for your agent](https://docs.aws.amazon.com/bedrock/latest/userguide/deploy-agent-proc.html): The following procedure shows you how to create an alias and a version for your agent.
- [View information about versions of agents in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-version-view.html): After you create a version of your agent, you can view information about it or delete it.
- [Delete a version of an agent in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-version-delete.html): To learn how to delete a version of an agent, choose the tab for your preferred method, and then follow the steps:
- [View information about aliases of agents in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-alias-view.html): To learn how to view information about the aliases of an agent, choose the tab for your preferred method, and then follow the steps:
- [Edit an alias of an agent in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-alias-edit.html): To learn how to edit an alias of an agent, choose the tab for your preferred method, and then follow the steps:
- [Delete an alias of an agent in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-alias-delete.html): To learn how to delete an alias of an agent, choose the tab for your preferred method, and then follow the steps:
- [Invoke an agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-invoke-agent.html): Use your agent in an application by making an InvokeAgent request with an Agents for Amazon Bedrock runtime endpoint.

### [Prompt engineering concepts](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html)

Learn about prompt engineering in Amazon Bedrock.

- [What is prompt engineering?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-prompt-engineering.html): Definition of prompt engineering and use cases.
- [Intelligent prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html): Amazon Bedrock intelligent prompt routing provides a single serverless endpoint to efficiently route requests between different foundational models within the same model family.
- [Design a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html): Designing an appropriate prompt is an important step towards building a successful application using Amazon Bedrock models.
- [Prompt templates and examples for Amazon Bedrock text models](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-templates-and-examples.html): Collection of prompt templates to us with Amazon Bedrock.

### [Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html)

Amazon Bedrock Marketplace expands your model options for building generative AI applications on Amazon Bedrock.

- [Set up Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/setup-amazon-bedrock-marketplace.html): You can use the Amazon Bedrock Full Access policy to provide permissions to SageMaker AI.
- [Controlling Access to Amazon Bedrock Marketplace Models](https://docs.aws.amazon.com/bedrock/latest/userguide/control-amazon-bedrock-marketplace.html): You can use the Amazon Bedrock Full Access policy to provide permissions to SageMaker AI.
- [End-to-end workflow](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-end-to-end-workflow.html): After you've set up Amazon Bedrock Marketplace, you can use the following example code in your end-to-end workflow.
- [Discover a model](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-discover-a-model.html): You can discover both Amazon Bedrock Marketplace models and Amazon Bedrock serverless models from the model catalog.
- [Subscribe to a model](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-subscribe-to-a-model.html): To use a model from Amazon Bedrock Marketplace, you subscribe to the model.
- [Deploy a model](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-deploy-a-model.html): After you've subscribed to a model, you deploy it to a SageMaker AI endpoint.
- [Bring your own endpoint](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-bring-your-own-endpoint.html): You can register an endpoint hosting an Amazon Bedrock AWS Marketplace model you've created in SageMaker AI.
- [Call the endpoint](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-call-the-endpoint.html): You can start using your model after you've deployed it to an endpoint.
- [Manage your endpoints](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-manage-your-endpoints.html): You view and manage your Amazon Bedrock Marketplace model endpoints in the following ways:
- [Model compatibility](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-model-reference.html): All models can use the InvokeModel operation.

### [Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html)

Learn about how to create and configure flows for Amazon Bedrock

### [How it works](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html)

Learn about the key concepts and terms for Amazon Bedrock Flows and how to create nodes and connections.

- [Key definitions](https://docs.aws.amazon.com/bedrock/latest/userguide/key-definitions-flow.html): The following list introduces you to the basic concepts of Amazon Bedrock Flows.
- [Define inputs with expressions](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-expressions.html): When you configure the inputs for a node, you must define it in relation to the whole input that will enter the node.
- [Node types](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-nodes.html): Amazon Bedrock Flows provides the following node types to build your flow.
- [Supported Regions and models](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-supported.html): Learn about regional and model support for flows.
- [Prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-prereq.html): Learn about the prerequisites to fulfill before you create your flows in Amazon Bedrock.

### [Create and design a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html)

Learn how to create a flow with Amazon Bedrock to help your customers perform tasks.

- [Create your first flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-get-started.html): Learn how to create a flow with Amazon Bedrock to help your customers perform tasks.
- [Design a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-design.html): In this section you design an Amazon Bedrock flow.

### [Try example flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-ex.html)

Try out some example simple flows to understand how it works.

- [Create a flow with a single prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-ex-prompt.html): The following image shows a flow consisting of a single prompt, defined inline in the node.
- [Create a flow with a condition node](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-ex-condition.html): The following image shows a flow with one condition node returns one of three possible values based on the condition that is fulfilled:
- [Use a template to create a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-templates.html): Learn about how to create and configure flows for Amazon Bedrock
- [View information about flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-view.html): Learn how to view information about flows.
- [Modify a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-modify.html): Learn how to modify a flow.
- [Include guardrails in your flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-guardrails.html): Learn how to include guardrails in a flow with Amazon Bedrock to block unwanted content.

### [Test a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html)

Learn how to test your flow.

- [Track each step in your flow by viewing its trace](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html): When you invoke a flow, you can view the trace to see the inputs to and outputs from each node.
- [Run a flow asynchronously](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create-async.html): Learn how Amazon Bedrock flow executions let you run flows for longer durations so that your application can perform interim tasks.

### [Deploy to your application using versions and aliases](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html)

Learn how to deploy your flow to production by publishing versions and creating alias.

- [Create a version](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-version-create.html): Learn how to create a static version of your flow.
- [View information about versions](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-version-view.html): Learn how to view information about versions of your flow
- [Delete a version](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-version-delete.html): Learn how to delete a version of your flow
- [Create an alias](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-alias-create.html): Learn how to create an alias of your flow that you can point to a version.
- [View information about aliases](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-alias-view.html): Learn how to view information about aliases of your flow
- [Modify an alias](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-alias-modify.html): Learn how to modify an alias of your flow
- [Delete an alias](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-alias-delete.html): Learn how to delete an alias of your flow
- [Invoke a Lambda function in a different AWS account](https://docs.aws.amazon.com/bedrock/latest/userguide/flow-cross-account-lambda.html): An Amazon Bedrock flow can invoke a AWS Lambda function that is in a different AWS account from the flow.
- [Converse with a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-multi-turn-invocation.html)
- [Run code samples](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-code-ex.html): Run some code samples to test out Amazon Bedrock Flows capabilities.
- [Delete a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-delete.html): Learn how to delete a flow.

### [Session management](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html)

Learn about using Amazon Bedrock session APIs to store and retrieve conversation history and context for customer interactions with open-source agents.

- [Session encryption](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions-encryption.html): Learn about default session encryption and how to use a customer managed AWS KMS key.
- [Create a session](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions-create.html): Create a session
- [Store conversation history and context in a session](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions-store-coversation.html): Learn how to upload state checkpoints, including text and images, to your session
- [Retrieve conversation history and context from a session](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions-retrieve-coversation.html): Learn how to retrieve state checkpoints, including text and images, from your session
- [End a session when the user ends the conversation](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions-end-session.html): Learn how to end a session when the user ends the conversation.
- [Delete a session and all of its data](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions-delete-session.html): Learn how to delete a session and all of its data.
- [Manage sessions with BedrockSessionSaver LangGraph library](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions-opensource-library.html): Learn how to store and retrieve conversation history and context in LangGraph with the BedrockSessionSaver library.


## [Code examples](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples.html)

### [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock.html)

Code examples that show how to use Amazon Bedrock with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock_basics.html)

The following code examples show how to use the basics of Amazon Bedrock with AWS SDKs.

- [Hello Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock_example_bedrock_Hello_section.html): Hello Amazon Bedrock

### [Actions](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock_actions.html)

The following code examples show how to use Amazon Bedrock with AWS SDKs.

- [GetFoundationModel](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock_example_bedrock_GetFoundationModel_section.html): Use GetFoundationModel with an AWS SDK
- [ListFoundationModels](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock_example_bedrock_ListFoundationModels_section.html): Use ListFoundationModels with an AWS SDK

### [Scenarios](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock_scenarios.html)

The following code examples show how to use Amazon Bedrock with AWS SDKs.

- [Orchestrate generative AI applications with Step Functions](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock_example_cross_ServerlessPromptChaining_section.html): Build and orchestrate generative AI applications with Amazon Bedrock and Step Functions

### [Amazon Bedrock Runtime](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime.html)

Code examples that show how to use Amazon Bedrock Runtime with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_basics.html)

The following code examples show how to use the basics of Amazon Bedrock Runtime with AWS SDKs.

- [Hello Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Hello_section.html): Hello Amazon Bedrock

### [Scenarios](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_scenarios.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [Create a playground application to interact with Amazon Bedrock foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_cross_FMPlayground_section.html): Create a sample application that offers playgrounds to interact with Amazon Bedrock foundation models using an AWS SDK
- [Create and invoke a managed prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-agent_GettingStartedWithBedrockPrompts_section.html): An end-to-end example showing how to create and invoke Amazon Bedrock managed prompts using an AWS SDK
- [Generate videos from text prompts using Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Scenario_GenerateVideos_NovaReel_section.html): Generate videos from text prompts using Amazon Bedrock and Nova-Reel
- [Invoke multiple foundation models on Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Scenario_InvokeModels_section.html): Invoke multiple foundation models on Amazon Bedrock
- [Orchestrate generative AI applications with Step Functions](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_cross_ServerlessPromptChaining_section.html): Build and orchestrate generative AI applications with Amazon Bedrock and Step Functions
- [Tool use with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Scenario_ToolUse_section.html): A tool use example illustrating how to connect AI models on Amazon Bedrock with a custom tool or API

### [Amazon Nova](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_amazon_nova.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Converse_AmazonNovaText_section.html): Invoke Amazon Nova on Amazon Bedrock using Bedrock's Converse API
- [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_ConverseStream_AmazonNovaText_section.html): Invoke Amazon Nova on Amazon Bedrock using Bedrock's Converse API with a response stream
- [Document understanding](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_AmazonNova_section.html): Send and process a document with Amazon Nova on Amazon Bedrock
- [Scenario: Tool use with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Scenario_ToolUseDemo_AmazonNova_section.html): A tool use demo illustrating how to connect AI models on Amazon Bedrock with a custom tool or API

### [Amazon Nova Canvas](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_amazon_nova_canvas.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_AmazonNovaImageGeneration_section.html): Invoke Amazon Nova Canvas on Amazon Bedrock to generate an image

### [Amazon Nova Reel](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_amazon_nova_reel.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [Text-to-video](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Scenario_AmazonNova_TextToVideo_section.html): Use Amazon Nova Reel to generate a video from a text prompt

### [Amazon Titan Image Generator](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_amazon_titan_image_generator.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_TitanImageGenerator_section.html): Invoke Amazon Titan Image on Amazon Bedrock to generate an image

### [Amazon Titan Text](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_amazon_titan_text.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_TitanText_section.html): Invoke Amazon Titan Text models on Amazon Bedrock using the Invoke Model API

### [Amazon Titan Text Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_amazon_titan_text_embeddings.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_TitanTextEmbeddings_section.html): Invoke Amazon Titan Text Embeddings on Amazon Bedrock

### [Anthropic Claude](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_anthropic_claude.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Converse_AnthropicClaude_section.html): Invoke Anthropic Claude on Amazon Bedrock using Bedrock's Converse API
- [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_ConverseStream_AnthropicClaude_section.html): Invoke Anthropic Claude on Amazon Bedrock using Bedrock's Converse API with a response stream
- [Document understanding](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_AnthropicClaude_section.html): Send and process a document with Anthropic Claude on Amazon Bedrock
- [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_AnthropicClaude_section.html): Invoke Anthropic Claude on Amazon Bedrock using the Invoke Model API
- [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_AnthropicClaude_section.html): Invoke Anthropic Claude models on Amazon Bedrock using the Invoke Model API with a response stream
- [Reasoning](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Converse_AnthropicClaudeReasoning_section.html): Use Anthropic Claude 3.7 Sonnet's reasoning capability on Amazon Bedrock
- [Reasoning with a streaming response](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_ConverseStream_AnthropicClaudeReasoning_section.html): Use Anthropic Claude 3.7 Sonnet's reasoning capability on Amazon Bedrock
- [Scenario: Tool use with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Scenario_ToolUseDemo_AnthropicClaude_section.html): A tool use demo illustrating how to connect AI models on Amazon Bedrock with a custom tool or API

### [Cohere Command](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_cohere_command.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Converse_CohereCommand_section.html): Invoke Cohere Command on Amazon Bedrock using Bedrock's Converse API
- [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_ConverseStream_CohereCommand_section.html): Invoke Cohere Command on Amazon Bedrock using Bedrock's Converse API with a response stream
- [Document understanding](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_CohereCommand_section.html): Send and process a document with Cohere Command models on Amazon Bedrock
- [InvokeModel: Command R and R+](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_CohereCommandR_section.html): Invoke Cohere Command R and R+ on Amazon Bedrock using the Invoke Model API
- [InvokeModelWithResponseStream: Command R and R+](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_CohereCommandR_section.html): Invoke Cohere Command R and R+ on Amazon Bedrock using the Invoke Model API with a response stream
- [Scenario: Tool use with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Scenario_ToolUseDemo_CohereCommand_section.html): A tool use demo illustrating how to connect AI models on Amazon Bedrock with a custom tool or API

### [DeepSeek](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_deepseek.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [Document understanding](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_DeepSeek_section.html): Send and process a document with DeepSeek on Amazon Bedrock

### [Meta Llama](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_meta_llama.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Converse_MetaLlama_section.html): Invoke Meta Llama on Amazon Bedrock using Bedrock's Converse API
- [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_ConverseStream_MetaLlama_section.html): Invoke Meta Llama on Amazon Bedrock using Bedrock's Converse API with a response stream
- [Document understanding](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_MetaLlama_section.html): Send and process a document with Llama on Amazon Bedrock
- [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_MetaLlama3_section.html): Invoke Meta Llama on Amazon Bedrock using the Invoke Model API
- [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_MetaLlama3_section.html): Invoke Meta Llama on Amazon Bedrock using the Invoke Model API with a response stream

### [Mistral AI](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_mistral_ai.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [Converse](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_Converse_Mistral_section.html): Invoke Mistral on Amazon Bedrock using Bedrock's Converse API
- [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_ConverseStream_Mistral_section.html): Invoke Mistral on Amazon Bedrock using Bedrock's Converse API with a response stream
- [Document understanding](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_Mistral_section.html): Send and process a document with Mistral models on Amazon Bedrock
- [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_MistralAi_section.html): Invoke Mistral AI models on Amazon Bedrock using the Invoke Model API
- [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_MistralAi_section.html): Invoke Mistral AI models on Amazon Bedrock using the Invoke Model API with a response stream

### [Stable Diffusion](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-runtime_stable_diffusion.html)

The following code examples show how to use Amazon Bedrock Runtime with AWS SDKs.

- [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_StableDiffusion_section.html): Invoke Stability.ai Stable Diffusion XL on Amazon Bedrock to generate an image

### [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-agent.html)

Code examples that show how to use Amazon Bedrock Agents with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-agent_basics.html)

The following code examples show how to use the basics of Amazon Bedrock Agents with AWS SDKs.

- [Hello Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_Hello_section.html): Hello Amazon Bedrock Agents

### [Actions](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-agent_actions.html)

The following code examples show how to use Amazon Bedrock Agents with AWS SDKs.

- [CreateAgent](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_CreateAgent_section.html): Use CreateAgent with an AWS SDK
- [CreateAgentActionGroup](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_CreateAgentActionGroup_section.html): Use CreateAgentActionGroup with an AWS SDK
- [CreateAgentAlias](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_CreateAgentAlias_section.html): Use CreateAgentAlias with an AWS SDK
- [CreateFlow](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_CreateFlow_section.html): Use CreateFlow with an AWS SDK
- [CreateFlowAlias](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_CreateFlowAlias_section.html): Use CreateFlowAlias with an AWS SDK
- [CreateFlowVersion](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_CreateFlowVersion_section.html): Use CreateFlowVersion with an AWS SDK
- [CreateKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_CreateKnowledgeBase_section.html): Use CreateKnowledgeBase with an AWS SDK
- [CreatePrompt](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_CreatePrompt_section.html): Use CreatePrompt with an AWS SDK
- [CreatePromptVersion](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_CreatePromptVersion_section.html): Use CreatePromptVersion with an AWS SDK
- [DeleteAgent](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_DeleteAgent_section.html): Use DeleteAgent with an AWS SDK
- [DeleteAgentAlias](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_DeleteAgentAlias_section.html): Use DeleteAgentAlias with an AWS SDK
- [DeleteFlow](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_DeleteFlow_section.html): Use DeleteFlow with an AWS SDK
- [DeleteFlowAlias](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_DeleteFlowAlias_section.html): Use DeleteFlowAlias with an AWS SDK
- [DeleteFlowVersion](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_DeleteFlowVersion_section.html): Use DeleteFlowVersion with an AWS SDK
- [DeleteKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_DeleteKnowledgeBase_section.html): Use DeleteKnowledgeBase with an AWS SDK
- [DeletePrompt](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_DeletePrompt_section.html): Use DeletePrompt with an AWS SDK
- [GetAgent](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_GetAgent_section.html): Use GetAgent with an AWS SDK
- [GetFlow](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_GetFlow_section.html): Use GetFlow with an AWS SDK
- [GetFlowVersion](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_GetFlowVersion_section.html): Use GetFlowVersion with an AWS SDK
- [GetKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_GetKnowledgeBase_section.html): Use GetKnowledgeBase with an AWS SDK
- [GetPrompt](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_GetPrompt_section.html): Use GetPrompt with an AWS SDK
- [ListAgentActionGroups](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_ListAgentActionGroups_section.html): Use ListAgentActionGroups with an AWS SDK
- [ListAgentKnowledgeBases](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_ListAgentKnowledgeBases_section.html): Use ListAgentKnowledgeBases with an AWS SDK
- [ListAgents](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_ListAgents_section.html): Use ListAgents with an AWS SDK
- [ListFlowAliases](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_ListFlowAliases_section.html): Use ListFlowAliases with an AWS SDK
- [ListFlowVersions](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_ListFlowVersions_section.html): Use ListFlowVersions with an AWS SDK
- [ListFlows](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_ListFlows_section.html): Use ListFlows with an AWS SDK
- [ListKnowledgeBases](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_ListKnowledgeBases_section.html): Use ListKnowledgeBases with an AWS SDK
- [ListPrompts](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_ListPrompts_section.html): Use ListPrompts with an AWS SDK
- [PrepareAgent](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_PrepareAgent_section.html): Use PrepareAgent with an AWS SDK
- [PrepareFlow](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_PrepareFlow_section.html): Use PrepareFlow with an AWS SDK
- [UpdateFlow](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_UpdateFlow_section.html): Use UpdateFlow with an AWS SDK
- [UpdateFlowAlias](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_UpdateFlowAlias_section.html): Use UpdateFlowAlias with an AWS SDK
- [UpdateKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_UpdateKnowledgeBase_section.html): Use UpdateKnowledgeBase with an AWS SDK

### [Scenarios](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-agent_scenarios.html)

The following code examples show how to use Amazon Bedrock Agents with AWS SDKs.

- [Create and invoke a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_GettingStartedWithBedrockFlows_section.html): An end-to-end example showing how to create and invoke an Amazon Bedrock flow using an AWS SDK
- [Create and invoke a managed prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_GettingStartedWithBedrockPrompts_section.html): An end-to-end example showing how to create and invoke Amazon Bedrock managed prompts using an AWS SDK
- [Create and invoke an agent](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_bedrock-agent_GettingStartedWithBedrockAgents_section.html): An end-to-end example showing how to create and invoke Amazon Bedrock Agents using an AWS SDK
- [Orchestrate generative AI applications with Step Functions](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent_example_cross_ServerlessPromptChaining_section.html): Build and orchestrate generative AI applications with Amazon Bedrock and Step Functions

### [Amazon Bedrock Agents Runtime](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-agent-runtime.html)

Code examples that show how to use Amazon Bedrock Agents Runtime with an AWS SDK.

### [Basics](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-agent-runtime_basics.html)

The following code examples show how to use the basics of Amazon Bedrock Agents Runtime with AWS SDKs.

- [Learn the basics](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent-runtime_example_bedrock-agent-runtime_Scenario_ConverseWithFlow_section.html): Converse with an Amazon Bedrock flow

### [Actions](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-agent-runtime_actions.html)

The following code examples show how to use Amazon Bedrock Agents Runtime with AWS SDKs.

- [InvokeAgent](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent-runtime_example_bedrock-agent-runtime_InvokeAgent_section.html): Use InvokeAgent with an AWS SDK
- [InvokeFlow](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent-runtime_example_bedrock-agent-runtime_InvokeFlow_section.html): Use InvokeFlow with an AWS SDK

### [Scenarios](https://docs.aws.amazon.com/bedrock/latest/userguide/service_code_examples_bedrock-agent-runtime_scenarios.html)

The following code examples show how to use Amazon Bedrock Agents Runtime with AWS SDKs.

- [Create and invoke a flow](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent-runtime_example_bedrock-agent_GettingStartedWithBedrockFlows_section.html): An end-to-end example showing how to create and invoke an Amazon Bedrock flow using an AWS SDK
- [Orchestrate generative AI applications with Step Functions](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-agent-runtime_example_cross_ServerlessPromptChaining_section.html): Build and orchestrate generative AI applications with Amazon Bedrock and Step Functions


## [References/Advanced](https://docs.aws.amazon.com/bedrock/latest/userguide/references.html)

- [Key terminology](https://docs.aws.amazon.com/bedrock/latest/userguide/key-definitions.html): Learn essential generative AI and Amazon Bedrock terminology to understand foundation models, model inference, and advanced features.
- [Working with AWS SDKs](https://docs.aws.amazon.com/bedrock/latest/userguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
- [API Error Codes](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html): Learn about common Amazon Bedrock API errors, their causes, and how to resolve them when using Amazon Bedrock services.

### [Detailed getting started guide](https://docs.aws.amazon.com/bedrock/latest/userguide/detailed-getting-started.html)

Content coming soon.

- [Get started in the console](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-console.html): Get started in the console with Amazon Bedrock.

### [Get started with the API](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api.html)

Learn how to use the APIs with Amazon Bedrock foundation models.

- [Get started with a 30-day Amazon Bedrock API key](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api-keys.html): Learn how to quickly generate a long-term Amazon Bedrock API key that lasts 30 days and use it to make your first Converse API call.
- [Run examples with the AWS CLI](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api-ex-cli.html): Test example API requests with the AWS CLI.
- [Run examples with the AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api-ex-python.html): Test example API requests through the AWS SDK for Python (Boto3).
- [Run examples with a SageMaker AI notebook](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-api-ex-sm.html): This section guides you through trying out some common operations in Amazon Bedrock with an Amazon SageMaker AI notebook to test that your Amazon Bedrock role permissions are set up properly.

### [Flow tutorial](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-mortgage-flow.html)

This tutorial shows you how to create a complete mortgage processing system using Amazon Bedrock builder tools.

- [Templates](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-mortgage-flow-template.html): The cloudformation-mortgage-flow-setup.zip file that you download contains the following files:
- [Mortgage processing flow details](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-mortgage-flow-details.html): The visual representation of the mortgage processing flow in the AWS Management Console is as follows:
- [Document history](https://docs.aws.amazon.com/bedrock/latest/userguide/doc-history.html): Find the revision dates and related releases for Amazon Bedrock.
