# Source: https://docs.base44.com/developers/references/cli/commands/entities-push.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# entities push

> Push local entity schemas to Base44

Synchronize your local [entity schema definitions](/developers/backend/resources/entities/overview) with your Base44 project. The command reads all `.json` and `.jsonc` files in your entities directory, validates them, and pushes them to Base44.

Your project's entities directory is defined in the [`config.jsonc`](/developers/backend/overview/project-structure#config-jsonc) file.

## Usage

```bash  theme={null}
base44 entities push
```

## Sync behavior

The command performs a full sync operation. For each entity, the action taken is determined by its state locally and remotely:

| Local state    | Remote state   | Result                                          |
| -------------- | -------------- | ----------------------------------------------- |
| Entity exists  | Entity exists  | Remote schema is replaced                       |
| Entity exists  | Entity missing | New entity is created                           |
| Entity missing | Entity exists  | Remote entity is removed. See the warning below |

<Warning>
  Deleting an entity removes its schema from Base44. Existing data in that
  entity is not automatically deleted, but the entity will no longer be
  accessible through the SDK.
</Warning>

## See also

* [Project Structure](/developers/backend/overview/project-structure): How entity schemas fit into your project
* [Quickstart - Backend only](/developers/backend/quickstart/templates/quickstart-backend-only): Create your first backend-only project
* [Quickstart - React](/developers/backend/quickstart/templates/quickstart-react-template): Build a full-stack React app with Base44


Built with [Mintlify](https://mintlify.com).