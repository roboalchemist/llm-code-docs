# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/outattr-on-pinvoke.md

---
title: Do not use OutAttribute on string parameters for P/Invokes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use OutAttribute on string parameters for P/Invokes
---

# Do not use OutAttribute on string parameters for P/Invokes

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/outattr-on-pinvoke`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The `OutAttribute` on string parameters for P/Invoke methods is not recommended because strings in .NET are immutable. When you pass a string to a method as an output parameter, it's not possible to modify the original string. This can lead to unexpected behaviors and bugs in your code.

This rule is important because it helps to prevent these issues, ensuring that your P/Invoke methods work correctly and as expected. Adhering to this rule will result in more robust and maintainable code.

## How to remediate{% #how-to-remediate %}

Use `StringBuilder` instead of `string` for output parameters. The `StringBuilder` class is mutable and can handle the modifications made by the P/Invoke method. In the compliant code example, `StringBuilder` is used with the `GetComputerName` method, and the method is able to modify the `StringBuilder` object and reflect the changes in the calling code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System;
using System.Runtime.InteropServices;

class Program
{
    [DllImport("kernel32.dll", CharSet = CharSet.Unicode)]
    public static extern void GetComputerName([Out] string name, ref int size);

    [DllImport("kernel32.dll", CharSet = CharSet.Unicode)]
    public static void GetComputerNameInternal([Out] string name, ref int size){

    }

    static void Main()
    {
        int size = 256;
        string name = new string('\0', size);
        GetComputerName(name, ref size);
        Console.WriteLine(name);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System;
using System.Runtime.InteropServices;
using System.Text;

class Program
{
    [DllImport("kernel32.dll", CharSet = CharSet.Unicode)]
    public static extern bool GetComputerName(StringBuilder name, ref int size);

    static void Main()
    {
        int size = 256;
        StringBuilder name = new StringBuilder(size);
        if (GetComputerName(name, ref size))
        {
            Console.WriteLine(name.ToString());
        }
        else
        {
            Console.WriteLine("Failed to get computer name.");
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
