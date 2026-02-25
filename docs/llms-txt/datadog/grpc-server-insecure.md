# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/grpc-server-insecure.md

---
title: Avoid insecure GRPC server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid insecure GRPC server
---

# Avoid insecure GRPC server

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/grpc-server-insecure`

**Language:** Go

**Severity:** Info

**Category:** Security

**CWE**: [300](https://cwe.mitre.org/data/definitions/300.html)

## Description{% #description %}

The provided code snippet creates a new gRPC server instance without any transport security options, which makes it insecure. By default, the server will use an insecure communication channel, allowing data to be transmitted without encryption.

To fix this security issue, it is crucial to enable transport security using TLS (Transport Layer Security) in the gRPC server. Here's an example of how the code can be updated to ensure a secure connection:

```go
tlsCredentials, err := credentials.NewServerTLSFromFile("cert.pem", "key.pem")
if err != nil {
    // handle error
}

s := grpc.NewServer(grpc.Creds(tlsCredentials))
```

In the updated code, TLS credentials are loaded from the "cert.pem" and "key.pem" files. These credentials contain the server's certificate and private key necessary for TLS encryption. By passing the TLS credentials to `grpc.Creds()`, the gRPC server is configured to use transport security, ensuring that all incoming connections are secured.

It is important to generate valid TLS certificates and private keys from a trusted certificate authority (CA), or self-sign the certificates for development/testing purposes. Additionally, make sure to keep the private key file secure and protect it from unauthorized access.

Enabling transport security with TLS in the gRPC server helps protect sensitive data exchanged between clients and the server by encrypting it, preventing unauthorized users from intercepting or tampering with the communication.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    s := grpc.NewServer()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    options := []grpc.ServerOption{
        grpc.Creds(credentials.NewClientTLSFromCert(ceertificatePool, address)),
    }
    server := grpc.NewServer(options...)
}
```

```go
// filename is not_compliant_test.go
func main() {
    s := grpc.NewServer()
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
