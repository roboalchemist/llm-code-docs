# Source: https://docs.base44.com/developers/references/cli/commands/agents-push.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# agents push

> Push local agent configurations to Base44

Upload local [AI agent configurations](/developers/backend/resources/agents-config) to Base44. The command reads all `.json` and `.jsonc` files in your `base44/agents/` directory and pushes them to Base44.

<Warning>
  This is a full sync. Remote agents not present locally will be deleted. See the Sync behavior table below for details.
</Warning>

## Usage

```bash  theme={null}
base44 agents push
```

## Sync behavior

| Local state         | Remote state        | Result                                  |
| ------------------- | ------------------- | --------------------------------------- |
| Agent exists        | Agent exists        | Remote agent configuration is replaced. |
| Agent exists        | Agent doesn't exist | New agent is created in Base44.         |
| Agent doesn't exist | Agent exists        | Remote agent is deleted.                |

## See also

* [`agents pull`](/developers/references/cli/commands/agents-pull): Sync agent configurations from Base44 to local
* [Agent Configurations](/developers/backend/resources/agents-config): Learn how to configure AI agents
* [Setting up AI agents](/Building-your-app/AI-agents): Guide to creating AI agents


Built with [Mintlify](https://mintlify.com).