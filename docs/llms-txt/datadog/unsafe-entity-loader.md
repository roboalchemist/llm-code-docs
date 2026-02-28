# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/unsafe-entity-loader.md

---
title: Avoid enabling entity loader
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid enabling entity loader
---

# Avoid enabling entity loader

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/unsafe-entity-loader`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [611](https://cwe.mitre.org/data/definitions/611.html)

## Description{% #description %}

The ability to load external entities while parsing XML data should be disabled. This helps prevent XML External Entity (XXE) attacks, which can lead to disclosure of internal files, denial of service, server side request forgery, port scanning from the perspective of the machine where the parser is located, and other system impacts.

In PHP versions before 8.0, `libxml_disable_entity_loader()` is set to `true` by default, which means that loading of external entities is disabled. However, if you explicitly set this function to `false`, as seen in the non-compliant code sample, you are enabling the loading of external entities, thereby opening up potential security vulnerabilities.

To adhere to this rule and ensure the security of your PHP applications, you should avoid enabling the entity loader. This means that you should not use `libxml_disable_entity_loader(false)`. Instead, let the function retain its default value of `true`. If you need to parse XML data, use secure functions such as `simplexml_load_string()` or `DOMDocument::loadXML()`, as seen in the compliant code sample. These functions are designed to safely parse XML data without exposing your application to XXE attacks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php

class Foo extends Controller {
  public function test($input) {
    libxml_disable_entity_loader(false);
    $doc = new DOMDocument();
    $doc->loadXML($input);
    return view('user.index', []);
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php

class Foo extends Controller {
  public function test($id) {
    libxml_disable_entity_loader(true);
    $data = simplexml_load_string($xml_input);
    return view('user.index', ['data' => $data]);
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
