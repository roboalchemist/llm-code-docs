# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/mktemp.md

---
title: Make sure temporary files are secure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Make sure temporary files are secure
---

# Make sure temporary files are secure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/mktemp`

**Language:** Python

**Severity:** Notice

**Category:** Security

**CWE**: [377](https://cwe.mitre.org/data/definitions/377.html)

## Description{% #description %}

Using insecure temporary files makes your program vulnerable to attacks. The official [Python documentation](https://docs.python.org/3/library/tempfile.html) reports this module being vulnerable to attacks. Instead of `mktemp`, use the secure version `mkstemp()`.

#### Learn More{% #learn-more %}

- [CWE-377 - Insecure Temporary File](https://cwe.mitre.org/data/definitions/377.html)
- [Python documentation for mktemp()](https://docs.python.org/3/library/tempfile.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
from tempfile import mktemp
mktemp(dir=self._tmp_dir)
```

```python
import tempfile
tempfile.mktemp(dir=self._tmp_dir)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
tempfile.mktemp(dir=self._tmp_dir)
```

```python
import tempfile
tempfile.mkstemp(dir=self._tmp_dir)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
