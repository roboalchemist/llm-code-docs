# Source: https://checklyhq.com/docs/cli/checkly-logout.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# checkly logout

> Log out of your Checkly account.

The `checkly logout` command signs out of your current Checkly account and removes stored authentication tokens from your local machine.

<Accordion title="Prerequisites">
  Before using `checkly logout`, ensure you have:

  * Checkly CLI installed
  * Currently authenticated with Checkly CLI

  No internet connection is required as logout works locally.
</Accordion>

## Usage

The basic command logs out of your current Checkly account and removes stored authentication tokens.

```bash Terminal theme={null}
npx checkly logout [options]
```

| Option        | Required | Description                                |
| ------------- | -------- | ------------------------------------------ |
| `--force, -f` | -        | Force mode. Skips the confirmation dialog. |

## Command Options

<ResponseField name="--force, -f" type="boolean">
  Skip confirmation dialogs and proceed with the operation.

  Usage:

  ```bash Terminal theme={null}
  npx checkly logout --force
  npx checkly logout -f
  ```

  **Examples:**

  ```bash Terminal theme={null}
  # Standard logout
  npx checkly logout --force

  # Output
  See you soon! 👋
  ```
</ResponseField>

## What Happens During Logout

### Session Invalidation

The logout process will:

1. **Remove local tokens** from your machine
2. **Require re-authentication** for future CLI usage

### Token Removal

The command removes authentication tokens stored locally in:

* **macOS**: `~/Library/Preferences/@checkly/cli-nodejs/auth.json`
* **Linux**: `~/.config/@checkly/cli-nodejs/auth.json`
* **Windows**: `%APPDATA%\@checkly\cli-nodejs\auth.json`

## After Logout

Once logged out, you'll need to run [`checkly login`](/cli/checkly-login) before using other CLI commands that require authentication.

## Related Commands

* [`checkly login`](/cli/checkly-login) - Authenticate with your Checkly account
* [`checkly whoami`](/cli/checkly-whoami) - Display current account information
* [`checkly switch`](/cli/checkly-switch) - Switch between multiple accounts


Built with [Mintlify](https://mintlify.com).