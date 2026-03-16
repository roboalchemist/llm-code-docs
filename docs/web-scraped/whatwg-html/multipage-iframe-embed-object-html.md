# Source: https://html.spec.whatwg.org/multipage/iframe-embed-object.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/iframe-embed-object.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 4.8.4 Images](https://html.spec.whatwg.org/multipage/images.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.8.8 The video element →](https://html.spec.whatwg.org/multipage/media.html)
1.       1.           1.   [4.8.5 The `iframe` element](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-iframe-element)
        2.   [4.8.6 The `embed` element](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-embed-element)
        3.   [4.8.7 The `object` element](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-object-element)

#### 4.8.5 The `iframe` element[](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-iframe-element)

[Element/iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe "The <iframe> HTML element represents a nested browsing context, embedding another HTML page into the current one.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera 15+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 14+

[HTMLIFrameElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement "The HTMLIFrameElement interface provides special properties and methods (beyond those of the HTMLElement interface it also has available to it by inheritance) for manipulating the layout and presentation of inline frame elements.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

[HTMLIFrameElement/src](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/src "The HTMLIFrameElement.src property reflects the HTML referrerpolicy attribute of the <iframe> element defining which referrer is sent when fetching the resource.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLObjectElement/width](https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement/width "The width property of the HTMLObjectElement interface returns a string that reflects the width HTML attribute, specifying the displayed width of the resource in CSS pixels.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLObjectElement/height](https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement/height "The height property of the HTMLObjectElement interface Returns a string that reflects the height HTML attribute, specifying the displayed height of the resource in CSS pixels.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category).[Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Nothing](https://html.spec.whatwg.org/multipage/dom.html#concept-content-nothing).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`src` — Address of the resource `srcdoc` — A document to render in the `iframe``name` — Name of [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable)`sandbox` — Security rules for nested content `allow` — [Permissions policy](https://w3c.github.io/webappsec-feature-policy/#permissions-policy) to be applied to the `iframe`'s contents `allowfullscreen` — Whether to allow the `iframe`'s contents to use `requestFullscreen()``width` — Horizontal dimension `height` — Vertical dimension `referrerpolicy` — [Referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy) for [fetches](https://fetch.spec.whatwg.org/#concept-fetch) initiated by the element `loading` — Used when determining loading deferral [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-iframe).[For implementers](https://w3c.github.io/html-aam/#el-iframe).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLIFrameElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, ReflectURL] attribute USVString src;
  [CEReactions] attribute (TrustedHTML or DOMString) srcdoc;
  [CEReactions, Reflect] attribute DOMString name;
  [SameObject, PutForwards=value, Reflect] readonly attribute DOMTokenList sandbox;
  [CEReactions, Reflect] attribute DOMString allow;
  [CEReactions, Reflect] attribute boolean allowFullscreen;
  [CEReactions, Reflect] attribute DOMString width;
  [CEReactions, Reflect] attribute DOMString height;
  [CEReactions] attribute DOMString referrerPolicy;
  [CEReactions] attribute DOMString loading;
  readonly attribute Document? contentDocument;
  readonly attribute WindowProxy? contentWindow;
  Document? getSVGDocument();

  // also has obsolete members
};
```

The `iframe` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) its [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable).

The `src` attribute gives the [URL](https://url.spec.whatwg.org/#concept-url) of a page that the element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is to contain. The attribute, if present, must be a [valid non-empty URL potentially surrounded by spaces](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#valid-non-empty-url-potentially-surrounded-by-spaces). If the `itemprop` attribute is specified on an `iframe` element, then the `src` attribute must also be specified.

[Element/iframe#attr-srcdoc](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-srcdoc "The <iframe> HTML element represents a nested browsing context, embedding another HTML page into the current one.")

Support in all current engines.

Firefox 25+Safari 6+Chrome 20+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android?

The `srcdoc` attribute gives the content of the page that the element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is to contain. The value of the attribute is used to [construct](https://html.spec.whatwg.org/multipage/browsing-the-web.html#create-navigation-params-from-a-srcdoc-resource)an `iframe``srcdoc` document, which is a `Document` whose [URL](https://dom.spec.whatwg.org/#concept-document-url)[matches `about:srcdoc`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#matches-about:srcdoc).

The above requirements apply in [XML documents](https://dom.spec.whatwg.org/#xml-document) as well.

Here a blog uses the `srcdoc` attribute in conjunction with the `sandbox` attribute described below to provide users of user agents that support this feature with an extra layer of protection from script injection in the blog post comments:

```
<article>
 <h1>I got my own magazine!</h1>
 <p>After much effort, I've finally found a publisher, and so now I
 have my own magazine! Isn't that awesome?! The first issue will come
 out in September, and we have articles about getting food, and about
 getting in boxes, it's going to be great!</p>
 <footer>
  <p>Written by <a href="/users/cap">cap</a>, 1 hour ago.
 </footer>
 <article>
  <footer> Thirteen minutes ago, <a href="/users/ch">ch</a> wrote: </footer>
  <iframe sandbox srcdoc="<p>did you get a cover picture yet?"></iframe>
 </article>
 <article>
  <footer> Nine minutes ago, <a href="/users/cap">cap</a> wrote: </footer>
  <iframe sandbox srcdoc="<p>Yeah, you can see it <a href=&quot;/gallery?mode=cover&amp;amp;page=1&quot;>in my gallery</a>."></iframe>
 </article>
 <article>
  <footer> Five minutes ago, <a href="/users/ch">ch</a> wrote: </footer>
  <iframe sandbox srcdoc="<p>hey that's earl's table.
<p>you should get earl&amp;amp;me on the next cover."></iframe>
 </article>
```

Notice the way that quotes have to be escaped (otherwise the `srcdoc` attribute would end prematurely), and the way raw ampersands (e.g. in URLs or in prose) mentioned in the sandboxed content have to be _doubly_ escaped — once so that the ampersand is preserved when originally parsing the `srcdoc` attribute, and once more to prevent the ampersand from being misinterpreted when parsing the sandboxed content.

Furthermore, notice that since the [DOCTYPE](https://html.spec.whatwg.org/multipage/syntax.html#syntax-doctype) is optional in [`iframe``srcdoc` documents](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#an-iframe-srcdoc-document), and the `html`, `head`, and `body` elements have [optional start and end tags](https://html.spec.whatwg.org/multipage/syntax.html#syntax-tag-omission), and the `title` element is also optional in [`iframe``srcdoc` documents](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#an-iframe-srcdoc-document), the markup in a `srcdoc` attribute can be relatively succinct despite representing an entire document, since only the contents of the `body` element need appear literally in the syntax. The other elements are still present, but only by implication.

In [the HTML syntax](https://html.spec.whatwg.org/multipage/syntax.html#syntax), authors need only remember to use U+0022 QUOTATION MARK characters (") to wrap the attribute contents and then to escape all U+0026 AMPERSAND (&) and U+0022 QUOTATION MARK (") characters, and to specify the `sandbox` attribute, to ensure safe embedding of content. (And remember to escape ampersands before quotation marks, to ensure quotation marks become &quot; and not &amp;quot;.)

In XML the U+003C LESS-THAN SIGN character (<) needs to be escaped as well. In order to prevent [attribute-value normalization](https://www.w3.org/TR/xml/#AVNormalize), some of XML's whitespace characters — specifically U+0009 CHARACTER TABULATION (tab), U+000A LINE FEED (LF), and U+000D CARRIAGE RETURN (CR) — also need to be escaped. [[XML]](https://html.spec.whatwg.org/multipage/references.html#refsXML)

If the `src` attribute and the `srcdoc` attribute are both specified together, the `srcdoc` attribute takes priority. This allows authors to provide a fallback [URL](https://url.spec.whatwg.org/#concept-url) for legacy user agents that do not support the `srcdoc` attribute.

* * *

This happens without any `unload` events firing (the element's [content document](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-bcc-content-document) is _[destroyed](https://html.spec.whatwg.org/multipage/document-sequences.html#destroy-a-child-navigable)_, not _[unloaded](https://html.spec.whatwg.org/multipage/document-lifecycle.html#unload-a-document)_).

Although `iframe`s are processed while in a [shadow tree](https://dom.spec.whatwg.org/#concept-shadow-tree), per the above, several other aspects of their behavior are not well-defined with regards to shadow trees. See [issue #763](https://github.com/whatwg/html/issues/763) for more detail.

Whenever an `iframe` element with a non-null [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) has its `srcdoc` attribute set, changed, or removed, the user agent must [process the `iframe` attributes](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#process-the-iframe-attributes).

Similarly, whenever an `iframe` element with a non-null [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) but with no `srcdoc` attribute specified has its `src` attribute set, changed, or removed, the user agent must [process the `iframe` attributes](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#process-the-iframe-attributes).

To process the `iframe` attributes for an element element, with an optional boolean initialInsertion (default false):

1.   If element's `srcdoc` attribute is specified, then:

    1.   Set element's [current navigation was lazy loaded](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#current-navigation-was-lazy-loaded) boolean to false.

    2.   If the [will lazy load element steps](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#will-lazy-load-element-steps) given element return true, then:

        1.   Set element's [lazy load resumption steps](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-resumption-steps) to the rest of this algorithm starting with the step labeled _navigate to the srcdoc resource_.

        2.   Set element's [current navigation was lazy loaded](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#current-navigation-was-lazy-loaded) boolean to true.

        3.   [Start intersection-observing a lazy loading element](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#start-intersection-observing-a-lazy-loading-element) for element.

        4.   Return.

    3.   _Navigate to the srcdoc resource_: [Navigate an `iframe` or `frame`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#navigate-an-iframe-or-frame) given element, `about:srcdoc`, the empty string, and the value of element's `srcdoc` attribute.

The resulting `Document` must be considered [an `iframe``srcdoc` document](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#an-iframe-srcdoc-document).

2.   Otherwise:

    1.   Let url be the result of running the [shared attribute processing steps for `iframe` and `frame` elements](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#shared-attribute-processing-steps-for-iframe-and-frame-elements) given element and initialInsertion.

    2.   If url is null, then return.

    3.   If url[matches `about:blank`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#matches-about:blank) and initialInsertion is true, then:

        1.   Run the [iframe load event steps](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-load-event-steps) given element.

        2.   Return.

    4.   Let referrerPolicy be the current state of element's `referrerpolicy` content attribute.

    5.   Set element's [current navigation was lazy loaded](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#current-navigation-was-lazy-loaded) boolean to false.

    6.   If the [will lazy load element steps](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#will-lazy-load-element-steps) given element return true, then:

        1.   Set element's [lazy load resumption steps](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-load-resumption-steps) to the rest of this algorithm starting with the step labeled _navigate_.

        2.   Set element's [current navigation was lazy loaded](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#current-navigation-was-lazy-loaded) boolean to true.

        3.   [Start intersection-observing a lazy loading element](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#start-intersection-observing-a-lazy-loading-element) for element.

        4.   Return.

    7.   _Navigate_: [Navigate an `iframe` or `frame`](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#navigate-an-iframe-or-frame) given element, url, and referrerPolicy.

The shared attribute processing steps for `iframe` and `frame` elements, given an element element and a boolean initialInsertion, are:

1.   Let url be the [URL record](https://url.spec.whatwg.org/#concept-url)`about:blank`.

2.   If element has a `src` attribute specified, and its value is not the empty string, then:

    1.   Let maybeURL be the result of [encoding-parsing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url) given that attribute's value, relative to element's [node document](https://dom.spec.whatwg.org/#concept-node-document).

    2.   If maybeURL is not failure, then set url to maybeURL.

3.   If the [inclusive ancestor navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#inclusive-ancestor-navigables) of element's [node navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#node-navigable) contains a [navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) whose [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document)'s [URL](https://dom.spec.whatwg.org/#concept-document-url)[equals](https://url.spec.whatwg.org/#concept-url-equals)url with _[exclude fragments](https://url.spec.whatwg.org/#url-equals-exclude-fragments)_ set to true, then return null.

4.   If url[matches `about:blank`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#matches-about:blank) and initialInsertion is true, then perform the [URL and history update steps](https://html.spec.whatwg.org/multipage/browsing-the-web.html#url-and-history-update-steps) given element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) and url.

This is necessary in case url is something like `about:blank?foo`. If url is just plain `about:blank`, this will do nothing.

5.   Return url.

To navigate an `iframe` or `frame` given an element element, a [URL](https://url.spec.whatwg.org/#concept-url)url, a [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy)referrerPolicy, an optional string-or-null srcdocString (default null), and an optional boolean initialInsertion (default false):

1.   Let historyHandling be "`auto`".

2.   If element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document) is not [completely loaded](https://html.spec.whatwg.org/multipage/document-lifecycle.html#completely-loaded), then set historyHandling to "`replace`".

3.   If element is an `iframe`, then set element's [pending resource-timing start time](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-pending-resource-timing-start-time) to the [current high resolution time](https://w3c.github.io/hr-time/#dfn-current-high-resolution-time) given element's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global).

4.   [Navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate)element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) to url using element's [node document](https://dom.spec.whatwg.org/#concept-node-document), with _[historyHandling](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-hh)_ set to historyHandling, _[referrerPolicy](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-referrer-policy)_ set to referrerPolicy, _[documentResource](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-resource)_ set to srcdocString, and _[initialInsertion](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-initial-insertion)_ set to initialInsertion.

Each `Document` has an iframe load in progress flag and a mute iframe load flag. When a `Document` is created, these flags must be unset for that `Document`.

To run the iframe load event steps, given an `iframe` element element:

1.   [Assert](https://infra.spec.whatwg.org/#assert): element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is not null.

2.   Let childDocument be element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document).

3.   If childDocument has its [mute iframe load](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#mute-iframe-load) flag set, then return.

4.   If element's [pending resource-timing start time](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-pending-resource-timing-start-time) is not null, then:

    1.   Let global be element's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global).

    2.   Let fallbackTimingInfo be a new [fetch timing info](https://fetch.spec.whatwg.org/#fetch-timing-info) whose [start time](https://fetch.spec.whatwg.org/#fetch-timing-info-start-time) is element's [pending resource-timing start time](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-pending-resource-timing-start-time) and whose [response end time](https://fetch.spec.whatwg.org/#fetch-timing-info-end-time) is the [current high resolution time](https://w3c.github.io/hr-time/#dfn-current-high-resolution-time) given global.

    3.   [Mark resource timing](https://w3c.github.io/resource-timing/#dfn-mark-resource-timing) given fallbackTimingInfo, url, "`iframe`", global, the empty string, a new [response body info](https://fetch.spec.whatwg.org/#response-body-info), and 0.

    4.   Set element's [pending resource-timing start time](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-pending-resource-timing-start-time) to null.

5.   Set childDocument's [iframe load in progress](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-load-in-progress) flag.

6.   [Fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `load` at element.

7.   Unset childDocument's [iframe load in progress](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#iframe-load-in-progress) flag.

This, in conjunction with scripting, can be used to probe the URL space of the local network's HTTP servers. User agents may implement [cross-origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin) access control policies that are stricter than those described above to mitigate this attack, but unfortunately such policies are typically not compatible with existing web content.

Each `iframe` element has an associated current navigation was lazy loaded boolean, initially false. It is set and unset in the [process the `iframe` attributes](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#process-the-iframe-attributes) algorithm.

An `iframe` element whose [current navigation was lazy loaded](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#current-navigation-was-lazy-loaded) boolean is false [potentially delays the load event](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#potentially-delays-the-load-event).

Each `iframe` element has an associated null or [`DOMHighResTimeStamp`](https://w3c.github.io/hr-time/#dom-domhighrestimestamp)pending resource-timing start time, initially set to null.

If, when the element is created, the `srcdoc` attribute is not set, and the `src` attribute is either also not set or set but its value cannot be [parsed](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url), the element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) will remain at the [initial `about:blank`](https://html.spec.whatwg.org/multipage/dom.html#is-initial-about:blank)`Document`.

If the user [navigates](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) away from this page, the `iframe`'s [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable)'s [active `WindowProxy`](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-wp) object will proxy new `Window` objects for new `Document` objects, but the `src` attribute will not change.

* * *

The `name` attribute, if present, must be a [valid navigable target name](https://html.spec.whatwg.org/multipage/document-sequences.html#valid-navigable-target-name). The given value is used to name the element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) if present when that is [created](https://html.spec.whatwg.org/multipage/document-sequences.html#create-a-new-child-navigable).

* * *

[Element/iframe#attr-sandbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-sandbox "The <iframe> HTML element represents a nested browsing context, embedding another HTML page into the current one.")

Support in all current engines.

Firefox 17+Safari 5+Chrome 4+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `sandbox` attribute, when specified, enables a set of extra restrictions on any content hosted by the `iframe`. Its value must be an [unordered set of unique space-separated tokens](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#unordered-set-of-unique-space-separated-tokens) that are [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive). The allowed values are:

*   `allow-downloads`
*   `allow-forms`
*   `allow-modals`
*   `allow-orientation-lock`
*   `allow-pointer-lock`
*   `allow-popups`
*   `allow-popups-to-escape-sandbox`
*   `allow-presentation`
*   `allow-same-origin`
*   `allow-scripts`
*   `allow-top-navigation`
*   `allow-top-navigation-by-user-activation`
*   `allow-top-navigation-to-custom-protocols`

When the attribute is set, the content is treated as being from a unique [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque), forms, scripts, and various potentially annoying APIs are disabled, and links are prevented from targeting other [navigables](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable). The `allow-same-origin` keyword causes the content to be treated as being from its real origin instead of forcing it into an [opaque origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin-opaque); the `allow-top-navigation` keyword allows the content to [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) its [traversable navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-traversable); the `allow-top-navigation-by-user-activation` keyword behaves similarly but allows such [navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) only when the browsing context's [active window](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-window) has [transient activation](https://html.spec.whatwg.org/multipage/interaction.html#transient-activation); the `allow-top-navigation-to-custom-protocols` reenables navigations toward non [fetch scheme](https://fetch.spec.whatwg.org/#fetch-scheme) to be [handed off to external software](https://html.spec.whatwg.org/multipage/browsing-the-web.html#hand-off-to-external-software); and the `allow-forms`, `allow-modals`, `allow-orientation-lock`, `allow-pointer-lock`, `allow-popups`, `allow-presentation`, `allow-scripts`, and `allow-popups-to-escape-sandbox` keywords re-enable forms, modal dialogs, screen orientation lock, the pointer lock API, popups, the presentation API, scripts, and the creation of unsandboxed [auxiliary browsing contexts](https://html.spec.whatwg.org/multipage/document-sequences.html#auxiliary-browsing-context) respectively. The `allow-downloads` keyword allows content to perform downloads. [[POINTERLOCK]](https://html.spec.whatwg.org/multipage/references.html#refsPOINTERLOCK)[[SCREENORIENTATION]](https://html.spec.whatwg.org/multipage/references.html#refsSCREENORIENTATION)[[PRESENTATION]](https://html.spec.whatwg.org/multipage/references.html#refsPRESENTATION)

The `allow-top-navigation` and `allow-top-navigation-by-user-activation` keywords must not both be specified, as doing so is redundant; only `allow-top-navigation` will have an effect in such non-conformant markup.

Similarly, the `allow-top-navigation-to-custom-protocols` keyword must not be specified if either `allow-top-navigation` or `allow-popups` are specified, as doing so is redundant.

To allow `alert()`, `confirm()`, and `prompt()` inside sandboxed content, both the `allow-modals` and `allow-same-origin` keywords need to be specified, and the loaded URL needs to be [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) with the [top-level origin](https://html.spec.whatwg.org/multipage/webappapis.html#concept-environment-top-level-origin). Without the `allow-same-origin` keyword, the content is always treated as cross-origin, and cross-origin content [cannot show simple dialogs](https://html.spec.whatwg.org/multipage/timers-and-user-prompts.html#cannot-show-simple-dialogs).

Setting both the `allow-scripts` and `allow-same-origin` keywords together when the embedded page has the [same origin](https://html.spec.whatwg.org/multipage/browsers.html#same-origin) as the page containing the `iframe` allows the embedded page to simply remove the `sandbox` attribute and then reload itself, effectively breaking out of the sandbox altogether.

These flags only take effect when the [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) of the `iframe` element is [navigated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate). Removing them, or removing the entire `sandbox` attribute, has no effect on an already-loaded page.

Potentially hostile files should not be served from the same server as the file containing the `iframe` element. Sandboxing hostile content is of minimal help if an attacker can convince the user to just visit the hostile content directly, rather than in the `iframe`. To limit the damage that can be caused by hostile HTML content, it should be served from a separate dedicated domain. Using a different domain ensures that scripts in the files are unable to attack the site, even if the user is tricked into visiting those pages directly, without the protection of the `sandbox` attribute.

In this example, some completely-unknown, potentially hostile, user-provided HTML content is embedded in a page. Because it is served from a separate domain, it is affected by all the normal cross-site restrictions. In addition, the embedded page has scripting disabled, plugins disabled, forms disabled, and it cannot navigate any frames or windows other than itself (or any frames or windows it itself embeds).

```
<p>We're not scared of you! Here is your content, unedited:</p>
<iframe sandbox src="https://usercontent.example.net/getusercontent.cgi?id=12193"></iframe>
```

It is important to use a separate domain so that if the attacker convinces the user to visit that page directly, the page doesn't run in the context of the site's origin, which would make the user vulnerable to any attack found in the page.

In this example, a gadget from another site is embedded. The gadget has scripting and forms enabled, and the origin sandbox restrictions are lifted, allowing the gadget to communicate with its originating server. The sandbox is still useful, however, as it disables plugins and popups, thus reducing the risk of the user being exposed to malware and other annoyances.

```
<iframe sandbox="allow-same-origin allow-forms allow-scripts"
        src="https://maps.example.com/embedded.html"></iframe>
```

Suppose a file A contained the following fragment:

`<iframe sandbox="allow-same-origin allow-forms" src=B></iframe>`
Suppose that file B contained an iframe also:

`<iframe sandbox="allow-scripts" src=C></iframe>`
Further, suppose that file C contained a link:

`<a href=D>Link</a>`
For this example, suppose all the files were served as `text/html`.

Page C in this scenario has all the sandboxing flags set. Scripts are disabled, because the `iframe` in A has scripts disabled, and this overrides the `allow-scripts` keyword set on the `iframe` in B. Forms are also disabled, because the inner `iframe` (in B) does not have the `allow-forms` keyword set.

Suppose now that a script in A removes all the `sandbox` attributes in A and B. This would change nothing immediately. If the user clicked the link in C, loading page D into the `iframe` in B, page D would now act as if the `iframe` in B had the `allow-same-origin` and `allow-forms` keywords set, because that was the state of the [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) in the `iframe` in A when page B was loaded.

Generally speaking, dynamically removing or changing the `sandbox` attribute is ill-advised, because it can make it quite hard to reason about what will be allowed and what will not.

* * *

The `allow` attribute, when specified, determines the [container policy](https://w3c.github.io/webappsec-feature-policy/#container-policy) that will be used when the [permissions policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-permissions-policy) for a `Document` in the `iframe`'s [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is initialized. Its value must be a [serialized permissions policy](https://w3c.github.io/webappsec-feature-policy/#serialized-permissions-policy). [[PERMISSIONSPOLICY]](https://html.spec.whatwg.org/multipage/references.html#refsPERMISSIONSPOLICY)

In this example, an `iframe` is used to embed a map from an online navigation service. The `allow` attribute is used to enable the Geolocation API within the nested context.

`<iframe src="https://maps.example.com/" allow="geolocation"></iframe>`

The `allowfullscreen` attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute). When specified, it indicates that `Document` objects in the `iframe` element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) will be initialized with a [permissions policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-permissions-policy) which allows the "`fullscreen`" feature to be used from any [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin). This is enforced by the [process permissions policy attributes](https://w3c.github.io/webappsec-feature-policy/#process-permissions-policy-attributes) algorithm. [[PERMISSIONSPOLICY]](https://html.spec.whatwg.org/multipage/references.html#refsPERMISSIONSPOLICY)

Here, an `iframe` is used to embed a player from a video site. The `allowfullscreen` attribute is needed to enable the player to show its video fullscreen.

```
<article>
 <header>
  <p><img src="/usericons/1627591962735"> <b>Fred Flintstone</b></p>
  <p><a href="/posts/3095182851" rel=bookmark>12:44</a> — <a href="#acl-3095182851">Private Post</a></p>
 </header>
 <p>Check out my new ride!</p>
 <iframe src="https://video.example.com/embed?id=92469812" allowfullscreen></iframe>
</article>
```

Neither `allow` nor `allowfullscreen` can grant access to a feature in an `iframe` element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) if the element's [node document](https://dom.spec.whatwg.org/#concept-node-document) is not already allowed to use that feature.

Because they only influence the [permissions policy](https://html.spec.whatwg.org/multipage/dom.html#concept-document-permissions-policy) of the [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable)'s [active document](https://html.spec.whatwg.org/multipage/document-sequences.html#nav-document), the `allow` and `allowfullscreen` attributes only take effect when the [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) of the `iframe` is [navigated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate). Adding or removing them has no effect on an already-loaded document.

* * *

The `iframe` element supports [dimension attributes](https://html.spec.whatwg.org/multipage/embedded-content-other.html#dimension-attributes) for cases where the embedded content has specific dimensions (e.g. ad units have well-defined dimensions).

An `iframe` element never has [fallback content](https://html.spec.whatwg.org/multipage/dom.html#fallback-content), as it will always [create a new child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#create-a-new-child-navigable), regardless of whether the specified initial contents are successfully used.

* * *

The `referrerpolicy` attribute is a [referrer policy attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#referrer-policy-attribute). Its purpose is to set the [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy) used when [processing the `iframe` attributes](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#process-the-iframe-attributes) as well as allowing masking of some [origins](https://dom.spec.whatwg.org/#concept-document-origin) in the [internal ancestor origin objects list creation steps](https://html.spec.whatwg.org/multipage/dom.html#internal-ancestor-origin-objects-list-creation-steps). [[REFERRERPOLICY]](https://html.spec.whatwg.org/multipage/references.html#refsREFERRERPOLICY)

The `loading` attribute is a [lazy loading attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-loading-attribute). Its purpose is to indicate the policy for loading `iframe` elements that are outside the viewport.

* * *

Descendants of `iframe` elements represent nothing. (In legacy user agents that do not support `iframe` elements, the contents would be parsed as markup that could act as fallback content.)

The [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) treats markup inside `iframe` elements as text.

* * *

[HTMLIFrameElement/srcdoc](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/srcdoc "The srcdoc property of the HTMLIFrameElement specifies the content of the page.")

Support in all current engines.

Firefox 25+Safari 6+Chrome 20+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `srcdoc` setter steps are:

1.   Let compliantString be the result of invoking the [get trusted type compliant string](https://w3c.github.io/trusted-types/dist/spec/#get-trusted-type-compliant-string) algorithm with `TrustedHTML`, [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global), the given value, "`HTMLIFrameElement srcdoc`", and "`script`".

2.   [Set an attribute value](https://dom.spec.whatwg.org/#concept-element-attributes-set-value) given [this](https://webidl.spec.whatwg.org/#this), `srcdoc`'s [local name](https://dom.spec.whatwg.org/#concept-attribute-local-name), and compliantString.

The [supported tokens](https://dom.spec.whatwg.org/#concept-supported-tokens) for `sandbox`'s `DOMTokenList` are the allowed values defined in the `sandbox` attribute and supported by the user agent.

[HTMLIFrameElement/referrerPolicy](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/referrerPolicy "The HTMLIFrameElement.referrerPolicy property reflects the HTML referrerpolicy attribute of the <iframe> element defining which referrer is sent when fetching the resource.")

Support in all current engines.

Firefox 50+Safari 14+Chrome 52+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLIFrameElement/contentDocument](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/contentDocument "If the iframe and the iframe's parent document are Same Origin, returns a Document (that is, the active document in the inline frame's nested browsing context), else returns null.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLIFrameElement/contentWindow](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/contentWindow "The contentWindow property returns the Window object of an HTMLIFrameElement. You can use this Window object to access the iframe's document and its internal DOM. This attribute is read-only, but its properties can be manipulated like the global Window object.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 8+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Here is an example of a page using an `iframe` to include advertising from an advertising broker:

```
<iframe src="https://ads.example.com/?customerid=923513721&amp;format=banner"
        width="468" height="60"></iframe>
```

#### 4.8.6 The `embed` element[](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-embed-element)

[Element/embed](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed "The <embed> HTML element embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.")

Support in all current engines.

Firefox 1+Safari 4+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLEmbedElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLEmbedElement "The HTMLEmbedElement interface provides special properties (beyond the regular HTMLElement interface it also has available to it by inheritance) for manipulating <embed> elements.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category).[Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Nothing](https://html.spec.whatwg.org/multipage/dom.html#concept-content-nothing).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):No [end tag](https://html.spec.whatwg.org/multipage/syntax.html#syntax-end-tag).[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`src` — Address of the resource `type` — Type of embedded resource `width` — Horizontal dimension `height` — Vertical dimension Any other attribute that has no namespace (see prose).[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-embed).[For implementers](https://w3c.github.io/html-aam/#el-embed).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLEmbedElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, ReflectURL] attribute USVString src;
  [CEReactions, Reflect] attribute DOMString type;
  [CEReactions, Reflect] attribute DOMString width;
  [CEReactions, Reflect] attribute DOMString height;
  Document? getSVGDocument();

  // also has obsolete members
};
```

The `embed` element provides an integration point for an external application or interactive content.

The `src` attribute gives the [URL](https://url.spec.whatwg.org/#concept-url) of the resource being embedded. The attribute, if present, must contain a [valid non-empty URL potentially surrounded by spaces](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#valid-non-empty-url-potentially-surrounded-by-spaces).

If the `itemprop` attribute is specified on an `embed` element, then the `src` attribute must also be specified.

The `type` attribute, if present, gives the [MIME type](https://mimesniff.spec.whatwg.org/#mime-type) by which the plugin to instantiate is selected. The value must be a [valid MIME type string](https://mimesniff.spec.whatwg.org/#valid-mime-type). If both the `type` attribute and the `src` attribute are present, then the `type` attribute must specify the same type as the [explicit Content-Type metadata](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type) of the resource given by the `src` attribute.

While any of the following conditions are occurring, any [plugin](https://html.spec.whatwg.org/multipage/infrastructure.html#plugin) instantiated for the element must be removed, and the `embed` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) nothing:

*   The element has neither a `src` attribute nor a `type` attribute.

*   The element has a [media element](https://html.spec.whatwg.org/multipage/media.html#media-element) ancestor.

*   The element has an ancestor `object` element that is _not_ showing its [fallback content](https://html.spec.whatwg.org/multipage/dom.html#fallback-content).

Whenever an `embed` element that was not [potentially active](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#concept-embed-active) becomes [potentially active](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#concept-embed-active), and whenever a [potentially active](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#concept-embed-active)`embed` element that is remaining [potentially active](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#concept-embed-active) has its `src` attribute set, changed, or removed or its `type` attribute set, changed, or removed, the user agent must [queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) on the embed task source given the element to run [the `embed` element setup steps](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-embed-element-setup-steps) for that element.

The `embed` element setup steps for a given `embed` element element are as follows:

1.   If another [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) has since been queued to run [the `embed` element setup steps](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-embed-element-setup-steps) for element, then return.

2.   If element has a `src` attribute set, then:

    1.   Let url be the result of [encoding-parsing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url) given element's `src` attribute's value, relative to element's [node document](https://dom.spec.whatwg.org/#concept-node-document).

    2.   If url is failure, then return.

    3.   Let request be a new [request](https://fetch.spec.whatwg.org/#concept-request) whose [URL](https://fetch.spec.whatwg.org/#concept-request-url) is url, [client](https://fetch.spec.whatwg.org/#concept-request-client) is element's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object), [destination](https://fetch.spec.whatwg.org/#concept-request-destination) is "`embed`", [credentials mode](https://fetch.spec.whatwg.org/#concept-request-credentials-mode) is "`include`", [mode](https://fetch.spec.whatwg.org/#concept-request-mode) is "`navigate`", [initiator type](https://fetch.spec.whatwg.org/#request-initiator-type) is "`embed`", and whose [use-URL-credentials flag](https://fetch.spec.whatwg.org/#concept-request-use-url-credentials-flag) is set.

    4.   [Fetch](https://fetch.spec.whatwg.org/#concept-fetch)request, with _[processResponse](https://fetch.spec.whatwg.org/#process-response)_ set to the following steps given [response](https://fetch.spec.whatwg.org/#concept-response)response:

        1.   If another [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) has since been queued to run [the `embed` element setup steps](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-embed-element-setup-steps) for element, then return.

        2.   If response is a [network error](https://fetch.spec.whatwg.org/#concept-network-error), then [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `load` at element, and return.

        3.   Let type be the result of determining the [type of content](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#concept-embed-type) given element and response.

        4.   Switch on type:

null
            1.   [Display no plugin](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#display-no-plugin) for element.

Otherwise
            1.   If element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is null, then [create a new child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#create-a-new-child-navigable) for element.

            2.   [Navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate)element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) to response's [URL](https://fetch.spec.whatwg.org/#concept-response-url) using element's [node document](https://dom.spec.whatwg.org/#concept-node-document), with _[response](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-response)_ set to response, and _[historyHandling](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-hh)_ set to "`replace`".

element's `src` attribute does not get updated if the [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) gets further navigated to other locations.

            3.   element now [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) its [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable).

Fetching the resource must [delay the load event](https://html.spec.whatwg.org/multipage/parsing.html#delay-the-load-event) of element's [node document](https://dom.spec.whatwg.org/#concept-node-document).

3.   Otherwise, [display no plugin](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#display-no-plugin) for element.

To determine the type of the content given an `embed` element element and a [response](https://fetch.spec.whatwg.org/#concept-response)response, run the following steps:

1.   If element has a `type` attribute, and that attribute's value is a type that a [plugin](https://html.spec.whatwg.org/multipage/infrastructure.html#plugin) supports, then return the value of the `type` attribute.

2.   If the [path](https://url.spec.whatwg.org/#concept-url-path) component of response's [url](https://fetch.spec.whatwg.org/#concept-response-url) matches a pattern that a [plugin](https://html.spec.whatwg.org/multipage/infrastructure.html#plugin) supports, then return the type that that plugin can handle.

For example, a plugin might say that it can handle URLs with [path](https://url.spec.whatwg.org/#concept-url-path) components that end with the four character string "`.swf`".

3.   If response has [explicit Content-Type metadata](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type), and that value is a type that a [plugin](https://html.spec.whatwg.org/multipage/infrastructure.html#plugin) supports, then return that value.

4.   Return null.

It is intentional that the above algorithm allows response to have a non-[ok status](https://fetch.spec.whatwg.org/#ok-status). This allows servers to return data for plugins even with error responses (e.g., HTTP 500 Internal Server Error codes can still contain plugin data).

To display no plugin for an `embed` element element:

1.   [Destroy a child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#destroy-a-child-navigable) given element.

2.   Display an indication that no [plugin](https://html.spec.whatwg.org/multipage/infrastructure.html#plugin) could be found for element, as the contents of element.

3.   element now [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) nothing.

The `embed` element has no [fallback content](https://html.spec.whatwg.org/multipage/dom.html#fallback-content); its descendants are ignored.

Whenever an `embed` element that was [potentially active](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#concept-embed-active) stops being [potentially active](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#concept-embed-active), any [plugin](https://html.spec.whatwg.org/multipage/infrastructure.html#plugin) that had been instantiated for that element must be unloaded.

The `embed` element [potentially delays the load event](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#potentially-delays-the-load-event).

The `embed` element supports [dimension attributes](https://html.spec.whatwg.org/multipage/embedded-content-other.html#dimension-attributes).

#### 4.8.7 The `object` element[](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-object-element)

[Element/object](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object "The <object> HTML element represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLObjectElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement "The HTMLObjectElement interface provides special properties and methods (beyond those on the HTMLElement interface it also has available to it by inheritance) for manipulating the layout and presentation of <object> element, representing external resources.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLObjectElement/data](https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement/data "The data property of the HTMLObjectElement interface returns a string that reflects the data HTML attribute, specifying the address of a resource's data.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLObjectElement/type](https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement/type "The type property of the HTMLObjectElement interface returns a string that reflects the type HTML attribute, specifying the MIME type of the resource.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLObjectElement/name](https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement/name "The name property of the HTMLObjectElement interface returns a string that reflects the name HTML attribute, specifying the name of the browsing context.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category).[Listed](https://html.spec.whatwg.org/multipage/forms.html#category-listed)[form-associated element](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Transparent](https://html.spec.whatwg.org/multipage/dom.html#transparent).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`data` — Address of the resource `type` — Type of embedded resource `name` — Name of [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable)`form` — Associates the element with a `form` element `width` — Horizontal dimension `height` — Vertical dimension [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-object).[For implementers](https://w3c.github.io/html-aam/#el-object).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLObjectElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, ReflectURL] attribute USVString data;
  [CEReactions, Reflect] attribute DOMString type;
  [CEReactions, Reflect] attribute DOMString name;
  readonly attribute HTMLFormElement? form;
  [CEReactions, Reflect] attribute DOMString width;
  [CEReactions, Reflect] attribute DOMString height;
  readonly attribute Document? contentDocument;
  readonly attribute WindowProxy? contentWindow;
  Document? getSVGDocument();

  readonly attribute boolean willValidate;
  readonly attribute ValidityState validity;
  readonly attribute DOMString validationMessage;
  boolean checkValidity();
  boolean reportValidity();
  undefined setCustomValidity(DOMString error);

  // also has obsolete members
};
```

Depending on the type of content instantiated by the `object` element, the node also supports other interfaces.

The `object` element can represent an external resource, which, depending on the type of the resource, will either be treated as an image or as a [child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#child-navigable).

The `data` attribute specifies the [URL](https://url.spec.whatwg.org/#concept-url) of the resource. It must be present, and must contain a [valid non-empty URL potentially surrounded by spaces](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#valid-non-empty-url-potentially-surrounded-by-spaces).

The `type` attribute, if present, specifies the type of the resource. If present, the attribute must be a [valid MIME type string](https://mimesniff.spec.whatwg.org/#valid-mime-type).

The `name` attribute, if present, must be a [valid navigable target name](https://html.spec.whatwg.org/multipage/document-sequences.html#valid-navigable-target-name). The given value is used to name the element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable), if applicable, and if present when the element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is [created](https://html.spec.whatwg.org/multipage/document-sequences.html#create-a-new-child-navigable).

Whenever one of the following conditions occur:

*   the element is created, 
*   the element is popped off the [stack of open elements](https://html.spec.whatwg.org/multipage/parsing.html#stack-of-open-elements) of an [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) or [XML parser](https://html.spec.whatwg.org/multipage/xhtml.html#xml-parser), 
*   the element is not on the [stack of open elements](https://html.spec.whatwg.org/multipage/parsing.html#stack-of-open-elements) of an [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) or [XML parser](https://html.spec.whatwg.org/multipage/xhtml.html#xml-parser), and it is either [inserted into a document](https://html.spec.whatwg.org/multipage/infrastructure.html#insert-an-element-into-a-document) or [removed from a document](https://html.spec.whatwg.org/multipage/infrastructure.html#remove-an-element-from-a-document), 
*   the element's [node document](https://dom.spec.whatwg.org/#concept-node-document) changes whether it is [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), 
*   one of the element's ancestor `object` elements changes to or from showing its [fallback content](https://html.spec.whatwg.org/multipage/dom.html#fallback-content), 
*   the element's `classid` attribute is set, changed, or removed, 
*   the element's `classid` attribute is not present, and its `data` attribute is set, changed, or removed, 
*   neither the element's `classid` attribute nor its `data` attribute are present, and its `type` attribute is set, changed, or removed, 
*   the element changes from [being rendered](https://html.spec.whatwg.org/multipage/rendering.html#being-rendered) to not being rendered, or vice versa, 

...the user agent must [queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given the `object` element to run the following steps to (re)determine what the `object` element represents. This [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) being [queued](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-task) or actively running must [delay the load event](https://html.spec.whatwg.org/multipage/parsing.html#delay-the-load-event) of the element's [node document](https://dom.spec.whatwg.org/#concept-node-document).

1.   If the user has indicated a preference that this `object` element's [fallback content](https://html.spec.whatwg.org/multipage/dom.html#fallback-content) be shown instead of the element's usual behavior, then jump to the step below labeled _fallback_.

For example, a user could ask for the element's [fallback content](https://html.spec.whatwg.org/multipage/dom.html#fallback-content) to be shown because that content uses a format that the user finds more accessible.

2.   If the element has an ancestor [media element](https://html.spec.whatwg.org/multipage/media.html#media-element), or has an ancestor `object` element that is _not_ showing its [fallback content](https://html.spec.whatwg.org/multipage/dom.html#fallback-content), or if the element is not [in a document](https://dom.spec.whatwg.org/#in-a-document) whose [browsing context](https://html.spec.whatwg.org/multipage/document-sequences.html#concept-document-bc) is non-null, or if the element's [node document](https://dom.spec.whatwg.org/#concept-node-document) is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active), or if the element is still in the [stack of open elements](https://html.spec.whatwg.org/multipage/parsing.html#stack-of-open-elements) of an [HTML parser](https://html.spec.whatwg.org/multipage/parsing.html#html-parser) or [XML parser](https://html.spec.whatwg.org/multipage/xhtml.html#xml-parser), or if the element is not [being rendered](https://html.spec.whatwg.org/multipage/rendering.html#being-rendered), then jump to the step below labeled _fallback_.

3.   If the `data` attribute is present and its value is not the empty string, then:

    1.   If the `type` attribute is present and its value is not a type that the user agent supports, then the user agent may jump to the step below labeled _fallback_ without fetching the content to examine its real type.

    2.   Let url be the result of [encoding-parsing a URL](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#encoding-parsing-a-url) given the `data` attribute's value, relative to the element's [node document](https://dom.spec.whatwg.org/#concept-node-document).

    3.   If url is failure, then [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `error` at the element and jump to the step below labeled _fallback_.

    4.   Let request be a new [request](https://fetch.spec.whatwg.org/#concept-request) whose [URL](https://fetch.spec.whatwg.org/#concept-request-url) is url, [client](https://fetch.spec.whatwg.org/#concept-request-client) is the element's [node document](https://dom.spec.whatwg.org/#concept-node-document)'s [relevant settings object](https://html.spec.whatwg.org/multipage/webappapis.html#relevant-settings-object), [destination](https://fetch.spec.whatwg.org/#concept-request-destination) is "`object`", [credentials mode](https://fetch.spec.whatwg.org/#concept-request-credentials-mode) is "`include`", [mode](https://fetch.spec.whatwg.org/#concept-request-mode) is "`navigate`", [initiator type](https://fetch.spec.whatwg.org/#request-initiator-type) is "`object`", and whose [use-URL-credentials flag](https://fetch.spec.whatwg.org/#concept-request-use-url-credentials-flag) is set.

    5.   [Fetch](https://fetch.spec.whatwg.org/#concept-fetch)request.

Fetching the resource must [delay the load event](https://html.spec.whatwg.org/multipage/parsing.html#delay-the-load-event) of the element's [node document](https://dom.spec.whatwg.org/#concept-node-document) until the [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that is [queued](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-task) by the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) once the resource has been fetched (defined next) has been run.

    6.   If the resource is not yet available (e.g. because the resource was not available in the cache, so that loading the resource required making a request over the network), then jump to the step below labeled _fallback_. The [task](https://html.spec.whatwg.org/multipage/webappapis.html#concept-task) that is [queued](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-task) by the [networking task source](https://html.spec.whatwg.org/multipage/webappapis.html#networking-task-source) once the resource is available must restart this algorithm from this step. Resources can load incrementally; user agents may opt to consider a resource "available" whenever enough data has been obtained to begin processing the resource.

    7.   If the load failed (e.g. there was an HTTP 404 error, there was a DNS error), [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `error` at the element, then jump to the step below labeled _fallback_.

    8.   Determine the resource type, as follows:

        1.   Let the resource type be unknown.

        2.   If the user agent is configured to strictly obey Content-Type headers for this resource, and the resource has [associated Content-Type metadata](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type), then let the resource type be the type specified in [the resource's Content-Type metadata](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type), and jump to the step below labeled _handler_.

This can introduce a vulnerability, wherein a site is trying to embed a resource that uses a particular type, but the remote site overrides that and instead furnishes the user agent with a resource that triggers a different type of content with different security characteristics.

        3.   Run the appropriate set of steps from the following list:

If the resource has [associated Content-Type metadata](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type)
            1.   Let binary be false.

            2.   If the type specified in [the resource's Content-Type metadata](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type) is "`text/plain`", and the result of applying the [rules for distinguishing if a resource is text or binary](https://mimesniff.spec.whatwg.org/#rules-for-text-or-binary) to the resource is that the resource is not `text/plain`, then set binary to true.

            3.   If the type specified in [the resource's Content-Type metadata](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type) is "`application/octet-stream`", then set binary to true.

            4.   If binary is false, then let the resource type be the type specified in [the resource's Content-Type metadata](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type), and jump to the step below labeled _handler_.

            5.   If there is a `type` attribute present on the `object` element, and its value is not `application/octet-stream`, then run the following steps:

                1.   If the attribute's value is a type that starts with "`image/`" that is not also an [XML MIME type](https://mimesniff.spec.whatwg.org/#xml-mime-type), then let the resource type be the type specified in that `type` attribute.

                2.   Jump to the step below labeled _handler_.

Otherwise, if the resource does not have [associated Content-Type metadata](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#content-type)
            1.   If there is a `type` attribute present on the `object` element, then let the tentative type be the type specified in that `type` attribute.

Otherwise, let tentative type be the [computed type of the resource](https://mimesniff.spec.whatwg.org/#computed-mime-type).

            2.   If tentative type is _not_`application/octet-stream`, then let resource type be tentative type and jump to the step below labeled _handler_.

        4.   If applying the [URL parser](https://url.spec.whatwg.org/#concept-url-parser) algorithm to the [URL](https://url.spec.whatwg.org/#concept-url) of the specified resource (after any redirects) results in a [URL record](https://url.spec.whatwg.org/#concept-url) whose [path](https://url.spec.whatwg.org/#concept-url-path) component matches a pattern that a [plugin](https://html.spec.whatwg.org/multipage/infrastructure.html#plugin) supports, then let resource type be the type that that plugin can handle.

For example, a plugin might say that it can handle resources with [path](https://url.spec.whatwg.org/#concept-url-path) components that end with the four character string "`.swf`".

It is possible for this step to finish, or for one of the substeps above to jump straight to the next step, with resource type still being unknown. In both cases, the next step will trigger fallback.

    9.   _Handler_: Handle the content as given by the first of the following cases that matches:

If the resource type is an [XML MIME type](https://mimesniff.spec.whatwg.org/#xml-mime-type), or if the resource type does not start with "`image/`"
If the `object` element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) is null, then [create a new child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#create-a-new-child-navigable) for the element.

Let response be the [response](https://fetch.spec.whatwg.org/#concept-response) from [fetch](https://fetch.spec.whatwg.org/#concept-fetch).

If response's [URL](https://fetch.spec.whatwg.org/#concept-response-url) does not [match `about:blank`](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#matches-about:blank), then [navigate](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) the element's [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) to response's [URL](https://fetch.spec.whatwg.org/#concept-response-url) using the element's [node document](https://dom.spec.whatwg.org/#concept-node-document), with _[historyHandling](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigation-hh)_ set to "`replace`".

The `data` attribute of the `object` element doesn't get updated if the [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) gets further [navigated](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate) to other locations.

The `object` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) its [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable).

If the resource type starts with "`image/`", and support for images has not been disabled
[Destroy a child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#destroy-a-child-navigable) given the `object` element.

Apply the [image sniffing](https://mimesniff.spec.whatwg.org/#rules-for-sniffing-images-specifically) rules to determine the type of the image.

The `object` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the specified image.

If the image cannot be rendered, e.g. because it is malformed or in an unsupported format, jump to the step below labeled _fallback_.

Otherwise
The given resource type is not supported. Jump to the step below labeled _fallback_.

If the previous step ended with the resource type being unknown, this is the case that is triggered.

    10.   The element's contents are not part of what the `object` element represents.

    11.   If the `object` element does not represent its [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable), then once the resource is completely loaded, [queue an element task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-an-element-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) given the `object` element to [fire an event](https://dom.spec.whatwg.org/#concept-event-fire) named `load` at the element.

If the element _does_ represent its [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable), then an analogous task will be queued when the created `Document` is [completely finished loading](https://html.spec.whatwg.org/multipage/document-lifecycle.html#completely-finish-loading).

    12.   Return.

4.   _Fallback_: The `object` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the element's children. This is the element's [fallback content](https://html.spec.whatwg.org/multipage/dom.html#fallback-content). [Destroy a child navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#destroy-a-child-navigable) given the element.

Due to the algorithm above, the contents of `object` elements act as [fallback content](https://html.spec.whatwg.org/multipage/dom.html#fallback-content), used only when referenced resources can't be shown (e.g. because it returned a 404 error). This allows multiple `object` elements to be nested inside each other, targeting multiple user agents with different capabilities, with the user agent picking the first one it supports.

The `object` element [potentially delays the load event](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#potentially-delays-the-load-event).

The `form` attribute is used to explicitly associate the `object` element with its [form owner](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#form-owner).

The `object` element supports [dimension attributes](https://html.spec.whatwg.org/multipage/embedded-content-other.html#dimension-attributes).

[HTMLObjectElement/contentDocument](https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement/contentDocument "The contentDocument read-only property of the HTMLObjectElement interface Returns a Document representing the active document of the object element's nested browsing context, if any; otherwise null.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 8+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLObjectElement/contentWindow](https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement/contentWindow "The contentWindow read-only property of the HTMLObjectElement interface returns a WindowProxy representing the window proxy of the object element's nested browsing context, if any; otherwise null.")

Support in all current engines.

Firefox 22+Safari 13+Chrome 53+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)17+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `willValidate`, `validity`, and `validationMessage` attributes, and the `checkValidity()`, `reportValidity()`, and `setCustomValidity()` methods, are part of the [constraint validation API](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#the-constraint-validation-api). The `form` IDL attribute is part of the element's forms API.

In this example, an HTML page is embedded in another using the `object` element.

```
<figure>
 <object data="clock.html"></object>
 <figcaption>My HTML Clock</figcaption>
</figure>
```

[← 4.8.4 Images](https://html.spec.whatwg.org/multipage/images.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.8.8 The video element →](https://html.spec.whatwg.org/multipage/media.html)
