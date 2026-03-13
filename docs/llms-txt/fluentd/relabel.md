# Source: https://docs.fluentd.org/output/relabel.md

# Source: https://docs.fluentd.org/0.12/output/relabel.md

# relabel

The `relabel` output plugin re-labels events.

## Example Configuration

`out_relabel` is included in Fluentd's core. No additional installation process is required.

```
<match pattern>
  @type relabel
  @label @foo
</match>

<label @foo>
  <match patter>
    ...
  </match>
</label>
```

The above example puts a label `@foo` to matched events, and the `label` directive can take care of these events.

FYI: All of input and output plugins also have `@label` parameter provided by Fluentd core. The `relabel` plugin is a plugin which actually does nothing, but supports only `@label` parameter.

## Parameters

### type (required)

The value must be `relabel`.

### label

The label.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/0.12/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
