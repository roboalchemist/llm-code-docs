# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/rails-manual-template.md

---
title: Avoid manual template creation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid manual template creation
---

# Avoid manual template creation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/rails-manual-template`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

The rule 'Avoid manual template creation' is aimed at preventing the direct use of 'ERB.new' for creating new templates in Ruby. This is because manually creating templates can increase the risk of code injection attacks. An attacker could potentially inject malicious code into your templates, leading to significant security issues.

It's important to adhere to this rule because it promotes better security practices. By avoiding manual template creation, you reduce the potential attack surface for malicious actors. Additionally, manually creating templates can lead to messy and hard-to-maintain code, which can negatively impact the overall quality of your application.

Instead of manually creating templates, consider using Rails' built-in mechanisms for managing views and templates. For instance, you can use the 'render' method in your controller to render a view. Here's an example: `render 'template_name'`. This method automatically handles the loading and processing of ERB templates, making your code safer and cleaner.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
def scaffold_post_content
    ERB.new(File.read(File.expand_path(scaffold_path, site_template))).result
end
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 