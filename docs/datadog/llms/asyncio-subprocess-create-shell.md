# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/asyncio-subprocess-create-shell.md

---
title: Unsafe execution of shell commands
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Unsafe execution of shell commands
---

# Unsafe execution of shell commands

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/asyncio-subprocess-create-shell`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [78](https://cwe.mitre.org/data/definitions/78.html)

## Description{% #description %}

Detect unsafe shell execution in the asyncio framework. When we invoke the shell, we should make sure that the data is safe and secure. Use `shlex` to sanitize user inputs.

#### Learn More{% #learn-more %}

- [`Python shlex() module`](https://docs.python.org/3/library/shlex.html)
- [CWE 78 - Improper Neutralization of Special Elements used in an OS Command](https://cwe.mitre.org/data/definitions/78.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import asyncio

def handler(event, context):
    # Should sanitize arguments
    async_loop.run_until_complete(async_loop.create_subprocess_shell("mycommand"))
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import asyncio
import shlex

def handler(event, context):
    # Should sanitize arguments
    async_loop.run_until_complete(async_loop.create_subprocess_shell(shlex.quote("mycommand")))
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
