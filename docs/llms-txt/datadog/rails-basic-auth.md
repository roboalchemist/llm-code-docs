# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/rails-basic-auth.md

---
title: Avoid hardcoded basic auth with rails
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid hardcoded basic auth with rails
---

# Avoid hardcoded basic auth with rails

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/rails-basic-auth`

**Language:** Ruby

**Severity:** Info

**Category:** Security

**CWE**: [798](https://cwe.mitre.org/data/definitions/798.html)

## Description{% #description %}

This rule advises against hardcoding basic authentication credentials directly in your Rails application. Hardcoded credentials pose a significant security risk as they can easily be exposed unintentionally, leading to unauthorized access to sensitive data or systems.

It is important to adhere to this rule because it promotes good security practices. By avoiding hardcoded credentials, you reduce the potential for security breaches and ensure that your application's authentication mechanisms are robust and secure.

To avoid violating this rule, store your basic authentication credentials in a secure and encrypted format, such as environment variables or a secure credentials storage system. For instance, instead of hardcoding the password directly in the `http_basic_authenticate_with` method, you can fetch it from an environment variable like this: `http_basic_authenticate_with :name => "dhh", :password => ENV['SECRET_PASSWORD'], :except => :index`. This way, the actual password is not exposed in the code and can be securely managed outside of the application.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
class PostsController < ApplicationController
  http_basic_authenticate_with :name => "dhh", :password => "secret", :except => :index
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
class PostsController < ApplicationController
  http_basic_authenticate_with :name => "dhh", :password => secret, :except => :index
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 