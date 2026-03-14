# Source: https://docs.fluentd.org/input/sample.md

# sample

![](https://1982584918-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LR7OsqPORtP86IQxs6E-694727794%2Fuploads%2Fgit-blob-07d1252b5465c09c488efddaa87ae1a3d9986f0a%2Fdummy.png?alt=media)

The `in_sample` input plugin generates sample events. It is useful for testing, debugging, benchmarking and getting started with Fluentd.

It is included in Fluentd's core.

This plugin is the renamed version of `in_dummy`.

## Example Configuration

```
<source>
  @type sample
  sample {"hello":"world"}
  tag sample
</source>

# If you use fluentd v1.11.1 or earlier, use following configuration
<source>
  @type dummy
  dummy {"hello":"world"}
  tag dummy
</source>
```

Please see the [Config File](https://docs.fluentd.org/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Plugin Helpers

* [`thread`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-thread)
* [`storage`](https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-storage)
* See also: [Input Plugin Overview](https://docs.fluentd.org/input)

## Parameters

See [Common Parameters](https://docs.fluentd.org/configuration/plugin-common-parameters).

{% hint style="info" %}
NOTE: sample plugin doesn't support specific [Parse Parameters](https://docs.fluentd.org/configuration/parse-section) in `<parse>` section.
{% endhint %}

### `@type`

The value must be `sample`.

If you use fluentd v1.11.1 or earlier, use `dummy`.

### `tag`

| type   | default | version |
| ------ | ------- | ------- |
| string | Nothing | 0.14.0  |

The value is the tag assigned to the generated events.

### `size`

| type    | default | version |
| ------- | ------- | ------- |
| integer | 1       | 0.14.4  |

The number of events in the event stream of each emit.

### `rate`

| type    | default | version |
| ------- | ------- | ------- |
| integer | 1       | 0.14.0  |

It configures how many events to generate per second.

### `auto_increment_key`

| type   | default | version |
| ------ | ------- | ------- |
| string | nil     | 0.14.0  |

If specified, each generated event has an auto-incremented key field.

For example, with `auto_increment_key foo_key`, the first couple of events look like:

```
2014-12-14 23:23:38 +0000 test: {"message":"sample","foo_key":0}
2014-12-14 23:23:38 +0000 test: {"message":"sample","foo_key":1}
2014-12-14 23:23:38 +0000 test: {"message":"sample","foo_key":2}
```

### `suspend`

| type | default | version |
| ---- | ------- | ------- |
| bool | false   | 0.14.2  |

This parameter is removed since v1.10.0. This feature is automatically handled in the core.

### `sample`

| type   | default                  | version |
| ------ | ------------------------ | ------- |
| string | `[{"message":"sample"}]` | 0.14.0  |

The sample data to be generated. It should be either an array of JSON hashes or a single JSON hash. If it is an array of JSON hashes, the hashes in the array are cycled through in order.

If you use fluentd v1.11.1 or earlier, use `dummy`.

### `reuse_record`

| type | default | version |
| ---- | ------- | ------- |
| bool | false   | 1.17.1  |

If specified, it reuses the previously generated sample data. This is the default behavior in v1.17.0 or older version of Fluentd.

Since v1.17.1, the default behavior was changed to copy sample data by default to avoid the impact of destructive changes by subsequent plugins.

The new default behavior (`reuse_record false`) increases the load when generating large amounts of sample data. You can use this new parameter to have the same performance as before with `reuse_record`.

Note that there is one exception not to reuse the sample data even though `reuse_record` is specified. If `auto_increment_key` was specified, `reuse_record` will be ignored.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is an open-source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
