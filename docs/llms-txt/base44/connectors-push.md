# Source: https://docs.base44.com/developers/references/cli/commands/connectors-push.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# connectors push

> Push local connector configurations to Base44

Upload local [OAuth connector configurations](/developers/backend/resources/connectors) to Base44. The command reads all `.json` and `.jsonc` files in your connectors directory and syncs them with Base44. By default the connectors directory is `base44/connectors/`, but you can customize the path in your [project configuration](/developers/backend/overview/project-structure#config-jsonc).

Connectors require OAuth authorization before they can be used with the SDK. When pushing connectors that need authorization, the CLI prompts you to authorize each connector one by one. The CLI will suggest opening your browser automatically, and if you accept, it iterates through each integration's authorization page sequentially. You can also use the displayed OAuth URLs to authorize manually.

You can push connectors without completing authorization, but they won't be usable until you authorize them. Run `connectors push` again later to complete authorization.

If you push a connector with the same scopes it already has, you won't need to reauthorize.

<Note>
  Connectors cannot be created or configured through the Base44 dashboard. You must define them in local configuration files and push them using the CLI.
</Note>

<Warning>
  This is a full sync. Remote connectors not present locally will be removed. See the Sync behavior table below for details.
</Warning>

## Usage

```bash  theme={null}
base44 connectors push
```

## Sync behavior

The command performs a full sync for connectors:

| Local state             | Remote state            | Result                                                     |
| ----------------------- | ----------------------- | ---------------------------------------------------------- |
| Connector exists        | Connector exists        | Remote connector scopes are updated.                       |
| Connector exists        | Connector doesn't exist | New connector is created and requires OAuth authorization. |
| Connector doesn't exist | Connector exists        | Remote connector is removed.                               |

## See also

* [Connectors](/developers/backend/resources/connectors)
* [deploy](/developers/references/cli/commands/deploy)
* [SDK connectors module](/developers/references/sdk/docs/interfaces/connectors)
* [Using Connectors](/Integrations/Connectors)


Built with [Mintlify](https://mintlify.com).