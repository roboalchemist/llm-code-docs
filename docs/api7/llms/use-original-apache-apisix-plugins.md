# Source: https://docs.api7.ai/cloud/guides/product/use-original-apache-apisix-plugins.md

# Use Original Apache APISIX Plugins

API7 Cloud uses [Apache APISIX](https://apisix.apache.org) as its data plane gateway. Users can use all the original Apache APISIX plugins on API7 Cloud, users can configure these plugins on [service](https://docs.api7.ai/cloud/concepts/service.md), [route](https://docs.api7.ai/cloud/concepts/route.md), [consumer](https://docs.api7.ai/cloud/concepts/consumer.md) and [cluster](https://docs.api7.ai/cloud/concepts/cluster.md).

tip

Currently, API7 Cloud supports all plugins in Apache APISIX `2.15`.

Once users select an original Apache APISIX plugin, API7 Cloud will show a raw JSON editor, and users can edit the plugin configurations. Plugin schemas are the same as the ones defined by Apache APISIX.

For instance, here we configure the [API Breaker](https://apisix.apache.org/docs/apisix/plugins/api-breaker/) plugin.

![Configure API Breaker Plugin](https://static.api7.ai/2023/01/03/63b3dec5bfca0.png)

tip

For learning each original Apache APISIX plugin, please visit [Apache APISIX Website](https://apisix.apache.org/), and search the plugin name.

For most original Apache APISIX plugins, API7 Cloud doesn't implement the UI form for the following plugins own the UI form, and users don't have to configure them via the JSON editor.

* [CORS](https://docs.api7.ai/cloud/guides/security/cors.md) plugin
* [CSRF](https://docs.api7.ai/cloud/guides/security/csrf.md) plugin
* [Limit Count](https://docs.api7.ai/cloud/guides/traffic-management/limit-count.md) plugin
* [IP Restriction](https://docs.api7.ai/cloud/guides/security/ip-restriction.md) plugin
* [Proxy Rewrite](https://docs.api7.ai/cloud/guides/traffic-management/proxy-rewrite.md) plugin
* [Response Rewrite](https://docs.api7.ai/cloud/guides/traffic-management/response-rewrite.md) plugin
* [ACL](https://docs.api7.ai/cloud/guides/security/acl.md) plugin (this is a custom plugin developed by API7 Cloud)
* [Logging](https://docs.api7.ai/cloud/guides/observability/log-collection-with-http-logger.md) plugin
* [Authentication](https://docs.api7.ai/cloud/guides/traffic-management/authentication/basic-auth.md) plugin
* [Redirect](https://docs.api7.ai/cloud/guides/traffic-management/redirect.md) plugin
* [Request ID](https://docs.api7.ai/cloud/guides/product/request-id.md) plugin
* [Fault Injection](https://docs.api7.ai/cloud/guides/traffic-management/fault-injection.md) plugin
