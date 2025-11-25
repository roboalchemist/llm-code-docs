# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-model.md

# Source: https://docs.fireworks.ai/api-reference/get-model.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-model.md

# Source: https://docs.fireworks.ai/api-reference/get-model.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-model.md

# firectl get model

> Prints information about a model.

```
firectl get model [flags]
```

### Examples

```
firectl get model my-model
firectl get model accounts/fireworks/models/my-model
```

### Flags

```
  -h, --help   help for model
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
