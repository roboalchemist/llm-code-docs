# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/tsx-react/tsx-no-target-blank.md

---
title: Prevent target="_blank" links from security risks
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent target="_blank" links from security risks
---

# Prevent target="_blank" links from security risks

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `tsx-react/tsx-no-target-blank`

**Language:** TypeScript

**Severity:** Warning

**Category:** Security

## Description{% #description %}

Using `target="_blank"` in an anchor (`<a>`) tag allows a link to be opened in a new browser tab or window. Without proper precautions, this can introduce a security vulnerability known as "tabnabbing." A malicious page opened in the new tab can manipulate the `window.opener` object, potentially redirecting the original page to a phishing site or other unwanted content, misleading users into revealing sensitive information.

## How to Remediate{% #how-to-remediate %}

To mitigate this risk, always include `rel="noopener noreferrer"` when using `target="_blank"`. The `noopener` value prevents the new browsing context from accessing the `window.opener` property, thus isolating it from the original page. The `noreferrer` value has a similar effect while also preventing the new page from seeing the referrer HTTP header. This ensures that opening external links in a new tab does not expose your users to potential phishing attacks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```typescript
var Hello = <a target='_blank' href="https://example.com/"></a>
var Hello = <a target={`_blank`} href={dynamicLink}></a>
var Nested = <Link target={'_blank'} href="https://example.com/" />
var Nested = <Link target="_blank" href="https://example.com/" />
```

## Compliant Code Examples{% #compliant-code-examples %}

```typescript
var Hello = <p target={"_blank"}></p>
var Hello = <p target={`_blank`}></p>
var Hello = <a target="_blank" rel="noreferrer" href="https://example.com"></a>
var Hello = <a target="_blank" rel="noopener noreferrer" href="https://example.com"></a>
var Hello = <a target="_blank" href="relative/path/in/the/host"></a>
var Hello = <a target="_blank" href="/absolute/path/in/the/host"></a>
var Hello = <a></a>
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
