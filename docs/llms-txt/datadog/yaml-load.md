# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/yaml-load.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/yaml-load.md

---
title: avoid deserializing untrusted YAML
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > avoid deserializing untrusted YAML
---

# avoid deserializing untrusted YAML

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/yaml-load`

**Language:** Python

**Severity:** Warning

**Category:** Security

**CWE**: [502](https://cwe.mitre.org/data/definitions/502.html)

## Description{% #description %}

Avoid deserialization of untrusted YAML data via potential unsafe `yaml.load`.

This rule checks that the `yaml` module is used and the `load` method is used. It recommends the usage of `safe_load` that prevents unsafe deserialization.

**See Also**

- [CWE-502 - Deserialization of Untrusted Data](https://cwe.mitre.org/data/definitions/502.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
from yaml import load

load("string") # should use safe_load
```

```python
import yaml

yaml.load("string") # should use safe_load
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import os

from pathlib import Path
from glob import glob
from typing import List

# Rule is not for ruamel
from ruamel.yaml import YAML

yaml = YAML()
with open("/path/to/file.yaml", "r") as f:
    values = yaml.load(f)
```

```python
import yaml

yaml.load("string", Loader=yaml.SafeLoader) # uses SafeLoader, so load is okay
```

```python
yaml.load("string")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 