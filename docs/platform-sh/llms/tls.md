# Source: https://docs.upsun.com/domains/steps/tls.md

# Configure a third-party TLS certificate

Upsun automatically provides standard Transport Layer Security (TLS) certificates for all sites and environments.
These certificates are issued at no charge by [Let's Encrypt](https://letsencrypt.org/) and cover most needs.
To use them, you need to [specify HTTPS routes](https://docs.upsun.com../../define-routes/https.md#enable-https). 
Note that some [limitations](https://docs.upsun.com../../define-routes/https.md#lets-encrypt-limitations) apply.

Upsun allows you to use third-party TLS certificates free of charge.

You can use many kinds of custom certificates, including domain-validated, extended validation, high-assurance, or wildcard certificates.
Consult your TLS issuer for pricing and instructions on how to generate a TLS certificate.

Seven days before a third-party custom certificate is due to expire,
Upsun replaces it with a new default Let’s Encrypt certificate.
This helps prevent downtime.
To avoid switching to a default certificate,
make sure you replace your custom certificate with an updated one
more than seven days before its expiration date.

Note that custom certificates aren't necessary for preview environments as we provision Let's Encrypt certificates by default for them.

### Add a custom certificate

You can add a custom certificate using the [CLI](https://docs.upsun.com../../administration/cli.md) or in the [Console](https://docs.upsun.com../../administration/web.md).

Your certificate has to be in PKCS #1 format and start with `-----BEGIN RSA PRIVATE KEY-----`.
If it doesn't start that way, [change the format](#change-the-private-key-format).

To add your custom certificate, follow these steps:

For example:

```bash {}
upsun domain:add secure.example.com --cert /etc/TLS/private/secure-example-com.crt --key /etc/TLS/private/secure-example-com.key
```

You can optionally include intermediate SSL certificates by adding ``‐‐chain <PATH_TO_FILE>`` for each one.

 - Redeploy your production environment with the following command:

```bash {}
upsun environment:redeploy
```

 - Open the project where you want to add a certificate.
 - Click Settings **Settings**.
 - Click **Certificates**.
 - Click **+ Add**.
 - Fill in your private key, public key certificate, and (optionally) intermediate SSL certificates.
 - Click **Add Certificate**.
 - Access your production environment.
 - Click More **More**.
 - Click **Redeploy**.

### Change the private key format

The expected format for your certificate’s private key is PKCS #1.
Private keys in PKCS #1 format start with `-----BEGIN RSA PRIVATE KEY-----`.
If your private key starts with `-----BEGIN PRIVATE KEY-----`, it’s in PKCS #8 format, which isn’t appropriate.

To convert your private key (`private.key`) from PKCS #8 to PKCS #1 format (`private.rsa.key`), run the following command:

```bash
openTLS rsa -in private.key -out private.rsa.key
```

