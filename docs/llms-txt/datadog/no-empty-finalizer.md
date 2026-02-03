# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/no-empty-finalizer.md

---
title: Avoid empty finalizer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid empty finalizer
---

# Avoid empty finalizer

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/no-empty-finalizer`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Destructor should not be empty.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class MyClass {
    ~MyClass() {
        
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class MyClass {
    ~MyClass() {
        doSomething();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 