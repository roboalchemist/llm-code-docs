# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-bare-raise.md

---
title: Do not use a raise statement without a specific exception
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use a raise statement without a specific exception
---

# Do not use a raise statement without a specific exception

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-bare-raise`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Never use a bare raise and always use a specific exception. Using a specific exception helps you distinguish errors in your program and have appropriate error handling code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def myfunc():
  raise  # should use specific exception

if foo:
  raise
else:
  func1()
  raise

for v in list:
  do_something()
  raise
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def myfunc():
  raise MyException

try:
  foo()
except MyException:
  raise  # re-raise exception
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 