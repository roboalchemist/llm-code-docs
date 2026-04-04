# Source: https://docs.fluentd.org/input.md

# Source: https://docs.fluentd.org/0.12/input.md

# Input Plugins

Fluentd has 6 types of plugins: [Input](https://docs.fluentd.org/0.12/input), [Parser](https://docs.fluentd.org/0.12/parser), [Filter](https://docs.fluentd.org/0.12/filter), [Output](https://docs.fluentd.org/0.12/output), [Formatter](https://docs.fluentd.org/0.12/formatter) and [Buffer](https://docs.fluentd.org/0.12/buffer). This article gives an overview of Input Plugin.

## Overview

Input plugins extend Fluentd to retrieve and pull event logs from external sources. An input plugin typically creates a thread socket and a listen socket. It can also be written to periodically pull data from data sources.

## List of Input Plugins

* [in\_forward](https://docs.fluentd.org/0.12/input/forward)
* [in\_unix](https://docs.fluentd.org/0.12/input/unix)
* [in\_http](https://docs.fluentd.org/0.12/input/http)
* [in\_tail](https://docs.fluentd.org/0.12/input/tail)
* [in\_exec](https://docs.fluentd.org/0.12/input/exec)
* [in\_syslog](https://docs.fluentd.org/0.12/input/syslog)

## Other Input Plugins

Please refer to this list of available plugins to find out about other Input plugins.

* [Fluentd plugins](http://fluentd.org/plugin/)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
