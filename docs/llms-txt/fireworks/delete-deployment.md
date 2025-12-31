# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-deployment.md

# Source: https://docs.fireworks.ai/api-reference/delete-deployment.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-deployment.md

# Source: https://docs.fireworks.ai/api-reference/delete-deployment.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-deployment.md

# Source: https://docs.fireworks.ai/api-reference/delete-deployment.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-deployment.md

# Source: https://docs.fireworks.ai/api-reference/delete-deployment.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-deployment.md

# firectl delete deployment

> Deletes a deployment.

```
firectl delete deployment [flags]
```

### Examples

```
firectl delete deployment my-deployment
firectl delete deployment accounts/my-account/deployments/my-deployment
```

### Flags

```
      --hard                    Hard delete the deployment
  -h, --help                    help for deployment
      --ignore-checks           Skip checking if the deployment is in use before deleting
      --wait                    Wait until the deployment is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 1h0m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
