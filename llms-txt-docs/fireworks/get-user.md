# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-user.md

# Source: https://docs.fireworks.ai/api-reference/get-user.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/get-user.md

# firectl get user

> Prints information about a user.

```
firectl get user [flags]
```

### Examples

```
firectl get user my-user
firectl get user accounts/my-account/users/my-user
```

### Flags

```
  -h, --help   help for user
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
