# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/catch-nullreference.md

---
title: Prevent catching NullReference
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent catching NullReference
---

# Prevent catching NullReference

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/catch-nullreference`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Do not catch `NullReferenceException`. Instead, check directly if the value is `null` in your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    void myMethod()
    {
        try {

        }
        catch (NullReferenceException e) {

        }
        
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 