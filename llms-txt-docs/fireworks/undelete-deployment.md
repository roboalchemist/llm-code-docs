# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/undelete-deployment.md

# Source: https://docs.fireworks.ai/api-reference/undelete-deployment.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/undelete-deployment.md

# firectl undelete deployment

> Undeletes a deployment.

```
firectl undelete deployment [flags]
```

### Examples

```
firectl undelete deployment my-deployment
```

### Flags

```
  -h, --help                    help for deployment
      --wait                    Wait until the deployment is undeleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 1h0m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
