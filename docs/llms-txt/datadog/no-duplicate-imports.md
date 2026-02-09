# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-code-style/no-duplicate-imports.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-code-style/no-duplicate-imports.md

---
title: Avoid duplicate module imports
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid duplicate module imports
---

# Avoid duplicate module imports

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-code-style/no-duplicate-imports`

**Language:** JavaScript

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

Single imports are easier to read and maintain you can see everything being imported from a module in one line.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
import { merge } from 'module';
import something from 'another-module';
import { find } from 'module';

import something from 'something';
import { find } from 'something';
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
import { merge, find } from 'module';
import something from 'another-module';

// not mergeable
import { merge } from 'something';
import * as something from 'something';
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 