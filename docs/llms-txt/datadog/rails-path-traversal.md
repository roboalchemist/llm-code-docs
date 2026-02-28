# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/rails-path-traversal.md

---
title: Avoid path traversal for Ruby on Rails applications
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid path traversal for Ruby on Rails applications
---

# Avoid path traversal for Ruby on Rails applications

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/rails-path-traversal`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [35](https://cwe.mitre.org/data/definitions/35.html)

## Description{% #description %}

This rule aims to prevent path traversal vulnerabilities in Ruby on Rails applications. Path traversal occurs when user input is used to construct file paths without proper validation, allowing attackers to access sensitive files outside the intended directories. This can lead to unauthorized disclosure of system files, application source code, or configuration data.

It is crucial to avoid directly incorporating user-controlled parameters into file paths, especially when using methods like `render file:` or `send_file`. Attackers can manipulate these inputs to traverse directories using sequences like `../`, potentially exposing critical files. Such vulnerabilities can compromise the security and integrity of your application and underlying system.

To mitigate this risk, developers should avoid interpolating user input into file paths. Instead, use safer alternatives such as `render template:` with fixed or validated template names. If dynamic file access is necessary, ensure strict validation and sanitization of input parameters, or constrain access to a predefined whitelist of acceptable files. Following these practices helps maintain the application's security posture against path traversal attacks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def myfunction
    base = Rails.root.join("public/docs")
    requested = base.join(params[:path].to_s).cleanpath
    send_file requested, disposition: "inline"
end
```

```ruby
def myfunction
    # e.g. params[:page] = "../../etc/passwd"
    render file: Rails.root.join("app/views/pages", "#{params[:page]}.html.erb")
end
```

```ruby
# e.g. params[:page] = "../../etc/passwd"
render file: Rails.root.join("app/views/pages", "#{params[:page]}.html.erb")
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
module MyModule
  class User < BaseController
    def create
      # fetch from database, we assume the data is safe
      viewer = func(User.find(params[:user_id]))

      render json: {
        viewer_added: viewer.present?
      }
    end
  end
end
```

```ruby
render template: "pages/otherpage"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
