# Source: https://developers.cloudflare.com/firewall/llms.txt

# Firewall Rules (deprecated)

Create rules that examine incoming HTTP traffic against a set of powerful filters to block, challenge, log, or allow matching requests. Firewall Rules have been replaced with WAF custom rules.

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/firewall/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [Firewall Rules (deprecated) llms-full.txt](https://developers.cloudflare.com/firewall/llms-full.txt) for the complete Firewall Rules (deprecated) documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare Firewall Rules](https://developers.cloudflare.com/firewall/index.md)

## About

- [About](https://developers.cloudflare.com/firewall/cf-firewall-rules/index.md)
- [Firewall rules actions](https://developers.cloudflare.com/firewall/cf-firewall-rules/actions/index.md)
- [Order and priority](https://developers.cloudflare.com/firewall/cf-firewall-rules/order-priority/index.md)

## Manage rules in the dashboard

- [Manage rules in the dashboard](https://developers.cloudflare.com/firewall/cf-dashboard/index.md)
- [Create, edit, and delete rules](https://developers.cloudflare.com/firewall/cf-dashboard/create-edit-delete-rules/index.md)
- [Create a mTLS rule](https://developers.cloudflare.com/firewall/cf-dashboard/create-mtls-rule/index.md)
- [Preview rules](https://developers.cloudflare.com/firewall/cf-dashboard/rule-preview/index.md)

## Manage rules via the APIs

- [Manage rules via the APIs](https://developers.cloudflare.com/firewall/api/index.md)
- [Call sequence](https://developers.cloudflare.com/firewall/api/call-sequence/index.md)
- [Cloudflare Filters API](https://developers.cloudflare.com/firewall/api/cf-filters/index.md)
- [DELETE examples](https://developers.cloudflare.com/firewall/api/cf-filters/delete/index.md)
- [Endpoints](https://developers.cloudflare.com/firewall/api/cf-filters/endpoints/index.md)
- [GET examples](https://developers.cloudflare.com/firewall/api/cf-filters/get/index.md)
- [JSON object](https://developers.cloudflare.com/firewall/api/cf-filters/json-object/index.md)
- [POST example](https://developers.cloudflare.com/firewall/api/cf-filters/post/index.md)
- [PUT examples](https://developers.cloudflare.com/firewall/api/cf-filters/put/index.md)
- [Expression validation](https://developers.cloudflare.com/firewall/api/cf-filters/validation/index.md)
- [What is a filter?](https://developers.cloudflare.com/firewall/api/cf-filters/what-is-a-filter/index.md): A filter is a way of setting up if (traffic matches certain criteria), then do something.
- [Firewall Rules API](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/index.md)
- [DELETE examples](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/delete/index.md)
- [Endpoints](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/endpoints/index.md)
- [GET examples](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/get/index.md)
- [JSON object](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/json-object/index.md)
- [POST example](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/post/index.md)
- [PUT examples](https://developers.cloudflare.com/firewall/api/cf-firewall-rules/put/index.md)

## troubleshooting

- [Required firewall rule changes to enable URL normalization](https://developers.cloudflare.com/firewall/troubleshooting/required-changes-to-enable-url-normalization/index.md)