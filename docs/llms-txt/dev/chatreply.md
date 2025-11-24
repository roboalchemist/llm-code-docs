# Source: https://dev.writer.com/blueprints/chatreply.md

# Chat reply

Initializes conversations, adds messages, and generates replies.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7c8eee426d7191f7d24c4ed8f8cb33b1" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/chat-reply.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7f603d23bb586ab20c5a941e21890412 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b89ead260d100c43def2233f8a2d7ced 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=629f55e1dbf2eefab9db65d6649c002e 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e6c7fc898e4ceba1f27079097880453f 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=630e3b1907e00e184a5ddc3c9e9a0b64 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ef4b9946b57cc880cf943688ea427608 2500w" />

## Overview

The **Chat reply** block is a comprehensive chat solution that can initialize conversations, add messages, and generate replies in a single block. It's designed to handle the complete chat workflow efficiently.

You can specify a conversation state variable to store the chat history, system prompt, message, and various configuration options. The block manages the conversation state and generates appropriate responses. You can also configure tools that the AI can use during the conversation, such as function tools and Knowledge Graphs.

## Common use cases

* Building complete chat applications
* Creating AI assistants with conversation management
* Implementing interactive workflows with chat capabilities
* Developing conversational interfaces with tool calling

## How it works

1. **Conversation Object**: A binding variable that stores the chat history and metadata. If not provided or empty, a new conversation will be created and stored in the state.
2. **System prompt**: Set the context or behavior for the AI. Can be left empty if conversation is already initialized in state.
3. **Message**: Enter the user's message as an object with `role` and `content` properties; for example, `{"role": "user", "content": "What are the best practices for using the product?"}`. If you want to pass the user's message from the Chatbot interface to the Chat reply block, you can use the `@{payload}` variable.
4. **Configuration**: Set model (default: `palmyra-x5`), temperature (0-1), and max tokens (1-16384).
5. **Use streaming**: Choose whether to stream responses as they're generated or wait for complete responses.
6. **Tools configuration**: Configure tools that the AI can use during the conversation:
   * **Function tools**: Define custom functions with parameters that the AI can call
   * **Graph tools**: Connect to knowledge graphs for enhanced responses
   * **Tool routing**: Control when and how tools are called during the conversation
   * **Tool responses**: Handle and process the results returned from tool executions
   * See [tool calling](/agent-builder/tool-calling) for more information on how to configure tools.

## Examples

### Customer support chatbot

This example shows a customer support chatbot that can handle conversations and route to human agents if needed.

**Interface:**

1. A [**Chatbot** block](/components/chatbot) that displays the chat interface.

**Blueprint flow:**

1. **UI Trigger** → Customer sends message through chat interface
2. **Chat reply** → Processes message and generates AI response
3. **Classification** → Determines if human agent is needed
4. **Conditional routing** → Routes to human agent via HTTP Request block if a human agent is needed. Otherwise, the workflow starts again with the next user message.

**Chat reply block configuration:**

* **Conversation Object:** `@{chat}`
* **System prompt:**

```
You are a helpful customer support assistant. Be friendly and professional. 

IMPORTANT: If you encounter any of the following situations, clearly indicate that you need to route to a human agent:
- Complex technical issues beyond your capabilities
- Requests for account modifications or sensitive information
- Complaints that require escalation
- Situations where you're unsure or need human judgment
- Requests for supervisor or manager assistance

When routing to human, use phrases like:
- "I need to connect you with a human agent for this request"
- "Let me escalate this to our support team"
- "This requires human assistance, let me transfer you"
- "I'll need to route this to a specialist"

For routine questions and simple requests, provide helpful responses directly.
```

