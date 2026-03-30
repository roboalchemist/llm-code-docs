# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-code-style/short-method-name.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-code-style/short-method-name.md

---
title: Avoid short method names
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid short method names
---

# Avoid short method names

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-code-style/short-method-name`

**Language:** C#

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Method names should be descriptive of the function behavior and functionalities. Instead of using a very short name, always have a name that indicates what the function is doing.

#### Learn More{% #learn-more %}

- [C# Google Style Guide](https://google.github.io/styleguide/csharp-style.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    void ab(){

    }
}
```

```csharp
interface MyInterface {
    void ab();
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
interface MyInterface {
    void myMethod();
}
```

```csharp
class MyClass {
    void myMethod(){

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
