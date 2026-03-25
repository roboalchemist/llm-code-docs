# Source: https://docs.fluentd.org/input/tcp.md

# Source: https://docs.fluentd.org/0.12/input/tcp.md

# tcp

![](https://3804023877-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LR7OsqPORtP86IQxs6E%2F-LX0aKuKEQ8l83KlUg5z%2F-LWNPNp8xOgIEt_P8cTJ%2Ftcp.png?generation=1548362554751314\&alt=media)

The `in_tcp` Input plugin enables Fluentd to accept TCP payload.

Don't use this plugin for receiving logs from client libraries. Use `in_forward` for such cases.

## Example Configuration

`in_tcp` is included in Fluentd's core. No additional installation process is required.

```
<source>
  @type tcp
  tag tcp.events # required
  format /^(?<field1>\d+):(?<field2>\w+)$/ # required
  port 20001 # optional. 5170 by default
  bind 0.0.0.0 # optional. 0.0.0.0 by default
  delimiter \n # optional. \n (newline) by default
</source>
```

Please see the [Config File](https://docs.fluentd.org/0.12/configuration/config-file) article for the basic structure and syntax of the configuration file.

We\\'ve observed the drastic performance improvements on Linux, with proper kernel parameter settings. If you have high-volume TCP traffic, please make sure to follow the instruction described at [Before Installing Fluentd](https://docs.fluentd.org/0.12/articles/before-install).

## Parameters

### type (required)

The value must be `tcp`.

### tag (required)

tag of output events.

### port

The port to listen to. Default Value = 5170

### bind

The bind address to listen to. Default Value = 0.0.0.0

### delimiter

The payload is read up to this character. By default, it is "\n".

### source\_hostname\_key

The field name of the client's hostname. If set the value, the client's hostname will be set to its key. The default is nil (no adding hostname).

If you set following configuration:

```
source_hostname_key client_host
```

then the client's hostname is set to `client_host` field.

```
{
    ...
    "foo": "bar",
    "client_host": "client.hostname.org"
}
```

### format (required)

The format of the TCP payload. Here is the example by regular expression.

```
format /^(?<field1>\d+):(?<field2>\w+)$/
```

If you execute following command:

```
$ echo '123456:awesome' | netcat 0.0.0.0 5170
```

then got parsed result like below:

```
{"field1":"123456","field2":"awesome}
```

`in_tcp` uses parser plugin to parse the payload. See [parser article](https://docs.fluentd.org/0.12/parser) for more detail.

#### log\_level option

The `log_level` option allows the user to set different levels of logging for each plugin. The supported log levels are: `fatal`, `error`, `warn`, `info`, `debug`, and `trace`.

Please see the [logging article](https://docs.fluentd.org/0.12/deployment/logging) for further details.

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
