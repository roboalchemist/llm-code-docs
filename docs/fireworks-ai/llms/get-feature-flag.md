# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-feature-flag.md

# firectl get feature-flag

> Gets a feature flag.

```
firectl get feature-flag [flags]
```

### Examples

```
firectl get feature-flag my-account my-feature-flag
```

### Flags

```
  -h, --help   help for feature-flag
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
