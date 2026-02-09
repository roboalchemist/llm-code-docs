# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/dispose-objects-once.md

---
title: Dispose objects at most once
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Dispose objects at most once
---

# Dispose objects at most once

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/dispose-objects-once`

**Language:** C#

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

From the [documentation](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable.dispose?view=net-8.0&redirectedfrom=MSDN#System_IDisposable_Dispose), the `dispose()` method should be called only once. Additional calls do not have any impact other than potential performance overhead.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Net;

class MyClass {
    public static void routine()
    {
        Disposable myObject;

        myObject.dispose();
        foo.bar();
        if(foo) {
            something.dispose();
        } else {
            myObject.dispose();
        }
        
    }
}
```

```csharp
using System.Net;

class MyClass {
    public static void routine()
    {
        Disposable myObject;

        myObject.dispose();
        foo.bar();
        myObject.dispose();
    }
}
```

```csharp
using System.Net;

class MyClass {
    public static void routine()
    {
        Disposable myObject;

        myObject.dispose();
        foo.bar();
        if(foo) {
            myObject.dispose();
        }
        
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public static void routine()
    {
        Disposable myObject;

        myObject.dispose();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 