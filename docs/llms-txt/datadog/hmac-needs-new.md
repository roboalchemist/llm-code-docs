# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/hmac-needs-new.md

---
title: Calling hmac.New with unchanging hash.New
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Calling hmac.New with unchanging hash.New
---

# Calling hmac.New with unchanging hash.New

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/hmac-needs-new`

**Language:** Go

**Severity:** Error

**Category:** Security

## Description{% #description %}

No description found

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    hmacKey := []byte("secret")

    h := sha256.New()
    hmacInstance := hmac.New(func() hash.Hash { return h }, hmacKey)

    var h2 hash.Hash
    hmacInstance2 := hmac.New(func() hash.Hash { return h2 }, hmacKey)

    h3 := sha512.New()
    f := func() hash.Hash { return h3 }
    hmacInstance3 := hmac.New(f, hmacKey)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    hmacKey := []byte("secret")
    h := hmac.New(func() hash.Hash { return sha256.New() }, hmacKey)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 