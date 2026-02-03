# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/billing-export-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# firectl billing export-metrics

> Exports billing metrics

```
firectl billing export-metrics [flags]
```

### Examples

```
firectl billing export-metrics
```

### Flags

```
      --end-time string     The end time (exclusive).
      --filename string     The file name to export to. (default "billing_metrics.csv")
  -h, --help                help for export-metrics
      --start-time string   The start time (inclusive).
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
