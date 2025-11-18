# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-user.md

# firectl update user

> Updates a user.

```
firectl update user [flags]
```

### Examples

```
firectl update user my-user --display-name="Alice Cullen"
firectl update user accounts/my-account/users/my-user --display-name="Alice Cullen"
```

### Flags

```
      --display-name string   The display name of the user.
  -h, --help                  help for user
      --role string           The role of the user. Must be one of {user, admin}.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
