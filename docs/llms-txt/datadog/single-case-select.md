# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/single-case-select.md

---
title: Avoid select statement with one case
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid select statement with one case
---

# Avoid select statement with one case

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/single-case-select`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, using a `select` statement with a single case is generally considered a code smell and not a recommended practice.

Here are a few reasons why:

1. **Clarity and intent**: The purpose of a `select` statement is to select and execute the first `case` that is ready to proceed. When there is only a single `case` in the `select` statement, it becomes redundant and obscures the clarity of the code. It is better to use a straightforward control flow statement like `if` or `switch` instead, as it conveys the intent more directly.
1. **Readability and maintainability**: A `select` statement with a single case can make the code harder to read and understand. It adds unnecessary complexity and can confuse other developers who are reviewing or maintaining the codebase. It's important to write code that is easy to comprehend and follow.
1. **Flexibility for future additions**: Having a single case in a `select` statement limits the extensibility of the code. If additional cases need to be added in the future, it becomes clumsy to modify the code by converting the single case into a `default` case or by adding more cases. It's better to start with a more flexible structure, such as an `if` statement, that can accommodate future additions more easily.
1. **Linting and static analysis tools**: Many linting tools and static code analyzers can detect and flag a single `case` in a `select` statement as a potential code issue or a pattern that can be simplified. This can result in unnecessary noise and make it harder to identify genuine issues when reviewing the codebase with these tools.

To improve code readability and maintainability, it is recommended to use `select` statements when there are multiple cases with different synchronization or communication requirements. For a single case, it is clearer and more straightforward to use an `if` statement or a simple control flow construct.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    select {
        case <-ch: {

        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    select {
        case <-ch1: {

        }
        case <-ch2: {

        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 