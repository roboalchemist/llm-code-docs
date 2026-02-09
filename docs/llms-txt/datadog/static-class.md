# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/static-class.md

---
title: Class should be static
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Class should be static
---

# Class should be static

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/static-class`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule states that a class should be declared as `static` if it only contains `static` members. Declaring a class as `static` indicates that it cannot be instantiated or extended and that all its members are `static`. This provides a clear signal to other developers that this class is not meant to be used as an object.

## What the rule detects{% #what-the-rule-detects %}

The rule detects if all members are static . If they are, the rule recommends to declare the class static.

## How to fix the issue?{% #how-to-fix-the-issue %}

Declare the class static by adding the `static` keyword to its declaration.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
// all attributes are static, the class should be static
public class Foo
{
    private static string _f;

    public static void Bar()
    {
    }
}

public class FooBar
{
    private static readonly IList<MyObject> LargeCollection;

    FooBar()
    {
        string json = System.IO.File.ReadAllText(TestFixtureBase.ResolvePath("large.json"));

        LargeCollection = JsonConvert.DeserializeObject<IList<RootObject>>(json);
    }


    public static void Plop()
    {
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class StaticTestClass
{
    [JsonProperty]
    public int x = 1;

    [JsonProperty]
    public static int y = 2;

    [JsonProperty]
    public static int z { get; set; }

    static StaticTestClass()
    {
        z = 3;
    }
}
```

```csharp
public class Foo
{
    bool somethingAttribute;

    private static string _f;

    public static void Bar()
    {
    }
}

public class FooBar
{
    private static readonly IList<MyObject> LargeCollection;

    FooBar()
    {
        string json = System.IO.File.ReadAllText(TestFixtureBase.ResolvePath("large.json"));

        LargeCollection = JsonConvert.DeserializeObject<IList<RootObject>>(json);
    }


    public void Plop()
    {
    }
}


public class NoConstructorReadOnlyCollection<T> : ReadOnlyCollection<T>
{
    public NoConstructorReadOnlyCollection() : base(new List<T>())
    {
    }
}
```

```csharp
// has non-static properties
public class Foo
{
    public bool SomeAttributes { get; set; }

    private static string _f;

    public static void Bar()
    {
    }
}
```

```csharp
// not static recommended because one attribute is not static
public class Foo
{
    private static string _f;

    public void Bar()
    {
    }
}
```

```csharp
public static class Foo
{
    private static string _f;

    public static void Bar()
    {
    }
}

class Cat : Animal
{
    public Cat(string name)
        : base(name)
    {
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 