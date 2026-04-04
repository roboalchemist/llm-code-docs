# Source: https://docs.fluentd.org/plugin-helper-overview/api-plugin-helper-formatter.md

# Plugin Helper: Formatter

The `formatter` plugin helper manages the lifecycle of the formatter plugin.

Here is an example:

```ruby
require 'fluent/plugin/output'

module Fluent::Plugin
  class ExampleOutput < Output
    Fluent::Plugin.register_output('example', self)

    # 1. Load formatter helper
    helpers :formatter

    # Omit `shutdown` and other plugin APIs

    def configure(conf)
      super

      # 2. Call `formatter_create` to create object
      @formatter = formatter_create(usage: 'awesome_formatter')
    end

    def format(tag, time, record)
      # 3. Call `format` method to format `record`
      @formatter.format(tag, time, record)
    end
  end
end
```

For more details, see the following articles:

* [Formatter Plugin Overview](https://docs.fluentd.org/formatter)
* [Writing Formatter Plugins](https://docs.fluentd.org/plugin-development/api-plugin-formatter)
* [Format Section](https://docs.fluentd.org/configuration/format-section)

## Methods

### `formatter_create(usage: "", type: nil, conf: nil, default_type: nil)`

* `usage`: unique name required for multiple formatters
* `type`: formatter type
* `conf`: formatter plugin configuration
* `default_type`: default formatter type

**Examples**:

```ruby
def configure(conf)
  super
  # Create formatter plugin instance using <format> section in `fluent.conf` during configure phase
  @formatter = formatter_create
end

def format(tag, time, record)
  @formatter.format(tag, time, record)
end
```

JSON formatter example:

```ruby
# Create JSON formatter
def configure(conf)
  super
  @json_formatter = formatter_create(usage: 'formatter_in_example_json', type: 'json')
end

def format(tag, time, record)
  @json_formatter.format(tag, time, record)
end
```

MsgPack formatter example:

```ruby
# Create MsgPack formatter
def configure(conf)
  super
  @msgpack_formatter = formatter_create(usage: 'formatter_in_example_msgpack', type: 'msgpack')
end

def format(tag, time, record)
  @msgpack_formatter.format(tag, time, record)
end
```

## Plugins using `formatter`

* [`filter_stdout`](https://docs.fluentd.org/filter/stdout)
* [`out_stdout`](https://docs.fluentd.org/output/stdout)
* [`out_exec`](https://docs.fluentd.org/output/exec)
* [`out_exec_filter`](https://docs.fluentd.org/output/exec_filter)
* [`out_file`](https://docs.fluentd.org/output/file)
* [`out_s3`](https://docs.fluentd.org/output/s3)

If this article is incorrect or outdated, or omits critical information, please [let us know](https://github.com/fluent/fluentd-docs-gitbook/issues?state=open). [Fluentd](http://www.fluentd.org/) is an open-source project under [Cloud Native Computing Foundation (CNCF)](https://cncf.io/). All components are available under the Apache 2 License.
