# Source: https://kreya.app/docs/ssl-tls.md

# SSL / TLS / mTLS

Configure TLS and mTLS related settings in Kreya.

## TLS client certificates (mTLS)[​](#tls-client-certificates-mtls "Direct link to TLS client certificates (mTLS)")

TLS client certificates can be configured using the certificates settings. You can find them in the application menu via `Project > Certificates`.

![Editing a TLS client certificate in the certificates settings](/assets/ideal-img/certificates.c9720f4.400.png)

Currently, two types of certificates are supported:

* Single file certificates, which contain both the private key and the certificate. Supports both binary (DER) and Base64 encoding.
* Certificates consisting of a private key and a certificate file. Supports valid RFC 7468 PEM-encoded files.

Kreya only stores the path to these files. If you intend to share your Kreya project, make sure that the paths stay correct. Kreya uses relative paths by default, but you may also use system environment variables like `%APPDATA%` or `${GOPATH}`. They will work on any OS, regardless of the format.

We recommend that you only use certificates secured by a password, especially if you share your Kreya project. To keep the password from being synced in plain text, use [templating](/docs/templating.md) in combination with [user specific environment data](/docs/environments.md) to make sure that the password never leaves your computer.

As a final step, select the certificate in the "Auth" tab of the operation.

![Selecting a certificate in the Auth tab of the operation](/assets/ideal-img/select-certificate.1f069ac.400.png)

## Disable SSL/TLS server certificate validation[​](#disable-ssltls-server-certificate-validation "Direct link to Disable SSL/TLS server certificate validation")

Sometimes, for example when calling a local API, you find yourself working with invalid TLS server certificates. Kreya allows you to disable the server certificate validation, in which case it simply accepts all server certificates as valid.

![Settings tab is selected, where you can disable the server certificate validation](/assets/ideal-img/disable-server-certificate-validation.bd78f17.400.png)

Head over to the [default settings section](/docs/default-settings.md) if you want to disable the server certificate validation only for specific environments.
