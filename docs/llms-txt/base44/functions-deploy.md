# Source: https://docs.base44.com/developers/references/cli/commands/functions-deploy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# functions deploy

> Deploy local functions to Base44

Deploy your local serverless [backend functions](/developers/backend/resources/backend-functions/overview) to Base44. The command reads all function directories in your functions folder, validates their configurations, and deploys them to your Base44 project.

<Note>
  Each project supports a maximum of 50 backend functions.
</Note>

## Usage

```bash  theme={null}
base44 functions deploy
```

## Sync behavior

The command performs a full sync operation. For each function, the action taken is determined by its state locally and remotely:

| Local state      | Remote state     | Result                                            |
| ---------------- | ---------------- | ------------------------------------------------- |
| Function exists  | Function exists  | Remote function is updated                        |
| Function exists  | Function missing | New remote function is created                    |
| Function missing | Function exists  | Remote function is removed. See the warning below |

<Warning>
  Deleting a function removes it from Base44. Any endpoints or integrations that depend on this function will no longer work.
</Warning>

## See also

* [Backend Functions](/developers/backend/resources/backend-functions/overview): Learn about backend functions
* [Project Structure](/developers/backend/overview/project-structure): How project files are organized
* [`logs`](/developers/references/cli/commands/logs): View function logs after deploying


Built with [Mintlify](https://mintlify.com).