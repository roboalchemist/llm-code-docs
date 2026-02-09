# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/simplify-boolean-expression.md

---
title: Simplify boolean expression
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Simplify boolean expression
---

# Simplify boolean expression

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/simplify-boolean-expression`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, it is considered unnecessary and less readable to write a conditional statement that returns `true` or `false` explicitly based on a condition. Instead, it is recommended to directly return the condition itself. Here's why:

1. **Code simplicity and readability**: Writing `return condition` directly conveys the intent of the code more clearly and reduces unnecessary verbosity. It is easier for other developers to understand your code at a glance without having to analyze additional conditional statements.
1. **Avoidance of redundancy**: Explicitly returning `true` or `false` based on a condition introduces redundancy in the code. Since the condition itself already evaluates to a boolean value (`true` or `false`), there is no need to include additional `return true` or `return false` statements.
1. **Maintainability and refactoring**: The direct `return condition` approach is more maintainable and flexible for future code changes. If the condition or the desired return value changes, it is easier to modify a single line rather than multiple lines of code. This minimizes the chances of introducing errors or inconsistencies during refactoring.

Therefore, it is recommended to simply use `return condition` instead of `if condition { return true } return false`. By doing so, you improve code readability, reduce redundancy, and ensure better maintainability of your Go code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
	if foo == 1 {
		return true
	}
	return false
}
```

```go
func main() {
	if foo == 1 {
		return true
	} else {
		return false
	}

	if foo != 4 {
		// Comment 1
		return true
		// Comment 2
	} else {
		// Comment 3
		return false
		// Comment 4
	}
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
	if len(spec) == 0 {
		return true
	} else if slides.Contains(sped, candidate) {
		foobar()
		return true
	}
	return false
}
```

```go
func main() {
	exists, err := h.deduper.KeyExists(ctx, dedupeKey)
	if err != nil {
		return false, commonhandler.RetryErrHandleResp(err)
	} else if exists {
		return true, commonhandler.SuccessHandleResp
	}

	return false, commonhandler.SuccessHandleResp
}
```

```go
func main() {
	if foo == 1 {
		println("foo")
		return true
	} else {
		return false
	}

	if foo == 1 {
		// Some comment
		return true
	} else {
		// Another comment
		return true
	}

	if strings.TrimSpace(rawMessage.Custom.Git.RepositoryURL) == "" {
		return false, ""
	}
	return true, ""
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 