# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/invalid-host-port-pair.md

---
title: Common invalid host-port pairs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Common invalid host-port pairs
---

# Common invalid host-port pairs

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/invalid-host-port-pair`

**Language:** Go

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The `host:port` pair is invalid. The HTTP server needs to use a valid pair of address and port.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import ("net")

func main(){
    // Good
    http.ListenAndServe("localhost:8080", nil)
    http.ListenAndServe(":8080", nil)
    http.ListenAndServe(":http", nil)
    http.ListenAndServe("localhost:http", nil)
    http.ListenAndServe("my_server:8080", nil)
    http.ListenAndServe("", nil) // Defaults to ":http"

    // Bad
    http.ListenAndServe("localhost:8080/", nil)
    http.ListenAndServe("localhost", nil)

    // Good
    http.ListenAndServeTLS("localhost:8443", "cert.pem", "key.pem", nil)
    http.ListenAndServeTLS(":8443", "cert.pem", "key.pem", nil)
    http.ListenAndServeTLS("localhost:https", "cert.pem", "key.pem", nil)
    http.ListenAndServeTLS("my_server:8443", "cert.pem", "key.pem", nil)
    http.ListenAndServeTLS("", "cert.pem", "key.pem", nil) // Defaults to ":https"

    // Bad
    http.ListenAndServeTLS("localhost:8443/", "cert.pem", "key.pem", nil)
    http.ListenAndServeTLS("localhost", "cert.pem", "key.pem", nil)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
