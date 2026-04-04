# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/package-case.md

---
title: Package names should not contain uppercase characters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Package names should not contain uppercase characters
---

# Package names should not contain uppercase characters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/package-case`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Package names should only contain lowercase characters.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
package com.fooCompany;  // should be lowercase name

public class Foo {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
package com.foocompany;

public class Foo {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
