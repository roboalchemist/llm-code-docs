# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/spring-expression-injection.md

---
title: Potential code injection when using Spring Expression
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Potential code injection when using Spring Expression
---

# Potential code injection when using Spring Expression

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/spring-expression-injection`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [94](https://cwe.mitre.org/data/definitions/94.html)

## Description{% #description %}

A Spring expression is built on a dynamic value using an input string. The source should be checked to ensure there is no injection.

#### Learn More{% #learn-more %}

- [CWE-94: Improper Control of Generation of Code ('Code Injection')](https://cwe.mitre.org/data/definitions/94.html)
- [Beware of the Magic SpEL(L) â Part 2 (CVE-2018-1260)](https://www.gosecure.net/blog/2018/05/17/beware-of-the-magic-spell-part-2-cve-2018-1260/)
- [Potential code injection when using Spring Expression](https://find-sec-bugs.github.io/bugs.htm#SPEL_INJECTION)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyClass {
    public void parseExpressionInterface(Person personObj,String property) {

        ExpressionParser parser = new SpelExpressionParser();

        //Unsafe if the input is control by the user..
        Expression exp = parser.parseExpression(property+" == 'Albert'");

        StandardEvaluationContext testContext = new StandardEvaluationContext(personObj);
        boolean result = exp.getValue(testContext, Boolean.class);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 