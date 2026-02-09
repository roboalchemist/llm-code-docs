# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/tls-cipher.md

---
title: Do not use insecure ciphers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use insecure ciphers
---

# Do not use insecure ciphers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/tls-cipher`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

The use of these cipher suites can expose your application to security vulnerabilities.

1. `tls.TLS_RSA_WITH_AES_128_CBC_SHA256`: This cipher suite uses the RSA key exchange algorithm, AES-128 in CBC mode for encryption, and SHA-256 for message authentication. It is considered weak and deprecated because it relies on RSA key exchange, which has known vulnerabilities. Consider using cipher suites based on the Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) algorithm instead.
1. `tls.TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`: This cipher suite uses the ECDHE algorithm with ECDSA for key exchange, AES-128 in CBC mode for encryption, and SHA-256 for message authentication. However, it is also considered weak because of its reliance on CBC mode, which has known vulnerabilities. It is recommended to use cipher suites with GCM (Galois/Counter Mode) mode for better security.
1. `tls.TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA`: This cipher suite uses the ECDHE algorithm for key exchange, RSA for authentication, and 3DES in CBC mode for encryption. It is deprecated due to the use of 3DES, which is considered a weak encryption algorithm. It is advisable to use cipher suites that employ AES instead.
1. `tls.TLS_ECDHE_RSA_WITH_RC4_128_SHA` and `tls.TLS_ECDHE_ECDSA_WITH_RC4_128_SHA`: Both of these cipher suites use the ECDHE algorithm for key exchange, RSA/ECDSA for authentication, and RC4-128 for encryption. RC4 is considered a weak encryption algorithm due to several vulnerabilities. It is recommended to use more secure symmetric encryption algorithms such as AES.
1. `tls.TLS_RSA_WITH_AES_128_CBC_SHA256`, `tls.TLS_RSA_WITH_3DES_EDE_CBC_SHA`, and `tls.TLS_RSA_WITH_RC4_128_SHA`: These cipher suites use the RSA key exchange algorithm, but they also have weaknesses. They rely on RSA for key exchange and various encryption algorithms with SHA for message authentication. It is better to use cipher suites with ECDHE instead of RSA for key exchange and prefer AES-GCM-based encryption algorithms for better security.

To ensure secure communication in your Go applications, you should use modern and strong cipher suites that provide forward secrecy, secure key exchange, and authenticated encryption algorithms. Avoid using the deprecated and weak cipher suites mentioned above and refer to Go's `crypto/tls` documentation for the recommended cipher suites to use in your specific application.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
import (
	"crypto/tls"
	"fmt"
	"net/http"
)

func main() {
	http := &http.Transport{
		TLSClientConfig: &tls.Config{CipherSuites: []uint16{
			tls.TLS_RSA_WITH_RC4_128_SHA,
			tls.TLS_RSA_WITH_AES_128_CBC_SHA256,
		}},
	}
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
import (
	"crypto/tls"
	"fmt"
	"net/http"
)

func main() {
	http := &http.Transport{
		TLSClientConfig: &tls.Config{CipherSuites: []uint16{
			tls.TLS_AES_128_GCM_SHA256,
			tls.TLS_AES_256_GCM_SHA384,
		}},
	}
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 