# Source: https://docs.chatling.ai/chatbot/builder/blocks/inputs/buttons.md

# Source: https://docs.chatling.ai/ai-agent/actions/buttons.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Buttons

Displays a set of buttons in the chat, such as URL buttons to open a webpage or text buttons to send preset replies that keep the flow moving.

## Configuration

### `Action Name`

A short, specific identifier that tells the Agent what this action does (e.g. best\_sellers\_buttons, support\_button).

### `When to Use`

A detailed description of what the action does and when it must be used.

When applicable, you can specify one or more of the following:

* **Positive cues/phrases**: Example utterances and keywords that signal this action (include a few variations).
* **Preconditions**: What must be true before running.
* **Do not use when**: Explicit exclusions to avoid false triggers.

<img src="https://chatling-assets.b-cdn.net/action-when-to-use-field.jpg" width="450" alt="When to use option" />

### `Frequency`

Specify how often the Agent can invoke this action to avoid overusing it, e.g `Once per chat` or `Whenever applicable`.

<img src="https://chatling-assets.b-cdn.net/action-frequency-field.jpg" width="450" alt="Frequency option" />

### `Buttons`

Add the buttons that you want to display in the chat. Buttons can be of two types:

* **URL button**: Opens a webpage when clicked.
* **Text button**: Sends a message to the AI agent when clicked. If a `Message` is provided, it will be sent as the message. Otherwise, the button label will be used.

To reorder the buttons, click the drag handle next to a button and move it up or down.

<img src="https://chatling-assets.b-cdn.net/button-action-buttons-field.jpg" width="450" alt="Buttons option" />
