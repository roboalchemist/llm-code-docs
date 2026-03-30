# Source: https://docs.fluentd.org/output/copy.md

# Source: https://docs.fluentd.org/0.12/output/copy.md

# copy

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LXN2biv5zzn1JBo8u1T%2F-LWNPNcdtuUq_M7zUmC9%2Fcopy.png?generation=1548739338211471\&alt=media)

The `copy` output plugin copies events to multiple outputs.

## Example Configuration

`out_copy` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type copy
  <store>
    @type file
    path /var/log/fluent/myapp1
    ...
  </store>
  <store>
    ...
  </store>
  <store>
    ...
  </store>
</match>
```

Please see the [Config File](https://docs.fluentd.org/0.12/configuration/config-file) article for the basic structure and syntax of the configuration file.

Here is an example set up to send events to both a local file under `/var/log/fluent/myapp` and the collection `fluentd.test` in a local MongoDB instance (Please see the [out\_file](https://docs.fluentd.org/0.12/output/file) and [out\_mongo](https://docs.fluentd.org/0.12/output/mongo) articles for more details about the respective plugins.)

```
<match myevent.file_and_mongo>
  @type copy
  <store>
    @type file
    path /var/log/fluent/myapp
    time_slice_format %Y%m%d
    time_slice_wait 10m
    time_format %Y%m%dT%H%M%S%z
    compress gzip
    utc
  </store>
  <store>
    @type mongo
    host fluentd
    port 27017
    database fluentd
    collection test
  </store>
</match>
```

## Parameters

### type (required)

The value must be `copy`.

### deep\_copy

`out_copy` shares a record between `store` plugins by default.

When `deep_copy` is true, `out_copy` passes different record to each `store` plugin.

### \<store> (at least one required)

Specifies the storage destinations. The format is the same as the \ directive.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/0.12/deployment/logging) for further details.

## FAQ

### How to ignore each error in \\\\?

If one `store` raises an error, it affects other `<store>`. If you want to ignore an exception from less important `<store>`, you can use 3rd party [out\_copy\_ex](https://github.com/sonots/fluent-plugin-copy_ex) instead.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
