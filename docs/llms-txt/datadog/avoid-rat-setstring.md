# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/avoid-rat-setstring.md

---
title: Avoid SetString() from big.Rat
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid SetString() from big.Rat
---

# Avoid SetString() from big.Rat

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/avoid-rat-setstring`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [109](https://cwe.mitre.org/data/definitions/109.html)

## Description{% #description %}

Do not use the function `SetString` from `big.Rat` as it as a potential overflow in some Go versions. Even if your current Go runtime is not vulnerable to this issue, your code may be used by runtime that are. We recommend avoiding the function `SetString` from the `math/big` package for this reason.

#### Learn More{% #learn-more %}

- [CVE-2022-23772: Rat.SetString in math/big in Go before 1.16.14 and 1.17.x before 1.17.7 has an overflow that can lead to Uncontrolled Memory Consumption](https://nvd.nist.gov/vuln/detail/CVE-2022-23772)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
	"math/big"
	"fmt"
)

func main() {
	var r = big.Rat{}
	r.SetString("13e-9223372036854775808")

	fmt.Println(r)
}
```

```go
package main

import (
	"math/big"
	"fmt"
)

func anotherFunction() {
	r = big.Rat{}
	fmt.Println(r)
	r.SetString("13e-9223372036854775808")

	fmt.Println(r)
}

func anotherFunction2() {
	var r big.Rat
	fmt.Println(r)
	r.SetString("13e-9223372036854775808")

	fmt.Println(r)
}

func main() {
	var r = big.Rat{}
	r.SetString("13e-9223372036854775808")

	fmt.Println(r)
}
```

```go
package main

import (
	"math/big"
	"fmt"
)

func main() {
	r := big.Rat{}
	r.SetString("13e-9223372036854775808")

	fmt.Println(r)
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
package main

import (
	"math/big"
	"fmt"
)

func main() {
	r := big.NewRat(10, 3)

	fmt.Println(r)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 