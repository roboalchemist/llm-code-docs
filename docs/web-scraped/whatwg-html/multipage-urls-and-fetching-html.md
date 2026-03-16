# Source: https://html.spec.whatwg.org/multipage/urls-and-fetching.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/urls-and-fetching.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 2.3 Common microsyntaxes](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [2.6 Common DOM interfaces →](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html)
1.       1.   [2.4 URLs](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#urls)
        1.   [2.4.1 Terminology](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#terminology-2)
        2.   [2.4.2 Parsing URLs](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#resolving-urls)
        3.   [2.4.3 Document base URLs](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-urls)

    2.   [2.5 Fetching resources](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#fetching-resources)
        1.   [2.5.1 Terminology](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#terminology-3)
        2.   [2.5.2 Determining the type of a resource](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type-sniffing)
        3.   [2.5.3 Extracting character encodings from `meta` elements](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#extracting-character-encodings-from-meta-elements)
        4.   [2.5.4 CORS settings attributes](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cors-settings-attributes)
        5.   [2.5.5 Referrer policy attributes](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#referrer-policy-attributes)
        6.   [2.5.6 Nonce attributes](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#nonce-attributes)
        7.   [2.5.7 Lazy loading attributes](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-loading-attributes)
        8.   [2.5.8 Blocking attributes](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#blocking-attributes)
        9.   [2.5.9 Fetch priority attributes](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#fetch-priority-attributes)

### 2.4 URLs[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#urls)

#### 2.4.1 Terminology[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#terminology-2)

A string is a valid non-empty URL if it is a [valid URL string](https://url.spec.whatwg.org/#valid-url-string) but it is not the empty string.

* * *

This specification defines the URL `about:legacy-compat` as a reserved, though unresolvable, `about:` URL, for use in [DOCTYPE](https://html.spec.whatwg.org/multipage/syntax.html#syntax-doctype)s in [HTML documents](https://dom.spec.whatwg.org/#html-document) when needed for compatibility with XML tools. [[ABOUT]](https://html.spec.whatwg.org/multipage/references.html#refsABOUT)

This specification defines the URL `about:html-kind` as a reserved, though unresolvable, `about:` URL, that is used as an identifier for kinds of media tracks. [[ABOUT]](https://html.spec.whatwg.org/multipage/references.html#refsABOUT)

This specification defines the URL `about:srcdoc` as a reserved, though unresolvable, `about:` URL, that is used as the [URL](https://dom.spec.whatwg.org/#concept-document-url) of [`iframe``srcdoc` documents](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#an-iframe-srcdoc-document). [[ABOUT]](https://html.spec.whatwg.org/multipage/references.html#refsABOUT)

* * *

A [URL](https://url.spec.whatwg.org/#concept-url)matches `about:blank` if its [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is "`about`", its [path](https://url.spec.whatwg.org/#concept-url-path) contains a single string "`blank`", its [username](https://url.spec.whatwg.org/#concept-url-username) and [password](https://url.spec.whatwg.org/#concept-url-password) are the empty string, and its [host](https://url.spec.whatwg.org/#concept-url-host) is null.

Such a URL's [query](https://url.spec.whatwg.org/#concept-url-query) and [fragment](https://url.spec.whatwg.org/#concept-url-fragment) can be non-null. For example, the [URL record](https://url.spec.whatwg.org/#concept-url) created by [parsing](https://url.spec.whatwg.org/#concept-url-parser) "`about:blank?foo#bar`" [matches `about:blank`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#matches-about:blank).

A [URL](https://url.spec.whatwg.org/#concept-url)matches `about:srcdoc` if its [scheme](https://url.spec.whatwg.org/#concept-url-scheme) is "`about`", its [path](https://url.spec.whatwg.org/#concept-url-path) contains a single string "`srcdoc`", its [query](https://url.spec.whatwg.org/#concept-url-query) is null, its [username](https://url.spec.whatwg.org/#concept-url-username) and [password](https://url.spec.whatwg.org/#concept-url-password) are the empty string, and its [host](https://url.spec.whatwg.org/#concept-url-host) is null.

The reason that [matches `about:srcdoc`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#matches-about:srcdoc) ensures that the [URL](https://url.spec.whatwg.org/#concept-url)'s [query](https://url.spec.whatwg.org/#concept-url-query) is null is because it is not possible to create [an `iframe``srcdoc` document](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#an-iframe-srcdoc-document) whose [URL](https://dom.spec.whatwg.org/#concept-document-url) has a non-null [query](https://url.spec.whatwg.org/#concept-url-query), unlike `Document`s whose [URL](https://dom.spec.whatwg.org/#concept-document-url)[matches `about:blank`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#matches-about:blank). In other words, the set of all [URL](https://url.spec.whatwg.org/#concept-url)s that [match `about:srcdoc`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#matches-about:srcdoc) only vary in their [fragment](https://url.spec.whatwg.org/#concept-url-fragment).

#### 2.4.2 Parsing URLs[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#resolving-urls)

Parsing a URL is the process of taking a string and obtaining the [URL record](https://url.spec.whatwg.org/#concept-url) that it represents. While this process is defined in URL, the HTML standard defines several wrappers to abstract base URLs and encodings. [[URL]](https://html.spec.whatwg.org/multipage/references.html#refsURL)

Most new APIs are to use [parse a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#parse-a-url). Older APIs and HTML elements might have reason to use [encoding-parse a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url). When a custom base URL is needed or no base URL is desired, the [URL parser](https://url.spec.whatwg.org/#concept-url-parser) can of course be used directly as well.

To encoding-parse-and-serialize a URL, given a string url, relative to a `Document` object or [environment settings object](https://html.spec.whatwg.org/multipage/webappapis.html#environment-settings-object)environment, run these steps. They return failure or a string.

1.   Let url be the result of [encoding-parsing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url) given url, relative to environment.

2.   If url is failure, then return failure.

3.   Return the result of applying the [URL serializer](https://url.spec.whatwg.org/#concept-url-serializer) to url.

#### 2.4.3 Document base URLs[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#document-base-urls)

The fallback base URL of a `Document` object document is the [URL record](https://url.spec.whatwg.org/#concept-url) obtained by running these steps:

1.   If document is [an `iframe``srcdoc` document](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#an-iframe-srcdoc-document):

    1.   [Assert](https://infra.spec.whatwg.org/#assert): document's [about base URL](https://html.spec.whatwg.org/multipage/dom.html#concept-document-about-base-url) is non-null.

    2.   Return document's [about base URL](https://html.spec.whatwg.org/multipage/dom.html#concept-document-about-base-url).

2.   If document's [URL](https://dom.spec.whatwg.org/#concept-document-url)[matches `about:blank`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#matches-about:blank) and document's [about base URL](https://html.spec.whatwg.org/multipage/dom.html#concept-document-about-base-url) is non-null, then return document's [about base URL](https://html.spec.whatwg.org/multipage/dom.html#concept-document-about-base-url).

3.   Return document's [URL](https://dom.spec.whatwg.org/#concept-document-url).

* * *

To respond to base URL changes for a `Document`document:

1.   The user agent should update any user interface elements which are displaying affected URLs, or data derived from such URLs, to the user. Examples of such user interface elements would be a status bar that displays a [hyperlink](https://html.spec.whatwg.org/multipage/links.html#hyperlink)'s [url](https://html.spec.whatwg.org/multipage/links.html#concept-hyperlink-url), or some user interface which displays the URL specified by a `q`, `blockquote`, `ins`, or `del` element's `cite` attribute.

2.   Ensure that the CSS `:link`/`:visited`/etc. [pseudo-classes](https://drafts.csswg.org/selectors/#pseudo-class) are updated appropriately.

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)descendant of document's [shadow-including descendants](https://dom.spec.whatwg.org/#concept-shadow-including-descendant):

    1.   If descendant is a `script` element whose [result](https://html.spec.whatwg.org/multipage/scripting.html#concept-script-result) is a [speculation rules parse result](https://html.spec.whatwg.org/multipage/webappapis.html#speculation-rules-parse-result), then:

        1.   Let oldResult be element's [result](https://html.spec.whatwg.org/multipage/scripting.html#concept-script-result).

        2.   Let newResult be the result of [creating a speculation rules parse result](https://html.spec.whatwg.org/multipage/webappapis.html#create-a-speculation-rules-parse-result) given element's [child text content](https://dom.spec.whatwg.org/#concept-child-text-content) and element's [node document](https://dom.spec.whatwg.org/#concept-node-document).

        3.   [Update speculation rules](https://html.spec.whatwg.org/multipage/webappapis.html#update-speculation-rules) given element's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), oldResult, and newResult.

4.   [Consider speculative loads](https://html.spec.whatwg.org/multipage/speculative-loading.html#consider-speculative-loads) given document.

[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#example-base-url-change-img-unaffected)This means that changing the base URL doesn't affect, for example, the image displayed by `img` elements. Thus, subsequent accesses of the `src` IDL attribute from script will return a new [absolute URL](https://url.spec.whatwg.org/#syntax-url-absolute) that might no longer correspond to the image being shown.

### 2.5 Fetching resources[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#fetching-resources)

#### 2.5.1 Terminology[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#terminology-3)

A [response](https://fetch.spec.whatwg.org/#concept-response) whose [type](https://fetch.spec.whatwg.org/#concept-response-type) is "`basic`", "`cors`", or "`default`" is CORS-same-origin. [[FETCH]](https://html.spec.whatwg.org/multipage/references.html#refsFETCH)

A [response](https://fetch.spec.whatwg.org/#concept-response) whose [type](https://fetch.spec.whatwg.org/#concept-response-type) is "`opaque`" or "`opaqueredirect`" is CORS-cross-origin.

To create a potential-CORS request, given a url, destination, corsAttributeState, and an optional _same-origin fallback flag_, run these steps:

1.   Let mode be "`no-cors`" if corsAttributeState is [No CORS](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-crossorigin-none), and "`cors`" otherwise.

2.   If _same-origin fallback flag_ is set and mode is "`no-cors`", set mode to "`same-origin`".

3.   Let credentialsMode be "`include`".

4.   If corsAttributeState is [Anonymous](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-crossorigin-anonymous), set credentialsMode to "`same-origin`".

5.   Return a new [request](https://fetch.spec.whatwg.org/#concept-request) whose [URL](https://fetch.spec.whatwg.org/#concept-request-url) is url, [destination](https://fetch.spec.whatwg.org/#concept-request-destination) is destination, [mode](https://fetch.spec.whatwg.org/#concept-request-mode) is mode, [credentials mode](https://fetch.spec.whatwg.org/#concept-request-credentials-mode) is credentialsMode, and whose [use-URL-credentials flag](https://fetch.spec.whatwg.org/#concept-request-use-url-credentials-flag) is set.

#### 2.5.2 Determining the type of a resource[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type-sniffing)

The Content-Type metadata of a resource must be obtained and interpreted in a manner consistent with the requirements of MIME Sniffing. [[MIMESNIFF]](https://html.spec.whatwg.org/multipage/references.html#refsMIMESNIFF)

The [computed MIME type](https://mimesniff.spec.whatwg.org/#computed-mime-type) of a resource must be found in a manner consistent with the requirements given in MIME Sniffing. [[MIMESNIFF]](https://html.spec.whatwg.org/multipage/references.html#refsMIMESNIFF)

The [rules for sniffing images specifically](https://mimesniff.spec.whatwg.org/#rules-for-sniffing-images-specifically), the [rules for distinguishing if a resource is text or binary](https://mimesniff.spec.whatwg.org/#rules-for-text-or-binary), and the [rules for sniffing audio and video specifically](https://mimesniff.spec.whatwg.org/#rules-for-sniffing-audio-and-video-specifically) are also defined in MIME Sniffing. These rules return a [MIME type](https://mimesniff.spec.whatwg.org/#mime-type) as their result. [[MIMESNIFF]](https://html.spec.whatwg.org/multipage/references.html#refsMIMESNIFF)

It is imperative that the rules in MIME Sniffing be followed exactly. When a user agent uses different heuristics for content type detection than the server expects, security problems can occur. For more details, see MIME Sniffing. [[MIMESNIFF]](https://html.spec.whatwg.org/multipage/references.html#refsMIMESNIFF)

The , given a string s, is as follows. It returns either a character encoding or nothing.

1.   Let position be a pointer into s, initially pointing at the start of the string.

2.   _Loop_: Find the first seven characters in s after position that are an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the word "`charset`". If no such match is found, return nothing.

3.   Skip any [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace) that immediately follow the word "`charset`" (there might not be any).

4.   If the next character is not a U+003D EQUALS SIGN (=), then move position to point just before that next character, and jump back to the step labeled _loop_.

5.   Skip any [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace) that immediately follow the equals sign (there might not be any).

6.   Process the next character as follows:

If it is a U+0022 QUOTATION MARK character (") and there is a later U+0022 QUOTATION MARK character (") in s If it is a U+0027 APOSTROPHE character (') and there is a later U+0027 APOSTROPHE character (') in s Return the result of [getting an encoding](https://encoding.spec.whatwg.org/#concept-encoding-get) from the substring that is between this character and the next earliest occurrence of this character.If it is an unmatched U+0022 QUOTATION MARK character (")If it is an unmatched U+0027 APOSTROPHE character (')If there is no next character Return nothing.Otherwise Return the result of [getting an encoding](https://encoding.spec.whatwg.org/#concept-encoding-get) from the substring that consists of this character up to but not including the first [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace) or U+003B SEMICOLON character (;), or the end of s, whichever comes first.

This algorithm is distinct from those in the HTTP specifications (for example, HTTP doesn't allow the use of single quotes and requires supporting a backslash-escape mechanism that is not supported by this algorithm). While the algorithm is used in contexts that, historically, were related to HTTP, the syntax as supported by implementations diverged some time ago. [[HTTP]](https://html.spec.whatwg.org/multipage/references.html#refsHTTP)

#### 2.5.4 CORS settings attributes[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cors-settings-attributes)

[Attributes/crossorigin](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin "The crossorigin attribute, valid on the <audio>, <img>, <link>, <script>, and <video> elements, provides support for CORS, defining how the element handles cross-origin requests, thereby enabling the configuration of the CORS requests for the element's fetched data. Depending on the element, the attribute can be a CORS settings attribute.")

Support in all current engines.

Firefox 8+Safari 6+Chrome 13+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

A CORS settings attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | State | Brief description |
| --- | --- | --- |
| `anonymous` | Anonymous | [Requests](https://fetch.spec.whatwg.org/#concept-request) for the element will have their [mode](https://fetch.spec.whatwg.org/#concept-request-mode) set to "`cors`" and their [credentials mode](https://fetch.spec.whatwg.org/#concept-request-credentials-mode) set to "`same-origin`". |
| `use-credentials` | Use Credentials | [Requests](https://fetch.spec.whatwg.org/#concept-request) for the element will have their [mode](https://fetch.spec.whatwg.org/#concept-request-mode) set to "`cors`" and their [credentials mode](https://fetch.spec.whatwg.org/#concept-request-credentials-mode) set to "`include`". |

The majority of fetches governed by [CORS settings attributes](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cors-settings-attribute) will be done via the [create a potential-CORS request](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#create-a-potential-cors-request) algorithm.

For more modern features, where the request's [mode](https://fetch.spec.whatwg.org/#concept-request-mode) is always "`cors`", certain [CORS settings attributes](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cors-settings-attribute) have been repurposed to have a slightly different meaning, wherein they only impact the [request](https://fetch.spec.whatwg.org/#concept-request)'s [credentials mode](https://fetch.spec.whatwg.org/#concept-request-credentials-mode). To perform this translation, we define the CORS settings attribute credentials mode for a given [CORS settings attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cors-settings-attribute) to be determined by switching on the attribute's state:

[No CORS](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-crossorigin-none)[Anonymous](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-crossorigin-anonymous)"`same-origin`"[Use Credentials](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-crossorigin-none)"`include`"

#### 2.5.5 Referrer policy attributes[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#referrer-policy-attributes)

A referrer policy attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute). Each [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy), including the empty string, is a keyword for this attribute, mapping to a state of the same name.

The impact of these states on the processing model of various [fetches](https://fetch.spec.whatwg.org/#concept-fetch) is defined in more detail throughout this specification, in Fetch, and in Referrer Policy. [[FETCH]](https://html.spec.whatwg.org/multipage/references.html#refsFETCH)[[REFERRERPOLICY]](https://html.spec.whatwg.org/multipage/references.html#refsREFERRERPOLICY)

Several signals can contribute to which processing model is used for a given [fetch](https://fetch.spec.whatwg.org/#concept-fetch); a [referrer policy attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#referrer-policy-attribute) is only one of them. In general, the order in which these signals are processed are:

1.   First, the presence of a `noreferrer` link type;

2.   Then, the value of a [referrer policy attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#referrer-policy-attribute);

3.   Then, the presence of any `meta` element with `name` attribute set to `referrer`.

4.   Finally, the ``Referrer-Policy`` HTTP header.

#### 2.5.6 Nonce attributes[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#nonce-attributes)

[Global_attributes/nonce](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/nonce "The nonce global attribute is a content attribute defining a cryptographic nonce (\"number used once\") which can be used by Content Security Policy to determine whether or not a given fetch will be allowed to proceed for a given element.")

Support in all current engines.

Firefox 31+Safari Yes Chrome Yes

* * *

Opera?Edge Yes

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

A `nonce` content attribute represents a cryptographic nonce ("number used once") which can be used by Content Security Policy to determine whether or not a given fetch will be allowed to proceed. The value is text. [[CSP]](https://html.spec.whatwg.org/multipage/references.html#refsCSP)

Elements that have a `nonce` content attribute ensure that the cryptographic nonce is only exposed to script (and not to side-channels like CSS attribute selectors) by taking the value from the content attribute, moving it into an internal slot named [[CryptographicNonce]], exposing it to script via the `HTMLOrSVGElement` interface mixin, and setting the content attribute to the empty string. Unless otherwise specified, the slot's value is the empty string.

`element.nonce`
Returns the value set for element's cryptographic nonce. If the setter was not used, this will be the value originally found in the `nonce` content attribute.

`element.nonce = value`
Updates element's cryptographic nonce value.

[HTMLElement/nonce](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/nonce "The nonce property of the HTMLElement interface returns the cryptographic number used once that is used by Content Security Policy to determine whether a given fetch will be allowed to proceed.")

Firefox 75+Safari🔰 10+Chrome 61+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `nonce` IDL attribute must, on getting, return the value of this element's [[[CryptographicNonce]]](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cryptographicnonce); and on setting, set this element's [[[CryptographicNonce]]](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cryptographicnonce) to the given value.

[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#nonce-does-not-update-dom)Note how the setter for the `nonce` IDL attribute does not update the corresponding content attribute. This, as well as the below setting of the `nonce` content attribute to the empty string when an element [becomes browsing-context connected](https://html.spec.whatwg.org/multipage/infrastructure.html#becomes-browsing-context-connected), is meant to prevent exfiltration of the nonce value through mechanisms that can easily read content attributes, such as selectors. Learn more in [issue #2369](https://github.com/whatwg/html/issues/2369), where this behavior was introduced.

The following [attribute change steps](https://dom.spec.whatwg.org/#concept-element-attributes-change-ext) are used for the `nonce` content attribute:

1.   If element does not [include](https://webidl.spec.whatwg.org/#include)`HTMLOrSVGElement`, then return.

2.   If localName is not `nonce` or namespace is not null, then return.

3.   If value is null, then set element's [[[CryptographicNonce]]](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cryptographicnonce) to the empty string.

4.   Otherwise, set element's [[[CryptographicNonce]]](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cryptographicnonce) to value.

Whenever an element [including](https://webidl.spec.whatwg.org/#include)`HTMLOrSVGElement`[becomes browsing-context connected](https://html.spec.whatwg.org/multipage/infrastructure.html#becomes-browsing-context-connected), the user agent must execute the following steps on the element:

1.   Let CSP list be element's [shadow-including root](https://dom.spec.whatwg.org/#concept-shadow-including-root)'s [policy container](https://html.spec.whatwg.org/multipage/dom.html#concept-document-policy-container)'s [CSP list](https://html.spec.whatwg.org/multipage/browsers.html#policy-container-csp-list).

2.   If CSP list[contains a header-delivered Content Security Policy](https://w3c.github.io/webappsec-csp/#contains-a-header-delivered-content-security-policy), and element has a `nonce` content attribute whose value is not the empty string, then:

    1.   Let nonce be element's [[[CryptographicNonce]]](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cryptographicnonce).

    2.   [Set an attribute value](https://dom.spec.whatwg.org/#concept-element-attributes-set-value) for element using "`nonce`" and the empty string.

    3.   Set element's [[[CryptographicNonce]]](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cryptographicnonce) to nonce.

If element's [[[CryptographicNonce]]](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cryptographicnonce) were not restored it would be the empty string at this point.

#### 2.5.7 Lazy loading attributes[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-loading-attributes)

[Lazy_loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Lazy_loading "Lazy loading is a strategy to identify resources as non-blocking (non-critical) and load these only when needed. It's a way to shorten the length of the critical rendering path, which translates into reduced page load times.")

Support in all current engines.

Firefox 75+Safari 15.4+Chrome 77+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

A lazy loading attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | State | Brief description |
| --- | --- | --- |
| `lazy` | Lazy | Used to defer fetching a resource until some conditions are met. |
| `eager` | Eager | Used to fetch a resource immediately; the default state. |

The attribute directs the user agent to fetch a resource immediately or to defer fetching until some conditions associated with the element are met, according to the attribute's current state.

* * *

The will lazy load element steps, given an element element, are as follows:

1.   If [scripting is disabled](https://html.spec.whatwg.org/multipage/webappapis.html#concept-n-noscript) for element, then return false.

This is an anti-tracking measure, because if a user agent supported lazy loading when scripting is disabled, it would still be possible for a site to track a user's approximate scroll position throughout a session, by strategically placing images in a page's markup such that a server can track how many images are requested and when.

2.   If element's [lazy loading attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-loading-attribute) is in the [Lazy](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-loading-lazy-state) state, then return true.

3.   Return false.

Each `img` and `iframe` element has associated lazy load resumption steps, initially null.

For `img` and `iframe` elements that [will lazy load](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#will-lazy-load-element-steps), these steps are run from the [lazy load intersection observer](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-intersection-observer)'s callback or when their [lazy loading attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-loading-attribute) is set to the [Eager](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-loading-eager-state) state. This causes the element to continue loading.

Each `Document` has a lazy load intersection observer, initially set to null but can be set to an `IntersectionObserver` instance.

To start intersection-observing a lazy loading element element, run these steps:

1.   Let doc be element's [node document](https://dom.spec.whatwg.org/#concept-node-document).

2.   If doc's [lazy load intersection observer](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-intersection-observer) is null, set it to a new `IntersectionObserver` instance, initialized as follows:

The intention is to use the original value of the `IntersectionObserver` constructor. However, we're forced to use the JavaScript-exposed constructor in this specification, until Intersection Observer exposes low-level hooks for use in specifications. See bug [w3c/IntersectionObserver#464](https://github.com/w3c/IntersectionObserver/issues/464) which tracks this. [[INTERSECTIONOBSERVER]](https://html.spec.whatwg.org/multipage/references.html#refsINTERSECTIONOBSERVER)

    *   The callback is these steps, with arguments entries and observer:

        1.   For each entry in entries using a method of iteration which does not trigger developer-modifiable array accessors or iteration hooks:

            1.   Let resumptionSteps be null.

            2.   If entry.`isIntersecting` is true, then set resumptionSteps to entry.`target`'s [lazy load resumption steps](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-resumption-steps).

            3.   If resumptionSteps is null, then return.

            4.   [Stop intersection-observing a lazy loading element](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#stop-intersection-observing-a-lazy-loading-element) for entry.`target`.

            5.   Set entry.`target`'s [lazy load resumption steps](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-resumption-steps) to null.

            6.   Invoke resumptionSteps.

The intention is to use the original value of the `isIntersecting` and `target` getters. See [w3c/IntersectionObserver#464](https://github.com/w3c/IntersectionObserver/issues/464). [[INTERSECTIONOBSERVER]](https://html.spec.whatwg.org/multipage/references.html#refsINTERSECTIONOBSERVER)

    *   The options is an `IntersectionObserverInit` dictionary with the following dictionary members: «[ "`scrollMargin`" → [lazy load scroll margin](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-root-margin) ]»

This allows for fetching the image during scrolling, when it does not yet — but is about to — intersect the viewport.

The [lazy load scroll margin](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-root-margin) suggestions imply dynamic changes to the value, but the `IntersectionObserver` API does not support changing the scroll margin. See issue [w3c/IntersectionObserver#428](https://github.com/w3c/IntersectionObserver/issues/428).

3.   Call doc's [lazy load intersection observer](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-intersection-observer)'s `observe` method with element as the argument.

The intention is to use the original value of the `observe` method. See [w3c/IntersectionObserver#464](https://github.com/w3c/IntersectionObserver/issues/464). [[INTERSECTIONOBSERVER]](https://html.spec.whatwg.org/multipage/references.html#refsINTERSECTIONOBSERVER)

[![Image 2: (This is a tracking vector.)](https://resources.whatwg.org/tracking-vector.svg)](https://infra.spec.whatwg.org/#tracking-vector "There is a tracking vector here.") The lazy load scroll margin is an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) value, but with the following suggestions to consider:

*   Set a minimum value that most often results in the resources being loaded before they intersect the viewport under normal usage patterns for the given device.

*   The typical scrolling speed: increase the value for devices with faster typical scrolling speeds.

*   The current scrolling speed or momentum: the UA can attempt to predict where the scrolling will likely stop, and adjust the value accordingly.

*   The network quality: increase the value for slow or high-latency connections.

*   User preferences can influence the value.

It is important [for privacy](https://infra.spec.whatwg.org/#tracking-vector) that the [lazy load scroll margin](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-root-margin) not leak additional information. For example, the typical scrolling speed on the current device could be imprecise so as to not introduce a new fingerprinting vector.

#### 2.5.8 Blocking attributes[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#blocking-attributes)

A blocking attribute explicitly indicates that certain operations should be blocked on the fetching of an external resource. The operations that can be blocked are represented by possible blocking tokens, which are strings listed by the following table:

| Possible blocking token | Description |
| --- | --- |
| "`render`" | The element is [potentially render-blocking](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#potentially-render-blocking). |

[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#future-blocking-tokens)In the future, there might be more [possible blocking tokens](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#possible-blocking-token).

A [blocking attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#blocking-attribute) must have a value that is an [unordered set of unique space-separated tokens](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#unordered-set-of-unique-space-separated-tokens), each of which are [possible blocking tokens](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#possible-blocking-token). The [supported tokens](https://dom.spec.whatwg.org/#concept-supported-tokens) of a [blocking attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#blocking-attribute) are the [possible blocking tokens](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#possible-blocking-token). Any element can have at most one [blocking attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#blocking-attribute).

The blocking tokens set for an element el are the result of the following steps:

1.   Let value be the value of el's [blocking attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#blocking-attribute), or the empty string if no such attribute exists.

2.   Set value to value, [converted to ASCII lowercase](https://infra.spec.whatwg.org/#ascii-lowercase).

3.   Let rawTokens be the result of [splitting value on ASCII whitespace](https://infra.spec.whatwg.org/#split-on-ascii-whitespace).

4.   Return a set containing the elements of rawTokens that are [possible blocking tokens](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#possible-blocking-token).

An element is potentially render-blocking if its [blocking tokens set](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#blocking-tokens-set) contains "`render`", or if it is implicitly potentially render-blocking, which will be defined at the individual elements. By default, an element is not [implicitly potentially render-blocking](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#implicitly-potentially-render-blocking).

#### 2.5.9 Fetch priority attributes[](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#fetch-priority-attributes)

A fetch priority attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | State | Brief description |
| --- | --- | --- |
| `high` | High | Signals a high-priority [fetch](https://fetch.spec.whatwg.org/#concept-fetch) relative to other resources with the same [destination](https://fetch.spec.whatwg.org/#concept-request-destination). |
| `low` | Low | Signals a low-priority [fetch](https://fetch.spec.whatwg.org/#concept-fetch) relative to other resources with the same [destination](https://fetch.spec.whatwg.org/#concept-request-destination). |
| `auto` | Auto | Signals automatic determination of [fetch](https://fetch.spec.whatwg.org/#concept-fetch) priority relative to other resources with the same [destination](https://fetch.spec.whatwg.org/#concept-request-destination). |
[← 2.3 Common microsyntaxes](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [2.6 Common DOM interfaces →](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html)
