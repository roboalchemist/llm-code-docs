# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/open-file-unsanitized-data.md

---
title: Use of unsanitized data to open file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use of unsanitized data to open file
---

# Use of unsanitized data to open file

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/open-file-unsanitized-data`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [22](https://cwe.mitre.org/data/definitions/22.html)

## Description{% #description %}

Use of unsanitized from incoming request, leading to potential data leak and lack of control of the service. Do not use unsanitized data to control file operations. The code should check any incoming data and make sure it's safe to use it.

#### Learn More{% #learn-more %}

- [CWE-22: CWE-22: Improper Limitation of a Pathname to a Restricted Directory](https://cwe.mitre.org/data/definitions/22.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
@app.route("/read")
def read_file():
    filename = request.args.get("filename")
    if not filename:
        return "Missing 'filename' parameter", 400
    try:
        with open(filename, "r") as f:
            content = f.read()
            return f"<pre>{content}</pre>"
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
```

```python
import flask
import requests

app = flask.Flask(__name__)


@app.route("/route/to/resource/<resource_id>")
def resource1(resource_id):
    with open(resource_id) as f:
        pass
    with open(f"/path/to/{resource_id}") as f:
        pass
    with open("/path/to/{0}".format(resource_id)) as f:
        pass
    with open("/path/to/{0}".other(resource_id)) as f:
        pass

@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    file1 = open(resource_id)
    file2 = open(f"/path/to/{resource_id}")
    file3 = open("/path/to/{0}".format(resource_id))


@app.route("/route/to/resource")
def resource2():
    resource_id = flask.request.args.get("resource_id")
    file1 = open(resource_id)
    file2 = open(f"/path/to/{resource_id}")
    file3 = open("/path/to/{0}".format(resource_id))

from flask import Flask, request, render_template


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/")
def start():
    return render_template("index.html")
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import flask
import requests

app = flask.Flask(__name__)

@app.route("/route/to/resource/<resource_id>")
def resource2(resource_id):
    sanitized_resource_id = sanitize(resource_id)
    file1 = open(sanitized_resource_id)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
