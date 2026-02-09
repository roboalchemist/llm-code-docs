# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/telnet-request.md

---
title: Do not use telnet without encryption
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use telnet without encryption
---

# Do not use telnet without encryption

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/telnet-request`

**Language:** Go

**Severity:** Info

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

When sending telnet requests, it is important to use Secure Sockets Layer (SSL) or its successor, Transport Layer Security (TLS), to ensure secure communication. Telnet protocol transmits data in plaintext, which means that any information exchanged, including sensitive data like passwords or commands, can be intercepted and read by malicious actors if the connection is not encrypted.

By utilizing SSL/TLS with telnet requests, the data transmitted is encrypted, making it significantly more difficult for unauthorized parties to intercept and read the information being exchanged.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    telnet.DialToAndCall("my.telnet.server:23", caller)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    telnet.DialToAndCallTLS("my.telnet.server:992", caller)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 