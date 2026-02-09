# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# firectl deployment delete

> Deletes a deployment.

```
firectl deployment delete [flags]
```

### Examples

```
firectl deployment delete my-deployment
firectl deployment delete accounts/my-account/deployments/my-deployment
```

### Flags

```
      --dry-run                 Print the request proto without running it.
      --hard                    Hard delete the deployment
  -h, --help                    help for delete
      --ignore-checks           Skip checking if the deployment is in use before deleting
  -o, --output Output           Set the output format to "text", "json", or "flag". (default text)
      --wait                    Wait until the deployment is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 1h0m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
