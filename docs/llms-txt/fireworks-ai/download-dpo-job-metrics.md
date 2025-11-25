# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/download-dpo-job-metrics.md

# firectl download dpo-job-metrics

> Retrieves metrics for a dpo job.

```
firectl download dpo-job-metrics [flags]
```

### Examples

```
firectl download dpoj-metrics my-dpo-job
firectl download dpoj-metrics accounts/my-account/dpo-jobs/my-dpo-job
```

### Flags

```
      --filename string   The file name to export to. (default "metrics.jsonl")
  -h, --help              help for dpo-job-metrics
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
