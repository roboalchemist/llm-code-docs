# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/detect-non-literal-require.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/detect-non-literal-require.md

---
title: Avoid require with non-literal values
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid require with non-literal values
---

# Avoid require with non-literal values

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/detect-non-literal-require`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [22](https://cwe.mitre.org/data/definitions/22.html)

## Description{% #description %}

Importing packages from dynamic paths can be a security vulnerability. An attacker might provide an undesired path that leads to running arbitrary code or reading sensitive information from your file system.

In Node.js, the `require()` function is a built-in function that allows modules to be loaded. You can use it to include various types of files (like .js, .json, .node, etc) in your project.

If the argument to `require()` is a variable instead of a static string, and if that variable's value can be influenced by user input, then an attacker might be able to exploit this to run arbitrary code or read sensitive files from your server's disk. This is a serious security issue often referred to as arbitrary code execution.

Dynamic imports are a common source of arbitrary file read and code execution vulnerabilities. Avoid using variables with `require` or `import` statements. If you have an advanced use case that requires the use of dynamic imports, make sure to sanitize the input and have an allowed list of paths you can import code from. Always set the proper access control to your file system.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var a = require(c);
var a = require(`${c}`);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var a = require('b');
var a = require(`b`);
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
