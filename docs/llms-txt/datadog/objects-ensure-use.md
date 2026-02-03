# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-code-style/objects-ensure-use.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/objects-ensure-use.md

---
title: Ensure objects are used
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure objects are used
---

# Ensure objects are used

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/objects-ensure-use`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Creating an object and then not using it can lead to unexpected behavior if the constructor contains side effects.

If the code intentionally creates and drops an object to trigger the constructor side effects, consider moving them to a separate function and call it directly.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public void myMethod()
    {
        new MyClass();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public void myMethod()
    {
        var obj = new MyClass();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 