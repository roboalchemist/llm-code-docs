# Source: https://docs.fluentd.org/service_discovery.md

# Service Discovery Plugins

Fluentd has nine (9) types of plugins:

* [Input](https://docs.fluentd.org/input)
* [Parser](https://docs.fluentd.org/parser)
* [Filter](https://docs.fluentd.org/filter)
* [Output](https://docs.fluentd.org/output)
* [Formatter](https://docs.fluentd.org/formatter)
* [Storage](https://docs.fluentd.org/storage)
* [Service Discovery](https://docs.fluentd.org/service_discovery)
* [Buffer](https://docs.fluentd.org/buffer)
* [Metrics](https://docs.fluentd.org/metrics)

This article gives an overview of the Service Discovery Plugin.

## Overview

Some plugins support `<service_discovery>` (e.g. [`out_forward`](https://docs.fluentd.org/output/forward)). Sometimes, the service discovery for an output plugin does not meet one's needs. Fluentd has a pluggable system called Service Discovery that lets the user extend and reuse custom output service discovery.

## How To Use

Here is a simple example to update target by reading file (`/etc/fluentd/sd.yaml`) with `out_forward` and `service_discovery`:

```
<source>
  @type forward

  <service_discovery>
    @type file
    path "/etc/fluentd/sd.yaml"
  </service_discovery>
</source>
```

## List of Built-in Service Discovery

* [`static`](https://docs.fluentd.org/service_discovery/static)
* [`file`](https://docs.fluentd.org/service_discovery/file)
* [`srv`](https://docs.fluentd.org/service_discovery/srv)

## List of Core Output Plugins with Service Discovery support

* [`out_forward`](https://docs.fluentd.org/output/forward)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is an open-source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
