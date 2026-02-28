# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/dynamic-interface-castable.md

---
title: Check type of interface with DynamicInterfaceCastable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check type of interface with DynamicInterfaceCastable
---

# Check type of interface with DynamicInterfaceCastable

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/dynamic-interface-castable`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The rule "Check type of interface with DynamicInterfaceCastable" is important to ensure that your program uses the correct type of interface when dealing with dynamic types. DynamicInterfaceCastableImplementation attribute is used to indicate that an interface can be used with the DynamicInterfaceCastable class. This attribute allows the runtime to create a dynamic dispatch stub for any interface with this attribute that a class implements.

In C#, when an interface is marked with the `DynamicInterfaceCastableImplementation` attribute, any implementing class should provide a static method for the interface methods. A non-static method would lead to a violation of this rule.

The importance of this rule is to ensure correct implementation of dynamic interfaces, thereby preventing runtime errors and ensuring type safety. To avoid this rule violation, always ensure that methods in classes implementing a dynamic interface are static. This will ensure that the method can be accessed without creating an instance of the class, which is the expected behavior for dynamic interfaces.

## How to remediate{% #how-to-remediate %}

If a class inherits an interface with the attribute `DynamicInterfaceCastableImplementation`, make sure its members are static.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System;
using System.Runtime.CompilerServices;

[DynamicInterfaceCastableImplementation]
public interface IMyInterface
{
    void DoWork();
}

public class MyClass : IMyInterface
{
    // should be static
    public void DoWork()
    {
        Console.WriteLine("Work done!");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System;
using System.Runtime.CompilerServices;

// no inheritance
public interface IMyInterface
{
    void DoWork();
}

public class MyClass : IMyInterface
{

    public void DoWork()
    {
        Console.WriteLine("Work done!");
    }
}
```

```csharp
using System;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

[DynamicInterfaceCastableImplementation]
public interface IMyInterface
{
    void DoWork();
}

public class MyClass : IMyInterface
{
    public static void DoWork(IMyInterface instance)
    {
        Console.WriteLine("Work done!");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
