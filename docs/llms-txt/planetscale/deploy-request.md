# Source: https://planetscale.com/docs/cli/deploy-request.md

# PlanetScale CLI commands: deploy-request

## Getting Started

Make sure to first [set up your PlanetScale developer environment](/docs/cli/planetscale-environment-setup). Once you've installed the `pscale` CLI, you can interact with PlanetScale and manage your databases straight from the command line.

## The `deploy-request` command

This command allows you to create, review, diff, and manage deploy requests for your Vitess clusters. This command is not currently available for Postgres database clusters.

**Usage:**

```bash  theme={null}
pscale deploy-request <SUB-COMMAND> <FLAG>
```

<Note>
  Your database must have a production branch with [safe migrations](/docs/vitess/schema-changes/safe-migrations) enabled before you can create a deploy request.
</Note>

### Available sub-commands

| Sub-command                                       | Sub-command flags                                                                       | Description                                              | **Product** |
| :------------------------------------------------ | :-------------------------------------------------------------------------------------- | :------------------------------------------------------- | :---------- |
| `apply <DATABASE_NAME> <DR_NUMBER>`               |                                                                                         | Trigger a deploy request to swap over to the new schema. | All         |
| `cancel <DATABASE_NAME> <DR_NUMBER>`              |                                                                                         | Cancel a deploy request.                                 | All         |
| `close <DATABASE_NAME> <DR_NUMBER>`               |                                                                                         | Close the specified deploy request.                      | All         |
| `create <DATABASE_NAME> <BRANCH_NAME>`            | `--into <BRANCH_NAME>`, `--notes <NOTE>`, `--enable-auto-apply`, `--disable-auto-apply` | Create a new deploy request.                             | All         |
| `deploy <DATABASE_NAME> <DR_NUMBER\|BRANCH_NAME>` | `--instant`                                                                             | Deploy the specified deploy request.                     | All         |
| `diff <DATABASE_NAME> <DR_NUMBER>`                | `--web`                                                                                 | Show the diff of the specified deploy request.           | All         |
| `edit <DATABASE_NAME> <DR_NUMBER>`                | `--enable-auto-apply`, `--disable-auto-apply`                                           | Edit a deploy request.                                   | All         |
| `list <DATABASE_NAME>`                            | `--web`                                                                                 | List all deploy requests for a database.                 | All         |
| `revert <DATABASE_NAME> <DR_NUMBER>`              |                                                                                         | Revert a deployed deploy request.                        | All         |
| `review <DATABASE_NAME> <DR_NUMBER>`              | `--web`, `--approve`, `--comment <COMMENT>`                                             | Approve or comment on a deploy request.                  | All         |
| `show <DATABASE_NAME> <DR_NUMBER\|BRANCH_NAME>`   | `--web`                                                                                 | Show the specified deploy request.                       | All         |
| `skip-revert <DATABASE_NAME> <DR_NUMBER>`         |                                                                                         | Skip and close a pending deploy request revert.          | All         |

> \* *Flag is required*

The value `<DR_NUMBER>` represents the deploy request number (not to be confused with `id`). To see a deploy request number, run `pscale deploy-request list <DATABASE_NAME>`.

You can also find the number in the PlanetScale dashboard in the URL of the specified deploy request: `https://app.planetscale.com/<ORGANIZATION>/<DATABASE>/deploy-requests/<DR_NUMBER>`.

#### Sub-command flag descriptions

Some of the sub-commands have additional flags unique to the sub-command. This section covers what each of those does. See the above table for which context.

| Sub-command flag       | Description                                                                                                                         | Applicable sub-commands |
| :--------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :---------------------- |
| `--into <BRANCH_NAME>` | Specify that the new deploy request deploy to a specified branch. Default is `main`.                                                | `create`                |
| `--notes <NOTE>`       | A note describing the deploy request. Acts as the first comment.                                                                    | `create`                |
| `--enable-auto-apply`  | Enable auto-apply for this deploy request. When enabled, the deploy request will swap over to the new schema once ready.            | `create`, `edit`        |
| `--disable-auto-apply` | Disable auto-apply for this deploy request. If neither flag is provided, the setting is inherited from the previous deploy request. | `create`, `edit`        |
| `--web`                | Perform the action in your web browser                                                                                              | `diff`, `list`, `show`  |
| `--approve`            | Approve a deploy request                                                                                                            | `review`                |
| `--comment <COMMENT>`  | Leave a comment on a deploy request                                                                                                 | `review`                |
| `--instant`            | Deploy a deploy request using MySQL's built-in ALGORITHM=INSTANT option. Deployment will be faster, but cannot be reverted.         | `deploy`                |

### Available flags

| Flag                        | Description                                                        |
| :-------------------------- | :----------------------------------------------------------------- |
| `-h`, `--help`              | Get help with the `deploy-request` command                         |
| `--org <ORGANIZATION_NAME>` | Specify the organization for the deploy request you're acting upon |

### Global flags

| Command                         | Description                                                                          |
| :------------------------------ | :----------------------------------------------------------------------------------- |
| `--api-token <TOKEN>`           | The API token to use for authenticating against the PlanetScale API.                 |
| `--api-url <URL>`               | The base URL for the PlanetScale API. Default is `https://api.planetscale.com/`.     |
| `--config <CONFIG_FILE>`        | Config file. Default is `$HOME/.config/planetscale/pscale.yml`.                      |
| `--debug`                       | Enable debug mode.                                                                   |
| `-f`, `--format <FORMAT>`       | Show output in a specific format. Possible values: `human` (default), `json`, `csv`. |
| `--no-color`                    | Disable color output.                                                                |
| `--service-token <TOKEN>`       | The service token for authenticating.                                                |
| `--service-token-id <TOKEN_ID>` | The service token ID for authenticating.                                             |

## Examples

### The `deploy-request` command with `review` subcommand and `--comment` flag

**Command:**

```bash  theme={null}
pscale deploy-request review <DATABASE_NAME> 1 --comment 'Lets wait on this.'
```

**Output:**

A comment is added to the deploy request `<DATABASE_NAME>`/1.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt