# Source: https://docs.base44.com/developers/references/cli/commands/deploy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# deploy

> Deploy all project resources to Base44

Deploy all your project resources to Base44 in a single command. This includes [entities](/developers/backend/resources/entities/overview), [functions](/developers/backend/resources/backend-functions/overview), [connectors](/developers/backend/resources/connectors), and the build code for your frontend. The command provides a summary of what will be deployed and asks for confirmation before proceeding.

If any connectors require OAuth authorization, the deploy command will prompt you to authorize them in your browser, similar to running [`connectors push`](/developers/references/cli/commands/connectors-push).

You can also deploy resources individually using [`entities push`](/developers/references/cli/commands/entities-push), [`functions deploy`](/developers/references/cli/commands/functions-deploy), [`connectors push`](/developers/references/cli/commands/connectors-push), and [`site deploy`](/developers/references/cli/commands/site-deploy).

Before running this command, ensure that your built frontend files are in the directory specified by `site.outputDirectory` in your [`config.jsonc`](/developers/backend/overview/project-structure#config-jsonc) file.

## Usage

```bash  theme={null}
base44 deploy
```

## Sync behavior

The command performs a full sync for entities, functions, and connectors:

| Local state      | Remote state     | Result                                            |
| ---------------- | ---------------- | ------------------------------------------------- |
| Resource exists  | Resource exists  | Remote resource is updated                        |
| Resource exists  | Resource missing | New resource is created                           |
| Resource missing | Resource exists  | Remote resource is removed. See the warning below |

<Warning>
  Removing an entity removes its schema from Base44. Existing data is not deleted, but the entity will no longer be accessible through the SDK.

  Removing a function deletes it from Base44. Any endpoints or integrations that depend on the function will no longer work.

  Removing a connector removes the OAuth connection from Base44. Functions that use the connector will fail until it's reconnected.
</Warning>

## Flags

| Flag        | Description                  |
| ----------- | ---------------------------- |
| `-y, --yes` | Skip the confirmation prompt |

## See also

* [Project Structure](/developers/backend/overview/project-structure): How project resources are organized
* [Entities](/developers/backend/resources/entities/overview): Learn about database schema configuration
* [Backend Functions](/developers/backend/resources/backend-functions/overview): Create serverless API endpoints
* [Connectors](/developers/backend/resources/connectors): Set up OAuth connections to third-party services
* [`logs`](/developers/references/cli/commands/logs): View function logs after deploying


Built with [Mintlify](https://mintlify.com).