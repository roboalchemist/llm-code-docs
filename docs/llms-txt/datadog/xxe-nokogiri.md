# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/xxe-nokogiri.md

---
title: Avoid XXE vulnerabilities
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid XXE vulnerabilities
---

# Avoid XXE vulnerabilities

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `ruby-security/xxe-nokogiri`

**Language:** Ruby

**Severity:** Warning

**Category:** Security

**CWE**: [611](https://cwe.mitre.org/data/definitions/611.html)

## Description{% #description %}

This rule addresses the prevention of XML External Entity (XXE) with the Nokogiri library.

To avoid XXE vulnerabilities, developers should disable the processing of external entities and external DTDs when parsing XML. In Ruby, when using the Nokogiri library, this can be achieved by configuring the parser with `cfg.strict.nonet` and removing any external subsets from the document.

A secure approach involves parsing XML with a block that sets these options, for example: `doc = Nokogiri::XML(params[:xml]) do |cfg| cfg.strict.nonet end` followed by `doc.remove_external_subset`. This ensures that external resources are not loaded or processed, mitigating the risk of XXE attacks. Adopting these practices helps maintain the confidentiality and integrity of your application's data.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```ruby
doc = Nokogiri::XML(params[:xml]) # can fetch file:/// or http://â¦
val = doc.at("//token").text
```

## Compliant Code Examples{% #compliant-code-examples %}

```ruby
doc = Nokogiri::XML(params[:xml]) do |cfg|
  cfg.strict.nonet
end
doc.remove_external_subset
doc.xpath("//token").text
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 