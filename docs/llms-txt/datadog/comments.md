# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-inclusive/comments.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-inclusive/comments.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-inclusive/comments.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-inclusive/comments.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-inclusive/comments.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-inclusive/comments.md

---
title: Ensure comment wording is inclusive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure comment wording is inclusive
---

# Ensure comment wording is inclusive

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-inclusive/comments`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Avoid using words such as `blacklist`, `whitelist`, `slave` or `master` in comments. Consider using more inclusive wording in your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
abstract class Motorcycle
{
    // this is to get a blacklist
    public void Denylist() { }

    protected void AddGas(int denylistNames) {}


}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
abstract class Motorcycle
{
    // this is to get a denylist
    public void Denylist() { }

    protected void AddGas(int denylistNames) {}


}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 