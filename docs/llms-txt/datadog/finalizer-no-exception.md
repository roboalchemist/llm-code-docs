# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/finalizer-no-exception.md

---
title: Avoid exceptions in finalizers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid exceptions in finalizers
---

# Avoid exceptions in finalizers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/finalizer-no-exception`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Do not throw exceptions in finalizer blocks, as it can terminate the whole process if handled incorrectly.

From the official documentation: *"If [Finalize](https://learn.microsoft.com/en-us/dotnet/api/system.object.finalize?view=net-8.0) or an override of [Finalize](https://learn.microsoft.com/en-us/dotnet/api/system.object.finalize?view=net-8.0) throws an exception, and the runtime is not hosted by an application that overrides the default policy, the runtime terminates the process and no active `try`/`finally` blocks or finalizers are executed".*

#### Learn More{% #learn-more %}

- [Official Documentation](https://learn.microsoft.com/en-us/dotnet/api/system.object.finalize?view=net-8.0&redirectedfrom=MSDN#System_Object_Finalize)
- [An Exception Thrown From a Finalizer Will Be Treated as an Unhandled Exception](https://csharp.2000things.com/2012/09/17/672-an-exception-thrown-from-a-finalizer-will-be-treated-as-an-unhandled-exception/)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    ~MyClass()
    {
        if (foo) {
            throw new MyException();
        }
        
    }
}
```

```csharp
using System.Xml;

class MyClass {
    ~MyClass()
    {
        throw new MyException();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 