# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/no-sleep-in-tests.md

---
title: Avoid Thread.sleep in tests
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid Thread.sleep in tests
---

# Avoid Thread.sleep in tests

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/no-sleep-in-tests`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Avoid sleeping in tests. It blocks the test execution and leads to unpredictable results.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    [TestMethod]
    public void TestMyMethod()
    {
        Thread.Sleep(500);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    [TestMethod]
    public void TestMyMethod()
    {
        // statements
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
