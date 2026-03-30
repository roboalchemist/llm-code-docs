# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/startswith-indexof.md

---
title: Use StartsWith instead of IndexOf
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use StartsWith instead of IndexOf
---

# Use StartsWith instead of IndexOf

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/startswith-indexof`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule encourages developers to use the `StartsWith` method instead of relying on `IndexOf` to check if a string begins with a specific substring. Using `StartsWith` is more expressive and clearly communicates the intent of the code, improving readability and maintainability. From a performance perspective, `StartsWith` is often more efficient because it can stop checking as soon as a mismatch is found at the beginning of the string, whereas `IndexOf` may scan through the entire string to find the substring. This efficiency gain can be significant in performance-critical applications or when processing large volumes of text.

To comply with this rule, replace any condition that checks if `IndexOf` returns zero (indicating the substring is at the start) with a call to `StartsWith`. For example, instead of writing `if (text.IndexOf("abc") == 0)`, use `if (text.StartsWith("abc"))`. This practice leads to clearer, more concise, and potentially faster code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
if (text.IndexOf("abc") == 0)
{
    Console.WriteLine("Starts with abc");
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
if (text.StartsWith("abc"))
{
    Console.WriteLine("Starts with abc");
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
