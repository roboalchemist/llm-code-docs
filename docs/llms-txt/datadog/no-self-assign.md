# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/no-self-assign.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/no-self-assign.md

---
title: Do not assign a variable to itself
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not assign a variable to itself
---

# Do not assign a variable to itself

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/no-self-assign`

**Language:** C#

**Severity:** Notice

**Category:** Error Prone

## Description{% #description %}

Do not assign a value to itself, it has no effect.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public void myMethod()
    {
        var myValue1 = 2;
        myValue1 = myValue1;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public void myMethod()
    {
        var myValue1 = 2;
        var myValue2 = 3;
        myValue1 = myValue2;
        myMethod2(myValue1, { myValue2 = myValue2 });
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
