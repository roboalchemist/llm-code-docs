# Source: https://developers.cloudflare.com/ssl/llms.txt

# SSL/TLS

Encrypt your web traffic to prevent data theft and other tampering

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/ssl/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [SSL/TLS llms-full.txt](https://developers.cloudflare.com/ssl/llms-full.txt) for the complete SSL/TLS documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare SSL/TLS](https://developers.cloudflare.com/ssl/index.md): Cloudflare SSL/TLS offers free Universal SSL alongside advanced and enterprise features to meet your encryption and certificate management needs.

## Concepts

- [Concepts](https://developers.cloudflare.com/ssl/concepts/index.md): This page defines and articulates key concepts that are relevant to Cloudflare SSL/TLS and are used in the Cloudflare SSL/TLS documentation.

## Get started

- [Get started](https://developers.cloudflare.com/ssl/get-started/index.md)

## Edge certificates

- [Edge certificates](https://developers.cloudflare.com/ssl/edge-certificates/index.md): Edge certificates are the SSL/TLS certificates that Cloudflare presents to your visitors. Consider how different certificate types align to common use cases.
- [Always Use HTTPS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/always-use-https/index.md)
- [Automatic HTTPS Rewrites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/automatic-https-rewrites/index.md)
- [Certificate Signing Requests (CSRs)](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-signing-requests/index.md)
- [Certificate Transparency Monitoring](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/certificate-transparency-monitoring/index.md): Certificate Transparency (CT) Monitoring is an opt-in feature in public beta that aims at improving security by allowing you to double-check any SSL/TLS certificates issued for your domain.
- [Cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/index.md): Consider information about supported cipher suites, how to meet your security requirements, and how to troubleshoot compatibility and other issues.
- [Compliance standards](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/compliance-status/index.md)
- [Customize cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/index.md)
- [Customize cipher suites via API](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/api/index.md)
- [Customize cipher suites via dashboard](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/customize-cipher-suites/dashboard/index.md)
- [Security levels](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/recommendations/index.md)
- [Supported cipher suites](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/supported-cipher-suites/index.md)
- [Troubleshooting](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/cipher-suites/troubleshooting/index.md)
- [HTTP Strict Transport Security (HSTS)](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/http-strict-transport-security/index.md)
- [Minimum TLS Version](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/minimum-tls/index.md)
- [Opportunistic Encryption](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/opportunistic-encryption/index.md)
- [TLS 1.3](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/tls-13/index.md)
- [Total TLS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/index.md)
- [Enable](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/enable/index.md)
- [Error messages](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/total-tls/error-messages/index.md)
- [Advanced certificates](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/index.md)
- [API commands](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/api-commands/index.md)
- [Manage advanced certificates](https://developers.cloudflare.com/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/index.md): Learn how to create, delete and perform other operations to manage your Cloudflare Advanced SSL certificates.
- [Backup certificates](https://developers.cloudflare.com/ssl/edge-certificates/backup-certificates/index.md)
- [Add CAA records](https://developers.cloudflare.com/ssl/edge-certificates/caa-records/index.md)
- [Domain control validation (DCV)](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/index.md): Learn when and how to perform Domain Control Validation when using Cloudflare SSL/TLS.
- [Domain control validation flow](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/dcv-flow/index.md): Consider the steps that have to take place before the DCV process is completed and certificate authorities can issue SSL/TLS certificates.
- [Methods](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/index.md): Review different methods to perform Domain Control Validation when using Cloudflare SSL/TLS.
- [Delegated](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/delegated-dcv/index.md)
- [HTTP](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/http/index.md)
- [TXT](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/methods/txt/index.md)
- [Troubleshooting](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/troubleshooting/index.md)
- [Validation backoff schedule](https://developers.cloudflare.com/ssl/edge-certificates/changing-dcv-method/validation-backoff-schedule/index.md): Consider what happens if a domain control validation (DCV) fails and what schedule Cloudflare follows for new attempts and backoff.
- [Custom certificates](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/index.md)
- [Bundle methodologies](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/bundling-methodologies/index.md)
- [Remove key file password](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/remove-file-key-password/index.md)
- [Renewal and expiration](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/renewing/index.md): Learn how renewal and expiration work when using Cloudflare Custom SSL certificates.
- [Troubleshooting](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/troubleshooting/index.md): Troubleshoot issues with Client certificates
- [Manage custom certificates](https://developers.cloudflare.com/ssl/edge-certificates/custom-certificates/uploading/index.md)
- [ECH Protocol](https://developers.cloudflare.com/ssl/edge-certificates/ech/index.md)
- [Enforce HTTPS connections](https://developers.cloudflare.com/ssl/edge-certificates/encrypt-visitor-traffic/index.md)
- [Geo Key Manager](https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/index.md)
- [Setup](https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/setup/index.md): Learn how to set up Geo Key Manager and choose the geographical boundaries of where your private encryption keys are stored.
- [Supported options](https://developers.cloudflare.com/ssl/edge-certificates/geokey-manager/supported-options/index.md): Learn which options are supported for Geo Key Manager.
- [Staging environment](https://developers.cloudflare.com/ssl/edge-certificates/staging-environment/index.md)
- [Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/index.md)
- [Alerts](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/alerts/index.md)
- [Disable Universal SSL certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/disable-universal-ssl/index.md)
- [Enable Universal SSL certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/index.md)
- [Limitations](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/limitations/index.md): Review the limitations of Universal certificates, such as hostname coverage, certificate authority  choice, and compatibility with other products.
- [Troubleshooting](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/troubleshooting/index.md): Review how to troubleshoot issues such as certificate timeouts when using Cloudflare Universal SSL.

## Client certificates (mTLS)

- [Client certificates (mTLS)](https://developers.cloudflare.com/ssl/client-certificates/index.md): Use Cloudflare public key infrastructure (PKI) to create client certificates and enforce mutual Transport Layer Security (mTLS) encryption.
- [Bring your own CA for mTLS](https://developers.cloudflare.com/ssl/client-certificates/byo-ca/index.md): Cloudflare mTLS now supports client certificates that have not been issued by Cloudflare CA. Learn how you can bring your own CA and use it with Cloudflare mTLS.
- [Client certificate variables](https://developers.cloudflare.com/ssl/client-certificates/client-certificate-variables/index.md)
- [Configure your mobile app or IoT device](https://developers.cloudflare.com/ssl/client-certificates/configure-your-mobile-app-or-iot-device/index.md): This tutorial demonstrates how to configure your Internet-of-things (IoT) device and mobile application to use client certificates with API Shield.
- [Create a client certificate](https://developers.cloudflare.com/ssl/client-certificates/create-a-client-certificate/index.md)
- [Enable mTLS](https://developers.cloudflare.com/ssl/client-certificates/enable-mtls/index.md)
- [Forward certificate to server](https://developers.cloudflare.com/ssl/client-certificates/forward-a-client-certificate/index.md)
- [Label client certificates](https://developers.cloudflare.com/ssl/client-certificates/label-client-certificate/index.md)
- [Revoke a client certificate](https://developers.cloudflare.com/ssl/client-certificates/revoke-client-certificate/index.md)
- [Troubleshooting](https://developers.cloudflare.com/ssl/client-certificates/troubleshooting/index.md): Troubleshoot issues with client certificates
- [mTLS for Zero Trust](https://developers.cloudflare.com/ssl/client-certificates/zero-trust-mtls/index.md)

## Cloudflare for SaaS

- [Cloudflare for SaaS](https://developers.cloudflare.com/ssl/saas/index.md)

## Keyless SSL

- [Keyless SSL](https://developers.cloudflare.com/ssl/keyless-ssl/index.md)
- [Cloudflare Tunnel](https://developers.cloudflare.com/ssl/keyless-ssl/configuration/cloudflare-tunnel/index.md)
- [Public DNS](https://developers.cloudflare.com/ssl/keyless-ssl/configuration/public-dns/index.md)
- [Glossary](https://developers.cloudflare.com/ssl/keyless-ssl/glossary/index.md): Learn more about the common terms related to Keyless SSL.
- [Hardware security modules](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/index.md)
- [AWS cloud HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/aws-cloud-hsm/index.md): Learn how to use Keyless SSL with AWS CloudHSM.
- [Azure Dedicated HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/azure-dedicated-hsm/index.md): Learn how to use Keyless SSL with Azure Dedicated HSM.
- [Azure Managed HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/azure-managed-hsm/index.md): This tutorial uses Microsoft Azureâs Managed HSM to deploy a VM with the Keyless SSL daemon. Follow these instructions to deploy your keyless server.
- [Configuration](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/configuration/index.md)
- [Entrust nShield Connect](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/entrust-nshield-connect/index.md): Learn how to use Keyless SSL with Entrust nShield Connect.
- [Fortanix Data Security Manager](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/fortanix-dsm/index.md)
- [Google Cloud HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/google-cloud-hsm/index.md): Learn how to use Keyless SSL with Google Cloud HSM.
- [IBM Cloud HSM](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/ibm-cloud-hsm/index.md): Learn how to use Keyless SSL with IBM Cloud HSM.
- [SoftHSMv2](https://developers.cloudflare.com/ssl/keyless-ssl/hardware-security-modules/softhsmv2/index.md): Learn how to use Keyless SSL with SoftHSMv2.
- [High availability](https://developers.cloudflare.com/ssl/keyless-ssl/reference/high-availability/index.md)
- [Keyless delegation](https://developers.cloudflare.com/ssl/keyless-ssl/reference/keyless-delegation/index.md)
- [Scaling and benchmarking](https://developers.cloudflare.com/ssl/keyless-ssl/reference/scaling-and-benchmarking/index.md)
- [Troubleshooting](https://developers.cloudflare.com/ssl/keyless-ssl/troubleshooting/index.md): Review how to troubleshoot issues when using Cloudflare Keyless SSL.
- [Upgrade your key server](https://developers.cloudflare.com/ssl/keyless-ssl/upgrading-your-key-server/index.md)

## Post-quantum cryptography (PQC)

- [Post-quantum cryptography (PQC)](https://developers.cloudflare.com/ssl/post-quantum-cryptography/index.md): Get an overview of how Cloudflare is deploying post-quantum cryptography to protect you against harvest now, decrypt later.
- [Post-quantum cryptography in Cloudflare One](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-and-zero-trust/index.md)
- [PQC support](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-support/index.md): Consider information about post-quantum cryptography at Cloudflare - deployed key agreements and software support.
- [Post-quantum between Cloudflare and origin servers](https://developers.cloudflare.com/ssl/post-quantum-cryptography/pqc-to-origin/index.md): Learn about post-quantum cryptography in connections from Cloudflare to your origin servers.

## Troubleshooting

- [Troubleshooting](https://developers.cloudflare.com/ssl/troubleshooting/index.md)
- [General SSL errors](https://developers.cloudflare.com/ssl/troubleshooting/general-ssl-errors/index.md): Learn how to troubleshoot various SSL/TLS errors with Cloudflare.
- [Mixed content errors](https://developers.cloudflare.com/ssl/troubleshooting/mixed-content-errors/index.md)
- [ERR_TOO_MANY_REDIRECTS](https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/index.md): Learn how to troubleshoot ERR_TOO_MANY_REDIRECTS when using Cloudflare SSL/TLS.
- [ERR_SSL_VERSION_OR_CIPHER_MISMATCH](https://developers.cloudflare.com/ssl/troubleshooting/version-cipher-mismatch/index.md): Learn how to troubleshoot ERR_SSL_VERSION_OR_CIPHER_MISMATCH when using Cloudflare SSL/TLS.

## SSL/TLS FAQ

- [SSL/TLS FAQ](https://developers.cloudflare.com/ssl/faq/index.md): Get answers to commonly asked questions about the certificates you can obtain through Cloudflare and the CAs that Cloudflare partners with.

## Changelog

- [Changelog](https://developers.cloudflare.com/ssl/changelog/index.md)

## origin-configuration

- [Authenticated Origin Pulls (mTLS)](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/index.md): Authenticated Origin Pulls helps ensure requests to your origin server come from the Cloudflare network.
- [AWS integration](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/index.md): Learn how to set up Cloudflare Authenticated Origin Pulls with the AWS Application Load Balancer.
- [About](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/index.md)
- [Manage certificates](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/manage-certificates/index.md)
- [Per-hostname](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/index.md)
- [Roll back per-hostname AOP](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/rollback/index.md)
- [Zone-level](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/index.md)
- [Cipher suites](https://developers.cloudflare.com/ssl/origin-configuration/cipher-suites/index.md): Review a list of cipher suites that Cloudflare presents to origins during an SSL/TLS handshake.
- [Custom Origin Trust Store](https://developers.cloudflare.com/ssl/origin-configuration/custom-origin-trust-store/index.md): Custom Origin Trust Store allows you to upload certificate authorities (CAs) that Cloudflare will use to authenticate connections to your origin server.
- [Cloudflare origin CA](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/index.md): Encrypt traffic between Cloudflare and your origin web server and reduce origin bandwidth consumption.
- [Troubleshooting Cloudflare origin CA](https://developers.cloudflare.com/ssl/origin-configuration/origin-ca/troubleshooting/index.md): Troubleshoot issues like NET::ERR_CERT_AUTHORITY_INVALID when using Cloudflare origin CA.
- [Encryption modes](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/index.md): Encryption modes allow you to control how Cloudflare connects to your origin web server and how certificates presented by your origin are validated.
- [Flexible](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/flexible/index.md): Traffic from browsers to Cloudflare can be encrypted via HTTPS, but traffic from Cloudflare to the origin server is not. This mode is common for origins that do not support TLS, though upgrading the origin configuration is recommended whenever possible.
- [Full](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full/index.md): Cloudflare matches the browser request protocol when connecting to the origin. If the browser uses HTTP, Cloudflare connects to the origin via HTTP; if HTTPS, Cloudflare uses HTTPS without validating the originâs certificate. This mode is common for origins that use self-signed or otherwise invalid certificates.
- [Full (strict)](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/index.md): Similar to Full Mode, but with added validation of the origin serverâs certificate, which can be issued by a public CA like Letâs Encrypt or by Cloudflare Origin CA.
- [Off (no encryption)](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/off/index.md): No encryption is used for traffic between browsers and Cloudflare or between Cloudflare and origins. Everything is cleartext HTTP.
- [Strict (SSL-Only Origin Pull)](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/ssl-only-origin-pull/index.md): Regardless of whether the browser-to-Cloudflare connection uses HTTP or HTTPS, Cloudflare always connects to the origin over HTTPS with certificate validation.
- [SSL/TLS Recommender](https://developers.cloudflare.com/ssl/origin-configuration/ssl-tls-recommender/index.md)

## reference

- [Features and plans](https://developers.cloudflare.com/ssl/reference/all-features/index.md): Review information on all Cloudflare SSL/TLS features and their availability.
- [Browser compatibility](https://developers.cloudflare.com/ssl/reference/browser-compatibility/index.md): Review information about browser compatibility for the different Cloudflare SSL/TLS offerings.
- [Certificate and hostname priority](https://developers.cloudflare.com/ssl/reference/certificate-and-hostname-priority/index.md): Learn about how Cloudflare decides which certificate and associated SSL/TLS settings to apply to individual hostnames.
- [Certificate authorities](https://developers.cloudflare.com/ssl/reference/certificate-authorities/index.md): For publicly trusted certificates, Cloudflare partners with different certificate authorities (CAs). Refer to this page to check what CAs are used for each Cloudflare offering and for more details about the CAs features, limitations, and browser compatibility.
- [Certificate pinning](https://developers.cloudflare.com/ssl/reference/certificate-pinning/index.md): Learn why Cloudflare does not support HTTP public key pinning (HPKP) and consider an alternative solution to prevent certificate misissuance.
- [Certificate statuses](https://developers.cloudflare.com/ssl/reference/certificate-statuses/index.md): Understand certificate statuses in Cloudflare SSL/TLS, including stages like Initializing, Pending Validation, and Active. Monitor via dashboard or command line.
- [Validity periods and renewal](https://developers.cloudflare.com/ssl/reference/certificate-validity-periods/index.md): Learn about Cloudflare SSL certificate validity periods, auto renewal processes, and the benefits of shorter validity periods for enhanced security.
- [Cloudflare and CVE-2019-1559](https://developers.cloudflare.com/ssl/reference/cloudflare-and-cve-2019-1559/index.md)
- [PCI compliance and vulnerabilities mitigation](https://developers.cloudflare.com/ssl/reference/compliance-and-vulnerabilities/index.md)
- [Entrust distrust by major browsers](https://developers.cloudflare.com/ssl/reference/migration-guides/entrust-distrust/index.md): Chrome and Mozilla have announced they will no longer trust Entrust certificates. Read about this change and how you can use Cloudflare to reduce impact.
- [TLS protocols](https://developers.cloudflare.com/ssl/reference/protocols/index.md): Explore Cloudflare's support for TLS protocols from 1.0 to 1.3. Learn about differences, security standards, and recommendations on what version to use.