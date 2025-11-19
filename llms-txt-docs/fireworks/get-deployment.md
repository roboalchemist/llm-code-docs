# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-deployment.md

# Source: https://docs.fireworks.ai/api-reference/get-deployment.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-deployment.md

# firectl get deployment

> Prints information about a deployment.

```
firectl get deployment [flags]
```

### Examples

```
firectl get deployment my-deployment
firectl get deployment accounts/my-account/deployments/my-deployment
```

### Flags

```
  -h, --help   help for deployment
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
