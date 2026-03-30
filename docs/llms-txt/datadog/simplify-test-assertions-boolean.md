# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/simplify-test-assertions-boolean.md

---
title: Test assertions for booleans can be simplified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Test assertions for booleans can be simplified
---

# Test assertions for booleans can be simplified

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/simplify-test-assertions-boolean`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Test assertions can be made more concise through the utilization of a more specialized assertion method.

This rule checks for a not operator (`!`) in `assertTrue` or `assertFalse` methods and suggests replacing the operator with the `assertTrue` or `assertFalse` method.

This enhances the error message clarity and improves the overall readability of the assertion for other developers.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
import org.junit.Test;
import static org.junit.Assert.*;

class Foo {
    Object a,b;
    @Test
    void testFoo() {
        assertTrue(!something); // could be assertFalse(something);
        assertFalse(!something); // could be assertTrue(something);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
import org.junit.Test;
import static org.junit.Assert.*;

class Foo {
    Object a,b;
    @Test
    void testFoo() {
        assertFalse(something);
        assertTrue(something);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
