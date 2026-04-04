# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/jinja-autoescape.md

---
title: Auto escape should be set to true
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Auto escape should be set to true
---

# Auto escape should be set to true

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/jinja-autoescape`

**Language:** Python

**Severity:** Notice

**Category:** Security

**CWE**: [94](https://cwe.mitre.org/data/definitions/94.html)

## Description{% #description %}

By default, jinja2 is not autoescaping. This can lead to XSS attacks. The `autoescape` parameter should always be `True`.

#### Learn More{% #learn-more %}

- [OWASP XSS](https://owasp.org/www-community/attacks/xss/)
- [CWE-94 - Improper Control of Generation of Code](https://cwe.mitre.org/data/definitions/94.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import jinja2
env = jinja2.Environment(
    loader=PackageLoader("yourapp"),
    autoescape=False # should be True
)
```

```python
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("yourapp"),
    autoescape=False # should be True
)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import jinja2
env = Environment(
    loader=PackageLoader("yourapp"),
    autoescape=True
)
```

```python
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("yourapp"),
    autoescape=select_autoescape()
)
```

```python
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("yourapp"),
    autoescape=True
)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
