# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/if-return-no-else.md

---
title: when an if condition returns an value, else is not necessary
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > when an if condition returns an value, else is not necessary
---

# when an if condition returns an value, else is not necessary

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/if-return-no-else`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

If the code in the `if` branch returns a value, do not have the `else` branch present.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
if bla:
	foo()
	return 1
else:  # unnecessary, remove the else branch
	return 2
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
if bla:
	foo()
	return 1
elif bar:
	return 2
```

```python
if bla:
	foo()
	return 1
return 2
```

```python
if bla:
	foo()
else:
	return 2
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 