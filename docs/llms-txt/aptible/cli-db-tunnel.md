# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-db-tunnel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible db:tunnel

This command creates [Database Tunnels](/core-concepts/managed-databases/connecting-databases/database-tunnels). If your [Database](/core-concepts/managed-databases/overview) exposes multiple [Database Credentials](/core-concepts/managed-databases/connecting-databases/database-credentials), you can specify which one you'd like to tunnel to.

## Synopsis

```
Usage:
  aptible db:tunnel HANDLE

Options:
  --env, [--environment=ENVIRONMENT]
  [--port=N]
  [--type=TYPE]
```

# Examples

To tunnel using your Database's default Database Credential:

```shell  theme={null}
aptible db:tunnel "$DB_HANDLE"
```

To tunnel using a specific Database Credential:

```shell  theme={null}
aptible db:tunnel "$DB_HANDLE" --type "$CREDENTIAL_TYPE"
```
