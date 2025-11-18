# Source: https://docs.chatling.ai/chatbot/builder/blocks/inputs/buttons.md

# Buttons Block

> Learn about the Buttons input block and how to set it up in the Builder.

The Buttons block is used to display a set of buttons that users can click to trigger actions or provide responses. You can use this block to present multiple options to users and guide them through the conversation flow.

<img src="https://chatling-assets.b-cdn.net/input-buttons-block-preview.png" alt="Buttons block preview" width="400" />

Every button in the block has a connector that allows you to link it to other blocks.

# Configuration

Buttons have the following configuration options:

* **Label**: The text that appears on the button.
* **Store selected button in variable**: The variable where the selected button's value will be stored. For example, if the user selects the "Yes" button, you can store the value "Yes" in a variable for later use.

<img src="https://chatling-assets.b-cdn.net/input-buttons-block-editor.jpg" alt="Input buttons block editor" />

## Connecting buttons

Buttons must be connected to other blocks so that the chatbot can respond to the user's selection.

To connect a button, click the connector next to it and drag it to the group you want to connect it to.

In the example below, when the user clicks the "Software Development" button, the chatbot will display the "Sure thing! Our team can help..." message and continues the flow from there.

<img src="https://chatling-assets.b-cdn.net/connecting-button-blocks.gif" alt="Connect buttons" />
