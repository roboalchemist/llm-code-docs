# Source: https://docs.baseten.co/reference/cli/truss/whoami.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# truss whoami

> Show user information.

```sh  theme={"system"}
truss whoami [OPTIONS]
```

Shows the currently authenticated user information and exits. Use this command to verify your authentication status.

### Options

<ParamField body="--remote" type="TEXT">
  Name of the remote in .trussrc to check.
</ParamField>

**Example:**

To check the current authenticated user, use the following:

```sh  theme={"system"}
truss whoami
```
