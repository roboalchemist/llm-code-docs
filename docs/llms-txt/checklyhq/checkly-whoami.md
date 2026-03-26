# Source: https://checklyhq.com/docs/cli/checkly-whoami.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# checkly whoami

> Display current account and user information.

The `checkly whoami` command displays detailed information about your current Checkly authentication, including the logged-in user account and active Checkly account details.

This command can also be run without authentication to check your current status.

## Usage

The basic command shows current authentication status and account information.

```bash Terminal theme={null}
npx checkly whoami
```

### Authenticated

If you're logged in, you'll see:

```bash Terminal theme={null}
npx checkly whoami

You are currently on account "Monitoring as Code" (b2f...) as raccoon@checklyhq.com.
```

### Not Authenticated

If not logged in, you'll see:

```bash Terminal theme={null}
npx checkly whoami

Error: Run `npx checkly login` or manually set `CHECKLY_API_KEY` & `CHECKLY_ACCOUNT_ID`
environment variables to setup authentication.
```

## Related Commands

* [`checkly login`](/cli/checkly-login) - Sign in to your Checkly account
* [`checkly logout`](/cli/checkly-logout) - Sign out of your Checkly account
* [`checkly switch`](/cli/checkly-switch) - Switch between multiple accounts


Built with [Mintlify](https://mintlify.com).