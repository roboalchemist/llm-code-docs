# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/rails-send-file.md

---
title: Avoid sending files without sanitizing user input
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid sending files without sanitizing user input
---

# Avoid sending files without sanitizing user input

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/rails-send-file`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

## Description{% #description %}

This rule warns against sending files using user input directly without proper sanitization. When user input is incorporated into file paths without validation, it can lead to directory traversal attacks or unauthorized file access, potentially exposing sensitive data or compromising the system.

Ensuring that any user-supplied filename or path is sanitized or validated before being passed to methods like `send_file` is crucial. This can be done by whitelisting allowed filenames, restricting input to a predefined set of values, or explicitly constructing file paths without directly interpolating user input.

To avoid triggering this rule, developers should avoid passing raw parameters from user input into file paths. Instead, use fixed paths or sanitize inputs like `params['filename']` before usage, for example: `send_file("#{Rails.root}/foo.bar")` or by validating that the filename exists within an expected directory. This reduces the risk of serving unintended files and enhances the security of file delivery in the application.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def download_image
  path = "#{Rails.root}/#{params['filename']}"
  send_file(path)
end
```

```ruby
def download_image
  send_file("#{Rails.root}/#{params['filename']}")
end
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
def download_image
  path2 = "#{Rails.root}/#{params['filename']}"
  path = "#{Rails.root}/foo.bar"
  send_file(path)
end
```

```ruby
def download_image
  send_file("#{Rails.root}/public/images/image.jpg", type: "image/jpeg", disposition: "inline")
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
