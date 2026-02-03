# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/argument-same-name.md

---
title: do not have arguments with the same name
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not have arguments with the same name
---

# do not have arguments with the same name

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/argument-same-name`

**Language:** Python

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

Function parameters cannot have the same name. Each function parameter must have a distinct name.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def foo(bar, bar: int, bar = 3):  # use another name for the second argument
	pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def foo(bar, baz):
	pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 