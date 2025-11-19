# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-database-create.md

# aptible endpoints:database:create

This command creates a [Database Endpoint.](/core-concepts/managed-databases/connecting-databases/database-endpoints)

# Synopsis

```
Usage:
  aptible endpoints:database:create DATABASE

Options:
  --env, [--environment=ENVIRONMENT]
  [--internal], [--no-internal]   # Restrict this Endpoint to internal traffic
  [--ip-whitelist=one two three]  # A list of IPv4 sources (addresses or CIDRs) to which to restrict traffic to this Endpoint
```

# Examples

#### Create a new Database Endpoint

```shell  theme={null}
aptible endpoints:database:create  "$DATABASE_HANDLE"
```

#### Create a new Database Endpoint with IP Filtering

```shell  theme={null}
aptible endpoints:database:create  "$DATABASE_HANDLE" \
        --ip-whitelist 1.1.1.1/1 2.2.2.2
```
