# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/extends-object.md

---
title: Avoid unnecessary object extend
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unnecessary object extend
---

# Avoid unnecessary object extend

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/extends-object`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

A class implicitly extends `Object`. As a result, there is no need to extend it.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo extends Object {} // no need to extend Object
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
