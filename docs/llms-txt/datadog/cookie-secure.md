# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/cookie-secure.md

---
title: Session must be secure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Session must be secure
---

# Session must be secure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/cookie-secure`

**Language:** Go

**Severity:** Info

**Category:** Security

**CWE**: [614](https://cwe.mitre.org/data/definitions/614.html)

## Description{% #description %}

The `Secure` attribute of an `http.Cookie` is a security measure that indicates the cookie should only be sent over secure connections, such as HTTPS. Failing to set the `Secure` attribute can expose sensitive information to potential attacks, like man-in-the-middle attacks, where an attacker can intercept the communication between the client and the server.

To avoid this vulnerability, always ensure that the `Secure` attribute is set for cookies containing sensitive information. Also, make sure that your application enforces the use of HTTPS to encrypt the communication between the client and the server. By following these best practices, you can enhance the security of your application and protect user data from potential threats.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    cookie = http.Cookie {
        Path:   "/",
        HttpOnly: true,
    }
}
```

```go
func main () {
    cookie = http.Cookie {
        Path:   "/",
        HttpOnly: true,
        Secure: false,
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    cookie = http.Cookie {
        Path:   "/",
        Secure: true, // <-- true
        HttpOnly: true,
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 