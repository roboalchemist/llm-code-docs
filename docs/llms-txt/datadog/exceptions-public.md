# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/exceptions-public.md

---
title: Exceptions should be made public
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Exceptions should be made public
---

# Exceptions should be made public

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/exceptions-public`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Exceptions should not be made `internal` and should be made `public`. Exceptions are designed to be reused across the codebase or in multiple codebases. By making an exception `internal`, it then cannot be reused across the different codebases.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
internal class MyCustomException: Exception {
    
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class MyCustomException: Exception {
    
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 