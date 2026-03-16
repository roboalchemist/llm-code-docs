# Source: https://www.apollographql.com/docs/graphos/resources/saf/security.md

# Source: https://www.apollographql.com/docs/graphos/routing/security.md

# Source: https://www.apollographql.com/docs/graphos/connectors/security.md

# Connectors Security Configurations

Security is an essential aspect of any system that connects clients to backend services. When using Apollo Connectors to incorporate REST APIs into your graph, the GraphOS Router provides robust security features to protect your data and services. These include both the Connectors-specific configurations outlined below and the wider set of [router security features](https://www.apollographql.com/docs/graphos/routing/security).

## Authentication

Authentication ensures that your GraphQL API can securely access protected REST APIs. The router supports:

* **AWS Signature Version 4 (SigV4)** for AWS service authentication
* **Custom authentication flows** through coprocessors for dynamic token management
* **Header-based authentication** with static tokens or values from the request context

[Learn more about authentication configurations.](https://www.apollographql.com/docs/graphos/connectors/security/auth)

## TLS Configuration

TLS (Transport Layer Security) provides encryption and certificate-based authentication between your router and REST APIs. You can configure:

* **Certificate authorities** for server validation
* **TLS client authentication** with certificate chains and private keys
* **Source-specific TLS settings** for different security requirements

[Learn more about TLS configurations.](https://www.apollographql.com/docs/graphos/connectors/security/tls)

## Request Limits

Request limits protect your backend services from being overwhelmed with too many API calls. The router allows you to:

* **Set global request limits** across all Connector sources
* **Configure source-specific limits** for different backend services
* **Control behavior** when limits are exceeded

[Learn more about request limits.](https://www.apollographql.com/docs/graphos/connectors/security/request-limits)
