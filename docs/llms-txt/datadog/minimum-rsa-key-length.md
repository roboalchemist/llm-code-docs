# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/minimum-rsa-key-length.md

---
title: RSA keys should have a minimum of 2,048 bits
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > RSA keys should have a minimum of 2,048 bits
---

# RSA keys should have a minimum of 2,048 bits

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/minimum-rsa-key-length`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [326](https://cwe.mitre.org/data/definitions/326.html)

## Description{% #description %}

RSA keys should have a minimum length to ensure the security and strength of cryptographic operations. A key length is measured in bits and determines the complexity of the key, making it harder for attackers to break or decrypt the encryption.

## Arguments{% #arguments %}

- `min-length`: Minimum length of the RSA key. Default: 2048.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
	"crypto/rand"
	"crypto/rsa"
	"fmt"
)

func main() {
	privateKey, err := rsa.GenerateKey(rand.Reader, 1024)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(privateKey)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
package main

import (
	"crypto/rand"
	"crypto/rsa"
	"fmt"
)

func main() {
	privateKey, err := rsa.GenerateKey(rand.Reader, 2048)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(privateKey)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 