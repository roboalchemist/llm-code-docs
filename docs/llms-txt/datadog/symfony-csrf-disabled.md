# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/symfony-csrf-disabled.md

---
title: Do not disable CSRF protection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not disable CSRF protection
---

# Do not disable CSRF protection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/symfony-csrf-disabled`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [352](https://cwe.mitre.org/data/definitions/352.html)

## Description{% #description %}

CSRF (Cross-Site Request Forgery) is an attack that tricks the victim into submitting a malicious request. It uses the identity and privileges of the victim to perform an undesired function on their behalf.

Disabling CSRF protection exposes your application to such attacks, compromising user data and potentially leading to unauthorized actions. For instance, an attacker could forge a request to change the email address on record for the victim's account, effectively hijacking the account.

To avoid violating this rule, ensure that 'csrf_protection' is set to true in your PHP code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
class Foo
{
  public function configureOptions(OptionsResolver $resolver)
  {
    $resolver->setDefaults([
      'data_class'      => Type::class,
      'csrf_protection' => false
    ]);
    $resolver->setDefaults(array(
      'csrf_protection' => false
    ));
  }
}

class Bar extends Extension implements PrependExtensionInterface
{
  public function prepend(ContainerBuilder $container)
  {
    $container->prependExtensionConfig('framework', ['csrf_protection' => false]);
    $container->loadFromExtension('framework', ['csrf_protection' => false]);
  }
}

class Baz extends AbstractController
{
  public function action()
  {
    $this->createForm(TaskType::class, $task, array(
      'csrf_protection' => false,
    ));
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
class Foo
{
  public function configureOptions(OptionsResolver $resolver)
  {
    $resolver->setDefaults([
      'data_class'      => Type::class,
      'csrf_protection' => true,
    ]);
    $resolver->setDefaults(array(
      'csrf_protection' => true,
    ));
  }
}

class Bar extends Extension implements PrependExtensionInterface
{
  public function prepend(ContainerBuilder $container)
  {
    $container->prependExtensionConfig('framework', ['csrf_protection' => true]);
    $container->loadFromExtension('framework', ['csrf_protection' => true]);
  }
}

class Baz extends AbstractController
{
  public function action()
  {
    $this->createForm(TaskType::class, $task, array(
      'csrf_protection' => true,
    ));
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
