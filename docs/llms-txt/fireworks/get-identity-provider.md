# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-identity-provider.md

# firectl get identity-provider

> Prints information about an identity provider.

```
firectl get identity-provider [flags]
```

### Examples

```
firectl get identity-provider my-provider
```

### Flags

```
  -h, --help   help for identity-provider
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
