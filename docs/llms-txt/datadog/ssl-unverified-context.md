# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/ssl-unverified-context.md

---
title: should not bypass certificate verification
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > should not bypass certificate verification
---

# should not bypass certificate verification

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/ssl-unverified-context`

**Language:** Python

**Severity:** Notice

**Category:** Security

**CWE**: [295](https://cwe.mitre.org/data/definitions/295.html)

## Description{% #description %}

The call to `_create_unverified_context` from the ssl module bypass certificates verification. It should not be used and instead, certificates must be verified.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import xmlrpclib
import ssl

test = xmlrpclib.ServerProxy('https://admin:bz15h9v9n@localhost:9999/API',
                             verbose=False, use_datetime=True, 
                             context=ssl._create_unverified_context()) 
test.list_satellites()
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import xmlrpclib
import ssl

test = xmlrpclib.ServerProxy('https://admin:bz15h9v9n@localhost:9999/API',
                             verbose=False, use_datetime=True)
test.list_satellites()
```

```python
import xmlrpclib

test = xmlrpclib.ServerProxy('https://admin:bz15h9v9n@localhost:9999/API',
                             verbose=False, use_datetime=True, 
                             context=ssl._create_unverified_context())
test.list_satellites()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 