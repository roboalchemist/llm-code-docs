# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-grpc-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible endpoints:grpc:create

This command creates a new [gRPC Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/grpc-endpoints).

# Synopsis

```
Usage:
  aptible endpoints:grpc:create [--app APP] SERVICE

Options:
  --env, [--environment=ENVIRONMENT]
      [--app=APP]
  -r, [--remote=REMOTE]
      [--default-domain], [--no-default-domain]            # Enable Default Domain on this Endpoint
      [--port=N]                                           # A port to expose on this Endpoint   
      [--internal], [--no-internal]                        # Restrict this Endpoint to internal traffic
      [--ip-whitelist=one two three]                       # A list of IPv4 sources (addresses or CIDRs) to which to restrict traffic to this Endpoint
      [--certificate-file=CERTIFICATE_FILE]                # A file containing a certificate to use on this Endpoint
      [--private-key-file=PRIVATE_KEY_FILE]                # A file containing a private key to use on this Endpoint
      [--managed-tls], [--no-managed-tls]                  # Enable Managed TLS on this Endpoint
      [--managed-tls-domain=MANAGED_TLS_DOMAIN]            # A domain to use for Managed TLS
      [--certificate-fingerprint=CERTIFICATE_FINGERPRINT]  # The fingerprint of an existing Certificate to use on this Endpoint
```

# Examples

In all the examples below, `$SERVICE` represents the name of a [Service](/core-concepts/apps/deploying-apps/services) for the app you add an Endpoint to.

> 📘 If your app is using an [Implicit Service](/how-to-guides/app-guides/define-services#implicit-service-cmd), the service name is always `cmd`.

#### Create a new Endpoint using custom Container Ports and an existing [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate)

In the example below, `$CERTIFICATE_FINGERPRINT` is the SHA-256 fingerprint of a [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate) that exist in the same [Environment](/core-concepts/architecture/environments) as the App you are adding an Endpoint for.

> 📘 Tip: Use the Dashboard to easily locate the Certificate Fingerprint for a given Certificate.

> ❗️ Warning: Everything after the `--ports` argument is assumed to be part of the list of ports, so you need to pass it last.

```shell  theme={null}
aptible endpoints:grpc:create \
        "$SERVICE" \
        --app "$APP_HANDLE" \
        --certificate-fingerprint "$CERTIFICATE_FINGERPRINT" \
        --ports 8000 8001 8002 8003
```

#### More Examples

This command is fairly similar in usage to [`aptible endpoints:https:create`](/reference/aptible-cli/cli-commands/cli-endpoints-https-create). Review the examples there.
