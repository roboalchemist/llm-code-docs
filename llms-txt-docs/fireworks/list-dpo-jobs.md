# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-dpo-jobs.md

# firectl list dpo-jobs

> Lists all dpo jobs in an account.

```
firectl list dpo-jobs [flags]
```

### Examples

```
firectl list dpo-jobs
```

### Flags

```
  -h, --help   help for dpo-jobs
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
