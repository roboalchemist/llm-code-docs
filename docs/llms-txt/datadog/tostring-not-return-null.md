# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/tostring-not-return-null.md

---
title: ToString() should never return `null`
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > ToString() should never return `null`
---

# ToString() should never return `null`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/tostring-not-return-null`

**Language:** C#

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

The method `ToString()` should always return a value (for example, a string) and never return `null`. Instead of returning `null`, return `string.Empty`, which is an empty string.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public override string ToString()
    {
        if(foo) {
            return null;
        }
        return null;
        
    }
}
```

```csharp
class MyClass {
    public override string ToString()
    {
        return null;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public override string ToString()
    {
        return string.Empty;;    
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 