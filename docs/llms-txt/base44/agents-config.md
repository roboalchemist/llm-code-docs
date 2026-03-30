# Source: https://docs.base44.com/developers/backend/resources/agents-config.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# About Agents

> Define AI agents using local configuration files

<div className="dev-docs-banner">
  <div className="dev-docs-banner-content">
    <div className="dev-docs-banner-title">
      You're viewing developer documentation
    </div>

    <div className="dev-docs-banner-text">
      This documentation is for developers working with the Base44 developer platform. For information about AI agents in the app editor, see <a href="/Building-your-app/AI-agents">Setting up an AI agent</a>.
    </div>
  </div>
</div>

[AI agents](/Building-your-app/AI-agents) are customizable AI assistants that take action and connect to tools to help team members and end users. Define agent behavior, permissions, and tools using local JSONC configuration files.

## Create agents

Create JSONC configuration files in your `base44/agents/` directory (one file per agent), then run [`agents push`](/developers/references/cli/commands/agents-push) to sync them to Base44.

## Example

```jsonc  theme={null}
{
  "name": "customer_support",
  "description": "Handles customer support inquiries and ticket management",
  "instructions": "You are a friendly customer support agent. Help users resolve their issues politely and efficiently. If you cannot help, escalate to a human agent.",
  "model": "anthropic/claude-sonnet-4-20250514",
  "tool_configs": [
    {
      "entity_name": "tickets",
      "allowed_operations": ["read", "create", "update"],
    },
    {
      "entity_name": "customers",
      "allowed_operations": ["read"],
    },
    {
      "function_name": "send_notification",
      "description": "Sends a push notification to the customer",
    },
    {
      "function_name": "escalate_to_human",
      "description": "Escalates the conversation to a human support agent",
    },
  ],
  "whatsapp_greeting": "Hi, I'm your support assistant. How can I help you today?",
}
```

## Field reference

Agent configurations use JSONC. Each agent is defined in a separate file in the `base44/agents/` directory.

### Required fields

<ResponseField name="name" type="string" required>
  Unique identifier for the agent. Use lowercase letters and underscores. The
  name should match the filename, so an agent named `customer_support` would be
  in `customer_support.jsonc`.
</ResponseField>

<ResponseField name="description" type="string" required>
  Brief description of what the agent does.
</ResponseField>

<ResponseField name="instructions" type="string" required>
  System prompt that defines the agent's behavior, personality, and guidelines.
</ResponseField>

<ResponseField name="model" type="string" required>
  The AI model to use, in the format `provider/model-name`. Supported models: -
  `anthropic/claude-sonnet-4-20250514` - `anthropic/claude-3-5-sonnet-20241022`

  * `openai/gpt-4o` - `openai/gpt-4o-mini`
</ResponseField>

### Optional fields

<ResponseField name="tool_configs" type="array">
  Tools the agent can use to interact with your app. See [Tool
  configuration](#tool-configuration).
</ResponseField>

<ResponseField name="whatsapp_greeting" type="string">
  Welcome message for WhatsApp conversations with this agent.
</ResponseField>

## Tool configuration

The `tool_configs` array defines what capabilities your agent has. There are two types: **entity tools** and **function tools**.

### Entity tools

Entity tools allow the agent to perform CRUD operations on your app's [entities](/developers/backend/resources/entities/overview).

<ResponseField name="entity_name" type="string" required>
  Name of the entity. Must match an existing entity in your app.
</ResponseField>

<ResponseField name="allowed_operations" type="array" required>
  Operations the agent can perform on this entity. Valid values are `"read"`,
  `"create"`, `"update"`, and `"delete"`.
</ResponseField>

### Function tools

Function tools allow the agent to invoke your app's [backend functions](/developers/backend/resources/backend-functions/overview).

<ResponseField name="function_name" type="string" required>
  Name of the function. Must match an existing function in your app.
</ResponseField>

<ResponseField name="description" type="string" required>
  Description of what the function does. The agent uses this to decide when to
  call it.
</ResponseField>

## TypeScript types

Generate TypeScript types from your agent configurations to get type safety and autocomplete for agent names in your SDK code. Learn more about [dynamic types](/developers/references/sdk/getting-started/dynamic-types).

## See also

* [`agents pull`](/developers/references/cli/commands/agents-pull): Sync agent configurations from Base44 to your local project
* [`agents push`](/developers/references/cli/commands/agents-push): Deploy your local agent configurations to Base44
* [`agents`](/developers/references/sdk/docs/interfaces/agents): SDK reference for working with agents in your code
* [Setting up AI agents](/Building-your-app/AI-agents): Guide to creating and configuring AI agents


Built with [Mintlify](https://mintlify.com).