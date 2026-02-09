# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/for-select-default-empty.md

---
title: Prevent empty default case for select without condition
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent empty default case for select without condition
---

# Prevent empty default case for select without condition

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/for-select-default-empty`

**Language:** Go

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Go, the default case of a switch statement is executed when none of the preceding cases match the specified condition.

While it is technically allowed to have an empty default case, it is generally considered a bad practice because it can lead to confusion and make the code harder to read and maintain.

Here are a few reasons why the default case should not be empty in Go:

1. **Clarity and readability**: The primary goal of writing code is to make it understandable to other developers. Using an empty default case leaves the reader wondering why it is there and what its purpose might be. It is better to explicitly handle all possible cases, even if it means adding a placeholder or a comment.
1. **Future-proofing**: An empty default case can be a sign of incomplete or unfinished code. If new cases are added in the future and the default case remains empty, it may lead to unintended consequences or logic errors.
1. **Linting and static analysis tools**: Some linting tools and static analysis tools may flag empty default cases as potential mistakes or omissions. These tools can help identify and prevent potential bugs or issues in the code.

To address these concerns, it is recommended to either provide a meaningful action or simply include a comment in the default case explaining the reason for its presence. This helps improve code clarity, maintainability, and ensures proper handling of all possible cases in the switch statement.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main () {
    for {
		select {
		    case <-myChannel:
		    default:
		}
	}
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    for {
		select {
		    case <-myChannel:
				println("foo")
		    default:
				println("bar")
				
		}
	}

	for {
		select {
		    case <-myChannel2:
				println("foo")
		    default:
				// println("bar")
		}
	}

	for something {
		select {
		    case <-myChannel2:
				println("foo")
		    default:
		}
	}

	select {
		case <-myChannel:
		default:
	}

    for {
		select {
		    case <-myChannel:
		    default:
		}
		println("foo") // another statement after for, no warning
	}
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 