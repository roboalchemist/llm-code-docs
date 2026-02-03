# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/inefficient-empty-string-test.md

---
title: Avoid inefficient empty string test
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid inefficient empty string test
---

# Avoid inefficient empty string test

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/inefficient-empty-string-test`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule encourages developers to avoid using inefficient methods to check for empty strings, such as `str.equals("")`. Instead, it recommends using the more efficient and readable `str.isEmpty()` method. The `isEmpty()` method is specifically designed to check if a string has zero length, making it a clearer and more performant choice.

Using `str.equals("")` can be less efficient because it involves a method call that compares the content of the string, which may incur unnecessary overhead. Additionally, it can be less readable and more error-prone, especially if `str` might be `null` and proper null checks are not performed.

To comply with this rule, always use `str.isEmpty()` when checking if a string is empty. This improves code clarity and performance. For example, instead of writing `if (str.equals(""))`, write `if (str.isEmpty())`. This small change leads to cleaner and more efficient code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class MyClass {
    public void method() {
        if (str.equals("")) {
            System.out.println("foo");
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class MyClass {
    public void method() {
        if (str.isEmpty()) {
            System.out.println("foo");
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 