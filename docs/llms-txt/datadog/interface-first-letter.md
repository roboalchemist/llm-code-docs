# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-code-style/interface-first-letter.md

---
title: Interface names should start with I
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Interface names should start with I
---

# Interface names should start with I

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-code-style/interface-first-letter`

**Language:** C#

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

The first letter of an interface should be `I`.

#### Learn More{% #learn-more %}

- [C# Google Style Guide](https://google.github.io/styleguide/csharp-style.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
interface Service {
    void myMethod();
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
interface IService {
    void myMethod();
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
