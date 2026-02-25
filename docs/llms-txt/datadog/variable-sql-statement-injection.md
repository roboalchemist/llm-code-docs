# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/variable-sql-statement-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/variable-sql-statement-injection.md

---
title: Avoid SQL injections
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid SQL injections
---

# Avoid SQL injections

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-node-security/variable-sql-statement-injection`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [89](https://cwe.mitre.org/data/definitions/89.html)

## Description{% #description %}

Check for variable declarations in a SQL statement where there is potential for SQL injections.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var table = 'baz';

const foo = "SELECT foo FROM " + table;
const select = `SELECT foo FROM ${table}`;
var del = `DELETE FROM ${table} WHERE condition;`;
let update = ' UPDATE ' +
             table +
             "SET column1 = value1, column2 = value2" +
             "WHERE condition;";
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
