# Source: https://docs.airbyte.com/platform/connector-development/config-based/advanced-topics/string-interpolation.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/config-based/advanced-topics/string-interpolation.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/config-based/advanced-topics/string-interpolation.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/config-based/advanced-topics/string-interpolation.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/config-based/advanced-topics/string-interpolation.md

# String Interpolation

Copy Page

String values can be evaluated as Jinja2 templates.

If the input string is a raw string, the interpolated string will be the same. `"hello world" -> "hello world"`

The engine will evaluate the content passed within `{{...}}`, interpolating the keys from context-specific arguments. The "parameters" keyword [see ($parameters)](/platform/1.6/connector-development/config-based/advanced-topics/parameters.md) can be referenced.

For example, some\_object.inner\_object.key will evaluate to "Hello airbyte" at runtime.

```
some_object:
  $parameters:
    name: "airbyte"
  inner_object:
    key: "Hello {{ parameters.name }}"
```

Some components also pass in additional arguments to the context. This is the case for the [record selector](/platform/1.6/connector-development/config-based/understanding-the-yaml-file/record-selector.md), which passes in an additional `response` argument.

Both dot notation and bracket notations (with single quotes ( `'`)) are interchangeable. This means that both these string templates will evaluate to the same string:

1. `"{{ parameters.name }}"`
2. `"{{ parameters['name'] }}"`

In addition to passing additional values through the $parameters argument, macros can be called from within the string interpolation. For example, `"{{ max(2, 3) }}" -> 3`

The macros and variables available in all possible contexts are documented in the [YAML Reference](/platform/1.6/connector-development/config-based/understanding-the-yaml-file/reference.md#variables).

Additional information on jinja templating can be found at <https://jinja.palletsprojects.com/en/3.1.x/templates/#>
