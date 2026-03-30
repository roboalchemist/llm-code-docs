# Source: https://docs.api7.ai/api7-gateway/security-and-compliance/authenticate/mutual-tls-cp-dp.md

# Mutual TLS between Control Plane and Data Plane

Securing the communication channel between the Control Plane (CP) and Data Plane (DP) is fundamental to the integrity and security of the entire API7 API Gateway. All configuration changes, policy updates, and metrics reporting travel through this channel. To protect this critical infrastructure, API7 enforces mutual TLS (mTLS) for all CP-DP communication, with no option to disable it. This ensures that all data is encrypted in transit and that both planes can cryptographically verify each other's identity before any information is exchanged.

API7 employs a sophisticated Public Key Infrastructure (PKI) model to manage this process, providing a higher level of security and scalability compared to simpler shared-secret or pinned-certificate methods. This approach guarantees that even in a multi-tenant environment, each customer's infrastructure is securely isolated.

### How mTLS Works in API7[â](#how-mtls-works-in-api7 "Direct link to How mTLS Works in API7")

Mutual TLS extends the standard TLS protocol by requiring both the client and the server to present and validate a certificate. In the context of API7, the Data Plane acts as the client initiating the connection, and the Control Plane acts as the server.

The process follows a standard PKI trust model:

1. **Trust Anchor**: The Control Plane maintains a unique, automatically generated Certificate Authority (CA). This CA serves as the single root of trust for that specific API7 deployment.
2. **Certificate Issuance**: The Control Plane uses its private CA to issue unique certificates for itself (server certificate) and for each Data Plane node (client certificates).
3. **Handshake and Verification**: When a Data Plane node attempts to connect to the Control Plane, it presents its client certificate. The Control Plane verifies that the certificate was issued by its own trusted CA. Simultaneously, the Data Plane verifies the Control Plane's server certificate against the same CA.

This bidirectional verification ensures that only authorized Data Plane nodes can connect to the Control Plane, and Data Plane nodes only connect to a legitimate Control Plane, preventing man-in-the-middle attacks and unauthorized configuration injection.

<!-- -->

### CA and Certificate Management[â](#ca-and-certificate-management "Direct link to CA and Certificate Management")

API7 is designed to make certificate management as automated and secure as possible.

#### Automatic CA Generation[â](#automatic-ca-generation "Direct link to Automatic CA Generation")

On its initial startup, the API7 Control Plane checks the database for an existing CA. If no CA is found, it automatically generates a new root CA. This CA is unique to each customer's deployment, ensuring that certificates from one customer's environment cannot be trusted in another. The Control Plane then uses this CA to immediately issue the necessary server and client certificates for establishing secure communication.

#### Certificate Lifetime[â](#certificate-lifetime "Direct link to Certificate Lifetime")

When you install a new Data Plane node, you can specify the certificate validity period based on your organizational security policies. API7 offers the following predefined options:

| Validity Period | Use Case                                                           |
| --------------- | ------------------------------------------------------------------ |
| 1 year          | High-security environments requiring frequent certificate rotation |
| 2 years         | Balanced approach with regular rotation cycles                     |
| 3 years         | Standard enterprise deployments                                    |
| 5 years         | Long-lived production environments                                 |
| 10 years        | Default; suitable for stable, low-rotation deployments             |

By default, new Data Plane nodes are issued certificates with a **10-year validity period**. However, you can select a shorter validity period during the Data Plane installation process to enforce more frequent certificate rotation and align with your security compliance requirements.

#### Certificate Rotation[â](#certificate-rotation "Direct link to Certificate Rotation")

While certificate generation is automatic, the rotation process is currently a manual operation. Administrators are responsible for tracking certificate expiration and initiating the rotation process when required by their security policies or upon a potential compromise.

#### Deployment Flexibility[â](#deployment-flexibility "Direct link to Deployment Flexibility")

API7 offers flexibility in how Data Plane nodes are deployed. Each Data Plane node can be provisioned with its own unique certificate signed by the Control Plane's CA. Alternatively, for simpler deployment scenarios, multiple Data Plane nodes can share the same client certificate.

### Deployment and Configuration[â](#deployment-and-configuration "Direct link to Deployment and Configuration")

One of the key security strengths of API7 is that mTLS between the Control Plane and Data Plane is **enabled by default and cannot be disabled**. This is a zero-configuration feature.

When deploying a new Data Plane node, for instance using the official API7 Helm chart, the necessary CA and client certificates are automatically provisioned and injected into the Data Plane configuration. This out-of-the-box security removes the risk of misconfiguration and ensures that every new node in your cluster communicates securely from the moment it starts.

### Verifying mTLS Configuration[â](#verifying-mtls-configuration "Direct link to Verifying mTLS Configuration")

Verifying that mTLS is functioning correctly is straightforward. The primary indicator is the health and status of the Data Plane node itself.

* **Successful Connection**: If a Data Plane node starts up successfully and its status appears as healthy and connected within the Control Plane dashboard, it signifies that the mTLS handshake was successful and communication is established.
* **Failed Connection**: If the mTLS configuration is incorrect (e.g., due to a missing certificate, a corrupt certificate, or a network issue blocking the handshake), **the Data Plane node will fail to start**. It will not be able to connect to the Control Plane to fetch its configuration and will therefore not be able to proxy any traffic.

### Troubleshooting[â](#troubleshooting "Direct link to Troubleshooting")

The most common issue encountered with CP-DP communication is related to network connectivity, not the mTLS configuration itself. If a Data Plane node fails to connect, check the following:

* **Network Reachability**: Ensure there is a clear network path between the Data Plane node and the Control Plane on the required HTTPS port.
* **Firewall Rules**: Verify that no firewalls, security groups, or network policies are blocking traffic between the CP and DP.
* **DNS Resolution**: Confirm that the Data Plane node can correctly resolve the hostname of the Control Plane.

### Performance Considerations[â](#performance-considerations "Direct link to Performance Considerations")

The mTLS mechanism used for securing the CP-DP channel has **no performance impact** on the API traffic processed by the Data Plane. This secure channel is used exclusively for management tasks, such as the Control Plane pushing configuration updates to the Data Plane and the Data Plane reporting metrics back to the Control Plane. All client-facing API requests are handled by a separate, highly optimized data path that is not involved in this mTLS handshake.
