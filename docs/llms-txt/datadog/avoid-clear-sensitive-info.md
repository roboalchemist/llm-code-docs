# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/avoid-clear-sensitive-info.md

---
title: Avoid storing sensitive info
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid storing sensitive info
---

# Avoid storing sensitive info

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/avoid-clear-sensitive-info`

**Language:** Ruby

**Severity:** Notice

**Category:** Security

## Description{% #description %}

This rule highlights the importance of avoiding the storage of sensitive information, such as passwords, directly within objects or attributes. Storing sensitive data insecurely can lead to accidental exposure, especially if the data is logged, serialized, or accessed without proper safeguards.

Sensitive information often requires special handling, including encryption, secure storage mechanisms, or avoiding retention altogether. By not storing sensitive data in plain attributes, you reduce the risk of leaks and improve the overall security posture of your application.

To comply with this rule, avoid defining attribute accessors for sensitive fields like passwords. Instead, consider using secure authentication libraries or mechanisms that handle sensitive data safely. For example, store only hashed versions of passwords or use dedicated services for authentication rather than raw password storage in objects.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class User
  attr_accessor :name
  attr_accessor :password

  def initialize(name, password)
    self.name = name
    self.password = password
  end

  def update_name(new_password)
    self.password = new_password
  end
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class User
  attr_accessor :name

  def initialize(name)
    self.name = name  # using self to call the setter method
  end

  def update_name(new_name)
    self.name = new_name  # also uses the setter method
  end
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
