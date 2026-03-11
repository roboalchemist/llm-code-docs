# Source: https://docs.base44.com/developers/references/cli/commands/types-generate.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# types generate

> Generate TypeScript types from project resources

Generate a TypeScript declaration file (`types.d.ts`) from your local project resources. The command reads your [entities](/developers/backend/resources/entities/overview), [functions](/developers/backend/resources/functions), [agents](/developers/backend/resources/agents-config), and [connectors](/developers/references/sdk/docs/interfaces/connectors), and produces a type file that augments the `@base44/sdk` module with project-specific types. This gives you autocomplete for resource names, compile-time type checking, and typed data when reading or writing entities.

The generated file is written to `base44/.types/types.d.ts`. If a `tsconfig.json` file exists in your project root, the command automatically adds `base44/.types/*.d.ts` to its `include` array so TypeScript picks up the types without any manual configuration.

<Note>
  Re-run this command whenever you add, remove, or modify a resource to keep the
  types in sync.
</Note>

## Usage

```bash  theme={null}
base44 types generate
```

## What gets generated

**Entities** generate a TypeScript interface for each entity from its JSON schema. Fields are typed with required/optional markers and nested object types. An `EntityTypeRegistry` interface maps each entity name to its generated interface.

**Functions**, **agents**, and **connectors** generate name registries only (`FunctionNameRegistry`, `AgentNameRegistry`, and `ConnectorTypeRegistry`). These list the names of your functions, agents, and connector integration types so your editor can autocomplete them, but they don't include parameter types, return types, or other configuration details.

## See also

* [Dynamic Types](/developers/references/sdk/getting-started/dynamic-types): Learn how to use generated types in your code
* [Entities](/developers/backend/resources/entities/overview): Learn about database schema configuration
* [Backend Functions](/developers/backend/resources/backend-functions/overview): Create serverless API endpoints
* [Agent Configurations](/developers/backend/resources/agents-config): Configure AI agents for your app
* [Project Structure](/developers/backend/overview/project-structure): How types fit into your project


Built with [Mintlify](https://mintlify.com).