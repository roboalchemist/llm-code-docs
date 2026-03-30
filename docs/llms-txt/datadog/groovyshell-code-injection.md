# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/groovyshell-code-injection.md

---
title: Potential code injection when using GroovyShell
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Potential code injection when using GroovyShell
---

# Potential code injection when using GroovyShell

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/groovyshell-code-injection`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [94](https://cwe.mitre.org/data/definitions/94.html)

## Description{% #description %}

An expression for GroovyScript is built with a dynamic value. The source should be checked and filtered to prevent any user-input from the script.

#### Learn More{% #learn-more %}

- [Potential code injection when using GroovyShell](https://find-sec-bugs.github.io/bugs.htm#GROOVY_SHELL)
- [Example of Vulnerability](https://github.com/welk1n/exploiting-groovy-in-Java/)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyClass {

    public void evaluateScript(String script) {
        GroovyShell shell = new GroovyShell();
        shell.evaluate(script);

        foo = shell.evaluate(script);

        shell.evaluate("foo" + script);
        shell.evaluate(script + "foo");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class MyClass {

    public void evaluateScript(String script) {
        GroovyShell shell = new GroovyShell();
        shell.evaluate(checkScript(script));
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
