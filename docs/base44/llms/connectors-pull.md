# Source: https://docs.base44.com/developers/references/cli/commands/connectors-pull.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# connectors pull

> Pull connector configurations from Base44 to local files

Download [OAuth connector configurations](/developers/backend/resources/connectors) from Base44 to local `.jsonc` files. The command fetches all connectors and saves them to your connectors directory, one file per connector. By default the connectors directory is `base44/connectors/`, but you can customize the path in your [project configuration](/developers/backend/overview/project-structure#config-jsonc).

<Warning>
  This is a full sync. Local connectors not present remotely will be deleted. See the Sync behavior table below for details.
</Warning>

## Usage

```bash  theme={null}
base44 connectors pull
```

## Sync behavior

| Remote state            | Local state             | Result                              |
| ----------------------- | ----------------------- | ----------------------------------- |
| Connector exists        | Connector exists        | Local file is replaced with remote. |
| Connector exists        | Connector doesn't exist | Local file is created.              |
| Connector doesn't exist | Connector exists        | Local file is deleted.              |

## See also

* [`connectors push`](/developers/references/cli/commands/connectors-push): Push local connector configurations to Base44
* [Connectors](/developers/backend/resources/connectors): Learn how to configure OAuth connectors
* [Using Connectors](/Integrations/Connectors): Guide to using connectors in your app


Built with [Mintlify](https://mintlify.com).