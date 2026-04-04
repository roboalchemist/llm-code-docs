# Source: https://docs.chatling.ai/chatbot/builder/variables/how-to-use-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# How to use variables

> A guide on how to use Variables in your chatbot

Variables can be used for capturing information, displaying dynamic content, and processing data in your chatbot.

## How to store data in variables

You can store data in variables using the `Store answer in variable` or a similar option that's available for certain blocks in the builder. This option appears in the [block editor](/chatbot/builder/block-editor).

Let's take the [Text input block](/chatbot/builder/blocks/inputs/text) as an example. This block allows users to enter text. To store the user's response in a variable, click the dropdown below the `Store answer in variable` option and select a variable.

<img src="https://chatling-assets.b-cdn.net/store-answer-in-variable-option-text-input-block.jpg" alt="Store answer in variable option in Text Input block" width="400" />

## How to display variables in messages

You can display variables in messages using the `{variableName}` syntax. The variable name should be enclosed in curly braces.

As an example, let's you have a variable called `first_name` and you want to greet the user by their name. Here's how to do it:

1. Add a [Text output block](/chatbot/builder/blocks/send/text) to your chatbot.
2. Click the block to open the editor.
3. Type `Hello, {first_name}!` in the message field.

<img src="https://chatling-assets.b-cdn.net/inserting-variable-in-text-block.png" alt="Display variable in message in Text Output block" width="400" />

4. When the chatbot displays this block, it will replace `{first_name}` with the value stored by the variable.

<img src="https://chatling-assets.b-cdn.net/displaying-variables-in-output-text-messages.png" alt="Display variable in message" width="400" />

Note that the values stored are on a per-conversation basis. This means that the value of a variable is unique to each conversation and is not shared across different conversations.
