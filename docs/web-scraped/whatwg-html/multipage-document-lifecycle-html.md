# Source: https://html.spec.whatwg.org/multipage/document-lifecycle.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/document-lifecycle.html

Published Time: Mon, 16 Mar 2026 07:32:48 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 7.4 Navigation and session history](https://html.spec.whatwg.org/multipage/browsing-the-web.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [7.6 Speculative loading →](https://html.spec.whatwg.org/multipage/speculative-loading.html)
1.       1.   [7.5 Document lifecycle](https://html.spec.whatwg.org/multipage/document-lifecycle.html#document-lifecycle)
        1.   [7.5.1 Shared document creation infrastructure](https://html.spec.whatwg.org/multipage/document-lifecycle.html#shared-document-creation-infrastructure)
        2.   [7.5.2 Loading HTML documents](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-html)
        3.   [7.5.3 Loading XML documents](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-xml)
        4.   [7.5.4 Loading text documents](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-text)
        5.   [7.5.5 Loading `multipart/x-mixed-replace` documents](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-multipart-x-mixed-replace)
        6.   [7.5.6 Loading media documents](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-media)
        7.   [7.5.7 Loading a document for inline content that doesn't have a DOM](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-ua-inline)
        8.   [7.5.8 Finishing the loading process](https://html.spec.whatwg.org/multipage/document-lifecycle.html#loading-documents)
        9.   [7.5.9 Unloading documents](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unloading-documents)
        10.   [7.5.10 Destroying documents](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroying-documents)
        11.   [7.5.11 Aborting a document load](https://html.spec.whatwg.org/multipage/document-lifecycle.html#aborting-a-document-load)

### 7.5 Document lifecycle[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#document-lifecycle)

#### 7.5.1 Shared document creation infrastructure[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#shared-document-creation-infrastructure)

When loading a document using one of the below algorithms, we use the following steps to create and initialize a `Document` object, given a [type](https://dom.spec.whatwg.org/#concept-document-type)type, [content type](https://dom.spec.whatwg.org/#concept-document-content-type)contentType, and [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params)navigationParams:

`Document` objects are also created when [creating a new browsing context and document](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-browsing-context); such [initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank)`Document` are never created by this algorithm. Also, [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc)-less `Document` objects can be created via various APIs, such as `document.implementation.createHTMLDocument()`.

1.   Let browsingContext be the result of [obtaining a browsing context to use for a navigation response](https://html.spec.whatwg.org/multipage/browsers.html#obtain-browsing-context-navigation) given navigationParams.

This can result in a [browsing context group switch](https://html.spec.whatwg.org/multipage/browsers.html#browsing-context-group-switches-due-to-cross-origin-opener-policy), in which case browsingContext will be a [newly-created](https://html.spec.whatwg.org/multipage/document-sequences.html#creating-a-new-browsing-context)[browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#browsing-context) instead of being navigationParams's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable)'s [active browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-bc). In such a case, the created `Window`, `Document`, and [agent](https://tc39.es/ecma262/#sec-agents) will not end up being used; because the created `Document`'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is [opaque](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), we will end up creating a new [agent](https://tc39.es/ecma262/#sec-agents) and `Window`[later in this algorithm](https://html.spec.whatwg.org/multipage/document-lifecycle.html#create-new-agent-and-window) to go along with the new `Document`.

2.   Let permissionsPolicy be the result of [creating a permissions policy from a response](https://w3c.github.io/webappsec-feature-policy/#create-from-response) given navigationParams's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable)'s [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container), navigationParams's [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin), and navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response). [[PERMISSIONSPOLICY]](https://html.spec.whatwg.org/multipage/references.html#refsPERMISSIONSPOLICY)

3.   Let creationURL be navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [URL](https://fetch.spec.whatwg.org/#concept-response-url).

4.   If navigationParams's [request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request) is non-null, then set creationURL to navigationParams's [request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request)'s [current URL](https://fetch.spec.whatwg.org/#concept-request-current-url).

5.   Let window be null.

6.   If browsingContext's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [is initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank) is true, and browsingContext's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#active-document)'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is [same origin-domain](https://html.spec.whatwg.org/multipage/browsers.html#same-origin-domain) with navigationParams's [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin), then set window to browsingContext's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#active-window).

This means that both the [initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank)`Document`, and the new `Document` that is about to be created, will share the same `Window` object.

7.   Otherwise:

    1.   Let oacHeader be the result of [getting a structured field value](https://fetch.spec.whatwg.org/#concept-header-list-get-structured-header) given ``Origin-Agent-Cluster`` and "`item`" from navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [header list](https://fetch.spec.whatwg.org/#concept-response-header-list).

    2.   Let requestsOAC be true if oacHeader is not null and oacHeader[0] is the [boolean](https://httpwg.org/specs/rfc8941.html#boolean) true; otherwise false.

    3.   If navigationParams's [reserved environment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-reserved-environment) is a [non-secure context](https://html.spec.whatwg.org/multipage/webappapis.html#non-secure-context), then set requestsOAC to false.

    4.   Let agent be the result of [obtaining a similar-origin window agent](https://html.spec.whatwg.org/multipage/webappapis.html#obtain-similar-origin-window-agent) given navigationParams's [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin), browsingContext's [group](https://html.spec.whatwg.org/multipage/document-sequences.html#tlbc-group), and requestsOAC.

    5.   Let realmExecutionContext be the result of [creating a new realm](https://html.spec.whatwg.org/multipage/webappapis.html#creating-a-new-javascript-realm) given agent and the following customizations:

        *   For the global object, create a new `Window` object.

        *   For the global **this** binding, use browsingContext's `WindowProxy` object.

    6.   Set window to the [global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-realm-global) of realmExecutionContext's Realm component.

    7.   Let topLevelCreationURL be creationURL.

    8.   Let topLevelOrigin be navigationParams's [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin).

    9.   If navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container) is not null, then:

        1.   Let parentEnvironment be navigable's [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object).

        2.   Set topLevelCreationURL to parentEnvironment's [top-level creation URL](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-creation-url).

        3.   Set topLevelOrigin to parentEnvironment's [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin).

    10.   [Set up a window environment settings object](https://html.spec.whatwg.org/multipage/nav-history-apis.html#set-up-a-window-environment-settings-object) with creationURL, realmExecutionContext, navigationParams's [reserved environment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-reserved-environment), topLevelCreationURL, and topLevelOrigin.

This is the usual case, where the new `Document` we're about to create gets a new `Window` to go along with it.

8.   Let loadTimingInfo be a new [document load timing info](https://html.spec.whatwg.org/multipage/dom.html#document-load-timing-info) with its [navigation start time](https://html.spec.whatwg.org/multipage/dom.html#navigation-start-time) set to navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [timing info](https://fetch.spec.whatwg.org/#concept-response-timing-info)'s [start time](https://fetch.spec.whatwg.org/#fetch-timing-info-start-time).

9.   Let document be a new `Document`, with

[type](https://dom.spec.whatwg.org/#concept-document-type)type[content type](https://dom.spec.whatwg.org/#concept-document-content-type)contentType[origin](https://dom.spec.whatwg.org/#concept-document-origin)navigationParams's [origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin)[browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc)browsingContext[policy container](https://html.spec.whatwg.org/multipage/dom.html#concept-document-policy-container)navigationParams's [policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-policy-container)[permissions policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-permissions-policy)permissionsPolicy[active sandboxing flag set](https://html.spec.whatwg.org/multipage/browsers.html#active-sandboxing-flag-set)navigationParams's [final sandboxing flag set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-sandboxing)[opener policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-coop)navigationParams's [cross-origin opener policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop)[load timing info](https://html.spec.whatwg.org/multipage/dom.html#load-timing-info)loadTimingInfo[was created via cross-origin redirects](https://html.spec.whatwg.org/multipage/dom.html#was-created-via-cross-origin-redirects)navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [has cross-origin redirects](https://fetch.spec.whatwg.org/#response-has-cross-origin-redirects)[during-loading navigation ID for WebDriver BiDi](https://html.spec.whatwg.org/multipage/dom.html#concept-document-navigation-id)navigationParams's [id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-id)[URL](https://dom.spec.whatwg.org/#concept-document-url)creationURL[current document readiness](https://html.spec.whatwg.org/multipage/dom.html#current-document-readiness)"`loading`"[about base URL](https://html.spec.whatwg.org/multipage/dom.html#concept-document-about-base-url)navigationParams's [about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-about-base-url)[allow declarative shadow roots](https://dom.spec.whatwg.org/#concept-document-allow-declarative-shadow-roots)true[custom element registry](https://dom.spec.whatwg.org/#document-custom-element-registry)a new `CustomElementRegistry` object
10.   Set window's [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window) to document.

11.   Set document's [internal ancestor origin objects list](https://html.spec.whatwg.org/multipage/dom.html#concept-document-internal-ancestor-origin-objects-list) to the result of running the [internal ancestor origin objects list creation steps](https://html.spec.whatwg.org/multipage/dom.html#internal-ancestor-origin-objects-list-creation-steps) given document and navigationParams's [`iframe` element referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-iframe-referrer-policy).

12.   Set document's [ancestor origins list](https://html.spec.whatwg.org/multipage/dom.html#concept-document-ancestor-origins-list) to the result of running the [ancestor origins list creation steps](https://html.spec.whatwg.org/multipage/dom.html#ancestor-origins-list-creation-steps) given document.

13.   [Run CSP initialization for a `Document`](https://w3c.github.io/webappsec-csp/#run-document-csp-initialization) given document. [[CSP]](https://html.spec.whatwg.org/multipage/references.html#refsCSP)

14.   If navigationParams's [request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request) is non-null, then:

    1.   Set document's [referrer](https://html.spec.whatwg.org/multipage/dom.html#the-document's-referrer) to the empty string.

    2.   Let referrer be navigationParams's [request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request)'s [referrer](https://fetch.spec.whatwg.org/#concept-request-referrer).

    3.   If referrer is a [URL record](https://url.spec.whatwg.org/#concept-url), then set document's [referrer](https://html.spec.whatwg.org/multipage/dom.html#the-document's-referrer) to the [serialization](https://url.spec.whatwg.org/#concept-url-serializer) of referrer.

Per Fetch, referrer will be either a [URL record](https://url.spec.whatwg.org/#concept-url) or "`no-referrer`" at this point.

15.   If navigationParams's [fetch controller](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-fetch-controller) is not null, then:

    1.   Let fullTimingInfo be the result of [extracting the full timing info](https://fetch.spec.whatwg.org/#extract-full-timing-info) from navigationParams's [fetch controller](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-fetch-controller).

    2.   Let redirectCount be 0 if navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [has cross-origin redirects](https://fetch.spec.whatwg.org/#response-has-cross-origin-redirects) is true; otherwise navigationParams's [request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request)'s [redirect count](https://fetch.spec.whatwg.org/#concept-request-redirect-count).

    3.   [Create the navigation timing entry](https://w3c.github.io/navigation-timing/#dfn-create-the-navigation-timing-entry) for document, given fullTimingInfo, redirectCount, navigationTimingType, navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [service worker timing info](https://fetch.spec.whatwg.org/#response-service-worker-timing-info), and navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [body info](https://fetch.spec.whatwg.org/#concept-response-body-info).

16.   [Create the navigation timing entry](https://w3c.github.io/navigation-timing/#dfn-create-the-navigation-timing-entry) for document, with navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [timing info](https://fetch.spec.whatwg.org/#concept-response-timing-info), redirectCount, navigationParams's [navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-nav-timing-type), and navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)'s [service worker timing info](https://fetch.spec.whatwg.org/#response-service-worker-timing-info).

17.   If navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response) has a ``Refresh`` header, then:

    1.   Let value be the [isomorphic decoding](https://infra.spec.whatwg.org/#isomorphic-decode) of the value of the header.

    2.   Run the [shared declarative refresh steps](https://html.spec.whatwg.org/multipage/semantics.html#shared-declarative-refresh-steps) with document and value.

We do not currently have a spec for how to handle multiple ``Refresh`` headers. This is tracked as [issue #2900](https://github.com/whatwg/html/issues/2900).

18.   If navigationParams's [commit early hints](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-commit-early-hints) is not null, then call navigationParams's [commit early hints](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-commit-early-hints) with document.

19.   [Process link headers](https://html.spec.whatwg.org/multipage/semantics.html#process-link-headers) given document, navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response), and "`pre-media`".

20.   If navigationParams's [navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable) is a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable), then [process the ``Speculation-Rules`` header](https://html.spec.whatwg.org/multipage/speculative-loading.html#process-the-speculation-rules-header) given document and navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response).

This is conditional because [speculative loads are only considered for top-level traversables](https://html.spec.whatwg.org/multipage/speculative-loading.html#step-consider-speculative-loads-top-level-only), so it would be wasteful to fetch these rules otherwise.

21.   [Potentially free deferred fetch quota](https://fetch.spec.whatwg.org/#potentially-free-deferred-fetch-quota) for document.

22.   Return document.

In this example, the child document is not allowed to use `PaymentRequest`, despite being [same origin-domain](https://html.spec.whatwg.org/multipage/browsers.html#same-origin-domain) at the time the child document tries to use it. At the time the child document is initialized, only the parent document has set `document.domain`, and the child document has not.

```
<!-- https://foo.example.com/a.html -->
<!doctype html>
<script>
document.domain = 'example.com';
</script>
<iframe src=b.html></iframe>
```

```
<!-- https://bar.example.com/b.html -->
<!doctype html>
<script>
document.domain = 'example.com'; // This happens after the document is initialized
new PaymentRequest(…); // Not allowed to use
</script>
```

In this example, the child document _is_ allowed to use `PaymentRequest`, despite not being [same origin-domain](https://html.spec.whatwg.org/multipage/browsers.html#same-origin-domain) at the time the child document tries to use it. At the time the child document is initialized, none of the documents have set `document.domain` yet so [same origin-domain](https://html.spec.whatwg.org/multipage/browsers.html#same-origin-domain) falls back to a normal [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) check.

```
<!-- https://example.com/a.html -->
<!doctype html>
<iframe src=b.html></iframe>
<!-- The child document is now initialized, before the script below is run. -->
<script>
document.domain = 'example.com';
</script>
```

```
<!-- https://example.com/b.html -->
<!doctype html>
<script>
new PaymentRequest(…); // Allowed to use
</script>
```

#### 7.5.2 Loading HTML documents[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-html)

To load an HTML document, given [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params)navigationParams:

1.   Let document be the result of [creating and initializing a `Document` object](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object) given "`html`", "`text/html`", and navigationParams.

2.   If document's [URL](https://dom.spec.whatwg.org/#concept-document-url) is `about:blank`, then [populate with `html`/`head`/`body`](https://html.spec.whatwg.org/multipage/document-lifecycle.html#populate-with-html/head/body) given document.

This special case, where even non-[initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank)`Document`s are synchronously given their element nodes, is necessary for compatible with deployed content. In other words, it is not compatible to instead go down the "otherwise" branch and feed the empty [byte sequence](https://infra.spec.whatwg.org/#byte-sequence) into an [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) to asynchronously populate document.

3.   Otherwise, create an [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) and associate it with the document. Each [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) places on the [task queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue) while fetching runs must then fill the parser's [input byte stream](https://html.spec.whatwg.org/multipage/parsing.html#the-input-byte-stream) with the fetched bytes and cause the [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) to perform the appropriate processing of the input stream.

The first [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) places on the [task queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue) while fetching runs must [process link headers](https://html.spec.whatwg.org/multipage/semantics.html#process-link-headers) given document, navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response), and "`media`", after the task has been processed by the [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser).

Before any script execution occurs, the user agent must wait for [scripts may run for the newly-created document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scripts-may-run-for-the-newly-created-document) to be true for document.

The [input byte stream](https://html.spec.whatwg.org/multipage/parsing.html#the-input-byte-stream) converts bytes into characters for use in the [tokenizer](https://html.spec.whatwg.org/multipage/parsing.html#tokenization). This process relies, in part, on character encoding information found in the real [Content-Type metadata](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type) of the resource; the computed type is not used for this purpose.

When no more bytes are available, the user agent must [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to have the parser process the implied EOF character, which eventually causes a `load` event to be fired.

4.   Return document.

#### 7.5.3 Loading XML documents[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-xml)

When faced with displaying an XML file inline, provided [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params)navigationParams and a string type, user agents must follow the requirements defined in XML and Namespaces in XML, XML Media Types, DOM, and other relevant specifications to [create and initialize a `Document` object](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object)document, given "`xml`", type, and navigationParams, and return that `Document`. They must also create a corresponding [XML parser](https://html.spec.whatwg.org/multipage/xhtml.html#xml-parser). [[XML]](https://html.spec.whatwg.org/multipage/references.html#refsXML)[[XMLNS]](https://html.spec.whatwg.org/multipage/references.html#refsXMLNS)[[RFC7303]](https://html.spec.whatwg.org/multipage/references.html#refsRFC7303)[[DOM]](https://html.spec.whatwg.org/multipage/references.html#refsDOM)

At the time of writing, the XML specification community had not actually yet specified how XML and the DOM interact.

The first [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) places on the [task queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue) while fetching runs must [process link headers](https://html.spec.whatwg.org/multipage/semantics.html#process-link-headers) given document, navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response), and "`media`", after the task has been processed by the [XML parser](https://html.spec.whatwg.org/multipage/xhtml.html#xml-parser).

The actual HTTP headers and other metadata, not the headers as mutated or implied by the algorithms given in this specification, are the ones that must be used when determining the character encoding according to the rules given in the above specifications. Once the character encoding is established, the [document's character encoding](https://dom.spec.whatwg.org/#concept-document-encoding) must be set to that character encoding.

Before any script execution occurs, the user agent must wait for [scripts may run for the newly-created document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scripts-may-run-for-the-newly-created-document) to be true for the newly-created `Document`.

Once parsing is complete, the user agent must set document's [during-loading navigation ID for WebDriver BiDi](https://html.spec.whatwg.org/multipage/dom.html#concept-document-navigation-id) to null.

For HTML documents this is reset when parsing is complete, after firing the load event.

Error messages from the parse process (e.g., XML namespace well-formedness errors) may be reported inline by mutating the `Document`.

#### 7.5.4 Loading text documents[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-text)

To load a text document, given a [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params)navigationParams and a string type:

1.   Let document be the result of [creating and initializing a `Document` object](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object) given "`html`", type, and navigationParams.

2.   Set document's [parser cannot change the mode flag](https://html.spec.whatwg.org/multipage/parsing.html#parser-cannot-change-the-mode-flag) to true.

3.   Set document's [mode](https://dom.spec.whatwg.org/#concept-document-mode) to "`no-quirks`".

4.   Create an [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) and associate it with the document. Act as if the tokenizer had emitted a start tag token with the tag name "pre" followed by a single U+000A LINE FEED (LF) character, and switch the [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser)'s tokenizer to the [PLAINTEXT state](https://html.spec.whatwg.org/multipage/parsing.html#plaintext-state). Each [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) places on the [task queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue) while fetching runs must then fill the parser's [input byte stream](https://html.spec.whatwg.org/multipage/parsing.html#the-input-byte-stream) with the fetched bytes and cause the [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) to perform the appropriate processing of the input stream.

document's [encoding](https://dom.spec.whatwg.org/#concept-document-encoding) must be set to the character encoding used to decode the document during parsing.

The first [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) places on the [task queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue) while fetching runs must [process link headers](https://html.spec.whatwg.org/multipage/semantics.html#process-link-headers) given document, navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response), and "`media`", after the task has been processed by the [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser).

Before any script execution occurs, the user agent must wait for [scripts may run for the newly-created document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#scripts-may-run-for-the-newly-created-document) to be true for document.

When no more bytes are available, the user agent must [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to have the parser process the implied EOF character, which eventually causes a `load` event to be fired.

5.   User agents may add content to the `head` element of document, e.g., linking to a style sheet, providing script, or giving the document a `title`.

In particular, if the user agent supports the `Format=Flowed` feature of RFC 3676 then the user agent would need to apply extra styling to cause the text to wrap correctly and to handle the quoting feature. This could be performed using, e.g., a CSS extension.

6.   Return document.

The rules for how to convert the bytes of the plain text document into actual characters, and the rules for actually rendering the text to the user, are defined by the specifications for the [computed MIME type](https://mimesniff.spec.whatwg.org/#computed-mime-type) of the resource (i.e., type).

#### 7.5.5 Loading `multipart/x-mixed-replace` documents[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-multipart-x-mixed-replace)

For the purposes of algorithms processing these body parts as if they were complete stand-alone resources, the user agent must act as if there were no more bytes for those resources whenever the boundary following the body part is reached.

Thus, `load` events (and for that matter `unload` events) do fire for each body part loaded.

#### 7.5.6 Loading media documents[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-media)

To load a media document, given navigationParams and a string type:

1.   Let document be the result of [creating and initializing a `Document` object](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object) given "`html`", type, and navigationParams.

2.   Set document's [mode](https://dom.spec.whatwg.org/#concept-document-mode) to "`no-quirks`".

3.   [Populate with `html`/`head`/`body`](https://html.spec.whatwg.org/multipage/document-lifecycle.html#populate-with-html/head/body) given document.

4.   Append an element host element for the media, as described below, to the `body` element.

5.   Set the appropriate attribute of the element host element, as described below, to the address of the image, video, or audio resource.

6.   User agents may add content to the `head` element of document, or attributes to host element, e.g., to link to a style sheet, to provide a script, to give the document a `title`, or to make the media [autoplay](https://html.spec.whatwg.org/multipage/media.html#attr-media-autoplay).

7.   [Process link headers](https://html.spec.whatwg.org/multipage/semantics.html#process-link-headers) given document, navigationParams's [response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response), and "`media`".

8.   Act as if the user agent had [stopped parsing](https://html.spec.whatwg.org/multipage/parsing.html#stop-parsing)document.

9.   Return document.

The element host element to create for the media is the element given in the table below in the second cell of the row whose first cell describes the media. The appropriate attribute to set is the one given by the third cell in that same row.

| Type of media | Element for the media | Appropriate attribute |
| --- | --- | --- |
| Image | `img` | `src` |
| Video | `video` | `src` |
| Audio | `audio` | `src` |

#### 7.5.7 Loading a document for inline content that doesn't have a DOM[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#read-ua-inline)

When the user agent is to create a document to display a user agent page or PDF viewer inline, provided a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable, a [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id)navigationId, a `NavigationTimingType`navTimingType, and a [user navigation involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#user-navigation-involvement)userInvolvement, the user agent should:

1.   Let origin be a new [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque).

2.   Let coop be a new [opener policy](https://html.spec.whatwg.org/multipage/browsers.html#cross-origin-opener-policy).

3.   Let coopEnforcementResult be a new [opener policy enforcement result](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-result) with

[url](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-url)response's [URL](https://fetch.spec.whatwg.org/#concept-response-url)[origin](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-origin)origin[opener policy](https://html.spec.whatwg.org/multipage/browsers.html#coop-enforcement-coop)coop
4.   Let navigationParams be a new [navigation params](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params) with

[id](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-id)navigationId[navigable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-navigable)navigable[request](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-request)null[response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-response)a new [response](https://fetch.spec.whatwg.org/#concept-response)[origin](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-origin)origin[fetch controller](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-fetch-controller)null[commit early hints](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-commit-early-hints)null[COOP enforcement result](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop-enforcement-result)coopEnforcementResult[reserved environment](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-reserved-environment)null[policy container](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-policy-container)a new [policy container](https://html.spec.whatwg.org/multipage/browsers.html#policy-container)[final sandboxing flag set](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-sandboxing)an empty set[`iframe` element referrer policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-iframe-referrer-policy)the empty string[opener policy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-coop)coop[navigation timing type](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-nav-timing-type)navTimingType[about base URL](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-about-base-url)null[user involvement](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-params-user-involvement)userInvolvement
5.   Let document be the result of [creating and initializing a `Document` object](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object) given "`html`", "`text/html`", and navigationParams.

6.   Either associate document with a custom rendering that is not rendered using the normal `Document` rendering rules, or mutate document until it represents the content the user agent wants to render.

7.   Act as if the user agent had [stopped parsing](https://html.spec.whatwg.org/multipage/parsing.html#stop-parsing)document.

8.   Return document.

Because we ensure the resulting `Document`'s [origin](https://dom.spec.whatwg.org/#concept-document-origin) is [opaque](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), and the resulting `Document` cannot run script with access to the DOM, the existence and properties of this `Document` are not observable to web developer code. This means that most of the above values, e.g., the `text/html`[type](https://dom.spec.whatwg.org/#concept-document-type), do not matter. Similarly, most of the items in navigationParams don't have any observable effect, besides preventing the [`Document`-creation algorithm](https://html.spec.whatwg.org/multipage/document-lifecycle.html#initialise-the-document-object) from getting confused, and so are set to default values.

#### 7.5.8 Finishing the loading process[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#loading-documents)

A `Document` has a completely loaded time (a time or null), which is initially null.

A `Document` is considered completely loaded if its [completely loaded time](https://html.spec.whatwg.org/multipage/document-lifecycle.html#completely-loaded-time) is non-null.

To completely finish loading a `Document`document:

1.   [Assert](https://infra.spec.whatwg.org/#assert): document's [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc) is non-null.

2.   Set document's [completely loaded time](https://html.spec.whatwg.org/multipage/document-lifecycle.html#completely-loaded-time) to the current time.

3.   Let container be document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [container](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-container).

4.   If container is an `iframe` element, then [queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given container to run the [iframe load event steps](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-load-event-steps) given container.

5.   Otherwise, if container is non-null, then [queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given container to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `load` at container.

#### 7.5.9 Unloading documents[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unloading-documents)

A `Document` has a _salvageable_ state, which must initially be true, and a page showing boolean, which is initially false. The [page showing](https://html.spec.whatwg.org/multipage/document-lifecycle.html#page-showing) boolean is used to ensure that scripts receive `pageshow` and `pagehide` events in a consistent manner (e.g., that they never receive two `pagehide` events in a row without an intervening `pageshow`, or vice versa).

A `Document` has a `DOMHighResTimeStamp`suspension time, initially 0.

A `Document` has a [list](https://infra.spec.whatwg.org/#list) of suspended timer handles, initially empty.

[Event loops](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop) have a termination nesting level counter, which must initially be 0.

`Document` objects have an unload counter, which is used to ignore certain operations while the below algorithms run. Initially, the counter must be set to zero.

To unload a `Document`oldDocument, given an optional `Document`newDocument:

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running as part of a [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) queued on oldDocument's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop).

2.   Let unloadTimingInfo be a new [document unload timing info](https://html.spec.whatwg.org/multipage/dom.html#document-unload-timing-info).

3.   If newDocument is not given, then set unloadTimingInfo to null.

In this case there is no new document that needs to know about how long it took oldDocument to unload.

4.   Otherwise, if newDocument's [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop) is not oldDocument's [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop), then the user agent may be [unloading](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-a-document)oldDocument[in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel). In that case, the user agent should set unloadTimingInfo to null.

In this case newDocument's loading is not impacted by how long it takes to unload oldDocument, so it would be meaningless to communicate that timing info.

5.   Let intendToKeepInBfcache be true if the user agent intends to keep oldDocument alive in a [session history entry](https://html.spec.whatwg.org/multipage/browsing-the-web.html#session-history-entry), such that it can later be [used for history traversal](https://html.spec.whatwg.org/multipage/browsing-the-web.html#note-bfcache).

This must be false if oldDocument is not _[salvageable](https://html.spec.whatwg.org/multipage/document-lifecycle.html#concept-document-salvageable)_, or if there are any descendants of oldDocument which the user agent does not intend to keep alive in the same way (including due to their lack of _[salvageability](https://html.spec.whatwg.org/multipage/document-lifecycle.html#concept-document-salvageable)_).

6.   Let eventLoop be oldDocument's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop).

7.   Increase eventLoop's [termination nesting level](https://html.spec.whatwg.org/multipage/document-lifecycle.html#termination-nesting-level) by 1.

8.   Increase oldDocument's [unload counter](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-counter) by 1.

9.   If intendToKeepInBfcache is false, then set oldDocument's _[salvageable](https://html.spec.whatwg.org/multipage/document-lifecycle.html#concept-document-salvageable)_ state to false.

10.   If oldDocument's [page showing](https://html.spec.whatwg.org/multipage/document-lifecycle.html#page-showing) is true:

    1.   Set oldDocument's [page showing](https://html.spec.whatwg.org/multipage/document-lifecycle.html#page-showing) to false.

    2.   [Fire a page transition event](https://html.spec.whatwg.org/multipage/nav-history-apis.html#fire-a-page-transition-event) named `pagehide` at oldDocument's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) with oldDocument's _[salvageable](https://html.spec.whatwg.org/multipage/document-lifecycle.html#concept-document-salvageable)_ state.

    3.   [Update the visibility state](https://html.spec.whatwg.org/multipage/interaction.html#update-the-visibility-state) of oldDocument to "`hidden`".

11.   If unloadTimingInfo is not null, then set unloadTimingInfo's [unload event start time](https://html.spec.whatwg.org/multipage/dom.html#unload-event-start-time) to the [current high resolution time](https://w3c.github.io/hr-time/#dfn-current-high-resolution-time) given newDocument's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), [coarsened](https://w3c.github.io/hr-time/#dfn-coarsen-time) given oldDocument's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-cross-origin-isolated-capability).

12.   If oldDocument's _[salvageable](https://html.spec.whatwg.org/multipage/document-lifecycle.html#concept-document-salvageable)_ state is false, then [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `unload` at oldDocument's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), with _legacy target override flag_ set.

13.   If unloadTimingInfo is not null, then set unloadTimingInfo's [unload event end time](https://html.spec.whatwg.org/multipage/dom.html#unload-event-end-time) to the [current high resolution time](https://w3c.github.io/hr-time/#dfn-current-high-resolution-time) given newDocument's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), [coarsened](https://w3c.github.io/hr-time/#dfn-coarsen-time) given oldDocument's [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object)'s [cross-origin isolated capability](https://html.spec.whatwg.org/multipage/webappapis.html#concept-settings-object-cross-origin-isolated-capability).

14.   Decrease eventLoop's [termination nesting level](https://html.spec.whatwg.org/multipage/document-lifecycle.html#termination-nesting-level) by 1.

15.   Set oldDocument's [suspension time](https://html.spec.whatwg.org/multipage/document-lifecycle.html#suspension-time) to the [current high resolution time](https://w3c.github.io/hr-time/#dfn-current-high-resolution-time) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global).

16.   Set oldDocument's [suspended timer handles](https://html.spec.whatwg.org/multipage/document-lifecycle.html#suspended-timer-handles) to the result of [getting the keys](https://infra.spec.whatwg.org/#map-getting-the-keys) for the [map of active timers](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-active-timers).

17.   Set oldDocument's [has been scrolled by the user](https://html.spec.whatwg.org/multipage/browsing-the-web.html#has-been-scrolled-by-the-user) to false.

18.   Run any [unloading document cleanup steps](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unloading-document-cleanup-steps) for oldDocument that are defined by this specification and [other applicable specifications](https://html.spec.whatwg.org/multipage/infrastructure.html#other-applicable-specifications).

19.   If oldDocument's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) is a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable), [build not restored reasons for a top-level traversable and its descendants](https://html.spec.whatwg.org/multipage/browsing-the-web.html#build-not-restored-reasons-for-a-top-level-traversable-and-its-descendants) given oldDocument's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable).

20.   If oldDocument's _[salvageable](https://html.spec.whatwg.org/multipage/document-lifecycle.html#concept-document-salvageable)_ state is false, then [destroy](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document)oldDocument.

21.   Decrease oldDocument's [unload counter](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-counter) by 1.

22.   If newDocument is given, newDocument's [was created via cross-origin redirects](https://html.spec.whatwg.org/multipage/dom.html#was-created-via-cross-origin-redirects) is false, and newDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin) is the [same](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) as oldDocument's [origin](https://dom.spec.whatwg.org/#concept-document-origin), then set newDocument's [previous document unload timing](https://html.spec.whatwg.org/multipage/dom.html#previous-document-unload-timing) to unloadTimingInfo.

To unload a document and its descendants, given a `Document`document, an optional `Document`-or-null newDocument (default null), an optional set of steps afterAllUnloads, and an optional set of steps firePageSwapSteps:

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running within document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable)'s [session history traversal queue](https://html.spec.whatwg.org/multipage/document-sequences.html#tn-session-history-traversal-queue).

2.   Let childNavigables be document's [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable).

3.   Let numberUnloaded be 0.

4.   [For each](https://infra.spec.whatwg.org/#list-iterate)childNavigable of childNavigables in what order?, [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given childNavigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to perform the following steps:

    1.   Let incrementUnloaded be an algorithm step which increments numberUnloaded.

    2.   [Unload a document and its descendants](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-a-document-and-its-descendants) given childNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document), null, and incrementUnloaded.

5.   Wait until numberUnloaded equals childNavigable's [size](https://infra.spec.whatwg.org/#list-size).

6.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to perform the following steps:

    1.   If firePageSwapSteps is given, then run firePageSwapSteps.

    2.   [Unload](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-a-document)document, passing along newDocument if it is not null.

    3.   If afterAllUnloads was given, then run it.

This specification defines the following unloading document cleanup steps. Other specifications can define more. Given a `Document`document:

1.   Let window be document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global).

2.   For each `WebSocket` object webSocket whose [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) is window, [make disappear](https://websockets.spec.whatwg.org/#make-disappear)webSocket.

If this affected any `WebSocket` objects, then [make document unsalvageable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#make-document-unsalvageable) given document and "`websocket`".

3.   For each `WebTransport` object transport whose [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) is window, run the [context cleanup steps](https://w3c.github.io/webtransport/#context-cleanup-steps) given transport.

4.   If document's _[salvageable](https://html.spec.whatwg.org/multipage/document-lifecycle.html#concept-document-salvageable)_ state is false, then:

    1.   For each `EventSource` object eventSource whose [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) is equal to window, [forcibly close](https://html.spec.whatwg.org/multipage/server-sent-events.html#concept-eventsource-forcibly-close)eventSource.

    2.   [Clear](https://infra.spec.whatwg.org/#map-clear)window's [map of active timers](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#map-of-active-timers).

It would be better if specification authors sent a pull request to add calls from here into their specifications directly, instead of using the [unloading document cleanup steps](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unloading-document-cleanup-steps) hook, to ensure well-defined cross-specification call order. As of the time of this writing the following specifications are known to have [unloading document cleanup steps](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unloading-document-cleanup-steps), which will be run in an unspecified order: Fullscreen API, Web NFC, WebDriver BiDi, Compute Pressure, File API, Media Capture and Streams, Picture-in-Picture, Screen Orientation, Service Workers, WebLocks API, WebAudio API, WebRTC. [[FULLSCREEN]](https://html.spec.whatwg.org/multipage/references.html#refsFULLSCREEN)[[WEBNFC]](https://html.spec.whatwg.org/multipage/references.html#refsWEBNFC)[[WEBDRIVERBIDI]](https://html.spec.whatwg.org/multipage/references.html#refsWEBDRIVERBIDI)[[COMPUTEPRESSURE]](https://html.spec.whatwg.org/multipage/references.html#refsCOMPUTEPRESSURE)[[FILEAPI]](https://html.spec.whatwg.org/multipage/references.html#refsFILEAPI)[[MEDIASTREAM]](https://html.spec.whatwg.org/multipage/references.html#refsMEDIASTREAM)[[PICTUREINPICTURE]](https://html.spec.whatwg.org/multipage/references.html#refsPICTUREINPICTURE)[[SCREENORIENTATION]](https://html.spec.whatwg.org/multipage/references.html#refsSCREENORIENTATION)[[SW]](https://html.spec.whatwg.org/multipage/references.html#refsSW)[[WEBLOCKS]](https://html.spec.whatwg.org/multipage/references.html#refsWEBLOCKS)[[WEBAUDIO]](https://html.spec.whatwg.org/multipage/references.html#refsWEBAUDIO)[[WEBRTC]](https://html.spec.whatwg.org/multipage/references.html#refsWEBRTC)

[Issue #8906](https://github.com/whatwg/html/issues/8906) tracks the work to make the order of these steps clear.

#### 7.5.10 Destroying documents[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroying-documents)

To destroy a `Document`document:

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running as part of a [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) queued on document's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop).

2.   [Abort](https://html.spec.whatwg.org/multipage/document-lifecycle.html#abort-a-document)document.

3.   Set document's _[salvageable](https://html.spec.whatwg.org/multipage/document-lifecycle.html#concept-document-salvageable)_ state to false.

4.   Let ports be the list of `MessagePort`s whose [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global)'s [associated `Document`](https://html.spec.whatwg.org/multipage/nav-history-apis.html#concept-document-window) is document.

5.   For each port in ports, [disentangle](https://html.spec.whatwg.org/multipage/web-messaging.html#disentangle)port.

6.   Run any [unloading document cleanup steps](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unloading-document-cleanup-steps) for document that are defined by this specification and [other applicable specifications](https://html.spec.whatwg.org/multipage/infrastructure.html#other-applicable-specifications).

7.   Remove any [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) whose [document](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task-document) is document from any [task queue](https://html.spec.whatwg.org/multipage/webappapis.html#task-queue) (without running those tasks).

8.   Set document's [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc) to null.

9.   Set document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable)'s [active session history entry](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-active-history-entry)'s [document state](https://html.spec.whatwg.org/multipage/browsing-the-web.html#she-document-state)'s [document](https://html.spec.whatwg.org/multipage/browsing-the-web.html#document-state-document) to null.

10.   [Remove](https://infra.spec.whatwg.org/#list-remove)document from the [owner set](https://html.spec.whatwg.org/multipage/workers.html#concept-WorkerGlobalScope-owner-set) of each `WorkerGlobalScope` object whose set [contains](https://infra.spec.whatwg.org/#list-contain)document.

11.   [For each](https://infra.spec.whatwg.org/#list-iterate)workletGlobalScope in document's [worklet global scopes](https://html.spec.whatwg.org/multipage/worklets.html#concept-document-worklet-global-scopes), [terminate](https://html.spec.whatwg.org/multipage/worklets.html#terminate-a-worklet-global-scope)workletGlobalScope.

Even after destruction, the `Document` object itself might still be accessible to script, in the case where we are [destroying a child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#destroy-a-child-navigable).

To destroy a document and its descendants given a `Document`document and an optional set of steps afterAllDestruction, perform the following steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

1.   If document is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), then:

    1.   Let reason be a string from [user-agent specific blocking reasons](https://html.spec.whatwg.org/multipage/nav-history-apis.html#ua-specific-blocking-reasons). If none apply, then let reason be "`masked`".

    2.   [Make document unsalvageable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#make-document-unsalvageable) given document and reason.

    3.   If document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) is a [top-level traversable](https://html.spec.whatwg.org/multipage/document-sequences.html#top-level-traversable), [build not restored reasons for a top-level traversable and its descendants](https://html.spec.whatwg.org/multipage/browsing-the-web.html#build-not-restored-reasons-for-a-top-level-traversable-and-its-descendants) given document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable).

2.   Let childNavigables be document's [child navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable).

3.   Let numberDestroyed be 0.

4.   [For each](https://infra.spec.whatwg.org/#list-iterate)childNavigable of childNavigables in what order?, [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given childNavigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to perform the following steps:

    1.   Let incrementDestroyed be an algorithm step which increments numberDestroyed.

    2.   [Destroy a document and its descendants](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document-and-its-descendants) given childNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) and incrementDestroyed.

5.   Wait until numberDestroyed equals childNavigable's [size](https://infra.spec.whatwg.org/#list-size).

6.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given document's [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global) to perform the following steps:

    1.   [Destroy](https://html.spec.whatwg.org/multipage/document-lifecycle.html#destroy-a-document)document.

    2.   If afterAllDestruction was given, then run it.

#### 7.5.11 Aborting a document load[](https://html.spec.whatwg.org/multipage/document-lifecycle.html#aborting-a-document-load)

To abort a `Document`document:

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running as part of a [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) queued on document's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop).

2.   Cancel any instances of the [fetch](https://fetch.spec.whatwg.org/#concept-fetch) algorithm in the context of document, discarding any [tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task)[queued](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-task) for them, and discarding any further data received from the network for them. If this resulted in any instances of the [fetch](https://fetch.spec.whatwg.org/#concept-fetch) algorithm being canceled or any [queued](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-task)[tasks](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) or any network data getting discarded, then [make document unsalvageable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#make-document-unsalvageable) given document and "`fetch`".

3.   If document's [during-loading navigation ID for WebDriver BiDi](https://html.spec.whatwg.org/multipage/dom.html#concept-document-navigation-id) is non-null, then:

    1.   Invoke [WebDriver BiDi navigation aborted](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-aborted) with document's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) and a new [WebDriver BiDi navigation status](https://w3c.github.io/webdriver-bidi/#webdriver-bidi-navigation-status) whose [id](https://w3c.github.io/webdriver-bidi/#navigation-status-id) is document's [during-loading navigation ID for WebDriver BiDi](https://html.spec.whatwg.org/multipage/dom.html#concept-document-navigation-id), [status](https://w3c.github.io/webdriver-bidi/#navigation-status-status) is "`canceled`", and [url](https://w3c.github.io/webdriver-bidi/#navigation-status-url) is document's [URL](https://dom.spec.whatwg.org/#concept-document-url).

    2.   Set document's [during-loading navigation ID for WebDriver BiDi](https://html.spec.whatwg.org/multipage/dom.html#concept-document-navigation-id) to null.

4.   If document has an [active parser](https://html.spec.whatwg.org/multipage/dom.html#active-parser), then:

    1.   Set document's [active parser was aborted](https://html.spec.whatwg.org/multipage/dynamic-markup-insertion.html#active-parser-was-aborted) to true.

    2.   [Abort that parser](https://html.spec.whatwg.org/multipage/parsing.html#abort-a-parser).

    3.   [Make document unsalvageable](https://html.spec.whatwg.org/multipage/browsing-the-web.html#make-document-unsalvageable) given document and "`parser-aborted`".

To abort a document and its descendants given a `Document`document:

1.   [Assert](https://infra.spec.whatwg.org/#assert): this is running as part of a [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) queued on document's [relevant agent](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-agent)'s [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#concept-agent-event-loop).

2.   Let descendantNavigables be document's [descendant navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#descendant-navigables).

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)descendantNavigable of descendantNavigables in what order?, [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [navigation and traversal task source](https://html.spec.whatwg.org/multipage/webappapis.html#navigation-and-traversal-task-source) given descendantNavigable's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) to perform the following steps:

    1.   [Abort](https://html.spec.whatwg.org/multipage/document-lifecycle.html#abort-a-document)descendantNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

    2.   If descendantNavigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s _[salvageable](https://html.spec.whatwg.org/multipage/document-lifecycle.html#concept-document-salvageable)_ is false, then set document's _[salvageable](https://html.spec.whatwg.org/multipage/document-lifecycle.html#concept-document-salvageable)_ to false.

4.   [Abort](https://html.spec.whatwg.org/multipage/document-lifecycle.html#abort-a-document)document.

To stop loading a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable)navigable:

1.   Let document be navigable's [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

2.   If document's [unload counter](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-counter) is 0, and navigable's [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation) is a [navigation ID](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-id), then [set the ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#set-the-ongoing-navigation) for navigable to null.

This will have the effect of aborting any ongoing navigations of navigable, since at certain points during navigation, changes to the [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation) will cause further work to be abandoned.

3.   [Abort a document and its descendants](https://html.spec.whatwg.org/multipage/document-lifecycle.html#abort-a-document-and-its-descendants) given document.

Through their [user interface](https://html.spec.whatwg.org/multipage/speculative-loading.html#nav-traversal-ui), user agents also allow stopping traversals, i.e. cases where the [ongoing navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#ongoing-navigation) is "`traversal`". The above algorithm does not account for this. (On the other hand, user agents do not allow `window.stop()` to stop traversals, so the above algorithm is correct for that caller.) See [issue #6905](https://github.com/whatwg/html/issues/6905).

[← 7.4 Navigation and session history](https://html.spec.whatwg.org/multipage/browsing-the-web.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [7.6 Speculative loading →](https://html.spec.whatwg.org/multipage/speculative-loading.html)
