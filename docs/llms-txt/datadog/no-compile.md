# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/no-compile.md

---
title: The use of compile can be insecure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > The use of compile can be insecure
---

# The use of compile can be insecure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/no-compile`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [94](https://cwe.mitre.org/data/definitions/94.html)

## Description{% #description %}

`compile()` is insecure, and passing in unsanitized data could create a vulnerability, as reported by the [official Python documentation](https://docs.python.org/3/library/functions.html#compile). Generated code should be controlled as mentioned in CWE-94.

#### Learn More{% #learn-more %}

- [CWE-94](https://cwe.mitre.org/data/definitions/94.html) - Improper Control of Generation of Code

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
x = compile('print(55)', 'test', 'eval')
exec(x)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
print(55)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 