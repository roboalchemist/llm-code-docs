# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-inclusive/formal-parameters.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-inclusive/formal-parameters.md

---
title: Check parameter names for wording issues
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check parameter names for wording issues
---

# Check parameter names for wording issues

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-inclusive/formal-parameters`

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
function a(master, slave) {}
function a(blacklist, whitelist) {}
class A { foo(master, slave) {} }
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
function denyList(primary, secondary) {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 