* **Message:** `@{payload}`. This passes the user's message from the Chatbot interface to the Chat reply block.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=76541492b5999661ffdd1190a826c841" alt="" data-og-width="2710" width="2710" data-og-height="1584" height="1584" data-path="images/agent-builder/blueprints/chat-reply-block-configuration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7e5d7db70deca5e39e60e2ae2ce9d63b 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=86e76f9dd55582ff536ac2f8b834a1b8 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=3bc500c437f17ace111258bdfce5a33e 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=03a568ae7472d7db10a6f626a0f532ac 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b9e0c9365ca20e5e4315b253c3ca19be 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c8f06c5b7d6b9879f704de2bf0bbf756 2500w" />

This workflow provides automated customer support while ensuring complex issues go to human agents.

### Connect a chatbot to a Knowledge Graph

This example shows a chatbot that can answer questions about domain-specific knowledge within a Knowledge Graph.

**Interface:**

1. A [**Chatbot** block](/components/chatbot) that displays the chat interface.

**Blueprint flow:**

1. **UI Trigger** → Customer sends message through chat interface
2. **Chat reply** → Processes message and generates AI response. Configured with a Knowledge Graph tool to answer questions about the company's products and services.

**Chat reply block configuration:**

* **Conversation Object:** `@{chat}`
* **System prompt:**

```
You are a helpful customer support assistant. Be friendly and professional. You have access to information about the company's products and services.
```

* **Tools:**
  * **Tool type:** `Knowledge Graph`
  * **Tool name:** A name to help you identify the tool in the response.
  * **Graph id(s):** The list of Knowledge Graphs to use. You can select from a list of available Knowledge Graphs.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration-kg.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1c8957c81dfbf1ba3af0a10ec643b53d" alt="" data-og-width="2806" width="2806" data-og-height="1550" height="1550" data-path="images/agent-builder/blueprints/chat-reply-block-configuration-kg.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration-kg.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7220f3ba8236d7170329d0f974fe1848 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration-kg.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=5eeb330d793ab56fe98e7f65e24114d1 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration-kg.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0f6a7525231a0678d5138d4be3306ca5 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration-kg.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=06eab707edd0366982bb8ffd8279318e 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration-kg.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=001e5334619d8864263abedab6836e51 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/chat-reply-block-configuration-kg.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f58131dfb9c2588156f1375b9b6abf01 2500w" />

This workflow provides a chatbot that can answer questions about the company's products and services.

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Conversation Object</td>
      <td>Binding</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>The variable that has your conversation object.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>System prompt</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <code>""</code>
      </td>

      <td>A system prompt to set the context for the conversation. Can be left empty if conversation is already initialized in state.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Message</td>
      <td>Object</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>A message object. Content can be text string or array of objects for multimodal (text + images) with X5 model.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Generate reply</td>
      <td>Boolean</td>
      <td>-</td>

      <td>
        <code>yes</code>
      </td>

      <td>If set to 'yes', the block will generate a reply from the model after adding the message. If set to 'no', it will only add the message to the conversation.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Initial model</td>
      <td>Model Id</td>
      <td>-</td>

      <td>
        <code>palmyra-x5</code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Initial temperature</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <code>0.7</code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        Range:
        0    to  2
      </td>
    </tr>

    <tr>
      <td>Initial max tokens</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <code>1024</code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        Range:
        1    to  16384
      </td>
    </tr>

    <tr>
      <td>Use streaming</td>
      <td>Boolean</td>
      <td>-</td>

      <td>
        <code>yes</code>
      </td>

      <td>If set to 'yes', the block will stream the reply as it is generated. If set to 'no', it will wait for the entire reply to be generated before returning.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Tools</td>
      <td>Tools</td>
      <td>-</td>

      <td>
        <code>
          {"{}"}
        </code>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Tools</td>
      <td>tools</td>
      <td>dynamic</td>
      <td>Run associated tools.</td>
    </tr>

    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>If the function doesn't raise an Exception.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>If the function raises an Exception.</td>
    </tr>
  </tbody>
</table>

The `dynamic` end state means that the exact values of this end state change based on how you define the block.

The output of the **Chat reply** block is a string with the most recent response from the AI to the user's message. You can access the output in the next block with the `@{result}` variable.
