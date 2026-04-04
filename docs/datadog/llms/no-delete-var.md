# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-delete-var.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-delete-var.md

---
title: Avoid using delete on variables directly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using delete on variables directly
---

# Avoid using delete on variables directly

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-delete-var`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

**CWE**: [480](https://cwe.mitre.org/data/definitions/480.html)

## Description{% #description %}

The `delete` operator is designed to remove properties from objects in JavaScript. When used correctly, it can help manage object properties. However, using the `delete` operator on anything other than object properties can lead to unpredictable behavior.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
delete x
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
delete x.prop;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
