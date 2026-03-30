# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/ambiguous-variable-name.md

---
title: make sure variable names are readable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > make sure variable names are readable
---

# make sure variable names are readable

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/ambiguous-variable-name`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In some fonts, some characters are indistinguishable from the numerals one and zero, such as, O looks like a zero. Use characters that are not ambiguous.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
I = 1  # use i instead
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def i():
    pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
