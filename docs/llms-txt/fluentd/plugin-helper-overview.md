# Source: https://docs.fluentd.org/plugin-helper-overview.md

# Plugin Helper API

Fluentd provides plugin helpers to encapsulate and make commonly implemented features available such as timer, threading, formatting, parsing, ensuring configuration syntax's backward compatibility, etc.

## How To Use

To use plugin helpers, call `helpers(*snake_case_symbols)` method to make them available.

Example:

```ruby
helpers :timer, :storage, :compat_parameters
```

It will include `Timer`, `Storage`. and `CompatParameters` plugin helpers.

## Built-in Plugin Helpers

* [`child_process`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-child_process)
* [`compat_parameters`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-compat_parameters)
* [`event_emitter`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-event_emitter)
* [`event_loop`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-event_loop)
* [`extract`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-extract)
* [`formatter`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-formatter)
* [`inject`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-inject)
* [`metrics`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-metrics)
* [`parser`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-parser)
* [`record_accessor`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-record_accessor)
* [`server`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-server)
* [`socket`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-socket)
* [`storage`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-storage)
* [`thread`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-thread)
* [`timer`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-timer)
* [`http_server`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-http_server)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is an open-source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
