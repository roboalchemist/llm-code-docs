# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/function-already-exists.md

---
title: a function must be defined only once
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > a function must be defined only once
---

# a function must be defined only once

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/function-already-exists`

**Language:** Python

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

A function should only be defined once. Make sure you use unique name for each function in a module.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python

def my_function():
  pass

def foo():
  pass

def my_function(): # function already defined
  pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python

def my_function():
  pass

def foo():
  pass

def my_other_function():
  pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 