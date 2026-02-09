# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/ignored-threadstatic.md

---
title: Ensures ThreadStatic fields are marked static
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensures ThreadStatic fields are marked static
---

# Ensures ThreadStatic fields are marked static

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/ignored-threadstatic`

**Language:** C#

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

If a non-static field is marked [ThreadStatic](https://learn.microsoft.com/en-us/dotnet/api/system.threadstaticattribute), the ThreadStatic attribute will be ignored. In this case, this rule suggests changing the field to be `static`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class NonCompliant {
    [ThreadStatic] public int foo;
    [ThreadStatic] int foo;
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class Compliant {
    [ThreadStatic] static int foo;
    [ThreadStatic] public static int foo;

    int foo = 1;

    ThreadLocal<int> foo = new ThreadLocal<int> (() => 1);
    
    ThreadLocal<int> foo;
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 