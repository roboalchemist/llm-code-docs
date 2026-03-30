# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/no-unsafe-reflection.md

---
title: Avoid external input controlling reflection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid external input controlling reflection
---

# Avoid external input controlling reflection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/no-unsafe-reflection`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [470](https://cwe.mitre.org/data/definitions/470.html)

## Description{% #description %}

No description found

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class ExampleController : Controller
{
    public IActionResult Apply(string EffectName)
    {
        var EffectInstance = Activator.CreateInstance(null, EffectName); // Noncompliant
        object EffectPlugin = EffectInstance.Unwrap();

        if (((IEffect)EffectPlugin).ApplyFilter())
        {
            return Ok();
        }
        else
        {
            return Problem();
        }
    }
}

public interface IEffect
{
    bool ApplyFilter();
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
public class ExampleController : Controller
{
    private static readonly string[] EFFECT_ALLOW_LIST = {
        "SepiaEffect",
        "BlackAndWhiteEffect",
        "WaterColorEffect",
        "OilPaintingEffect"
    };

    public IActionResult Apply(string EffectName)
    {
        if (!EFFECT_ALLOW_LIST.Contains(EffectName))
        {
            return BadRequest("Invalid effect name. The effect is not allowed.");
        }

        var EffectInstance = Activator.CreateInstance(null, EffectName);
        object EffectPlugin = EffectInstance.Unwrap();

        if (((IEffect)EffectPlugin).ApplyFilter())
        {
            return Ok();
        }
        else
        {
            return Problem();
        }
    }
}

public interface IEffect
{
    bool ApplyFilter();
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
