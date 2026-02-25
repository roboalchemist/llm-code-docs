# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/grpc-client-insecure.md

---
title: Avoid insecure GRPC connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid insecure GRPC connection
---

# Avoid insecure GRPC connection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/grpc-client-insecure`

**Language:** Go

**Severity:** Info

**Category:** Security

**CWE**: [300](https://cwe.mitre.org/data/definitions/300.html)

## Description{% #description %}

The code provided is not considered good practice and can create a security issue because it is using the "grpc.WithInsecure()" option when establishing a gRPC connection. The "grpc.WithInsecure()" option disables transport security, also known as TLS (Transport Layer Security) or SSL (Secure Sockets Layer).

By disabling transport security, the code allows communication to occur over an unencrypted connection, leaving data transmitted between the client and the server vulnerable to eavesdropping, tampering, and other security threats. Without encryption, malicious parties can intercept sensitive information such as authentication credentials, session data, or sensitive API payloads.

To ensure data security and protect against potential attacks, it is highly recommended to use transport security (TLS) in gRPC connections.

To fix the security issue, the code should be modified to use a secure connection by providing the appropriate TLS credentials. Here is an example of how the code can be updated:

```go
tlsCredentials, err := credentials.NewClientTLSFromFile("cert.pem", "")
if err != nil {
    // handle error
}

conn, err := grpc.Dial(address, grpc.WithTransportCredentials(tlsCredentials))
```

In this updated code, a TLS certificate is loaded from the "cert.pem" file and used to create the necessary TLS credentials for the gRPC connection. By using "grpc.WithTransportCredentials()" instead of "grpc.WithInsecure()", the connection is secured with TLS, encrypting the data transmitted between the client and the server, and mitigating potential security risks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    conn, err := grpc.Dial(address, grpc.WithInsecure())
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    creds := credentials.NewTLS(&tls.Config{})
    conn, err := grpc.Dial(address, grpc.WithTransportCredentials(creds))
}
```

```go
func main() {
    // rule is ignored in tests
    conn, err := grpc.Dial(address, grpc.WithInsecure())
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
