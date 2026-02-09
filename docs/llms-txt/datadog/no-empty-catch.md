# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/no-empty-catch.md

---
title: Avoid empty catch sections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid empty catch sections
---

# Avoid empty catch sections

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/no-empty-catch`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Exceptions must be appropriately handled and have code to recover from the exceptions. If no recovery is added, the code should at least log the error.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void routine()
    {
        try {
            doSomething();
        } catch (MyException ex) {
            
        }
    }
}
```

```csharp
class MyClass {
    public static void routine()
    {
        try {
            doSomething();
        } catch (MyException ex) {
            // comment
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public static void routine()
    {
        try {
            doSomething();
        } catch (MyException ex) {
            handleException();
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 