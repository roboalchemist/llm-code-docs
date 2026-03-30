# Source: https://docs.api7.ai/enterprise/key-concepts/snis.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/snis.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/snis.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/snis.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/snis.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/snis.md

# SNIs

An SNI (Server Name Indication) object represents a many-to-many mapping between hostnames of [services](https://docs.api7.ai/enterprise/3.4.x/key-concepts/services.md) and [certificates](https://docs.api7.ai/enterprise/3.4.x/key-concepts/certificates.md). Therefore, a single certificate object can be shared by multiple services through the use of SNI.

## How SNI Works[â](#how-sni-works "Direct link to How SNI Works")

Since API7 Gateway sits in front of the actual backend services, it acts as the server in the handshake.

When a client initiates an SSL/TLS connection, it includes the hostname it is trying to reach in the Server Name Indication (SNI) field of the TLS handshake. The server uses the SNI received from the client to select the appropriate SSL certificate from its repository. Then the server presents the matched certificate to the client, completing the TLS handshake and establishing a secure connection.

In mTLS, CA certificate is also needed along with the SSL certificate. After the server presents its certificate, the client also presents its own certificate to the server. The server verifies the client certificate using the public key. This ensures that the client is authenticated and authorized to access the server's resources. Both the client and the server have now verified each other's identities, establishing a secure and mutually authenticated connection

## Use Cases[â](#use-cases "Direct link to Use Cases")

* **Efficient use of resources:** Allows multiple services with different hostnames to share certificate management, reducing infrastructure costs and complexity.
* **Enhanced security:** Ensures that the correct SSL certificate is presented for each hostname, maintaining secure connections and preventing potential security breaches.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Services](https://docs.api7.ai/enterprise/3.4.x/key-concepts/services.md)
  * [SNIs](https://docs.api7.ai/enterprise/3.4.x/key-concepts/snis.md)

* API Security
  <!-- -->
  * [Configure mTLS between Client and API7 Gateway](https://docs.api7.ai/enterprise/3.4.x/api-security/client-mtls.md)
