# Source: https://docs.baseten.co/reference/cli/truss/login.md

# truss login

> Authenticate with Baseten.

Authenticate with Baseten.

```
truss login [OPTIONS]
```

Authenticates with Baseten, storing the API key in the local configuration file.

If used with no options, runs in interactive mode. Otherwise, the API key can be passed as an option.

### Options

<ParamField body="--api-key">
  Baseten API Key. If this is passed, the command runs in non-interactive mode.
</ParamField>
