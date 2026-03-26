# Source: https://docs.api7.ai/ingress-controller/common-use-cases.md

# Common Use Cases

The Ingress Controller allows you to configure all plugins supported by the underlying gateway, covering a wide range of common use cases such as AI integration, traffic management, request transformation, authentication, security, observability, and more.

* API7 Ingress Controller: supports configuring all plugins available in API7 Enterprise.
* APISIX Ingress Controller: supports configuring all plugins available in APISIX.

For users familiar with APISIX or API7 Enterprise plugins, the concepts remain the same. For those new to the ecosystem, it is recommended to explore the [Plugin Hub](https://docs.api7.ai/hub.md) to review the available plugins and develop a general understanding of their capabilities.

This document introduces common use cases, highlights the plugins you can apply, and offers an overview of how to configure them using the Ingress Controller.

## How to Configure Plugins in AIC[â](#how-to-configure-plugins-in-aic "Direct link to How to Configure Plugins in AIC")

This document provides an overview rather than full configuration details for each plugin. Refer to the examples below and the CRD documentation for common plugin configuration patterns:

* [Configure a plugin on a route](https://docs.api7.ai/ingress-controller/reference/examples.md#configure-plugin-on-route)
* [Configure a plugin on a consumer](https://docs.api7.ai/ingress-controller/reference/examples.md#configure-plugin-on-consumer)
* [Configure a plugin in PluginConfig](https://docs.api7.ai/ingress-controller/reference/examples.md#configure-plugin-config)
* [Configure a global plugin](https://docs.api7.ai/ingress-controller/reference/examples.md#configure-global-plugin)
* [Configure plugin metadata](https://docs.api7.ai/ingress-controller/reference/examples.md#configure-plugin-metadata)

For detailed plugin parameters and usage, visit the [Plugin Hub](https://docs.api7.ai/hub.md).

## Rate Limiting[â](#rate-limiting "Direct link to Rate Limiting")

Rate limiting is a commonly used technique for managing API traffic. You can configure your APIs to control the rate of requests or connections, ensuring fair usage and protecting against attacks such as DDoS or excessive crawler traffic.

There are several rate limiting plugins available that help you implement rate limiting:

* [`limit-count`](https://docs.api7.ai/hub/limit-count.md) uses a fixed window algorithm, which sets limits on the number of requests within non-overlapping time intervals.
* [`limit-count-advanced`](https://docs.api7.ai/hub/limit-count-advanced.md) builds on [`limit-count`](https://docs.api7.ai/hub/limit-count.md) with additional features. It supports using a sliding window algorithm to enforce request limits over overlapping time intervals. This plugin is only available in API7 Enterprise.
* [`limit-req`](https://docs.api7.ai/hub/limit-req.md) limits requests by the number of requests within a given time interval and a set capacity.
* [`limit-conn`](https://docs.api7.ai/hub/limit-conn.md) limits requests by the number of concurrent connections.
* [`graphql-limit-count`](https://docs.api7.ai/hub/graphql-limit-count.md) limits requests by the depth of GraphQL operations or mutations within a given time interval. This plugin is only available in API7 Enterprise.

## Authentication[â](#authentication "Direct link to Authentication")

Authentication is the process of verifying the identity of a client before granting access to an API. It ensures that only authorized users or applications can interact with your services, protecting sensitive data and preventing unauthorized access.

There are a number of authentication plugins available to help you secure your APIs:

* [`key-auth`](https://docs.api7.ai/hub/key-auth.md) â verifies access using a simple API key.
* [`basic-auth`](https://docs.api7.ai/hub/basic-auth.md) â authenticates clients using a username and password.
* [`jwt-auth`](https://docs.api7.ai/hub/jwt-auth.md) â validates JSON Web Tokens (JWT) for stateless authentication.
* [`hmac-auth`](https://docs.api7.ai/hub/hmac-auth.md) â authenticates requests using HMAC signatures to ensure integrity and verify the clientâs identity.
* [and many more](https://docs.api7.ai/hub.md#authentication).

## Request & Response Transformation[â](#request--response-transformation "Direct link to Request & Response Transformation")

Request and response transformation allows you to modify incoming requests before they are sent to upstream services, as well as alter responses before they reach the client. This can include rewriting paths, adding or removing headers, adjusting query parameters, or modifying the request or response body. Transformations help ensure that your APIs remain consistent and compatible with different client requirements or upstream service expectations.

There are several plugins available to help you implement transformation:

* [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) â rewrites the request path, host, or headers.
* [`response-rewrite`](https://docs.api7.ai/hub/response-rewrite.md) â modifies response status codes, headers, or bodies.
* [`mocking`](https://docs.api7.ai/hub/mocking.md) â simulates API responses without forwarding requests to upstream services.
* [and many more](https://docs.api7.ai/hub.md#transformation).

These plugins allow you to adapt requests and responses without modifying your upstream services, making API integration more flexible and easier to maintain.

## AI Integration[â](#ai-integration "Direct link to AI Integration")

AI integration enables your APIs to connect with AI services. This supports functionality such as text generation, summarization, embedding search, retrievalâaugmented generation (RAG), content moderation, and more.

There are several plugins available to support AI integration:

* [`ai-proxy`](https://docs.api7.ai/hub/ai-proxy.md) â simplifies integration with LLM providers, such as OpenAI and DeepSeek.
* [`ai-rag`](https://docs.api7.ai/hub/ai-rag.md) â enables retrievalâaugmented generation to improve output relevance and accuracy.
* [`ai-aws-content-moderation`](https://docs.api7.ai/hub/ai-aws-content-moderation.md) / [`ai-aliyun-content-moderation`](https://docs.api7.ai/hub/ai-aliyun-content-moderation.md) â integrate with external contentâmoderation services to scan prompts for toxicity, hate speech or disallowed content, rejecting requests that fail the moderation.
* [`ai-rate-limiting`](https://docs.api7.ai/hub/ai-rate-limiting.md) â enforces tokenâbased rate limiting on LLM requests, helping you control usage, prevent abuse, and manage cost or resource usage.
* [and many more](https://docs.api7.ai/hub.md#ai).

## Observability[â](#observability "Direct link to Observability")

Observability provides insight into the behavior, health, and performance of your API traffic. With proper observability, you can monitor, trace, and log requests to detect anomalies, troubleshoot issues, and improve reliability across your microservices.

There are a number of observability plugins available, covering logging, metrics, and tracing:

* [`prometheus`](https://docs.api7.ai/hub/prometheus.md) â exposes gateway metrics to monitor performance.
* [`kafka-logger`](https://docs.api7.ai/hub/kafka-logger.md) â pushes logs in batches to a Kafka cluster for scalable log handling and downstream processing.
* [`opentelemetry`](https://docs.api7.ai/hub/opentelemetry.md) â instruments the gateway to generate traces according to the OpenTelemetry standard, allowing export to OTLPâcompatible collectors.
* [`zipkin`](https://docs.api7.ai/hub/zipkin.md), [`skywalking`](https://docs.api7.ai/hub/skywalking.md) â support sending trace data to compatible tracing backends for full-view request path tracing across services.
* [and many more](https://docs.api7.ai/hub.md#observability).

## Next Steps[â](#next-steps "Direct link to Next Steps")

Visit [how-to guides](https://docs.api7.ai/ingress-controller/proxy-to-weighted-backends.md) for configuration scenarios that are not covered by built-in plugin functionality.
