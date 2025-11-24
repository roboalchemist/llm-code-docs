# Source: https://dev.writer.com/agent-builder/chatbot-tutorial.md

# Build a chatbot connected to a Knowledge Graph

Agent Builder contains prebuilt UI and blueprint blocks that you can combine to build a full-featured chatbot.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/chatbot-preview.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6c0fc1c1e2d8a79fef0450311d53882d" alt="" data-og-width="3456" width="3456" data-og-height="1802" height="1802" data-path="images/agent-builder/chatbot-tutorial/chatbot-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/chatbot-preview.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=084392a471bb7efdce393ec4d4ffb48d 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/chatbot-preview.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6357545d42d08b1b5cd9e237686b53fb 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/chatbot-preview.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=910cb15918f8d15b9d4e280dd4ce0f09 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/chatbot-preview.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3b31132d0390399fa8ba2e46250aecf5 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/chatbot-preview.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=82436f0f91e26bbcd02b3cfa7248adf2 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/chatbot-preview.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7e13128916bca38d44d781f5b2165eb0 2500w" />

This tutorial demonstrates how to build a chatbot that's connected to the Palmyra X5 model and integrates with a Knowledge Graph for domain-specific knowledge. It covers the following steps:

1. Adding a [**Chatbot** block](/components/chatbot) to the UI
2. Adding a [**Chat reply** block](/blueprints/chatreply) to the blueprint
3. Connecting a Knowledge Graph to the chatbot

<Note>
  If you are unfamiliar with Agent Builder interface, check out the [Agent Builder Quickstart](/agent-builder/quickstart).
</Note>

## Build the UI

The UI for the agent contains a single **Chatbot** block. This block handles the full UI for the chatbot, including the chat interface and the chat messages.

<Steps>
  <Step title="Add a Chatbot block to the UI">
    Drag and drop a [**Chatbot** component](/components/chatbot) onto the Interface.

    In the block's configuration panel, set the following fields:

    * **Conversation**: `@{chat}`. This is the state variable that stores the chat conversation.
    * **Assistant initials**: `AI`. This is the text that appears next to the assistant's messages in the chat.
    * **User initials**: `YOU`. This is the text that appears next to the user's messages in the chat.
    * **Use markdown**: `no`. You can change this to `yes` if you want to parse Markdown formatting in messages.
    * **Enable file upload**: `no`. This disables the file uploads in the chatbot.
    * **Placeholder**: `Type your message here.`. This is the text that appears in the input field when it's empty.

        <img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chatbot-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=621776f311d0d757a1611cc02b0aa1c4" alt="" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/chatbot-tutorial/chatbot-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chatbot-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6e877cb949fd46a3216d09122dd4dbcb 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chatbot-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e62f5b2adc54f986c5fd874dfb66e4f6 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chatbot-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f55bb1f4dcb3e5eb224148dd00bf5aaf 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chatbot-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=af6ad7683eea9cf13790590bf5c4282c 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chatbot-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f0dd908b1cc6aee146356fdd95c08d8c 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chatbot-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c7bcbcb98eaf08a32bc69fee334468c0 2500w" />
  </Step>
</Steps>

## Build the blueprint

The blueprint for the agent contains the following blocks:

* **UI trigger** block to run the blueprint when a user enters a chat message
* **Chat reply** block to manage the conversation and generate a response to the user's message

