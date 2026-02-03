# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/useless-null.md

---
title: Avoid useless null checks on guaranteed non-null values.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid useless null checks on guaranteed non-null values.
---

# Avoid useless null checks on guaranteed non-null values.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/useless-null`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule flags null checks (`== null` or `!= null`) performed on expressions that are guaranteed by the Java language specification to never be null.

Certain expressions, such as the `this` keyword, object creation with `new`, literals (e.g., `"hello"`, `42`), and class literals (`.class`), can never evaluate to null. A check against null on any of these expressions is redundant and results in dead code that will never execute. This adds unnecessary clutter and can mislead developers into thinking the variable could be null under some circumstances.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
/**
 * This class serves as a comprehensive non-compliant test case.
 * Each method demonstrates a null check against an expression that is
 * guaranteed by the language to be non-null. The static analysis rule
 * should flag every "if" statement within this class.
 */
public class UselessNullChecks {

    private String name;

    public UselessNullChecks(String name) {
        this.name = name;
    }

    // 1. Checking 'this'
    public void checkThisKeyword() {
        if (this == null) { // Non-compliant: 'this' is never null.
            System.out.println("Error: 'this' is null.");
        }
    }

    // 2. Checking a 'new' object creation expression
    public void checkNewObject() {
        if (new UselessNullChecks("test") == null) { // Non-compliant: 'new' returns a non-null instance or throws.
            System.out.println("Error: Object creation resulted in null.");
        }
    }

    // 3. Checking various literals that are never null
    public void checkLiterals() {
        if ("some string" == null) { // Non-compliant: String literal
            System.out.println("Error: String literal is null.");
        }
        if (42 == null) { // Non-compliant: Integer literal
             System.out.println("Error: Integer literal is null.");
        }
        if (true != null) { // Non-compliant: Boolean literal
            System.out.println("Boolean literal is not null.");
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
/**
 * This class serves as a comprehensive compliant test case.
 * It showcases legitimate scenarios where a null check is necessary to
 * prevent NullPointerExceptions. The static analysis rule should not
*  flag any of the "if" statements within this class.
 */
public class NecessaryNullChecks {

    private String value;

    public NecessaryNullChecks(String value) {
        this.value = value;
    }

    // A method that can return null
    private String findProperty(String key) {
        if ("name".equals(key)) {
            return this.value;
        }
        return null; // A method can legitimately return null.
    }

    // 1. Checking a method parameter which could be null
    public void processInput(Object input) {
        if (input == null) { // Compliant: Parameters can be null.
            System.out.println("Input was null, cannot proceed.");
            return;
        }
        System.out.println("Processing: " + input.toString());
    }

    // 2. Checking the result of a method call that may return null
    public void checkMethodResult() {
        String property = findProperty("address");
        if (property == null) { // Compliant: The method is designed to return null.
            System.out.println("Property not found.");
        } else {
            System.out.println("Property length: " + property.length());
        }
    }

    // 3. Checking a field that can be null
    public void checkField() {
        // Create an instance where the field is null
        NecessaryNullChecks instance = new NecessaryNullChecks(null);
        if (instance.value == null) { // Compliant: A class field can be null.
            System.out.println("The instance's value field is null.");
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 