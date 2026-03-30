# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/avoid-propagate-exception-info.md

---
title: Avoid propagation exception messages
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid propagation exception messages
---

# Avoid propagation exception messages

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/avoid-propagate-exception-info`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule aims to discourage the direct propagation or usage of exception messages in the code. Exception messages can often contain sensitive or implementation-specific information that should not be exposed or relied upon for program logic. Relying on exception messages can lead to fragile code that breaks if the message text changes in future library or framework updates.

To comply with this rule, handle exceptions by using their types, custom error codes, or well-defined error objects instead of their message strings. For example, instead of `e.getMessage()`, consider catching specific exception subclasses or defining your own error classification. This approach leads to cleaner, more reliable error handling and protects sensitive information.

Example of compliant handling: `catch (SpecificException ex) { log("Known error occurred"); }` rather than inspecting `ex.getMessage()` contents.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Foo {
    public bar() {
        try {
            // something
        } catch (Exception e) {
            var message = someList.contains(e.getCause()) ? "known issue" : "unknown"
            System.out.println(message)
        }
    }
}
```

```java
class Foo {
    public bar() {
        try {
            // something
        } catch (Exception e) {
            var message = someList.contains(e.getMessage()) ? e.getMessage() : "unknown"
            System.out.println(message)
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Foo {
    public bar() {
        try {
            // something
        } catch (Exception e) {
            System.out.println(message)
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
