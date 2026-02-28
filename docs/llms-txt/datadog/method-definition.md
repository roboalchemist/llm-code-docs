# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-inclusive/method-definition.md

---
title: Check function definition language
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check function definition language
---

# Check function definition language

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-inclusive/method-definition`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Avoid using words such as `blacklist`, `whitelist`, `slave` or `master` in method names. Consider using more inclusive wording in your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
abstract class Motorcycle
{
    public void BlackList() { }

    protected void AddGas(int blacklistNames) {}


}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
abstract class Motorcycle
{
    public void Denylist() { }

    protected void AddGas(int denylistNames) {}


}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
