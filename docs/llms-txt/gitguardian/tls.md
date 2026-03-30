# Source: https://docs.gitguardian.com/self-hosting/installation/databases/tls.md

# Configure TLS

> Configure TLS encryption for PostgreSQL and Redis database connections in GitGuardian self-hosted.

## KOTS-based installation

### PostgreSQL

To configure TLS for an external PostgreSQL, you have the following
configuration options:

- PostgreSQL TLS mode: PostgreSQL server supports the following TLS mode:
  - Allow: first try an SSL connection; if that fails, try a non-SSL connection.
  - Require: only try an SSL connection. If a root Certificate Authority file is
    present, verify the certificate in the same way as if Verify Certificate
    Authority was specified.
  - Verify Certificate Authority: only try an SSL connection, and verify that
    the server certificate is issued by a trusted certificate authority (CA).
  - Verify Certificate Authority and Hostname: only try an SSL connection, and
    verify that the server certificate is issued by a trusted CA and that the
    requested server hostname matches that in the certificate.
- Custom certificate authority: custom certificate authority to use to
  authenticate PostgreSQL server identity.
- Client authentication required: PostgreSQL server configured to authenticate a
  client.
- PostgreSQL client TLS key.
- PostgreSQL client TLS certificate.

To disable TLS configuration, you should first set "Postgres TLS mode" to Allow
in the Admin Console and deploy the configuration. Then you can disable TLS on
the PostgreSQL server. Finally, disable the TLS configuration within the Admin
Console.

### Redis

To configure TLS for Redis, you have the following configuration options:

- Require Redis server authentication: force the application to require the
  Redis server to authenticate with a valid certificate. By checking this
  setting, you can provide a custom certificate authority to validate the Redis
  server certificate.
- Client authentication required: if the Redis server is configured to require
  client authentication, you need to check this box and provide:
  - a TLS key,
  - a TLS certificate.

For scaling recommendations, refer to the
[hardware requirements documentation](/self-hosting/system-requirements).

## Helm-based installation

With Helm-based installations, instead of parameters being set in the console,
they should be put in a YAML file served at installation.
There are 2 methods for handling certificates, but in both cases:

- For PostgreSQL, set `postgresql.tls.mode` to the SSL mode of your choice among
  `disable`, `allow`, `prefer`, `require`, `verify-ca`, and `verify-full`
- For Redis, set `redis.tls.requireServerCert` to true if you wish to require a
  Redis server certificate check.

### Certificates as a secret

This is the preferred method.

- Create a Kubernetes secret containing your custom certificate authority, TLS
  certificate and key.

```shell
kubectl create secret generic gitguardian-(postgresql|redis)-tls-secret \
  --from-file client.crt=/path/to/pg-tls-cert \
  --from-file client.key=/path/to/pg-tls-key \
  --from-file ca.crt=/path/to/ca-cert
```

:::caution
Previously, Postgresql and Redis TLS secrets were referenced directly in `(postgresql|redis).existingSecret` by specifying keys in `(postgresql|redis).existingSecretKeys.tls.(crt|key|caCrt)`, they must be now referenced in `(postgresql|redis).tls.existingSecret` by specifying keys in `(postgresql|redis).tls.existingSecretKeys.(crt|key|caCrt)`.
This change allows the use of TLS dedicated secrets.
:::

- Reference this secret in the YAML file under `(postgresql|redis).tls.existingSecret`
- Specify the keys used in the secret under
  `(postgresql|redis).tls.existingSecretKeys.(crt|key|caCrt)`

The file should look like this extract:

```yaml
postgresql:
  tls:
    # Possible values: disable, allow, prefer, require, verify-ca, verify-full
    mode: require
    existingSecret: gitguardian-postgresql-tls-secret
    existingSecretKeys:
      crt: client.crt
      key: client.key
      caCrt: ca.crt

redis:
  main:
    tls:
      requireServerCert: true
      existingSecret: gitguardian-redis-tls-secret
      existingSecretKeys:
        crt: client.crt
        key: client.key
        caCrt: ca.crt
```

### Certificates inline

Add the certificates inline under `(postgresql|redis).tls.(crt|key|caCrt)`

The file should look like this extract:

```yaml
postgresql:
  tls:
    # Possible values: disable, allow, prefer, require, verify-ca, verify-full
    mode: require
    crt: |
      -----BEGIN CERTIFICATE-----
      My certificate
      -----END CERTIFICATE-----
    key: |
      -----BEGIN RSA PRIVATE KEY-----
      My key
      -----END RSA PRIVATE KEY-----
    caCrt: |
      -----BEGIN CERTIFICATE-----
      My CA certificate
      -----END CERTIFICATE-----

redis:
  main:
    tls:
      requireServerCert: true
      crt: |
        -----BEGIN CERTIFICATE-----
        My certificate
        -----END CERTIFICATE-----
      key: |
        -----BEGIN RSA PRIVATE KEY-----
        My key
        -----END RSA PRIVATE KEY-----
      caCrt: |
        -----BEGIN CERTIFICATE-----
        My CA certificate
        -----END CERTIFICATE-----
```
