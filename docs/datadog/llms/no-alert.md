# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-alert.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-alert.md

---
title: Avoid the use of alert, confirm, and prompt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid the use of alert, confirm, and prompt
---

# Avoid the use of alert, confirm, and prompt

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-alert`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

JavaScript's `alert`, `confirm`, and `prompt` functions present obtrusive UI elements that prevent further user actions by taking control of the focus. These UI elements cannot be styled.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
alert(foo)
window.alert(foo)
window['alert'](foo)
confirm(foo)
window.confirm(foo)
window['confirm'](foo)
prompt(foo)
window.prompt(foo)
window['prompt'](foo)
function alert() {} window.alert(foo)
var alert = function() {};
window.alert(foo)
function foo(alert) { window.alert(); }
function foo() { alert(); }
function foo() { var alert = function() {}; }
alert();
this.alert(foo)
this['alert'](foo)
function foo() { var window = bar; window.alert(); }
window.alert();
globalThis['alert'](foo)
globalThis.alert();
function foo() { var globalThis = bar; globalThis.alert(); }
globalThis.alert();

// Optional chaining
window?.alert(foo);
(window?.alert)(foo);
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
a[o.k](1)
foo.alert(foo)
foo.confirm(foo)
foo.prompt(foo)
// global overrides are not recommened
// and wont be supported by this rule
// function alert() {} alert();
// var alert = function() {}; alert();
// function foo() { var alert = bar; alert(); }
// function foo(alert) { alert(); }
// var alert = function() {}; function test() { alert(); }
// function foo() { var alert = function() {}; function test() { alert(); } }
// function confirm() {} confirm();
// function prompt() {} prompt();
window[alert]();
// function foo() { this.alert(); }
// function foo() { var window = bar; window.alert(); }
// globalThis.alert();
// globalThis['alert']();
// globalThis.alert();
// var globalThis = foo; globalThis.alert();
// function foo() { var globalThis = foo; globalThis.alert(); }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
