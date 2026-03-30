# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/insecure-jwt.md

---
title: Ensure JWT signatures are verified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure JWT signatures are verified
---

# Ensure JWT signatures are verified

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/insecure-jwt`

**Language:** Python

**Severity:** Notice

**Category:** Security

**CWE**: [287](https://cwe.mitre.org/data/definitions/287.html)

## Description{% #description %}

Use `"verify_signature": False` when decoding a JWT bypasses security and may authenticate users that should not be authenticated.

**See Also**

- [CWE-287 - Improper Authentication](https://cwe.mitre.org/data/definitions/287.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import jwt

def insecure_verify(token):
    decoded = jwt.decode(token, verify=False)
    print decoded
    return True
```

```python
import jwt

jwt.decode(encoded, options={"verify_signature": False})
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import jwt

jwt.decode(encoded, bla={"verify_signature": False})

jwt.decode(encoded, options={"foobar": False})
```

```python
import jwt

jwt.decode(encoded, options={"verify_signature": True})
```

```python
jwt.decode(encoded, options={"verify_signature": False})
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
