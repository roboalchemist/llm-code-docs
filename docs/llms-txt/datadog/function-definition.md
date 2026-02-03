# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-inclusive/function-definition.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-inclusive/function-definition.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-inclusive/function-definition.md

---
title: Avoid non-inclusive terms in function and parameter names
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid non-inclusive terms in function and parameter names
---

# Avoid non-inclusive terms in function and parameter names

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-inclusive/function-definition`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule promotes inclusive language by flagging the use of potentially offensive or outdated terms in function and parameter names. Words like "blacklist", "whitelist", "master", and "slave" carry historical and social connotations that can be exclusionary and lead to a less welcoming codebase. Adopting inclusive terminology improves code readability, reflects modern best practices, and fosters a more diverse and respectful development environment.

## How to remediate{% #how-to-remediate %}

To fix this violation, replace the discouraged terms with their inclusive alternatives. For "blacklist," use "denylist" or "blocklist." For "whitelist," use "allowlist" or "safelist." For "master," use "primary," "main," or "controller." For "slave," use "secondary," "replica," or "worker." Applying these changes ensures your code aligns with contemporary language standards and promotes clarity without cultural bias.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class MyClass {
    void blacklist() {

    }

    int method(int WhiteList) {

    }
}
```

```java
class Blacklist {
    void blacklist() {

    }

    int BlackList(int WhiteList) {

    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class AllowList {
    void allowlist() {

    }

    int AllowList(int AllowList) {

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 