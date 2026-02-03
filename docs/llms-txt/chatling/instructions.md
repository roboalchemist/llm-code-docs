# Source: https://docs.chatling.ai/chatbot/ai/instructions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Instructions

> A guide on what AI Instructions are and how to use them.

Instructions are a way to provide guidance to the AI on how to respond.

You can use instructions to tailor the AI's responses to your specific needs, such as providing more detailed responses, using a specific tone, have a specific personality, or avoiding certain topics.

Here are a few examples:

* Your name is "Joanne" and you are our customer support assistant. When referring to yourself, do not mention anything about being an AI assistant or AI model. Instead, refer to yourself as "Joanne".
* Keep your answers short and to the point, and do not provide unnecessary information.
* Use a friendly and casual tone when responding to users.
* You must act as a professional customer support agent. NEVER break character.
* When responding in English, use American English spelling and grammar.
* Promote special offers or promotions when appropriate. For example, if a customer asks about a product, you can mention that we have a store-wide promotion of 50% off.
* Limit your answers to a maximum of 5 sentences.
* You are a lead generation assistant for a Digital Marketing agency and you are communicating with a prospective customer.
* Do not discuss politics, religion, or any other sensitive topics.

## How to add instructions

The method for adding instructions depends on the [Response Source](/chatbot/builder/blocks/ai/ai-response#what-is-the-response-source) that you've set for the [AI Response](/chatbot/builder/blocks/ai/ai-response) block.

### Response Source: Knowledge Base

If you are using the Knowledge Base as the response source, you can add instructions using the [AI Configuration menu](/chatbot/builder/sidebar#ai-configuration) in the Builder's sidebar.

1. Click on the AI Configuration menu in the sidebar.

<img src="https://chatling-assets.b-cdn.net/open-ai-configuration-menu-from-sidebar.jpg" alt="Open AI Configuration menu from sidebar" width="350" />

2. Go to `Instructions`.

<img src="https://chatling-assets.b-cdn.net/open-instructions-page-kb-ai-configuration-sidebar.jpg" alt="Open Instructions page from AI Configuration sidebar menu" width="350" />

3. Click the `Add instruction` button and enter your instruction.

<img src="https://chatling-assets.b-cdn.net/add-new-instruction-kb-ai-configuration-sidebar.jpg" alt="Add new instruction in AI Configuration sidebar menu" width="350" />

4. To add more instructions, click the `New` button to create a new instruction.

### Response Source: AI Model

If you are using the AI Model as the response source, you can add instructions directly from the [AI Response block](/chatbot/builder/blocks/ai/ai-response).

1. Click the AI Response block on the canvas to open the block editor.
2. Under the `Instructions` section, you can add all your instructions. You can add multiple instructions in the same field, separated by a new line.

<img src="https://chatling-assets.b-cdn.net/add-instructions-to-ai-model-response-block.jpg" alt="Add instructions for AI Model response source" width="450" />
