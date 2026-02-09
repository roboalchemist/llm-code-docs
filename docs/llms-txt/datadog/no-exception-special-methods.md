# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/no-exception-special-methods.md

---
title: Do not throw exceptions in special methods
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not throw exceptions in special methods
---

# Do not throw exceptions in special methods

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/no-exception-special-methods`

**Language:** C#

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

Do not throw exceptions in special methods such as `ToString()`, `Dispose()` or `GetHashCode`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public override string GetHashCode()
    {
        if (something)
        {
            throw new Exception();
        }
        throw new Exception();
    }
}
```

```csharp
class MyClass {
    public override string ToString()
    {
        if (something)
        {
            throw new Exception();
        }
        throw new Exception();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 