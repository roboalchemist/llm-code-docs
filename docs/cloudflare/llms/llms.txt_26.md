# Source: https://developers.cloudflare.com/turnstile/llms.txt

# Turnstile

Turnstile is Cloudflare's smart CAPTCHA alternative

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/turnstile/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Turnstile llms-full.txt](https://developers.cloudflare.com/turnstile/llms-full.txt) for the complete Turnstile documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Turnstile](https://developers.cloudflare.com/turnstile/index.md)

## Plans

- [Plans](https://developers.cloudflare.com/turnstile/plans/index.md)

## Get started

- [Get started](https://developers.cloudflare.com/turnstile/get-started/index.md)
- [Embed the widget](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/index.md)
- [Widget configurations](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/widget-configurations/index.md)
- [Mobile implementation](https://developers.cloudflare.com/turnstile/get-started/mobile-implementation/index.md)
- [Validate the token](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/index.md)
- [Create and manage widgets using Cloudflare API](https://developers.cloudflare.com/turnstile/get-started/widget-management/api/index.md)
- [Create and manage widgets using the Cloudflare dashboard](https://developers.cloudflare.com/turnstile/get-started/widget-management/dashboard/index.md)
- [Create and manage widgets using Terraform](https://developers.cloudflare.com/turnstile/get-started/widget-management/terraform/index.md)

## Turnstile Analytics

- [Turnstile Analytics](https://developers.cloudflare.com/turnstile/turnstile-analytics/index.md): Use Turnstile Analytics to view the number of challenges issued, the challenge solve rate, and the metrics of issued challenges.
- [Challenge outcome](https://developers.cloudflare.com/turnstile/turnstile-analytics/challenge-outcomes/index.md)
- [Token validation](https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/index.md)

## Migration

- [Migration](https://developers.cloudflare.com/turnstile/migration/index.md)
- [Migrate from hCaptcha](https://developers.cloudflare.com/turnstile/migration/hcaptcha/index.md)
- [Migrate from reCAPTCHA](https://developers.cloudflare.com/turnstile/migration/recaptcha/index.md)

## Tutorials

- [Tutorials](https://developers.cloudflare.com/turnstile/tutorials/index.md)
- [Conditionally enforce Turnstile](https://developers.cloudflare.com/turnstile/tutorials/conditionally-enforcing-turnstile/index.md): This tutorial explains how to conditionally enforce Turnstile based on the incoming request, such as a pre-shared secret in a header or a specific IP address.
- [Exclude Turnstile from E2E tests](https://developers.cloudflare.com/turnstile/tutorials/excluding-turnstile-from-e2e-tests/index.md): This tutorial explains how to handle Turnstile in your end-to-end (E2E) tests by using Turnstile's dedicated testing keys.
- [Fraud detection with Ephemeral IDs](https://developers.cloudflare.com/turnstile/tutorials/fraud-detection-with-ephemeral-ids/index.md): Learn how to implement fraud detection using Turnstile's Ephemeral IDs to identify and block bad actors who rotate IP addresses.
- [Integrate Turnstile, WAF, & Bot Management](https://developers.cloudflare.com/turnstile/tutorials/integrating-turnstile-waf-and-bot-management/index.md): This tutorial will guide you on how to integrate Cloudflare Turnstile, Web Application Firewall (WAF), and Bot Management. This combination creates a robust defense against various threats, including automated attacks and malicious login attempts.
- [Protect your forms](https://developers.cloudflare.com/turnstile/tutorials/login-pages/index.md): This tutorial will guide you through integrating Cloudflare Turnstile to protect your web forms, such as login, signup, or contact forms.

## Community resources

- [Community resources](https://developers.cloudflare.com/turnstile/community-resources/index.md)

## Changelog

- [Changelog](https://developers.cloudflare.com/turnstile/changelog/index.md)

## additional-configuration

- [Ephemeral IDs](https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/index.md)
- [Hostname management](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/index.md)
- [Any Hostname (Enterprise only)](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/any-hostname/index.md)
- [Pre-clearance configuration](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/pre-clearance/index.md)
- [Remove Cloudflare branding with Offlabel](https://developers.cloudflare.com/turnstile/additional-configuration/offlabel/index.md)
- [Pre-clearance support](https://developers.cloudflare.com/turnstile/additional-configuration/pre-clearance-support/index.md)

## concepts

- [Cloudflare Challenges](https://developers.cloudflare.com/turnstile/concepts/challenges/index.md)
- [Turnstile widgets](https://developers.cloudflare.com/turnstile/concepts/widget/index.md)

## extensions

- [Implement Turnstile with Google Firebase](https://developers.cloudflare.com/turnstile/extensions/google-firebase/index.md)
- [Pages Plugin](https://developers.cloudflare.com/turnstile/extensions/pages-plugin/index.md)
- [Waiting Room Analytics](https://developers.cloudflare.com/turnstile/extensions/waiting-room/index.md)

## reference

- [Content Security Policy](https://developers.cloudflare.com/turnstile/reference/content-security-policy/index.md)
- [Supported browsers](https://developers.cloudflare.com/turnstile/reference/supported-browsers/index.md)
- [Supported languages](https://developers.cloudflare.com/turnstile/reference/supported-languages/index.md)
- [Turnstile Privacy Addendum](https://developers.cloudflare.com/turnstile/reference/turnstile-privacy-addendum/index.md)

## troubleshooting

- [Challenge solve issues](https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/index.md)
- [Client-side errors](https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/index.md)
- [Error codes](https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/error-codes/index.md)
- [Feedback reports](https://developers.cloudflare.com/turnstile/troubleshooting/feedback-reports/index.md)
- [Rotate secret key](https://developers.cloudflare.com/turnstile/troubleshooting/rotate-secret-key/index.md)
- [Test your Turnstile implementation](https://developers.cloudflare.com/turnstile/troubleshooting/testing/index.md)