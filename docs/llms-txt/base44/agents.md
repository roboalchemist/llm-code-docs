# Source: https://docs.base44.com/developers/references/sdk/docs/interfaces/agents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# agents

***

## Overview

Agents module for managing AI agent conversations.

This module provides methods to create and manage conversations with AI agents,
send messages, and subscribe to realtime updates. Conversations can be used
for chat interfaces, support systems, or any interactive AI app.

### Key Features

The agents module enables you to:

* **Create conversations** with agents defined in the app.
* **Send messages** from users to agents and receive AI-generated responses.
* **Retrieve conversations** individually or as filtered lists with sorting and pagination.
* **Subscribe to realtime updates** using WebSocket connections to receive instant notifications when new messages arrive.
* **Attach metadata** to conversations for tracking context, categories, priorities, or linking to external systems.
* **Generate WhatsApp connection URLs** for users to interact with agents through WhatsApp.

### Conversation Structure

The agents module operates with a two-level hierarchy:

1. **Conversations**: Top-level containers that represent a dialogue with a specific agent. Each conversation has a unique ID, is associated with an agent by name, and belongs to the user who created it. Conversations can include optional metadata for tracking app-specific context like ticket IDs, categories, or custom fields.

2. **Messages**: Individual exchanges within a conversation. Each message has a role, content, and optional metadata like token usage, tool calls, file attachments, and reasoning information. Messages are stored as an array within their parent conversation.

### Authentication Modes

This module is available to use with a client in all authentication modes:

* **Anonymous or User authentication** (`base44.agents`): Access is scoped to the current user's permissions. Users must be authenticated to create and access conversations.
* **Service role authentication** (`base44.asServiceRole.agents`): Operations have elevated admin-level permissions. Can access all conversations that the app's admin role has access to.

### Generated Types

If you're working in a TypeScript project, you can generate types from your agents to get autocomplete on agent names when creating conversations or subscribing to updates. See the [Dynamic Types](/developers/references/sdk/getting-started/dynamic-types) guide to get started.

## Methods

### getConversations()

> **getConversations**(): `Promise`\<`AgentConversation`\[]>

Gets all conversations from all agents in the app.

