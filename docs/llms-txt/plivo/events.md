# Source: https://plivo.com/docs/aiagent/aistudio/agentconfiguration/events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Configure callback URLs for hangup events, recordings, and transcripts

# Events

Event callbacks allow you to receive important updates from your AI agent. By configuring callback URLs, you can automatically capture data such as variables, recordings, transcripts, and summaries—without manual intervention.

### Hangup URL

The **Hangup URL event** is triggered when a user ends a call or when the call is disconnected due to other reasons. This event allows you to access node variables (extracted using the AI conversation node or system variables) even after the call has ended.

You can use the Hangup URL event in two ways:

1. **Send variables to a URL (URL)** – The extracted variables will be posted to the URL configured by you.
2. **Start another agent interaction (Trigger an agent)** – The extracted variables can be passed forward to trigger and initialize another agent flow.

### Recording URL

The **Recording URL event** is triggered when a call recording is available. The recording file is sent to the URL configured by you. Along with the recording, you can also receive:

* **Conversation transcripts** – Text version of the entire call.
* **Conversation summary** – A concise overview of the key points discussed during the call.
