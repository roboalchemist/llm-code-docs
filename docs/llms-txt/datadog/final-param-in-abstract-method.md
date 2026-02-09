# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/final-param-in-abstract-method.md

---
title: Avoid useless final type in interface method
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid useless final type in interface method
---

# Avoid useless final type in interface method

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/final-param-in-abstract-method`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

The rule "Avoid useless final type in interface method" advises against the unnecessary use of the `final` keyword in the method parameters of an interface. In Java, the `final` keyword is used to denote that a variable cannot be changed once assigned. However, in the context of an interface method, this is redundant as the value of the parameter cannot be changed within the method anyway.

The importance of this rule lies in the clarity and simplicity of code. Unnecessary use of `final` in this context can lead to confusion for those reading the code, as it suggests that there may be a specific reason for its use when there is not. It can also clutter the code, making it less readable.

Good coding practices to avoid this rule violation include simply not using the `final` keyword in the method parameters of an interface. This does not affect the functionality of the code, but it makes it cleaner and easier to understand. For example, instead of writing `void process(final Object arg);`, you can write `void process(Object arg);`. This maintains the same functionality but improves the readability of the code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public interface FooInterface {
  void process(final Object arg); // Avoid using final here
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public interface FooInterface {
  void process(Object arg);
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 