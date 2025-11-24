# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/download-billing-metrics.md

# firectl download billing-metrics

> Exports billing metrics

```
firectl download billing-metrics [flags]
```

### Examples

```
firectl export billing-metrics
```

### Flags

```
      --end-time string     The end time (exclusive).
      --filename string     The file name to export to. (default "billing_metrics.csv")
  -h, --help                help for billing-metrics
      --start-time string   The start time (inclusive).
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
  -p, --profile string      fireworks auth and settings profile to use.
```
