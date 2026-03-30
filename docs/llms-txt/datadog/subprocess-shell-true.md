# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/subprocess-shell-true.md

---
title: shell argument leads to unnecessary privileges
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > shell argument leads to unnecessary privileges
---

# shell argument leads to unnecessary privileges

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/subprocess-shell-true`

**Language:** Python

**Severity:** Warning

**Category:** Security

**CWE**: [78](https://cwe.mitre.org/data/definitions/78.html)

## Description{% #description %}

Never invoke `subprocess.Popen` with `shell = True` leads to unnecessary privileges and access to the underlying execution runtime. Execution with `shell = True` should clearly be verified and checked for code in production.

#### Learn More{% #learn-more %}

- [CWE-250](https://cwe.mitre.org/data/definitions/250.html) - Execution with Unnecessary Privileges
- [CWE-657](https://cwe.mitre.org/data/definitions/657.html) - Violation of Secure Design Principles

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import subprocess

def find_dogweb_packages():
    # setuptools.find_packages is too slow since it walks the entire codebase, including Javascript code.
    # This is an equivalent but optimized function, specific to our codebase, listing all the available
    # packages.

    # Look for __init__.py files using fast UNIX tools
    r = subprocess.Popen(
        "find %s -name '__init__.py'" % " ".join(MODULE_PATHS), shell=True, stdout=subprocess.PIPE
    ).stdout.read()
```

```python
from subprocess import Popen
Popen('/bin/ls %s' % ('something',), shell=True)
```

```python
import subprocess
subprocess.Popen('/bin/ls %s' % ('something',), shell=True)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
subprocess.Popen('/bin/ls %s' % ('something',), shell=False)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
