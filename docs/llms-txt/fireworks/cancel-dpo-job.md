# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/cancel-dpo-job.md

# firectl cancel dpo-job

> Cancels a running dpo job.

```
firectl cancel dpo-job [flags]
```

### Examples

```
firectl cancel dpo-job my-dpo-job
firectl cancel dpo-job accounts/my-account/dpo-jobs/my-dpo-job
```

### Flags

```
  -h, --help                    help for dpo-job
      --wait                    Wait until the dpo job is cancelled.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 10m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireworks.ai/llms.txt