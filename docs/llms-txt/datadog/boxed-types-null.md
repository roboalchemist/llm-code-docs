# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/boxed-types-null.md

---
title: Check that boxed types are not null
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check that boxed types are not null
---

# Check that boxed types are not null

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/boxed-types-null`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule checks that boxed primitive types (such as `Integer`, `Float`, `Double`, and `Boolean`) are not used in a way that assumes they can never be null. Boxed types can hold a `null` value, which may lead to `NullPointerException` if dereferenced without a null check. Ensuring that these types are either properly checked for null or avoided helps maintain code robustness and prevents runtime errors.

It is important to avoid unnecessary use of boxed types when primitive types suffice, as primitives cannot be null and thus eliminate the risk of null-related exceptions. When a boxed type is necessary, for example, when using collections or generics, always perform explicit null checks before usage. Additionally, consider using primitive types directly (`int`, `float`, `double`, `boolean`) whenever possible to improve performance and safety.

To comply with this rule, prefer using primitive types in variable declarations and operations. If you must use boxed types, write defensive code by checking for null values before any dereference. For example, instead of `Float foo = 1.0;` without null checks, use `float foo = 1.0f;` or ensure null safety when using `Float`. This practice leads to more reliable and maintainable Java code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyClass {
    public void foo() {
        Float foo = 1.0;
        if (bla) {
            foo = 2.0;
        }
        foo = 3.0;
    }
}
```

```java
class MyClass {
    public void foo() {
        Double foo = 1.0;
        if (bla) {
            foo = 2.0;
        }
        foo = 3.0;
    }
}
```

```java
class MyClass {
    public void foo() {
        Integer foo = 1;
        if (bla) {
            foo = 3;
        }
        foo = 2;
    }
}
```

```java
class MyClass {
    public void foo() {
        Boolean foo = true;
        if (bla) {
            foo = true;
        }
        foo = false;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class MyClass {
    public void foo() {
        float foo = 1.0;
        if (bla) {
            foo = 3.0;
        }
        foo = 2.0;
    }
}
```

```java
class MyClass {
    public void foo() {
        int foo = 1;
        if (bla) {
            foo = 3;
        }
        foo = 2;
    }
}
```

```java
class MyClass {
    public void foo() {
        Integer foo = 1;
        if (bla) {
            foo = null;
        }
        foo = 2;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 