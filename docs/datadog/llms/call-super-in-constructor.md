# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/call-super-in-constructor.md

---
title: Consider calling super in constructor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Consider calling super in constructor
---

# Consider calling super in constructor

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/call-super-in-constructor`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

In Java, it is suggested to call `super()` in an extended class. This rule will report a violation if both a call to `super()` and an overloaded constructor are absent.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo extends Bar{
    public Foo() {} // missing super()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo extends Bar{
    public Foo() {
        super(); // calls the Bar constructor
    }

    public Foo(int code) {
        this(); // also valid
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
