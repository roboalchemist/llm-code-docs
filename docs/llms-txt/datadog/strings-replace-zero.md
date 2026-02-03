# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/strings-replace-zero.md

---
title: strings.Replace with 0 does not do anything
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > strings.Replace with 0 does not do anything
---

# strings.Replace with 0 does not do anything

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/strings-replace-zero`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The code `strings.Replace(str, something, somethingElse, 0)` is considered bad practice because it won't actually replace anything in the string `str`.

In Go's `strings.Replace` function, the last argument `n` represents the maximum number of replacements to be made. When `n` is set to 0, the function doesn't perform any replacements, and the original string `str` remains unchanged.

Therefore, if the intention is to replace occurrences of `something` with `somethingElse` in the string `str`, setting `n` to 0 will prevent any replacements from occurring.

To correctly replace occurrences in a string, the value of `n` should be set to a positive integer that indicates the maximum number of replacements to be made, or -1 to replace all occurrences.

For example, to replace all occurrences of `something` with `somethingElse`, the code should be modified as follows:

```json
strings.Replace(str, something, somethingElse, -1)
```

By setting `n` to -1, the `strings.Replace` function will replace all instances of `something` with `somethingElse` in the string `str`.

Using the appropriate value for `n` ensures that the replacements are performed as intended and the desired behavior is achieved. It is important to read the function documentation and understand the purpose and behavior of each parameter to avoid unexpected results in your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    strings.Replace(str, something, somethingElse, 0)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    strings.Replace(str, something, somethingElse, -1)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 