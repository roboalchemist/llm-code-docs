# Source: https://docs.api7.ai/apisix/key-concepts/plugin-global-rules.md

# Plugin Global Rules

In this document, you will learn the basic concept of plugin global rules in APISIX and why you may need them.

Explore additional resources at the end of the document for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

In APISIX, a *global rule* object is used to create [plugins](https://docs.api7.ai/apisix/key-concepts/plugins.md) that are triggered on every incoming request and executed before other plugins locally bound to objects, such as [routes](https://docs.api7.ai/apisix/key-concepts/routes.md), [services](https://docs.api7.ai/apisix/key-concepts/services.md), [consumers](https://docs.api7.ai/apisix/key-concepts/consumers.md), [consumer groups](https://docs.api7.ai/apisix/key-concepts/consumer-groups.md), or [plugin configs](https://docs.api7.ai/apisix/key-concepts/plugin-configs.md). Certain plugins, such as rate limiting and observability plugins, are frequently enabled globally in order to provide consistent and comprehensive protection for APIs.

The following diagram illustrates an example of enabling [`key-auth`](https://docs.api7.ai/hub/key-auth.md) plugin globally for all incoming requests. Once a request is authenticated, the route uses the [`proxy-rewrite`](https://docs.api7.ai/hub/proxy-rewrite.md) plugin to set an additional request header, which demonstrates the [plugins execution order](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-order):

![key-auth global rule diagram](https://static.api7.ai/uploads/2024/09/12/oP3EEnCP_globalrule_cred.svg)

This configuration ensures that only the authenticated requests are allowed to interact with the upstream service. If a request is sent to APISIX:

* without any key or with a wrong key, the request is rejected.
* with `global-key` but to a non-existent route, the request is authenticated but APISIX returns an error warning users that the route is not found.
* with `global-key` to an existing route, the request is first authenticated, then the header of the request is modified by the plugin on the route, and finally the request is forwarded to the upstream service.

The example above used two different plugins in a global rule and a route. If the same plugin is configured in both objects, both instances of the plugin will be [executed sequentially](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-execution-order), rather than overwriting each other.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts

  <!-- -->

  * [Plugins](https://docs.api7.ai/apisix/key-concepts/plugins.md)
  * [Consumers](https://docs.api7.ai/apisix/key-concepts/consumers.md)
  * [Credentials](https://docs.api7.ai/apisix/key-concepts/credentials.md)

* [Plugin Hub](https://docs.api7.ai/hub.md)

* Admin API - [Plugin Global Rules](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Global-Rule)
