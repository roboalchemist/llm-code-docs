# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/do-not-compare-nan.md

---
title: No value is equal to NaN
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > No value is equal to NaN
---

# No value is equal to NaN

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/do-not-compare-nan`

**Language:** Go

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

You do not need to convert the string into a slice of bytes to use `Write`, you can just use the string directly.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
	"fmt"
	"math"
)

func main() {
	n := 5.0
	aNaN := math.NaN()
	// This case cannot be caught with current capabilities
	if n == aNaN {
		fmt.Println("hello")
	} else if n > math.NaN() {
		fmt.Println("hi")
	}

	fmt.Println("goodbye")
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 