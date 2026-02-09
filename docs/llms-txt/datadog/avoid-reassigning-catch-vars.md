# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/avoid-reassigning-catch-vars.md

---
title: Don't reassign a catch variable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Don't reassign a catch variable
---

# Don't reassign a catch variable

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/avoid-reassigning-catch-vars`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Maintaining a consistent link between the caught variable and the exception thrown in the corresponding `try` block brings clarity and predictability. Reassigning the caught variable disrupts this expectation and can lead to confusion. By refraining from these reassignments, developers can know that the variable encapsulates the essence of the original exception.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    public void foo() {
        try {
            // do something
        } catch (Exception e) {
            e = new NullPointerException(); // should not reassign here
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
    public void foo() {
        try {
            // do something
        } catch (MyException e) {
            newError = new RuntimeException(); // created a new error variable
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 