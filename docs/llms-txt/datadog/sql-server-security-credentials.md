# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/sql-server-security-credentials.md

---
title: do not pass hardcoded credentials
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > do not pass hardcoded credentials
---

# do not pass hardcoded credentials

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/sql-server-security-credentials`

**Language:** Python

**Severity:** Error

**Category:** Security

## Description{% #description %}

Hardcoding database credentials directly in your source code is a security risk as anyone with access to your source code and see your credentials. It's strongly recommended to use a different approach that limits the exposure of your credentials.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import psycopg2

conn = psycopg2.connect(database="db_name",
                        host="db_host",
                        user="db_user",
                        password="db_pass", # hardcoded password
                        port="db_port")
```

```python
import mysql.connector

connection = mysql.connector.connect(
  host=host,
  user=user,
  passwd=f"password", # hardcoded password
  database=database,
  charset='utf8mb4',
  use_pure=True,
  connection_timeout=5)
```

```python
import mysql.connector

connection = mysql.connector.connect(
  host=host,
  user=user,
  passwd="password", # hardcoded password
  database=database,
  charset='utf8mb4',
  use_pure=True,
  connection_timeout=5)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import mysql.connector

connection = mysql.connector.connect(
  host=host,
  user=user,
  passwd=password,
  database=database,
  charset='utf8mb4',
  use_pure=True,
  connection_timeout=5)
```

```python
import mysql.connector

connection = mysql.connector.another_function(
  host=host,
  user=user,
  passwd=f"password",
  database=database,
  charset='utf8mb4',
  use_pure=True,
  connection_timeout=5)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
