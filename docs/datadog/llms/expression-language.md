# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/expression-language.md

---
title: Dynamic Instrumentation Expression Language
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Dynamic Instrumentation > Dynamic
  Instrumentation Expression Language
---

# Dynamic Instrumentation Expression Language

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

The Dynamic Instrumentation Expression Language helps you formulate log probe message templates, metric probe expressions, span tag values, and probe conditions. It borrows syntax elements from common programming languages, but also has its own unique rules. The language lets you access local variables, method parameters, and nested fields within objects, and it supports the use of comparison and logical operators.

Examples:

- `someVar.someField`
- `request.headers["Host"]`
- `any(post.tags, {@it == "debugger"})`
- `@duration > 10 && len(p.data) < 100`

{% image
   source="https://datadog-docs.imgix.net/images/tracing/dynamic_instrumentation/expressions.6ea538da5fe9562f79d7cc2a9771e795.png?auto=format"
   alt="Example log probe with expressions" /%}

Generally, the Expression Language supports:

- Accessing local variables, method parameters, and deeply nested fields and attributes within objects.
- Using comparison operators (`<`, `>`, `>=`, `<=`, `==`, `!=`, `instanceof`) to compare variables, fields, and constants in your conditions, for example: `localVar1.field1.field2 != 15`.
- Using logical operators (`&&`, `||`, and `!` or `not(...)`) to build complex Boolean conditions, for example: `!isEmpty(user.email) && not(contains(user.name, "abc"))`.
- Using the `null` literal (which is automatically translated to `None` in Python and `nil` in Ruby).

It does **not** support:

- Calling methods. Dynamic Instrumentation does not permit executing code that may have side effects. However, you can access `private` fields directly.
- Other native programming language syntax beyond what is described on this page.

Try [autocomplete and search (in Preview)][6] for an improved user experience using the Expression Language.

## Applications{% #applications %}

Expressions can be used to produce metrics or logs, and as conditions to emit filtered data.

For example, you can create a histogram from the length of a string using `len(data)` as the metric expression. Metric expressions must evaluate to a number.

Logs can be emitted using templates. In log templates and tag values, expressions are delimited from the static parts of the template with brackets, for example: `User name is {user.name}`. Log template expressions can evaluate to any value.

Probe conditions must evaluate to a Boolean, for example:

- `startsWith(user.name, "abc")`
- `len(str) > 20`
- `a == b`

## Contextual variables{% #contextual-variables %}

The Expression Language provides contextual variables for different instrumentation scenarios: method instrumentation variables (`@return`, `@duration`, `@exception`) are available only when instrumenting entire methods, while collection and dictionary variables (`@it`, `@key`, `@value`) are only available within predicate expressions for filtering and transforming collections.

| Keyword      | Description                                                                                                     |
| ------------ | --------------------------------------------------------------------------------------------------------------- |
| `@return`    | Provides access to the method return value.                                                                     |
| `@duration`  | Provides access to the method call execution duration, as a floating-point value in milliseconds.               |
| `@exception` | Provides access to the exception thrown within the method (only available if an uncaught exception exists).     |
| `@it`        | Provides access to the current element during collection iteration. Used in predicates for list operations.     |
| `@key`       | Provides access to the current key during dictionary iteration. Used in predicates for dictionary operations.   |
| `@value`     | Provides access to the current value during dictionary iteration. Used in predicates for dictionary operations. |

## General operations{% #general-operations %}

The following examples assume a variable named `myString` with value `Hello, world!`:

