# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/dpo-job-cancel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# firectl dpo-job cancel

> Cancels a running dpo job.

```
firectl dpo-job cancel [flags]
```

### Examples

```
firectl dpo-job cancel my-dpo-job
firectl dpo-job cancel accounts/my-account/dpoJobs/my-dpo-job
```

### Flags

```
  -h, --help                    help for cancel
      --wait                    Wait until the dpo job is cancelled.
      --wait-timeout duration   Maximum time to wait when using --wait flag. (default 10m0s)
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
