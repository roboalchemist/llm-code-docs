# Source: https://checklyhq.com/docs/cli/checkly-destroy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# checkly destroy

> Destroy all project resources from your Checkly account.

export const command_0 = "checkly destroy"

The `checkly destroy` command removes all resources associated with your project from your Checkly account, including checks, check groups, alert channels, maintenance windows, and other project-defined resources.

<Accordion title="Prerequisites">
  Before using <code>{command_0}</code>, ensure you have:

  * An initialized Checkly CLI project
  * At least one check or resource defined in your project
  * Valid Checkly account authentication (run `npx checkly login` if needed)
  * A `checkly.config.ts` or `checkly.config.js` configuration file

  For additional setup information, see [CLI overview](/cli/overview).
</Accordion>

<Warning>
  This command permanently deletes resources from your Checkly account. This action cannot be undone.
</Warning>

## Usage

The basic command destroys all project resources with a confirmation prompt.

```bash Terminal theme={null}
npx checkly destroy [options]
```

| Option         | Required | Description                                                                                                        |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------ |
| `--config, -c` | -        | The Checkly CLI configuration file. If not passed, uses the `checkly.config.ts\|js` file in the current directory. |
| `--force, -f`  | -        | Force mode. Skips the confirmation dialog.                                                                         |

## Command Options

<ResponseField name="--config, -c" type="string">
  Specify a particular configuration file to use instead of the default `checkly.config.ts` or `checkly.config.js`.

  **Usage:**

  ```bash Terminal theme={null}
  npx checkly destroy --config=<file-path>
  npx checkly destroy -c=<file-path>
  ```

  **Examples:**

  ```bash Terminal theme={null}
  $ npx checkly destroy --config="./checkly.staging.config.ts"
  ```
</ResponseField>

<ResponseField name="--force, -f" type="boolean">
  Skip confirmation dialogs and proceed with the operation.

  **Usage:**

  ```bash Terminal theme={null}
  npx checkly destroy --force
  npx checkly destroy -f
  ```

  <Warning>Use with extreme caution as this command option bypasses safety prompts.</Warning>
</ResponseField>

## What Gets Destroyed

The `destroy` command removes the all the resources managed by the specified project. These resources could include:

* **Checks** (API, Browser, Heartbeat, etc.)
* **Monitors** (URL, TCP, DNC, etc.)
* **Check Groups** and their configurations
* **Alert Channels** defined in your project
* **Maintenance Windows** created via CLI
* **Private Locations** (if managed by the project)

## Safety Considerations

By default, the command prompts for confirmation:

```bash Terminal theme={null}
$ npx checkly destroy

? Are you sure you want to delete all resources in project "Website Monitoring" for account "Monitoring as Code"?
Please confirm by typing the project name "Website Monitoring":
```

## Related Commands

* [`checkly deploy`](/cli/checkly-deploy) - Deploy resources to Checkly
* [`checkly test`](/cli/checkly-test) - Test your setup before deployment


Built with [Mintlify](https://mintlify.com).