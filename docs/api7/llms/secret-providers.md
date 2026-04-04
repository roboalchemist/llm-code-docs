# Source: https://docs.api7.ai/apisix/enterprise-feature/secret-providers.md

# Secret Providers

As a critical infrastructure component, API gateways interact with various upstream services and handle API traffic, which may involve sensitive data such as passwords, tokens, and SSL certificates. This sensitive information must be properly stored, encrypted, rotated, and retired to ensure system security.

Users can store and manage these secrets directly in API7 Enterprise, which will encrypt and store them according to [FIPS standards](https://docs.api7.ai/apisix/enterprise-feature/apisix/enterprise-feature/compliance#1-fips-140-2). Alternatively, they can store them in third-party secrets managers like HashiCorp Vault or AWS Secrets Manager, referencing them in API7 Enterprise via variables.

## Why Use Secret Providers[â](#why-use-secret-providers "Direct link to Why Use Secret Providers")

API7 Enterprise employs Secret Providers to decouple secret storage and management from API gateways, thus enhancing overall security. Currently, secret providers integrate with HashiCorp Vault and AWS Secrets Manager. More popular secret managers, like GCP Secret Manager, will be supported in future releases. A secret provider object contains connection and authentication information for a specific secret manager:

![Secret Provider Configuration](https://static.api7.ai/uploads/2024/12/05/u49Cs1CU_secret-providers-1.png)

Users can store secrets such as credentials used for consumer authentication or SSL certificates used during HTTPS requests in the secret manager. These secrets are then integrated and referenced in API7 Enterprise via secret providers. This setup allows API7 Enterprise to securely reference the corresponding secrets, such as the key needed to authenticate a consumer.

![Reference Secret from AWS Secrets Manager](https://static.api7.ai/uploads/2024/12/05/STJu4ZzU_secret-providers-2.png)

The diagram below illustrates the consumer authentication flow, where secrets are stored in the secret provider, and API7 Enterprise retrieves secrets from the secret providers after connecting and authenticating with them. This process decouples the secrets from the API gateway.

![Diagram of Retrieving Secrets from Secret Providers](https://static.api7.ai/uploads/2024/12/06/fHE6vTIf_secret-providers.png)

## Key Features[â](#key-features "Direct link to Key Features")

* Store sensitive information using third-party secret providers, decoupling secrets from API gateways and enhancing security.
* Reference externally stored secrets as variables, simplifying configuration management.
* Support multiple secret providers to accommodate complex enterprise architectures and unify secret management.
* Precisely control access to sensitive information, preventing unauthorized usage and data breaches.

## Use Cases[â](#use-cases "Direct link to Use Cases")

### Enhanced Data Security[â](#enhanced-data-security "Direct link to Enhanced Data Security")

Managing large volumes of sensitive information is a significant challenge for many enterprises. API7 Enterprise offers a secure solution by integrating with third-party secret providers such as HashiCorp Vault and AWS Secrets Manager. Enterprises can store sensitive data on these third-party platforms and reference them as variables within API7 Enterprise, decoupling API gateway and secret management. This prevents sensitive information from being exposed in system configurations, greatly enhancing data security. Additionally, centralizing sensitive data and keys on a dedicated management platform improves efficiency, enables audit tracking, and allows flexible access control. This helps enterprises effectively address complex security challenges.

### Transparent Key Rotation for API Gateways[â](#transparent-key-rotation-for-api-gateways "Direct link to Transparent Key Rotation for API Gateways")

Before implementing the dynamic key retrieval mechanism, enterprises typically managed sensitive information statically by hardcoding keys and other sensitive data in configuration files for access. In API7 Enterprise, dynamic key retrieval is achieved by specifying the path for key access. As long as the key storage path remains the same, any changes to the key will not affect its usage in API7 Enterprise. This approach eliminates the need for manual key management, reducing errors, simplifying key management, and significantly improving security.

### Audit and Compliance[â](#audit-and-compliance "Direct link to Audit and Compliance")

Using keys and sensitive information typically needs to comply with industry standards and regulatory requirements. After integrating with third-party secrets managers, API7 Enterprise can record detailed access logs and audit information for secret provider resources, such as creating, editing, or deleting secret providers. This helps enterprises with compliance checks and security analysis. Through audit tracking, businesses can promptly detect abnormal access behavior and take appropriate protective measures.

The reference relationships for variables in consumer credentials can be viewed in the reference list of the secret provider on the API7 dashboard. When editing or deleting a secret provider, reference checks are performed to prevent configuration errors due to invalid variable references.
