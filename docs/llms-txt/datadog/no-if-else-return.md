# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-if-else-return.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-if-else-return.md

---
title: Avoid unnecessary if-else chains that only returns a boolean
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unnecessary if-else chains that only returns a boolean
---

# Avoid unnecessary if-else chains that only returns a boolean

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-if-else-return`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule is designed to simplify your code by avoiding unnecessary if-else chains that only return a boolean. In JavaScript, it's not necessary to use an if-else statement to return a boolean value from a function. Instead, you can return the result of the boolean expression. This makes your code shorter, cleaner, and easier to understand.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
function getFoo() {
  const foo = computeFoo();
  if (foo) {
    return true;
  } else {
    return false;
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
function getFoo() {
  const foo = computeFoo();
  return foo;
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 