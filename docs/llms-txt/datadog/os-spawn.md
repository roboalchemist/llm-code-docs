# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/os-spawn.md

---
title: Call of a spawn process without sanitization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Call of a spawn process without sanitization
---

# Call of a spawn process without sanitization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/os-spawn`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [78](https://cwe.mitre.org/data/definitions/78.html)

## Description{% #description %}

Detect unsafe shell execution with the `os` module. We should ensure the command is safe before execution. Use `shlex` to sanitize user inputs.

#### Learn More{% #learn-more %}

- [Python `os.spawn*()` documentation](https://docs.python.org/3/library/os.html#os.spawnl)
- [`Python shlex() module`](https://docs.python.org/3/library/shlex.html)
- [CWE 78 - Improper Neutralization of Special Elements used in an OS Command](https://cwe.mitre.org/data/definitions/78.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import os

directory = "/tmp"

# Use of unsanitized data to create a process
os.spawnl(os.P_WAIT, "/bin/ls")
os.spawnle(os.P_WAIT, "/bin/ls")
os.spawnlp(os.P_WAIT, "/bin/ls")
os.spawnlpe(os.P_WAIT, "/bin/ls")
os.spawnv(os.P_WAIT, "/bin/ls")
os.spawnve(os.P_WAIT, "/bin/ls")
os.spawnvp(os.P_WAIT, "/bin/ls")
os.spawnvpe(os.P_WAIT, "/bin/ls")


os.spawnvpe(os.P_WAIT, "/bin/ls " + directory)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import os
import shlex

# Use of shlex() to sanitize data
os.spawnl(os.P_WAIT, shlex.escape("/bin/ls"))
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 