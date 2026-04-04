# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-double-unary-operator.md

---
title: do not use operator -- and ++
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use operator -- and ++
---

# do not use operator -- and ++

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-double-unary-operator`

**Language:** Python

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Operator `--` and `++` do not exists in Python. Increment or decrement the variable appropriately.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
--n  # use n = n - 1
++n  # use n = n + 1
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
n = n + 1
n = n - 1
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
