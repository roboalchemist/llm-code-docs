# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-reinforcement-fine-tuning-job.md

# Source: https://docs.fireworks.ai/api-reference/delete-reinforcement-fine-tuning-job.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-reinforcement-fine-tuning-job.md

# Source: https://docs.fireworks.ai/api-reference/delete-reinforcement-fine-tuning-job.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-reinforcement-fine-tuning-job.md

# firectl delete reinforcement-fine-tuning-job

> Deletes a reinforcement fine-tuning job.

```
firectl delete reinforcement-fine-tuning-job [flags]
```

### Examples

```
firectl delete reinforcement-fine-tuning-job my-rftj
firectl delete reinforcement-fine-tuning-job accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

### Flags

```
  -h, --help                    help for reinforcement-fine-tuning-job
      --wait                    Wait until the reinforcement fine-tuning job is deleted.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 30m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
