# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-equal-unary.md

---
title: do not use operations =+ and =-
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use operations =+ and =-
---

# do not use operations =+ and =-

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-equal-unary`

**Language:** Python

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Operator `=+` and `=-` do not exist in Python. The code is valid but is unlikely doing what the developer wants to achieve.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
# =+ does not exists in Python, use n = n + 3
n =+ 3

# =- does not exists in Python, use n = n - 3
n =- 3
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
n = n + 3

n = n - 3

foo = -1
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 