# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/reference-equals-value-types.md

---
title: Do not use ReferenceEquals with value types
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use ReferenceEquals with value types
---

# Do not use ReferenceEquals with value types

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/reference-equals-value-types`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The `Object.ReferenceEquals` method in C# is used to determine if two object references refer to the same object, not if the objects themselves are equal. This rule is important because value types in C# are not reference types. They are stored on the stack, not the heap, and each instance has its own copy of the data. Therefore, using `Object.ReferenceEquals` with value types will always return false because they are boxed into separate objects on the heap.

## How to remediate{% #how-to-remediate %}

To avoid breaking this rule, you should not use `Object.ReferenceEquals` to compare value types. Instead, you can use the `==` operator or `Object.Equals` method, which are designed to compare the values of two objects, not their references. This is the correct way to compare value types in C#, and it will give you the expected behavior.

For example, instead of writing `Object.ReferenceEquals(int1, int2)`, you should write `int1 == int2` or `Object.Equals(int1, int2)`. These expressions will correctly compare the values of `int1` and `int2`, not their references.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
int int1 = 1
int int2 = 1;

Console.WriteLine(Object.ReferenceEquals(int1, int2));
```

```csharp
int int1 = 1, int2 = 1;

Console.WriteLine(Object.ReferenceEquals(int1, int2));
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
int int1 = 1, int2 = 1;

Console.WriteLine(int1 == int2);
Console.WriteLine(object.Equals(int1, int2));
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
