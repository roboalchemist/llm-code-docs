# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-best-practices/import-single-module.md

---
title: only one module to import per import statement
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > only one module to import per import statement
---

# only one module to import per import statement

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-best-practices/import-single-module`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Import using the `import` keyword should be done on separate lines.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import os, sys  # when using an import statement, import one module at a time
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
from collections.abc import Mapping, Sequence
import os
import sys
from typing import Any, NewType
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 