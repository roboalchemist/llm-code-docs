# Source: https://developers.cloudflare.com/cloudflare-for-platforms/llms.txt

# Cloudflare for Platforms

Build your own multi-tenant platform using Cloudflare as infrastructure

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/cloudflare-for-platforms/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Cloudflare for Platforms llms-full.txt](https://developers.cloudflare.com/cloudflare-for-platforms/llms-full.txt) for the complete Cloudflare for Platforms documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/index.md)

## Workers for Platforms

- [Workers for Platforms](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/index.md)
- [Bindings](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/bindings/index.md)
- [Custom limits](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/index.md)
- [Dynamic dispatch Worker](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/dynamic-dispatch/index.md)
- [Hostname routing](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/hostname-routing/index.md): Learn how to route requests to the dispatch worker.
- [Observability](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/observability/index.md)
- [Outbound Workers](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/outbound-workers/index.md)
- [Static assets](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/static-assets/index.md): Host static assets on Cloudflare's global network and deliver faster load times worldwide with Workers for Platforms.
- [Tags](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/tags/index.md)
- [Get started](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/get-started/index.md)
- [How Workers for Platforms works](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/how-workers-for-platforms-works/index.md)
- [Platform Starter Kit](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/platform-templates/platform-starter-kit/index.md)
- [Deploy an AI vibe coding platform](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/platform-templates/vibesdk/index.md)
- [Limits](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/limits/index.md)
- [Local development](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/local-development/index.md)
- [User Worker metadata](https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/index.md)
- [API examples](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/platform-examples/index.md): REST API and TypeScript SDK examples for deploying Workers programmatically.
- [Pricing](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/pricing/index.md)
- [Worker Isolation](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/reference/worker-isolation/index.md)
- [WFP REST API](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/wfp-api/index.md)

## Cloudflare for SaaS

- [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/index.md)
- [API reference](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/api-reference/index.md)
- [Design guide](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/design-guide/index.md)
- [Custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/index.md)
- [Create custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/create-custom-hostnames/index.md): Learn how to create custom hostnames.
- [Custom metadata](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/index.md): Configure per-hostname settings such as URL rewriting and custom headers.
- [Hostname validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/index.md)
- [Backoff schedule](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/backoff-schedule/index.md)
- [Error codes](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/index.md)
- [Pre-validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/index.md)
- [Real-time validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/index.md)
- [Validation status](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/index.md)
- [Move hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/migrating-custom-hostnames/index.md): Learn how to move hostnames between different zones.
- [Remove custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/remove-custom-hostnames/index.md): Learn how to remove custom hostnames for inactive customers.
- [Analytics](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/hostname-analytics/index.md)
- [Performance](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/index.md)
- [Argo Smart Routing for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/argo-for-saas/index.md)
- [Cache for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/cache-for-saas/index.md)
- [Early Hints for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/early-hints-for-saas/index.md)
- [Plans](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/index.md): Learn what features and limits are part of various Cloudflare plans.
- [Certificate authorities](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/certificate-authorities/index.md)
- [Certificate statuses](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/certificate-statuses/index.md)
- [Connection request details](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/connection-details/index.md)
- [Domain control validation backoff schedule](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/dcv-validation-backoff/index.md)
- [Certificate and hostname priority](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/hostname-priority/index.md)
- [Custom CSRs](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/status-codes/custom-csrs/index.md)
- [Custom hostnames](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/status-codes/custom-hostnames/index.md)
- [Token validity periods](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/token-validity-periods/index.md)
- [Troubleshooting](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/troubleshooting/index.md)
- [Deprecation - Version 1](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/reference/versioning/index.md)
- [SaaS customers](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/index.md)
- [How it works](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/how-it-works/index.md)
- [Product compatibility](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/product-compatibility/index.md)
- [BigCommerce](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/bigcommerce/index.md): Learn how to configure your Enterprise zone with BigCommerce.
- [HubSpot](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/hubspot/index.md): Learn how to configure your zone with HubSpot.
- [Kinsta](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/kinsta/index.md): Learn how to configure your Enterprise zone with Kinsta.
- [Render](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/render/index.md): Learn how to configure your Enterprise zone with Render.
- [Salesforce Commerce Cloud](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/salesforce-commerce-cloud/index.md): Learn how to configure your Enterprise zone with Salesforce Commerce Cloud.
- [Shopify](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/shopify/index.md): Learn how to configure your zone with Shopify.
- [Webflow](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/webflow/index.md): Learn how to configure your Cloudflare zone with Webflow.
- [WP Engine](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/wpengine/index.md): Learn how to configure your zone with WP Engine.
- [Remove domain](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/remove-domain/index.md)
- [Security](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/index.md)
- [Certificate management](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/index.md)
- [Certificate statuses](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/certificate-statuses/index.md)
- [Custom certificates](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/index.md)
- [Certificate signing requests (CSRs)](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/certificate-signing-requests/index.md): Cloudflare for SaaS allows you to generate a Certificate Signing Request (CSR) A CSR contains information about your domain, common name, and Subject Alternative Names.
- [Manage custom certificates](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/custom-certificates/uploading-certificates/index.md): Learn how to manage custom certificates for your Cloudflare for SaaS custom hostnames.
- [TLS Management](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/enforce-mtls/index.md)
- [Issue](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/issue-certificates/index.md)
- [Renew](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/renew-certificates/index.md)
- [Validate](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/index.md): Learn which methods you should use to validate Cloudflare for SaaS certificates.
- [Delegated](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/delegated-dcv/index.md)
- [HTTP](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/http/index.md)
- [Troubleshooting](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/troubleshooting/index.md)
- [TXT](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/issue-and-validate/validate-certificates/txt/index.md)
- [Webhook definitions](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/webhook-definitions/index.md)
- [Secure with Cloudflare Access](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/secure-with-access/index.md)
- [WAF for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/index.md)
- [Managed rulesets](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/security/waf-for-saas/managed-rulesets/index.md)
- [Apex proxying](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/index.md)
- [Setup](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/setup/index.md)
- [Custom origin server](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/index.md)
- [Regional Services for SaaS](https://developers.cloudflare.com/data-localization/regional-services/get-started/index.md)
- [Workers as your fallback origin](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/index.md): Learn how to use a Worker as the fallback origin for your SaaS zone.
- [Common API Calls](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/common-api-calls/index.md)
- [Enable](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/enable/index.md)
- [Configuring Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/index.md): Get started with Cloudflare for SaaS