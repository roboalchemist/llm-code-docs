# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/deserialize-untrusted-data.md

---
title: avoid unsafe function to (de)serialize data
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > avoid unsafe function to (de)serialize data
---

# avoid unsafe function to (de)serialize data

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/deserialize-untrusted-data`

**Language:** Python

**Severity:** Notice

**Category:** Security

**CWE**: [502](https://cwe.mitre.org/data/definitions/502.html)

## Description{% #description %}

Do not deserialize untrusted data. Make sure you use alternatives to check that the data can be deserialized safely. There is no workaround around this: unless you **really** trust the data source, it's better to use another way to exchange data, such as an API or other protocols such as [protobuf](https://developers.google.com/protocol-buffers) or [thrift](https://thrift.apache.org/).

### Learn More{% #learn-more %}

- [Unsafe Deserialization in Python (CWE-502)](https://www.codiga.io/blog/python-unsafe-deserialization/)

- [CWE-502: Deserialization of Untrusted Data](https://cwe.mitre.org/data/definitions/502.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import marshal
person = {"name":"xyz", "age":22, "marks":[45,56,78]}
data = marshal.dumps(person)
obj = marshal.loads(data)
```

```python
import pickle

data = pickle.loads(data)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import pickle

data = pickle.loads(data)
```

```python
data = pickle.loads(data)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 