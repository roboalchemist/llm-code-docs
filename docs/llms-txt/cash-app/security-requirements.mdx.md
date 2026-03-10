# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/integrating-with-cash-app-pay/security-requirements.mdx

***

## stoplight-id: c557c8082c8b7

# Security Requirements

## Encryption

* All Cash App Pay data stored must be encrypted at rest.
* All Cash App Pay data must be encrypted during transit.
* All communications to the Cash App Pay API must use HTTPS and TLS 1.2+.
* All communications with the Network API and Management API must provide HMAC signatures in the `X-Signature` header.

## Credentials

* API keys must be rotated automatically every 30 days.
* API keys should be scoped to the least amount of access needed to process requests. For example, if a service only needs the ability to respond to disputes, you don't need to give it permission to register new merchants.

## Refreshing QR Codes

For security reasons, the QR codes expire periodically. If this happens, a new code will be generated automatically. This is called a **Refresh**.

![QR-code-refresh.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/QR-code-refresh.png)

![QR-code.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/QR-code.png)
