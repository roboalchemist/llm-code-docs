# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/modify-parameter.md

---
title: Do not modify function parameter
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not modify function parameter
---

# Do not modify function parameter

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/modify-parameter`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Assigning new values to function parameters exhibits several bad coding practices and should be avoided for several reasons:

1. Redefining parameters: The code redefines a parameter within the function body by assigning a new value. This is considered a bad practice because it can lead to confusion and make the code harder to understand. Modifying a function parameter in this manner breaks the expected behavior and can cause unexpected side effects. It is generally best to treat function parameters as read-only values and avoid reassigning them.
1. Shadowing variables: The code further exacerbates the issue by using the short variable declaration `:=` to define a new variable within the function body. This shadows the original parameter, making it inaccessible within the function. Shadowing variables can cause confusion and make the code harder to reason about. It is better to use distinct variable names to maintain clarity and avoid any unintended side effects.

To write more maintainable and understandable code, it is advisable to adhere to the following practices:

- Avoid redefining function parameters.
- Use descriptive and unambiguous variable names.
- Avoid shadowing variables.
- Maintain consistency in variable references.

By following these best practices, the code becomes more readable and easier to manage and avoids introducing unnecessary complexity and confusion.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func fun1(param int) {
    // Shadowing 'param'
    param := 51
}

func (r *Type) fun2(param int) {
    param := 51
}

func fun3(param int) {
    if true {
        // Outside of the main function body, := always shadows
        param, err := doSomething()
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func fun1(param int) {
    // Assign a new value to the parameter
    param = doSomething()
}

func fun2(param int) {
    // In the main function body, := with multiple variables in the left
    // will reassign instead of shadowing
    param, err := doSomethingElse()
}

func fun3(param int) {
    const fun4 = func() {
        // Shadowing inside an inner function doesn't affect the outer function
        param := doSomething()
    }
}
```

```go
func fun(_ int) {
	for true {
		// We don't check _ for shadowing
		_, err := doSomething()
	}
}
```

```go
func (r *Type) fun1(ctx context.Context) {
	// As a special case, we allow shadowing context parameters
	ctx := context.WithCancel(ctx)
}

func fun2(ctx context.Context) {
	ctx := context.WithCancel(ctx)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 