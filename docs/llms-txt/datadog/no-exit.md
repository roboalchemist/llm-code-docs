# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/no-exit.md

---
title: do not use exit()
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use exit()
---

# do not use exit()

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/no-exit`

**Language:** Python

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Use `sys.exit()` instead of `exit()`. Exit is a [builtin](https://docs.python.org/3/library/constants.html#exit) and done mostly for the console. `sys.exit()` is done for program with a proper return argument ([see documentation](https://docs.python.org/3/library/sys.html#sys.exit)).

#### Learn More{% #learn-more %}

- [Python documentation for `sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
print("bla")
exit(0)  # use sys.exit() instead
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import sys
print("bla")
sys.exit(0)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
