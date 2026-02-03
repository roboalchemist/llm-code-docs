# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-if-true.md

---
title: do not compare to True in a condition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not compare to True in a condition
---

# do not compare to True in a condition

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-if-true`

**Language:** Python

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Do not use `variable == True`, just use `variable`. Comparing against `True` makes the code more complicated to read.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
if foo == True:  # just used if foo
  print("bar")
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
if foo:
  print("bar")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 