# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/sqlalchemy-injection.md

---
title: Use of unsanitized data to issue SQL queries
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use of unsanitized data to issue SQL queries
---

# Use of unsanitized data to issue SQL queries

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/sqlalchemy-injection`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [89](https://cwe.mitre.org/data/definitions/89.html)

## Description{% #description %}

Use of unsanitized data from incoming requests in SQL queries may lead to SQL injections. Instead, the data should be filtered and sanitized before use, making sure all potential SQL injections are avoided.

#### Learn More{% #learn-more %}

- [CWE-89: Improper Neutralization of Special Elements used in an SQL Command](https://cwe.mitre.org/data/definitions/89.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import flask
import requests

app = flask.Flask(__name__)

@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    file1 = query.order_by(resource_id)
    file2 = query.having(f"{resource_id}")

@app.route("/route/to/resource/<resource_id>")
def resource3(resource_id):
    file3 = query.filter("{0}".format(resource_id))

@app.route("/route/to/resource")
def resource2():
    resource_id = flask.request.args.get("resource_id")
    file1 = query.group_by(resource_id)
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import flask
import requests

app = flask.Flask(__name__)

@app.route("/route/to/resource")
def resource2():
    resource_id = flask.request.args.get("resource_id")
    file1 = query.group_by(sanitize(resource_id))
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
