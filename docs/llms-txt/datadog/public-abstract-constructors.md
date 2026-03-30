# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/public-abstract-constructors.md

---
title: Avoid using a public contructor for an abstract class
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using a public contructor for an abstract class
---

# Avoid using a public contructor for an abstract class

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/public-abstract-constructors`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Using an [abstract](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/abstract) modifier in a class declaration indicates that a class is intended only to be a base class of other classes and not instantiated by itself. Due to this, there is no need for `public` or `internal` constructors within. Any initialization logic should be added in a `private`,`private protected`, or `protected` constructor.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
abstract class Foo
{
    internal Foo()
    {
      //...
    }
}
```

```csharp
abstract class Foo
{
    public Foo()
    {
      //...
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
abstract class Foo
{
    private protected Foo()
    {
      //...
    }
}
```

```csharp
abstract class Foo
{
    private Foo()
    {
      //...
    }
}
```

```csharp
abstract class Foo
{
    protected Foo()
    {
      //...
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
