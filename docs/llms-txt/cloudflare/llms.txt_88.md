# Source: https://developers.cloudflare.com/byoip/llms.txt

# BYOIP

Get Cloudflare's security and performance while using your own IPs

> Links below point directly to Markdown versions of each page. Any page can also be retrieved as Markdown by sending an `Accept: text/markdown` header to the page's URL without the `index.md` suffix (for example, `curl -H "Accept: text/markdown" https://developers.cloudflare.com/byoip/`).
>
> For other Cloudflare products, see the [Cloudflare documentation directory](https://developers.cloudflare.com/llms.txt).
>
> Use [BYOIP llms-full.txt](https://developers.cloudflare.com/byoip/llms-full.txt) for the complete BYOIP documentation in a single file, intended for offline indexing, bulk vectorization, or large-context models.

## Overview

- [Cloudflare BYOIP](https://developers.cloudflare.com/byoip/index.md): Get Cloudflare's security and performance while using your own IPs.

## Get started

- [Get started](https://developers.cloudflare.com/byoip/get-started/index.md)

## About address maps

- [About address maps](https://developers.cloudflare.com/byoip/address-maps/index.md)
- [Set up address maps](https://developers.cloudflare.com/byoip/address-maps/setup/index.md)

## IP address service bindings

- [IP address service bindings](https://developers.cloudflare.com/byoip/service-bindings/index.md): In IP address management, service binding refers to the association of IPs to specific Cloudflare services. Review the available options and the API endpoints to set up service bindings.
- [Use BYOIP with CDN and Spectrum](https://developers.cloudflare.com/byoip/service-bindings/cdn-and-spectrum/index.md): Cloudflare allows users to use their Cloudflare prefix to route traffic to a different service. Service bindings must be created on the parent account of the prefix.
- [Use BYOIP with Magic Transit and CDN](https://developers.cloudflare.com/byoip/service-bindings/magic-transit-with-cdn/index.md): Service bindings allow BYOIP customers to selectively route traffic on a per-IP address basis to the CDN pipeline. It is important to note that traffic routed to the CDN pipeline is protected at Layers 3 and 4 by the inherent DDoS protection capabilities.

## Route Leak Detection

- [Route Leak Detection](https://developers.cloudflare.com/byoip/route-leak-detection/index.md)

## Troubleshooting

- [Troubleshooting](https://developers.cloudflare.com/byoip/troubleshooting/index.md): Review common troubleshooting scenarios for BYOIP.
- [Troubleshoot prefix validation](https://developers.cloudflare.com/byoip/troubleshooting/prefix-validation/index.md)

## Glossary

- [Glossary](https://developers.cloudflare.com/byoip/glossary/index.md)

## Changelog

- [Changelog](https://developers.cloudflare.com/byoip/changelog/index.md)

## concepts

- [Dynamic advertisement](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/index.md)
- [Best practices](https://developers.cloudflare.com/byoip/concepts/dynamic-advertisement/best-practices/index.md)
- [Internet Routing Registry (IRR)](https://developers.cloudflare.com/byoip/concepts/irr-entries/index.md)
- [Manage IRR entries](https://developers.cloudflare.com/byoip/concepts/irr-entries/best-practices/index.md)
- [Letter of Agency](https://developers.cloudflare.com/byoip/concepts/loa/index.md)
- [Prefix delegations](https://developers.cloudflare.com/byoip/concepts/prefix-delegations/index.md)
- [Route filtering and RPKI](https://developers.cloudflare.com/byoip/concepts/route-filtering-rpki/index.md)
- [Static IPs](https://developers.cloudflare.com/byoip/concepts/static-ips/index.md)