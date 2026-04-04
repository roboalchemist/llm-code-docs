# Source: https://docs.api7.ai/cloud/concepts/plugin.md

# What is Plugin

In API7 Cloud, a plugin is a rule that defines how the gateway instance will handle the requests. By saying handled, it means requests might be:

1. transformed (headers, query parameters, body);
2. protected (authentication, authorization, rate-limiting, etc.);
3. recorded (logging, metrics, etc.);

A plugin can be attached on a specific [service](https://docs.api7.ai/cloud/concepts/service.md), [route](https://docs.api7.ai/cloud/concepts/route.md), [consumer](https://docs.api7.ai/cloud/concepts/consumer.md), or [cluster](https://docs.api7.ai/cloud/concepts/cluster.md). The effective rules of the plugin are as follows:

* Plugins attached to the route only work for this route and will override the same ones on the service (instead of running them twice).
* Plugins attached to the service will affect all routes in this Service.
* Plugins attached to the consumer only work for this consumer and will override the same ones on the service and route (instead of running them twice).
* Plugins attached to the cluster will be effective for all API requests. Care must be taken that these plugins won't override the same ones on the service, route, and consumer, i.e. same plugins will be run twice (the one on cluster runs first).

## What's Next[â](#whats-next "Direct link to What's Next")

API7 Cloud provides several plugins for different purposes. Please refer to the table of contents below to learn the details.

* Security

  <!-- -->

  * [ACL Plugin](https://docs.api7.ai/cloud/guides/security/acl.md)
  * [CORS Plugin](https://docs.api7.ai/cloud/guides/security/cors.md)
  * [CSRF Plugin](https://docs.api7.ai/cloud/guides/security/csrf.md)
  * [IP Restriction Plugin](https://docs.api7.ai/cloud/guides/security/ip-restriction.md)

* Traffic Management

  <!-- -->

  * Authentication Plugin

    <!-- -->

    * [Basic Auth](https://docs.api7.ai/cloud/guides/traffic-management/authentication/basic-auth.md)
    * [HMAC Auth](https://docs.api7.ai/cloud/guides/traffic-management/authentication/hmac-auth.md)
    * [JWT Auth](https://docs.api7.ai/cloud/guides/traffic-management/authentication/jwt-auth.md)
    * [Key Auth](https://docs.api7.ai/cloud/guides/traffic-management/authentication/key-auth.md)
    * [OpenID Connect](https://docs.api7.ai/cloud/guides/traffic-management/authentication/openid-connect.md)

  * [Limit Count Plugin](https://docs.api7.ai/cloud/guides/traffic-management/limit-count.md)

  * [Fault Injection Plugin](https://docs.api7.ai/cloud/guides/traffic-management/fault-injection.md)

  * [Redirect Plugin](https://docs.api7.ai/cloud/guides/traffic-management/redirect.md)

  * [Request Rewrite Plugin](https://docs.api7.ai/cloud/guides/traffic-management/proxy-rewrite.md)

  * [Response Rewrite Plugin](https://docs.api7.ai/cloud/guides/traffic-management/response-rewrite.md)

* Product
  <!-- -->
  * [Request ID Plugin](https://docs.api7.ai/cloud/guides/product/request-id.md)

* Observability

  <!-- -->

  * [Logging Plugin with HTTP Logger](https://docs.api7.ai/cloud/guides/observability/log-collection-with-http-logger.md)
  * [Logging Plugin with Kafka Logger](https://docs.api7.ai/cloud/guides/observability/log-collection-with-kafka-logger.md)
