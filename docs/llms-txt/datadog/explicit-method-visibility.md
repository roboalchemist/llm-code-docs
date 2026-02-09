# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/explicit-method-visibility.md

---
title: Methods should explicitly declare their visibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Methods should explicitly declare their visibility
---

# Methods should explicitly declare their visibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-best-practices/explicit-method-visibility`

**Language:** PHP

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In PHP, it's considered best practice to explicitly declare the visibility of methods in a class. The visibility of a method or property can be defined by prefixing the declaration with the keywords `public`, `protected`, or `private`.

The importance of this rule lies in the principle of encapsulation in object-oriented programming. By declaring method visibility, you ensure that your code is more readable, maintainable, and less prone to errors or unexpected behavior. It also helps in controlling the accessibility of the methods, which is crucial for large-scale applications and team projects.

To abide by this rule, always ensure that you specify the visibility when declaring methods in your classes. This could be `public`, `protected`, or `private`, depending on the level of accessibility you want to provide. For example, use `public function test()` instead of just `function test()`. This will ensure your code is compliant, easier to understand, and better organized.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
class Foo {
    function test() {
        echo "Test";
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
class Foo {
    public function test() {
        echo "Test";
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 