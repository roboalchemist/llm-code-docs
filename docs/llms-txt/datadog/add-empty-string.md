# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/add-empty-string.md

---
title: Do not add an empty string
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not add an empty string
---

# Do not add an empty string

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/add-empty-string`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Do not add an empty string. Use the appropriate method to generate the data you need, and add the `toString` method of the type you want to export as a string.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Main {

    public static void main(String[] args) {
        String s = "" + 239;
        String t = "123" + 456;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Main {

    public static void main(String[] args) {
        String s = Integer.toString(239);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
