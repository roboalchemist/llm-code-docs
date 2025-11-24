# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-supervised-fine-tuning-job.md

# Source: https://docs.fireworks.ai/api-reference/delete-supervised-fine-tuning-job.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-supervised-fine-tuning-job.md

# firectl delete supervised-fine-tuning-job

> Deletes a supervised fine-tuning job.

```
firectl delete supervised-fine-tuning-job [flags]
```

### Examples

```
firectl delete supervised-fine-tuning-job my-sft-job
firectl delete supervised-fine-tuning-job accounts/my-account/supervised-fine-tuning-jobs/my-sft-job
```

### Flags

```
  -h, --help                    help for supervised-fine-tuning-job
      --wait                    Wait until the supervised fine-tuning job is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
