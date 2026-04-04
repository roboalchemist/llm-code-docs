# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-useless-constructor.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-useless-constructor.md

---
title: Avoid constructors that do nothing or only call super
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid constructors that do nothing or only call super
---

# Avoid constructors that do nothing or only call super

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-useless-constructor`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule is designed to flag constructors that either do nothing or only call the `super` function. These constructors are unnecessary and can be safely removed. In JavaScript, if a class extends another class and does not have a constructor, it automatically calls the `super` function with all the arguments it receives.

Unnecessary constructors can lead to confusion for other developers who may be reading or maintaining your code. They might spend time trying to figure out why a constructor is there when it doesn't need to be, or they might assume that the constructor is doing something important when it's not. To follow this rule and write good, clean code, you should only write a constructor if it's doing something other than just calling `super`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
class Foo {
    constructor () {}
}

class Bar extends Foo {
    constructor (...args) {
      super(...args);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
class Foo {}

class Bar {
    constructor () {
        doComputation();
    }
}

class Baz extends Foo {
    constructor() {
        super('baz arg');
    }
}

class Quux extends Foo {
    constructor() {
        super();
        doComputation();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
