# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/http-request-secure.md

---
title: Ensure we use https://
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure we use https://
---

# Ensure we use https://

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/http-request-secure`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [319](https://cwe.mitre.org/data/definitions/319.html)

## Description{% #description %}

Making HTTP requests (using `http://`) instead of HTTPS requests (using `https://`) can pose security risks, as information transmitted over HTTP is not encrypted and can be easily intercepted by malicious actors. This could potentially lead to sensitive data being exposed, such as login credentials or personal information.

To avoid this security risk, it's important to always make HTTP requests using HTTPS. This ensures that the data being transmitted is encrypted, offering a higher level of security and protecting sensitive information.

To follow best practices and avoid making HTTP requests, developers should:

1. Always specify `https://` in URIs when making API calls or requesting resources.
1. Use libraries or frameworks that automatically default to HTTPS for requests.
1. Implement a Content Security Policy (CSP) on web applications to enforce secure connections.
1. Avoid hardcoding URLs and consider using environment variables to store and retrieve URLs dynamically.

By following these practices, developers can enhance the security of their applications and protect sensitive data from potential threats.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    response, err := http.Get("http://www.datadoghq.com")
    response, err := http.Head("http://www.datadoghq.com", something, somethingElse)
    response, err := http.Post("http://www.datadoghq.com")
    response, err := http.PostForm("http://www.datadoghq.com", myForm)

    response, err := http.PostForm("http://domain.tld/localhost", myForm)

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    response, err := http.Get("https://www.datadoghq.com")
    response, err := http.Head("https://www.datadoghq.com", something, somethingElse)
    response, err := http.Post("https://www.datadoghq.com")
    response, err := http.PostForm("https://www.datadoghq.com", myForm)

    response, err := http.PostForm("http://localhost", myForm)
    response, err := http.PostForm("http://127.0.0.1", myForm)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 