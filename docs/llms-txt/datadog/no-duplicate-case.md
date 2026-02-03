# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-duplicate-case.md

---
title: Avoid duplicate case labels
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid duplicate case labels
---

# Avoid duplicate case labels

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-duplicate-case`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

It is easy to copy and paste a switch statement case, and leave behind duplicated test cases.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
var a = 1; switch (a) {case 1: break; case 1: break; case 2: break; default: break;}
var a = '1'; switch (a) {case '1': break; case '1': break; case '2': break; default: break;}
var a = 1, one = 1; switch (a) {case one: break; case one: break; case 2: break; default: break;}
var a = 1, p = {p: {p1: 1, p2: 1}}; switch (a) {case p.p.p1: break; case p.p.p1: break; default: break;}
var a = 1, f = function(b) { return b ? { p1: 1 } : { p1: 2 }; }; switch (a) {case f(true).p1: break; case f(true).p1: break; default: break;}
var a = 1, f = function(s) { return { p1: s } }; switch (a) {case f(a + 1).p1: break; case f(a + 1).p1: break; default: break;}
var a = 1, f = function(s) { return { p1: s } }; switch (a) {case f(a === 1 ? 2 : 3).p1: break; case f(a === 1 ? 2 : 3).p1: break; default: break;}
var a = 1, f1 = function() { return { p1: 1 } }; switch (a) {case f1().p1: break; case f1().p1: break; default: break;}
var a = [1, 2]; switch(a.toString()){case ([1, 2]).toString():break; case ([1, 2]).toString():break; default:break;}
switch (a) { case a: case a: }
switch (a) { case a: break; case b: break; case a: break; case c: break; case a: break; }
var a = 1, f = function(s) { return { p1: s } }; switch (a) {case f(a + 1).p1: break; case f(a+1).p1: break; default: break;}
// limitations
var a = 1, p = {p: {p1: 1, p2: 1}}; switch (a) {case p.p.p1: break; case p. p // comment
 .p1: break; default: break;}
var a = 1, p = {p: {p1: 1, p2: 1}}; switch (a) {case p .p
    /* comment */
    .p1: break; case p.p.p1: break; default: break;}
var a = 1, p = {p: {p1: 1, p2: 1}}; switch (a) {case p .p
    /* comment */
    .p1: break; case p. p // comment
 .p1: break; default: break;}
var a = 1, p = {p: {p1: 1, p2: 1}}; switch (a) {
    case p.p.p1: break; case p. p // comment
     .p1: break; case p .p
     /* comment */
     .p1: break; default: break;}
var a = 1, f = function(s) { return { p1: s } }; switch (a) {case f(
    a + 1 // comment
    ).p1: break; case f(a+1)
    .p1: break; default: break;}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
var a = 1; switch (a) {case 1: break; case 2: break; default: break;}
var a = 1; switch (a) {case 1: break; case '1': break; default: break;}
var a = 1; switch (a) {case 1: break; case true: break; default: break;}
var a = 1; switch (a) {default: break;}
var a = 1, p = {p: {p1: 1, p2: 1}}; switch (a) {case p.p.p1: break; case p.p.p2: break; default: break;}
var a = 1, f = function(b) { return b ? { p1: 1 } : { p1: 2 }; }; switch (a) {case f(true).p1: break; case f(true, false).p1: break; default: break;}
var a = 1, f = function(s) { return { p1: s } }; switch (a) {case f(a + 1).p1: break; case f(a + 2).p1: break; default: break;}
var a = 1, f = function(s) { return { p1: s } }; switch (a) {case f(a == 1 ? 2 : 3).p1: break; case f(a === 1 ? 2 : 3).p1: break; default: break;}
var a = 1, f1 = function() { return { p1: 1 } }, f2 = function() { return { p1: 2 } }; switch (a) {case f1().p1: break; case f2().p1: break; default: break;}
var a = [1,2]; switch(a.toString()){case ([1,2]).toString():break; case ([1]).toString():break; default:break;}
switch(a) { case a: break; } switch(a) { case a: break; }
switch(a) { case toString: break; 
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 