Retrieves all conversations. Use [`listConversations()`](#listconversations) to filter which conversations are returned, apply sorting, or paginate results. Use [`getConversation()`](#getconversation) to retrieve a specific conversation by ID.

#### Returns

`AgentConversation`

An agent conversation containing messages exchanged with an AI agent.

<Accordion title="Properties">
  <ResponseField name="id" type="string" required>
    Unique identifier for the conversation.
  </ResponseField>

  <ResponseField name="app_id" type="string" required>
    App ID.
  </ResponseField>

  <ResponseField name="agent_name" type="string" required>
    Name of the agent in this conversation.
  </ResponseField>

  <ResponseField name="created_by_id" type="string" required>
    ID of the user who created the conversation.
  </ResponseField>

  <ResponseField name="created_date" type="string" required>
    When the conversation was created.
  </ResponseField>

  <ResponseField name="updated_date" type="string" required>
    When the conversation was last updated.
  </ResponseField>

  <ResponseField name="messages" type="AgentMessage[]" required>
    Array of messages in the conversation.

    <Accordion title="Properties">
      <ResponseField name="id" type="string" required>
        Unique identifier for the message.
      </ResponseField>

      <ResponseField name="role" type="&#x22;user&#x22; | &#x22;assistant&#x22; | &#x22;system&#x22;" required>
        Role of the message sender.
      </ResponseField>

      <ResponseField name="created_date" type="string" required>
        When the message was created.
      </ResponseField>

      <ResponseField name="updated_date" type="string" required>
        When the message was last updated.
      </ResponseField>

      <ResponseField name="reasoning" type="AgentMessageReasoning | null">
        Optional reasoning information for the message.

        <Accordion title="Properties">
          <ResponseField name="start_date" type="string" required>
            When reasoning started.
          </ResponseField>

          <ResponseField name="end_date" type="string">
            When reasoning ended.
          </ResponseField>

          <ResponseField name="content" type="string" required>
            Reasoning content.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="content" type="string | Record<string, any>">
        Message content.
      </ResponseField>

      <ResponseField name="file_urls" type="string[]">
        URLs to files attached to the message.
      </ResponseField>

      <ResponseField name="tool_calls" type="AgentMessageToolCall[]">
        Tool calls made by the agent.

        <Accordion title="Properties">
          <ResponseField name="id" type="string" required>
            Tool call ID.
          </ResponseField>

          <ResponseField name="name" type="string" required>
            Name of the tool called.
          </ResponseField>

          <ResponseField name="arguments_string" type="string" required>
            Arguments passed to the tool as JSON string.
          </ResponseField>

          <ResponseField name="status" type="&#x22;success&#x22; | &#x22;error&#x22; | &#x22;running&#x22; | &#x22;stopped&#x22;" required>
            Status of the tool call.
          </ResponseField>

          <ResponseField name="results" type="string">
            Results from the tool call.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="usage" type="AgentMessageUsage">
        Token usage statistics.

        <Accordion title="Properties">
          <ResponseField name="prompt_tokens" type="number">
            Number of tokens in the prompt.
          </ResponseField>

          <ResponseField name="completion_tokens" type="number">
            Number of tokens in the completion.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="hidden" type="boolean">
        Whether the message is hidden from the user.
      </ResponseField>

      <ResponseField name="custom_context" type="AgentMessageCustomContext[]">
        Custom context provided with the message.

        <Accordion title="Properties">
          <ResponseField name="message" type="string" required>
            Context message.
          </ResponseField>

          <ResponseField name="data" type="Record<string, any>" required>
            Associated data for the context.
          </ResponseField>

          <ResponseField name="type" type="string" required>
            Type of context.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="model" type="string">
        Model used to generate the message.
      </ResponseField>

      <ResponseField name="checkpoint_id" type="string">
        Checkpoint ID for the message.
      </ResponseField>

      <ResponseField name="metadata" type="AgentMessageMetadata">
        Metadata about when and by whom the message was created.

        <Accordion title="Properties">
          <ResponseField name="created_date" type="string" required>
            When the message was created.
          </ResponseField>

          <ResponseField name="created_by_email" type="string" required>
            Email of the user who created the message.
          </ResponseField>

          <ResponseField name="created_by_full_name" type="string" required>
            Full name of the user who created the message.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="additional_message_params" type="Record<string, any>">
        Additional custom parameters for the message.
      </ResponseField>
    </Accordion>
  </ResponseField>

  <ResponseField name="metadata" type="Record<string, any>">
    Optional metadata associated with the conversation.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Get all conversations theme={null}
  const conversations = await base44.agents.getConversations();
  console.log(`Total conversations: ${conversations.length}`);
  ```
</CodeGroup>

#### See

* [`listConversations()`](#listconversations) for filtering, sorting, and pagination
* [`getConversation()`](#getconversation) for retrieving a specific conversation by ID

***

### getConversation()

> **getConversation**(`conversationId`): `Promise`\<`AgentConversation` | `undefined`>

Gets a specific conversation by ID.

Retrieves a single conversation using its unique identifier. To retrieve
all conversations, use [`getConversations()`](#getconversations). To filter, sort, or paginate conversations, use [`listConversations()`](#listconversations).

This function returns the complete stored conversation including full tool call results, even for large responses.

#### Parameters

<ParamField body="conversationId" type="string" required>
  The unique identifier of the conversation.
</ParamField>

#### Returns

`AgentConversation`

An agent conversation containing messages exchanged with an AI agent.

<Accordion title="Properties">
  <ResponseField name="id" type="string" required>
    Unique identifier for the conversation.
  </ResponseField>

  <ResponseField name="app_id" type="string" required>
    App ID.
  </ResponseField>

  <ResponseField name="agent_name" type="string" required>
    Name of the agent in this conversation.
  </ResponseField>

  <ResponseField name="created_by_id" type="string" required>
    ID of the user who created the conversation.
  </ResponseField>

  <ResponseField name="created_date" type="string" required>
    When the conversation was created.
  </ResponseField>

  <ResponseField name="updated_date" type="string" required>
    When the conversation was last updated.
  </ResponseField>

  <ResponseField name="messages" type="AgentMessage[]" required>
    Array of messages in the conversation.

    <Accordion title="Properties">
      <ResponseField name="id" type="string" required>
        Unique identifier for the message.
      </ResponseField>

      <ResponseField name="role" type="&#x22;user&#x22; | &#x22;assistant&#x22; | &#x22;system&#x22;" required>
        Role of the message sender.
      </ResponseField>

      <ResponseField name="created_date" type="string" required>
        When the message was created.
      </ResponseField>

      <ResponseField name="updated_date" type="string" required>
        When the message was last updated.
      </ResponseField>

      <ResponseField name="reasoning" type="AgentMessageReasoning | null">
        Optional reasoning information for the message.

        <Accordion title="Properties">
          <ResponseField name="start_date" type="string" required>
            When reasoning started.
          </ResponseField>

          <ResponseField name="end_date" type="string">
            When reasoning ended.
          </ResponseField>

          <ResponseField name="content" type="string" required>
            Reasoning content.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="content" type="string | Record<string, any>">
        Message content.
      </ResponseField>

      <ResponseField name="file_urls" type="string[]">
        URLs to files attached to the message.
      </ResponseField>

      <ResponseField name="tool_calls" type="AgentMessageToolCall[]">
        Tool calls made by the agent.

        <Accordion title="Properties">
          <ResponseField name="id" type="string" required>
            Tool call ID.
          </ResponseField>

          <ResponseField name="name" type="string" required>
            Name of the tool called.
          </ResponseField>

          <ResponseField name="arguments_string" type="string" required>
            Arguments passed to the tool as JSON string.
          </ResponseField>

          <ResponseField name="status" type="&#x22;success&#x22; | &#x22;error&#x22; | &#x22;running&#x22; | &#x22;stopped&#x22;" required>
            Status of the tool call.
          </ResponseField>

          <ResponseField name="results" type="string">
            Results from the tool call.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="usage" type="AgentMessageUsage">
        Token usage statistics.

        <Accordion title="Properties">
          <ResponseField name="prompt_tokens" type="number">
            Number of tokens in the prompt.
          </ResponseField>

          <ResponseField name="completion_tokens" type="number">
            Number of tokens in the completion.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="hidden" type="boolean">
        Whether the message is hidden from the user.
      </ResponseField>

      <ResponseField name="custom_context" type="AgentMessageCustomContext[]">
        Custom context provided with the message.

        <Accordion title="Properties">
          <ResponseField name="message" type="string" required>
            Context message.
          </ResponseField>

          <ResponseField name="data" type="Record<string, any>" required>
            Associated data for the context.
          </ResponseField>

          <ResponseField name="type" type="string" required>
            Type of context.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="model" type="string">
        Model used to generate the message.
      </ResponseField>

      <ResponseField name="checkpoint_id" type="string">
        Checkpoint ID for the message.
      </ResponseField>

      <ResponseField name="metadata" type="AgentMessageMetadata">
        Metadata about when and by whom the message was created.

        <Accordion title="Properties">
          <ResponseField name="created_date" type="string" required>
            When the message was created.
          </ResponseField>

          <ResponseField name="created_by_email" type="string" required>
            Email of the user who created the message.
          </ResponseField>

          <ResponseField name="created_by_full_name" type="string" required>
            Full name of the user who created the message.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="additional_message_params" type="Record<string, any>">
        Additional custom parameters for the message.
      </ResponseField>
    </Accordion>
  </ResponseField>

  <ResponseField name="metadata" type="Record<string, any>">
    Optional metadata associated with the conversation.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Get a specific conversation by ID theme={null}
  const conversation = await base44.agents.getConversation('conv-123');
  if (conversation) {
    console.log(`Conversation has ${conversation.messages.length} messages`);
  }
  ```
</CodeGroup>

#### See

* [`getConversations()`](#getconversations) for retrieving all conversations
* [`listConversations()`](#listconversations) for filtering and sorting conversations

***

### listConversations()

> **listConversations**(`filterParams`): `Promise`\<`AgentConversation`\[]>

Lists conversations with filtering, sorting, and pagination.

Provides querying capabilities including filtering by fields, sorting, pagination, and field selection. For cases where you need all conversations without filtering, use [`getConversations()`](#getconversations). To retrieve a specific conversation by ID, use [`getConversation()`](#getconversation).

#### Parameters

<ParamField body="filterParams" type="ModelFilterParams" required>
  Filter parameters for querying conversations.
</ParamField>

<Accordion title="Properties">
  <ParamField body="q" type="Record<string, any>">
    Query object with field-value pairs for filtering.
  </ParamField>

  <ParamField body="sort" type="string | null">
    Sort parameter. For example, "-created\_date" for descending order.
  </ParamField>

  <ParamField body="sort_by" type="string | null">
    Alternative sort parameter. Use either `sort` or `sort_by`.
  </ParamField>

  <ParamField body="limit" type="number | null">
    Maximum number of results to return.
  </ParamField>

  <ParamField body="skip" type="number | null">
    Number of results to skip. Used for pagination.
  </ParamField>

  <ParamField body="fields" type="string[] | null">
    Array of field names to include in the response.
  </ParamField>
</Accordion>

#### Returns

`AgentConversation`

An agent conversation containing messages exchanged with an AI agent.

<Accordion title="Properties">
  <ResponseField name="id" type="string" required>
    Unique identifier for the conversation.
  </ResponseField>

  <ResponseField name="app_id" type="string" required>
    App ID.
  </ResponseField>

  <ResponseField name="agent_name" type="string" required>
    Name of the agent in this conversation.
  </ResponseField>

  <ResponseField name="created_by_id" type="string" required>
    ID of the user who created the conversation.
  </ResponseField>

  <ResponseField name="created_date" type="string" required>
    When the conversation was created.
  </ResponseField>

  <ResponseField name="updated_date" type="string" required>
    When the conversation was last updated.
  </ResponseField>

  <ResponseField name="messages" type="AgentMessage[]" required>
    Array of messages in the conversation.

    <Accordion title="Properties">
      <ResponseField name="id" type="string" required>
        Unique identifier for the message.
      </ResponseField>

      <ResponseField name="role" type="&#x22;user&#x22; | &#x22;assistant&#x22; | &#x22;system&#x22;" required>
        Role of the message sender.
      </ResponseField>

      <ResponseField name="created_date" type="string" required>
        When the message was created.
      </ResponseField>

      <ResponseField name="updated_date" type="string" required>
        When the message was last updated.
      </ResponseField>

      <ResponseField name="reasoning" type="AgentMessageReasoning | null">
        Optional reasoning information for the message.

        <Accordion title="Properties">
          <ResponseField name="start_date" type="string" required>
            When reasoning started.
          </ResponseField>

          <ResponseField name="end_date" type="string">
            When reasoning ended.
          </ResponseField>

          <ResponseField name="content" type="string" required>
            Reasoning content.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="content" type="string | Record<string, any>">
        Message content.
      </ResponseField>

      <ResponseField name="file_urls" type="string[]">
        URLs to files attached to the message.
      </ResponseField>

      <ResponseField name="tool_calls" type="AgentMessageToolCall[]">
        Tool calls made by the agent.

        <Accordion title="Properties">
          <ResponseField name="id" type="string" required>
            Tool call ID.
          </ResponseField>

          <ResponseField name="name" type="string" required>
            Name of the tool called.
          </ResponseField>

          <ResponseField name="arguments_string" type="string" required>
            Arguments passed to the tool as JSON string.
          </ResponseField>

          <ResponseField name="status" type="&#x22;success&#x22; | &#x22;error&#x22; | &#x22;running&#x22; | &#x22;stopped&#x22;" required>
            Status of the tool call.
          </ResponseField>

          <ResponseField name="results" type="string">
            Results from the tool call.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="usage" type="AgentMessageUsage">
        Token usage statistics.

        <Accordion title="Properties">
          <ResponseField name="prompt_tokens" type="number">
            Number of tokens in the prompt.
          </ResponseField>

          <ResponseField name="completion_tokens" type="number">
            Number of tokens in the completion.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="hidden" type="boolean">
        Whether the message is hidden from the user.
      </ResponseField>

      <ResponseField name="custom_context" type="AgentMessageCustomContext[]">
        Custom context provided with the message.

        <Accordion title="Properties">
          <ResponseField name="message" type="string" required>
            Context message.
          </ResponseField>

          <ResponseField name="data" type="Record<string, any>" required>
            Associated data for the context.
          </ResponseField>

          <ResponseField name="type" type="string" required>
            Type of context.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="model" type="string">
        Model used to generate the message.
      </ResponseField>

      <ResponseField name="checkpoint_id" type="string">
        Checkpoint ID for the message.
      </ResponseField>

      <ResponseField name="metadata" type="AgentMessageMetadata">
        Metadata about when and by whom the message was created.

        <Accordion title="Properties">
          <ResponseField name="created_date" type="string" required>
            When the message was created.
          </ResponseField>

          <ResponseField name="created_by_email" type="string" required>
            Email of the user who created the message.
          </ResponseField>

          <ResponseField name="created_by_full_name" type="string" required>
            Full name of the user who created the message.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="additional_message_params" type="Record<string, any>">
        Additional custom parameters for the message.
      </ResponseField>
    </Accordion>
  </ResponseField>

  <ResponseField name="metadata" type="Record<string, any>">
    Optional metadata associated with the conversation.
  </ResponseField>
</Accordion>

#### Examples

<CodeGroup>
  ```typescript List recent conversations with pagination theme={null}
  const recentConversations = await base44.agents.listConversations({
    limit: 10,
    sort: '-created_date'
  });
  ```

  ```typescript Filter by agent and metadata theme={null}
  const supportConversations = await base44.agents.listConversations({
    q: {
      agent_name: 'support-agent',
      'metadata.priority': 'high'
    },
    sort: '-created_date',
    limit: 20
  });
  ```
</CodeGroup>

#### See

* [`getConversations()`](#getconversations) for retrieving all conversations without filtering
* [`getConversation()`](#getconversation) for retrieving a specific conversation by ID

***

### createConversation()

> **createConversation**(`conversation`): `Promise`\<`AgentConversation`>

Creates a new conversation with an agent.

#### Parameters

<ParamField body="conversation" type="CreateConversationParams" required>
  Conversation details including agent name and optional metadata.
</ParamField>

<Accordion title="Properties">
  <ParamField body="agent_name" type="string" required>
    The name of the agent to create a conversation with.
  </ParamField>

  <ParamField body="metadata" type="Record<string, any>">
    Optional metadata to attach to the conversation.
  </ParamField>
</Accordion>

#### Returns

`AgentConversation`

An agent conversation containing messages exchanged with an AI agent.

<Accordion title="Properties">
  <ResponseField name="id" type="string" required>
    Unique identifier for the conversation.
  </ResponseField>

  <ResponseField name="app_id" type="string" required>
    App ID.
  </ResponseField>

  <ResponseField name="agent_name" type="string" required>
    Name of the agent in this conversation.
  </ResponseField>

  <ResponseField name="created_by_id" type="string" required>
    ID of the user who created the conversation.
  </ResponseField>

  <ResponseField name="created_date" type="string" required>
    When the conversation was created.
  </ResponseField>

  <ResponseField name="updated_date" type="string" required>
    When the conversation was last updated.
  </ResponseField>

  <ResponseField name="messages" type="AgentMessage[]" required>
    Array of messages in the conversation.

    <Accordion title="Properties">
      <ResponseField name="id" type="string" required>
        Unique identifier for the message.
      </ResponseField>

      <ResponseField name="role" type="&#x22;user&#x22; | &#x22;assistant&#x22; | &#x22;system&#x22;" required>
        Role of the message sender.
      </ResponseField>

      <ResponseField name="created_date" type="string" required>
        When the message was created.
      </ResponseField>

      <ResponseField name="updated_date" type="string" required>
        When the message was last updated.
      </ResponseField>

      <ResponseField name="reasoning" type="AgentMessageReasoning | null">
        Optional reasoning information for the message.

        <Accordion title="Properties">
          <ResponseField name="start_date" type="string" required>
            When reasoning started.
          </ResponseField>

          <ResponseField name="end_date" type="string">
            When reasoning ended.
          </ResponseField>

          <ResponseField name="content" type="string" required>
            Reasoning content.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="content" type="string | Record<string, any>">
        Message content.
      </ResponseField>

      <ResponseField name="file_urls" type="string[]">
        URLs to files attached to the message.
      </ResponseField>

      <ResponseField name="tool_calls" type="AgentMessageToolCall[]">
        Tool calls made by the agent.

        <Accordion title="Properties">
          <ResponseField name="id" type="string" required>
            Tool call ID.
          </ResponseField>

          <ResponseField name="name" type="string" required>
            Name of the tool called.
          </ResponseField>

          <ResponseField name="arguments_string" type="string" required>
            Arguments passed to the tool as JSON string.
          </ResponseField>

          <ResponseField name="status" type="&#x22;success&#x22; | &#x22;error&#x22; | &#x22;running&#x22; | &#x22;stopped&#x22;" required>
            Status of the tool call.
          </ResponseField>

          <ResponseField name="results" type="string">
            Results from the tool call.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="usage" type="AgentMessageUsage">
        Token usage statistics.

        <Accordion title="Properties">
          <ResponseField name="prompt_tokens" type="number">
            Number of tokens in the prompt.
          </ResponseField>

          <ResponseField name="completion_tokens" type="number">
            Number of tokens in the completion.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="hidden" type="boolean">
        Whether the message is hidden from the user.
      </ResponseField>

      <ResponseField name="custom_context" type="AgentMessageCustomContext[]">
        Custom context provided with the message.

        <Accordion title="Properties">
          <ResponseField name="message" type="string" required>
            Context message.
          </ResponseField>

          <ResponseField name="data" type="Record<string, any>" required>
            Associated data for the context.
          </ResponseField>

          <ResponseField name="type" type="string" required>
            Type of context.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="model" type="string">
        Model used to generate the message.
      </ResponseField>

      <ResponseField name="checkpoint_id" type="string">
        Checkpoint ID for the message.
      </ResponseField>

      <ResponseField name="metadata" type="AgentMessageMetadata">
        Metadata about when and by whom the message was created.

        <Accordion title="Properties">
          <ResponseField name="created_date" type="string" required>
            When the message was created.
          </ResponseField>

          <ResponseField name="created_by_email" type="string" required>
            Email of the user who created the message.
          </ResponseField>

          <ResponseField name="created_by_full_name" type="string" required>
            Full name of the user who created the message.
          </ResponseField>
        </Accordion>
      </ResponseField>

      <ResponseField name="additional_message_params" type="Record<string, any>">
        Additional custom parameters for the message.
      </ResponseField>
    </Accordion>
  </ResponseField>

  <ResponseField name="metadata" type="Record<string, any>">
    Optional metadata associated with the conversation.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Create a new conversation with metadata theme={null}
  const conversation = await base44.agents.createConversation({
    agent_name: 'support-agent',
    metadata: {
      order_id: 'ORD-789',
      product_id: 'PROD-456',
      category: 'technical-support'
    }
  });
  console.log(`Created conversation: ${conversation.id}`);
  ```
</CodeGroup>

***

### addMessage()

> **addMessage**(`conversation`, `message`): `Promise`\<`AgentMessage`>

Adds a message to a conversation.

Sends a message to the agent and updates the conversation. This method
also updates the realtime socket to notify any subscribers.

#### Parameters

<Accordion title="Properties">
  <ParamField body="conversation" type="AgentConversation" required>
    The conversation to add the message to.
  </ParamField>

  <Accordion title="Properties">
    <ParamField body="id" type="string" required>
      Unique identifier for the conversation.
    </ParamField>

    <ParamField body="app_id" type="string" required>
      App ID.
    </ParamField>

    <ParamField body="agent_name" type="string" required>
      Name of the agent in this conversation.
    </ParamField>

    <ParamField body="created_by_id" type="string" required>
      ID of the user who created the conversation.
    </ParamField>

    <ParamField body="created_date" type="string" required>
      When the conversation was created.
    </ParamField>

    <ParamField body="updated_date" type="string" required>
      When the conversation was last updated.
    </ParamField>

    <ParamField body="messages" type="AgentMessage[]" required>
      Array of messages in the conversation.

      <Accordion title="Properties">
        <ParamField body="id" type="string" required>
          Unique identifier for the message.
        </ParamField>

        <ParamField body="role" type="&#x22;user&#x22; | &#x22;assistant&#x22; | &#x22;system&#x22;" required>
          Role of the message sender.
        </ParamField>

        <ParamField body="created_date" type="string" required>
          When the message was created.
        </ParamField>

        <ParamField body="updated_date" type="string" required>
          When the message was last updated.
        </ParamField>

        <ParamField body="reasoning" type="AgentMessageReasoning | null">
          Optional reasoning information for the message.

          <Accordion title="Properties">
            <ParamField body="start_date" type="string" required>
              When reasoning started.
            </ParamField>

            <ParamField body="end_date" type="string">
              When reasoning ended.
            </ParamField>

            <ParamField body="content" type="string" required>
              Reasoning content.
            </ParamField>
          </Accordion>
        </ParamField>

        <ParamField body="content" type="string | Record<string, any>">
          Message content.
        </ParamField>

        <ParamField body="file_urls" type="string[]">
          URLs to files attached to the message.
        </ParamField>

        <ParamField body="tool_calls" type="AgentMessageToolCall[]">
          Tool calls made by the agent.

          <Accordion title="Properties">
            <ParamField body="id" type="string" required>
              Tool call ID.
            </ParamField>

            <ParamField body="name" type="string" required>
              Name of the tool called.
            </ParamField>

            <ParamField body="arguments_string" type="string" required>
              Arguments passed to the tool as JSON string.
            </ParamField>

            <ParamField body="status" type="&#x22;success&#x22; | &#x22;error&#x22; | &#x22;running&#x22; | &#x22;stopped&#x22;" required>
              Status of the tool call.
            </ParamField>

            <ParamField body="results" type="string">
              Results from the tool call.
            </ParamField>
          </Accordion>
        </ParamField>

        <ParamField body="usage" type="AgentMessageUsage">
          Token usage statistics.

          <Accordion title="Properties">
            <ParamField body="prompt_tokens" type="number">
              Number of tokens in the prompt.
            </ParamField>

            <ParamField body="completion_tokens" type="number">
              Number of tokens in the completion.
            </ParamField>
          </Accordion>
        </ParamField>

        <ParamField body="hidden" type="boolean">
          Whether the message is hidden from the user.
        </ParamField>

        <ParamField body="custom_context" type="AgentMessageCustomContext[]">
          Custom context provided with the message.

          <Accordion title="Properties">
            <ParamField body="message" type="string" required>
              Context message.
            </ParamField>

            <ParamField body="data" type="Record<string, any>" required>
              Associated data for the context.
            </ParamField>

            <ParamField body="type" type="string" required>
              Type of context.
            </ParamField>
          </Accordion>
        </ParamField>

        <ParamField body="model" type="string">
          Model used to generate the message.
        </ParamField>

        <ParamField body="checkpoint_id" type="string">
          Checkpoint ID for the message.
        </ParamField>

        <ParamField body="metadata" type="AgentMessageMetadata">
          Metadata about when and by whom the message was created.

          <Accordion title="Properties">
            <ParamField body="created_date" type="string" required>
              When the message was created.
            </ParamField>

            <ParamField body="created_by_email" type="string" required>
              Email of the user who created the message.
            </ParamField>

            <ParamField body="created_by_full_name" type="string" required>
              Full name of the user who created the message.
            </ParamField>
          </Accordion>
        </ParamField>

        <ParamField body="additional_message_params" type="Record<string, any>">
          Additional custom parameters for the message.
        </ParamField>
      </Accordion>
    </ParamField>

    <ParamField body="metadata" type="Record<string, any>">
      Optional metadata associated with the conversation.
    </ParamField>
  </Accordion>

  <ParamField body="message" type="Partial<AgentMessage>" required>
    The message to add.
  </ParamField>

  <Accordion title="Properties">
    <ParamField body="id" type="string" required>
      Unique identifier for the message.
    </ParamField>

    <ParamField body="role" type="&#x22;user&#x22; | &#x22;assistant&#x22; | &#x22;system&#x22;" required>
      Role of the message sender.
    </ParamField>

    <ParamField body="created_date" type="string" required>
      When the message was created.
    </ParamField>

    <ParamField body="updated_date" type="string" required>
      When the message was last updated.
    </ParamField>

    <ParamField body="reasoning" type="AgentMessageReasoning | null">
      Optional reasoning information for the message.

      <Accordion title="Properties">
        <ParamField body="start_date" type="string" required>
          When reasoning started.
        </ParamField>

        <ParamField body="end_date" type="string">
          When reasoning ended.
        </ParamField>

        <ParamField body="content" type="string" required>
          Reasoning content.
        </ParamField>
      </Accordion>
    </ParamField>

    <ParamField body="content" type="string | Record<string, any>">
      Message content.
    </ParamField>

    <ParamField body="file_urls" type="string[]">
      URLs to files attached to the message.
    </ParamField>

    <ParamField body="tool_calls" type="AgentMessageToolCall[]">
      Tool calls made by the agent.

      <Accordion title="Properties">
        <ParamField body="id" type="string" required>
          Tool call ID.
        </ParamField>

        <ParamField body="name" type="string" required>
          Name of the tool called.
        </ParamField>

        <ParamField body="arguments_string" type="string" required>
          Arguments passed to the tool as JSON string.
        </ParamField>

        <ParamField body="status" type="&#x22;success&#x22; | &#x22;error&#x22; | &#x22;running&#x22; | &#x22;stopped&#x22;" required>
          Status of the tool call.
        </ParamField>

        <ParamField body="results" type="string">
          Results from the tool call.
        </ParamField>
      </Accordion>
    </ParamField>

    <ParamField body="usage" type="AgentMessageUsage">
      Token usage statistics.

      <Accordion title="Properties">
        <ParamField body="prompt_tokens" type="number">
          Number of tokens in the prompt.
        </ParamField>

        <ParamField body="completion_tokens" type="number">
          Number of tokens in the completion.
        </ParamField>
      </Accordion>
    </ParamField>

    <ParamField body="hidden" type="boolean">
      Whether the message is hidden from the user.
    </ParamField>

    <ParamField body="custom_context" type="AgentMessageCustomContext[]">
      Custom context provided with the message.

      <Accordion title="Properties">
        <ParamField body="message" type="string" required>
          Context message.
        </ParamField>

        <ParamField body="data" type="Record<string, any>" required>
          Associated data for the context.
        </ParamField>

        <ParamField body="type" type="string" required>
          Type of context.
        </ParamField>
      </Accordion>
    </ParamField>

    <ParamField body="model" type="string">
      Model used to generate the message.
    </ParamField>

    <ParamField body="checkpoint_id" type="string">
      Checkpoint ID for the message.
    </ParamField>

    <ParamField body="metadata" type="AgentMessageMetadata">
      Metadata about when and by whom the message was created.

      <Accordion title="Properties">
        <ParamField body="created_date" type="string" required>
          When the message was created.
        </ParamField>

        <ParamField body="created_by_email" type="string" required>
          Email of the user who created the message.
        </ParamField>

        <ParamField body="created_by_full_name" type="string" required>
          Full name of the user who created the message.
        </ParamField>
      </Accordion>
    </ParamField>

    <ParamField body="additional_message_params" type="Record<string, any>">
      Additional custom parameters for the message.
    </ParamField>
  </Accordion>
</Accordion>

#### Returns

`AgentMessage`

A message in an agent conversation.

<Accordion title="Properties">
  <ResponseField name="id" type="string" required>
    Unique identifier for the message.
  </ResponseField>

  <ResponseField name="role" type="&#x22;user&#x22; | &#x22;assistant&#x22; | &#x22;system&#x22;" required>
    Role of the message sender.
  </ResponseField>

  <ResponseField name="created_date" type="string" required>
    When the message was created.
  </ResponseField>

  <ResponseField name="updated_date" type="string" required>
    When the message was last updated.
  </ResponseField>

  <ResponseField name="reasoning" type="AgentMessageReasoning | null">
    Optional reasoning information for the message.

    <Accordion title="Properties">
      <ResponseField name="start_date" type="string" required>
        When reasoning started.
      </ResponseField>

      <ResponseField name="end_date" type="string">
        When reasoning ended.
      </ResponseField>

      <ResponseField name="content" type="string" required>
        Reasoning content.
      </ResponseField>
    </Accordion>
  </ResponseField>

  <ResponseField name="content" type="string | Record<string, any>">
    Message content.
  </ResponseField>

  <ResponseField name="file_urls" type="string[]">
    URLs to files attached to the message.
  </ResponseField>

  <ResponseField name="tool_calls" type="AgentMessageToolCall[]">
    Tool calls made by the agent.

    <Accordion title="Properties">
      <ResponseField name="id" type="string" required>
        Tool call ID.
      </ResponseField>

      <ResponseField name="name" type="string" required>
        Name of the tool called.
      </ResponseField>

      <ResponseField name="arguments_string" type="string" required>
        Arguments passed to the tool as JSON string.
      </ResponseField>

      <ResponseField name="status" type="&#x22;success&#x22; | &#x22;error&#x22; | &#x22;running&#x22; | &#x22;stopped&#x22;" required>
        Status of the tool call.
      </ResponseField>

      <ResponseField name="results" type="string">
        Results from the tool call.
      </ResponseField>
    </Accordion>
  </ResponseField>

  <ResponseField name="usage" type="AgentMessageUsage">
    Token usage statistics.

    <Accordion title="Properties">
      <ResponseField name="prompt_tokens" type="number">
        Number of tokens in the prompt.
      </ResponseField>

      <ResponseField name="completion_tokens" type="number">
        Number of tokens in the completion.
      </ResponseField>
    </Accordion>
  </ResponseField>

  <ResponseField name="hidden" type="boolean">
    Whether the message is hidden from the user.
  </ResponseField>

  <ResponseField name="custom_context" type="AgentMessageCustomContext[]">
    Custom context provided with the message.

    <Accordion title="Properties">
      <ResponseField name="message" type="string" required>
        Context message.
      </ResponseField>

      <ResponseField name="data" type="Record<string, any>" required>
        Associated data for the context.
      </ResponseField>

      <ResponseField name="type" type="string" required>
        Type of context.
      </ResponseField>
    </Accordion>
  </ResponseField>

  <ResponseField name="model" type="string">
    Model used to generate the message.
  </ResponseField>

  <ResponseField name="checkpoint_id" type="string">
    Checkpoint ID for the message.
  </ResponseField>

  <ResponseField name="metadata" type="AgentMessageMetadata">
    Metadata about when and by whom the message was created.

    <Accordion title="Properties">
      <ResponseField name="created_date" type="string" required>
        When the message was created.
      </ResponseField>

      <ResponseField name="created_by_email" type="string" required>
        Email of the user who created the message.
      </ResponseField>

      <ResponseField name="created_by_full_name" type="string" required>
        Full name of the user who created the message.
      </ResponseField>
    </Accordion>
  </ResponseField>

  <ResponseField name="additional_message_params" type="Record<string, any>">
    Additional custom parameters for the message.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Send a message to the agent theme={null}
  const message = await base44.agents.addMessage(conversation, {
    role: 'user',
    content: 'Hello, I need help with my order #12345'
  });
  console.log(`Message sent with ID: ${message.id}`);
  ```
</CodeGroup>

***

### subscribeToConversation()

> **subscribeToConversation**(`conversationId`, `onUpdate?`): () => `void`

Subscribes to realtime updates for a conversation.

Establishes a WebSocket connection to receive instant updates when new
messages are added to the conversation. Returns an unsubscribe function
to clean up the connection.

<Note>
  When receiving messages through this function, tool call data is truncated for efficiency. The `arguments_string` is limited to 500 characters and `results` to 50 characters. The complete tool call data is always saved in storage and can be retrieved by calling [`getConversation()`](#getconversation) after the message completes.
</Note>

#### Parameters

<Accordion title="Properties">
  <ParamField body="conversationId" type="string" required>
    The conversation ID to subscribe to.
  </ParamField>

  <ParamField body="onUpdate" type="(conversation) => void">
    Callback function called when the conversation is updated. The callback receives a conversation object with the following properties:

    * `id`: Unique identifier for the conversation.
    * `agent_name`: Name of the agent in this conversation.
    * `created_date`: ISO 8601 timestamp of when the conversation was created.
    * `updated_date`: ISO 8601 timestamp of when the conversation was last updated.
    * `messages`: Array of messages in the conversation. Each message includes `id`, `role` (`'user'`, `'assistant'`, or `'system'`), `content`, `created_date`, and optionally `tool_calls`, `reasoning`, `file_urls`, and `usage`.
    * `metadata`: Optional metadata associated with the conversation.
  </ParamField>
</Accordion>

#### Returns

Unsubscribe function to stop receiving updates.

#### Example

<CodeGroup>
  ```typescript Subscribe to realtime updates theme={null}
  const unsubscribe = base44.agents.subscribeToConversation(
    'conv-123',
    (updatedConversation) => {
      const latestMessage = updatedConversation.messages[updatedConversation.messages.length - 1];
      console.log('New message:', latestMessage.content);
    }
  );

  // Later, clean up the subscription
  unsubscribe();
  ```
</CodeGroup>

***

### getWhatsAppConnectURL()

> **getWhatsAppConnectURL**(`agentName`): `string`

Gets WhatsApp connection URL for an agent.

Generates a URL that users can use to connect with the agent through WhatsApp.
The URL includes authentication if a token is available.

#### Parameters

<ParamField body="agentName" type="string" required>
  The name of the agent.
</ParamField>

#### Returns

`string`

WhatsApp connection URL.

#### Example

<CodeGroup>
  ```typescript Get WhatsApp connection URL theme={null}
  const whatsappUrl = base44.agents.getWhatsAppConnectURL('support-agent');
  console.log(`Connect through WhatsApp: ${whatsappUrl}`);
  // User can open this URL to start a WhatsApp conversation
  ```
</CodeGroup>

## Type Definitions

### AgentName

***

> **AgentName** = keyof `AgentNameRegistry` *extends* `never` ? `string` : keyof `AgentNameRegistry`

Union of all agent names from the [`AgentNameRegistry`](#agentnameregistry). Defaults to `string` when no types have been generated.

#### Example

<CodeGroup>
  ```typescript Using generated agent name types theme={null}
  // With generated types, you get autocomplete on agent names
  const conversation = await base44.agents.createConversation({ agent_name: 'SupportBot' });
  ```
</CodeGroup>

### AgentNameRegistry

***

Registry of agent names. The [`types generate`](/developers/references/cli/commands/types-generate) command fills this registry, then [`AgentName`](#agentname) resolves to a union of the keys.


Built with [Mintlify](https://mintlify.com).