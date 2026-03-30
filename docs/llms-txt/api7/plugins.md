# Source: https://docs.api7.ai/enterprise-whitepaper/features/plugins.md

# Source: https://docs.api7.ai/enterprise/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.8.x/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.7.x/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.6.x/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.5.x/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.4.x/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/plugins.md

# Source: https://docs.api7.ai/apisix/key-concepts/plugins.md

# Source: https://docs.api7.ai/enterprise/3.3.x/key-concepts/plugins.md

# Source: https://docs.api7.ai/apisix/key-concepts/plugins.md

# Plugins

In this document, you will learn the basic concept of plugins in APISIX and why you need plugins. You will be introduced to a few relevant concepts, including plugins enablement, plugins configuration files precedence, plugins execution filter and order, as well as plugins development.

Explore additional resources at the end of the document for more information on related topics.

## Overview[â](#overview "Direct link to Overview")

APISIX *plugins* extend APISIX's functionalities to meet organization or user-specific requirements in traffic management, observability, security, request/response transformation, serverless computing, and more.

APISIX offers many existing plugins that can be customized and orchestrated to suit your needs. These plugins can be globally enabled to be triggered on every incoming request, or locally bound to other objects, such as [routes](https://docs.api7.ai/apisix/key-concepts/routes.md), [services](https://docs.api7.ai/apisix/key-concepts/services.md), [consumers](https://docs.api7.ai/apisix/key-concepts/consumers.md), [consumer groups](https://docs.api7.ai/apisix/key-concepts/consumer-groups.md), or [plugin configs](https://docs.api7.ai/apisix/key-concepts/plugin-configs.md). See [plugin hub](https://docs.api7.ai/hub.md) for an inventory of plugins and their usage.

If existing APISIX plugins do not meet your needs, you can also write your own plugins in Lua or other languages such as Java, Python, Go, and Wasm.

## Plugins Installation[â](#plugins-installation "Direct link to Plugins Installation")

By default, most APISIX plugins are [installed](https://github.com/apache/apisix/blob/master/apisix/cli/config.lua):

apisix/cli/config.lua

```
local _M = {
  ...
  plugins = {
    "real-ip",
    "ai",
    "client-control",
    "proxy-control",
    "request-id",
    "zipkin",
    "ext-plugin-pre-req",
    "fault-injection",
    "mocking",
    "serverless-pre-function",
    ...
  },
  ...
}
```

If you would like to make adjustments to plugins installation, add the customized `plugins` configuration to `config.yaml`. For example:

```
plugins:
  - real-ip
  - ai
  - client-control
  - proxy-control
  - request-id
  - zipkin     
  - ext-plugin-pre-req
  - fault-injection
  # - mocking                 # do not install
  - serverless-pre-function
  ...                         # other plugins
```

See `config.yaml.example`(<https://github.com/apache/apisix/blob/master/conf/config.yaml.example>) for a complete configuration reference.

[Reload APISIX](https://docs.api7.ai/apisix/reference/apisix-cli.md#apisix-reload) for changes to take effect.

## Plugins Execution Lifecycle[â](#plugins-execution-lifecycle "Direct link to Plugins Execution Lifecycle")

An installed plugin is first initialized. The configuration of the plugin is then checked against the defined [JSON Schema](https://json-schema.org) to make sure the plugin configuration schema is correct.

When a request goes through APISIX, the plugin's corresponding methods are executed in one or more of the following phases: `rewrite`, `access`, `before_proxy`, `header_filter`, `body_filter`, and `log`. These phases are largely influenced by the [OpenResty directives](https://openresty-reference.readthedocs.io/en/latest/Directives/).

<br />

![Routes Diagram](https://static.api7.ai/uploads/2023/03/09/ZsH5C8Og_plugins-phases.png)

<br />

To learn more about phases for your custom plugins development, see the [plugin development how-to guide](https://docs.api7.ai/apisix/how-to-guide/custom-plugins/create-plugin-in-lua.md).

## Plugins Execution Order[â](#plugins-execution-order "Direct link to Plugins Execution Order")

In general, plugins are executed in the following order:

1. Plugins in [global rules](https://docs.api7.ai/apisix/key-concepts/plugin-global-rules.md)

   1. plugins in rewrite phase
   2. plugins in access phase

2. Plugins bound to other objects

   1. plugins in rewrite phase
   2. plugins in access phase

Within each [phase](#plugins-execution-lifecycle), you can optionally define a new priority value in the `_meta.priority` attribute of the plugin, which takes precedence over the default plugin priority during execution. Plugins with higher priority values are executed first. See plugin [common configurations](https://docs.api7.ai/apisix/reference/plugin-common-configurations.md#_metapriority) for an example.

## Plugins Merging Precedence[â](#plugins-merging-precedence "Direct link to Plugins Merging Precedence")

When the same plugin is configured both globally in a global rule and locally in an object (e.g. a route), both plugin instances are executed sequentially.

However, if the same plugin is configured locally on multiple objects, such as on [routes](https://docs.api7.ai/apisix/key-concepts/routes.md), [services](https://docs.api7.ai/apisix/key-concepts/services.md), [consumers](https://docs.api7.ai/apisix/key-concepts/consumers.md), [consumer groups](https://docs.api7.ai/apisix/key-concepts/consumer-groups.md), or [plugin configs](https://docs.api7.ai/apisix/key-concepts/plugin-configs.md), only one copy of configuration is used as each non-global plugin is only executed once. This is because during execution, plugins configured in these objects are merged with respect to a specific order of precedence:

`Consumer` > `Consumer Group` > `Route` > `Plugin Config` > `Service`

such that if the same plugin has different configurations in different objects, the plugin configuration with the highest order of precedence during merging will be used.

## Plugins Execution Filter[â](#plugins-execution-filter "Direct link to Plugins Execution Filter")

By default, all plugins are triggered by incoming requests that match the configured rules in routes. However, in some cases, you may want more granular control over plugins execution; that is, conditionally determine which plugins are triggered for requests.

APISIX allows for dynamic control over plugin execution by applying the `_meta.filter` configuration to the plugins. The configuration supports the evaluation of a wide range of [built-in variables](https://docs.api7.ai/apisix/reference/built-in-variables.md) and [APISIX expressions](https://docs.api7.ai/apisix/reference/apisix-expressions.md).

See plugin [common configurations](https://docs.api7.ai/apisix/reference/plugin-common-configurations.md#_metafilter) for an example.

## Plugins Development[â](#plugins-development "Direct link to Plugins Development")

APISIX supports plugin extension in multiple languages, including Lua, Java, Python, Go, and Wasm. Plugins run in three major ways:

* Lua plugins run natively in APISIX.
* Java, Python, and Go plugins run in their corresponding APISIX plugin runners, communicating over [remote procedure calls (RPCs)](https://apisix.apache.org/docs/apisix/internal/plugin-runner/).
* Wasm plugins run in the APISIX Wasm plugin runtime.

To learn more about developing plugins, see [create plugin in Lua](https://docs.api7.ai/apisix/how-to-guide/custom-plugins/create-plugin-in-lua.md).

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Getting Started - [Configure Rate Limiting](https://docs.api7.ai/apisix/getting-started/rate-limiting.md)
* Reference - [Plugin Common Configurations](https://docs.api7.ai/apisix/reference/plugin-common-configurations.md)
* [Plugin Hub](https://docs.api7.ai/hub.md)
* [Create Plugin in Lua](https://docs.api7.ai/apisix/how-to-guide/custom-plugins/create-plugin-in-lua.md)
