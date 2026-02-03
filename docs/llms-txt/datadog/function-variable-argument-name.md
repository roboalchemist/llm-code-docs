# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/function-variable-argument-name.md

---
title: Do not assign to function arguments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not assign to function arguments
---

# Do not assign to function arguments

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/function-variable-argument-name`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

A function parameter should only be read and not be modified. If your intent is to modify the value of the parameter, return the value in the function and handle the new value in the caller of the function.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def func(arg1, arg2):
	arg1 = foo  # assign to a variable that is an argument
```

```python
def func(arg1, arg2):
	(arg1, arg3, arg2) = foo  # assign to a variable that is an argument
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def func(arg1, arg2):
	arg3 = foo
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 