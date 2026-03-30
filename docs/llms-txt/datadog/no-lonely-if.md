# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-lonely-if.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-lonely-if.md

---
title: Avoid if statements as the only statement in else blocks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid if statements as the only statement in else blocks
---

# Avoid if statements as the only statement in else blocks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-lonely-if`

**Language:** JavaScript

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Prefers `else if` statement instead of an lonely `if` statement. Using `else if` statements` is a cleaner code practice.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
if (a) {;} else { if (b) {;} }

if (a) {
  foo();
} else {
  if (b) {
    bar();
  }
}

if (a) {
  foo();
} else /* comment */ {
  if (b) {
    bar();
  }
}


if (a) {
  foo();
} else {
  /* otherwise, do the other thing */ if (b) {
    bar();
  }
}

if (a) {
  foo();
} else {
  if /* this comment is ok */ (b) {
    bar();
  }
}

if (a) {
  foo();
} else {
  if (b) {
    bar();
  } /* this comment will prevent this test case from being autofixed. */
}
if (foo) {} else { if (bar) baz(); }

// Not fixed; removing the braces would cause a SyntaxError.
if (foo) {} else { if (bar) baz() } qux();

// This is fixed because there is a semicolon after baz().
if (foo) {} else { if (bar) baz(); } qux();

// Not fixed; removing the braces would change the semantics due to ASI.
if (foo) {
} else {
  if (bar) baz()
}
[1, 2, 3].forEach(foo);

// Not fixed; removing the braces would change the semantics due to ASI.
if (foo) {
} else {
    if (bar) baz++
}
foo;

// This is fixed because there is a semicolon after baz++
if (foo) {
} else {
  if (bar) baz++;
}
foo;

// Not fixed; bar() would be interpreted as a template literal tag
if (a) {
  foo();
} else {
  if (b) bar()
}
`template literal`;

if (a) {
  foo();
} else {
  if (b) {
    bar();
  } else if (c) {
    baz();
  } else {
    qux();
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
if (a) {;} else if (b) {;}
if (a) {;} else { if (b) {;} ; }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
