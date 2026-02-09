# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/import-sha1.md

---
title: The SHA-1 algorithm family is no longer secure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > The SHA-1 algorithm family is no longer secure
---

# The SHA-1 algorithm family is no longer secure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/import-sha1`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

In Go, it is strongly discouraged to use the `crypto/sha1` package for cryptographic operations involving the Secure Hash Algorithm 1 (SHA-1). Avoid the `crypto/sha1` package for the following reasons:

1. Vulnerabilities: SHA-1 is no longer considered secure for cryptographic use due to significant vulnerabilities. Collision attacks against SHA-1 have been demonstrated, which allows for the creation of different inputs that produce the same hash output. This undermines data integrity and can lead to security breaches.
1. Weak security: SHA-1 produces a fixed-sized 160-bit hash value, which is considered relatively short in comparison to more modern and secure hash functions like SHA-256 or SHA-3. A shorter hash length reduces resistance against brute-force attacks and increases the risk of collisions, where different inputs produce the same hash value.
1. Deprecated by industry standards: In response to the vulnerabilities of SHA-1, industry standards bodies and security organizations have deprecated the use of SHA-1 for cryptographic purposes. The National Institute of Standards and Technology (NIST) and the Internet Engineering Task Force (IETF) have strongly recommended the transition from SHA-1 to stronger hash functions.

#### Recommended alternatives{% #recommended-alternatives %}

Go provides the `crypto/sha256` package to implement the Secure Hash Algorithm 2 (SHA-2) with a hash length of 256 bits. SHA-256 is considered more secure and resistant to collision attacks compared to SHA-1. It is widely adopted and recommended for cryptographic applications where data integrity and security are critical. |

To ensure secure and reliable hashing operations, it is best to avoid using the `crypto/sha1` package and opt for stronger hash functions like SHA-256 provided by the `crypto/sha256` package in Go. This transition helps to mitigate the vulnerabilities associated with SHA-1 and maintain the security of your applications.

Stay up-to-date with the latest security recommendations and best practices to ensure the integrity and confidentiality of your cryptographic operations. Choosing stronger hash functions is an essential step in safeguarding sensitive data and protecting against potential attacks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
	"crypto/sha1"
	"fmt"
)

func main() {
	h := sha1.New()
	fmt.Printf("% x", h.Sum(nil))
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 