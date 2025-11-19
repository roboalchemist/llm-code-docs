# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-endpoints-https-create.md

# aptible endpoints:https:create

This command created a new [HTTPS Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/overview).

# Synopsis

```
Usage:
  aptible endpoints:https:create [--app APP] SERVICE

Options:
  --env, [--environment=ENVIRONMENT]
      [--app=APP]
  -r, [--remote=REMOTE]
      [--default-domain], [--no-default-domain]                        # Enable Default Domain on this Endpoint
      [--port=N]                                                       # A port to expose on this Endpoint
      [--load-balancing-algorithm-type=LOAD_BALANCING_ALGORITHM_TYPE]  # The load balancing algorithm for this Endpoint. Valid options are round_robin, least_outstanding_requests, and weighted_random
      [--internal], [--no-internal]                                    # Restrict this Endpoint to internal traffic
      [--ip-whitelist=one two three]                                   # A list of IPv4 sources (addresses or CIDRs) to which to restrict traffic to this Endpoint
      [--certificate-file=CERTIFICATE_FILE]                            # A file containing a certificate to use on this Endpoint
      [--private-key-file=PRIVATE_KEY_FILE]                            # A file containing a private key to use on this Endpoint
      [--managed-tls], [--no-managed-tls]                              # Enable Managed TLS on this Endpoint
      [--managed-tls-domain=MANAGED_TLS_DOMAIN]                        # A domain to use for Managed TLS
      [--certificate-fingerprint=CERTIFICATE_FINGERPRINT]              # The fingerprint of an existing Certificate to use on this Endpoint
      [--shared], [--no-shared]                                        # Share this Endpoint's load balancer with other Endpoints
```

# Examples

In all the examples below, `$SERVICE` represents the name of a [Service](/core-concepts/apps/deploying-apps/services) for the app you are adding an Endpoint to.

> 📘 If your app is using an [Implicit Service](/how-to-guides/app-guides/define-services#implicit-service-cmd), the service name is always `cmd`.

#### Create a new Endpoint using a new [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate)

In the example below, `$CERTIFICATE_FILE` is the path to a file containing a PEM-formatted certificate bundle, and `$PRIVATE_KEY_FILE` is the path to a file containing the matching private key (see [Format](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate#format) for more information).

```shell  theme={null}
aptible endpoints:https:create \
        --app "$APP_HANDLE" \
        --certificate-file "$CERTIFICATE_FILE" \
        --private-key-file "$PRIVATE_KEY_FILE" \
        "$SERVICE"
```

#### Create a new Endpoint using an existing [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate)

In the example below, `$CERTIFICATE_FINGERPRINT` is the SHA-256 fingerprint of a [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate) that exist in the same [Environment](/core-concepts/architecture/environments) as the App you are adding an Endpoint for.

> 📘 Tip: Use the Dashboard to easily locate the Certificate Fingerprint for a given Certificate.

```shell  theme={null}
aptible endpoints:https:create \
        --app "$APP_HANDLE" \
        --certificate-fingerprint "$CERTIFICATE_FINGERPRINT" \
        "$SERVICE"
```

#### Create a new Endpoint using [Managed TLS](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls)

In the example below, `$YOUR_DOMAIN` is the domain you intend to use with your Endpoint.

After initial provisioning completes, the CLI will return the [Managed HTTPS Validation Records](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls#managed-https-validation-records) you need to create in order to finalize the Endpoint.

Once you've created these records, use the [`aptible endpoints:renew`](/reference/aptible-cli/cli-commands/cli-endpoints-renew) to complete provisioning.

```shell  theme={null}
aptible endpoints:https:create \
        --app "$APP_HANDLE" \
        --managed-tls \
        --managed-tls-domain "$YOUR_DOMAIN"
        "$SERVICE"
```

#### Create a new Endpoint using a [Default Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/default-domain)

```shell  theme={null}
aptible endpoints:https:create \
        --app "$APP_HANDLE" \
        --default-domain \
        "$SERVICE"
```

#### Create a new Endpoint using a custom Container Port and an existing Certificate

```shell  theme={null}
aptible endpoints:https:create \
        --app "$APP_HANDLE" \
        --certificate-fingerprint "$CERTIFICATE_FINGERPRINT" \
        --port 80 \
        "$SERVICE"
```
