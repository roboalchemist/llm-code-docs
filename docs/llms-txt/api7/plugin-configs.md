# Source: https://docs.api7.ai/apisix/key-concepts/plugin-configs.md

# Plugin Configs

In this document, you will learn the basic concept of plugin configs in APISIX and why you may need them.

Explore additional resources at the end of the document for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

In APISIX, a *plugin config* object extracts common plugin configurations, eliminating repetitive plugin configurations on [routes](https://docs.api7.ai/apisix/key-concepts/routes.md). This makes API management more streamlined and efficient. To apply the configured [plugins](https://docs.api7.ai/apisix/key-concepts/plugins.md) on a plugin config object in routes, you can simply refer to the plugin config ID in route configurations.

The following diagram illustrates the concept of plugin configs with two routes pointing to two different backend systems - one for orders and the other one for deliveries. A plugin config object is used in the APISIX configuration, such that `limit-count` and `proxy-rewrite` plugins are configured in a centralized place while being utilized by multiple routes:

<br />

![plugin configs diagram with two routes and one plugin config object](https://static.api7.ai/uploads/2023/03/22/0VcbwzBw_plugin_configs.svg)

<br />

In addition to shared plugin configs, you can still configure route-specific plugins separately on routes. See [plugins configuration precedence](https://docs.api7.ai/apisix/key-concepts/plugins.md#plugins-configuration-precedence) to learn more about how APISIX prioritizes configurations when the same plugin is configured in multiple objects.

## Additional Resource(s)[â](#additional-resources "Direct link to Additional Resource(s)")

* Key Concepts - [Plugins](https://docs.api7.ai/apisix/key-concepts/plugins.md)
* Admin API - [Plugin Configs](https://docs.api7.ai/apisix/reference/admin-api/.md#tag/Plugin-Config)
* [Plugin Hub](https://docs.api7.ai/hub.md)
