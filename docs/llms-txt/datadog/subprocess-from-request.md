# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-django/subprocess-from-request.md

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

**ID:** `python-django/subprocess-from-request`

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
import subprocess

def execute_command(request):
    cmd = request.GET.get("cmd")
    print("foobar")
    subprocess.run(cmd)
    subprocess.call(cmd)
    subprocess.capture_output(cmd)
    subprocess.call(["bash", cmd])

    bli = subprocess.run(cmd)
    bla = subprocess.call(cmd)
    ble = subprocess.capture_output(cmd)
    blo = subprocess.call(["bash", cmd])
    blip = subprocess.call("bash {0}".format(cmd))
    blop = subprocess.call("bash " + cmd)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import subprocess

def execute_command(request):
    cmd = request.GET.get("cmd")
    print("foobar")
    subprocess.run(shlex.escape(cmd))
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
