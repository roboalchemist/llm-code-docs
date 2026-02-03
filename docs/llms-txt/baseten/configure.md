# Source: https://docs.baseten.co/reference/cli/truss/configure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# truss configure

> Configure Truss settings.

```sh  theme={"system"}
truss configure [OPTIONS]
```

Configures Truss settings interactively. Use this command to set up or modify your local Truss configuration.

**Example:**

To configure Truss settings interactively, use the following:

```sh  theme={"system"}
truss configure
```

You should see a configuration file that you can edit, for example:

```yaml ~/.trussrc theme={"system"}
[baseten]
remote_provider = baseten
api_key = YOUR_API_KEY
remote_url = https://app.baseten.co
```
