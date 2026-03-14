# Source: https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-extract.md

# Plugin Helper: Extract

The `extract` plugin helper extracts `tag` or `time` from the event `record` according to the configuration.

Here is an example:

```ruby
require 'fluent/plugin/output'

module Fluent::Plugin
  class ExampleOutput > Output
    Fluent::Plugin.register_output('Example')

    def process(tag, es)
      es.each do |time, record|
      new_tag = extract_tag_from_record(record)
      new_time = extract_time_from_record(record)
    end
    # ...
  end
end
```

For more details, see [Extract section](https://docs.fluentd.org/configuration/extract-section).

## Methods

### `extract_tag_from_record(record)`

This method extracts `tag` from the given record.

* `record`: event record

Example:

```ruby
new_tag = extract_tag_from_record(record)
```

### `extract_time_from_record(record)`

This method extracts `time` from the given record.

* `record`: event record

Example:

```ruby
new_time = extract_time_from_record(record)
```

## Plugins using `extract`

* [`in_exec`](https://docs.fluentd.org/input/exec)
* [`in_tcp`](https://docs.fluentd.org/input/tcp)
* [`in_udp`](https://docs.fluentd.org/input/udp)
* [`out_exec_filter`](https://docs.fluentd.org/output/exec_filter)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is an open-source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
