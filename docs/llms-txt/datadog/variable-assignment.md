# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-inclusive/variable-assignment.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-inclusive/variable-assignment.md

---
title: Check variable assignment language
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check variable assignment language
---

# Check variable assignment language

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-inclusive/variable-assignment`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Avoid using words such as `blacklist`, `whitelist`, `slave` or `master` in variable names. Consider using more inclusive wording in your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class Student
{
    static void Main()
    {
        TestClass slaveVariable = new TestClass();

    }
}
```

```csharp
class Student
{
    private int masterName;


}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class Student
{
    static void Main()
    {
        TestClass secondaryVariable = new TestClass();

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
