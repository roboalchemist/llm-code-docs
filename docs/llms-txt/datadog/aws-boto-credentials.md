# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/aws-boto-credentials.md

---
title: use env vars over hardcoded values
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > use env vars over hardcoded values
---

# use env vars over hardcoded values

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/aws-boto-credentials`

**Language:** Python

**Severity:** Notice

**Category:** Security

**CWE**: [798](https://cwe.mitre.org/data/definitions/798.html)

## Description{% #description %}

This rule makes sure that the `boto3` library use the environments variables to authenticate instead of using hardcoded credentials. This rule checks for the `boto3.client` and `boto3.Session` calls. It addresses the [CWE-798 rule](https://cwe.mitre.org/data/definitions/798.html) - uses of hardcoded credentials in code.

#### Learn More{% #learn-more %}

- [AWS credentials](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials)
- [CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
from boto3 import client

cli = client(
    's3',
    aws_access_key_id="AGPAFOOBAR",
    aws_secret_access_key="bar",
    aws_session_token=SESSION_TOKEN
)
```

```python
import boto3 

client = boto3.client(
    's3',
    aws_access_key_id="AGPAFOOBAR",
    aws_secret_access_key="bar",
    aws_session_token=SESSION_TOKEN
)
```

```python
import boto3

client = boto3.Session(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token="foobar" # hard coded credential
)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import boto3

client = boto3.Session(
    's3',
    aws_session_token=SESSION_TOKEN
)
```

```python
import boto3

client = boto3.client(
    's3',
    aws_session_token=SESSION_TOKEN
)
```

```python
client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    aws_session_token=SESSION_TOKEN
)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 