# Source: https://developers.cloudflare.com/cache/llms.txt

# Cache / CDN

Make websites faster by caching content across our global server network

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/cache/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Cache / CDN llms-full.txt](https://developers.cloudflare.com/cache/llms-full.txt) for the complete Cache / CDN documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Cache](https://developers.cloudflare.com/cache/index.md)

## Plans

- [Plans](https://developers.cloudflare.com/cache/plans/index.md)

## Get started

- [Get started](https://developers.cloudflare.com/cache/get-started/index.md)

## Changelog

- [Changelog](https://developers.cloudflare.com/cache/changelog/index.md)

## advanced-configuration

- [Cache Reserve](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/index.md)
- [Crawler Hints](https://developers.cloudflare.com/cache/advanced-configuration/crawler-hints/index.md)
- [Early Hints](https://developers.cloudflare.com/cache/advanced-configuration/early-hints/index.md)
- [Query String Sort](https://developers.cloudflare.com/cache/advanced-configuration/query-string-sort/index.md)
- [Serving tailored content with Cloudflare](https://developers.cloudflare.com/cache/advanced-configuration/serve-tailored-content/index.md)
- [Vary for images](https://developers.cloudflare.com/cache/advanced-configuration/vary-for-images/index.md)

## cache-security

- [Avoid web cache poisoning](https://developers.cloudflare.com/cache/cache-security/avoid-web-poisoning/index.md)
- [Cache Deception Armor](https://developers.cloudflare.com/cache/cache-security/cache-deception-armor/index.md)
- [Cross-Origin Resource Sharing (CORS)](https://developers.cloudflare.com/cache/cache-security/cors/index.md)

## concepts

- [Head Requests and Set-Cookie Headers](https://developers.cloudflare.com/cache/concepts/cache-behavior/index.md)
- [Origin Cache Control](https://developers.cloudflare.com/cache/concepts/cache-control/index.md)
- [Cloudflare cache responses](https://developers.cloudflare.com/cache/concepts/cache-responses/index.md)
- [CDN-Cache-Control](https://developers.cloudflare.com/cache/concepts/cdn-cache-control/index.md)
- [Customize cache](https://developers.cloudflare.com/cache/concepts/customize-cache/index.md)
- [Default cache behavior](https://developers.cloudflare.com/cache/concepts/default-cache-behavior/index.md)
- [Retention vs Freshness (TTL)](https://developers.cloudflare.com/cache/concepts/retention-vs-freshness/index.md)
- [Revalidation](https://developers.cloudflare.com/cache/concepts/revalidation/index.md)

## Glossary

- [Glossary](https://developers.cloudflare.com/cache/glossary/index.md)

## how-to

- [Always Online](https://developers.cloudflare.com/cache/how-to/always-online/index.md)
- [Cache keys](https://developers.cloudflare.com/cache/how-to/cache-keys/index.md)
- [Cache Response Rules](https://developers.cloudflare.com/cache/how-to/cache-response-rules/index.md)
- [Create a rule via API](https://developers.cloudflare.com/cache/how-to/cache-response-rules/create-api/index.md)
- [Create a rule in the dashboard](https://developers.cloudflare.com/cache/how-to/cache-response-rules/create-dashboard/index.md)
- [Available settings](https://developers.cloudflare.com/cache/how-to/cache-response-rules/settings/index.md)
- [Terraform example](https://developers.cloudflare.com/cache/how-to/cache-response-rules/terraform-example/index.md)
- [Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/index.md)
- [Create a rule via API](https://developers.cloudflare.com/cache/how-to/cache-rules/create-api/index.md)
- [Create a rule in the dashboard](https://developers.cloudflare.com/cache/how-to/cache-rules/create-dashboard/index.md)
- [Browser Cache TTL](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/browser-cache-ttl/index.md): Browser Cache TTL
- [Bypass Cache on Cookie](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/bypass-cache-on-cookie/index.md): Bypass Cache on Cookie
- [Cache Deception Armor](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-deception-armor/index.md): Cache Deception Armor
- [Cache by Device Type](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-device-type/index.md): Cache by Device Type
- [Cache Level (Cache Everything)](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything/index.md): Cache Level (Cache Everything)
- [Cache Everything while ignoring query strings](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-everything-ignore-query-strings/index.md): Cache Everything while ignoring query strings
- [Cache TTL by status code](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/cache-ttl-by-status-code/index.md): Cache TTL by status code
- [Custom Cache Key](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/custom-cache-key/index.md): Custom Cache Key
- [Edge Cache TTL](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/edge-ttl/index.md): Edge Cache TTL
- [Origin Cache Control](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/origin-cache-control/index.md): Origin Cache Control
- [Query String Sort](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/query-string-sort/index.md): Query String Sort
- [Respect Strong ETags](https://developers.cloudflare.com/cache/how-to/cache-rules/examples/respect-strong-etags/index.md): Respect Strong ETags
- [Order and priority](https://developers.cloudflare.com/cache/how-to/cache-rules/order/index.md)
- [Migration from Page Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/page-rules-migration/index.md)
- [Available settings](https://developers.cloudflare.com/cache/how-to/cache-rules/settings/index.md)
- [Terraform example](https://developers.cloudflare.com/cache/how-to/cache-rules/terraform-example/index.md)
- [Cache by status code](https://developers.cloudflare.com/cache/how-to/configure-cache-status-code/index.md)
- [Edge and Browser Cache TTL](https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/index.md)
- [Set Browser Cache TTL](https://developers.cloudflare.com/cache/how-to/edge-browser-cache-ttl/set-browser-ttl/index.md)
- [Purge cache](https://developers.cloudflare.com/cache/how-to/purge-cache/index.md)
- [âPurge cache by prefix (URL)](https://developers.cloudflare.com/cache/how-to/purge-cache/purge_by_prefix/index.md)
- [âPurge cache by hostname](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-hostname/index.md)
- [âPurge by single-file](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-single-file/index.md)
- [Purge cache by cache-tags](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-by-tags/index.md)
- [Purge cache key resources](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-cache-key/index.md)
- [âPurge everything](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-everything/index.md)
- [Pâurge varied images](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-varied-images/index.md)
- [Purge zone versions via API](https://developers.cloudflare.com/cache/how-to/purge-cache/purge-zone-versions/index.md)
- [Caching levels](https://developers.cloudflare.com/cache/how-to/set-caching-levels/index.md)
- [Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/index.md)

## interaction-cloudflare-products

- [Enable cache in an R2 bucket](https://developers.cloudflare.com/cache/interaction-cloudflare-products/r2/index.md)
- [Control cache access with WAF and Snippets](https://developers.cloudflare.com/cache/interaction-cloudflare-products/waf-snippets/index.md)
- [Customize cache behavior with Workers](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers/index.md)
- [How Workers interact with Cache Rules](https://developers.cloudflare.com/cache/interaction-cloudflare-products/workers-cache-rules/index.md)

## performance-review

- [Cache Analytics](https://developers.cloudflare.com/cache/performance-review/cache-analytics/index.md)
- [Cache performance](https://developers.cloudflare.com/cache/performance-review/cache-performance/index.md)

## reference

- [CDN Reference Architecture](https://developers.cloudflare.com/cache/reference/cdn-reference-architecture/index.md)
- [CSAM Scanning Tool](https://developers.cloudflare.com/cache/reference/csam-scanning/index.md)
- [Development Mode](https://developers.cloudflare.com/cache/reference/development-mode/index.md)
- [Using ETag Headers with Cloudflare](https://developers.cloudflare.com/cache/reference/etag-headers/index.md)

## troubleshooting

- [Always Online](https://developers.cloudflare.com/cache/troubleshooting/always-online/index.md)