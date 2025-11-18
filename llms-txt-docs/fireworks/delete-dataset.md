# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-dataset.md

# firectl delete dataset

> Deletes a dataset.

```
firectl delete dataset [flags]
```

### Examples

```
firectl delete dataset my-dataset
firectl delete dataset accounts/my-account/datasets/my-dataset
```

### Flags

```
  -h, --help                    help for dataset
      --wait                    Wait until the dataset is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
