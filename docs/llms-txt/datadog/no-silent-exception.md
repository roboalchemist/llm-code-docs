# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-silent-exception.md

---
title: Do not ignore Exception with a pass statement
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not ignore Exception with a pass statement
---

# Do not ignore Exception with a pass statement

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-silent-exception`

**Language:** Python

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Using the `pass` statement in an exception block ignores the exception. Exceptions should never be ignored. Instead, the user must add code to notify an exception occurred and attempt to handle it or recover from it.

The exception to this rule is the use of `StopIteration` or `StopAsyncIteration` when implementing a custom iterator (as those errors are used to acknowledge the end of a successful iteration).

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
a = 2
b = 0
try:
  c = a / b
# should use a regular statement and not ignore the exception
except Exception as e:
  pass
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
a = 2
b = 0
try:
  c = a / b
except ZeroDivisionError as e:
  print(e)
  pass

try:
  get_config_values()
except FileNotFoundError:
  # (Comment explaining why no handling happens here)
  pass

try:
  do_iteration()
# Handling the iterator's successful conclusion is OK
except StopIteration:
  pass

try:
  do_async_iteration()
# Handling the iterator's successful conclusion is OK
except StopAsyncIteration:
  pass
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 