# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/class-naming-conventions.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-code-style/class-naming-conventions.md

---
title: Follow class naming conventions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Follow class naming conventions
---

# Follow class naming conventions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-code-style/class-naming-conventions`

**Language:** C#

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Class names should use the `PascalCase` and start with an uppercase.

#### Learn More{% #learn-more %}

- [C# Google Style Guide](https://google.github.io/styleguide/csharp-style.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class My_Class {
    void SampleMethod();
}
```

```csharp
class myClass {
    void SampleMethod();
}
```

```csharp
interface myInterface {
    void SampleMethod();
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    void SampleMethod();
}
```

```csharp
class MyClass {
    void SampleMethod();
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
