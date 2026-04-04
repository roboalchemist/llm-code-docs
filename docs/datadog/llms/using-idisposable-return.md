# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/using-idisposable-return.md

---
title: Prevents the return of an IDisposable from a using statement
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevents the return of an IDisposable from a using statement
---

# Prevents the return of an IDisposable from a using statement

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/using-idisposable-return`

**Language:** C#

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

In a [using statement](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/using), the acquired IDisposable instance is disposed of when control leaves the block. If this instance is returned from a function, a runtime error will likely occur when the value is read.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.IO;
using System.Text;

class NonCompliant {
    public FileStream Write(string filePath)
    {
        using (FileStream fs = new FileStream(filePath, FileMode.Create))
        {
            var bytes = Encoding.UTF8.GetBytes("foo");
            fs.Write(bytes, 0, bytes.Length);
            return fs;
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.IO;
using System.Text;

class Compliant {
    public FileStream Write(string filePath)
    {
        FileStream fs = new FileStream(filePath, FileMode.Create);
        var bytes = Encoding.UTF8.GetBytes("foo");
        fs.Write(bytes, 0, bytes.Length);
        return fs;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
