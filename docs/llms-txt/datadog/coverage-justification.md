# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/coverage-justification.md

---
title: Ensure code coverage exclusions are justified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure code coverage exclusions are justified
---

# Ensure code coverage exclusions are justified

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/coverage-justification`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

When using `ExcludeFromCodeCoverage`, always provide a reason for the exclusion. This helps with code maintenance and is part of the documentation that helps other engineers understand why the code is excluded from coverage.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    [ExcludeFromCodeCoverage]
    public void MyMethod()
    {
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    [ExcludeFromCodeCoverage(Justification = "Code used by some flaky test that will be removed soon")]
    public void MyMethod()
    {
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 