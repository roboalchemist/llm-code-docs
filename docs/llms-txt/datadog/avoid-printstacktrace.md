# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/avoid-printstacktrace.md

---
title: Avoid using printStackTrace()
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using printStackTrace()
---

# Avoid using printStackTrace()

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/avoid-printstacktrace`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Use a logging framework instead of `printStackTrace()` when handling exceptions. `printStackTrace()` can be useful during development for quick debugging, but it is not suitable for production code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Foo {
    void bar() {
        try {
            // removed for brevity
        } catch (MyException myException) {
            myException.printStackTrace();
        } catch (Exception e) {
            if ("foo" != "bar") {
                e.printStackTrace();
            }
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Foo {
    void bar() {
        try {
            // removed for brevity
        } catch (MyException myException) {
            myException.printStackTrace();
        } catch (Exception e) {
            if ("foo" != "bar") {
                e.printStackTrace();
            }
        }
    }
}
```

```java
import java.util.logging.Logger;

class Foo {
    private static final Logger logger = Logger.getLogger(Foo.class.getName());

    void bar() {
        try {
            // Code that may throw an exception
            throw new RuntimeException("Something went wrong!");
        } catch (Exception e) {
            // Log the exception using the Java logger
            logger.severe("An error occurred:");
            logger.severe(e.toString());

            if ("foo" != "bar") {
                // Log the exception again if needed
                logger.severe("An error occurred in an additional context:");
                logger.severe(e.toString());
            }
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
