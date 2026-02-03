# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/redundant-negation.md

---
title: Do not use redundant negation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use redundant negation
---

# Do not use redundant negation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/redundant-negation`

**Language:** Go

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

You do not need to convert the string into a slice of bytes to use `Write`, you can just use the string directly.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

func main() {
	n := 5
	if !!(n == 5) {
		fmt.Println("hello")
	} else if !(!(n == 5)) {
		fmt.Println("hi")
	} 
	
	if !!true{
		fmt.Println("howdy")
	} else if !(!true){
		fmt.Println("partner")
	}

	fmt.Println("goodbye")
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
package main

func main() {
	n := 5
	if !(n == 5) {
		fmt.Println("hello")
	}

	fmt.Println("goodbye")
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 