# Source: https://docs.base44.com/developers/references/cli/commands/agents-pull.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# agents pull

> Pull agent configurations from Base44 to local files

Download [AI agent configurations](/developers/backend/resources/agents-config) from Base44 to local JSONC files. The command saves all agents to the `base44/agents/` directory, one file per agent.

<Warning>
  This is a full sync. Local agents not present remotely will be deleted. See the Sync behavior table below for details.
</Warning>

## Usage

```bash  theme={null}
base44 agents pull
```

## Sync behavior

| Remote state        | Local state         | Result                              |
| ------------------- | ------------------- | ----------------------------------- |
| Agent exists        | Agent exists        | Local file is replaced with remote. |
| Agent exists        | Agent doesn't exist | Local file is created.              |
| Agent doesn't exist | Agent exists        | Local file is deleted.              |

## See also

* [`agents push`](/developers/references/cli/commands/agents-push): Deploy your local agent configurations
* [Agent Configurations](/developers/backend/resources/agents-config): Learn how to configure AI agents
* [Setting up AI agents](/Building-your-app/AI-agents): Guide to creating AI agents


Built with [Mintlify](https://mintlify.com).