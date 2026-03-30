# Source: https://docs.fluentd.org/configuration/service_discovery-section.md

# Config: Service Discovery Section

Some of the Fluentd plugins support the `<service_discovery>` section to set the target nodes dynamically.

## Service Discovery Section Overview

The **`service_discovery`** section comes under `<match>`.

```
<match tag.*>
  @type forward
  # ...
  <service_discovery>
    # ...
  </service_discovery>
</match>
```

## Service Discovery Plugin Type

The `@type` parameter of `<service_discovery>` section specifies the type of the plugin. Fluentd core bundles [some useful service discovery plugins](https://docs.fluentd.org/service_discovery) e.g. `file`.

```
<service_discovery>
  @type file
  # ...
</service_discovery>
```

Here's the list of built-in service discovery plugins:

* [`static`](https://docs.fluentd.org/service_discovery/static)
* [`file`](https://docs.fluentd.org/service_discovery/file)
* [`srv`](https://docs.fluentd.org/service_discovery/srv)

For more details, see plugins documentation.

### `@type`

The `@type` parameter specifies the type of service discovery plugin.

```
<service_discovery>
  @type static
  # ...
</service_discovery>
```

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is an open-source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
