# Source: https://docs.fluentd.org/formatter.md

# Source: https://docs.fluentd.org/0.12/formatter.md

# Formatter Plugins

Fluentd has 6 types of plugins: [Input](https://docs.fluentd.org/0.12/input), [Parser](https://docs.fluentd.org/0.12/parser), [Filter](https://docs.fluentd.org/0.12/filter), [Output](https://docs.fluentd.org/0.12/output), [Formatter](https://docs.fluentd.org/0.12/formatter) and [Buffer](https://docs.fluentd.org/0.12/buffer). This article gives an overview of Formatter Plugin.

## Overview

Sometimes, the output format for an output plugin does not meet one's needs. Fluentd has a pluggable system called Text Formatter that lets the user extend and re-use custom output formats.

## How To Use

For an output plugin that supports Text Formatter, the `format` parameter can be used to change the output format.

For example, by default, [out\_file](https://docs.fluentd.org/0.12/output/file) plugin outputs data as

```
2014-08-25 00:00:00 +0000<TAB>foo.bar<TAB>{"k1":"v1", "k2":"v2"}
```

However, if you set `format json` like this

```
<match foo.bar>
  @type file
  path /path/to/file
  format json
</match>
```

The output changes to

```
{"time": "2014-08-25 00:00:00 +0000", "tag":"foo.bar", "k1:"v1", "k2":"v2"}
```

i.e., each line is a single JSON object with "time" and "tag fields to retain the event's timestamp and tag.

See [this section](https://docs.fluentd.org/0.12/developer/plugin-development#text-formatter-plugins) to learn how to develop a custom formatter.

## List of Built-in Formatters

* [out\_file](https://docs.fluentd.org/0.12/formatter/out_file)
* [json](https://docs.fluentd.org/0.12/formatter/json)
* [ltsv](https://docs.fluentd.org/0.12/formatter/ltsv)
* [csv](https://docs.fluentd.org/0.12/formatter/csv)
* [msgpack](https://docs.fluentd.org/0.12/formatter/msgpack)
* [hash](https://docs.fluentd.org/0.12/formatter/hash)
* [single\_value](https://docs.fluentd.org/0.12/formatter/single_value)

## List of Output Plugins with Text Formatter Support

* [out\_file](https://docs.fluentd.org/0.12/output/file)
* [out\_s3](https://docs.fluentd.org/0.12/output/s3)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is a open source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
