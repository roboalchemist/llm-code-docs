# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/generics-naming.md

---
title: Enforce generic naming standards
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce generic naming standards
---

# Enforce generic naming standards

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/generics-naming`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Generic values should not contain more than a single uppercase letter.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
// 'e' is lowercased
public interface GenericFoo<e extends BaseBar, K extends Serializable> {}

// 'EF' is two characters.
public interface GenericFoo<EF extends BaseBar, K extends Serializable> {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public interface GenericFoo<E extends BaseBar, K extends Serializable> extends BaseFoo {
    // This is ok...
}

public interface GenericFoo<E extends BaseBar, K extends Serializable> {
    // Also this
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 