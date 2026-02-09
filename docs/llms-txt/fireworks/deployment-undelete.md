# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-undelete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# firectl deployment undelete

> Undeletes a deployment.

```
firectl deployment undelete [flags]
```

### Examples

```
firectl deployment undelete my-deployment
```

### Flags

```
  -h, --help                    help for undelete
      --wait                    Wait until the deployment is undeleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 1h0m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
