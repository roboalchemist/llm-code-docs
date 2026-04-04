# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-express/external-filename-upload.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-express/external-filename-upload.md

---
title: Avoid using unsanitized user input with sendFile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using unsanitized user input with sendFile
---

# Avoid using unsanitized user input with sendFile

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-express/external-filename-upload`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [73](https://cwe.mitre.org/data/definitions/73.html)

## Description{% #description %}

Using unsanitized user input in a `sendFile` method can allow attackers to access unintended resources.

Set the `root` option directly in your `sendFile` options will make this rule not report a violation.

#### Learn More{% #learn-more %}

- [Express sendFile API reference](http://expressjs.com/en/5x/api.html#res.sendFile)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
app.post("/upload", (req, res) => {
    res.sendFile(req.params.filename)

    // options passed, but no root set
    res.sendFile(req.params.filename, { maxAge: 0 })

    // options passed, but no root set, and a callback is set
    res.sendFile(req.params.filename, { maxAge: 0 }, (err) => console.log(err))
})
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
app.post("/upload", (req, res) => {
    res.sendFile("foo")

    const options = { maxAge: 0, root: path.join(__dirname, "upload") }

    // options with root set
    res.sendFile(req.params.filename, options)
    res.sendFile(req.params.filename, { maxAge: 0, root: path.join(__dirname, "upload") })

    // options with root set (and a callback is set)
    res.sendFile(req.params.filename, options, (err) => console.log(err))
    res.sendFile(req.params.filename, { maxAge: 0, root: path.join(__dirname, "upload") }, (err) => console.log(err))
})
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
