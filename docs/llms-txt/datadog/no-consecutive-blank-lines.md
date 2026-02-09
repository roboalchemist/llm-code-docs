# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/no-consecutive-blank-lines.md

---
title: Enforce consistent newline usage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce consistent newline usage
---

# Enforce consistent newline usage

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/no-consecutive-blank-lines`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Code is more consistent and readable when there are not a variable number of consecutive newlines.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
package com.datadog.appsec;


import com.datadog.appsec.event.data.Address;
import java.util.Collection;




public interface AppSecModule { }
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
package com.datadog.appsec;

import com.datadog.appsec.event.data.Address;
import java.util.Collection;


////////////////////////////////////
// Newlines between comments are ok
////////////////////////////////////


public interface AppSecModule { }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 