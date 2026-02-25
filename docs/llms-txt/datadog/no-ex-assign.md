# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-ex-assign.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-ex-assign.md

---
title: Avoid reassigning exceptions in catch clauses
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid reassigning exceptions in catch clauses
---

# Avoid reassigning exceptions in catch clauses

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-ex-assign`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

Catching an exception and assigning a different value to the error parameter will overwrite the reference to the original error data, which will be lost since there is no `arguments` object in a catch clause.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
try { } catch (e) { e = 10; }
try { } catch (ex) { ex = 10; }
try { } catch (ex) { [ex] = []; }
try { } catch (ex) { ({x: ex = 0} = {}); }
try { } catch ({message}) { message = 10; }
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
try { } catch (e) { three = 2 + 1; }
try { } catch ({e}) { this.something = 2; }
function foo() { try { } catch (e) { return false; } }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
