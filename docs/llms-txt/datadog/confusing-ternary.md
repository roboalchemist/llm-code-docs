# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/confusing-ternary.md

---
title: Avoid negation in your ternary operation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid negation in your ternary operation
---

# Avoid negation in your ternary operation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/confusing-ternary`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Using a negative comparison in `if` expressions with an `else` clause can be confusing. Consider modifying your comparison by switching your `if` and else` block statements.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    String bar(int x, int y) {
        return (x != y) ? "diff" : "same";
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
    String bar(int x, int y) {
        return (x == y) ? "same" : "diff";
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 