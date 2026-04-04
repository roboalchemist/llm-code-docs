# Source: https://www.aptible.com/docs/how-to-guides/app-guides/generate-certificate-signing-requests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to generate certificate signing requests

> 📘 If you're unsure about creating certificates or don't want to manage them, use Aptible's [Managed TLS](/core-concepts/apps/connecting-to-apps/app-endpoints/managed-tls) option!

A [Certificate Signing Request](https://en.wikipedia.org/wiki/Certificate_signing_request) (CSR) file contains information about an SSL / TLS certificate you'd like a Certification Authority (CA) to issue. If you'd like to use a [Custom Certificate](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-certificate) with your [Endpoints](/core-concepts/apps/connecting-to-apps/app-endpoints/overview), you will need to generate a CSR:

**Step 1:** You can generate a new CSR using OpenSSL's `openssl req` command:

```bash  theme={null}
openssl req -newkey rsa:2048 -nodes \
        -keyout "$DOMAIN.key" -out "$DOMAIN.csr"
```

**Step 2:** Store the private key (the `$DOMAIN.key` file) and CSR (the `$DOMAIN.csr` file) in a secure location, then request a certificate from the CA of your choice.

**Step 3:** Once your CSR is approved, request an "NGiNX / other" format if the CA asks what certificate format you prefer.

## Matching Certificates, Private Keys and CSRs

If you are unsure which certificates, private keys, and CSRs match each other, you can compare the hashes of the modulus of each:

```bash  theme={null}
openssl x509 -noout -modulus -in certificate.crt | openssl md5
openssl rsa -noout -modulus -in "$DOMAIN.key" | openssl md5
openssl req -noout -modulus -in "$DOMAIN.csr" | openssl md5
```

The certificate, private key and CSR are compatible if all three hashes match. You can use `diff3` to compare the moduli from all three files at once:

```bash  theme={null}
openssl x509 -noout -modulus -in certificate.crt > certificate-mod.txt
openssl rsa -noout -modulus -in "$DOMAIN.key" > private-key-mod.txt
openssl req -noout -modulus -in "$DOMAIN.csr" > csr-mod.txt
diff3 cert-mod.txt privkey-mod.txt csr-mod.txt
```

If all three files are identical, `diff3` will produce no output.

> 📘 You can reuse a private key and CSR when renewing an SSL / TLS certificate, but from a security perspective, it's often a better idea to generate a new key and CSR when renewing.
