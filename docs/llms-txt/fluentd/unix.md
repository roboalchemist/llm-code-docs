# Source: https://docs.fluentd.org/input/unix.md

# Source: https://docs.fluentd.org/0.12/input/unix.md

# unix

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LWwh_8--1Ryw8aKcc_g%2F-LWNPQiUhR3aRmVTbAFG%2Funix.png?generation=1548280566526225\&alt=media)

The `in_unix` Input plugin enables Fluentd to retrieve records from the Unix Domain Socket. The wire protocol is the same as [in\_forward](https://docs.fluentd.org/0.12/input/forward), but the transport layer is different.

## Example Configuration

`in_unix` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type unix
  path /path/to/socket.sock
</source>
```

Please see the [Config File](https://docs.fluentd.org/0.12/configuration/config-file) article for the basic structure and syntax of the configuration file.

## Parameters

### type (required)

The value must be `unix`.

### path (required)

The path to your Unix Domain Socket.

### backlog

The backlog of Unix Domain Socket. The default is `1024`.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/0.12/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
