# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/indexof-char.md

---
title: Do not use a string with only one character
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use a string with only one character
---

# Do not use a string with only one character

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/indexof-char`

**Language:** Java

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

When using `indexOf` with only one character, use a character and not a string as it executes faster.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        int pos = s.indexOf("f"); 
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        int pos = s.indexOf('f'); 
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 