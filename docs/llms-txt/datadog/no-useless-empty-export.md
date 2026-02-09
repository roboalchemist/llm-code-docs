# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-useless-empty-export.md

---
title: Avoid empty exports that don't change anything
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid empty exports that don't change anything
---

# Avoid empty exports that don't change anything

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `typescript-code-style/no-useless-empty-export`

**Language:** TypeScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Do not use empty exports.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
export const value = 'Hello, world!';
export {};

import 'some-other-module';
export {};
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
declare module '_';
import {} from '_';
import * as _ from '_';
export = {};
export = 3;
export const _ = {};

const _ = {};
export default _;

export * from '_';
export = {};
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 