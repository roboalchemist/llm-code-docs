# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/unreachable-code.md

---
title: avoid unreachable code
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > avoid unreachable code
---

# avoid unreachable code

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/unreachable-code`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Avoid unreachable code. If the code cannot be reached because of a coding mistake, fix the business logic. If the code should not be used, remove it.

#### Learn More{% #learn-more %}

- [Carnegie Mellon University: Avoid having unreachable code](https://wiki.sei.cmu.edu/confluence/display/android/Avoid+having+unreachable+code)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def foo():
  return 3
  foo()  # unreachable code
  pass  # unreachable code
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def foo():
	foo()
	pass
	return 3
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 