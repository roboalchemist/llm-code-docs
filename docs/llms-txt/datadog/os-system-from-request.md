# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/os-system-from-request.md

---
title: Command coming from incoming request
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Command coming from incoming request
---

# Command coming from incoming request

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-django/os-system-from-request`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [20](https://cwe.mitre.org/data/definitions/20.html)

## Description{% #description %}

Execute a process using unsanitized and unvalidated user-inputs. The user data should be sanitized and validated before being used to launch a new process.

#### Learn More{% #learn-more %}

- [CWE-20: Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import os

def execute_command(request):
    cmd = request.GET.get("cmd")
    print("foobar")
    os.system(cmd)

    bli = os.system(cmd)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import os
import shlex

def execute_command(request):
    cmd = request.GET.get("cmd")
    print("foobar")
    os.system(shlex.escape(cmd))
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 