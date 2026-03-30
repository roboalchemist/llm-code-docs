# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/no-render-template-string.md

---
title: Do not use template created with strings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use template created with strings
---

# Do not use template created with strings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/no-render-template-string`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [96](https://cwe.mitre.org/data/definitions/96.html)

## Description{% #description %}

Using templates created with string leads to server-side injection. Use template based on files.

#### Learn More{% #learn-more %}

- [CWE-96: Improper Neutralization of Directives in Statically Saved](https://cwe.mitre.org/data/definitions/96.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import os
from functools import wraps
from flask import request, redirect, url_for, render_template_string


API_KEY = os.environ.get('VULN_FLASK_APP_API_KEY')

# Decorator to check if user is logged in
def require_api_key(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        api_key = request.cookies.get('api_key')
        if API_KEY is None or api_key == API_KEY:
            return f(*args, **kwargs)
        else:
            return render_template_string('no api key found'), 401
    return wrap
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
