# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-unnecessary-class.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-unnecessary-class.md

---
title: Avoid unnecessary classes containing only static members
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unnecessary classes containing only static members
---

# Avoid unnecessary classes containing only static members

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-unnecessary-class`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule advises against the unnecessary use of classes that contain only static members, or nothing. In JavaScript, classes are primarily used for object-oriented programming, where each instance of a class has its own state and behavior. Static members, on the other hand, belong to the class itself and not to any instance of the class.

When a class contains only static members, it does not make use of JavaScript's object-oriented capabilities, and it can be more difficult to understand, test, and maintain than necessary. In order to avoid this issue, consider using regular functions and variables instead of static class members. This makes your code easier to understand and maintain, and it allows you to make better use of JavaScript's features.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
class Statics {
  static total = 10;

  static doubleTotal() {
    return Statics.total * 2;
  }
}

class DoThing {
  constructor() {
    thing.do();
  }
}

class Useless {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
export const total = 10;

export function doubleTotal() {
  return total * 2;
}

function doThing() {
  return thing.do();
}

class Foo {
  constructor() {
    this.prop = 'prop';
  }

  getProp() {
    return this.prop;
  }
}

class Foo2 {
  static foo;
  constructor() {
    this.prop = 'prop';
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 