# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/comparison-constant-left.md

---
title: in comparisons, variables must be left
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > in comparisons, variables must be left
---

# in comparisons, variables must be left

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/comparison-constant-left`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In a comparison that compare a variable with a value, put the variable on the left side of the comparison expression.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
if 1 <= i:  # use i >= 1
  pass
```

```python
if 1.0 <= i:  # use i >= 1.0
  pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
if i >= 1:
  pass

if 0 < nextSx <= len(subject):
    px = nextPx
    sx = nextSx

if 1 in ctx:
  print("foo")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
