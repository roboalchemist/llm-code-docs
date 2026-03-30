# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/simplify-test-assertions-ops.md

---
title: Test assertions using operator comparison can be simplified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Test assertions using operator comparison can be simplified
---

# Test assertions using operator comparison can be simplified

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/simplify-test-assertions-ops`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Test assertions can be made more concise through the utilization of a more specialized assertion method.

In this rule, we check for the use of operators, such as, `==` and `!=` in `assertTrue` or `assertFalse` methods and suggest replacing with either a `assertSame` or `assertNotSame` method.

This enhances the error message clarity and improves the overall readability of the assertion for other developers.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
import org.junit.Test;
import static org.junit.Assert.*;

class Foo {
    Object a,b;
    @Test
    void testFoo() {
        assertTrue(a == b); // could be assertSame(a, b);
        assertTrue(a != b); // could be assertNotSame(a, b);

        assertFalse(a == b); // could be assertNotSame(a, b);
        assertFalse(a != b); // could be assertSame(a, b);
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
        assertSame(a, b);
        assertNotSame(a, b);

        assertNotSame(a, b);
        assertSame(a, b);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
