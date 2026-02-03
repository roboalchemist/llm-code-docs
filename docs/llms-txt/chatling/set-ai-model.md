# Source: https://docs.chatling.ai/chatbot/ai/set-ai-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting the AI model

> Learn how to set the LLM model used by the AI.

There are various [AI models](/ai/supported-ai-models) available in Chatling that you can use to generate responses for your chatbot.

We recommend testing with different models to see which one works best for your chatbot and provides the most accurate responses. Each model uses a different amount of credits per response.

## How to set the AI model?

The method for choosing the AI model depends on the [Response Source](/chatbot/builder/blocks/ai/ai-response#what-is-the-response-source) that you've set for the [AI Response](/chatbot/builder/blocks/ai/ai-response) block.

Below are the instructions based on the response source you've selected.

### 1. Response Source: Knowledge Base

If you are using the Knowledge Base as the response source, you can set the AI model using the [AI Configuration menu](/chatbot/builder/sidebar#ai-configuration) in the Builder's sidebar.

1. Click on the AI Configuration menu in the sidebar.

<img src="https://chatling-assets.b-cdn.net/open-ai-configuration-menu-from-sidebar.jpg" alt="Open AI Configuration menu from sidebar" width="350" />

2. Go to `Settings`.

<img src="https://chatling-assets.b-cdn.net/ai-configuration-settings-menu-sidebar.jpg" alt="Open Settings page from AI Configuration sidebar menu" width="350" />

3. Select the AI model you want to use from the dropdown list.

<img src="https://chatling-assets.b-cdn.net/set-ai-model-kb-ai-configuration-sidebar.jpg" alt="Select AI model in AI Configuration settings sidebar menu" width="350" />

Once you've selected the AI model, all AI Response blocks that use the Knowledge Base as the response source will use this model to generate responses.

#### Setting the model on a per-block basis

If you want to set the AI model on a per-block basis, you can do so by opening the AI Response block's editor and settings the `Model` option. This will override the default model set in the AI Configuration settings.

<img src="https://chatling-assets.b-cdn.net/override-ai-model-setting-kb-ai-response.jpg" alt="Override AI model setting in AI Response block" width="450" />

### 2. Response Source: AI Model

If you are using the "AI Model" as the response source, you can set the AI model from the block's editor using the `Model` option.

<img src="https://chatling-assets.b-cdn.net/set-ai-model-kb-ai-configuration-sidebar.jpeg" alt="Set model in AI Model response block" width="450" />
