# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/init-no-return-value.md

---
title: No return in an __init__ function
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > No return in an __init__ function
---

# No return in an __init__ function

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/init-no-return-value`

**Language:** Python

**Severity:** Info

**Category:** Error Prone

## Description{% #description %}

The `__init__` method (and the `__new__` method) should never return a non-`None` value.

#### Learn More{% #learn-more %}

- [`__init__` function on the Python datamodel documentation](https://docs.python.org/3/reference/datamodel.html#object.__init__)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
class Foo:
	def __init__(self):
		#  __init__ should not return a value
		return 3

	def my_method():
		return 10
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
class Foo:
	def __init__(self):
		pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 