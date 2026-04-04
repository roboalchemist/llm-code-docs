# Source: https://docs.baseten.co/reference/cli/truss/login.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# truss login

> Authenticate with Baseten.

```sh  theme={"system"}
truss login [OPTIONS]
```

Authenticates with Baseten, storing the API key in the local configuration file.

If used with no options, runs in interactive mode. Otherwise, the API key can be passed as an option.

### Options

<ParamField body="--api-key" type="TEXT">
  Baseten API key. If provided, the command runs in non-interactive mode.
</ParamField>

**Example:**

To authenticate interactively, use the following:

```sh  theme={"system"}
truss login
```

To authenticate with your API key, use the following:

```sh  theme={"system"}
truss login --api-key YOUR_API_KEY
```
