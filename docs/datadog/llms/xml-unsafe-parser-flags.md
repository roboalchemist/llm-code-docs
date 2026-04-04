# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/xml-unsafe-parser-flags.md

---
title: Avoid using unsafe flags in XML parsers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using unsafe flags in XML parsers
---

# Avoid using unsafe flags in XML parsers

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `php-security/xml-unsafe-parser-flags`

**Language:** PHP

**Severity:** Error

**Category:** Security

**CWE**: [611](https://cwe.mitre.org/data/definitions/611.html)

## Description{% #description %}

This rule is designed to prevent potential XML External Entity (XXE) attacks, which could allow an attacker to read local files on the server, interact with any external systems that the server can access, or perform a Denial-of-Service (DoS) attack.

The `LIBXML_NOENT` and `LIBXML_DTDLOAD` flags in PHP's `DOMDocument` or `SimpleXML` classes are particularly risky. The `LIBXML_NOENT` flag allows for the substitution of XML entities by their values, while the `LIBXML_DTDLOAD` flag enables loading of the XML Document Type Definition (DTD), both of which are common vectors for XXE attacks.

To avoid violating this rule, refrain from using these flags when loading XML data. Instead, use safer methods like `simplexml_load_string()` without any flags, as shown in the compliant code sample. This ensures that your PHP applications are not susceptible to XXE attacks, thus enhancing their security.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```php
<?php
class UserController extends Controller {
  public function xml($input) {
    $doc = new DOMDocument();
    $doc->loadXML($input, LIBXML_NOENT | LIBXML_DTDLOAD);
    return view('user.index', ['data' => $doc]);
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```php
<?php
class Foo extends Controller {
  public function xml($input) {
    $data = simplexml_load_string($xml_input);
    return view('user.index', ['data' => $data]);
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
