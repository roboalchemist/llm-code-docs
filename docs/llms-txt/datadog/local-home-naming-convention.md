# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/local-home-naming-convention.md

---
title: Enforce using the LocalHome suffix for Session EJB
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce using the LocalHome suffix for Session EJB
---

# Enforce using the LocalHome suffix for Session EJB

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/local-home-naming-convention`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

When extending Session EJB, you should use `LocalHome` as a suffix.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public interface MissingProperSuffix extends javax.ejb.EJBLocalHome {}  // non-standard name

public class MissingProperSuffix extends javax.ejb.EJBLocalHome {}  // non-standard name
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public interface MyBeautifulLocalHome extends javax.ejb.EJBLocalHome {}

public class MyBeautifulLocalHome extends javax.ejb.EJBLocalHome {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 