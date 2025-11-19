# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-tcp-create.md

# aptible endpoints:tcp:create

This command creates a new App [TCP Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/tcp-endpoints).

# Synopsis

```
Usage:
  aptible endpoints:tcp:create [--app APP] SERVICE

Options:
  --env, [--environment=ENVIRONMENT]
      [--app=APP]
  -r, [--remote=REMOTE]
      [--default-domain], [--no-default-domain]  # Enable Default Domain on this Endpoint
      [--ports=one two three]                    # A list of ports to expose on this Endpoint
      [--internal], [--no-internal]              # Restrict this Endpoint to internal traffic
      [--ip-whitelist=one two three]             # A list of IPv4 sources (addresses or CIDRs) to which to restrict traffic to this Endpoint
```

# Examples

In all the examples below, `$SERVICE` represents the name of a [Service](/core-concepts/apps/deploying-apps/services) for the Spp you are adding an Endpoint to.

> 📘 If your app is using an [Implicit Service](/how-to-guides/app-guides/define-services#implicit-service-cmd), the service name is always `cmd`.

#### Create a new Endpoint

```shell  theme={null}
aptible endpoints:tcp:create \
        --app "$APP_HANDLE" \
        "$SERVICE"
```

#### Create a new Endpoint using a [Default Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/default-domain)

```shell  theme={null}
aptible endpoints:tcp:create \
        --app "$APP_HANDLE" \
        --default-domain \
        "$SERVICE"
```

#### Create a new Endpoint using a custom set of Container Ports

> ❗️ Warning

> The `--ports` argument accepts a list of ports, so you need to pass it last.

```shell  theme={null}
aptible endpoints:tcp:create \
        --app "$APP_HANDLE" \
        "$SERVICE" \
        --ports 8000 8001 8002 8003
```
