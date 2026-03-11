# Source: https://docs.base44.com/developers/references/cli/commands/logout.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# logout

> Sign out and clear stored credentials

End your current CLI session and remove stored authentication credentials from your device.

## Usage

```bash  theme={null}
base44 logout
```

## What gets removed

Running `logout` deletes the authentication file at `~/.base44/auth/auth.json`. This file contains your:

* Authentication token
* Stored user email
* Stored user display name

After logging out, you'll need to run [`base44 login`](/developers/references/cli/commands/login) to authenticate again.

## See also

* [`login`](/developers/references/cli/commands/login): Sign in to the CLI
* [`whoami`](/developers/references/cli/commands/whoami): Check your logged-in user


Built with [Mintlify](https://mintlify.com).