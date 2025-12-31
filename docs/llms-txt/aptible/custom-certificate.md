# Source: https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate.md

# Custom Certificate

When an [Endpoint](/core-concepts/apps/connecting-to-apps/app-endpoints/overview) requires a Certificate to perform SSL / TLS termination on your behalf, you can opt to provide your own certificate and private key instead of Aptible managing them via [Managed TLS](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls). Start by generating a [Certificate Signing Request](https://en.wikipedia.org/wiki/Certificate_signing_request)(CSR) using [these steps](/how-to-guides/app-guides/generate-certificate-signing-requests). With the certificate and private key in hand:

* Select the appropriate App
* Navigate to Endpoints
* Add an endpoint
* Under **Endpoint Type**, select the *Use a custom domain with a custom certificate* option.
* Under **Certificate**, add a new certificate
* Add the certificate and private key to the respective sections
* Save Endpoint

> 📘 Aptible doesn't *require* that you use a valid certificate. If you want, you're free to use a self-signed certificate, but of course, your clients will receive errors when they connect.

# Format

The certificate should be a PEM-formatted certificate bundle, which means you should concatenate your certificate file along with the intermediate CA certificate files provided by your CA.

As for the private key, it should be unencrypted and PEM-formatted as well.

> ❗️ Don't forget to include intermediate certificates! Otherwise, your customers may receive a certificate error when they attempt to connect. However, you don't need to worry about the ordering of certificates in your bundle: Aptible will sort it properly for you.

# Hostname

When you use a Custom Certificate, it's your responsibility to ensure the [Custom Domain](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain) you use and your certificate match.

If they don't, your users will see certificate errors.

# Supported Keys

Aptible supports the following types of keys for Custom Certificates:

* RSA 1024
* RSA 2048
* RSA 4096
* ECDSA prime256v1
* ECDSA secp384r1
* ECDSA secp521r1
