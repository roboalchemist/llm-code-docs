# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/use-standard-crypto.md

---
title: Use standard crypto algorithms
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use standard crypto algorithms
---

# Use standard crypto algorithms

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/use-standard-crypto`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

Implementing your hash/cryptographic algorithm may lead to errors and potential vulnerabilities. Always use proven algorithms that are available in the C# library ecosystem.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class CustomHash : HashAlgorithm {
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
