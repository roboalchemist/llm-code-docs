# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/import-rc4.md

---
title: RC4 encryption is now insecure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > RC4 encryption is now insecure
---

# RC4 encryption is now insecure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/import-rc4`

**Language:** Go

**Severity:** Warning

**Category:** Security

## Description{% #description %}

In Go, it is strongly discouraged to use the `crypto/rc4` package for cryptographic operations involving the RC4 (Rivest Cipher 4) algorithm. Avoid the `crypto/rc4` package for the following reasons:

1. Weak Security: The RC4 algorithm is considered weak and insecure for modern cryptographic applications. It is susceptible to significant vulnerabilities, making it unsuitable for ensuring data confidentiality. Several attacks, such as the Fluhrer-Mantin-Shamir attack and biases in the keystream, have been discovered over the years. Due to these vulnerabilities, the RC4 algorithm is no longer considered secure.
1. Cryptographic Strength: RC4 has a small key size of up to 256 bits (variable length), which is relatively short compared to modern symmetric encryption algorithms like AES (Advanced Encryption Standard). A shorter key size reduces the complexity of brute-force attacks and increases the likelihood of successful attacks on the encryption.
1. Lack of Compatibility: The `crypto/rc4` package in Go does not provide compatibility with more advanced modes of operation or options for authenticated encryption. Modern cryptographic systems often require these features to ensure data integrity and protect against known vulnerabilities.

#### Recommended Alternatives{% #recommended-alternatives %}

Instead of using RC4, it is recommended to use stronger and more secure algorithms like AES (Advanced Encryption Standard). The Go standard library offers the `crypto/aes` package to implement AES encryption, which provides significant security improvements and better support for advanced cryptographic features. |

To ensure secure and reliable cryptographic operations, it is essential to avoid using the `crypto/rc4` package and opt for stronger algorithms like AES. AES provides enhanced security, compatibility with modern cryptographic practices, and support for larger key sizes. By adopting modern and secure algorithms, you can protect data confidentiality effectively.

Always stay updated with the latest best practices and security recommendations to ensure the integrity and security of your cryptographic operations. Choosing strong encryption algorithms is crucial for safeguarding sensitive data in your Go applications.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
    "crypto/rc4"
)

func main() {
    _, err := rc4.NewCipher([]byte("mySample"))
    if err != nil {
        panic(err)
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
