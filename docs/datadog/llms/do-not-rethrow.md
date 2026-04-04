# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/do-not-rethrow.md

---
title: Do not rethrow exception
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not rethrow exception
---

# Do not rethrow exception

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/do-not-rethrow`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The rule "Do not rethrow exception" advises against rethrowing an exception using the `throw ex;` syntax. This practice is discouraged because it resets the stack trace of the original exception to the current catch block, which can lead to loss of valuable debugging information.

The importance of this rule lies in maintaining the integrity of exception stack traces. These traces provide crucial information about the sequence of method calls that led to the exception, making it easier to locate and fix the source of the error.

## How to Remediate{% #how-to-remediate %}

To fix this issue, use the `throw;` statement without an exception object in catch blocks to rethrow the original exception while preserving its stack trace. For example, replace `throw ex;` with just `throw;`. This ensures that the original exception's stack trace is maintained and aids in effective debugging.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class Foo {
    public void Bar() {
        try {
            myMethod();
        }
        catch (System.Exception ex)
        {
            throw ex;
        }
        catch (System.Exception ex2)
        {
            if (foo) {
                throw ex2;
            }

        }
    }
}
```

```csharp
class Foo {
    public void Bar() {
        try {
            myMethod();
        }
        catch (Exception ex)
        {
            throw ex;
        }
        catch (Exception ex2)
        {
            if (foo) {
                throw ex2;
            }

        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class Foo {
    public void Bar() {
        try {
            myMethod();
        }
        catch (Exception ex)
        {
            throw;
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
