# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-account.md

# firectl get account

> Prints information about an account.

```
firectl get account [flags]
```

### Examples

```
firectl get account
firectl get account my-account
firectl get account accounts/my-account
```

### Flags

```
  -h, --help   help for account
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
