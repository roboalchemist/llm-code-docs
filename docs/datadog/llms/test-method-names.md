# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/test-method-names.md

---
title: Test method name should follow conventions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Test method name should follow conventions
---

# Test method name should follow conventions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/test-method-names`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Test methods should follow the following guidelines:

- must be `public` and not `async`
- the name should start with `Test`

#### Learn More{% #learn-more %}

- [mstest documentation](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-mstest)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyTests {
    [TestMethod]
    void FooBar()
    {

    }

    [TestMethod]
    public async void BlipBlop()
    {

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyTests {
    [TestMethod]
    public void TestSomething()
    {

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
