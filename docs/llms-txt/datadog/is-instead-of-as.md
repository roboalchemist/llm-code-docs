# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/is-instead-of-as.md

---
title: Prefer is keyword over as
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer is keyword over as
---

# Prefer is keyword over as

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/is-instead-of-as`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The `is` keyword in C# is used for checking the compatibility of an object with a given type, and the result of the operation is a Boolean: true if the object is of the given type, and false otherwise. The `as` operator, on the other hand, performs a type conversion and returns the object if the conversion is successful, or null if it isn't.

Using the `as` operator to check for type compatibility can lead to less straightforward and potentially confusing code. It can also have performance implications. When you use `as`, the runtime performs the type check and the conversion, and if you then use the result in a conditional statement, you're effectively checking the type twice: once with `as`, and once with the `null` check.

## How to Remediate{% #how-to-remediate %}

To remediate this error, prefer using the `is` keyword when the aim is to check for type compatibility. This not only makes the code clearer and more straightforward, but it also eliminates the unnecessary type check, leading to potentially better performance. For instance, instead of `if (x as string != null)`, you should use `if (x is string)`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
// checking type with the "as" keyword
if (x as string != null)
{
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
// testing type with is
if (foo is string)
{
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
