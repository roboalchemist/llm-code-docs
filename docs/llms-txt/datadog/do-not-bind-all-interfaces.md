# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/do-not-bind-all-interfaces.md

---
title: Binding to 0.0.0.0 opens up the application to all traffic
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Binding to 0.0.0.0 opens up the application to all traffic
---

# Binding to 0.0.0.0 opens up the application to all traffic

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/do-not-bind-all-interfaces`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [1327](https://cwe.mitre.org/data/definitions/1327.html)

## Description{% #description %}

Binding a server to all interfaces or IP addresses can pose a security risk as it potentially exposes the server to unauthorized access from external sources. When a server is bound to all interfaces, it means that it is listening for incoming connections on all network interfaces available on the machine, including public interfaces.

This can lead to unintended exposure of the server to the internet or other insecure networks, making it vulnerable to attacks such as unauthorized access, DDOS attacks, and data breaches.

To avoid this security risk, it is recommended to bind servers only to the specific interfaces or IP addresses that are necessary for the server to function properly. This can be achieved by explicitly specifying the network interface or IP address in the server configuration settings.

Developers should follow the principle of least privilege when configuring server settings, ensuring that only necessary services are exposed to the network and unnecessary interfaces are disabled or not bound to the server. Regular security assessments and audits should also be conducted to identify and address any potential vulnerabilities in the server configuration.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import ("net")

func main(){
    // Bad
    http.ListenAndServe("0.0.0.0", nil) 

    // Bad
    http.ListenAndServeTLS("0.0.0.0", "cert.pem", "key.pem", nil)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 