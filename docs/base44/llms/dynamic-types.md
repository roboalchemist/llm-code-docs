# Source: https://docs.base44.com/developers/references/sdk/getting-started/dynamic-types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic Types

> Get full type safety and autocomplete with TypeScript types that stay in sync with your backend

When you work with Base44 in a TypeScript project, you can use dynamic types. Your [entities](/developers/references/sdk/docs/type-aliases/entities), [functions](/developers/references/sdk/docs/interfaces/functions), [agents](/developers/references/sdk/docs/interfaces/agents), and [connectors](/developers/references/sdk/docs/interfaces/connectors) have corresponding TypeScript types that provide:

* **Autocomplete**: Your IDE suggests available entities, fields, functions, agents, and connector integration types.
* **Type safety**: Catch typos and invalid fields at compile time instead of runtime.
* **Documentation**: Hover over types in your IDE to see field descriptions and types.

## How it works

Base44 reads your backend configuration and creates a `base44/.types/types.d.ts` file that augments the SDK with types from your project. The types file includes:

* Entity schemas with typed fields and CRUD operations
* Function names for autocomplete
* Agent names for autocomplete
* Connector integration type names for autocomplete

## Entity types

Dynamic types provide full type safety for all entity operations. Your entity fields, return types, and parameters are all strongly typed.

<CodeGroup>
  ```typescript CRUD operations theme={null}
  import type { EntityRecord } from "@base44/sdk";

  type TaskRecord = EntityRecord["Task"];

  // All fields are typed
  const task = await base44.entities.Task.create({
    title: "Complete documentation",
    status: "in-progress",
    priority: "high",
  });

  // Return type includes both your fields and server fields
  console.log(task.id); // Server field
  console.log(task.created_date); // Server field
  console.log(task.title); // Your field

  // Get with full type safety
  const retrieved = await base44.entities.Task.get(task.id);

  // Update with type checking
  await base44.entities.Task.update(task.id, {
    status: "completed",
  });
  ```

  ```typescript Field selection theme={null}
  import type { EntityRecord } from "@base44/sdk";

  type TaskRecord = EntityRecord["Task"];

  // Only get specific fields using autocomplete
  const tasks = await base44.entities.Task.list("-created_date", 10, 0, [
    "title",
    "status",
  ]);

  // TypeScript knows only selected fields are available
  tasks.forEach((task) => {
    console.log(task.title);
    console.log(task.status);
  });
  ```

  ```typescript Filtering theme={null}
  import type { EntityRecord } from "@base44/sdk";

  type TaskRecord = EntityRecord["Task"];

  // Query is type-checked against Task fields
  const activeTasks = await base44.entities.Task.filter({
    status: "active",
    priority: "high",
  });
  ```
</CodeGroup>

## Function types

Function names are typed for autocomplete when invoking functions:

```typescript  theme={null}
// Autocomplete shows all available functions
const result = await base44.functions.invoke("calculateTotal", {
  items: ["item1", "item2"],
});
```

<Note>
  Function parameter types are not generated. Refer to your function
  implementation for expected parameters.
</Note>

## Agent types

Agent names are typed for autocomplete when working with conversations:

```typescript  theme={null}
// Autocomplete shows all available agents
const conversation = await base44.agents.createConversation("SupportBot");
```

## Connector types

Connector integration type names are typed for autocomplete when retrieving connections:

```typescript  theme={null}
// Autocomplete shows all available connector integration types
const { accessToken } = await base44.asServiceRole.connectors.getConnection(
  "googlecalendar"
);
```

<Note>
  The connectors module is only available in service role mode (backend
  environments).
</Note>

## Generate types

To generate or update your types file, run the [`types generate`](/developers/references/cli/commands/types-generate) command:

```bash  theme={null}
base44 types generate
```

<Note>
  Re-run `types generate` whenever you modify entities, add functions, or change
  agents to keep types up to date.
</Note>

## See also

* [`types generate`](/developers/references/cli/commands/types-generate): CLI command to generate types from your project
* [`entities`](/developers/references/sdk/docs/type-aliases/entities): SDK reference for working with entities
* [`functions`](/developers/references/sdk/docs/interfaces/functions): SDK reference for invoking backend functions
* [`agents`](/developers/references/sdk/docs/interfaces/agents): SDK reference for working with AI agents
* [`connectors`](/developers/references/sdk/docs/interfaces/connectors): SDK reference for managing OAuth tokens


Built with [Mintlify](https://mintlify.com).