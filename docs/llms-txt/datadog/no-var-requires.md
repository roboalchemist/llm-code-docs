# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-var-requires.md

---
title: Avoid require statements
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid require statements
---

# Avoid require statements

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/no-var-requires`

**Language:** TypeScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Use ESM instead of CommonJS imports.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
var foo = require('foo');
const foo = require('foo');
let foo = require('foo');
let foo = trick(require('foo'));
var foo = require?.('foo');
const foo = require?.('foo');
let foo = require?.('foo');
let foo = trick(require?.('foo'));
let foo = trick?.(require('foo'));
const foo = require('./foo.json') as Foo;
const foo: Foo = require('./foo.json').default;

// const foo = <Foo>require('./foo.json');

// https://github.com/typescript-eslint/typescript-eslint/issues/3883
// const configValidator = new Validator(require('./a.json'));
// configValidator.addSchema(require('./a.json'));
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
import foo = require('foo');
require('foo');
require?.('foo');
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 