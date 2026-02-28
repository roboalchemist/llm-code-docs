# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-inclusive/identifiers.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-inclusive/identifiers.md

---
title: Check identifier names for wording issues
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check identifier names for wording issues
---

# Check identifier names for wording issues

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-inclusive/identifiers`

**Language:** JavaScript

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Ensure that some words are not used in the codebase and suggest a replacement when appropriate.

Examples of replacement suggestions:

- `blacklist` with `denylist`
- `whitelist` with `allowlist`
- `master` with `primary`
- `slave` with `secondary`

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
{ slave: false }
const a = { 'master': false, };
const a = { ['master']: false, };
const a = { c, ...blacklist } = b;
const { whitelist } = b;
const a = { whitelist };
const { whitelist: slave } = b;
[slave, ...master] = blacklist;
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
{ secondary: false }
const a = { 'primary': false, };
const a = { c, ...denylist } = b;
const { AllowedList } = b;
[primary, ...secondary] = b;
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
