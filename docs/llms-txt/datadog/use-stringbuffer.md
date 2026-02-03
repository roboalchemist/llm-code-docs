# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/use-stringbuffer.md

---
title: Use StringBuffer to concatenate strings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use StringBuffer to concatenate strings
---

# Use StringBuffer to concatenate strings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/use-stringbuffer`

**Language:** Java

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

Use `StringBuffer` to create and concatenate long strings. Concatenating strings multiple times slows your program execution.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        String result = "";
        for (Person p: persons) {
            foo();
            result += p.getName() + ",";
            bar();
        }
        for(int i = 0 ; i < persons.size() ; i++) {
            foo();
            result += persons.get(i).getName() + ",";
            bar();
        }
        return result;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        StringBuilder result = new StringBuilder();
        for (Person p: persons) {
            result.append(p.getName() + ",");
        }
        return result.toString();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 