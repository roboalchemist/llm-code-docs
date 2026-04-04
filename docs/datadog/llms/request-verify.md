# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/request-verify.md

---
title: verify should be True
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > verify should be True
---

# verify should be True

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/request-verify`

**Language:** Python

**Severity:** Error

**Category:** Security

## Description{% #description %}

The `verify` parameter controls whether the SSL certificate should be verified during your server requests. It's strongly recommended to set this parameter to `True` which is the default value. This rule will warn you when it's detected `False` has been set.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import requests

def fetch_data():
    r = requests.get(w, verify=False, timeout=5)
```

```python
from requests import get
r = get(w, verify=False)  # verify should be True
r = get(w, verify=False, timeout=10)  # verify should be True
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
from requests import get
r = get(w)
r = get(w, timeout=10, verify=True)
```

```python
from requests import get
r = get(w)
r = get(w, timeout=10)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
