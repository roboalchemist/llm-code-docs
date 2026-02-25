# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/no-empty.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/no-empty.md

---
title: Avoid empty block statements
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid empty block statements
---

# Avoid empty block statements

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/no-empty`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

**CWE**: [670](https://cwe.mitre.org/data/definitions/670.html)

## Description{% #description %}

Empty or non-functional blocks in the code can be misleading and lead to maintenance difficulties. They can also lead to a false sense of security or functionality. While they may not directly introduce security issues, their presence can suggest that some logic or error handling is implemented when it is not.

You can avoid this problem by including a comment to indicate that you intend to leave the block empty. For example:

```javascript
while (runIteration()) {
  // do nothing
}
```

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
try {} catch (ex) {throw ex}
try { foo() } catch (ex) {}
try { foo() } catch (ex) {throw ex} finally {}
if (foo) {}
while (foo) {}
for (;foo;) {}
switch(foo) {}
switch (foo) { /* empty */ }
try {} catch (ex) {}
try { foo(); } catch (ex) {} finally {}
try {} catch (ex) {} finally {}
try { foo(); } catch (ex) {} finally {}
(function() { }())
var foo = () => {}
function foo() { }
function foo() {

}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
if (foo) { bar() }
while (foo) { bar() }
for (;foo;) { bar() }
try { foo() } catch (ex) { foo() }
switch(foo) {case 'foo': break;}
if (foo) {/* empty */}
while (foo) {/* empty */}
for (;foo;) {/* empty */}
try { foo() } catch (ex) {/* empty */}
try { foo() } catch (ex) {// empty
}
try { foo() } finally {// empty
}
try { foo() } finally {// test
}
try { foo() } finally {

    // hi i am off no use
}
try { foo() } catch (ex) {/* test111 */}
if (foo) { bar() } else { // nothing in me
}
if (foo) { bar() } else { /**/
}
if (foo) { bar() } else { //
}
function foo() {
  const test = {};
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
