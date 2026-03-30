# Source: https://docs.api7.ai/portal/introduction.md

# Source: https://docs.api7.ai/enterprise-whitepaper/introduction.md

# Source: https://docs.api7.ai/enterprise/introduction.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/introduction.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/introduction.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/introduction.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/introduction.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/introduction.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/introduction.md

# Source: https://docs.api7.ai/enterprise/3.8.x/introduction.md

# Source: https://docs.api7.ai/enterprise/3.7.x/introduction.md

# Source: https://docs.api7.ai/enterprise/3.6.x/introduction.md

# Source: https://docs.api7.ai/enterprise/3.5.x/introduction.md

# Source: https://docs.api7.ai/enterprise/3.4.x/introduction.md

# Source: https://docs.api7.ai/enterprise/3.3.x/introduction.md

# Overview

**API7 Enterprise extends the core open-source functionality of [Apache APISIX](https://github.com/apache/apisix) to provide customized, full-lifecycle API management for enterprises.** It offers a comprehensive API management solution with **API7 Gateway** and the new **API7 Portal (Beta)**.

API7 Enterprise also offers enterprise-level 24/7 support, advanced features, system integration, and SLA guarantees.

## What Is API7 Enterprise?[â](#what-is-api7-enterprise "Direct link to What Is API7 Enterprise?")

API7 Enterprise is a full-lifecycle API management solution designed specifically for enterprises, offering a wide range of essential functionalities. These include multi-tenancy, Role-Based Access Control (RBAC), a developer portal, and more.

With a variety of protocol transcoding plugins and professional and timely technical support, API7 Enterprise modernizes legacy applications, monetizes your APIs, and delivers products faster and more securely.

## Why API7 Enterprise?[â](#why-api7-enterprise "Direct link to Why API7 Enterprise?")

Going beyond the core open-source capabilities, API7 Enterprise extends Apache APISIX to provide full-lifecycle API management tailored for enterprises. It delivers enterprise-grade 24/7 support, commercial features, plugin integrations, and SLA guarantees to realize the maximum potential of APISIX-driven API management.

API7 Enterprise has the most requested enterprise-grade features tested and validated by the market. With robust support for security, traffic management, analytics, and developer engagement, API7 Enterprise adapts to diverse enterprise API requirements and use cases across sectors.

By complementing Apache APISIX with enterprise-grade support and capabilities, API7 Enterprise enables enterprises to focus on delivering business value from APIs rather than complex management.

With API7 Enterprise, enterprises can accelerate and optimize their end-to-end API lifecycle without having to build in-house expertise:

* Govern API security, access, and traffic at scale
* Gain visibility through analytics across the full-lifecycle
* Integrate API gateways with existing systems and processes
* Future-proof API infrastructure management as needs grow
* Provide fine-grained traffic control with dynamic load balancing, circuit breaking, rate limiting, and so on

API7 Enterprise enables enterprises to realize the full potential of APIs while addressing complexities at scale.

## Advantages and Highlights[â](#advantages-and-highlights "Direct link to Advantages and Highlights")

![advantages-and-highlights](https://static.api7.ai/uploads/2023/08/29/XAO2dI0y_Advantages.PNG)

* **Cloud-Native**

  API7 Enterprise is a cloud-native gateway that is platform-agnostic, eliminating the risk of vendor lock-in. It supports various environments including bare metal, virtual machines, Kubernetes, OpenShift, and ARM64. In addition, API7 Enterprise seamlessly integrates with other components like SkyWalking, Prometheus, Kafka, Zipkin, and others, providing comprehensive capabilities for enterprises.

* **High Availability**

  API7 Enterprise can effortlessly handle millisecond-level configuration updates and support thousands of gateway nodes. The statelessness of gateway nodes allows for effortless scaling and resizing.

* **Multiple Protocol Conversion**

  API7 Enterprise supports a wide range of protocols, including TCP/UDP, Dubbo, MQTT, gRPC, SOAP, and WebSocket.

* **Enhanced Security and Protection**

  API7 Enterprise comes with a variety of built-in authentication and security capabilities, such as Basic Auth, JSON Web Token, IP blacklists/whitelists, and OAuth.

* **Exceptional Performance**

  With its radix tree algorithm for high-performance and flexible routing, API7 Enterprise achieves impressive results on AWS 8-core servers. API7 Enterprise can handle approximately 140,000 queries per second (QPS) with a latency of around 0.2 milliseconds.

* **Fully Dynamic**

  Modifications to gateway configurations, additions, or alterations of plugins can take effect in real-time without requiring gateway service restarts. API7 Enterprise also supports dynamically loading SSL certificates.

* **Strong Extensibility**

  With the flexible plugin mechanism, API7 Enterprise allows for customizations catering to specific internal business requirements. It supports custom load balancing and routing algorithms and facilitates Serverless execution through runtime execution of user-defined functions. Therefore, API7 Enterprise enhances flexibility at the gateway's edge nodes.

* **Comprehensive Governance**

  API7 Enterprise provides a rich set of governance capabilities, such as fault isolation, circuit-breaking, rate limiting, and throttling. By enabling active health checks, the gateway intelligently tracks the health status of upstream nodes and automatically filters out unhealthy nodes, enhancing overall service stability.

## Supported Functionalities[â](#supported-functionalities "Direct link to Supported Functionalities")

* **API Publishing**

  * Request routing

    <!-- -->

    * URI parameter matching
    * HTTP request header matching
    * HTTP request method matching
    * Conditional expressions
    * IPv6
    * GeoIP location matching
    * Routing time-to-live (TTL)
    * Priority matching

  * Request rewrite

    <!-- -->

    * URI rewrite
    * Add, modify, and delete HTTP request headers
    * 301, 302 redirect
    * Force redirect to HTTPS

  * Response rewrite

    <!-- -->

    * Add, modify, and delete HTTP response headers
    * Modify HTTP response code
    * Modify response body

  * Protocol conversion

    <!-- -->

    * HTTP/1.1, HTTP/2
    * HTTP/3
    * TLS/HTTPS
    * MQTT
    * UDP
    * WebSocket
    * Dubbo
    * Custom Layer 4 protocol
    * Custom Layer 7 protocol

  * Canary release

    <!-- -->

    * Canary release
    * Blue-green deployment

  * Response caching

  * Traffic mirroring

  * Circuit breaking

    <!-- -->

    * API circuit breaking
    * Service degradation

  * Fault injection

  * Traffic staining

  * Service Discovery

* **API Consumption**
  * Consumer Management

* **API Runtime**

  * Monitoring

    <!-- -->

    * Data throughput
    * Response time
    * Upstream response time
    * Status code
    * API call volume
    * Gateway instance version and status
    * Certificate expiration

  * Logging

    <!-- -->

    * Push to HTTP/TCP/UDP log servers
    * SkyWalking
    * Kafka
    * RocketMQ
    * ClickHouse
    * Syslog
    * Aliyun SLS
    * Google Cloud Logging Service
    * Splunk HTTP Event Collector (HEC)
    * Specific file on disk
    * Elasticsearch
    * Tencent Cloud CLS
    * Grafana Loki

  * Tracing

    <!-- -->

    * SkyWalking
    * Zipkin
    * OpenTracing

* **API Security**

  * Request authentication

    <!-- -->

    * JWT
    * Key-auth
    * HMAC
    * Basic-auth
    * Keycloak
    * Casdoor
    * OpenID Connect
    * LDAP
    * Lua Casbin
    * Open Policy Agent
    * External auth servers (Auth0, Okta, etc.)
    * OAuth 2.0

  * Rate limiting

    <!-- -->

    * Request limiting based on a fixed window
    * Request limiting based on the leaky bucket principle
    * Limiting concurrent requests

  * IP restriction

    <!-- -->

    * Blacklist
    * Whitelist
    * Preventing ReDoS attacks
    * Preventing replay attacks

  * URI restriction

    <!-- -->

    * Blacklist
    * Whitelist

  * CORS

* **User Management**
  * Role-based Access Control (RBAC)

* **Data Security**

  * mTLS
  * FIPS
  * SSL certificate rotation

* **Tools**

  * CLI
  * Helm charts
  * Rollback
  * YAML for standalone mode

* **Advanced**

  * Data sovereignty
  * Configuration hot update

## Related Topics[â](#related-topics "Direct link to Related Topics")

* If you want to have a basic knowledge of API7 Enterprise, see [concepts](https://docs.api7.ai/enterprise/3.3.x/key-concepts/services.md) section.
* If you want to get started with API7 Enterprise, see [install API7 Enterprise](https://docs.api7.ai/enterprise/3.3.x/getting-started/install-api7-ee.md) and [launch your first API](https://docs.api7.ai/enterprise/3.3.x/getting-started/launch-your-first-api.md).
