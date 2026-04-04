# Source: https://docs.fluentd.org/storage.md

# Storage Plugins

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

This article gives an overview of Storage Plugin.

## Overview

Sometimes, the input/filter/output plugin needs to save its internal state in memory, storage, or key-value store. Fluentd has a pluggable system called Storage that lets a plugin store and reuse its internal state as key-value pairs.

## How To Use

For an input, an output, and filter plugin that supports Storage, the `<storage>` directive can be used to store key-value pair into a key-value store such as a JSON file, MongoDB, Redis, etc.

Here is an example with `in_sample`:

```
<source>
  @type sample
  tag docs.fluentd.storage
  <storage awesome_path>
    @type my_custom_storage
  </storage>
</source>
```

## List of Built-in Storage

* [`local`](https://docs.fluentd.org/storage/local)

## List of Core Plugins with Storage support

* [`in_sample`](https://docs.fluentd.org/input/sample)

## List of 3rd party storage plugins

NOTE: This 3rd party storage plugin list does not fully covers all of them.

* [fluent-plugin-storage-leveldb](https://github.com/cosmo0920/fluent-plugin-storage-leveldb)
* [fluent-plugin-storage-memcached](https://github.com/cosmo0920/fluent-plugin-storage-memcached)
* [fluent-plugin-storage-mongo](https://github.com/cosmo0920/fluent-plugin-storage-mongo)
* [fluent-plugin-storage-redis](https://github.com/cosmo0920/fluent-plugin-storage-redis)

## List of 3rd party Plugins with Storage support

NOTE: This 3rd party plugin list does not fully covers all of them.

* [fluent-plugin-systemd](https://github.com/fluent-plugin-systemd/fluent-plugin-systemd)
* [fluent-plugin-windows-eventlog](https://github.com/fluent/fluent-plugin-windows-eventlog)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is an open-source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
