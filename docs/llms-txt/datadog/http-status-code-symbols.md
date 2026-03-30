# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/rails-best-practices/http-status-code-symbols.md

---
title: Prefer using HTTP status code symbols
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer using HTTP status code symbols
---

# Prefer using HTTP status code symbols

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `rails-best-practices/http-status-code-symbols`

**Language:** Ruby

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule encourages the use of symbolic representations of HTTP status codes over their numeric counterparts, making the code more self-explanatory and easier to understand. Numeric HTTP status codes can be cryptic and hard to remember, especially for developers who are not familiar with them.

To adhere to this rule, simply replace the numeric HTTP status code with its symbolic equivalent in your code. For example, instead of using `403` for a forbidden request, use `:forbidden`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class ApplicationController < ActionController::Base
  def access_denied
    render status: 403 # Avoid using numeric HTTP status code
  end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class ApplicationController < ActionController::Base
  def access_denied
    render status: :forbidden
  end
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
