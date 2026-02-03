# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/boolean-get-method-name.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-code-style/boolean-get-method-name.md

---
title: Avoid prefix boolean returning method with `get`
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid prefix boolean returning method with `get`
---

# Avoid prefix boolean returning method with `get`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-code-style/boolean-get-method-name`

**Language:** C#

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

If a method returns a boolean, do not use a name that starts with `get`. Instead, use a name that shows a better description of the method objective. For example, start the method name with `is`, `has`, or `can`.

#### Learn More{% #learn-more %}

- [C# Google Style Guide](https://google.github.io/styleguide/csharp-style.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    bool getAttribute(){
        
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    bool hasAttribute(){
        
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 