| Operation                                    | Description                                                                                                                                                                           | Example                                                       |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `isDefined(var)`                             | Checks whether a variable is defined. Returns `true` if the variable exists in the current scope, `false` otherwise. Useful for conditional logic when a variable may not be present. | {% interactive-demo for="â isDefined(myString)" /%}           |
| `len(value_src)`                             | Gets the string length.                                                                                                                                                               | {% interactive-demo for="â len(myString)" /%}                 |
| `isEmpty(value_src)`                         | Checks whether the string is empty. Equivalent to `len(value_src) == 0`.                                                                                                              | {% interactive-demo for="â isEmpty(myString)" /%}             |
| `substring(value_src, startIndex, endIndex)` | Gets a substring.                                                                                                                                                                     | {% interactive-demo for="â substring(myString, 0, 2)" /%}     |
| `startsWith(value_src, string_literal)`      | Checks whether a string starts with the given string literal.                                                                                                                         | {% interactive-demo for="â startsWith(myString, \"He\")" /%}  |
| `endsWith(value_src, string_literal)`        | Checks whether the string ends with the given string literal.                                                                                                                         | {% interactive-demo for="â endsWith(myString, \"rdl!\")" /%}  |
| `contains(value_src, string_literal)`        | Checks whether the string contains the string literal, or whether a collection contains an element.                                                                                   | {% interactive-demo for="â contains(myString, \"ll\")" /%}    |
| `matches(value_src, string_literal)`         | Checks whether the string matches the regular expression provided as a string literal.                                                                                                | {% interactive-demo for="â matches(myString, \"^H.*!$\")" /%} |

## Collection operations{% #collection-operations %}

When working with collections (lists, maps, and so on), you can use contextual variables in predicates to access elements during iteration. See the Contextual variables section for details.

The following examples assume a variable named `mySequence` with value `[1,2,3,4]` and `myMap` with value `{"a": 1, "b": 2, "c": 3}`:

| Operation                        | Description                                                                                                                                                                                                                                                                                                                           | Example                                                                                                                       |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `len(value_src)`                 | Gets the collection size.                                                                                                                                                                                                                                                                                                             | {% interactive-demo for="â len(mySequence)" /%}

  {% interactive-demo for="â len(myMap)" /%}                                |
| `isEmpty(value_src)`             | Checks whether the collection is empty. Equivalent to `len(value_src) == 0`.                                                                                                                                                                                                                                                          | {% interactive-demo for="â isEmpty(mySequence)" /%}

  {% interactive-demo for="â isEmpty(myMap)" /%}                        |
| `[ i ]`, `[ key ]`               | For sequential containers returns the `i`-th item in the collection (where `i` must be an integer). For dictionaries, returns the value that corresponds to the `key` (where `key` must match the key type of the dictionary). If the item does not exist, the expression yields an error or returns null, depending on the language. | {% interactive-demo for="â mySequence[3]" /%}

  {% interactive-demo for="â myMap[\"b\"]" /%}                                |
| `any(value_src, {predicate})`    | Checks if there is at least one element in the collection that satisfies the given predicate. The current element is accessed with the `@it` reference for sequential containers, and with `@key`, `@value` for dictionaries.                                                                                                         | {% interactive-demo for="â any(mySequence, {@it > 2})" /%}

  {% interactive-demo for="â any(myMap, {@value > 2})" /%}       |
| `all(value_src, {predicate})`    | Checks whether every element in a collection satisfies the specified predicate. The current element is accessed with the `@it` reference.                                                                                                                                                                                             | {% interactive-demo for="â all(mySequence, {@it > 2})" /%}

  {% interactive-demo for="â all(myMap, {@key == \"b\"})" /%}    |
| `filter(value_src, {predicate})` | Filters the elements of the collection using the predicate. The current element is accessed with the `@it` reference.                                                                                                                                                                                                                 | {% interactive-demo for="â filter(mySequence, {@it > 1})" /%}

  {% interactive-demo for="â filter(myMap, {@value > 1})" /%} |

## Try your own conditions{% #try-your-own-conditions %}

This interactive simulator helps you experiment with the Expression Language syntax in a realistic environment. It shows how conditions affect whether a log line will be generated when instrumenting a method.

Select one of the examples or enter an expression in the "when" field and click "SIMULATE" to see if the log would be generated based on your condition.

Available variables in this example:

- `loops`: The route parameter hardcoded to `5`
- `myString`: A string `"Hello, world!"`
- `mySequence`: An array of integers `[1, 2, 3]`
- `myMap`: A dictionary `{"a": 1, "b": 2, "c": 3}`
- `i`: The current loop iteration index
Try these examples:   **Note:** Condition evaluations and variable access patterns may vary when using the product.1112@app.route('/hello_world/<int:loops>')13def hello_world(loops):14myString = "hello world"15mySequence = [1, 2, 3, 4]16myMap = {"a": 1, "b": 2, "c": 3}17for i in range(loops):EmitLog â¼with templateLog on loop {i+1} generatedwhen 18pass19return "OK", 20020 curl http://example-app:80/hello_world/5