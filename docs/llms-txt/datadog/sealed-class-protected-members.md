# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/sealed-class-protected-members.md

---
title: Avoid protected members in sealed class
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid protected members in sealed class
---

# Avoid protected members in sealed class

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/sealed-class-protected-members`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

While authorized by the compiler, `protected` visibility in `sealed` classes does not make sense as these classes cannot be inherited. Use `public` or `private` instead.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public sealed class MyClass {
    protected int foo;

    protected void myMethod() {
        
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public sealed class Application() : ParentClass
{


    protected override void myFunctionOverride()
    {
    }

}
```

```csharp
public sealed class MyClass {
    private int foo;

    private void myMethod() {
        
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 