# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/update-deployed-model.md

# firectl update deployed-model

> Update a deployed model.

```
firectl update deployed-model [flags]
```

### Examples

```
firectl update deployed-model my-deployed-model
firectl update deployed-model accounts/my-account/deployed-models/my-deployed-model
```

### Flags

```
      --default #<deployment>   If true, this is the default deployment when querying this model without the #<deployment> suffix.
      --description string      Description of the deployed model. Must be fewer than 1000 characters long.
      --display-name string     Human-readable name of the deployed model. Must be fewer than 64 characters long.
  -h, --help                    help for deployed-model
      --public                  If true, the deployed model will be publicly reachable.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --dry-run             Print the request proto without running it.
  -o, --output Output       Set the output format to "text", "json", or "flag". (default text)
  -p, --profile string      fireworks auth and settings profile to use.
```
