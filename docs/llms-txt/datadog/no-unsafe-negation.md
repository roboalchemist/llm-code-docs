# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-unsafe-negation.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-unsafe-negation.md

---
title: Avoid negating the left operand of relational operators
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid negating the left operand of relational operators
---

# Avoid negating the left operand of relational operators

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-unsafe-negation`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Negation of the left-hand side of an expression is often unintended.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
!a in b
(!a in b)
!(a) in b
!a instanceof b
(!a instanceof b)
!(a) instanceof b
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
a in b
a in b === false
!(a in b);
(!a) in b
a instanceof b
a instanceof b === false;
!(a instanceof b);
(!a) instanceof b;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 