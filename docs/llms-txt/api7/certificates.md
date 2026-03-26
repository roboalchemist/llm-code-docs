# Source: https://docs.api7.ai/enterprise/key-concepts/certificates.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/certificates.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/certificates.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/certificates.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/certificates.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/certificates.md

# Certificates

Certificates are used when configuring TLS or mTLS between client applications and API7 Gateway. This system of SSL and CA certificates is crucial for establishing trust and security online, allowing users to browse and interact with websites confidently.

* SSL Certificate: Used for Transport Layer Security (TLS). Secure Sockets Layer (SSL) protocol is a cryptographic protocol designed to secure communication between two parties.
* CA Certificate: Used for Mutual Transport Layer Security (mTLS). It is like a double-check system for secure connections, where both sides verify each other's identities before exchanging information.

## SSL Certificate[â](#ssl-certificate "Direct link to SSL Certificate")

TLS is implemented on top of an existing protocol, such as HTTP or TCP. It provides an additional layer of security by establishing a connection through a TLS handshake and encrypting data transmission.

The following illustration highlights the **one-way TLS handshake** in:

* [TLS v1.2](https://www.rfc-editor.org/rfc/rfc5246)
* [TLS v1.3](https://www.rfc-editor.org/rfc/rfc8446)

TLS v1.2 and TLS v1.3 are the two most commonly used TLS versions.

![TLS Handshake for TLS v1.2 and TLS v1.3](https://static.api7.ai/uploads/2023/08/24/OtRgQadG_acvck7tc_handshake.svg)

During this process, the server authenticates itself to the client by presenting its certificate. The client verifies the certificate to ensure that it is valid and issued by a trusted authority. Once the certificate has been verified, the client and server agree on a shared secret, which is used to encrypt and decrypt the application data.

![SSL](https://static.api7.ai/uploads/2024/12/13/vtqOSnyr_key-concept-ssl.png)

## CA Certificate[â](#ca-certificate "Direct link to CA Certificate")

API7 Enterprise also supports mutual TLS (mTLS), where the client also authenticates itself to API7 Gateway by presenting its certificate, effectively creating a two-way TLS connection. This ensures that both parties are authenticated and helps prevent network attacks like [man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack).

## Use Cases[â](#use-cases "Direct link to Use Cases")

To enable TLS or mTLS in your system with API7 Enterprise, you should generate and configure certificates and associate them with [SNIs](https://docs.api7.ai/enterprise/3.4.x/key-concepts/snis.md).

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.4.x/key-concepts/services.md)
  * [SNIs](https://docs.api7.ai/enterprise/3.4.x/key-concepts/snis.md)

* API Security
  <!-- -->
  * [Configure mTLS between Client and API7 Gateway](https://docs.api7.ai/enterprise/3.4.x/api-security/client-mtls.md)
