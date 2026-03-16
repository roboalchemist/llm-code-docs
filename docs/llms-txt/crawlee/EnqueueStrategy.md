# Source: https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md

# EnqueueStrategy<!-- -->

The different enqueueing strategies available.

Depending on the strategy you select, we will only check certain parts of the URLs found. Here is a diagram of each URL part and their name:

```
Protocol          Domain
┌────┐          ┌─────────┐
https://example.crawlee.dev/...
│       └─────────────────┤
│             Hostname    │
│                         │
└─────────────────────────┘
         Origin
```

* The `Protocol` is usually `http` or `https`
* The `Domain` represents the path without any possible subdomains to a website. For example, `crawlee.dev` is the domain of `https://example.crawlee.dev/`
* The `Hostname` is the full path to a website, including any subdomains. For example, `example.crawlee.dev` is the hostname of `https://example.crawlee.dev/`
* The `Origin` is the combination of the `Protocol` and `Hostname`. For example, `https://example.crawlee.dev` is the origin of `https://example.crawlee.dev/`

## Index[**](#Index)

### Enumeration Members

* [**All](#All)
* [**SameDomain](#SameDomain)
* [**SameHostname](#SameHostname)
* [**SameOrigin](#SameOrigin)

## Enumeration Members<!-- -->[**](<#Enumeration Members>)

### [**](#All)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L220)All

**All: all

Matches any URLs found

### [**](#SameDomain)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L238)SameDomain

**SameDomain: same-domain

Matches any URLs that have the same domain as the base URL. For example, `https://wow.an.example.com` and `https://example.com` will both be matched for a base url of `https://example.com`.

> This strategy will match both `http` and `https` protocols regardless of the base URL protocol.

### [**](#SameHostname)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L229)SameHostname

**SameHostname: same-hostname

Matches any URLs that have the same hostname. For example, `https://wow.example.com/hello` will be matched for a base url of `https://wow.example.com/`, but `https://example.com/hello` will not be matched.

> This strategy will match both `http` and `https` protocols regardless of the base URL protocol.

### [**](#SameOrigin)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L247)SameOrigin

**SameOrigin: same-origin

Matches any URLs that have the same hostname and protocol. For example, `https://wow.example.com/hello` will be matched for a base url of `https://wow.example.com/`, but `http://wow.example.com/hello` will not be matched.

> This strategy will ensure the protocol of the base URL is the same as the protocol of the URL to be enqueued.
