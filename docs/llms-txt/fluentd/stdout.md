# Source: https://docs.fluentd.org/formatter/stdout.md

# Source: https://docs.fluentd.org/filter/stdout.md

# Source: https://docs.fluentd.org/output/stdout.md

# Source: https://docs.fluentd.org/0.12/filter/stdout.md

# Source: https://docs.fluentd.org/0.12/output/stdout.md

# stdout

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPOdBSQRXROLDre1M%2Fstdout.png?generation=1548362554725017\&alt=media)

The `stdout` output plugin prints events to stdout (or logs if launched with daemon mode). This output plugin is useful for debugging purposes.

## Example Configuration

`out_stdout` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type stdout
</match>
```

Please see the [Config File](https://docs.fluentd.org/0.12/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `stdout`.

### output\_type

Output format. The following formats are supported:

* json
* hash (Ruby's hash)

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/0.12/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
