# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/avoid-notimplementedexception.md

---
title: Avoid NotImplementedException
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid NotImplementedException
---

# Avoid NotImplementedException

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/avoid-notimplementedexception`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The exception `NotImplementedException` is used for future features. While not a bug, it should be tracked so that features are fully implemented.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void routine()
    {
        throw new NotImplementedException();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
