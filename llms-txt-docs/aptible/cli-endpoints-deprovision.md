# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-deprovision.md

# aptible endpoints:deprovision

This command deprovisions an [App Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) or a [Database Endpoint](/core-concepts/managed-databases/connecting-databases/database-endpoints).

# Synopsis

```
Usage:
  aptible endpoints:deprovision [--app APP | --database DATABASE] ENDPOINT_HOSTNAME

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
      [--database=DATABASE]
```

# Examples

The examples below `$ENDPOINT_HOSTNAME` reference the [Endpoint Hostname](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain#endpoint-hostname) for the Endpoint you'd like to deprovision.

> 📘 Use the [`aptible endpoints:list`](/reference/aptible-cli/cli-commands/cli-endpoints-list) command to easily locate the [Endpoint Hostname](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain#endpoint-hostname) for a given Endpoint.

#### Deprovision an App Endpoint

```shell  theme={null}
aptible endpoints:deprovision \
        --app "$APP_HANDLE" \
        "$ENDPOINT_HOSTNAME"
```

#### Deprovision a Database Endpoint

```shell  theme={null}
aptible endpoints:deprovision \
        --database "$DATABASE_HANDLE" \
        "$ENDPOINT_HOSTNAME"
```
