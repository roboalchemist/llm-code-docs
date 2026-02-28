# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/avoid-string-instantiation.md

---
title: 'Avoid instantiating strings '
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid instantiating strings
---

# Avoid instantiating strings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/avoid-string-instantiation`

**Language:** Java

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

Instead of creating a new string with `new String()`, use the string directly.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Main{
    public static void main(String[] args){
        String s = new String("foobar");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Main{
    public static void main(String[] args){
        String s = "foobar";
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
