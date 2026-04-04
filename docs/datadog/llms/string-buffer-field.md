# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/string-buffer-field.md

---
title: Do not use StringBuffer or StringBuilder as a class field
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use StringBuffer or StringBuilder as a class field
---

# Do not use StringBuffer or StringBuilder as a class field

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/string-buffer-field`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

StringBuffers and StringBuilders have the potential to grow significantly, which could lead to memory leaks if they are retained within objects with extended lifetimes.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {

    private StringBuffer buffer1;    // potential memory leak as an instance variable;
    private String buffer2;
    private StringBuilder buffer3;    // potential memory leak as an instance variable;

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {

    public void method() {
        StringBuffer buffer;
    }

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
