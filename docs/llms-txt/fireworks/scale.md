# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/scale.md

# firectl scale

> Scales a deployment to a specified number of replicas.

```
firectl scale [flags]
```

### Examples

```
firectl scale my-deployment --replica-count=3
firectl scale accounts/my-account/deployments/my-deployment --replica-count=3
```

### Flags

```
  -h, --help                  help for scale
      --replica-count int32   The desired number of replicas. Must be non-negative.
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
