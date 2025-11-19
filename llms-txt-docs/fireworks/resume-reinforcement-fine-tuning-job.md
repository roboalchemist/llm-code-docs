# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/resume-reinforcement-fine-tuning-job.md

# Source: https://docs.fireworks.ai/api-reference/resume-reinforcement-fine-tuning-job.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/resume-reinforcement-fine-tuning-job.md

# firectl resume reinforcement-fine-tuning-job

> Resumes a failed reinforcement fine-tuning job.

```
firectl resume reinforcement-fine-tuning-job [flags]
```

### Examples

```
firectl resume reinforcement-fine-tuning-job my-rftj
firectl resume reinforcement-fine-tuning-job accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

### Flags

```
  -h, --help   help for reinforcement-fine-tuning-job
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
