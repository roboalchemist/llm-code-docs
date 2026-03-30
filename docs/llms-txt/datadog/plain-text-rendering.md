# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/rails-best-practices/plain-text-rendering.md

---
title: Prefer using render plain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using render plain
---

# Prefer using render plain

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `rails-best-practices/plain-text-rendering`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule enforces the use of `render plain:` syntax in Ruby on Rails applications instead of the `render text:` syntax. This is because `render text:` defaults to rendering the MIME type as `text/html`, which may not always be the desired outcome. On the other hand, `render plain:` explicitly renders the MIME type as `text/plain`.

By using `render plain:`, the developer is being explicit about the MIME type that is being rendered, which can prevent potential issues down the line. It is especially crucial when working with text that should not be interpreted as HTML.

To adhere to this rule, simply replace any instances of `render text:` with `render plain:`. If the content type needs to be specified, it can be done so directly within the `render plain:` call, e.g., `render plain: 'foo', content_type: 'text/plain'`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
# default MIME of `text/html`
render text: 'foo'

# can simplify with plain
render text: 'bar', content_type: 'text/plain'
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
render plain: 'foo'
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
