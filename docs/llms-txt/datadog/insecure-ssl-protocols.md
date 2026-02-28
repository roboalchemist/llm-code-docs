# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/insecure-ssl-protocols.md

---
title: Do not use insecure encryption protocols
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use insecure encryption protocols
---

# Do not use insecure encryption protocols

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `python-security/insecure-ssl-protocols`

**Language:** Python

**Severity:** Notice

**Category:** Security

## Description{% #description %}

The following security protocols should never be used in Python: `SSLv3`, `SSLv2`, `TLSv1`. For more details, read the [SSL module page](https://docs.python.org/3/library/ssl.html) of the official documentation.

The issue addresses the [CWE-757](https://cwe.mitre.org/data/definitions/757.html) - selection of less-secure algorithm during negotiation.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```python
import ssl

def newconnect(self):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote = ssl.wrap_socket(s,
                             ca_certs= CA,
                             cert_reqs=ssl.CERT_REQUIRED,
                             ssl_version = ssl.PROTOCOL_SSLv3)
    remote.connect(self.server.seradd)
    if not self.server.seradd[0] == remote.getpeercert()['subjectAltName'][0][1]:
      logging.error('Server crt error !! Server Name don\'t mach !!')
      logging.error(remote.getpeercert()['subjectAltName'][0][1])
      return
    if not self.send_PW(remote):
      logging.warn('PW error !')
      return
    except socket.error, e:
      logging.warn(e)
      return
```

## Compliant Code Examples{% #compliant-code-examples %}

```python
import ssl

def newconnect(self):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote = ssl.wrap_socket(s,
                             ca_certs= CA,
                             cert_reqs=ssl.CERT_REQUIRED,
                             ssl_version = ssl.PROTOCOL_TLS)
    remote.connect(self.server.seradd)
    if not self.server.seradd[0] == remote.getpeercert()['subjectAltName'][0][1]:
      logging.error('Server crt error !! Server Name don\'t mach !!')
      logging.error(remote.getpeercert()['subjectAltName'][0][1])
      return
    if not self.send_PW(remote):
      logging.warn('PW error !')
      return
    except socket.error, e:
      logging.warn(e)
      return
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
