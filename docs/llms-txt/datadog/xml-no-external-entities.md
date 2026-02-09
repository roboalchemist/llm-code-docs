# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-common-security/xml-no-external-entities.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-common-security/xml-no-external-entities.md

---
title: Do not use external XML entities
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use external XML entities
---

# Do not use external XML entities

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-common-security/xml-no-external-entities`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [611](https://cwe.mitre.org/data/definitions/611.html)

## Description{% #description %}

Process external entities in XML files may lead to XXE attack. Do not load external entities unless they have been explicitly checked.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var libxmljs = require('libxmljs');
var fs = require('fs');

var xml = fs.readFileSync('file.xml', 'utf8');
libxmljs.parseXmlString(xml, {
    noent: true,
});
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var libxmljs = require('libxmljs');
var fs = require('fs');

var xml = fs.readFileSync('file.xml', 'utf8');
libxmljs.parseXmlString(xml);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 