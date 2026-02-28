# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-flask/avoid-ssrf.md

---
title: Avoid potential SSRF attacks in your Python code
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid potential SSRF attacks in your Python code
---

# Avoid potential SSRF attacks in your Python code

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-flask/avoid-ssrf`

**Language:** Python

**Severity:** Error

**Category:** Security

**CWE**: [918](https://cwe.mitre.org/data/definitions/918.html)

## Description{% #description %}

This rule helps prevent Server-Side Request Forgery (SSRF) attacks. SSRF attacks manipulate the server to make HTTP requests to an arbitrary domain of the attacker's choosing. This can lead to unauthorized actions or access to data within the server, potentially exposing sensitive information.

This rule is important to enforce because SSRF attacks can cause significant damage, allowing attackers to bypass firewall protections, perform actions on behalf of the server, or gain unauthorized access to data. The impact of such an attack can be severe, leading to data breaches or server control takeover.

Good coding practices to avoid SSRF attacks include validating and sanitizing user inputs and limiting the server's ability to initiate outbound requests.

## Learn More{% #learn-more %}

- [OWASP Page](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
@app.route("/cmd", methods=['POST'])
def cmd():
    filename = request.form['filename']
    try:
        if "http" not in str(urlparse(filename).scheme):
            host = request.url[:-4]
            filename = host+"/static/" + filename
            result = eval(requests.get(filename).text)
            return render_template("index.html", result=result)
        else:
            result = eval(requests.get(filename).text)
            return render_template("index.html", result=result)
    except Exception:
        return render_template("index.html", result="Unexpected error during the execution of the predefined command.")
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import requests
from flask import request, render_template
from urllib.parse import urlparse

@app.route("/cmd", methods=['POST'])
def cmd():
    filename = request.form.get('filename')

    try:
        if not filename or len(filename) > 255:
            raise ValueError("Invalid filename")

        if any(c in filename for c in [';', '&', '|', '$', '<', '>', '`']):
            raise ValueError("Invalid filename")

        parsed_url = urlparse(filename)
        if parsed_url.scheme not in ["http", "https"]:
            host = request.url_root.rstrip('/')
            filename = f"{host}/static/{filename}"

        response = requests.get(filename)
        response.raise_for_status()
        result = response.text

        return render_template("index.html", result=result)
    except Exception as e:
        return render_template("index.html", result="Unexpected error during the execution of the predefined command.")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
