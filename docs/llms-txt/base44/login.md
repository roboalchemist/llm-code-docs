# Source: https://docs.base44.com/developers/references/cli/commands/login.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# login

> Authenticate with Base44 using device code flow

Authenticate your CLI session with Base44. The CLI uses a secure device code flow, so you'll receive a code to enter in your browser to complete authentication.

For a walkthrough of the authentication process, see the [Backend only](/developers/backend/quickstart/templates/quickstart-backend-only) or [React](/developers/backend/quickstart/templates/quickstart-react-template) quickstart.

## Usage

```bash  theme={null}
base44 login
```

## Authentication storage

On successful login, your credentials are stored at `~/.base44/auth/auth.json`. This file contains your:

* Authentication token
* User email
* User display name

<Note>
  Your token remains valid until you explicitly log out or it expires. You don't
  need to log in before every command.
</Note>

## See also

* [Quickstart - Backend only](/developers/backend/quickstart/templates/quickstart-backend-only): Create your first backend-only project
* [Quickstart - React](/developers/backend/quickstart/templates/quickstart-react-template): Build a full-stack React app
* [`logout`](/developers/references/cli/commands/logout): Sign out from the CLI
* [`whoami`](/developers/references/cli/commands/whoami): Check your logged-in user


Built with [Mintlify](https://mintlify.com).