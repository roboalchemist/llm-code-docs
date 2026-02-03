# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/os-environ-no-assign.md

---
title: assigning to os.environ does not clear the environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > assigning to os.environ does not clear the environment
---

# assigning to os.environ does not clear the environment

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/os-environ-no-assign`

**Language:** Python

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

Assigning to `os.environ` does not clear the environment. To clear the environment, use `os.environ.clear()`

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import os

os.environ = {}  # use os.environ.clear
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import os

os.environ.clear()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 