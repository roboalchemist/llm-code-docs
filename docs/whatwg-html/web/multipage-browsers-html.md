# Source: https://html.spec.whatwg.org/multipage/browsers.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/browsers.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 6.12 The popover attribute](https://html.spec.whatwg.org/multipage/popover.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [7.2 APIs related to navigation and session history →](https://html.spec.whatwg.org/multipage/nav-history-apis.html)
1.   [7 Loading web pages](https://html.spec.whatwg.org/multipage/browsers.html#browsers)
    1.   [7.1 Supporting concepts](https://html.spec.whatwg.org/multipage/browsers.html#loading-web-pages-supporting-concepts)
        1.   [7.1.1 Origins](https://html.spec.whatwg.org/multipage/browsers.html#origin)
            1.   [7.1.1.1 Sites](https://html.spec.whatwg.org/multipage/browsers.html#sites)
            2.   [7.1.1.2 Relaxing the same-origin restriction](https://html.spec.whatwg.org/multipage/browsers.html#relaxing-the-same-origin-restriction)
            3.   [7.1.1.3 The `Origin` interface](https://html.spec.whatwg.org/multipage/browsers.html#the-origin-interface)

        2.   [7.1.2 Origin-keyed agent clusters](https://html.spec.whatwg.org/multipage/browsers.html#origin-keyed-agent-clusters)
        3.   [7.1.3 Cross-origin opener policies](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policies)
            1.   [7.1.3.1 The headers](https://html.spec.whatwg.org/multipage/browsers.html#the-coop-headers)
            2.   [7.1.3.2 Browsing context group switches due to opener policy](https://html.spec.whatwg.org/multipage/browsers.html#browsing-context-group-switches-due-to-cross-origin-opener-policy)
            3.   [7.1.3.3 Reporting](https://html.spec.whatwg.org/multipage/browsers.html#coop-reporting)

        4.   [7.1.4 Cross-origin embedder policies](https://html.spec.whatwg.org/multipage/browsers.html#coep)
            1.   [7.1.4.1 The headers](https://html.spec.whatwg.org/multipage/browsers.html#the-coep-headers)
            2.   [7.1.4.2 Embedder policy checks](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-checks)

        5.   [7.1.5 Sandboxing](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing)
        6.   [7.1.6`iframe` element referrer policy](https://html.spec.whatwg.org/multipage/browsers.html#iframe-element-referrer-policy)
        7.   [7.1.7 Policy containers](https://html.spec.whatwg.org/multipage/browsers.html#policy-containers)

7 Loading web pages[](https://html.spec.whatwg.org/multipage/browsers.html#browsers)
------------------------------------------------------------------------------------

This section describes features that apply most directly to web browsers. Having said that, except where specified otherwise, the requirements defined in this section _do_ apply to all user agents, whether they are web browsers or not.

### 7.1 Supporting concepts[](https://html.spec.whatwg.org/multipage/browsers.html#loading-web-pages-supporting-concepts)

#### 7.1.1 Origins[](https://html.spec.whatwg.org/multipage/browsers.html#origin)

Origins are the fundamental currency of the web's security model. Two actors in the web platform that share an origin are assumed to trust each other and to have the same authority. Actors with differing origins are considered potentially hostile versus each other, and are isolated from each other to varying degrees.

For example, if Example Bank's web site, hosted at `bank.example.com`, tries to examine the DOM of Example Charity's web site, hosted at `charity.example.org`, a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException` will be raised.

* * *

An origin is one of the following:

An opaque origin
An internal value, with no serialization it can be recreated from (it is serialized as "`null`" per [serialization of an origin](https://html.spec.whatwg.org/multipage/browsers.html#ascii-serialisation-of-an-origin)), for which the only meaningful operation is testing for equality.

A tuple origin
A [tuple](https://infra.spec.whatwg.org/#tuple) consisting of:

*   A scheme (an [ASCII string](https://infra.spec.whatwg.org/#ascii-string)).
*   A host (a [host](https://url.spec.whatwg.org/#concept-host)).
*   A port (null or a 16-bit unsigned integer).
*   A domain (null or a [domain](https://url.spec.whatwg.org/#concept-domain)). Null unless stated otherwise.

[Origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) can be shared, e.g., among multiple `Document` objects. Furthermore, [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) are generally immutable. Only the [domain](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-domain) of a [tuple origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-tuple) can be changed, and only through the `document.domain` API.

The effective domain of an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)origin is computed as follows:

1.   If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return null.

2.   If origin's [domain](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-domain) is non-null, then return origin's [domain](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-domain).

3.   Return origin's [host](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-host).

The serialization of an origin is the string obtained by applying the following algorithm to the given [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)origin:

1.   If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return "`null`".

2.   Otherwise, let result be origin's [scheme](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-scheme).

3.   Append "`://`" to result.

4.   Append origin's [host](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-host), [serialized](https://url.spec.whatwg.org/#concept-host-serializer), to result.

5.   If origin's [port](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-port) is non-null, append a U+003A COLON character (:), and origin's [port](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-port), [serialized](https://url.spec.whatwg.org/#serialize-an-integer), to result.

6.   Return result.

The [serialization](https://html.spec.whatwg.org/multipage/browsers.html#ascii-serialisation-of-an-origin) of ("`https`", "`xn--maraa-rta.example`", null, null) is "`https://xn--maraa-rta.example`".

[](https://html.spec.whatwg.org/multipage/browsers.html#unicode-serialisation-of-an-origin)There used to also be a _Unicode serialization of an origin_. However, it was never widely adopted.

* * *

Two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin), A and B, are said to be same origin if the following algorithm returns true:

1.   If A and B are the same [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return true.

2.   If A and B are both [tuple origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-tuple) and their [schemes](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-scheme), [hosts](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-host), and [port](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-port) are identical, then return true.

3.   Return false.

Two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin), A and B, are said to be same origin-domain if the following algorithm returns true:

1.   If A and B are the same [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return true.

2.   If A and B are both [tuple origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-tuple):

    1.   If A and B's [schemes](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-scheme) are identical, and their [domains](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-domain) are identical and non-null, then return true.

    2.   Otherwise, if A and B are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) and their [domains](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-domain) are both null, return true.

3.   Return false.

| A | B | [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) | [same origin-domain](https://html.spec.whatwg.org/multipage/browsers.html#same-origin-domain) |
| --- | --- | --- | --- |
| ("`https`", "`example.org`", null, null) | ("`https`", "`example.org`", null, null) | ✅ | ✅ |
| ("`https`", "`example.org`", 314, null) | ("`https`", "`example.org`", 420, null) | ❌ | ❌ |
| ("`https`", "`example.org`", 314, "`example.org`") | ("`https`", "`example.org`", 420, "`example.org`") | ❌ | ✅ |
| ("`https`", "`example.org`", null, null) | ("`https`", "`example.org`", null, "`example.org`") | ✅ | ❌ |
| ("`https`", "`example.org`", null, "`example.org`") | ("`http`", "`example.org`", null, "`example.org`") | ❌ | ❌ |

##### 7.1.1.1 Sites[](https://html.spec.whatwg.org/multipage/browsers.html#sites)

A scheme-and-host is a [tuple](https://infra.spec.whatwg.org/#tuple) of a scheme (an [ASCII string](https://infra.spec.whatwg.org/#ascii-string)) and a host (a [host](https://url.spec.whatwg.org/#concept-host)).

A site is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque) or a [scheme-and-host](https://html.spec.whatwg.org/multipage/browsers.html#scheme-and-host).

To obtain a site, given an origin origin, run these steps:

1.   If origin is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return origin.

2.   If origin's [host](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-host)'s [registrable domain](https://url.spec.whatwg.org/#host-registrable-domain) is null, then return (origin's [scheme](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-scheme), origin's [host](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-host)).

3.   Return (origin's [scheme](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-scheme), origin's [host](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-host)'s [registrable domain](https://url.spec.whatwg.org/#host-registrable-domain)).

Two [sites](https://html.spec.whatwg.org/multipage/browsers.html#site), A and B, are said to be same site if the following algorithm returns true:

1.   If A and B are the same [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return true.

2.   If A or B is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return false.

3.   If A's and B's [scheme](https://html.spec.whatwg.org/multipage/browsers.html#concept-scheme-and-host-scheme) values are different, then return false.

4.   If A's and B's [host](https://html.spec.whatwg.org/multipage/browsers.html#concept-scheme-and-host-host) values are not [equal](https://url.spec.whatwg.org/#concept-host-equals), then return false.

5.   Return true.

The serialization of a site is the string obtained by applying the following algorithm to the given [site](https://html.spec.whatwg.org/multipage/browsers.html#site)site:

1.   If site is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return "`null`".

2.   Let result be site[0].

3.   Append "`://`" to result.

4.   Append site[1], [serialized](https://url.spec.whatwg.org/#concept-host-serializer), to result.

5.   Return result.

It needs to be clear from context that the serialized value is a site, not an origin, as there is not necessarily a syntactic difference between the two. For example, the origin ("`https`", "`shop.example`", null, null) and the site ("`https`", "`shop.example`") have the same serialization: "`https://shop.example`".

Two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin), A and B, are said to be schemelessly same site if the following algorithm returns true:

1.   If A and B are the same [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), then return true.

2.   If A and B are both [tuple origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-tuple), then:

    1.   Let hostA be A's [host](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-host), and let hostB be B's [host](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-host).

    2.   If hostA[equals](https://url.spec.whatwg.org/#concept-host-equals)hostB and hostA's [registrable domain](https://url.spec.whatwg.org/#host-registrable-domain) is null, then return true.

    3.   If hostA's [registrable domain](https://url.spec.whatwg.org/#host-registrable-domain)[equals](https://url.spec.whatwg.org/#concept-host-equals)hostB's [registrable domain](https://url.spec.whatwg.org/#host-registrable-domain) and is non-null, then return true.

3.   Return false.

Two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin), A and B, are said to be same site if the following algorithm returns true:

1.   Let siteA be the result of [obtaining a site](https://html.spec.whatwg.org/multipage/browsers.html#obtain-a-site) given A.

2.   Let siteB be the result of [obtaining a site](https://html.spec.whatwg.org/multipage/browsers.html#obtain-a-site) given B.

3.   If siteA is [same site](https://html.spec.whatwg.org/multipage/browsers.html#concept-site-same-site) with siteB, then return true.

4.   Return false.

Unlike the [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) and [same origin-domain](https://html.spec.whatwg.org/multipage/browsers.html#same-origin-domain) concepts, for [schemelessly same site](https://html.spec.whatwg.org/multipage/browsers.html#schemelessly-same-site) and [same site](https://html.spec.whatwg.org/multipage/browsers.html#same-site), the [port](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-port) and [domain](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-domain) components are ignored.

For the reasons [explained in URL](https://url.spec.whatwg.org/#warning-avoid-psl), the [same site](https://html.spec.whatwg.org/multipage/browsers.html#same-site) and [schemelessly same site](https://html.spec.whatwg.org/multipage/browsers.html#schemelessly-same-site) concepts should be avoided when possible, in favor of [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) checks.

Given that `wildlife.museum`, `museum`, and `com` are [public suffixes](https://url.spec.whatwg.org/#host-public-suffix) and that `example.com` is not:

| A | B | [schemelessly same site](https://html.spec.whatwg.org/multipage/browsers.html#schemelessly-same-site) | [same site](https://html.spec.whatwg.org/multipage/browsers.html#same-site) |
| --- | --- | --- | --- |
| ("`https`", "`example.com`") | ("`https`", "`sub.example.com`") | ✅ | ✅ |
| ("`https`", "`example.com`") | ("`https`", "`sub.other.example.com`") | ✅ | ✅ |
| ("`https`", "`example.com`") | ("`http`", "`non-secure.example.com`") | ✅ | ❌ |
| ("`https`", "`r.wildlife.museum`") | ("`https`", "`sub.r.wildlife.museum`") | ✅ | ✅ |
| ("`https`", "`r.wildlife.museum`") | ("`https`", "`sub.other.r.wildlife.museum`") | ✅ | ✅ |
| ("`https`", "`r.wildlife.museum`") | ("`https`", "`other.wildlife.museum`") | ❌ | ❌ |
| ("`https`", "`r.wildlife.museum`") | ("`https`", "`wildlife.museum`") | ❌ | ❌ |
| ("`https`", "`wildlife.museum`") | ("`https`", "`wildlife.museum`") | ✅ | ✅ |
| ("`https`", "`example.com`") | ("`https`", "`example.com.`") | ❌ | ❌ |

(Here we have omitted the [port](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-port) and [domain](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-domain) components since they are not considered.)

##### 7.1.1.2 Relaxing the same-origin restriction[](https://html.spec.whatwg.org/multipage/browsers.html#relaxing-the-same-origin-restriction)

`document.domain [ = domain ]`
Returns the current domain used for security checks.

Can be set to a value that removes subdomains, to change the [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)'s [domain](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-domain) to allow pages on other subdomains of the same domain (if they do the same thing) to access each other. This enables pages on different hosts of a domain to synchronously access each other's DOMs.

In sandboxed `iframe`s, `Document`s with [opaque origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), and `Document`s without a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc), the setter will throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror) exception. In cases where `crossOriginIsolated` or `originAgentCluster` return true, the setter will do nothing.

Avoid using the `document.domain` setter. It undermines the security protections provided by the same-origin policy. This is especially acute when using shared hosting; for example, if an untrusted third party is able to host an HTTP server at the same IP address but on a different port, then the same-origin protection that normally protects two different sites on the same host will fail, as the ports are ignored when comparing origins after the `document.domain` setter has been used.

Because of these security pitfalls, this feature is in the process of being removed from the web platform. (This is a long process that takes many years.)

Instead, use `postMessage()` or `MessageChannel` objects to communicate across origins in a safe manner.

The `domain` getter steps are:

1.   Let effectiveDomain be [this](https://webidl.spec.whatwg.org/#this)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin)'s [effective domain](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-effective-domain).

2.   If effectiveDomain is null, then return the empty string.

3.   Return effectiveDomain, [serialized](https://url.spec.whatwg.org/#concept-host-serializer).

The `domain` setter steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this)'s [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc) is null, then throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException`.

2.   If [this](https://webidl.spec.whatwg.org/#this)'s [active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set) has its [sandboxed `document.domain` browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-document.domain-browsing-context-flag) set, then throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException`.

3.   Let effectiveDomain be [this](https://webidl.spec.whatwg.org/#this)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin)'s [effective domain](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-effective-domain).

4.   If effectiveDomain is null, then throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException`.

5.   If the given value [is not a registrable domain suffix of and is not equal to](https://html.spec.whatwg.org/multipage/browsers.html#is-a-registrable-domain-suffix-of-or-is-equal-to)effectiveDomain, then throw a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException`.

6.   If the [surrounding agent](https://tc39.es/ecma262/#surrounding-agent)'s [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters)'s [is origin-keyed](https://html.spec.whatwg.org/multipage/webappapis.html#is-origin-keyed) is true, then return.

7.   Set [this](https://webidl.spec.whatwg.org/#this)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin)'s [domain](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-domain) to the result of [parsing](https://url.spec.whatwg.org/#concept-host-parser) the given value.

To determine if a [scalar value string](https://infra.spec.whatwg.org/#scalar-value-string)hostSuffixString is a registrable domain suffix of or is equal to a [host](https://url.spec.whatwg.org/#concept-host)originalHost:

1.   If hostSuffixString is the empty string, then return false.

2.   Let hostSuffix be the result of [parsing](https://url.spec.whatwg.org/#concept-host-parser)hostSuffixString.

3.   If hostSuffix is failure, then return false.

4.   If hostSuffix does not [equal](https://url.spec.whatwg.org/#concept-host-equals)originalHost, then:

    1.   If hostSuffix or originalHost is not a [domain](https://url.spec.whatwg.org/#concept-domain), then return false.

This excludes [hosts](https://url.spec.whatwg.org/#concept-host) that are [IP addresses](https://url.spec.whatwg.org/#ip-address).

    2.   If hostSuffix, prefixed by U+002E (.), does not match the end of originalHost, then return false.

    3.   If any of the following are true:

        *   hostSuffix[equals](https://url.spec.whatwg.org/#concept-host-equals)hostSuffix's [public suffix](https://url.spec.whatwg.org/#host-public-suffix); or

        *   hostSuffix, prefixed by U+002E (.), matches the end of originalHost's [public suffix](https://url.spec.whatwg.org/#host-public-suffix),

then return false. [[URL]](https://html.spec.whatwg.org/multipage/references.html#refsURL)

    4.   [Assert](https://infra.spec.whatwg.org/#assert): originalHost's [public suffix](https://url.spec.whatwg.org/#host-public-suffix), prefixed by U+002E (.), matches the end of hostSuffix.

5.   Return true.

| hostSuffixString | originalHost | Outcome of [is a registrable domain suffix of or is equal to](https://html.spec.whatwg.org/multipage/browsers.html#is-a-registrable-domain-suffix-of-or-is-equal-to) | Notes |
| --- | --- | --- | --- |
| "`0.0.0.0`" | `0.0.0.0` | ✅ |  |
| "`0x10203`" | `0.1.2.3` | ✅ |  |
| "`[0::1]`" | `::1` | ✅ |  |
| "`example.com`" | `example.com` | ✅ |  |
| "`example.com`" | `example.com.` | ❌ | Trailing dot is significant. |
| "`example.com.`" | `example.com` | ❌ |
| "`example.com`" | `www.example.com` | ✅ |  |
| "`com`" | `example.com` | ❌ | At the time of writing, `com` is a public suffix. |
| "`example`" | `example` | ✅ |  |
| "`compute.amazonaws.com`" | `example.compute.amazonaws.com` | ❌ | At the time of writing, `*.compute.amazonaws.com` is a public suffix. |
| "`example.compute.amazonaws.com`" | `www.example.compute.amazonaws.com` | ❌ |
| "`amazonaws.com`" | `www.example.compute.amazonaws.com` | ❌ |
| "`amazonaws.com`" | `test.amazonaws.com` | ✅ | At the time of writing, `amazonaws.com` is a registrable domain. |

##### 7.1.1.3 The `Origin` interface[](https://html.spec.whatwg.org/multipage/browsers.html#the-origin-interface)

The `Origin` interface represents an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin), allowing robust [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) and [same site](https://html.spec.whatwg.org/multipage/browsers.html#same-site) comparisons.

```
[Exposed=*]
interface Origin {
  constructor();

  static Origin from(any value);

  readonly attribute boolean opaque;

  boolean isSameOrigin(Origin other);
  boolean isSameSite(Origin other);
};
```

`Origin` objects have an associated origin, which holds an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin).

[Platform objects](https://webidl.spec.whatwg.org/#dfn-platform-object) have an operation, which returns null unless otherwise specified.

Objects implementing the `Origin` interface's [extract an origin](https://html.spec.whatwg.org/multipage/browsers.html#extract-an-origin) steps are to return [this](https://webidl.spec.whatwg.org/#this)'s [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-origin).

The `new Origin()` constructor steps are to set [this](https://webidl.spec.whatwg.org/#this)'s [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-origin) to a unique [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque).

The static `from(value)` method steps are:

1.   If value is a [platform object](https://webidl.spec.whatwg.org/#dfn-platform-object):

    1.   Let origin be the result of executing value's [extract an origin](https://html.spec.whatwg.org/multipage/browsers.html#extract-an-origin) operation.

    2.   If origin is not null, then return a new `Origin` object whose [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-origin) is origin.

2.   If value is a [string](https://infra.spec.whatwg.org/#string):

    1.   Let parsedURL be the result of [basic URL parsing](https://url.spec.whatwg.org/#concept-basic-url-parser)value.

    2.   If parsedURL is not failure, then return a new `Origin` object whose [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-origin) is set to parsedURL's [origin](https://url.spec.whatwg.org/#concept-url-origin).

3.   Throw a `TypeError`.

The `opaque` getter steps are to return true if [this](https://webidl.spec.whatwg.org/#this)'s [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-origin) is an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque); otherwise false.

The `isSameOrigin(other)` method steps are to return true if [this](https://webidl.spec.whatwg.org/#this)'s [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-origin) is [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with other's [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-origin); otherwise false.

The `isSameSite(other)` method steps are to return true if [this](https://webidl.spec.whatwg.org/#this)'s [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-origin) is [same site](https://html.spec.whatwg.org/multipage/browsers.html#same-site) with other's [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-origin); otherwise false.

#### 7.1.2 Origin-keyed agent clusters[](https://html.spec.whatwg.org/multipage/browsers.html#origin-keyed-agent-clusters)

`window.originAgentCluster`
Returns true if this `Window` belongs to an [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters) which is [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)-[keyed](https://html.spec.whatwg.org/multipage/webappapis.html#agent-cluster-key), in the manner described in this section.

A `Document` delivered over a [secure context](https://html.spec.whatwg.org/multipage/webappapis.html#secure-context) can request that it be placed in an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)-[keyed](https://html.spec.whatwg.org/multipage/webappapis.html#agent-cluster-key)[agent cluster](https://tc39.es/ecma262/#sec-agent-clusters), by using the ``Origin-Agent-Cluster`` HTTP response header. This header is a [structured header](https://httpwg.org/specs/rfc8941.html) whose value must be a [boolean](https://httpwg.org/specs/rfc8941.html#boolean). [[STRUCTURED-FIELDS]](https://html.spec.whatwg.org/multipage/references.html#refsSTRUCTURED-FIELDS)

Per the processing model in the [create and initialize a new `Document` object](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object), values that are not the [structured header boolean](https://httpwg.org/specs/rfc8941.html#boolean) true value (i.e., ``?1``) will be ignored.

The consequences of using this header are that the resulting `Document`'s [agent cluster key](https://html.spec.whatwg.org/multipage/webappapis.html#agent-cluster-key) is its [origin](https://dom.spec.whatwg.org/#concept-document-origin), instead of the [corresponding site](https://html.spec.whatwg.org/multipage/browsers.html#obtain-a-site). In terms of observable effects, this means that attempting to [relax the same-origin restriction](https://html.spec.whatwg.org/multipage/browsers.html#relaxing-the-same-origin-restriction) using `document.domain` will instead do nothing, and it will not be possible to send `WebAssembly.Module` objects to cross-origin `Document`s (even if they are [same site](https://html.spec.whatwg.org/multipage/browsers.html#same-site)). Behind the scenes, this isolation can allow user agents to allocate implementation-specific resources corresponding to [agent clusters](https://tc39.es/ecma262/#sec-agent-clusters), such as processes or threads, more efficiently.

Note that within a [browsing context group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group), the ``Origin-Agent-Cluster`` header can never cause same-origin `Document` objects to end up in different [agent clusters](https://tc39.es/ecma262/#sec-agent-clusters), even if one sends the header and the other doesn't. This is prevented by means of the [historical agent cluster key map](https://html.spec.whatwg.org/multipage/document-sequences.html#historical-agent-cluster-key-map).

This means that the `originAgentCluster` getter can return false, even if the header is set, if the header was omitted on a previously-loaded same-origin page in the same [browsing context group](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-group). Similarly, it can return true even when the header is not set.

`Document`s with an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque) can be considered unconditionally origin-keyed; for them the header has no effect, and the `originAgentCluster` getter will always return true.

Similarly, `Document`s whose [agent cluster](https://tc39.es/ecma262/#sec-agent-clusters)'s [cross-origin isolation mode](https://html.spec.whatwg.org/multipage/webappapis.html#agent-cluster-cross-origin-isolation) is not "`none`" are automatically origin-keyed. The ``Origin-Agent-Cluster`` header might be useful as an additional hint to implementations about resource allocation, since the ``Cross-Origin-Opener-Policy`` and ``Cross-Origin-Embedder-Policy`` headers used to achieve cross-origin isolation are more about ensuring that everything in the same address space opts in to being there. But adding it would have no additional observable effects on author code.

#### 7.1.3 Cross-origin opener policies[](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policies)

An opener policy value allows a document which is navigated to in a [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context) to force the creation of a new [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context), and a corresponding [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group). The possible values are:

"`unsafe-none`"
This is the (current) default and means that the document will occupy the same [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context) as its predecessor, unless that document specified a different [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy).

""
This forces the creation of a new [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context) for the document, unless its predecessor specified the same [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy) and they are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin).

"`same-origin`"
This behaves the same as "", with the addition that any [auxiliary browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#auxiliary-browsing-context) created needs to contain [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) documents that also have the same [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy) or it will appear closed to the opener.

"`same-origin-plus-COEP`"
This behaves the same as "`same-origin`", with the addition that it sets the (new) [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context)'s [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group)'s [cross-origin isolation mode](https://html.spec.whatwg.org/multipage/document-sequences.html#bcg-cross-origin-isolation) to one of "`logical`" or "`concrete`".

"`same-origin-plus-COEP`" cannot be directly set via the ``Cross-Origin-Opener-Policy`` header, but results from a combination of setting both ``Cross-Origin-Opener-Policy: same-origin`` and a ``Cross-Origin-Embedder-Policy`` header whose value is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation) together.

""
This forces the creation of a new [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context) for the document, regardless of its predecessor.

While including a value severs the opener relationship between the document on which it is applied and its opener, it does not create a robust security boundary between those same-origin documents.

Other risks from same-origin applications include:

*   Same-origin requests fetching the document's content — could be mitigated through Fetch Metadata filtering. [[FETCHMETADATA]](https://html.spec.whatwg.org/multipage/references.html#refsFETCHMETADATA)

*   Same-origin framing - could be mitigated through `X-Frame-Options` or CSP `frame-ancestors`.

*   JavaScript accessible cookies - can be mitigated by ensuring all cookies are `httponly`.

*   `localStorage` access to sensitive data.

*   Service worker installation.

*   [Cache API](https://w3c.github.io/ServiceWorker/#cache) manipulation or access to sensitive data. [[SW]](https://html.spec.whatwg.org/multipage/references.html#refsSW)

*   `postMessage` or `BroadcastChannel` messaging that exposes sensitive information.

*   Autofill which may not require user interaction for same-origin documents.

Developers using need to make sure that their sensitive applications don't rely on client-side features accessible to other same-origin documents, e.g., `localStorage` and other client-side storage APIs, `BroadcastChannel` and related same-origin communication mechanisms. They also need to make sure that their server-side endpoints don't return sensitive data to non-navigation requests, whose response content is accessible to same-origin documents.

An opener policy consists of:

*   A value, which is an [opener policy value](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy-value), initially "`unsafe-none`".

*   A reporting endpoint, which is string or null, initially null.

*   A report-only value, which is an [opener policy value](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy-value), initially "`unsafe-none`".

*   A report-only reporting endpoint, which is a string or null, initially null.

To match opener policy values, given an [opener policy value](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy-value)documentCOOP, an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)documentOrigin, an [opener policy value](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy-value)responseCOOP, and an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)responseOrigin:

1.   If documentCOOP is "`unsafe-none`" and responseCOOP is "`unsafe-none`", then return true.

2.   If documentCOOP is "`unsafe-none`" or responseCOOP is "`unsafe-none`", then return false.

3.   If documentCOOP is responseCOOP and documentOrigin is [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with responseOrigin, then return true.

4.   Return false.

[Headers/Cross-Origin-Opener-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy "The HTTP Cross-Origin-Opener-Policy (COOP) response header allows you to ensure a top-level document does not share a browsing context group with cross-origin documents.")

Support in all current engines.

Firefox 79+Safari 15.2+Chrome 83+

* * *

Opera No Edge 83+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android No Samsung Internet?Opera Android No

A 's [cross-origin opener policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-coop) is derived from the ``Cross-Origin-Opener-Policy`` and ``Cross-Origin-Opener-Policy-Report-Only`` HTTP response headers. These headers are [structured headers](https://httpwg.org/specs/rfc8941.html) whose value must be a [token](https://httpwg.org/specs/rfc8941.html#token). [[STRUCTURED-FIELDS]](https://html.spec.whatwg.org/multipage/references.html#refsSTRUCTURED-FIELDS)

The valid [token](https://httpwg.org/specs/rfc8941.html#token) values are the [opener policy values](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy-value). The token may also have attached [parameters](https://httpwg.org/specs/rfc8941.html#param); of these, the "`report-to`" parameter can have a [valid URL string](https://url.spec.whatwg.org/#valid-url-string) identifying an appropriate reporting endpoint. [[REPORTING]](https://html.spec.whatwg.org/multipage/references.html#refsREPORTING)

Per the processing model described below, user agents will ignore this header if it contains an invalid value. Likewise, user agents will ignore this header if the value cannot be parsed as a [token](https://httpwg.org/specs/rfc8941.html#token).

* * *

To obtain an opener policy given a [response](https://fetch.spec.whatwg.org/#concept-response)response and an [environment](https://html.spec.whatwg.org/multipage/webappapis.html#environment)reservedEnvironment:

1.   Let policy be a new [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy).

2.   If reservedEnvironment is a [non-secure context](https://html.spec.whatwg.org/multipage/webappapis.html#non-secure-context), then return policy.

3.   Let parsedItem be the result of [getting a structured field value](https://fetch.spec.whatwg.org/#concept-header-list-get-structured-header) given `` and "`item`" from response's [header list](https://fetch.spec.whatwg.org/#concept-response-header-list).

4.   If parsedItem is not null, then:

    1.   If parsedItem[0] is "", then:

        1.   Let coep be the result of [obtaining a cross-origin embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#obtain-an-embedder-policy) from response and reservedEnvironment.

        2.   If coep's [value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value-2) is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation), then set policy's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value) to "".

        3.   Otherwise, set policy's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value) to "".

    2.   If parsedItem[0] is "", then set policy's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value) to "".

    3.   If parsedItem[0] is "", then set policy's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value) to "".

    4.   If parsedItem[1][""] [exists](https://infra.spec.whatwg.org/#map-exists) and it is a string, then set policy's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) to parsedItem[1][""].

5.   Set parsedItem to the result of [getting a structured field value](https://fetch.spec.whatwg.org/#concept-header-list-get-structured-header) given `` and "`item`" from response's [header list](https://fetch.spec.whatwg.org/#concept-response-header-list).

6.   If parsedItem is not null, then:

    1.   If parsedItem[0] is "", then:

        1.   Let coep be the result of [obtaining a cross-origin embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#obtain-an-embedder-policy) from response and reservedEnvironment.

        2.   If coep's [value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value-2) is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation) or coep's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-report-only-value) is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation), then set policy's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) to "".

Report only COOP also considers report-only COEP to assign the special "" value. This allows developers more freedom in the order of deployment of COOP and COEP.

        3.   Otherwise, set policy's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) to "".

    2.   If parsedItem[0] is "", then set policy's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) to "".

    3.   If parsedItem[1][""] [exists](https://infra.spec.whatwg.org/#map-exists) and it is a string, then set policy's [report-only reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-endpoint) to parsedItem[1][""].

7.   Return policy.

##### 7.1.3.2 Browsing context group switches due to opener policy[](https://html.spec.whatwg.org/multipage/browsers.html#browsing-context-group-switches-due-to-cross-origin-opener-policy)

To , given two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)responseOrigin and activeDocumentNavigationOrigin, and two [opener policy values](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value)responseCOOPValue and activeDocumentCOOPValue:

1.   If responseCOOPValue is "", then return true.

2.   If all of the following are true:

    *   activeDocumentCOOPValue's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value) is "" or ""; and

    *   responseCOOPValue is "`unsafe-none`",

then return false.

3.   If the result of [matching](https://html.spec.whatwg.org/multipage/browsers.html#matching-coop)activeDocumentCOOPValue, activeDocumentNavigationOrigin, responseCOOPValue, and responseOrigin is true, then return false.

4.   Return true.

To check if COOP values require a browsing context group switch, given a boolean isInitialAboutBlank, two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)responseOrigin and activeDocumentNavigationOrigin, and two [opener policy values](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value)responseCOOPValue and activeDocumentCOOPValue:

1.   If isInitialAboutBlank is true, then return the result of [checking if popup COOP values requires a browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#check-browsing-context-group-switch-coop-value-popup) with responseOrigin, activeDocumentNavigationOrigin, responseCOOPValue, and activeDocumentCOOPValue.

2.   Here we are dealing with a non-popup navigation.

If the result of [matching](https://html.spec.whatwg.org/multipage/browsers.html#matching-coop)activeDocumentCOOPValue, activeDocumentNavigationOrigin, responseCOOPValue, and responseOrigin is true, then return false.

3.   Return true.

To check if enforcing report-only COOP would require a browsing context group switch, given a boolean isInitialAboutBlank, two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)responseOrigin, activeDocumentNavigationOrigin, and two [opener policies](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)responseCOOP and activeDocumentCOOP:

1.   If the result of [checking if COOP values require a browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#check-browsing-context-group-switch-coop-value) given isInitialAboutBlank, responseOrigin, activeDocumentNavigationOrigin, responseCOOP's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value), and activeDocumentCOOPReportOnly's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) is false, then return false.

Matching report-only policies allows a website to specify the same report-only opener policy on all its pages and not receive violation reports for navigations between these pages.

2.   If the result of [checking if COOP values require a browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#check-browsing-context-group-switch-coop-value) given isInitialAboutBlank, responseOrigin, activeDocumentNavigationOrigin, responseCOOP's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value), and activeDocumentCOOPReportOnly's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) is true, then return true.

3.   If the result of [checking if COOP values require a browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#check-browsing-context-group-switch-coop-value) given isInitialAboutBlank, responseOrigin, activeDocumentNavigationOrigin, responseCOOP's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value), and activeDocumentCOOPReportOnly's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value) is true, then return true.

4.   Return false.

An opener policy enforcement result is a [struct](https://infra.spec.whatwg.org/#struct) with the following [items](https://infra.spec.whatwg.org/#struct-item):

*   A boolean needs a browsing context group switch, initially false.

*   A boolean would need a browsing context group switch due to report-only, initially false.

*   A [URL](https://url.spec.whatwg.org/#concept-url)url.

*   An [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)origin.

*   An [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)opener policy.

*   A boolean current context is navigation source, initially false.

To enforce a response's opener policy, given a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)browsingContext, a [URL](https://url.spec.whatwg.org/#concept-url)responseURL, an [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)responseOrigin, an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)responseCOOP, an [opener policy enforcement result](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-result)currentCOOPEnforcementResult, and a [referrer](https://fetch.spec.whatwg.org/#concept-request-referrer)referrer:

1.   Let newCOOPEnforcementResult be a new [opener policy enforcement result](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-result) with

[needs a browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-bcg-switch)currentCOOPEnforcementResult's [needs a browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-bcg-switch)[would need a browsing context group switch due to report-only](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-bcg-switch-report-only)currentCOOPEnforcementResult's [would need a browsing context group switch due to report-only](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-bcg-switch-report-only)[url](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-url)responseURL[origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin)responseOrigin[opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-coop)responseCOOP[current context is navigation source](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-source)true
2.   Let isInitialAboutBlank be browsingContext's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [is initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank).

3.   If isInitialAboutBlank is true and browsingContext's [initial URL](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-initial-url) is null, set browsingContext's [initial URL](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-initial-url) to responseURL.

4.   If the result of [checking if COOP values require a browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#check-browsing-context-group-switch-coop-value) given isInitialAboutBlank, currentCOOPEnforcementResult's [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-coop)'s [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value), currentCOOPEnforcementResult's [origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin), responseCOOP's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value), and responseOrigin is true, then:

    1.   Set newCOOPEnforcementResult's [needs a browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-bcg-switch) to true.

    2.   If browsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group)'s [browsing context set](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-set)'s [size](https://infra.spec.whatwg.org/#list-size) is greater than 1, then:

        1.   [Queue a violation report for browsing context group switch when navigating to a COOP response](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-navigation-to) with responseCOOP, "`enforce`", responseURL, currentCOOPEnforcementResult's [url](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-url), currentCOOPEnforcementResult's [origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin), responseOrigin, and referrer.

        2.   [Queue a violation report for browsing context group switch when navigating away from a COOP response](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-navigation-from) with currentCOOPEnforcementResult's [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-coop), "`enforce`", currentCOOPEnforcementResult's [url](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-url), responseURL, currentCOOPEnforcementResult's [origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin), responseOrigin, and currentCOOPEnforcementResult's [current context is navigation source](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-source).

5.   If the result of [checking if enforcing report-only COOP would require a browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#check-bcg-switch-navigation-report-only) given isInitialAboutBlank, responseOrigin, currentCOOPEnforcementResult's [origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin), responseCOOP, and currentCOOPEnforcementResult's [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-coop), is true, then:

    1.   Set newCOOPEnforcementResult's [would need a browsing context group switch due to report-only](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-bcg-switch-report-only) to true.

    2.   If browsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group)'s [browsing context set](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-set)'s [size](https://infra.spec.whatwg.org/#list-size) is greater than 1, then:

        1.   [Queue a violation report for browsing context group switch when navigating to a COOP response](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-navigation-to) with responseCOOP, "`reporting`", responseURL, currentCOOPEnforcementResult's [url](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-url), currentCOOPEnforcementResult's [origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin), responseOrigin, and referrer.

        2.   [Queue a violation report for browsing context group switch when navigating away from a COOP response](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-navigation-from) with currentCOOPEnforcementResult's [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-coop), "`reporting`", currentCOOPEnforcementResult's [url](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-url), responseURL, currentCOOPEnforcementResult's [origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin), responseOrigin, and currentCOOPEnforcementResult's [current context is navigation source](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-source).

6.   Return newCOOPEnforcementResult.

To obtain a browsing context to use for a navigation response, given [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params)navigationParams:

1.   Let browsingContext be navigationParams's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable)'s [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc).

2.   If browsingContext is not a [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context), then return browsingContext.

3.   Let coopEnforcementResult be navigationParams's [COOP enforcement result](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop-enforcement-result).

4.   Let swapGroup be coopEnforcementResult's [needs a browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-bcg-switch).

5.   Let sourceOrigin be browsingContext's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin).

6.   Let destinationOrigin be navigationParams's [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin).

7.   If sourceOrigin is not [same site](https://html.spec.whatwg.org/multipage/browsers.html#same-site) with destinationOrigin:

    1.   If either of sourceOrigin or destinationOrigin have a [scheme](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-scheme) that is not an [HTTP(S) scheme](https://fetch.spec.whatwg.org/#http-scheme) and the user agent considers it necessary for sourceOrigin and destinationOrigin to be isolated from each other (for [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) reasons), optionally set swapGroup to true.

For example, if a user navigates from `about:settings` to `https://example.com`, the user agent could force a swap.

[Issue #10842](https://github.com/whatwg/html/issues/10842) tracks settling on an interoperable behavior here, instead of letting this be optional.

    2.   If navigationParams's [user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-user-involvement) is "`browser UI`", optionally set swapGroup to true.

[Issue #6356](https://github.com/whatwg/html/issues/6356) tracks settling on an interoperable behavior here, instead of letting this be optional.

8.   If browsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group)'s [browsing context set](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-set)'s [size](https://infra.spec.whatwg.org/#list-size) is 1, optionally set swapGroup to true.

Some implementations swap browsing context groups here for performance reasons.

The check for other contexts that could script this one is not sufficient to prevent differences in behavior that could affect a web page. Even if there are currently no other contexts, the destination page could open a window, then if the user navigates back, the previous page could expect to be able to script the opened window. Doing a swap here would break that use case.

9.   If swapGroup is false, then:

    1.   If coopEnforcementResult's [would need a browsing context group switch due to report-only](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-bcg-switch-report-only) is true, set browsingContext's [virtual browsing context group ID](https://html.spec.whatwg.org/multipage/document-sequences.html#virtual-browsing-context-group-id) to a new unique identifier.

    2.   Return browsingContext.

10.   Let newBrowsingContext be the first return value of [creating a new top-level browsing context and document](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-top-level-browsing-context).

In this case we are going to perform a browsing context group swap. browsingContext will not be used by the new `Document` that we are about to [create](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object). If it is not used by other `Document`s either (such as ones in the back/forward cache), then the user agent might [destroy it](https://html.spec.whatwg.org/multipage/document-sequences.html#a-browsing-context-is-discarded) at this point.

11.   Let navigationCOOP be navigationParams's [cross-origin opener policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop).

12.   If navigationCOOP's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value) is "`same-origin-plus-COEP`", then set newBrowsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group)'s [cross-origin isolation mode](https://html.spec.whatwg.org/multipage/document-sequences.html#bcg-cross-origin-isolation) to either "`logical`" or "`concrete`". The choice of which is [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined).

It is difficult on some platforms to provide the security properties required by the [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-cross-origin-isolated-capability). "`concrete`" grants access to it and "`logical`" does not.

13.   Let sandboxFlags be a [clone](https://infra.spec.whatwg.org/#list-clone) of navigationParams's [final sandboxing flag set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-sandboxing).

14.   If sandboxFlags is not empty, then:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): navigationCOOP's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value) is "`unsafe-none`".

    2.   [Assert](https://infra.spec.whatwg.org/#assert): newBrowsingContext's [popup sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#popup-sandboxing-flag-set)[is empty](https://infra.spec.whatwg.org/#list-is-empty).

    3.   Set newBrowsingContext's [popup sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#popup-sandboxing-flag-set) to sandboxFlags.

15.   Return newBrowsingContext.

##### 7.1.3.3 Reporting[](https://html.spec.whatwg.org/multipage/browsers.html#coop-reporting)

An accessor-accessed relationship is an enum that describes the relationship between two [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) between which an access happened. It can take the following values:

accessor is opener
The accessor [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) or one of its [ancestors](https://html.spec.whatwg.org/multipage/document-sequences.html#ancestor-browsing-context) is the [opener browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-browsing-context) of the accessed [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)'s [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc).

accessor is openee
The accessed [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) or one of its [ancestors](https://html.spec.whatwg.org/multipage/document-sequences.html#ancestor-browsing-context) is the [opener browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-browsing-context) of the accessor [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)'s [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc).

none
There is no opener relationship between the accessor [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context), the accessor [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context), or any of their [ancestors](https://html.spec.whatwg.org/multipage/document-sequences.html#ancestor-browsing-context).

To check if an access between two browsing contexts should be reported, given two [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context)accessor and accessed, a JavaScript property name P, and an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)environment:

1.   If P is not a [cross-origin accessible window property name](https://html.spec.whatwg.org/multipage/nav-history-apis.html#cross-origin-accessible-window-property-name), then return.

2.   [Assert](https://infra.spec.whatwg.org/#assert): accessor's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document) and accessed's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document) are both [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active).

3.   Let accessorTopDocument be accessor's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document).

4.   Let accessorInclusiveAncestorOrigins be the list obtained by taking the [origin](https://dom.spec.whatwg.org/#concept-document-origin) of the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of each of accessor's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [inclusive ancestor navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#inclusive-ancestor-navigables).

5.   Let accessedTopDocument be accessed's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document).

6.   Let accessedInclusiveAncestorOrigins be the list obtained by taking the [origin](https://dom.spec.whatwg.org/#concept-document-origin) of the [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) of each of accessed's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [inclusive ancestor navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#inclusive-ancestor-navigables).

7.   If any of accessorInclusiveAncestorOrigins are not [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with accessorTopDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin), or if any of accessedInclusiveAncestorOrigins are not [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with accessedTopDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin), then return.

This avoids leaking information about cross-origin iframes to a top level frame with opener policy reporting.

8.   If accessor's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [virtual browsing context group ID](https://html.spec.whatwg.org/multipage/document-sequences.html#virtual-browsing-context-group-id) is accessed's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [virtual browsing context group ID](https://html.spec.whatwg.org/multipage/document-sequences.html#virtual-browsing-context-group-id), then return.

9.   Let accessorAccessedRelationship be a new [accessor-accessed relationship](https://html.spec.whatwg.org/multipage/browsers.html#accessor-accessed-relationship) with value [none](https://html.spec.whatwg.org/multipage/browsers.html#accessor-accessed-none).

10.   If accessed's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [opener browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-browsing-context) is accessor or is an [ancestor](https://html.spec.whatwg.org/multipage/document-sequences.html#ancestor-browsing-context) of accessor, then set accessorAccessedRelationship to [accessor is opener](https://html.spec.whatwg.org/multipage/browsers.html#accessor-accessed-opener).

11.   If accessor's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [opener browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-browsing-context) is accessed or is an [ancestor](https://html.spec.whatwg.org/multipage/document-sequences.html#ancestor-browsing-context) of accessed, then set accessorAccessedRelationship to [accessor is openee](https://html.spec.whatwg.org/multipage/browsers.html#accessor-accessed-openee).

12.   [Queue violation reports for accesses](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-access), given accessorAccessedRelationship, accessorTopDocument's [opener policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-coop), accessedTopDocument's [opener policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-coop), accessor's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [URL](https://dom.spec.whatwg.org/#concept-document-url), accessed's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [URL](https://dom.spec.whatwg.org/#concept-document-url), accessor's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [initial URL](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-initial-url), accessed's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [initial URL](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context-initial-url), accessor's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin), accessed's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin), accessor's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [opener origin at creation](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-origin-at-creation), accessed's [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#bc-tlbc)'s [opener origin at creation](https://html.spec.whatwg.org/multipage/document-sequences.html#opener-origin-at-creation), accessorTopDocument's [referrer](https://html.spec.whatwg.org/multipage/dom.html#dom-document-referrer), accessedTopDocument's [referrer](https://html.spec.whatwg.org/multipage/dom.html#dom-document-referrer), P, and environment.

To queue a violation report for browsing context group switch when navigating to a COOP response given an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)coop, a string disposition, a [URL](https://url.spec.whatwg.org/#concept-url)coopURL, a [URL](https://url.spec.whatwg.org/#concept-url)previousResponseURL, two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)coopOrigin and previousResponseOrigin, and a [referrer](https://fetch.spec.whatwg.org/#concept-request-referrer)referrer:

1.   If coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) is null, return.

2.   Let coopValue be coop's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value).

3.   If disposition is "`reporting`", then set coopValue to coop's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value).

4.   Let serializedReferrer be an empty string.

5.   If referrer is a [URL](https://url.spec.whatwg.org/#concept-url), set serializedReferrer to the [serialization](https://url.spec.whatwg.org/#concept-url-serializer) of referrer.

6.   Let body be a new object containing the following properties:

| key | value |
| --- | --- |
| disposition | disposition |
| effectivePolicy | coopValue |
| previousResponseURL | If coopOrigin and previousResponseOrigin are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) this is the [sanitization](https://html.spec.whatwg.org/multipage/browsers.html#sanitize-url-report) of previousResponseURL, null otherwise. |
| referrer | serializedReferrer |
| type | "`navigation-to-response`" |
7.   [Queue](https://w3c.github.io/reporting/#queue-report)body as "`coop`" for coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) with coopURL.

To queue a violation report for browsing context group switch when navigating away from a COOP response given an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)coop, a string disposition, a [URL](https://url.spec.whatwg.org/#concept-url)coopURL, a [URL](https://url.spec.whatwg.org/#concept-url)nextResponseURL, two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)coopOrigin and nextResponseOrigin, and a boolean isCOOPResponseNavigationSource:

1.   If coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) is null, return.

2.   Let coopValue be coop's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value).

3.   If disposition is "`reporting`", then set coopValue to coop's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value).

4.   Let body be a new object containing the following properties:

| key | value |
| --- | --- |
| disposition | disposition |
| effectivePolicy | coopValue |
| nextResponseURL | If coopOrigin and nextResponseOrigin are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) or isCOOPResponseNavigationSource is true, this is the [sanitization](https://html.spec.whatwg.org/multipage/browsers.html#sanitize-url-report) of nextResponseURL, null otherwise. |
| type | "`navigation-from-response`" |
5.   [Queue](https://w3c.github.io/reporting/#queue-report)body as "`coop`" for coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) with coopURL.

To queue violation reports for accesses, given an [accessor-accessed relationship](https://html.spec.whatwg.org/multipage/browsers.html#accessor-accessed-relationship)accessorAccessedRelationship, two [opener policies](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)accessorCOOP and accessedCOOP, four [URLs](https://url.spec.whatwg.org/#concept-url)accessorURL, accessedURL, accessorInitialURL, accessedInitialURL, four [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)accessorOrigin, accessedOrigin, accessorCreatorOrigin and accessedCreatorOrigin, two [referrers](https://html.spec.whatwg.org/multipage/dom.html#dom-document-referrer)accessorReferrer and accessedReferrer, a string propertyName, and an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)environment:

1.   If coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) is null, return.

2.   Let coopValue be coop's [value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-value).

3.   If disposition is "`reporting`", then set coopValue to coop's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value).

4.   If accessorAccessedRelationship is [accessor is opener](https://html.spec.whatwg.org/multipage/browsers.html#accessor-accessed-opener):

    1.   [Queue a violation report for access to an opened window](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-access-to-opened), given accessorCOOP, accessorURL, accessedURL, accessedInitialURL, accessorOrigin, accessedOrigin, accessedCreatorOrigin, propertyName, and environment.

    2.   [Queue a violation report for access from the opener](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-access-from-opener), given accessedCOOP, accessedURL, accessorURL, accessedOrigin, accessorOrigin, propertyName, and accessedReferrer.

5.   Otherwise, if accessorAccessedRelationship is [accessor is openee](https://html.spec.whatwg.org/multipage/browsers.html#accessor-accessed-openee):

    1.   [Queue a violation report for access to the opener](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-access-to-opener), given accessorCOOP, accessorURL, accessedURL, accessorOrigin, accessedOrigin, propertyName, accessorReferrer, and environment.

    2.   [Queue a violation report for access from an opened window](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-access-from-opened), given accessedCOOP, accessedURL, accessorURL, accessorInitialURL, accessedOrigin, accessorOrigin, accessorCreatorOrigin, and propertyName.

6.   Otherwise:

    1.   [Queue a violation report for access to another window](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-access-to-opened), given accessorCOOP, accessorURL, accessedURL, accessorOrigin, accessedOrigin, propertyName, and environment.

    2.   [Queue a violation report for access from another window](https://html.spec.whatwg.org/multipage/browsers.html#coop-violation-access-from-other), given accessedCOOP, accessedURL, accessorURL, accessedOrigin, accessorOrigin, and propertyName.

To queue a violation report for access to the opener, given an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)coop, two [URLs](https://url.spec.whatwg.org/#concept-url)coopURL and openerURL, two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)coopOrigin and openerOrigin, a string propertyName, a [referrer](https://fetch.spec.whatwg.org/#concept-request-referrer)referrer, and an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)environment:

1.   Let sourceFile, lineNumber, and columnNumber be the relevant script URL and problematic position which triggered this report.

2.   Let serializedReferrer be an empty string.

3.   If referrer is a [URL](https://url.spec.whatwg.org/#concept-url), set serializedReferrer to the [serialization](https://url.spec.whatwg.org/#concept-url-serializer) of referrer.

4.   Let body be a new object containing the following properties:

| key | value |
| --- | --- |
| disposition | "`reporting`" |
| effectivePolicy | coop's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) |
| property | propertyName |
| openerURL | If coopOrigin and openerOrigin are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin), this is the [sanitization](https://html.spec.whatwg.org/multipage/browsers.html#sanitize-url-report) of openerURL, null otherwise. |
| referrer | serializedReferrer |
| sourceFile | sourceFile |
| lineNumber | lineNumber |
| columnNumber | columnNumber |
| type | "`access-to-opener`" |
5.   [Queue](https://w3c.github.io/reporting/#queue-report)body as "`coop`" for coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) with coopURL and environment.

To queue a violation report for access to an opened window, given an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)coop, three [URLs](https://url.spec.whatwg.org/#concept-url)coopURL, openedWindowURL and initialWindowURL, three [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)coopOrigin, openedWindowOrigin, and openerInitialOrigin, a string propertyName, and an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)environment:

1.   Let sourceFile, lineNumber, and columnNumber be the relevant script URL and problematic position which triggered this report.

2.   Let body be a new object containing the following properties:

| key | value |
| --- | --- |
| disposition | "`reporting`" |
| effectivePolicy | coop's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) |
| property | propertyName |
| openedWindowURL | If coopOrigin and openedWindowOrigin are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin), this is the [sanitization](https://html.spec.whatwg.org/multipage/browsers.html#sanitize-url-report) of openedWindowURL, null otherwise. |
| openedWindowInitialURL | If coopOrigin and openerInitialOrigin are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin), this is the [sanitization](https://html.spec.whatwg.org/multipage/browsers.html#sanitize-url-report) of initialWindowURL, null otherwise. |
| sourceFile | sourceFile |
| lineNumber | lineNumber |
| columnNumber | columnNumber |
| type | "`access-to-opener`" |
3.   [Queue](https://w3c.github.io/reporting/#queue-report)body as "`coop`" for coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) with coopURL and environment.

To queue a violation report for access to another window, given an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)coop, two [URLs](https://url.spec.whatwg.org/#concept-url)coopURL and otherURL, two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)coopOrigin and otherOrigin, a string propertyName, and an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)environment:

1.   Let sourceFile, lineNumber, and columnNumber be the relevant script URL and problematic position which triggered this report.

2.   Let body be a new object containing the following properties:

| key | value |
| --- | --- |
| disposition | "`reporting`" |
| effectivePolicy | coop's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) |
| property | propertyName |
| otherURL | If coopOrigin and otherOrigin are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin), this is the [sanitization](https://html.spec.whatwg.org/multipage/browsers.html#sanitize-url-report) of otherURL, null otherwise. |
| sourceFile | sourceFile |
| lineNumber | lineNumber |
| columnNumber | columnNumber |
| type | "`access-to-opener`" |
3.   [Queue](https://w3c.github.io/reporting/#queue-report)body as "`coop`" for coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) with coopURL and environment.

To queue a violation report for access from the opener, given an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)coop, two [URLs](https://url.spec.whatwg.org/#concept-url)coopURL and openerURL, two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)coopOrigin and openerOrigin, a string propertyName, and a [referrer](https://fetch.spec.whatwg.org/#concept-request-referrer)referrer:

1.   If coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) is null, return.

2.   Let serializedReferrer be an empty string.

3.   If referrer is a [URL](https://url.spec.whatwg.org/#concept-url), set serializedReferrer to the [serialization](https://url.spec.whatwg.org/#concept-url-serializer) of referrer.

4.   Let body be a new object containing the following properties:

| key | value |
| --- | --- |
| disposition | "`reporting`" |
| effectivePolicy | coop's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) |
| property | propertyName |
| openerURL | If coopOrigin and openerOrigin are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin), this is the [sanitization](https://html.spec.whatwg.org/multipage/browsers.html#sanitize-url-report) of openerURL, null otherwise. |
| referrer | serializedReferrer |
| type | "`access-to-opener`" |
5.   [Queue](https://w3c.github.io/reporting/#queue-report)body as "`coop`" for coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) with coopURL.

To queue a violation report for access from an opened window, given an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)coop, three [URLs](https://url.spec.whatwg.org/#concept-url)coopURL, openedWindowURL and initialWindowURL, three [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)coopOrigin, openedWindowOrigin, and openerInitialOrigin, and a string propertyName:

1.   If coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) is null, return.

2.   Let body be a new object containing the following properties:

| key | value |
| --- | --- |
| disposition | "`reporting`" |
| effectivePolicy | coopValue |
| property | coop's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) |
| openedWindowURL | If coopOrigin and openedWindowOrigin are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin), this is the [sanitization](https://html.spec.whatwg.org/multipage/browsers.html#sanitize-url-report) of openedWindowURL, null otherwise. |
| openedWindowInitialURL | If coopOrigin and openerInitialOrigin are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin), this is the [sanitization](https://html.spec.whatwg.org/multipage/browsers.html#sanitize-url-report) of initialWindowURL, null otherwise. |
| type | "`access-to-opener`" |
3.   [Queue](https://w3c.github.io/reporting/#queue-report)body as "`coop`" for coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) with coopURL.

To queue a violation report for access from another window, given an [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy)coop, two [URLs](https://url.spec.whatwg.org/#concept-url)coopURL and otherURL, two [origins](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)coopOrigin and otherOrigin, and a string propertyName:

1.   If coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) is null, return.

2.   Let body be a new object containing the following properties:

| key | value |
| --- | --- |
| disposition | "`reporting`" |
| effectivePolicy | coop's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-only-value) |
| property | propertyName |
| otherURL | If coopOrigin and otherOrigin are [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin), this is the [sanitization](https://html.spec.whatwg.org/multipage/browsers.html#sanitize-url-report) of otherURL, null otherwise. |
| type | `access-to-opener` |
3.   [Queue](https://w3c.github.io/reporting/#queue-report)body as "`coop`" for coop's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#coop-struct-report-endpoint) with coopURL.

#### 7.1.4 Cross-origin embedder policies[](https://html.spec.whatwg.org/multipage/browsers.html#coep)

[Headers/Cross-Origin-Embedder-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Embedder-Policy "The HTTP Cross-Origin-Embedder-Policy (COEP) response header configures embedding cross-origin resources into the document.")

Support in all current engines.

Firefox 79+Safari 15.2+Chrome 83+

* * *

Opera?Edge 83+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 86+Samsung Internet?Opera Android?

An embedder policy value is one of three strings that controls the fetching of cross-origin resources without explicit permission from resource owners.

"`unsafe-none`"
This is the default value. When this value is used, cross-origin resources can be fetched without giving explicit permission through the [CORS protocol](https://fetch.spec.whatwg.org/#http-cors-protocol) or the ``Cross-Origin-Resource-Policy`` header.

"`require-corp`"
When this value is used, fetching cross-origin resources requires the server's explicit permission through the [CORS protocol](https://fetch.spec.whatwg.org/#http-cors-protocol) or the ``Cross-Origin-Resource-Policy`` header.

"`credentialless`"
When this value is used, fetching cross-origin no-CORS resources omits credentials. In exchange, an explicit ``Cross-Origin-Resource-Policy`` header is not required. Other requests sent with credentials require the server's explicit permission through the [CORS protocol](https://fetch.spec.whatwg.org/#http-cors-protocol) or the ``Cross-Origin-Resource-Policy`` header.

An [embedder policy value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value) is compatible with cross-origin isolation if it is "`credentialless`" or "`require-corp`".

An embedder policy consists of:

*   A value, which is an [embedder policy value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value), initially "`unsafe-none`".

*   A reporting endpoint string, initially the empty string.

*   A report only value, which is an [embedder policy value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value), initially "`unsafe-none`".

*   A report only reporting endpoint string, initially the empty string.

The "`coep`" report type is a [report type](https://w3c.github.io/reporting/#report-type) whose value is "`coep`". It is [visible to `ReportingObserver`s](https://w3c.github.io/reporting/#visible-to-reportingobservers).

The ``Cross-Origin-Embedder-Policy`` and ``Cross-Origin-Embedder-Policy-Report-Only`` HTTP response headers allow a server to declare an [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy) for an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object). These headers are [structured headers](https://httpwg.org/specs/rfc8941.html) whose values must be [token](https://httpwg.org/specs/rfc8941.html#token). [[STRUCTURED-FIELDS]](https://html.spec.whatwg.org/multipage/references.html#refsSTRUCTURED-FIELDS)

The valid [token](https://httpwg.org/specs/rfc8941.html#token) values are the [embedder policy values](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value). The token may also have attached [parameters](https://httpwg.org/specs/rfc8941.html#param); of these, the "`report-to`" parameter can have a [valid URL string](https://url.spec.whatwg.org/#valid-url-string) identifying an appropriate reporting endpoint. [[REPORTING]](https://html.spec.whatwg.org/multipage/references.html#refsREPORTING)

The [processing model](https://html.spec.whatwg.org/multipage/browsers.html#obtain-an-embedder-policy) fails open (by defaulting to "") in the presence of a header that cannot be parsed as a token. This includes inadvertent lists created by combining multiple instances of the `` header present in a given response:

| ``Cross-Origin-Embedder-Policy`` | Final [embedder policy value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value) |
| --- | --- |
| _No header delivered_ | "`unsafe-none`" |
| ``require-corp`` | "`require-corp`" |
| ``unknown-value`` | "`unsafe-none`" |
| ``require-corp, unknown-value`` | "`unsafe-none`" |
| ``unknown-value, unknown-value`` | "`unsafe-none`" |
| ``unknown-value, require-corp`` | "`unsafe-none`" |
| ``require-corp, require-corp`` | "`unsafe-none`" |

(The same applies to ``.)

* * *

To obtain an embedder policy from a [response](https://fetch.spec.whatwg.org/#concept-response)response and an [environment](https://html.spec.whatwg.org/multipage/webappapis.html#environment)environment:

1.   Let policy be a new [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy).

2.   If environment is a [non-secure context](https://html.spec.whatwg.org/multipage/webappapis.html#non-secure-context), then return policy.

3.   Let parsedItem be the result of [getting a structured field value](https://fetch.spec.whatwg.org/#concept-header-list-get-structured-header) with `` and "`item`" from response's [header list](https://fetch.spec.whatwg.org/#concept-response-header-list).

4.   If parsedItem is non-null and parsedItem[0] is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation):

    1.   Set policy's [value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value-2) to parsedItem[0].

    2.   If parsedItem[1][""] [exists](https://infra.spec.whatwg.org/#map-exists), then set policy's [endpoint](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-reporting-endpoint) to parsedItem[1][""].

5.   Set parsedItem to the result of [getting a structured field value](https://fetch.spec.whatwg.org/#concept-header-list-get-structured-header) with `` and "`item`" from response's [header list](https://fetch.spec.whatwg.org/#concept-response-header-list).

6.   If parsedItem is non-null and parsedItem[0] is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation):

    1.   Set policy's [report only value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-report-only-value) to parsedItem[0].

    2.   If parsedItem[1][""] [exists](https://infra.spec.whatwg.org/#map-exists), then set policy's [endpoint](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-report-only-reporting-endpoint) to parsedItem[1][""].

7.   Return policy.

##### 7.1.4.2 Embedder policy checks[](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-checks)

To check a navigation response's adherence to its embedder policy given a [response](https://fetch.spec.whatwg.org/#concept-response)response, a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, and an [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy)responsePolicy:

1.   If navigable is not a [child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable), then return true.

2.   Let parentPolicy be navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document)'s [policy container](https://html.spec.whatwg.org/multipage/dom.html#concept-document-policy-container)'s [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-embedder-policy).

3.   If parentPolicy's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-report-only-value) is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation) and responsePolicy's [value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value-2) is not, then [queue a cross-origin embedder policy inheritance violation](https://html.spec.whatwg.org/multipage/browsers.html#queue-a-cross-origin-embedder-policy-inheritance-violation) with response, "`navigation`", parentPolicy's [report only reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-report-only-reporting-endpoint), "`reporting`", and navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

4.   If parentPolicy's [value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value-2) is not [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation) or responsePolicy's [value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value-2) is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation), then return true.

5.   [Queue a cross-origin embedder policy inheritance violation](https://html.spec.whatwg.org/multipage/browsers.html#queue-a-cross-origin-embedder-policy-inheritance-violation) with response, "`navigation`", parentPolicy's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-reporting-endpoint), "`enforce`", and navigable's [container document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container-document)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

6.   Return false.

To check a global object's embedder policy given a `WorkerGlobalScope`workerGlobalScope, an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)owner, and a [response](https://fetch.spec.whatwg.org/#concept-response)response:

1.   If workerGlobalScope is not a `DedicatedWorkerGlobalScope` object, then return true.

2.   Let policy be workerGlobalScope's [embedder policy](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-embedder-policy).

3.   Let ownerPolicy be owner's [policy container](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-policy-container)'s [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-embedder-policy).

4.   If ownerPolicy's [report-only value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-report-only-value) is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation) and policy's [value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value-2) is not, then [queue a cross-origin embedder policy inheritance violation](https://html.spec.whatwg.org/multipage/browsers.html#queue-a-cross-origin-embedder-policy-inheritance-violation) with response, "
```
worker
   initialization
```
", ownerPolicy's [report only reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-report-only-reporting-endpoint), "`reporting`", and owner.

5.   If ownerPolicy's [value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value-2) is not [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation) or policy's [value](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-value-2) is [compatible with cross-origin isolation](https://html.spec.whatwg.org/multipage/browsers.html#compatible-with-cross-origin-isolation), then return true.

6.   [Queue a cross-origin embedder policy inheritance violation](https://html.spec.whatwg.org/multipage/browsers.html#queue-a-cross-origin-embedder-policy-inheritance-violation) with response, "`worker initialization`", ownerPolicy's [reporting endpoint](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy-reporting-endpoint), "`enforce`", and owner.

7.   Return false.

To queue a cross-origin embedder policy inheritance violation given a [response](https://fetch.spec.whatwg.org/#concept-response)response, a string type, a string endpoint, a string disposition, and an [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)settings:

1.   Let serialized be the result of [serializing a response URL for reporting](https://fetch.spec.whatwg.org/#serialize-a-response-url-for-reporting) with response.

2.   Let body be a new object containing the following properties:

| key | value |
| --- | --- |
| type | type |
| blockedURL | serialized |
| disposition | disposition |
3.   [Queue](https://w3c.github.io/reporting/#queue-report)body as the ["`coep`" report type](https://html.spec.whatwg.org/multipage/browsers.html#coep-report-type) for endpoint on settings.

#### 7.1.5 Sandboxing[](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing)

A sandboxing flag set is a set of zero or more of the following flags, which are used to restrict the abilities that potentially untrusted resources have:

The sandboxed navigation browsing context flag
This flag [prevents content from navigating browsing contexts other than the sandboxed browsing context itself](https://html.spec.whatwg.org/multipage/browsing-the-web.html#sandboxLinks) (or browsing contexts further nested inside it), [auxiliary browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#auxiliary-browsing-context) (which are protected by the [sandboxed auxiliary navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-auxiliary-navigation-browsing-context-flag) defined next), and the [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context) (which is protected by the [sandboxed top-level navigation without user activation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-top-level-navigation-without-user-activation-browsing-context-flag) and [sandboxed top-level navigation with user activation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-top-level-navigation-with-user-activation-browsing-context-flag) defined below).

If the [sandboxed auxiliary navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-auxiliary-navigation-browsing-context-flag) is not set, then in certain cases the restrictions nonetheless allow popups (new [top-level browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context)) to be opened. These [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) always have one permitted sandboxed navigator, set when the browsing context is created, which allows the [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) that created them to actually navigate them. (Otherwise, the [sandboxed navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-navigation-browsing-context-flag) would prevent them from being navigated even if they were opened.)

The sandboxed auxiliary navigation browsing context flag
This flag [prevents content from creating new auxiliary browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#sandboxWindowOpen), e.g. using the `target` attribute or the `window.open()` method.

The sandboxed top-level navigation without user activation browsing context flag
This flag [prevents content from navigating their top-level browsing context](https://html.spec.whatwg.org/multipage/browsing-the-web.html#sandboxLinks) and [prevents content from closing their top-level browsing context](https://html.spec.whatwg.org/multipage/nav-history-apis.html#sandboxClose). It is consulted only when the sandboxed browsing context's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#active-window) does not have [transient activation](https://html.spec.whatwg.org/multipage/interaction.html#transient-activation).

When the [sandboxed top-level navigation without user activation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-top-level-navigation-without-user-activation-browsing-context-flag) is _not_ set, content can navigate its [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context), but other [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) are still protected by the [sandboxed navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-navigation-browsing-context-flag) and possibly the [sandboxed auxiliary navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-auxiliary-navigation-browsing-context-flag).

The sandboxed top-level navigation with user activation browsing context flag
This flag [prevents content from navigating their top-level browsing context](https://html.spec.whatwg.org/multipage/browsing-the-web.html#sandboxLinks) and [prevents content from closing their top-level browsing context](https://html.spec.whatwg.org/multipage/nav-history-apis.html#sandboxClose). It is consulted only when the sandboxed browsing context's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#active-window) has [transient activation](https://html.spec.whatwg.org/multipage/interaction.html#transient-activation).

As with the [sandboxed top-level navigation without user activation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-top-level-navigation-without-user-activation-browsing-context-flag), this flag only affects the [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context); if it is not set, other [browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) might still be protected by other flags.

The sandboxed origin browsing context flag
This flag [forces content into an opaque origin](https://html.spec.whatwg.org/multipage/document-sequences.html#sandboxOrigin), thus preventing it from accessing other content from the same [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin).

This flag also [prevents script from reading from or writing to the `document.cookie` IDL attribute](https://html.spec.whatwg.org/multipage/dom.html#sandboxCookies), and blocks access to `localStorage`.

The sandboxed forms browsing context flag
This flag [blocks form submission](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#sandboxSubmitBlocked).

The sandboxed pointer lock browsing context flag
This flag disables the Pointer Lock API. [[POINTERLOCK]](https://html.spec.whatwg.org/multipage/references.html#refsPOINTERLOCK)

The sandboxed scripts browsing context flag
This flag [blocks script execution](https://html.spec.whatwg.org/multipage/webappapis.html#sandboxScriptBlocked).

The sandboxed automatic features browsing context flag
This flag blocks features that trigger automatically, such as [automatically playing a video](https://html.spec.whatwg.org/multipage/media.html#attr-media-autoplay) or [automatically focusing a form control](https://html.spec.whatwg.org/multipage/interaction.html#attr-fe-autofocus).

The sandboxed `document.domain` browsing context flag
This flag prevents content from using the `document.domain` setter.

The sandbox propagates to auxiliary browsing contexts flag
This flag prevents content from escaping the sandbox by ensuring that any [auxiliary browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#auxiliary-browsing-context) it creates inherits the content's [active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set).

The sandboxed modals flag
This flag prevents content from using any of the following features to produce modal dialogs:

*   `window.alert()`
*   `window.confirm()`
*   `window.print()`
*   `window.prompt()`
*   the `beforeunload` event

The sandboxed orientation lock browsing context flag
This flag disables the ability to lock the screen orientation. [[SCREENORIENTATION]](https://html.spec.whatwg.org/multipage/references.html#refsSCREENORIENTATION)

The sandboxed presentation browsing context flag
This flag disables the Presentation API. [[PRESENTATION]](https://html.spec.whatwg.org/multipage/references.html#refsPRESENTATION)

The sandboxed downloads browsing context flag
This flag prevents content from initiating or instantiating downloads, whether through [downloading hyperlinks](https://html.spec.whatwg.org/multipage/links.html#downloading-hyperlinks) or through [navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-as-a-download) that gets [handled as a download](https://html.spec.whatwg.org/multipage/links.html#handle-as-a-download).

The sandboxed custom protocols navigation browsing context flag
This flag prevents navigations toward non [fetch schemes](https://fetch.spec.whatwg.org/#fetch-scheme) from being [handed off to external software](https://html.spec.whatwg.org/multipage/browsing-the-web.html#hand-off-to-external-software).

When the user agent is to parse a sandboxing directive, given a string input and a [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set)output, it must run the following steps:

1.   [Split input on ASCII whitespace](https://infra.spec.whatwg.org/#split-on-ascii-whitespace), to obtain tokens.

2.   Let output be empty.

3.   Add the following flags to output:

    *   The [sandboxed navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-navigation-browsing-context-flag).

    *   The [sandboxed auxiliary navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-auxiliary-navigation-browsing-context-flag), unless tokens contains the `allow-popups` keyword.

    *   The [sandboxed top-level navigation without user activation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-top-level-navigation-without-user-activation-browsing-context-flag), unless tokens contains the `allow-top-navigation` keyword.

    *   The [sandboxed top-level navigation with user activation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-top-level-navigation-with-user-activation-browsing-context-flag), unless tokens contains either the `allow-top-navigation-by-user-activation` keyword or the `allow-top-navigation` keyword.

This means that if the `allow-top-navigation` is present, the `allow-top-navigation-by-user-activation` keyword will have no effect. For this reason, specifying both is a document conformance error.

    *   The [sandboxed origin browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-origin-browsing-context-flag), unless the tokens contains the `allow-same-origin` keyword.

The `allow-same-origin` keyword is intended for two cases.

First, it can be used to allow content from the same site to be sandboxed to disable scripting, while still allowing access to the DOM of the sandboxed content.

Second, it can be used to embed content from a third-party site, sandboxed to prevent that site from opening popups, etc, without preventing the embedded page from communicating back to its originating site, using the database APIs to store data, etc. 
    *   The [sandboxed forms browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-forms-browsing-context-flag), unless tokens contains the `allow-forms` keyword.

    *   The [sandboxed pointer lock browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-pointer-lock-browsing-context-flag), unless tokens contains the `allow-pointer-lock` keyword.

    *   The [sandboxed scripts browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-scripts-browsing-context-flag), unless tokens contains the `allow-scripts` keyword.

    *   The [sandboxed automatic features browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-automatic-features-browsing-context-flag), unless tokens contains the `allow-scripts` keyword (defined above).

This flag is relaxed by the same keyword as scripts, because when scripts are enabled these features are trivially possible anyway, and it would be unfortunate to force authors to use script to do them when sandboxed rather than allowing them to use the declarative features.

    *   The [sandboxed `document.domain` browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-document.domain-browsing-context-flag).

    *   The [sandbox propagates to auxiliary browsing contexts flag](https://html.spec.whatwg.org/multipage/browsers.html#sandbox-propagates-to-auxiliary-browsing-contexts-flag), unless tokens contains the `allow-popups-to-escape-sandbox` keyword.

    *   The [sandboxed modals flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-modals-flag), unless tokens contains the `allow-modals` keyword.

    *   The [sandboxed orientation lock browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-orientation-lock-browsing-context-flag), unless tokens contains the `allow-orientation-lock` keyword.

    *   The [sandboxed presentation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-presentation-browsing-context-flag), unless tokens contains the `allow-presentation` keyword.

    *   The [sandboxed downloads browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-downloads-browsing-context-flag), unless tokens contains the `allow-downloads` keyword.

    *   The [sandboxed custom protocols navigation browsing context flag](https://html.spec.whatwg.org/multipage/browsers.html#sandboxed-custom-protocols-navigation-browsing-context-flag), unless tokens contains either the `allow-top-navigation-to-custom-protocols` keyword, the `allow-popups` keyword, or the `allow-top-navigation` keyword.

* * *

Every [top-level browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-browsing-context) has a popup sandboxing flag set, which is a [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set). When a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) is created, its [popup sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#popup-sandboxing-flag-set) must be empty. It is populated by [the rules for choosing a navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#the-rules-for-choosing-a-navigable) and the [obtain a browsing context to use for a navigation response](https://html.spec.whatwg.org/multipage/browsers.html#obtain-browsing-context-navigation) algorithm.

Every `iframe` element has an `iframe` sandboxing flag set, which is a [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set). Which flags in an [`iframe` sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#iframe-sandboxing-flag-set) are set at any particular time is determined by the `iframe` element's `sandbox` attribute.

Every `Document` has an active sandboxing flag set, which is a [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set). When the `Document` is created, its [active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set) must be empty. It is populated by the [navigation algorithm](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate).

Every [CSP list](https://w3c.github.io/webappsec-csp/#csp-list)cspList has CSP-derived sandboxing flags, which is a [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set). It is the return value of the following algorithm:

1.   Let directives be an empty [ordered set](https://infra.spec.whatwg.org/#ordered-set).

2.   [For each](https://infra.spec.whatwg.org/#list-iterate) policy in cspList:

    1.   If policy's [disposition](https://w3c.github.io/webappsec-csp/#policy-disposition) is not "`enforce`", then [continue](https://infra.spec.whatwg.org/#iteration-continue).

    2.   If policy's [directive set](https://w3c.github.io/webappsec-csp/#policy-directive-set)[contains](https://infra.spec.whatwg.org/#list-contain) a [directive](https://w3c.github.io/webappsec-csp/#directives) whose name is "`sandbox`", then [append](https://infra.spec.whatwg.org/#list-append) that directive to directives.

3.   If directives is empty, then return an empty [sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set).

4.   Let directive be directives[directives's [size](https://infra.spec.whatwg.org/#list-size) − 1].

5.   Return the result of [parsing the sandboxing directive](https://html.spec.whatwg.org/multipage/browsers.html#parse-a-sandboxing-directive)directive.

* * *

To determine the creation sandboxing flags for a [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc)browsing context, given null or an element embedder, return the [union](https://infra.spec.whatwg.org/#set-union) of the flags that are present in the following [sandboxing flag sets](https://html.spec.whatwg.org/multipage/browsers.html#sandboxing-flag-set):

*   If embedder is null, then: the flags set on browsing context's [popup sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#popup-sandboxing-flag-set).

*   If embedder is an element, then: the flags set on embedder's [`iframe` sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#iframe-sandboxing-flag-set).

*   If embedder is an element, then: the flags set on embedder's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set).

#### 7.1.6`iframe` element referrer policy[](https://html.spec.whatwg.org/multipage/browsers.html#iframe-element-referrer-policy)

To determine the `iframe` element referrer policy given an element-or-null embedder:

1.   If embedder is an `iframe` element, then return embedder's `referrerpolicy` attribute's state's corresponding keyword.

2.   Return the empty string.

This is used for allowing masking of some [origins](https://dom.spec.whatwg.org/#concept-document-origin) in the [internal ancestor origin objects list creation steps](https://html.spec.whatwg.org/multipage/dom.html#internal-ancestor-origin-objects-list-creation-steps).

#### 7.1.7 Policy containers[](https://html.spec.whatwg.org/multipage/browsers.html#policy-containers)

A policy container is a [struct](https://infra.spec.whatwg.org/#struct) containing policies that apply to a `Document`, a `WorkerGlobalScope`, or a `WorkletGlobalScope`. It has the following [items](https://infra.spec.whatwg.org/#struct-item):

*   A CSP list, which is a [CSP list](https://w3c.github.io/webappsec-csp/#csp-list). It is initially empty.

*   An embedder policy, which is an [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy). It is initially a new [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#embedder-policy).

*   A referrer policy, which is a [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy). It is initially the [default referrer policy](https://w3c.github.io/webappsec-referrer-policy/#default-referrer-policy).

*   An integrity policy, which is an [integrity policy](https://w3c.github.io/webappsec-subresource-integrity/#integrity-policy), initially a new [integrity policy](https://w3c.github.io/webappsec-subresource-integrity/#integrity-policy).

*   A report only integrity policy, which is an [integrity policy](https://w3c.github.io/webappsec-subresource-integrity/#integrity-policy), initially a new [integrity policy](https://w3c.github.io/webappsec-subresource-integrity/#integrity-policy).

Move other policies into the policy container.

To clone a policy container given a [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container)policyContainer:

1.   Let clone be a new [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container).

2.   [For each](https://infra.spec.whatwg.org/#list-iterate)policy in policyContainer's [CSP list](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-csp-list), [append](https://infra.spec.whatwg.org/#list-append) a copy of policy into clone's [CSP list](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-csp-list).

3.   Set clone's [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-embedder-policy) to a copy of policyContainer's [embedder policy](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-embedder-policy).

4.   Set clone's [referrer policy](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-referrer-policy) to policyContainer's [referrer policy](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-referrer-policy).

5.   Set clone's [integrity policy](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-integrity-policy) to a copy of policyContainer's [integrity policy](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-integrity-policy).

6.   Return clone.

To determine whether a [URL](https://url.spec.whatwg.org/#concept-url)url requires storing the policy container in history:

1.   If url's [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is "`blob`", then return false.

2.   If url[is local](https://fetch.spec.whatwg.org/#is-local), then return true.

3.   Return false.

To determine navigation params policy container given a [URL](https://url.spec.whatwg.org/#concept-url)responseURL and four [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container)-or-nulls historyPolicyContainer, initiatorPolicyContainer, parentPolicyContainer, and responsePolicyContainer:

1.   If historyPolicyContainer is not null, then:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): responseURL[requires storing the policy container in history](https://html.spec.whatwg.org/multipage/browsers.html#requires-storing-the-policy-container-in-history).

    2.   Return a [clone](https://html.spec.whatwg.org/multipage/browsers.html#clone-a-policy-container) of historyPolicyContainer.

2.   If responseURL is `about:srcdoc`, then:

    1.   [Assert](https://infra.spec.whatwg.org/#assert): parentPolicyContainer is not null.

    2.   Return a [clone](https://html.spec.whatwg.org/multipage/browsers.html#clone-a-policy-container) of parentPolicyContainer.

3.   If responseURL[is local](https://fetch.spec.whatwg.org/#is-local) and initiatorPolicyContainer is not null, then return a [clone](https://html.spec.whatwg.org/multipage/browsers.html#clone-a-policy-container) of initiatorPolicyContainer.

4.   If responsePolicyContainer is not null, then return responsePolicyContainer.

5.   Return a new [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container).

To initialize a worker global scope's policy container given a `WorkerGlobalScope`workerGlobalScope, a [response](https://fetch.spec.whatwg.org/#concept-response)response, and an [environment](https://html.spec.whatwg.org/multipage/webappapis.html#environment)environment:

1.   If workerGlobalScope's [url](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-url)[is local](https://fetch.spec.whatwg.org/#is-local) but its [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is not "`blob`":

    1.   [Assert](https://infra.spec.whatwg.org/#assert): workerGlobalScope's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set)'s [size](https://infra.spec.whatwg.org/#list-size) is 1.

    2.   Set workerGlobalScope's [policy container](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-policy-container) to a [clone](https://html.spec.whatwg.org/multipage/browsers.html#clone-a-policy-container) of workerGlobalScope's [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set)[0]'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [policy container](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-policy-container).

2.   Otherwise, set workerGlobalScope's [policy container](https://html.spec.whatwg.org/multipage/workers.html#concept-workerglobalscope-policy-container) to the result of [creating a policy container from a fetch response](https://html.spec.whatwg.org/multipage/browsers.html#creating-a-policy-container-from-a-fetch-response) given response and environment.

[← 6.12 The popover attribute](https://html.spec.whatwg.org/multipage/popover.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [7.2 APIs related to navigation and session history →](https://html.spec.whatwg.org/multipage/nav-history-apis.html)
