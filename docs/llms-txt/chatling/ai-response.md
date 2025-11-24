# Source: https://docs.chatling.ai/chatbot/builder/blocks/ai/ai-response.md

# AI Response Block

> Learn about the AI Response block and how to set it up in the Builder.

The AI Response block is used for generating responses to user input using AI. It can provide answers based on the information you have added to the [Knowledge Base](/knowledge-base/overview) or from the AI's pretrained data.

The AI uses natural language processing (NLP) to understand the user's input and generate relevant responses.

## What is the "Response Source"?

The Response Source determines where the AI will look for answers to user queries. You can choose from the following options:

* **Knowledge Base**: The AI will search the data you've uploaded to the Knowledge Base for the relevant information and return the corresponding answer.
* **AI Model**: The AI will use its pretrained data to generate a response based on the user's query. This is ideal for a general-purpose AI that can answer a wide range of questions without limiting its responses to the data in the knowledge base.

## Configurations for Knowledge Base Response Source

<img src="https://chatling-assets.b-cdn.net/ai-knowledge-base-response-source-settings.png" alt="AI block knowledge base settings" />

When you select the "Knowledge Base" as the Response Source, you can configure the following settings:

* **Question**: The user's input or query that the AI will process to generate a response. You can use variables to make the question dynamic. For example, you can capture the user's input using a Text input block and store it in a variable called `user_input`. Then, you can use this variable in the "Question" field to make the AI response dynamic.
* **Store response in variable**: You can store the AI response in a variable to use it in other blocks.
* **Stream**: When enabled, the AI response will be streamed to the user in real-time as it is generated. This provides a more interactive experience for the user.
  * When Stream is enabled, some features that require post-processing, such as "Not Found path" will be disabled.
* **Not Found path**: The path to follow if the AI does not find a relevant answer in the Knowledge Base.
* **Model**: The AI model to use for generating responses.
* **Language**: The language in which the AI will respond to the user. If you set it to "Auto," the AI will detect the language of the user's input and respond in the same language.
  * If you want the AI to respond in a certain dialect or accent, you can specify it in Instructions section of the [AI Configuration](/chatbot/builder/sidebar#ai-configuration).
* **Temperature**: The randomness of the AI's responses. A higher temperature value will result in more diverse and creative responses, while a lower value will produce more accurate responses.

### What does "Use global AI settings" mean?

When you set an option, such as the AI model, language, or temperature to "Use global AI settings", the AI will use the settings defined in the [AI Configuration](/chatbot/builder/sidebar#ai-configuration) menu in the [sidebar](/chatbot/builder/sidebar). This allows you to define global settings that will be applied to all AI blocks in your bot.

## Configurations for AI Model Response Source

When you set the Response Source to "AI Model", you can configure the following settings:

* **Prompt**: The message or query that the AI will use to generate a response. You can use variables to make the prompt dynamic.
* **Store response in variable**: You can store the AI response in a variable to use it in other blocks.
* **Instructions**: Additional instructions for the AI to follow when generating a response. For example, you can specify its personality, tone, or style, or provide specific context for the response.
* **Model**: The AI model to use for generating responses.
* **Max Length**: Maximum number of tokens to generate, shared between the prompt and the response. One token is roughly 4 characters.
* **Temperature**: Randomness of the AI's responses. A higher temperature value will result in more diverse and creative responses, while a lower value will produce more focused and deterministic responses.
* **Top P**: Controls diversity via nucleus sampling: 0.5 means half of all likelihood-weighted options are considered.
* **Frequency Penalty**: How much to penalize new tokens based on their existing frequency in the text so far. Decreases the model's likelihood to repeat the same line verbatim.
* **Presence Penalty**: How much to penalize new tokens based on whether they appear in the text so far. Increases the model's likelihood to talk about new topics.

## How to set up the AI block to respond from the knowledge base?

Here's a high level overview of how the AI generates responses using the knowledge base:

* The user inputs a question or query, which is saved in a variable of your choice.
* The stored input is passed to the AI which uses natural language processing (NLP) to understand the user's query and the context of the conversation.
* The AI searches the knowledge base for relevant information.
* The AI generates the response and displays it to the user.

To set up the AI block, follow these steps:

1. Add a Text input block to the canvas. We'll use this block to capture the user's input and store it in a variable so it can be passed to the AI block.

<img src="https://chatling-assets.b-cdn.net/add-text-input-block-to-canvas.gif" alt="Adding text input block to the builder" />

2. Click on the Text block to open the editor. In the `Store answer in variable` field, enter a variable where the user's input will be stored. In this example, we'll create and use a variable called `user_query`.

<img src="https://chatling-assets.b-cdn.net/create-new-variable.jpg" alt="Storing user input in a variable" width="350" />

3. Next, drag and drop the AI Response block onto the canvas.

<img src="https://chatling-assets.b-cdn.net/setting-up-ai-kb-response.jpg" alt="Setting up AI block for knowledge base response" width="350" />

4. Connect the Text input block to the AI block by dragging the connector from the Text block to the AI block.

<img src="https://chatling-assets.b-cdn.net/setting-up-ai-kb-response-1.gif" alt="Connecting text input to AI block" />

5. Click the AI Response block to open the editor. In the `Question` field, enter the variable where the user's input is stored. In step 2, we used the `user_query` variable, so we'll enter `{user_query}` in the Question field.

<img src="https://chatling-assets.b-cdn.net/setting-up-ai-kb-response-2.jpg" alt="Setting up AI block for knowledge base response" width="350" />

6. Set up the global AI settings by going to the `AI Configuration` in the sidebar. You can define settings such as the AI model, instructions, language, and business name.

7. Lastly, set up the block connections accordingly. For example, a setup like below will allow the user to continually ask questions and receive responses from the AI.

<img src="https://chatling-assets.b-cdn.net/setting-up-ai-kb-response-3.png" alt="Setting up AI block for knowledge base response" width="650" />