<Steps>
  <Step title="Add a UI trigger for the chat message event">
    To run the blueprint when a user enters a chat message, add a [**UI trigger** block](/blueprints/uitrigger) to the canvas. In the block's configuration panel, update the following fields:

    * **Component Id**: select the `Chatbot` component from the dropdown of UI blocks
    * **Event type**: `wf-chatbot-message`

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/ui-trigger.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d6eeabe1cabaf87f66b7dcafe1e2b5c7" alt="" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/chatbot-tutorial/ui-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/ui-trigger.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=59a1514070f803aedeb4f597103305df 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/ui-trigger.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=36e17bc7508a7970f75deccd395a901e 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/ui-trigger.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=6cfdcd7311073125329f582aa8598962 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/ui-trigger.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4516706d7b0da1d13c8b3d472464b21a 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/ui-trigger.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=82201092805c68e36aa6e0127c6d5d1a 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/chatbot-tutorial/ui-trigger.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3e63009fb036d02f621dfa03220a1772 2500w" />
  </Step>

  <Step title="Add a Chat reply block">
    Add a **Chat reply** block to the canvas, which runs after the UI trigger block. This block manages the chat conversation, including the chat messages and the chat history.

    Connect the **UI trigger** block to the **Chat reply** block by dragging a line from the green dot on the **UI trigger** block to the **Chat reply** block.

    In the **Chat reply** block's configuration panel, set the following fields:

    * **Conversation object**: `chat`
    * **System prompt**: This provides the context for the chat conversation and gives instructions to the model about how to act or respond. The example below uses a system prompt that instructs the model to act as a helpful assistant regarding Writer's developer platform. System prompts help the model understand the context of the chat conversation and the goals of the chatbot. Learn more in [Prompting strategies](/home/prompting).

    ```
    You are a helpful assistant for Writer's developer platform. Use the provided documentation to answer questions about Writer's APIs, SDKs, and Agent Builder.

    Be clear and concise, include code examples when helpful, and reference specific docs when appropriate. If you're unsure about something, say so and suggest checking the documentation directly.
    ```

    * **Message**: `@{payload}`. This is the message that the user sends to the chatbot that triggers the blueprint to run.

        <img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chat-reply-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f4e32a11c5fe4dcc92e934bdd3dd01c5" alt="" data-og-width="3456" width="3456" data-og-height="1814" height="1814" data-path="images/agent-builder/chatbot-tutorial/chat-reply-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chat-reply-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=3a13c60d4bb16981c6e9fcaf0160ac90 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chat-reply-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=8162377efa83a541c3033af564f2c11b 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chat-reply-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=8774f42d478b19dfbb8a7a7233ea838c 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chat-reply-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d06ecda231e250927c2a11fabe86f9cb 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chat-reply-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1340f7f7669a63ada59891a1ab4eca6e 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/chat-reply-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f4b4a7a23598acadd457e18e34f5cbe1 2500w" />
  </Step>
</Steps>

At this point, the chatbot isn't connected to a Knowledge Graph, but it's configured to respond to messages from the user. You can preview the agent to see how it works and then [connect a Knowledge Graph to the chatbot](#connect-a-knowledge-graph-to-the-chatbot) to enable the chatbot to answer domain-specific questions.

## Preview the agent

To preview the agent, navigate to the **Preview** tab. Type a message in the chatbot and see the response from the model.

## Connect a Knowledge Graph to the chatbot

You can connect one or more [Knowledge Graphs](/home/knowledge-graph) to the chatbot to answer questions about data related to your business or a specific dataset.

To connect a Knowledge Graph to the chatbot, update the **Chat reply** block.

<Steps>
  <Step title="Update the Chat reply block">
    * Click the **Chat reply** block to open its configuration panel
    * Click the **+ Add tool** button under **Tools**
    * Select "Knowledge graph" under **Tool type**
    * Under **Graph id(s)**, select one or more Knowledge Graphs you want to connect to the chatbot. The example below connects the chatbot to a Knowledge Graph that contains developer docs and a Knowledge Graph connected to the support center.
    * Click **Save** to save the changes.

        <img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/add-knowledge-graph-tool.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b71b33e1b7c579e9d634499bc1b2797c" alt="" data-og-width="3456" width="3456" data-og-height="1812" height="1812" data-path="images/agent-builder/chatbot-tutorial/add-knowledge-graph-tool.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/add-knowledge-graph-tool.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=aae7d4be6c106b0682959db110f598fe 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/add-knowledge-graph-tool.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=32dab8c5daf2630e534d5d15d6c052f0 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/add-knowledge-graph-tool.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=70ef802a1a46b65b2acb5dc5cf735fdc 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/add-knowledge-graph-tool.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=92879204977d50f8b39d1cd88b920943 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/add-knowledge-graph-tool.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=3bac154d1fca78852ede979863959596 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/chatbot-tutorial/add-knowledge-graph-tool.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6cec67281d3c04ca3497d9ae3cd65796 2500w" />
  </Step>
</Steps>

Now when the user asks questions related to data in the connected Knowledge Graphs, the chatbot can reference the data in the Knowledge Graphs to answer the question.

If you encounter any issues, refer to the [Troubleshooting](/agent-builder/troubleshooting) guide for debugging information.

<feedback />
