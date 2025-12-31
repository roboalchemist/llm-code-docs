# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/cancel-supervised-fine-tuning-job.md

# firectl cancel supervised-fine-tuning-job

> Cancels a running supervised fine-tuning job.

```
firectl cancel supervised-fine-tuning-job [flags]
```

### Examples

```
firectl cancel supervised-fine-tuning-job my-sft-job
firectl cancel supervised-fine-tuning-job accounts/my-account/supervisedFineTuningJobs/my-sft-job
```

### Flags

```
  -h, --help   help for supervised-fine-tuning-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireworks.ai/llms.txt