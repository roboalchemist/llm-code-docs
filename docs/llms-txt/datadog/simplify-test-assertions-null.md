# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/simplify-test-assertions-null.md

---
title: Test assertions using null comparison can be simplified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Test assertions using null comparison can be simplified
---

# Test assertions using null comparison can be simplified

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/simplify-test-assertions-null`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Test assertions can be made more concise through the use of a more specialized assertion method.

In this rule, we check for `null` comparisons in `assertTrue` or `assertFalse` methods and suggest replacing with either an `assertNull` or `assertNonNull` method.

This enhances the error message clarity and improves the overall readability of the assertion for other developers.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
import org.junit.Test;
import static org.junit.Assert.*;

class Foo {
    Object a,b;
    @Test
    void testFoo() {
        assertTrue(a == null); // could be assertNull(a);
        assertTrue(a != null); // could be assertNotNull(a);

        assertFalse(a == null); // could be assertNotNull(a);
        assertFalse(a != null); // could be assertNull(a);
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
        assertNull(a);
        assertNotNull(a);

        assertNotNull(a);
        assertNull(a);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 