# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-user.md

# Source: https://docs.fireworks.ai/api-reference/create-user.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-user.md

# Source: https://docs.fireworks.ai/api-reference/create-user.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/create-user.md

# firectl create user

> Creates a new user.

```
firectl create user [flags]
```

### Examples

```
firectl create user --email="alice.cullen@gmail.com"
firectl create user --service-account --user-id="my-bot"
```

### Flags

```
      --display-name string   The display name of the user.
      --email string          The email address of the user (not required for service accounts).
  -h, --help                  help for user
      --role string           The user's role, must be one of "user" or "admin" (default "user")
      --service-account       Admin only: Create as a service account (email will be auto-generated)
      --user-id string        The ID of the user (required for service accounts).
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
