# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/avoid-protected-in-final-class.md

---
title: Avoid using protected field in final class
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using protected field in final class
---

# Avoid using protected field in final class

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/avoid-protected-in-final-class`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Avoid setting fields as protected inside a final class as they cannot be subclassed.

If flagged, review your class and its usage. Consider adjusting your modifiers and their access.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public final class Foo {
    private int x;
    protected int y; // visibility should be reviewed

    protected int getY() { // visibility should be reviewed
        return y;
    };
    Foo() {}
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public final class Foo {
    private int x;
    public int y;

    public int getY() {
        return y;
    };
    Foo() {}
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
