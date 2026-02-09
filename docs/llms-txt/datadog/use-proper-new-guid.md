# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/use-proper-new-guid.md

---
title: Enforce Guid parameter initialization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce Guid parameter initialization
---

# Enforce Guid parameter initialization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/use-proper-new-guid`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule will warn you that you have instantiated the `Guid` struct without a parameter.

For an empty `Guid`, using `Guid.Empty` is cleaner.

For a randomly-generated `Guid`, use `Guid.NewGuid()` instead.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public void Foo()
{
    var foo1 = new Guid();
    Guid foo2 = new Guid();
    Guid foo3 = new();
    var foo4 = default(Guid);
    Guid foo5 = default(Guid);
    Guid foo6 = default;
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public void Foo(byte[] bytes)
{
    var g1 = Guid.Empty;
    var g2 = Guid.NewGuid();
    var g3 = new Guid(bytes);
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 