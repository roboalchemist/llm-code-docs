# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/requests-timeout.md

---
title: no timeout was given on call to external resource
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > no timeout was given on call to external resource
---

# no timeout was given on call to external resource

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/requests-timeout`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [1088](https://cwe.mitre.org/data/definitions/1088.html)

## Description{% #description %}

Access to remote resources should always use a timeout and appropriately handle the timeout and recovery. When using `requests.get`, `requests.put`, `requests.patch`, etc. - we should always use a `timeout` as an argument.

#### Learn More{% #learn-more %}

- [CWE-1088 - Synchronous Access of Remote Resource without Timeout](https://cwe.mitre.org/data/definitions/1088.html)
- [Python Best Practices: always use a timeout with the requests library](https://www.codiga.io/blog/python-requests-timeout/)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
from requests import get, put
r = get(w, verify=False) # missing a timeout
r = get(w, verify=False, timeout=10)

def bla():
    r = get(w, verify=False)
```

```python
import requests
r = requests.put(w, verify=False) # missing a timeout
```

```python
import requests
r = requests.get(w, verify=False) # missing a timeout
r = requests.get(w, verify=False, timeout=10)



def foo():
    r = requests.get(w, verify=False) # missing a timeout
    
    if bar:
        r = requests.get(w, verify=False)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
r = requests.put(w, verify=False)
```

```python
import requests
r = requests.get(w, verify=False, timeout=5)
r = requests.get(w, verify=False, timeout=10)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 