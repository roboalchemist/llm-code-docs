# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/hashsum.md

---
title: Odd hash.Sum call flow
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Odd hash.Sum call flow
---

# Odd hash.Sum call flow

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/hashsum`

**Language:** Go

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

When you use a hash function that implements `hash.Hash`, you need to use `Write()` to provide the data before calling `Sum()`.

```golang
// Correct usage of hash.Hash
h := sha256.New()
h.Write(data)
sum := h.Sum(nil)
// 'sum' contains the SHA256 sum of 'data'
```

Since the `Sum()` member function takes a byte array as an argument, it is a common mistake to believe that this argument contains the data to be hashed. In reality, this argument contains some data to which the hash will be appended.

```golang
// Incorrect usage of hash.Hash
h := sha256.New()
sum := h.Sum(data)
// wrong: 'sum' contains 'data' followed by the SHA256 sum of an empty string
```

This rule detects these erroneous usages of `hash.Hash`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
import "crypto/sha256"

func main() {
    out := make([]byte, 64)
    h := sha256.New()
    hashed := h.Sum(out)

    hashed := sha256.New().Sum(out)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
import "crypto/sha256"

func main() {
    arr := []byte{1, 2, 3}
    out := make([]byte, 64)
    h := sha256.New()
    h.Write(arr)
    hashed := h.Sum(out)

    h2 := sha256.New()
    hashArr(h2, arr)
    hashed2 := h2.Sum(out)
}

func hashArr(h hash.Hash, b []byte) {
    h.Write(b)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 