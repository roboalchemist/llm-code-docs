# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/stringcomparison.md

---
title: Use StringComparison to compare strings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use StringComparison to compare strings
---

# Use StringComparison to compare strings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/stringcomparison`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The rule "Use StringComparison to compare strings" is critical in ensuring accurate and efficient string comparisons in C#. Using methods like `ToUpper()` or `ToLower()` or operators like `==` to compare strings can lead to incorrect results due to cultural differences in string representation. Furthermore, these methods can cause unnecessary memory allocation and performance issues.

The importance of this rule lies in its ability to prevent potential bugs and enhance the performance of your code. It ensures that string comparisons are done in a way that respects cultural differences and avoids unnecessary operations.

## How to remediate{% #how-to-remediate %}

To adhere to this rule, always use the `StringComparison` enumeration when comparing strings. For example, use `string.Equals(foo, bar, StringComparison.OrdinalIgnoreCase)` instead of `foo.ToUpper() == bar.ToUpper()`. This will perform a case-insensitive, culture-invariant comparison that is also more performant.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
// do not use `==` to compare strings
if (foo.ToUpper() == bar.ToUpper())
{
}
```

```csharp
// do not use `==` to compare strings
if (foo.ToLower() == bar.ToLower())
{
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
if (foo.Foo() == bar.Bar())
{
}
```

```csharp
if (string.Equals(foo, bar, StringComparison.OrdinalIgnoreCase))
{
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 