# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-best-practices/for-direction.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-best-practices/for-direction.md

---
title: Check for loop is moving in the right direction
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Check for loop is moving in the right direction
---

# Check for loop is moving in the right direction

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-best-practices/for-direction`

**Language:** JavaScript

**Severity:** Error

**Category:** Best Practices

## Description{% #description %}

This rule prevents you from creating conditions in which a `for` loop might end up in an infinite loop. If you need an infinite loop, use `while` statements.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
// test if '++', '--'
for(var i = 0; i < 10; i--){}
for(var i = 0; i <= 10; i--){}
for(var i = 10; i > 10; i++){}
for(var i = 10; i >= 0; i++){}

// test if '+=', '-='
for(var i = 0; i < 10; i-=1){}
for(var i = 0; i <= 10; i-=1){}
for(var i = 10; i > 10; i+=1){}
for(var i = 10; i >= 0; i+=1){}
for(var i = 0; i < 10; i+=-1){}
for(var i = 0; i <= 10; i+=-1){}
for(var i = 10; i > 10; i-=-1){}
for(var i = 10; i >= 0; i-=-1){}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
// test if '++', '--'
for(var i = 0; i < 10; i++){}
for(var i = 0; i <= 10; i++){}
for(var i = 10; i > 0; i--){}
for(var i = 10; i >= 0; i--){}

// test if '+=', '-=',
for(var i = 0; i < 10; i+=1){}
for(var i = 0; i <= 10; i+=1){}
for(var i = 0; i < 10; i-=-1){}
for(var i = 0; i <= 10; i-=-1){}
for(var i = 10; i > 0; i-=1){}
for(var i = 10; i >= 0; i-=1){}
for(var i = 10; i > 0; i+=-1){}
for(var i = 10; i >= 0; i+=-1){}

// test if no update.
for(var i = 10; i > 0;){}
for(var i = 10; i >= 0;){}
for(var i = 10; i < 0;){}
for(var i = 10; i <= 0;){}
for(var i = 10; i <= 0; j++){}
for(var i = 10; i <= 0; j--){}
for(var i = 10; i >= 0; j++){}
for(var i = 10; i >= 0; j--){}
for(var i = 10; i >= 0; j += 2){}
for(var i = 10; i >= 0; j -= 2){}
for(var i = 10; i >= 0; i |= 2){}
for(var i = 10; i >= 0; i %= 2){}
for(var i = 0; i < MAX; i += STEP_SIZE);
for(var i = 0; i < MAX; i -= STEP_SIZE);
for(var i = 10; i > 0; i += STEP_SIZE);

// other cond-expressions.
for(var i = 0; i !== 10; i+=1){}
for(var i = 0; i === 10; i+=1){}
for(var i = 0; i == 10; i+=1){}
for(var i = 0; i != 10; i+=1){}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 