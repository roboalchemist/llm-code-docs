# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/preserve-stack-trace.md

---
title: Preserve the thrown stack trace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Preserve the thrown stack trace
---

# Preserve the thrown stack trace

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/preserve-stack-trace`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule identifies when exceptions are raised within a `catch` block but are not relevant to the exception parameter specified in the `catch` block. This can result in the original exception's stack trace information being lost, which leads to throwing less detailed exceptions.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    void foo() {
        try {
            Integer.parseInt("foo");
        } catch (Exception e) {
            throw new Exception(e.getMessage()); // only throwing the message here
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
    void foo() {
        try {
            Integer.parseInt("foo");
        } catch (Exception e) {
            throw new Exception(e); // sending the full exception at least
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
