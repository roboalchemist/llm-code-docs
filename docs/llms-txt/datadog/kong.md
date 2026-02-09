# Source: https://docs.datadoghq.com/tracing/trace_collection/proxy_setup/kong.md

---
title: Instrumenting Kong
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Tracing a Proxy > Instrumenting
  Kong
---

# Instrumenting Kong

Datadog APM is available for [Kong Gateway](https://docs.konghq.com/gateway/latest/) using the [kong-plugin-ddtrace](https://github.com/DataDog/kong-plugin-ddtrace) plugin.

## Installation{% #installation %}

The plugin is installed using `luarocks`.

```
luarocks install kong-plugin-ddtrace
```

Kong Gateway is not a bundled plugin, so it needs to be configured before it can be enabled. To enable it, include `bundled` and `ddtrace` in the `KONG_PLUGINS` environment variable, or set `plugins=bundled,ddtrace` in `/etc/kong/kong.conf`. Next, restart Kong Gateway to apply the change.

```gdscript3
# Set the KONG_PLUGINS environment variable or edit /etc/kong/kong.conf to enable the ddtrace plugin
export KONG_PLUGINS=bundled,ddtrace
kong restart
```

## Configuration{% #configuration %}

The plugin can be enabled globally or on specific services in Kong Gateway.

```
# Enabled globally
curl -i -X POST --url http://localhost:8001/plugins/ --data 'name=ddtrace'
# Enabled for specific service only
curl -i -X POST --url http://localhost:8001/services/example-service/plugins/ --data 'name=ddtrace'
```

Options are available for setting the service name, environment, and other features within the plugin. The example below sets the service name to `mycorp-internal-api` in the `prod` environment.

```
curl -i -X POST --url http://localhost:8001/plugins/ --data 'name=ddtrace' --data 'config.service_name=mycorp-internal-api' --data 'config.environment=prod'
```

More configuration options can be found on the [kong-plugin-ddtrace](https://github.com/DataDog/kong-plugin-ddtrace#configuration) plugin documentation.

## Further Reading{% #further-reading %}

- [Kong website](https://docs.konghq.com/gateway/latest/)
- [Datadog APM Plugin for Kong](https://github.com/DataDog/kong-plugin-ddtrace/)
