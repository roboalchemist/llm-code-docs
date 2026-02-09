# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/array-is-stored-directly.md

---
title: Should clone array
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Should clone array
---

# Should clone array

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/array-is-stored-directly`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Java, it is recommended that constructors and methods clone any arrays received through parameters. This practice prevents the original array from being affected by any future changes made by the caller.

It is advisable to clone the array before storing it to ensure that you retain a copy of the array that will remain unaffected by any external changes made to the original array. By following this approach, you can promote code safety and maintain the integrity of the original array.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    private String[] x;
    private int y;
    
    public Foo(String[] param1, int param2) {
        this.x = param1; // should make a copy of this array first
    }
}
```

```java
public class Foo {
    private int[] x;
    private int y;
    
    public void foo (int[] param1, int param2) {
        this.x = param1; // should make a copy of this array first
    }
}
```

```java
public class Foo {
    private String[] x;
    private int y;
    
    public void foo (String[] param1, int param2) {
        this.x = param1; // should make a copy of this array first
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
    private String[] x;
    private int y;
    
    public void foo (String[] param1, int param2) {
        this.x = Arrays.copyOf(param1, param1.length);
    }
}
```

```java
public class Foo {
    private String[] x;
    private int y;
    
    private void foo (String[] param1, int param2) {
        this.x = param1; // no violation since the method is private
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 