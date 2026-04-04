# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/import-modules-twice.md

---
title: module imported twice
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > module imported twice
---

# module imported twice

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/import-modules-twice`

**Language:** Python

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Always define a module once. Do not import the module multiple times and/or import the module using different methods. It makes the code harder to understand. Import a module once and for all with only one import mechanism.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import logging
import logging  # do not import the same module again.
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import typing
from typing import cast
```

```python
import logging
```

```python
import logging
from logging import foo # not an issue since we are using a from import
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
