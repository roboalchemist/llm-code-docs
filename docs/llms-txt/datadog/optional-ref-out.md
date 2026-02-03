# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/optional-ref-out.md

---
title: Do not use Optional on ref or out. parameters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use Optional on ref or out. parameters
---

# Do not use Optional on ref or out. parameters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/optional-ref-out`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The modifier `Optional` should not be used on `ref` or `out` parameters because it's semantically incorrect:

- an `out` parameter is used as a value to return from the function and, therefore, is not optional
- a `ref` parameter is passed back to the caller

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {

    public static void routine([Optional] out i)
    {
    }
}
```

```csharp
class MyClass {
    public static void routine([Optional] ref int i)
    {
    }

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 