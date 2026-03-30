# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/os-system-unsanitized-data.md

---
title: Use of unsanitized data to create processes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use of unsanitized data to create processes
---

# Use of unsanitized data to create processes

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/os-system-unsanitized-data`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [78](https://cwe.mitre.org/data/definitions/78.html)

## Description{% #description %}

Use of unsanitized from incoming request to execute a command may lead to command injection. It is highly recommended that data is checked and sanitized before use.

#### Learn More{% #learn-more %}

- [CWE-78: roper Neutralization of Special Elements used in an OS](https://cwe.mitre.org/data/definitions/78.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import flask
import os

app = flask.Flask(__name__)

@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    file1 = subprocess.call(resource_id)
    file2 = subprocess.capture_output(f"/path/to/{resource_id}")

@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    file4 = os.system("/path/to/{0}".format(resource_id))
    os.system(request.remote_addr)
    bla = os.system(request.foo)

@app.route("/route/to/resource")
def resource2():
    resource_id = flask.request.args.get("resource_id")
    subprocess.call(resource_id)
    subprocess.run(["command", resource_id])

@app.route("/route/to/resource")
def resource3():
    resource_id = request.args['resource_id'];
    subprocess.call(resource_id)
    subprocess.run(["command", resource_id])
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import flask
import os

app = flask.Flask(__name__)

@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    file1 = subprocess.call(sanitize(resource_id))
    file2 = subprocess.capture_output(f"/path/to/{sanitize(resource_id)}")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
