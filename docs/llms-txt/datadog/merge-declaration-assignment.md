# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/merge-declaration-assignment.md

---
title: Declare and assign variables in one statement
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Declare and assign variables in one statement
---

# Declare and assign variables in one statement

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/merge-declaration-assignment`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

In Go, it is recommended to avoid using separate variable declaration and assignment statements and instead prefer initializing variables directly in the declaration.

Here are a few reasons why:

1. **Simplicity and readability**: Initializing a variable in the declaration with `var x uint = 1` provides a clear and concise way to express the intent of assigning an initial value to the variable. It reduces unnecessary lines of code, making the code more readable and easier to understand.
1. **Avoiding empty initial values**: If you declare a variable with `var x uint` and then assign it a value of 1 separately, it might initially have an undesired default value (in this case, 0) before you assign the actual desired value. By initializing the variable directly in the declaration, you ensure it starts with the desired initial value.
1. **Encouraging good practice**: Initializing variables in the declaration is a recommended coding practice in Go. It follows the principle of declaring variables closer to their usage, promotes legible code, and is widely accepted in the Go community.

Therefore, it is preferable to use `var x uint = 1` rather than declaring the variable on one line and assigning it on another. This approach improves code clarity, reduces unnecessary lines, and ensures variables start with the desired initial value.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    var commands []domain.Command
    commands = append(commands, domain.ChangeAttributes{
        Command: domain.NewCommand(domain.NewKeyIdentifier(testOrgID, c.CaseID), model.NewUserAuthor(testUserUUID)),
        Attributes: domain.CreateAttributesFromProto(
            domain.MapArrayToMapListValue(map[string][]string{
                "service": {"case-api-test"},
            },
        )),
    })
}
```

```go
func main () {
    var x uint
    x = 1
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main () {
    var generatedUuid uuid.UUID
    // not triggering is we have two elements on the left side
    generatedUuid, err = uuid.NewUUID()
}
```

```go
func main () {
    var x uint
    x = 1
    x = 2
}
```

```go
func main () {
    var (
        x uint
        y int
    )
    x = 1
    x = 2
}
```

```go
func main () {
    var x uint = 1
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 