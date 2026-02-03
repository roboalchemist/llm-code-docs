# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/one-declaration-per-line.md

---
title: Separate lines for each field declaration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Separate lines for each field declaration
---

# Separate lines for each field declaration

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/one-declaration-per-line`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Java, it is possible to declare multiple variables of the same type on a single line using commas. This can make code more cluttered and less readable. Declare each variable on a separate line to improve code clarity and maintainability.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Person {
    // combined declarations (same line) - a violation
    String firstName, lastName;

    // combined declaration (diff line) - no violation
    String firstName,
        lastName;
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Person {
    // separate declarations - no violation
    String firstName;
    String lastName;     
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 