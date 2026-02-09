# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/external-resource.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/external-resource.md

---
title: Avoid rendering resource based on unsanitized user input
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid rendering resource based on unsanitized user input
---

# Avoid rendering resource based on unsanitized user input

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-express/external-resource`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [706](https://cwe.mitre.org/data/definitions/706.html)

## Description{% #description %}

Rendering resources based on unsanitized user input should be avoided. At a minimum, one should use a safelist to restrict the potential resources that are exposed.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
app.get("/", (req, res) => {
    res.render(req.body.path)
    res.render(req.cookies.path)
    res.render(req.headers.path)
    res.render(req.params.path)
    res.render(req.query.path)
})
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
app.get("/", (req, res) => {
    const path = req.body.path
    if (["posts", "pages"].includes(path)) {
        return res.render(`${path}/success`)
    }
    res.render("error-page")
})
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 