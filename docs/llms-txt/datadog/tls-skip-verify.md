# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/tls-skip-verify.md

---
title: Ensure TLS verification
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Ensure TLS verification
---

# Ensure TLS verification

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/tls-skip-verify`

**Language:** Go

**Severity:** Info

**Category:** Security

**CWE**: [295](https://cwe.mitre.org/data/definitions/295.html)

## Description{% #description %}

The Transport Layer Security (TLS) protocol serves to secure communications between a client and server in a network, so it's integral to maintaining the integrity and confidentiality of data transmission.

In the Go programming language, a common pitfall is that developers sometimes set the parameter `InsecureSkipVerify` of `tls.Config` to `true` to simplify coding or avoid certificate validation errors during testing. However, this parameter must never be set to `true` in a production environment.

When `InsecureSkipVerify` is set to `true`, the TLS verification process is bypassed entirely. Essentially, this action is skipping the very phase that confirms the server identity, leading to possibilities of "Man-in-the-Middle" (MitM) attacks. MitM attacks occur when a malicious actor intercepts and potentially alters the communication between two parties without their knowledge.

By validating the server's certificate, the client verifies the server's identity and ensures that it's safe to transmit data. If `InsecureSkipVerify` is set to `true`, even a server with an invalid or compromised certificate may appear trustworthy, posing significant security risks.

Therefore, always ensure that the `InsecureSkipVerify` parameter is set to 'false' to avoid these possible security breaches. Instead of turning this parameter to 'true' to fix certificate issues, find and resolve the reason the certificate is considered invalid. This could involve renewing expired certificates, trusting a self-signed certificate, or fixing hostname mismatches. This way, you can uphold the authenticity and privacy of your application's client-server interactions.

#### Learn More{% #learn-more %}

- [CWE-295: Improper Certificate Validation](https://cwe.mitre.org/data/definitions/295.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
	"crypto/tls"
	"fmt"
	"net/http"
)

func main() {
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
package main

import (
	"crypto/tls"
	"fmt"
	"net/http"
)

func main() {
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: false},
	}

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 