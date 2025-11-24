# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-database-modify.md

# aptible endpoints:database:modify

This command modifies an existing [Database Endpoint.](/core-concepts/managed-databases/connecting-databases/database-endpoints)

# Synopsis

```
Usage:
  aptible endpoints:database:modify --database DATABASE ENDPOINT_HOSTNAME

Options:
  --env, [--environment=ENVIRONMENT]
  [--database=DATABASE]
  [--ip-whitelist=one two three]  # A list of IPv4 sources (addresses or CIDRs) to which to restrict traffic to this Endpoint
  [--no-ip-whitelist]             # Disable IP Whitelist
```
