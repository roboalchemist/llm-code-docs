# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/switch-few-branches.md

---
title: Avoid switch with very few branches
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid switch with very few branches
---

# Avoid switch with very few branches

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/switch-few-branches`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

`switch` statements are used to trigger different block of code based on different values. Developers should avoid `switch` statements with less than 3 branches. If a `switch` statement has less than 3 branches, we should rather use a `if` statement.

## Arguments{% #arguments %}

- `max-cases`: Max number of cases allowed

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        switch (condition) {
            case value1:
                break;
        }

        switch (condition) {
            case value1:
                break;
            case value2:
                break;
            default:
                break;
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        switch (condition) {
            case value1:
                break;
            case value2:
                break;
            default:
                break;
        }

        switch (condition) {
            case value1: // comments are supported
            case value2:
                break;
            default:
                break;
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 