# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/regexp-raw-string.md

---
title: Prevent using escapes in regular expression
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent using escapes in regular expression
---

# Prevent using escapes in regular expression

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/regexp-raw-string`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, it is better to avoid using double backslashes (`\\`) in regular expressions and instead use raw string literals (enclosed by backticks) to define regular expressions.

When using double backslashes, each backslash has a special meaning and needs to be escaped. This can lead to confusion and make regular expressions harder to read and understand.

Using raw string literals with backticks, on the other hand, treats backslashes as regular characters and avoids the need for escaping. This simplifies the expression and makes it more readable.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
   regexp.Compile("\\A(\\w+) total: items \\d+\\n\\z")
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
   regexp.Compile(`\A(\w+) total: items \d+\n\z`)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
