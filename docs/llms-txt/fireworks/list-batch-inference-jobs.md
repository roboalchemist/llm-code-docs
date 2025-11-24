# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-batch-inference-jobs.md

# Source: https://docs.fireworks.ai/api-reference/list-batch-inference-jobs.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-batch-inference-jobs.md

# firectl list batch-inference-jobs

> Lists all batch inference jobs in an account.

```
firectl list batch-inference-jobs [flags]
```

### Examples

```
firectl list batch-inference-jobs
```

### Flags

```
  -h, --help   help for batch-inference-jobs
```

### Global flags

```
  -a, --account-id string   The Fireworks account ID. If not specified, reads account_id from ~/.fireworks/auth.ini.
      --api-key string      An API key used to authenticate with Fireworks.
      --filter string       Only resources satisfying the provided filter will be listed. See https://google.aip.dev/160 for the filter grammar.
      --no-paginate         List all resources without pagination.
      --order-by string     A list of fields to order by. To specify a descending order for a field, append a " desc" suffix
      --page-size int32     The maximum number of resources to list.
      --page-token string   The page to list. A number from 0 to the total number of pages (number of entities / page size).
  -p, --profile string      fireworks auth and settings profile to use.
```
