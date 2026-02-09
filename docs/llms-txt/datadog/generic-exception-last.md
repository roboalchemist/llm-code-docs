# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/generic-exception-last.md

---
title: If using generic exception, it should be last
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > If using generic exception, it should be last
---

# If using generic exception, it should be last

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/generic-exception-last`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

When multiple exceptions are caught, the generic `Exception` must be caught last. Catching `Exception` is very generic and if placed before specific exceptions, it will caught all exceptions and specific exception handlers will not be caught.

For this reason, generic `Exception` must be the last to be handled to let specific exception handlers to be triggered/executed.

#### Learn More{% #learn-more %}

- [Python tutorials on errors](https://docs.python.org/3/tutorial/errors.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
try:
	pass
except Exception:
	pass
except FileNotFound as e:
	pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
try:
	pass
except MyError:
	pass
except Exception as e:
	pass
```

```python
try:
	pass
except MyError:
	pass
except FileNotFound as e:
	pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 