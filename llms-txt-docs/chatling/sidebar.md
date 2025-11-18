# Source: https://docs.chatling.ai/chatbot/builder/sidebar.md

# Sidebar

> Learn about the Sidebar and its functionalities in the Builder.

<img src="https://chatling-assets.b-cdn.net/Sidebar.jpg" width="300" />

The sidebar contains four menus:

* Blocks
* Variables
* AI Configuration
* Settings

## Sidebar Menus

### Blocks

The Blocks menu contains all the blocks you can add to your flow. [Blocks](/chatbot/builder/blocks/overview) build up the conversational flow of your chatbot.

You can drag and drop blocks onto the canvas to add them to your flow.

![Adding blocks](https://chatling-assets.b-cdn.net/Drag%20blocks.gif)

Here are the different categories of blocks that are available:

* **Send message**: Display a message to the user.
* **Capture response**: Capture answers from the user, such as text, email, form submission, and more.
* **AI**: Use AI to generate responses to user's questions.
* **Logic**: Add conditions and logic to your flow.
* **Integration**: Connect your chatbot to external services.

### Variables

Variables are placeholders that store information during the conversation. You can use variables to store user inputs, API responses, and more. These variables can be used to personalize the conversation and make it more dynamic.

<img src="https://chatling-assets.b-cdn.net/variables-sidebar-menu.png" width="350" />

There are two types of variables:

* **System variables**: These are predefined variables that store system information or can be used to perform a specific action. For example, the `contact_email` variable can be used to store the user's email address and save them as a lead.

  If you click on a system variable, you can view its purpose.

  There are also additional system variables that aren't imported by default. To view and import them, click the `Import system variables` button.

* **Custom variables**: These are variables you create to store information specific to your chatbot. For example, you can create a custom variable to store the user's question and use it in the `AI Response` block to generate a response from the AI.

### AI Configuration

The AI Configuration menu allows you to configure the default AI settings for your chatbot. These settings are used when the chatbot generates AI responses using the Knowledge Base.

<img src="https://chatling-assets.b-cdn.net/ai-configuration-sidebar-menu.png" width="350" />

You can configure the following settings:

* **Instructions**: Provide instructions to the AI to tailor its responses. For example, you can instruct the AI to provide more detailed responses or to use a specific tone. You can click the `View examples` button to see examples of instructions you can provide.
* **Settings**:
  * **Business, product, or brand name**: This will be used by the AI to generate more relevant responses and avoids answering off-topics questions that aren't related to your business, product, or brand, such as questions related to your competitors, weather, etc.
  * **AI Model**: The AI model to use for generating responses. Every model uses a different amount of credits per response. We recommend testing with different models to see which one works best for your chatbot.
  * **Language**: The language in which the AI should generate responses. If you set it to Auto, the AI will detect the language of the user's question and generate a response in the same language.
  * **Temperature**: Controls the randomness of the responses. A higher temperature will generate more creative responses, while a lower temperature will generate more accurate responses.

### Settings

The Settings menu allows you to configure the chatbot's general settings. Here's what you can configure:

* **Message Delay**: The time delay in seconds between chatbot's messages.
