# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible endpoints:list

This command lists the Endpoints for an [App](/core-concepts/apps/overview) or [Database](/core-concepts/managed-databases/overview).

# Synopsis

```
Usage:
  aptible endpoints:list [--app APP | --database DATABASE]

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
      [--database=DATABASE]
```

# Examples

#### List Endpoints for an App

```shell  theme={null}
aptible endpoints:list \
        --app "$APP_HANDLE"
```

#### List Endpoints for a Database

```shell  theme={null}
aptible endpoints:list \
        --database "$DATABASE_HANDLE"
```

#### Sample Output

```
Service: cmd
Hostname: elb-foobar-123.aptible.in
Status: provisioned
Type: https
Port: default
Load Balancing Algorithm Type: round_robin
Shared: false
Internal: false
IP Whitelist: all traffic
Default Domain Enabled: false
Managed TLS Enabled: true
Managed TLS Domain: app.example.com
Managed TLS DNS Challenge Hostname: acme.elb-foobar-123.aptible.in
Managed TLS Status: ready
```

> 📘 The above block is repeated for each matching Endpoint.
