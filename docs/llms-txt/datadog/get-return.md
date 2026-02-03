# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/get-return.md

---
title: Functions prefixed by get should return something
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Functions prefixed by get should return something
---

# Functions prefixed by get should return something

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/get-return`

**Language:** Go

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In programming, it is a common convention to prefix functions with "get" when they are intended to retrieve or fetch some data or state from an object or system. When following this convention, it is generally expected that functions prefixed with "get" should return a value rather than modifying the state directly. This practice offers a number of benefits:

1. Intuitive and predictable: Using the "get" prefix indicates to other developers that the function is meant to retrieve data rather than make changes or perform actions. Developers can expect the function to return a value, making the code more intuitive and easy to understand.
1. Encapsulation and data hiding: By having "get" functions return a value, it encourages encapsulation and proper abstraction of the underlying internal state. The function acts as an interface to access the data, shielding its internals and allowing the object or system to manage access to its state effectively.
1. Immutability and consistency: Returning a value from a "get" function helps maintain the principle of immutability, ensuring that the data accessed through the function cannot be modified by external code. This promotes consistency and helps prevent unintended modifications that could lead to bugs or unexpected behavior.
1. Adaptability and flexibility: Returning a value from "get" functions allows for potential changes or enhancements in the future. By returning a value, additional logic or transformations can be applied before returning the data, providing flexibility to modify the behavior of the "get" function without impacting the code that accesses it.

By adhering to the practice of having "get" functions return a value, you improve code clarity, maintain good encapsulation, promote immutability, and allow for future adaptability and extensibility. Following this convention makes the codebase more intuitive, predictable, and maintainable.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go

func GetSomething() {

}

func getSomethingElse() {

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go

func GetSomething() int {

}

func getSomethingElse() (type1, type2){

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 