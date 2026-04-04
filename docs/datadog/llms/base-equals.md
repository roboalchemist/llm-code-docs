# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/base-equals.md

---
title: 'Enforces that base is object when using base.Equals '
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforces that base is object when using base.Equals
---

# Enforces that base is object when using base.Equals

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/base-equals`

**Language:** C#

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Using `base.Equals` can be dangerous when the base is not an `object` because the new base class can override `Equals`, leading to unexpected behavior. This rule prevents the use of `base.Equals` in a class where the base is not an `object`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class NonCompliant : Compliant
{
    private int bar;

    public override bool Equals(object other)
    {
        bool eq1;
        eq1 = base.Equals(other);
        var eq2 = base.Equals(other);
        if (base.Equals(other))
        {
            return true;
        }
        return this.bar == ((NonCompliant)other).bar;
    }
}

class Compliant
{
    private int foo;

    public override bool Equals(object other)
    {
        if (base.Equals(other))
        {
            return true;
        }
        return this.foo == ((Compliant)other).foo;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class Compliant
{
    private int foo;

    public override bool Equals(object other)
    {
        if (base.Equals(other))
        {
            return true;
        }
        return this.foo == ((Compliant)other).foo;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
