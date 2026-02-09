# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/avoid-calendar-creation.md

---
title: Avoid Calendar class use
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid Calendar class use
---

# Avoid Calendar class use

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/avoid-calendar-creation`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Creating instances of `java.util.Calendar` is expensive. Use alternatives that are less heavy and better in terms of performance.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Main {
    public static void main(String[] args) {
        Date d = Calendar.getInstance().getTime();
        long ms = Calendar.getInstance().getTimeInMillis();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Main {
    public static void main(String[] args) {
        Date d = new Date();
        long ms = System.currentTimeMillis();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 