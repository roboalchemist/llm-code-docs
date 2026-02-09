# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-browser-security/react-dangerously-inner-html.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-browser-security/react-dangerously-inner-html.md

---
title: Do not inject unsanitized HTML
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not inject unsanitized HTML
---

# Do not inject unsanitized HTML

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `javascript-browser-security/react-dangerously-inner-html`

**Language:** JavaScript

**Severity:** Warning

**Category:** Security

**CWE**: [79](https://cwe.mitre.org/data/definitions/79.html)

## Description{% #description %}

Always sanitize HTML data before injecting it in the DOM. Use libraries such as [DOMPurify](https://github.com/cure53/DOMPurify) before using it.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```javascript
const App = () => {
  const data = `lorem <b onmouseover="alert('mouseover');">ipsum</b>`;
  const otherData = `<img src=x onerror=alert('xss') />`;

  return (
    <div
      dangerouslySetInnerHTML={{__html: data}}
      foobar={{foo: bar}}
    >
    <div dangerouslySetInnerHTML={{__html: data + " " + otherData}} />
    </div>
  );
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```javascript
const App = () => {
  const data = `lorem <b onmouseover="alert('mouseover');">ipsum</b>`;

  return (
    <div
      dangerouslySetInnerHTML={{__html: sanitize(data)}}
    />
  );
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 