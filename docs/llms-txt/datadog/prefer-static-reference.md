# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/prefer-static-reference.md

---
title: References in a static method should prefer static over self
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > References in a static method should prefer static over self
---

# References in a static method should prefer static over self

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-best-practices/prefer-static-reference`

**Language:** PHP

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

This rule relates to how static methods are referenced within a class in PHP. The `self` keyword is used to refer to the same class in which the new keyword is being used. However, when dealing with static methods, it's considered best practice to use the `static` keyword instead of `self`.

The reason for this preference lies in the late static binding concept of PHP. If a child class inherits a static method from a parent class and you use `self` to reference it, it will call the parent's version of the method. But if you use `static`, it will call the child's version if it exists, providing more flexibility and correctly implementing the behavior of inheritance in object-oriented programming.

To adhere to this rule, always use `static` instead of `self` when referencing static methods within the same class. For instance, instead of `self::print()`, use `static::print()`. This practice ensures that your code is more robust and adaptable to changes in class hierarchy. You should do this even if your class is final; this will ensure that your code is still compliant if you ever decide to make it not final.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
public class Test {
    private static function print() {
        echo "Testing";
    }

    public static function display() {
        self::print();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
public class Test {
    private static function print() {
        echo "Testing";
    }

    public static function display() {
        static::print();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 