# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/reinforcement-fine-tuning-job-resume.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# firectl reinforcement-fine-tuning-job resume

> Resumes a failed reinforcement fine-tuning job.

```
firectl reinforcement-fine-tuning-job resume [flags]
```

### Examples

```
firectl reinforcement-fine-tuning-job resume my-rftj
firectl reinforcement-fine-tuning-job resume accounts/my-account/reinforcementFineTuningJobs/my-rftj
```

### Flags

```
  -h, --help   help for resume
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
