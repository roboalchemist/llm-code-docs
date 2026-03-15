# Source: https://docs.firehydrant.com/docs/common-expression-language.md

# Common Expression Language (CEL)

FireHydrant allows you to query data and relationships in your Signals using [Common Expression Language](https://opensource.google/projects/cel) (CEL).

A basic query in FireHydrant includes an entity with properties available via dot notation (e.g., `entity.property`) and logical operators with a comparison value. Today's only available entity is a Signal, which represents the incoming <Glossary>Event</Glossary> from webhooks. A basic query might look like the following:

```go
// entity.property == "value"
signal.summary == "CPU Utilization Spiking" 
```

Each Signal has properties that can be evaluated and a specific value you wish to express. CEL queries can be performed on the Signals list page and when creating Signals Rules for a team.

## Basic CEL Usage

> 📘 Note:
>
> These tables are not all-inclusive; they only cover some of the most commonly-used operators, functions, or macros. For full documentation, visit [Google's Language Definition for CEL](https://github.com/google/cel-spec/blob/master/doc/langdef.md).

**Logical Operators**

| Operator | Meaning        | Examples returning true |    |             |    |          |
| :------- | :------------- | :---------------------- | -- | ----------- | -- | -------- |
| `==`     | Equals         | `2 == 2`                |    |             |    |          |
| `!=`     | Does not equal | `3 != 2`                |    |             |    |          |
| `>`      | Greater than   | `3 > 2`                 |    |             |    |          |
| `<`      | Less Than      | `2 < 3`                 |    |             |    |          |
| `&&`     | And            | `2 == 2 && 2 != 3`      |    |             |    |          |
| \`\\     | \\             | \`                      | Or | \`2 == 3 \\ | \\ | 2 == 2\` |
| `in`     | Inclusion test | `'test' in ['test']`    |    |             |    |          |

**CEL Functions**

| Function       | Example                                                                                              |
| -------------- | ---------------------------------------------------------------------------------------------------- |
| `contains()`   | `signal.summary.contains("CPU")`                                                                     |
| `matches()`    | ` signal.summary.matches("CPU")` or `matches(signal.summary, "CPU")`                                 |
| `size()`       | Check array length: `size(signal.images) > 1` <br /> Check string length: `size(signal.summary) > 3` |
| `startsWith()` | `signal.summary.startsWith("CPU")`                                                                   |
| `endsWith()`   | `signal.summary.endsWith("Spiking")`                                                                 |

**CEL Macros**

| Macro      | Example                                     | Definition                                                                  |
| :--------- | :------------------------------------------ | :-------------------------------------------------------------------------- |
| `all()`    | ` signal.all(x, has(x))`                    | Tests whether a predicate function holds for all properties of a signal     |
| `exists()` | ` signal.exists(x, has(x))`                 | Tests whether a predicate function holds for any properties of a signal     |
| `filter()` | `signal.images.map(image, image.src != "")` | Filters a list and provides matching values to be returned in a new list    |
| `has()`    | `has(signal.summary)`                       | Tests whether a field is available                                          |
| `map()`    | `signal.links.map(link, link.url != "")`    | Maps a list and provides each value to be mapped and returned in a new list |

> 📘 Note:
>
> 📚 You can check out [the full documentation of CEL](https://chromium.googlesource.com/external/github.com/google/cel-go/+/refs/tags/v0.9.0/README.md) to explore even more about leveraging CEL inside of FireHydrant for querying signals.

## Example Signal and CEL Query

```json
{
  "summary": "CPU Utilization Spiking",
  "body": "The production server is experiencing greater than 99% utilizations of compute.",
  "level": 0,
  "status": 0,
  "images": [
    {
      "src": "https://site.com/images/123.png",
      "alt": "A simple, sample image"
    }
  ],
  "links": [
    {
      "href": "https://site.com/monitors/123",
      "text": "Monitoring Source"
    }
  ],
  "annotations": {
    "policy": "escalatable"
  },
  "tags": ["service:core-application", "env:prod"],
  "received_at": "2023-11-09T18:22:16.000+00:00"
}

```

Below is an example CEL expression that would return true on this payload:

```go
signal.summary.contains("CPU") && signal.level == 2 && signal.annotations.policy.equals("escalatable")

```

In this expression:

* **`signal`** refers to the instance of the Signal.
* **`signal.summary`** checks if the summary field in the Signal message contains "CPU".
* **`signal.level checks`** if the level field in the Signal message equals the enum for “ERROR”. The standard system levels are available here: INFO: 0 , WARN: 1, ERROR: 2, & FATAL: 3
* **`signal.annotations.policy.equals('escalatable')`** accesses a `policy` key and checks if it equals "escalatable." If the key doesn't exist, then this value will automatically evaluate to `false`

☝️ **Note about Signals Levels**

Signals can take on a standard “Level” based on data from a webhook. You can run CEL queries based on the ENUM value for each, as shown below.

```go
INFO = 0;
WARN = 1;
ERROR = 2;
FATAL = 3;
```

## Other Resources

* [Google CEL Spec](https://github.com/google/cel-spec)
* [List of Standard CEL Definitions and Functions](https://github.com/google/cel-spec/blob/master/doc/langdef.md#list-of-standard-definitions)