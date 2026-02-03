# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/session-secure.md

---
title: Session must be secure
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Session must be secure
---

# Session must be secure

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/session-secure`

**Language:** Go

**Severity:** Info

**Category:** Security

**CWE**: [614](https://cwe.mitre.org/data/definitions/614.html)

## Description{% #description %}

Setting `Secure` to true in the `sessions.Options` structure is important for maintaining the security of web sessions. This flag indicates that the session cookie should only be sent over encrypted connections (HTTPS). By setting `Secure` to true, you ensure that the session cookie is not transmitted over unencrypted HTTP connections, which can help prevent eavesdropping and various types of attacks like session hijacking and man-in-the-middle attacks.

To avoid potential security risks and best protect sensitive data, it is advisable to always set `Secure` to true when working with session management. Additionally, using HTTPS throughout your application ensures end-to-end encryption of all data transmitted between the client and the server.

In conclusion, always setting `Secure` to true in the `sessions.Options` structure is a good coding practice to enhance the security of your web application and protect your users' data from potential threats.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
import (
	"github.com/gorilla/sessions"
)

func main () {
    session = sessions.Options {
        Path:   "/",
        MaxAge: 3600,
        HttpOnly: true,
        Secure: false,
    }

}
```

```go
import (
	"github.com/gorilla/sessions"
)

func main () {
    session = sessions.Options {
        Path:   "/",
        MaxAge: 3600,
        HttpOnly: true,
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
import (
	"github.com/gorilla/sessions"
)

func main () {
    session = sessions.Options {
        Path:   "/",
        MaxAge: 3600,
        HttpOnly: true,
        Secure: true,
    }
    
    foo.bar = sub.String("w", "something-something", &argparse.Options{Required: true})
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 