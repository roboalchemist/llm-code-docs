# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/logging-no-format.md

---
title: do not use format string with logging functions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not use format string with logging functions
---

# do not use format string with logging functions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/logging-no-format`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Avoid using format string with the `format` method when logging information.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import logging
import shlex

logging.info("error {0} {1}".format(plop, plip))  # use instead logging.info("error %s", plop)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import logging

logging.info("wfwef")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
