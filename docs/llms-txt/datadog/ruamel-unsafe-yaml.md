# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/ruamel-unsafe-yaml.md

---
title: Do not use insecure YAML deserialization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use insecure YAML deserialization
---

# Do not use insecure YAML deserialization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/ruamel-unsafe-yaml`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [502](https://cwe.mitre.org/data/definitions/502.html)

## Description{% #description %}

Unsafe YAML deserialization. Make sure to use safe deserialization methods to avoid execution or arbitrary code.

#### Learn More{% #learn-more %}

- [ruamel.yaml documentation](https://yaml.readthedocs.io/en/latest/basicuse.html?highlight=typ)
- [CWE 502 - Deserialization of Untrusted Data](https://cwe.mitre.org/data/definitions/502.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
from ruamel.yaml import YAML

foo = YAML(typ='unsafe')

def myfunction(arg):
    bar = YAML(typ='base')
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
foo = YAML(typ='unsafe')

def myfunction(arg):
    bar = YAML(typ='base')
```

```python
from ruamel.yaml import YAML

default = YAML()

rt = YAML(typ='rt')

safe = YAML(typ='safe')
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 