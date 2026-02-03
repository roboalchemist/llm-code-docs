# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-code-style/short-variable.md

---
title: Avoid short variable names
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid short variable names
---

# Avoid short variable names

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-code-style/short-variable`

**Language:** C#

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Variable names should be descriptive of the purpose of the variable. Do not use names that are too short, and use names that help other developers understand the objective of this variable.

#### Learn More{% #learn-more %}

- [C# Google Style Guide](https://google.github.io/styleguide/csharp-style.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    void myMethod(){
        int fo = 20 + 10;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    void myMethod(){
        int foobar = 20 + 10;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 