# Source: https://docs.aws.amazon.com/nova/latest/nova2-userguide/llms.txt

# Amazon Nova Developer Guide for Amazon Nova 2

> Developer guide for Amazon Nova 2 foundation models organized by developer workflow

- [What is Amazon Nova 2?](https://docs.aws.amazon.com/nova/latest/nova2-userguide/what-is-nova-2.html)
- [What's new in Amazon Nova 2](https://docs.aws.amazon.com/nova/latest/nova2-userguide/whats-new.html)
- [Responsible use](https://docs.aws.amazon.com/nova/latest/nova2-userguide/responsible-use.html)
- [Quotas](https://docs.aws.amazon.com/nova/latest/nova2-userguide/quotas.html)
- [Monitoring](https://docs.aws.amazon.com/nova/latest/nova2-userguide/monitoring-overview.html)
- [Security](https://docs.aws.amazon.com/nova/latest/nova2-userguide/security.html)
- [Create resources with CloudFormation](https://docs.aws.amazon.com/nova/latest/nova2-userguide/creating-resources-with-cloudformation.html)
- [Document history](https://docs.aws.amazon.com/nova/latest/nova2-userguide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-nova-2.html)

- [Getting started in the console](https://docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-console.html): Get started in the console with Amazon Nova.
- [Getting started with the API](https://docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-api.html): Get started with the Amazon Nova API.


## [Core inference](https://docs.aws.amazon.com/nova/latest/nova2-userguide/core-inference.html)

- [Using the Converse API](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-converse-api.html): The Converse API provides a unified interface for interacting with Amazon Nova models.
- [Using the Invoke API](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-invoke-api.html): The Invoke API provides direct access to Amazon Nova models with more ability to control the request and response format.
- [Streaming responses](https://docs.aws.amazon.com/nova/latest/nova2-userguide/streaming-responses.html): Streaming allows you to receive model responses incrementally as they are generated, providing a more interactive user experience.
- [Using Amazon Nova embeddings](https://docs.aws.amazon.com/nova/latest/nova2-userguide/embeddings.html): Amazon Nova Multimodal Embeddings is a multimodal embeddings model for agentic RAG and semantic search applications.
- [On-demand inference](https://docs.aws.amazon.com/nova/latest/nova2-userguide/on-demand-inference.html): On-demand inference provides serverless access to Amazon Nova models without requiring provisioned capacity.


## [Using Nova capabilities](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-nova-capabilities.html)

- [Reasoning](https://docs.aws.amazon.com/nova/latest/nova2-userguide/reasoning-capabilities.html): Amazon Nova 2 Lite supports extended thinking, which is disabled by default.
- [Multimodal understanding](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-multimodal-models.html): Amazon Nova 2 Lite can understand multiple input modalities.


## [Speech-to-Speech](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-conversational-speech.html)

- [Getting started](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-getting-started.html): The following sections provide an example and step-by-step explanation of how to implement a simple, real-time audio streaming application using Amazon Nova 2 Sonic.
- [Code examples](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-code-examples.html): These code examples help you quickly get started with Amazon Nova 2 Sonic.
- [Voice conversation prompts](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html): Nova 2 introduces Speech Prompts â a specialized prompting capability designed to control speech-specific transcription formatting for Hindi.

### [Core concepts](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-core-concepts.html)

Amazon Nova 2 Sonic uses a bidirectional streaming architecture with structured events for real-time conversational AI.

- [Event lifecycle](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-event-lifecycle.html): The following diagram illustrates the complete bi-directional streaming event lifecycle:
- [Event flow sequence](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-event-flow.html): A typical conversation follows this event sequence:
- [Handling input events with the bidirectional API](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-input-events.html): The bidirectional Stream API uses an event-driven architecture with structured input and output events.
- [Handling output events with the bidirectional API](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-output-events.html): When the Amazon Nova Sonic model responds, it follows a structured event sequence.
- [Barge-in](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-barge-in.html): Barge-in allows users to interrupt the AI assistant while it's speaking, just like in natural human conversations.
- [Turn-taking controllability](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-turn-taking.html): Turn-taking is a fundamental aspect of natural conversation.
- [Cross-modal input](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-cross-modal.html): Amazon Nova 2 Sonic now supports cross-modal input, allowing you to send text messages in addition to voice input during a conversation session.
- [Language support and multilingual capabilities](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-language-support.html): Amazon Nova 2 Sonic provides a diverse selection of voices across multiple languages, enabling you to create conversational AI applications that feel natural and culturally appropriate for your users.
- [Managing chat history](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-chat-history.html): Amazon Nova 2 Sonic responses include ASR (Automatic Speech Recognition) transcripts for both user and assistant voices.
- [Tool configuration](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-tool-configuration.html): Amazon Nova 2 Sonic supports tool use (also known as function calling), allowing the model to request external information or actions during conversations, such as API calls, database queries, or custom code functions.
- [Asynchronous tool calling](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-async-tools.html): Unlike traditional synchronous tool calling where the AI waits silently for tool results, Amazon Nova 2 Sonic's asynchronous approach allows it to:
- [Integrations](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-integrations.html): Amazon Nova 2 Sonic can be integrated with various frameworks and platforms to build conversational AI applications.


## [Advanced systems with Nova](https://docs.aws.amazon.com/nova/latest/nova2-userguide/advanced-systems.html)

- [Extended Thinking](https://docs.aws.amazon.com/nova/latest/nova2-userguide/extended-thinking.html): Amazon Nova 2 Lite introduces extended thinking capabilities that enable the model to engage in deeper reasoning for complex problems.
- [Tool use](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-tools.html): Learn how to extend Amazon Nova capabilities with external tools and APIs through function calling.
- [Building AI agents](https://docs.aws.amazon.com/nova/latest/nova2-userguide/building-ai-agents.html): Amazon Nova models are optimized for building AI agents with Amazon Nova Act.
- [Web Grounding](https://docs.aws.amazon.com/nova/latest/nova2-userguide/web-grounding.html): Enable Amazon Nova to search the web and provide responses with citations using Web Grounding.


## [Prompt engineering](https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompt-engineering-guide.html)

- [What is prompt engineering](https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompting-what-is.html): Prompt engineering refers to the practice of optimizing textual input to a large language model (LLM) to improve output and receive the responses you want.

### [Best practices](https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompting-best-practices.html)

Learn best practices for prompting Amazon Nova text models to get high-quality responses.

- [Create precise prompts](https://docs.aws.amazon.com/nova/latest/nova2-userguide/create-precise-prompts.html): Crafting specific user queries is crucial in prompt engineering.
- [Bring focus to sections of the prompt](https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompting-bring-focus.html): Amazon Nova 2 models can pay close attention to specific parts in the prompt by formatting instructions in sections and then referring to those specific sections.
- [Using the system role](https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompting-system-role.html): The System Role is a role where you can provide instructions to the model that define how it will respond to end users of your application.
- [Provide examples (few-shot prompting)](https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompting-provide-examples.html): By including a few examples of your task within the prompt, you can build a structured template for Amazon Nova 2 to follow.
- [Tool calling systems](https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompting-tools-function.html): Tool calling is available for the Amazon Nova models by passing a tool configuration schema in your request.
- [Advanced prompting techniques](https://docs.aws.amazon.com/nova/latest/nova2-userguide/advanced-prompting-techniques.html): These sections provide advanced guidance for how to improve the quality of your prompts and leverage key features like extended thinking.
- [Prompting multimodal inputs](https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompting-multimodal.html): Guidelines for prompting with images, documents, videos and audio.


## [Code and Troubleshooting](https://docs.aws.amazon.com/nova/latest/nova2-userguide/code-and-troubleshooting.html)

- [Code library](https://docs.aws.amazon.com/nova/latest/nova2-userguide/code-library.html): This section provides code examples for common Amazon Nova operations using either the Converse API or the InvokeModel API.
- [Troubleshooting](https://docs.aws.amazon.com/nova/latest/nova2-userguide/troubleshooting.html): This section provides solutions to common issues when working with Amazon Nova models.


## [API and SDK reference](https://docs.aws.amazon.com/nova/latest/nova2-userguide/api-sdk-reference.html)

- [Request and response schema](https://docs.aws.amazon.com/nova/latest/nova2-userguide/request-response-schema.html): The request schema is nearly identical between the Invoke API and Converse API.
- [SDK reference](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sdk-reference.html): SDK documentation and code examples for Amazon Nova.


## [Amazon Nova model customization](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model.html)

- [General prerequisites](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-general-prerequisites.html): The customization process involves several key stages including model training, evaluation, and deployment for inference, each requiring specific resources and configurations.
- [Amazon Nova recipes](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-recipes.html): Learn how to get base Amazon Nova models recipes before start a training job.

### [On SageMaker training jobs](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-training-job.html)

Learn how to customize Amazon Nova models on SageMaker Training Jobs environment.

- [Nova Customization SDK](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-customization-sdk.html): Learn how to use the Nova Customization SDK for customizing Amazon Nova models with ease.

### [Training](https://docs.aws.amazon.com/nova/latest/nova2-userguide/smtj-training.html)

Learn how to train Amazon Nova models on SageMaker Training Jobs using various training techniques.

- [Supervised fine-tuning (SFT)](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-fine-tune-2.html): Fine-tuning Amazon Nova models with SageMaker Training Jobs offers a powerful way to customize foundation models for your specific use cases.
- [Reinforcement Fine-Tuning (RFT)](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-reinforcement-fine-tuning.html): Learn how to use reinforcement fine-tuning (RFT) to improve model performance through feedback signals.
- [Monitoring Progress Across Iterations](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-monitor.html): Learn how to monitor progress across iterations.

### [Evaluation](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-evaluation.html)

Learn how to evaluate your SageMaker AI-trained Amazon Nova model before starting a training job.

- [Reasoning model evaluation](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-reasoning-model-evaluation.html): Learn how to evaluate reasoning-capable Nova models.
- [RFT evaluation](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-rft-evaluation.html): Learn how to evaluate models using RFT evaluation methods.
- [Implementing reward functions](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-implementing-reward-functions.html): Learn how to implement custom reward functions for RFT training.
- [Iterative training](https://docs.aws.amazon.com/nova/latest/nova2-userguide/smtj-iterative-training.html): Iterative training is a systematic approach to fine-tuning models through multiple training cycles, where each round builds on the previous checkpoint by addressing specific weaknesses discovered through evaluation.

### [On SageMaker HyperPod](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp.html)

Learn how to customize Amazon Nova models, including the latest Amazon Nova 2.0 models, on Hyperpod.

- [Nova Customization SDK](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-customization-sdk.html): Learn how to use the Amazon Nova Customization SDK for customizing Amazon Amazon Nova models with ease for SageMaker HyperPod .
- [HP cluster setup](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-cluster.html): Learn how to create a SageMaker HyperPod EKS cluster with a restricted instance group (RIG), which provides a specialized environment for training Amazon Amazon Nova models.
- [Essential Commands Guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-essential-commands-guide.html): Learn essential commands for managing SageMaker HyperPod training workflows, from connecting to your cluster to monitoring job progress.

### [Nova Forge access and setup](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge-hp-access.html)

Build custom frontier models using Amazon Nova Forge.

- [Subscribe to Nova Forge](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge-subscribing.html): To access Amazon Nova Forge features, complete the following steps:
- [Set up HyperPod infrastructure](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge-hyperpod-setup.html): Once your Amazon Nova Forge subscription is approved, set up the necessary infrastructure to use Forge-enabled features.
- [Responsible AI](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge-responsible-ai.html): Content moderation settings: Amazon Nova Forge customers have access to Customizable Content Moderation Settings (CCMS) for Amazon Nova Lite 1.0 and Pro 1.0 models.

### [Training](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-training.html)

Learn how to train Amazon Nova models on SageMaker HyperPod using various training techniques.

### [Continued pre-training (CPT)](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-cpt.html)

Continued pre-training (CPT) is a training technique that extends the pre-training phase of a foundation model by exposing it to additional unlabeled text from specific domains or corpora.

- [CPT on Nova 2.0](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-cpt-2.html): Amazon Nova Lite 2.0 is a reasoning model trained on larger and more diverse datasets than Nova Lite 1.0.

### [Supervised fine-tuning (SFT)](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-fine-tune.html)

The SFT training process consists of two main stages:

- [SFT on Nova 2.0](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-sft-2-fine-tune.html): Amazon Nova Lite 2.0 brings enhanced capabilities for supervised fine-tuning, including advanced reasoning mode, improved multimodal understanding, and extended context handling.

### [Reinforcement Fine-Tuning (RFT)](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-rft.html)

Learn how to use Reinforcement Fine-Tuning (RFT) to optimize Amazon Nova models using reward-based learning on SageMaker HyperPod.

### [RFT on Nova 2.0](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-rft-nova2.html)

RFT training data follows the OpenAI conversational format.

- [Monitoring RFT training](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-rft-monitoring.html): Monitor key metrics during training to ensure effective learning and identify potential issues early.

### [Evaluation](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-evaluate.html)

Learn about model evaluation in Amazon Nova customization on Hyperpod.

- [Available benchmark tasks](https://docs.aws.amazon.com/nova/latest/nova2-userguide/customize-fine-tune-evaluate-available-tasks.html): A sample code package is available that demonstrates how to calculate benchmark metrics using the SageMaker AI model evaluation feature for Amazon Nova.
- [Understanding the recipe parameters](https://docs.aws.amazon.com/nova/latest/nova2-userguide/customize-fine-tune-evaluate-understand-modify.html)
- [Evaluation recipe examples](https://docs.aws.amazon.com/nova/latest/nova2-userguide/customize-fine-tune-evaluate-recipe-examples.html): Amazon Nova provides four types of evaluation recipes, which are available in the SageMaker HyperPod recipes GitHub repository.
- [Starting an evaluation job](https://docs.aws.amazon.com/nova/latest/nova2-userguide/customize-fine-tune-evaluate-start-job.html): The following provides a suggested evaluation instance type and model type configuration:
- [Accessing and analyzing evaluation results](https://docs.aws.amazon.com/nova/latest/nova2-userguide/customize-fine-tune-evaluate-access-results.html): After your evaluation job completes successfully, you can access and analyze the results using the information in this section.
- [RFT evaluation](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-evaluate-rft.html)
- [MLflow monitoring](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-mlflow.html): Learn how to set up and use MLflow to monitor Amazon Nova model training jobs on SageMaker HyperPod.
- [Iterative Training](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-iterative-training.html): Learn how to use iterative training to improve model performance over multiple training cycles.

### [SageMaker Inference](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-sagemaker-inference.html)

Learn how to deploy trained Amazon Nova models to SageMaker for real-time inference.

- [Getting started](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-sagemaker-inference-getting-started.html): Learn how to deploy customized Amazon Nova models on SageMaker real-time endpoints, configure inference parameters, and invoke your models for testing.
- [API reference](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-sagemaker-inference-api-reference.html): Learn about the API reference for Amazon Nova models on SageMaker inference.
- [Evaluate models](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-eval-on-sagemaker-inference.html): Learn how to evaluate customized Amazon Nova models using SageMaker inference endpoints with Inspect AI.
- [Abuse detection for Amazon Nova Forge](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-sagemaker-inference-abuse-detection.html): Learn about automated abuse detection mechanisms for Amazon Nova Forge models deployed on SageMaker inference.

### [Amazon Bedrock inference](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-bedrock-inference.html)

Learn how to deploy trained Amazon Nova models to Amazon Bedrock inference.

### [Deploy a custom model for on-demand inference](https://docs.aws.amazon.com/nova/latest/nova2-userguide/deploy-custom-model.html)

Learn how to deploy your custom Amazon Nova model for on-demand inference with Amazon Bedrock.

- [Deploy a custom model](https://docs.aws.amazon.com/nova/latest/nova2-userguide/deploying-custom-model.html): Learn how to deploy your custom model using the console, CLI, or SDKs to enable on-demand inference.
- [Use a deployment for on-demand inference](https://docs.aws.amazon.com/nova/latest/nova2-userguide/use-custom-model-on-demand.html): Learn how to use your custom model for on-demand inference with Amazon Bedrock.
- [Delete a custom model deployment](https://docs.aws.amazon.com/nova/latest/nova2-userguide/delete-custom-model-deployment.html): After you are finished using your model for on-demand inference, you can delete the deployment.
- [Limitations](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-model-limitations.html): Learn limitations of customizing Amazon Nova models using SageMaker training jobs.


## [Nova Forge](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge.html)

- [Nova Forge access and setup](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge-access.html): Build custom frontier models using Nova Forge.
- [Continued Pre-Training and Mid-Training](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge-cpt.html)
- [Supervised Fine-Tuning](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-forge-sft.html)
- [Reinforcement Learning](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-hp-rft-forge.html)
- [Responsible AI Toolkit](https://docs.aws.amazon.com/nova/latest/nova2-userguide/nova-responsible-ai-toolkit.html): Use the Responsible AI Toolkit and customizable content moderation settings.
