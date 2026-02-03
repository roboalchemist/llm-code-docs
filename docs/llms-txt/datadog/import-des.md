# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/import-des.md

---
title: DES and Triple DES are now insecure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > DES and Triple DES are now insecure
---

# DES and Triple DES are now insecure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/import-des`

**Language:** Go

**Severity:** Warning

**Category:** Security

## Description{% #description %}

In Go, it is strongly recommended to avoid using the `crypto/des` package for cryptographic operations involving the Data Encryption Standard (DES) algorithm. Avoid the `crypto/des` package for the following reasons:

1. Weak security: The DES algorithm, which `crypto/des` implements, is considered weak and outdated. It uses a 56-bit key size, which is now vulnerable to brute-force attacks. In modern cryptography, it is recommended to use stronger algorithms like AES (Advanced Encryption Standard) with longer key sizes to ensure robust security.
1. Lack of compatibility: The `crypto/des` package does not provide compatibility with more advanced modes of operation like cipher block chaining (CBC) or counter mode (CTR). These modes offer additional protection against known vulnerabilities in basic DES, such as deterministic patterns and susceptibility to certain types of attacks.
1. Limited functionality: The `crypto/des` package only supports the basic DES algorithm without any additional functionality. It lacks support for more advanced encryption modes, padding schemes, or authenticated encryption, which are essential in modern cryptographic systems.

#### Recommended alternatives{% #recommended-alternatives %}

The Go standard library provides a more secure and versatile cryptographic package called `crypto/aes` that implements the AES algorithm. AES is a widely adopted and industry-standard symmetric encryption algorithm known for its robustness and efficiency. It supports various key sizes and modes of operation, making it a suitable replacement for DES in most applications.

To ensure secure and reliable cryptographic operations, it is best to migrate away from the `crypto/des` package and adopt stronger algorithms like AES. The `crypto/aes` package provides the necessary functionality and security for symmetric encryption operations in Go, offering a safer alternative to DES.

It's important to regularly review and update cryptographic choices, considering the latest best practices and standards to maintain the security of your applications and protect sensitive data.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
	"crypto/des"
)

func main() {
	key := []byte("mySample")

	_, err := des.NewCipher(key)
	if err != nil {
		panic(err)
	}
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 