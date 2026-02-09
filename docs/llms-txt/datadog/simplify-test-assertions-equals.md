# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/simplify-test-assertions-equals.md

---
title: Test assertions using equals comparison can be simplified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Test assertions using equals comparison can be simplified
---

# Test assertions using equals comparison can be simplified

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/simplify-test-assertions-equals`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Test assertions can be made more concise through the utilization of a more specialized assertion method.

This rule checks for the use of `equals` in `assertTrue` or `assertFalse` methods and suggests replacing with either an `assertEquals` or `assertNotEquals` method.

This enhances the error message clarity and improves the overall readability of the assertion for other developers.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
import org.junit.Test;
import static org.junit.Assert.*;

class Foo {
    Object a,b;
    @Test
    void testFoo() {
        assertTrue(a.equals(b)); // could be assertEquals(a, b);
        assertTrue(!a.equals(b)); // could be assertNotEquals(a, b);

        assertFalse(a.equals(b)); // could be assertNotEquals(a, b);
        assertFalse(!a.equals(b)); // could be assertEquals(a, b);
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
        assertEquals(a, b);
        assertNotEquals(a, b);

        assertNotEquals(a, b);
        assertEquals(a, b);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 