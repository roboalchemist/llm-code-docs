# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-secret.md

# Source: https://docs.fireworks.ai/api-reference/update-secret.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-secret.md

# Source: https://docs.fireworks.ai/api-reference/update-secret.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-secret.md

# firectl update secret

> Updates an existing secret.

```
firectl update secret [flags]
```

### Examples

```
firectl update secret --id MY_SECRET --value newvalue
```

### Flags

```
  -h, --help           help for secret
      --id string      The id of the secret to be updated
      --value string   The new value of the secret
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
