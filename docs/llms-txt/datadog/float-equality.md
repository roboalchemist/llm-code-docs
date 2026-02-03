# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/float-equality.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/float-equality.md

---
title: Prevents using `==` and `!=` operators on floats and doubles
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevents using `==` and `!=` operators on floats and doubles
---

# Prevents using `==` and `!=` operators on floats and doubles

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/float-equality`

**Language:** C#

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Floating point math is inherently imprecise, so checking strict equality to a `float` or `double` will very likely lead to unexpected bugs.

For example: **Input**

```gdscript3
var a = 0.1f;
var b = 0.2f;
var c = 0.3f;
Console.WriteLine($"{a + b == c}");
```

**Output**

```
False
```

(Note: exact results can vary depending on the compiler used)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class NonCompliant
{
    public static void Main()
    {
        float foo = 1.2345f;

        if (foo == 1.2345f) { /* ... */ }

        if (4.567d == 4.567d) { /* ... */ }
        if (4.567f != 4.567f) { /* ... */ }

        bool isEqual = foo == 1.2345f;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class Compliant
{
    public static void Main()
    {
        float foo = 1.2345f;
        var tolerance = 0.000000001f;
        if (Math.Abs(foo - 1.2345f) < tolerance) { /* ... */ }
        decimal bar = 1.2345m;
        if (bar == 1.2345m) { /* ... */ }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 