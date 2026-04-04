# Source: https://docs.api7.ai/apisix/enterprise-feature/security-hardening.md

# Security Hardening

Security Hardening is the process of implementing configurations, controls, and best practices to minimize vulnerabilities and protect systems from unauthorized access or attacks. In the context of an API gateway, security hardening is crucial, as the gateway often serves as a single point of entry to numerous backend services, data sources, and sensitive business logic. By hardening security on the gateway, organizations reduce potential attack surfaces and ensure that only authorized, properly authenticated requests reach critical resources. In addition, understanding where and how sensitive information is stored is important when planning to implement robust security measures and safeguard against unauthorized access, data breaches, or malicious attacks in your organization. Security hardening for API gateways is essential not only to protect sensitive data but also to maintain performance, regulatory compliance, and trust in the system.

The following is an architecture diagram illustrating various components of API7 Enterprise and how they interact:

![architecture diagram of various API7 Enterprise components](https://static.api7.ai/uploads/2024/11/28/IVzIOALY_security-hardening.png)

## Security Hardening Features[â](#security-hardening-features "Direct link to Security Hardening Features")

* The communication between the dashboard and the DP manager uses HTTPS by default.
* Sensitive data are masked in audit logs before the logs are saved to the database. Any additional alteration to audit logs is forbidden.
* User credentials, including username and password, as well as access token, are salted and PBKDF2 encrypted before being saved to the database.
* Sensitive plugin configurations, such as Redis password, are specified in `encrypted_fields` in the plugin schema. Information in these fields is encrypted with AES256 before being saved to the database.
* Keyrings, which can be used to encrypt sensitive information, differ by gateway group. They are also encrypted before being saved to the database.

## Security Hardening Measures[â](#security-hardening-measures "Direct link to Security Hardening Measures")

The following are a few additional security measures you can optionally choose to harden API7 Enterprise security.

### Secure Data Plane Communication[â](#secure-data-plane-communication "Direct link to Secure Data Plane Communication")

To ensure the confidentiality and integrity of data exchanged between clients and API7 Enterprise, as well as between API7 Enterprise and upstream services, TLS or mTLS (mutual TLS) can be configured for communication, using the SSL configuration in API7 Enterprise. By enabling TLS, data transmitted between the client and API7 Enterprise, or between API7 Enterprise and upstream services, is encrypted, protecting against interception and tampering. This setup ensures that unauthorized parties cannot read or alter the data in transit, providing a secure channel over potentially insecure networks.

With mTLS, both partiesâAPI7 Enterprise and its client or upstream serviceâauthenticate each other. This bidirectional authentication is particularly valuable for high-security environments, where verifying the identity of both communicating parties prevents unauthorized access. mTLS is commonly used to secure communication with sensitive back-end systems or between internal services where data protection is critical.

### Encrypt Data with Keyring[â](#encrypt-data-with-keyring "Direct link to Encrypt Data with Keyring")

`data_encryption` is a configurable option in the `config.yaml`, which is set to false by default. When set to true, API7 Enterprise will encrypt sensitive plugin fields specified in `encrypt_fields` and TLS certificate private key before saving them to the database.

A `keyring` is a collection of encryption keys used for securing the specified sensitive data. Regularly rotating keyrings is a recommended security practice to minimize the risk of key compromise, maintain data integrity, and align with best practices for cryptographic key management.

config.yaml

```
  data_encryption:
    enable: false
    keyring:
      - qeddd145sfvddff3
```

When performing key rotation, beware that if your API7 Enterprise is already running and has data encrypted, do not remove the old keys. Add the new keys at the top of the array, so that the encrypted data can be correctly decrypted. Removing the old keys directly can render the encrypted data irreversible.

### Manage Secrets in Secrets Manager[â](#manage-secrets-in-secrets-manager "Direct link to Manage Secrets in Secrets Manager")

To enhance security and simplify the management of sensitive data, API7 Enterprise allows you to store keys in secrets managers such as HashiCorp Vault and AWS Secrets Manager. Secrets managers provide a centralized, encrypted repository for sensitive information, such as API tokens, credentials, and encryption keys.

For example, in API7 Enterprise, sensitive plugin fieldsâsuch as Redis passwords or private keys for TLS certificatesâcan be securely stored in a secrets manager. At runtime, API7 retrieves these secrets via integration with the secrets manager, ensuring that sensitive data remains protected throughout its lifecycle.

One key advantage of using a secrets manager is enhanced security. This reduces the data risk associated with embedding sensitive information directly into configuration files or exposing it through environment variables. Another advantage is the support for automatic key rotation. Regularly rotating keys is a security best practice, as it minimizes the risk of compromised credentials being exploited over time. Many secrets managers automate this process, updating keys and ensuring that dependent services can access the latest versions without manual intervention. This automation reduces operational overhead while helping organizations comply with regulatory requirements and industry standards.

### Incorporate Continuous Monitoring[â](#incorporate-continuous-monitoring "Direct link to Incorporate Continuous Monitoring")

Incorporating continuous monitoring into your stack helps harden your API infrastructure security by collecting and analyzing real-time metrics. This approach provides early detection of threats, such as unauthorized access or unusual traffic patterns, and helps optimize API performance by identifying bottlenecks.

API7 Enterprise offers a built-in event-based alerting system with a series of pre-configured conditions that can trigger alerts, such as Control Plane certificate nearing expiration, gateway instances going offline, or CPU quota exceeded. The alert events can be configured on the Dashboard, each of which can be further customized with severity, check intervals, thresholds, and notification content. See [Alerts and Contact Points](https://docs.api7.ai/apisix/enterprise-feature/alerts-and-contact-points.md) for more information.

API7 Enterprise can also integrate with external tools like Prometheus and Datadog. The Gateway supports exposing a comprehensive set of metrics to the monitoring tools with minimal delay. These integrations allow administrators to visualize metrics, configure alerts, and quickly respond to critical events. Additionally, monitoring helps optimize API performance by pinpointing resource inefficiencies, ensuring smooth operation even under high traffic loads. For organizations subject to regulatory requirements, continuous monitoring also supports compliance by offering detailed metrics and logs necessary for audits and reporting.
