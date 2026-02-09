# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/class-no-private-constructors.md

---
title: Warns on class private constructors that are dead code
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Warns on class private constructors that are dead code
---

# Warns on class private constructors that are dead code

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/class-no-private-constructors`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Classes with a private constructor can't be instantiated outside of the class itself. Because they are unreachable, they should be removed or made public.

An exception is made for classes that access their own constructors (like a singleton), and classes that derive from `System.Runtime.InteropServices.SafeHandle`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class NonCompliant {
    private static int n1 = 1;
    private NonCompliant() { /* ... */ }
}

class NonCompliant : Test {
    private NonCompliant() { /* ... */ }
}

class NonCompliant {
    private static readonly Foo _foo = new Foo();
    private NonCompliant() { /* ... */ }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class Compliant {
    private NonCompliant() { /* ... */ }
    public static int n = 1;
}

class Compliant {
    public static int n1 = 1;
    public static int n2 = 2;
}

class Compliant {
    public Compliant() { /* ... */ }
}

class Compliant {
    private static readonly Compliant _singleton = new Compliant();
    private Compliant() { /* ... */ }
}

public sealed class CompliantEnum : SmartEnum<CompliantEnum> {
    public static readonly CompliantEnum One = new CompliantEnum(nameof(One), 1);
    private CompliantEnum(string name, int value) : base(name, value) {}
}

// Utility class
public static class Compliant {
    public static int Sum(int a, int b) { /* ... */ }
    private Compliant() { /* ... */ }
    public static int Value = 1;
}

class Compliant : SafeAccessTokenHandle {
    private Compliant() { /* ... */ }
}

class Compliant {
    private static readonly Compliant _singleton = new Compliant();
    public Compliant() { /* ... */ }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 