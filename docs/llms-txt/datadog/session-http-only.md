# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/session-http-only.md

---
title: Prevent XSS injection by setting HttpOnly to false
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent XSS injection by setting HttpOnly to false
---

# Prevent XSS injection by setting HttpOnly to false

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/session-http-only`

**Language:** Go

**Severity:** Info

**Category:** Security

**CWE**: [1004](https://cwe.mitre.org/data/definitions/1004.html)

## Description{% #description %}

By setting the "HTTP-only" flag in session cookies, web developers effectively restrict the client-side access to the session cookie. This means that the cookie can only be accessed and transmitted over a secure HTTP connection, preventing it from being accessed by JavaScript code or through client-side scripting attacks such as cross-site scripting (XSS).

Here are some good coding practices to avoid session cookie vulnerabilities:

1. Set the "HTTP-only" flag: When creating session cookies, ensure that the "HTTP-only" flag is set, preventing client-side scripts from accessing the cookie information.
1. Secure cookie transmission: Use secure HTTPS connections to transmit session cookies between clients and servers. This protects the session cookies from being intercepted or tampered with by malicious actors.
1. Implement strong session management practices: Follow secure session management practices, such as generating random and unique session IDs, setting appropriate expiration times for sessions, and invalidating sessions after logout or timeout.
1. Protect against session fixation attacks: Implement mechanisms that protect against session fixation attacks, such as generating a new session ID for each authenticated user and regenerating session IDs after user authentication.
1. Regularly review and update session-related code: Continuously review and update session-related code to ensure it aligns with the latest security best practices and guidelines.

By implementing these good coding practices, developers can mitigate session cookie vulnerabilities and enhance the security of web applications.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
import (
    "github.com/gorilla/sessions"
)

func main () {
    session = sessions.Options {
        Path:   "/",
        MaxAge: 3600,
        HttpOnly: false,
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
import (
    "github.com/gorilla/sessions"
)

func main () {
    session = sessions.Options {
        Path:   "/",
        MaxAge: 3600,
        HttpOnly: true,
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
