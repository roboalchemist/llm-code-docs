# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/no-double-operators.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/no-double-operators.md

---
title: Do not use the same operator twice
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use the same operator twice
---

# Do not use the same operator twice

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/no-double-operators`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Do not use the same operator twice; it will cancel the first operator and have no effect.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public void myMethod()
    {
        int myInt = 1;
        var myValue1 = !!myInt;
        var myValue2 = ~~myInt;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public void myMethod()
    {
        int myInt = 1;
        var myValue1 = myInt;
        var myValue2 = myInt;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 