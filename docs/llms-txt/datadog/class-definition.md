# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-inclusive/class-definition.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-inclusive/class-definition.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-inclusive/class-definition.md

---
title: Check class definition language
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check class definition language
---

# Check class definition language

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-inclusive/class-definition`

**Language:** C#

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Avoid using words such as `blacklist`, `whitelist`, `slave` or `master` in class names. Consider using more inclusive wording in your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class Whitelist {

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class AllowList {

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
