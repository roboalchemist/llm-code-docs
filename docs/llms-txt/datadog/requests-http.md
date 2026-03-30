# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/requests-http.md

---
title: Do not make http calls without encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not make http calls without encryption
---

# Do not make http calls without encryption

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/requests-http`

**Language:** Python

**Severity:** Warning

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

Making a request with http enables attackers to listen to the traffic and obtain sensitive information. Use `https://` instead.

#### Learn More{% #learn-more %}

- [CWE-319: Cleartext Transmission of Sensitive Information](https://cwe.mitre.org/data/definitions/319.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
def test1():
    url1 = "http://api.tld"
    requests.get(url1)


def test2():
    url2 = "http://api.tld/user/{0}".format(user_id)
    requests.get(url2)

def test3():
    url3 = f"http://api.tld/user/{user_id}"
    requests.get(url3)
    requests.get(url4)
```

```python
def test1():
    requests.get("http://api.tld")
    requests.get("http://api.tld/user/{0}".format(user_id))
    requests.get(f"http://api.tld/user/{user_id}")
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
def download_stuff(identifier, data):
    directory = "/tmp"
    attachments = data.get("attachments", [])

    attachment_url = attachments[0].get("attachment_url", "")

    try:
        response = requests.get(attachment_url, timeout=300)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return (False, "")
```

```python
def test1():
    requests.get("https://api.tld")
    requests.get("https://api.tld/user/{0}".format(user_id))
    requests.get(f"https://api.tld/user/{user_id}")
    requests.get(f"http://localhost/user/{user_id}") # localhost and 127.0.0.1 are safe
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
