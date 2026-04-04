# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/user-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# firectl user create

> Creates a new user.

```
firectl user create [flags]
```

### Examples

```
firectl user create --email="alice.cullen@gmail.com"
firectl user create --service-account --user-id="my-bot"
```

### Flags

```
      --display-name string   The display name of the user.
      --dry-run               Print the request proto without running it.
      --email string          The email address of the user (not required for service accounts).
  -h, --help                  help for create
  -o, --output Output         Set the output format to "text", "json", or "flag". (default text)
      --role string           The user's role, must be one of "user", "admin", "contributor", or "inference-user". (default "user")
      --service-account       Admin only: Create as a service account (email will be auto-generated)
      --user-id string        The ID of the user (required for service accounts).
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
