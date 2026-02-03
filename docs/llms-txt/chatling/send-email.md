# Source: https://docs.chatling.ai/chatbot/builder/blocks/action/send-email.md

# Source: https://docs.chatling.ai/ai-agent/actions/send-email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Send Email

The Send Email action allows the AI Agent to send emails to one or more recipients. You can use it to send notifications, follow ups, order confirmations, transactional emails and other types of emails.

<img src="https://chatling-assets.b-cdn.net/send-email-action-sample-chat.jpg" width="350" alt="Send Email action preview" />

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

### `Input parameters`

Define the parameters the Agent must gather before sending the request. The Agent can capture these from user input, existing chat context, or saved contact data.

For each parameter, you can specify the following:

* **Name**: The name of the parameter. Must start with a letter and contain only letters, numbers, and underscores.
* **Description** (optional): A description of the parameter to indicate what it is and if applicable, the formatting rules and min/max length.
* **Save to variable** (optional): The variable where the data can be saved. Useful when you want to use the data in the email setup, such as the recipient's email address.

### `Email Setup`

Configure the email setup.

* **Sender Name**: The name of the sender.
* **To**: The email addresses of the recipients (max 5).
* **Reply-to**: The email addresses to reply to (max 5).
* **CC**: The email addresses of the recipients who will receive a copy of the email (max 5).
* **Subject**: The subject of the email.
* **Message**: The content of the email.
