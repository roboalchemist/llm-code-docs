# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/list-credit-redemptions.md

# firectl list credit-redemptions

> Lists credit code redemptions for the current account.

```
firectl list credit-redemptions [flags]
```

### Examples

```
firectl list credit-redemptions
```

### Flags

```
  -h, --help   help for credit-redemptions
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


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireworks.ai/llms.txt