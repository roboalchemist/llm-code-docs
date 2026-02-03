# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/redundant-initializer.md

---
title: Avoid redundant initialization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid redundant initialization
---

# Avoid redundant initialization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/redundant-initializer`

**Language:** Java

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

When initializing fields, prevent initializing fields to the default value. Any additional initialization means more bytecode instructions, and allocating many of these objects may impact your application performance.

If you initialize to a default value, remove the initialization.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Test {
    boolean b   = false;
    byte by     = 0;
    short s     = 0;
    char c      = 0;
    int i       = 0;
    long l      = 0;
    float f     = .0f;
    double d    = 0d;
    Object o    = null;

    MyClass mca[] = null;
    int i1 = 0, i2 = 0;
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Test {
    boolean b                = true;
    byte by                  = 1;
    short s                  = 2;
    char c                   = 3;
    int i                    = 4;
    long l                   = 5;
    public final boolean b   = false;
    final long l             = 0;
    float f                  = .1f;
    double d                 = 10d;
    Object o                 = new Object();

    MyClass mca[] = new MyClass[3];
    int i1 = 1, ia1[] = new Something[];

}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 