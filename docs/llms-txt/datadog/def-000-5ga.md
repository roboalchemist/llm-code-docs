# Source: https://docs.datadoghq.com/security/default_rules/def-000-5ga.md

---
title: Authentication route use Basic Auth
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Authentication route use Basic Auth
---

# Authentication route use Basic Auth
 
## Description{% #description %}

The API endpoint uses an authentication protocol that is not considered secure. The "HTTP/1.0" protocol includes the specification for a [Basic Access Authentication scheme](https://datatracker.ietf.org/doc/html/rfc7617). That scheme is not a secure method of user authentication, as the user name and password are passed over the network in an unencrypted form.

There are a few issues with HTTP Basic Auth:

- The password is sent over the wire in base64 encoding, which can easily be converted to plaintext if the request was intercepted.
- The password is sent repeatedly, for each request creating a large attack window.
- Does not support logout or session management

## Rationale{% #rationale %}

This finding works by identifying an API that accepts Basic Authentication as the [authentication mechanism](https://docs.datadoghq.com/security/application_security/api-inventory/#endpoint-authentication).

## Remediation{% #remediation %}

- Replace the Basic or Digest accesss authentication with a secure one. Some strong authentication protocols for web-based applications include:

  - Use of Token-Based authentication, implementing temporary access grants by using Access and Refresh tokens ([RFC-8898](https://datatracker.ietf.org/doc/html/rfc8898)).
  - Public key authentication, usually implemented over HTTPS with an SSL client certificate.

### References{% #references %}

| Reference                                                                                                            | Description                                                                                |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [OWASP - Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) | Authentication Cheat Sheet: guidance on the best practices in authentication area.         |
| [OWASP - REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)   | REST Security Cheat Sheet: guidance on the best practices in REST services implementation. |
