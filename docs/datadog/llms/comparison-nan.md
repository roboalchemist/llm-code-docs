# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/comparison-nan.md

---
title: Do not compare with NaN
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not compare with NaN
---

# Do not compare with NaN

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/comparison-nan`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Using a comparison with `float.NaN` or `double.NaN` also returns false. If you want to check the validity of a number, use `float.isNaN` or `double.isNaN`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public void myMethod(float v, double d)
    {
        if (float.NaN == v) {

        }

        if(double.NaN == d) {

        }
    }
}
```

```csharp
class MyClass {
    public void myMethod(float v, double d)
    {
        if (v == float.NaN) {

        }

        if(d == double.NaN) {

        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public void myMethod(float v, double d)
    {
        if (float.isNan(f)) {

        }

        if(double.isNan(f)) {

        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
