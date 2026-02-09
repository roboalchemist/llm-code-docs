# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/use-specific-exceptions.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/use-specific-exceptions.md

---
title: Do not throw generic exceptions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not throw generic exceptions
---

# Do not throw generic exceptions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/use-specific-exceptions`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Exceptions should be specific to the application to help points the exact issue. For these reasons, generic exceptions should not be used and we should instead favor specific exception types.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void processString(string s)
    {
        throw new Exception("foo");
        throw new ApplicationException("oh no something got wrong");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public static void processString(string s)
    {
        throw new MyCustomException("oh no!");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 