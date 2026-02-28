# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/while-loop-with-literal-boolean.md

---
title: Loops can be simplified or removed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Loops can be simplified or removed
---

# Loops can be simplified or removed

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/while-loop-with-literal-boolean`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Using `do {} while (true);` makes it less obvious that the loop runs forever, since the loop condition is placed after the loop body. By using `while (true) {}`, your code clearly indicates an infinite loop from the beginning.

The `do {} while (false);` construct is redundant and may cause confusion too. In a `do-while` loop, the loop body is executed first, and then the condition is checked. Since the condition `while (false)` always evaluates to false, the loop exits after one iteration. When an inner variable scope is required within this loop, a simple block `{}` can be used instead of the `do-while` construct.

Unlike the `do {} while (false);` above, the `while (false) {}` construct represents dead code because the loop condition here is evaluated first and the body will never execute. Removing unnecessary loops here can enhances your code's readability and maintainability.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
  {
    while (false) { }
    do { } while (true);
    do { } while (false);
    do { } while (false | false);
    do { } while (false || false);
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
  {
    while (true) { }
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
