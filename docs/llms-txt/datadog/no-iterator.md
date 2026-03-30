# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-iterator.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-iterator.md

---
title: Avoid the use of the __iterator__ property
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid the use of the __iterator__ property
---

# Avoid the use of the __iterator__ property

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-iterator`

**Language:** JavaScript

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

The `__iterator__` property was exclusive to the SpiderMonkey engine. Avoid using it as other JavaScript engines do not implement it.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var a = test.__iterator__;
Foo.prototype.__iterator__ = function() {};
var a = test['__iterator__'];
var a = test[`__iterator__`];
test[`__iterator__`] = function () {};
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var a = test[__iterator__];
var __iterator__ = null;
foo[`__iterator`] = null;
foo[`__iterator__
`] = null;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
