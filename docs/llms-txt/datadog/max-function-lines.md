# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/swift-code-style/max-function-lines.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-code-style/max-function-lines.md

---
title: Functions must be less than 200 lines
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Functions must be less than 200 lines
---

# Functions must be less than 200 lines

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-code-style/max-function-lines`

**Language:** Python

**Severity:** Error

**Category:** Code Style

## Description{% #description %}

This rule stipulates that functions in Python should not exceed 200 lines of code. The primary reason for this rule is to promote readability and maintainability of the code. When functions are concise and focused, they are easier to understand, test, and debug.

Long functions often indicate that a single function is doing too much. Adhering to the Single Responsibility Principle (SRP) can help avoid this. SRP states that a function should have only one reason to change. If a function is doing more than one thing, it can usually be split into several smaller, more specific functions.

In practice, to adhere to this rule, you can often break up long functions into smaller helper functions. If a piece of code within a function is independent and can be isolated, it is a good candidate to be moved into a separate function. This also increases code reusability. For instance, if a function `process_data()` is too long, you can identify independent tasks within it - such as `clean_data()`, `transform_data()`, and `save_data()` - and create separate functions for them. This makes the code easier to reason about and test, and promotes good coding practices.

## Arguments{% #arguments %}

- `max-lines`: Maximum number of lines. Default: 200.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def myfunction():
	foo()
	bar()











	










	










	










	










	










	










	










	










	










	










	










	










	










	










	










	










	










	










	










	
	pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def myfunction(args):
	foo()
	bar()
	pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 