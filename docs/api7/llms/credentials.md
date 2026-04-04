# Source: https://docs.api7.ai/apisix/key-concepts/credentials.md

# Source: https://docs.api7.ai/apisix/enterprise-feature/credentials.md

# Source: https://docs.api7.ai/apisix/key-concepts/credentials.md

# Source: https://docs.api7.ai/apisix/enterprise-feature/credentials.md

# Credentials

Credentials are data used to verify the identity of an individual or system. They serve as a way to authenticate and authorize access to protected resources, proving that a user or system is who they claim to be.

Credentials can take various forms, including but not limited to:

* Usernames and passwords: a unique username paired with a secret password.
* API keys or tokens: alphanumeric strings generated for applications or users to access APIs securely.

In API7 Enterprise, credentials are associated with consumers and contain authentication data. A consumer can be associated with one or more credentials from a designated list of authentication plugins, including `key-auth`, `basic-auth`, `jwt-auth`, and `hmac-auth`. The decoupling of credentials from consumers facilitates credential reuse and rotation as well as enhanced security.

Consider a scenario where API keys have a defined lifespanâsuch as one monthâconfiguring multiple credentials of the same type allows administrators to assign a new API key while the existing one is still valid. The approach provides a buffer period during which both keys are accepted, enabling administrators to update client applications with the new key while avoiding any disruption to active services. Once the new key is in use, the old key can be securely removed, mitigating risks associated with abrupt credential changes and reducing the chance of application downtime or access issues during credential rotation.

![key rotation transition period diagram](https://static.api7.ai/uploads/2024/12/06/B065grtp_credential-concept.png)

## Key Features[â](#key-features "Direct link to Key Features")

* Have a one-to-many relationship with consumers.
* Support the key management of multiple authentication methods, including key authentication, JWT, HMAC, and basic authentication.
* Allow for independent management and updates to consumer authentication details, which promotes better security practices, simplifies maintenance, and prevents unintended changes to consumers.
* Forward the `X-Credential-Identifier` header containing the configured credential ID to upstream services, which allows for additional business logic to be implemented.
* When examining consumer details, the returned information does not expose the consumer-associated credentials, reducing the attack surface.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Mitigate Configuration Drift[â](#mitigate-configuration-drift "Direct link to Mitigate Configuration Drift")

When configuring authentication credentials directly on consumers, each credential rotation or reconfiguration could inadvertently alter or overwrite existing consumer configurations, potentially leading to service disruptions. When decoupling the credential configuration, the credentials can be updated or rotated without touching the consumer-specific settings, reducing the likelihood of configuration driftâa scenario where unexpected changes accumulate over time, leading to mismatched or conflicting configurations compared with what was originally planned.

### Support Credential Rotation[â](#support-credential-rotation "Direct link to Support Credential Rotation")

The ability to configure multiple credentials of the same type for a consumer allows for smooth credential rotation, which is essential for maintaining secure access while minimizing disruptions. For example, in cases where API keys have a defined lifespanâsuch as one monthâhaving multiple credentials of the same type allows administrators to assign a new API key while the existing one remains valid. This controlled overlap period facilitates a seamless transition, where both keys remain active temporarily, ensuring uninterrupted access for dependent applications. Once the new API key is confirmed to be fully operational, the outdated credential can be safely removed.

### Enhance Security Compliance[â](#enhance-security-compliance "Direct link to Enhance Security Compliance")

Regularly rotating credentials, a process that can be facilitated by the use of credentials in API7 Enterprise, is a critical practice for aligning with security frameworks and standards. For example, PCI-DSS (Payment Card Industry Data Security Standard) requires frequent updates of passwords and other credentials for systems handling cardholder data, reducing the risk of unauthorized access due to outdated or compromised credentials.
