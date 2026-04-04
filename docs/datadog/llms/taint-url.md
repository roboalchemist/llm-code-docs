# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/taint-url.md

---
title: Do not use tainted URL
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use tainted URL
---

# Do not use tainted URL

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/taint-url`

**Language:** Go

**Severity:** Warning

**Category:** Security

## Description{% #description %}

URLs are URLs that have been manipulated or compromised, potentially carrying malicious content such as scripts for executing cross-site scripting (XSS) or SQL injection attacks. These vulnerable URLs provide an avenue for cyber attackers to exploit and gain unauthorized access to sensitive information.

Specifically in the context of Go programming language, if you are calling `http.Get` with a tainted URL, you open up a risk of potential security breaches. The `http.Get` function processes whatever URL it is given, including tainted ones. If the tainted URL contains malicious scripts, executing `http.Get` on them would execute the malicious scripts as well, leading to unintended behaviors such as unauthorized data access or modification, or even service disruption.

Therefore, to maintain a secure code environment, it is crucial to avoid using tainted URLs when calling the `http.Get` function in Go. Always validate and sanitize input URLs before using them in your code. This can involve checking for unexpected characters or patterns in the URL, removing any embedded user input from the URL, or even using safe URL construction methods provided by Go's url package.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
)

url := "https://www.datadoghq.com"
func main() {


    resp, err := http.Get(url)
    if err != nil {
        panic(err)
    }
}
```

```go
package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
)

var url string = "https://www.datadoghq.com"

func main() {
    resp, err := http.Get(url)
    if err != nil {
        panic(err)
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
)

const url = "https://www.datadoghq.com"
func main() {


    resp, err := http.Get(url)
    if err != nil {
        panic(err)
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
