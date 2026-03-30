# Source: https://docs.api7.ai/apisix/enterprise-feature/enterprise-plugins.md

# Enterprise Plugins

API7 Enterprise offers a robust suite of advanced plugins designed to enhance API gateway capabilities, catering to a wide range of use cases. These enterprise-exclusive plugins provide powerful tools for traffic management, data transformation, authentication, and security, ensuring a secure, efficient, and scalable API ecosystem. By leveraging these plugins, organizations can achieve granular control over API traffic, customize gateway responses, and secure their APIs against potential threats.

With continuous innovation, API7 Enterprise plugins are tailored to meet complex business needs. From implementing advanced rate-limiting algorithms to customizing error pages and transforming gateway responses, the plugin library empowers enterprises to optimize API performance, enhance security, and improve the overall user experience. You can start exploring Enterprise plugins using the API7 Enterprise free trial.

## Enterprise Plugins[â](#enterprise-plugins "Direct link to Enterprise Plugins")

The following is a list of plugins exclusive for API7 Enterprise by category, which is still rapidly growing over time. Visit [Plugin Hub](https://docs.api7.ai/hub.md) to see all available plugins.

![enterprise plugins](https://static.api7.ai/uploads/2024/12/13/PuKMkitO_enterprise-plugins.png)

### Traffic Management[â](#traffic-management "Direct link to Traffic Management")

* `graphql-limit-count`: rate limit GraphQL requests based on the depth of the GraphQL queries or mutations.
* `graphql-proxy-cache`: provides the capability to cache responses for GraphQL queries.
* `oas-validator`: validates requests or responses against a defined Open API schema.
* `proxy-buffering`: dynamically disables the NGINX `proxy_buffering` directive to work with SSE (Server-Sent Events) and other upstream services sending stream data.
* `traffic-label`: label traffic based on user-defined rules and takes actions based on labels and the associated weights for actions.
* `limit-count-advanced`: offers sliding window algorithm in addition to the fixed window algorithm to rate limit requests.

### Transformation[â](#transformation "Direct link to Transformation")

* `exit-transformer`: supports the customization of gateway responses based on the status codes, headers, and bodies returned from APISIX plugins.
* `soap`: provides a convenient approach to transform between RESTful HTTP requests and SOAP requests, as well as their corresponding responses.

### Authentication[â](#authentication "Direct link to Authentication")

* `saml-auth`: enables API7 to act as the service provider (SP) and authenticate users via SAML 2.0 by interacting with identity providers (IdP).

### Security[â](#security "Direct link to Security")

* `acl`: allows or denies request access to upstream resources by verifying whether the user initiating the request is in the access control lists.
* `data-mask`: provides the capability to remove or replace sensitive information in request headers, request bodies, and URL queries.

### General[â](#general "Direct link to General")

* `error-page`: allows customizing the error page served when APISIX encounters an exception.

## Use Cases[â](#use-cases "Direct link to Use Cases")

The following are a few use cases using Enterprise plugins. For more information, please see [plugin docs](https://docs.api7.ai/hub.md).

### Redact Sensitive Information[â](#redact-sensitive-information "Direct link to Redact Sensitive Information")

Use `data-mask` plugin to remove or replace sensitive information in the request body before the request is forwarded to upstream services. For example, when forwarding user input to an LLM upstream service, sensitive data such as social insurance numbers, birthdays, or other confidential details might be included in the input prompt. With `data-mask` plugin, the Gateway can automatically detect and mask such information before it reaches upstream services. This ensures compliance with privacy regulations, reduces the risk of data breaches, and maintains user trust.

### Disable Proxy Buffering for SSE[â](#disable-proxy-buffering-for-sse "Direct link to Disable Proxy Buffering for SSE")

When integrating with Server-Sent Events upstream services, real-time data transmission is critical for applications like live notifications, stock updates, or chat systems. By default, NGINXâs `proxy_buffering` directive can introduce latency, as it buffers data before forwarding it to the client. The `proxy-buffering` plugin allows dynamic disabling of this directive at runtime, ensuring that SSE upstream services stream data to clients without unnecessary delays.

### Customize Error Pages[â](#customize-error-pages "Direct link to Customize Error Pages")

The `error-page` plugin allows customizing the error page when APISIX throws `404`, `500`, `502`, or `503` errors. For instance, when APISIX encounters an exception, such as an unavailable upstream service or a gateway timeout, the Gateway can return a customized error page, which aligns with the applicationâs branding or provides actionable steps, to users. You can configure different error pages for the supported error code. The customized error pages help ensure a consistent and professional user experience.

### Apply Rate Limiting with Sliding Window[â](#apply-rate-limiting-with-sliding-window "Direct link to Apply Rate Limiting with Sliding Window")

The `limit-count-advanced` plugin builds on top of the `limit-count` plugin and supports sliding window algorithm when rate limiting. The sliding window algorithm tracks requests in overlapping intervals, smoothing out the rate limit by counting recent requests within the last configured time period, regardless of when the interval began. This method reduces traffic spikes and is more effective at evenly distributing requests over time. For example, in an e-commerce API handling high-traffic flash sales, using the sliding window algorithm ensures requests are distributed smoothly, preventing sudden traffic spikes from overwhelming the system.

### Implement Access Control List[â](#implement-access-control-list "Direct link to Implement Access Control List")

The `acl` plugin regulates requests to upstream resources by verifying whether the user initiating the request is in the access control lists. The user identities can be obtained from consumer labels or user information from third-party identity providers, such as Keycloak. For instance, in a multi-tenant SaaS platform, the API gateway can use ACLs to verify if a user or service attempting to access specific endpoints is authorized. By allowing or denying requests based on predefined access control lists, the plugin ensures that only permitted tenants or teams can reach their designated APIs. This centralized enforcement at the gateway level enhances security, simplifies management, and reduces the risk of unauthorized access across the entire API ecosystem.
