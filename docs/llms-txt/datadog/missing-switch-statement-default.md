# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/missing-switch-statement-default.md

---
title: Switch statements should have a default case
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Switch statements should have a default case
---

# Switch statements should have a default case

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/missing-switch-statement-default`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

To improve the understandability your `switch` statement, it is recommended to make your statements exhaustive by incorporating a `default` case.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Foo {
    public String getValue() {
        int num = 10;
        System.out.println("foobar");
        switch (num) {
            case 1:
                return "One";
            case 2:
                return "Two";
            case 3:
                return "Three";
        }
    }

    public String getValue() {
        int num = 10;
        switch (num) {
            case 1:
                return "One";
            case 2:
                return "Two";
            case 3:
                return "Three";
        }
    }
}
```

```java
class Foo {
    public String getValue(int num) {
        switch (num) {
            case 1:
                return "One";
            case 2:
                return "Two";
            case 3:
                return "Three";
        }
    }
    public String getValue2(MyType num) {
        switch (num) {
            case 1:
                return "One";
            case 2:
                return "Two";
            case 3:
                return "Three";
        }
    }
}

class Bar {
    public String getValue(int num) {
        if (something) {
            switch (num) {
                case 1: // a comment
                    return "One";
                case 2:
                    return "Two"; // another comment
                case 3:
                    return "Three";
            }
        } else {
            if (somethingElse) {
                switch (num) {
                    case 'j': // a comment
                        return "One";
                    case 2.3:
                        return "Two"; // another comment
                    case 3:
                        return "Three";
                }
            }
        }
        
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Foo {
    public String getValue(int num) {
        switch (num) {
            case 1:
                return "One";
            case 2:
                return "Two";
            case 3:
                return "Three";
            default:
                return "Unknown"
        }
    }
}

class Bar {
    public String getValue(int num) {
        switch (num) {
            case 1: // a comment
                return "One";
            case 2:
                return "Two"; // another comment
            case 3:
                return "Three";
            default:
                return "Unknown"
        }
    }
}

class Bar {
    public String getValue(int num) {
        return switch (num) {
            case 1 -> "one";
            case 2 -> "two";
            default -> "unknown";
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 