# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-secret.md

# Source: https://docs.fireworks.ai/api-reference/create-secret.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-secret.md

# Source: https://docs.fireworks.ai/api-reference/create-secret.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-secret.md

# firectl create secret

> Creates a secret for the signed in user.

```
firectl create secret [flags]
```

### Examples

```
firectl create secret --name MY_SECRET --value mysecretvalue
```

### Flags

```
  -h, --help           help for secret
      --name string    The name of the secret to be created
      --value string   The value of the secret
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
