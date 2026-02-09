# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-pandas/import-as-pd.md

---
title: Import pandas according to coding guidelines
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Import pandas according to coding guidelines
---

# Import pandas according to coding guidelines

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-pandas/import-as-pd`

**Language:** Python

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The `pandas` library is generally imported using the following code snippet.

```python
import pandas as pd
```

It is good practice to ensure that all pandas import are done this way. This rule ensures that all code uses this pattern.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import pandas # should use import pandas as pd


import pandas as foo


import foo as bar
```

```python
from pandas import something # should use import pandas as pd
```

```python
import pandas as something # should use import pandas as pd
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import pandas as pd # should use import pandas as pd
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 