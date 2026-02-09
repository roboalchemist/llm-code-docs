# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/triple-slash-reference.md

---
title: Avoid triple slash in favor of ES6 import declarations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid triple slash in favor of ES6 import declarations
---

# Avoid triple slash in favor of ES6 import declarations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-best-practices/triple-slash-reference`

**Language:** TypeScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Use ESM instead of references.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
/// <reference path="foo" />
/// <reference types="bar" />
/// <reference lib="baz" />
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
import * as foo from 'foo';
import * as bar from 'bar';
import * as baz from 'baz';
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 