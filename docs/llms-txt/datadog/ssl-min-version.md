# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/ssl-min-version.md

---
title: Ensure MinVersion is defined for TLS client
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure MinVersion is defined for TLS client
---

# Ensure MinVersion is defined for TLS client

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/ssl-min-version`

**Language:** Go

**Severity:** Info

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

In Go's `tls.Config`, it is important to specify the `MinVersion` field to ensure secure and up-to-date communication protocols are used between the client and server.

The `MinVersion` field allows you to specify the minimum acceptable TLS version for establishing secure connections. By setting a minimum TLS version, you can prevent the use of outdated and insecure protocols that may have known vulnerabilities.

Here are a few reasons why specifying `MinVersion` is important:

1. Security: Older versions of TLS, such as TLS 1.0 and TLS 1.1, have known security vulnerabilities. They may be susceptible to attacks including BEAST (Browser Exploit Against SSL/TLS), POODLE (Padding Oracle On Downgraded Legacy Encryption), and other advanced cryptographic attacks. By setting `MinVersion` to TLS 1.2 or higher, you can ensure that only the more secure and robust protocols are used for communication.
1. Compliance: Many regulatory standards and best practices, such as the Payment Card Industry Data Security Standard (PCI-DSS) and the General Data Protection Regulation (GDPR), require the use of modern TLS versions for data transmission. Specifying `MinVersion` allows you to comply with these industry standards and maintain a secure environment.
1. Interoperability: Specifying the minimum TLS version also ensures compatibility and interoperability with modern systems and services. Some third-party services, APIs, or clients may only support TLS 1.2 or higher, and specifying a minimum version prevents potential communication failures.

When setting the `MinVersion`, it's generally recommended to use `tls.VersionTLS13` if your application can support it. TLS 1.3 provides numerous security improvements and performance optimizations over its predecessors. However, depending on your specific requirements and compatibility considerations, you may choose to set it to a lower minimum version like `tls.VersionTLS12`.

Here is an example of setting the `MinVersion` field in a `tls.Config` struct:

```go
tlsConfig := &tls.Config{
    MinVersion: tls.VersionTLS12, // Set the minimum TLS version to TLS 1.2
    // ... Other TLS configuration options ...
}
```

By explicitly specifying the `MinVersion` in your `tls.Config`, you can ensure secure and modern TLS versions are used for secure communication in your Go applications.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
import (
    "crypto/tls"
)

func main () {
    config := tls.Config{

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
import (
    "crypto/tls"
)

func main () {
    config := tls.Config{
        MinVersion:         tls.VersionTLS10,
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 