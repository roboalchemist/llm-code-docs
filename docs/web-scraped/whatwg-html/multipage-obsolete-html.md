# Source: https://html.spec.whatwg.org/multipage/obsolete.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/obsolete.html

Published Time: Mon, 16 Mar 2026 07:32:48 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 15 Rendering](https://html.spec.whatwg.org/multipage/rendering.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [17 IANA considerations →](https://html.spec.whatwg.org/multipage/iana.html)
1.   [16 Obsolete features](https://html.spec.whatwg.org/multipage/obsolete.html#obsolete)
    1.   [16.1 Obsolete but conforming features](https://html.spec.whatwg.org/multipage/obsolete.html#obsolete-but-conforming-features)
        1.   [16.1.1 Warnings for obsolete but conforming features](https://html.spec.whatwg.org/multipage/obsolete.html#warnings-for-obsolete-but-conforming-features)

    2.   [16.2 Non-conforming features](https://html.spec.whatwg.org/multipage/obsolete.html#non-conforming-features)
    3.   [16.3 Requirements for implementations](https://html.spec.whatwg.org/multipage/obsolete.html#requirements-for-implementations)
        1.   [16.3.1 The `marquee` element](https://html.spec.whatwg.org/multipage/obsolete.html#the-marquee-element)
        2.   [16.3.2 Frames](https://html.spec.whatwg.org/multipage/obsolete.html#frames)
        3.   [16.3.3 Other elements, attributes and APIs](https://html.spec.whatwg.org/multipage/obsolete.html#other-elements,-attributes-and-apis)

16 Obsolete features[](https://html.spec.whatwg.org/multipage/obsolete.html#obsolete)
-------------------------------------------------------------------------------------

### 16.1 Obsolete but conforming features[](https://html.spec.whatwg.org/multipage/obsolete.html#obsolete-but-conforming-features)

Features listed in this section will trigger warnings in conformance checkers.

Authors should not specify a `border` attribute on an `img` element. If the attribute is present, its value must be the string "`0`". CSS should be used instead.

Authors should not specify a `charset` attribute on a `script` element. If the attribute is present, its value must be an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for "`utf-8`". (This has no effect in a document that conforms to the requirements elsewhere in this standard of being encoded as [UTF-8](https://encoding.spec.whatwg.org/#utf-8).)

Authors should not specify a `language` attribute on a `script` element. If the attribute is present, its value must be an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`JavaScript`" and either the `type` attribute must be omitted or its value must be an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`text/javascript`". The attribute should be entirely omitted instead (with the value "`JavaScript`", it has no effect), or replaced with use of the `type` attribute.

Authors should not specify a value for the `type` attribute on `script` elements that is the empty string or a [JavaScript MIME type essence match](https://mimesniff.spec.whatwg.org/#javascript-mime-type-essence-match). Instead, they should omit the attribute, which has the same effect.

Authors should not specify a `type` attribute on a `style` element. If the attribute is present, its value must be an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for "`text/css`".

Authors should not specify the `name` attribute on `a` elements. If the attribute is present, its value must not be the empty string and must neither be equal to the value of any of the [IDs](https://dom.spec.whatwg.org/#concept-id) in the element's [tree](https://dom.spec.whatwg.org/#concept-tree) other than the element's own [ID](https://dom.spec.whatwg.org/#concept-id), if any, nor be equal to the value of any of the other `name` attributes on `a` elements in the element's [tree](https://dom.spec.whatwg.org/#concept-tree). If this attribute is present and the element has an [ID](https://dom.spec.whatwg.org/#concept-id), then the attribute's value must be equal to the element's [ID](https://dom.spec.whatwg.org/#concept-id). In earlier versions of the language, this attribute was intended as a way to specify possible targets for [fragments](https://url.spec.whatwg.org/#concept-url-fragment) in [URLs](https://url.spec.whatwg.org/#concept-url). The `id` attribute should be used instead.

Authors should not, but may despite requirements to the contrary elsewhere in this specification, specify the `maxlength` and `size` attributes on `input` elements whose `type` attributes are in the [Number](https://html.spec.whatwg.org/multipage/input.html#number-state-(type=number)) state. One valid reason for using these attributes regardless is to help legacy user agents that do not support `input` elements with `type="number"` to still render the text control with a useful width.

#### 16.1.1 Warnings for obsolete but conforming features[](https://html.spec.whatwg.org/multipage/obsolete.html#warnings-for-obsolete-but-conforming-features)

To ease the transition from HTML4 Transitional documents to the language defined in _this_ specification, and to discourage certain features that are only allowed in very few circumstances, conformance checkers must warn the user when the following features are used in a document. These are generally old obsolete features that have no effect, and are allowed only to distinguish between likely mistakes (regular conformance errors) and mere vestigial markup or unusual and discouraged practices (these warnings).

The following features must be categorized as described above:

*   The presence of a `border` attribute on an `img` element if its value is the string "`0`".

*   The presence of a `charset` attribute on a `script` element if its value is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for "`utf-8`".

*   The presence of a `language` attribute on a `script` element if its value is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`JavaScript`" and if there is no `type` attribute or there is and its value is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`text/javascript`".

*   The presence of a `type` attribute on a `script` element if its value is a [JavaScript MIME type essence match](https://mimesniff.spec.whatwg.org/#javascript-mime-type-essence-match).

*   The presence of a `type` attribute on a `style` element if its value is an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for "`text/css`".

*   The presence of a `name` attribute on an `a` element, if its value is not the empty string.

*   The presence of a `maxlength` attribute on an `input` element whose `type` attribute is in the [Number](https://html.spec.whatwg.org/multipage/input.html#number-state-(type=number)) state.

*   The presence of a `size` attribute on an `input` element whose `type` attribute is in the [Number](https://html.spec.whatwg.org/multipage/input.html#number-state-(type=number)) state.

Conformance checkers must distinguish between pages that have no conformance errors and have none of these obsolete features, and pages that have no conformance errors but do have some of these obsolete features.

For example, a validator could report some pages as "Valid HTML" and others as "Valid HTML with warnings".

### 16.2 Non-conforming features[](https://html.spec.whatwg.org/multipage/obsolete.html#non-conforming-features)

Elements in the following list are entirely obsolete, and must not be used by authors:

`applet`
Use `embed` or `object` instead.

`acronym`
Use `abbr` instead.

`bgsound`
Use `audio` instead.

`dir`
Use `ul` instead.

`frame``frameset``noframes`
Either use `iframe` and CSS instead, or use server-side includes to generate complete pages with the various invariant parts merged in.

`isindex`
Use an explicit `form` and [text control](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)) combination instead.

`keygen`
For enterprise device management use cases, use native on-device management capabilities.

For certificate enrollment use cases, use the Web Cryptography API to generate a keypair for the certificate, and then export the certificate and key to allow the user to install them manually. [[WEBCRYPTO]](https://html.spec.whatwg.org/multipage/references.html#refsWEBCRYPTO)

`listing`
Use `pre` and `code` instead.

To implement a custom context menu, use script to handle the event.

`nextid`
Use GUIDs instead.

`noembed`
Use `object` instead of `embed` when fallback is necessary.

`param`
Use the `data` attribute of the `object` element to set the URL of the external resource.

`plaintext`
Use the "`text/plain`" [MIME type](https://mimesniff.spec.whatwg.org/#mime-type) instead.

`rb``rtc`
Providing the ruby base directly inside the `ruby` element or using nested `ruby` elements is sufficient.

`strike`
Use `del` instead if the element is marking an edit, otherwise use `s` instead.

`xmp`
Use `pre` and `code` instead, and escape "`<`" and "`&`" characters as "`&lt;`" and "`&amp;`" respectively.

`basefont``big``blink``center``font``marquee``multicol``nobr``spacer``tt`
Use appropriate elements or CSS instead.

Where the `tt` element would have been used for marking up keyboard input, consider the `kbd` element; for variables, consider the `var` element; for computer code, consider the `code` element; and for computer output, consider the `samp` element.

Similarly, if the `big` element is being used to denote a heading, consider using the `h1` element; if it is being used for marking up important passages, consider the `strong` element; and if it is being used for highlighting text for reference purposes, consider the `mark` element.

See also the [text-level semantics usage summary](https://html.spec.whatwg.org/multipage/text-level-semantics.html#usage-summary) for more suggestions with examples.

* * *

The following attributes are obsolete (though the elements are still part of the language), and must not be used by authors:

`charset` on `a` elements`charset` on `link` elements
Use an HTTP ``Content-Type`` header on the linked resource instead.

`charset` on `script` elements (except as noted in the previous section)
Omit the attribute. Both documents and scripts are required to use [UTF-8](https://encoding.spec.whatwg.org/#utf-8), so it is redundant to specify it on the `script` element since it inherits from the document.

`coords` on `a` elements`shape` on `a` elements
Use `area` instead of `a` for image maps.

`methods` on `a` elements`methods` on `link` elements
Use the HTTP OPTIONS feature instead.

`name` on `a` elements (except as noted in the previous section)`name` on `embed` elements`name` on `img` elements`name` on `option` elements
Use the `id` attribute instead.

`rev` on `a` elements`rev` on `link` elements
Use the `rel` attribute instead, with an opposite term. (For example, instead of `rev="made"`, use `rel="author"`.)

`urn` on `a` elements`urn` on `link` elements
Specify the preferred persistent identifier using the `href` attribute instead.

`accept` on `form` elements
Use the `accept` attribute directly on the `input` elements instead.

`hreflang` on `area` elements`type` on `area` elements
These attributes do not do anything useful, and for historical reasons there are no corresponding IDL attributes on `area` elements. Omit them altogether.

`nohref` on `area` elements
Omitting the `href` attribute is sufficient; the `nohref` attribute is unnecessary. Omit it altogether.

`profile` on `head` elements
Unnecessary. Omit it altogether.

`manifest` on `html` elements
Use service workers instead. [[SW]](https://html.spec.whatwg.org/multipage/references.html#refsSW)

`version` on `html` elements
Unnecessary. Omit it altogether.

`ismap` on `input` elements
Unnecessary. Omit it altogether. All `input` elements with a `type` attribute in the [Image Button](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)) state are processed as server-side image maps.

`usemap` on `input` elements`usemap` on `object` elements
Use the `img` element for image maps.

`longdesc` on `iframe` elements`longdesc` on `img` elements
Use a regular `a` element to link to the description, or (in the case of images) use an [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map) to provide a link from the image to the image's description.

`lowsrc` on `img` elements
Use a progressive JPEG image (given in the `src` attribute), instead of using two separate images.

`target` on `link` elements
Unnecessary. Omit it altogether.

 on elements
To implement a custom context menu, use script to handle the event. For toolbar menus, omit the attribute.

 on elements on all elements`onshow` on all elements
To implement a custom context menu, use script to handle the event.

`scheme` on `meta` elements
Use only one scheme per field, or make the scheme declaration part of the value.

`archive` on `object` elements`classid` on `object` elements`code` on `object` elements`codebase` on `object` elements`codetype` on `object` elements
Use the `data` and `type` attributes to invoke [plugins](https://html.spec.whatwg.org/multipage/infrastructure.html#plugin).

`declare` on `object` elements
Repeat the `object` element completely each time the resource is to be reused.

`standby` on `object` elements
Optimize the linked resource so that it loads quickly or, at least, incrementally.

`typemustmatch` on `object` elements
Avoid using `object` elements with untrusted resources.

`language` on `script` elements (except as noted in the previous section)
Omit the attribute for JavaScript; for [data blocks](https://html.spec.whatwg.org/multipage/scripting.html#data-block), use the `type` attribute instead.

`event` on `script` elements`for` on `script` elements
Use DOM events mechanisms to register event listeners. [[DOM]](https://html.spec.whatwg.org/multipage/references.html#refsDOM)

`type` on `style` elements (except as noted in the previous section)
Omit the attribute for CSS; for [data blocks](https://html.spec.whatwg.org/multipage/scripting.html#data-block), use `script` as the container instead of `style`.

`datapagesize` on `table` elements
Unnecessary. Omit it altogether.

`summary` on `table` elements
Use one of the [techniques for describing tables](https://html.spec.whatwg.org/multipage/tables.html#table-descriptions-techniques) given in the `table` section instead.

`abbr` on `td` elements
Use text that begins in an unambiguous and terse manner, and include any more elaborate text after that. The `title` attribute can also be useful in including more detailed text, so that the cell's contents can be made terse. If it's a heading, use `th` (which has an `abbr` attribute).

`axis` on `td` and `th` elements
Use the `scope` attribute on the relevant `th`.

`scope` on `td` elements
Use `th` elements for heading cells.

`datasrc` on `a`, `button`, `div`, `frame`, `iframe`, `img`, `input`, `label`, `legend`, `marquee`, `object`, `option`, `select`, `span`, `table`, and `textarea` elements`datafld` on `a`, `button`, `div`, `fieldset`, `frame`, `iframe`, `img`, `input`, `label`, `legend`, `marquee`, `object`, `select`, `span`, and `textarea` elements`dataformatas` on `button`, `div`, `input`, `label`, `legend`, `marquee`, `object`, `option`, `select`, `span`, and `table` elements
Use script and a mechanism such as `XMLHttpRequest` to populate the page dynamically. [[XHR]](https://html.spec.whatwg.org/multipage/references.html#refsXHR)

`dropzone` on all elements
Use script to handle the `dragenter` and `dragover` events instead.

`alink` on `body` elements`bgcolor` on `body` elements`bottommargin` on `body` elements`leftmargin` on `body` elements`link` on `body` elements`marginheight` on `body` elements`marginwidth` on `body` elements`rightmargin` on `body` elements`text` on `body` elements`topmargin` on `body` elements`vlink` on `body` elements`clear` on `br` elements`align` on `caption` elements`align` on `col` elements`char` on `col` elements`charoff` on `col` elements`valign` on `col` elements`width` on `col` elements`align` on `div` elements`compact` on `dl` elements`align` on `embed` elements`hspace` on `embed` elements`vspace` on `embed` elements`align` on `hr` elements`color` on `hr` elements`noshade` on `hr` elements`size` on `hr` elements`width` on `hr` elements`align` on `h1`—`h6` elements`align` on `iframe` elements`allowtransparency` on `iframe` elements`frameborder` on `iframe` elements`framespacing` on `iframe` elements`hspace` on `iframe` elements`marginheight` on `iframe` elements`marginwidth` on `iframe` elements`scrolling` on `iframe` elements`vspace` on `iframe` elements`align` on `input` elements`border` on `input` elements`hspace` on `input` elements`vspace` on `input` elements`align` on `img` elements`border` on `img` elements (except as noted in the previous section)`hspace` on `img` elements`vspace` on `img` elements`align` on `legend` elements`type` on `li` elements on elements`align` on `object` elements`border` on `object` elements`hspace` on `object` elements`vspace` on `object` elements`compact` on `ol` elements`align` on `p` elements`width` on `pre` elements`align` on `table` elements`bgcolor` on `table` elements`border` on `table` elements`bordercolor` on `table` elements`cellpadding` on `table` elements`cellspacing` on `table` elements`frame` on `table` elements`height` on `table` elements`rules` on `table` elements`width` on `table` elements`align` on `tbody`, `thead`, and `tfoot` elements`char` on `tbody`, `thead`, and `tfoot` elements`charoff` on `tbody`, `thead`, and `tfoot` elements`height` on `thead`, `tbody`, and `tfoot` elements`valign` on `tbody`, `thead`, and `tfoot` elements`align` on `td` and `th` elements`bgcolor` on `td` and `th` elements`char` on `td` and `th` elements`charoff` on `td` and `th` elements`height` on `td` and `th` elements`nowrap` on `td` and `th` elements`valign` on `td` and `th` elements`width` on `td` and `th` elements`align` on `tr` elements`bgcolor` on `tr` elements`char` on `tr` elements`charoff` on `tr` elements`height` on `tr` elements`valign` on `tr` elements`compact` on `ul` elements`type` on `ul` elements`background` on `body`, `table`, `thead`, `tbody`, `tfoot`, `tr`, `td`, and `th` elements
Use CSS instead.

### 16.3 Requirements for implementations[](https://html.spec.whatwg.org/multipage/obsolete.html#requirements-for-implementations)

#### 16.3.1 The `marquee` element[](https://html.spec.whatwg.org/multipage/obsolete.html#the-marquee-element)

The `marquee` element is a presentational element that animates content. CSS transitions and animations are a more appropriate mechanism. [[CSSANIMATIONS]](https://html.spec.whatwg.org/multipage/references.html#refsCSSANIMATIONS)[[CSSTRANSITIONS]](https://html.spec.whatwg.org/multipage/references.html#refsCSSTRANSITIONS)

The `marquee` element must implement the `HTMLMarqueeElement` interface.

```
[Exposed=Window]
interface HTMLMarqueeElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute DOMString behavior;
  [CEReactions, Reflect] attribute DOMString bgColor;
  [CEReactions, Reflect] attribute DOMString direction;
  [CEReactions, Reflect] attribute DOMString height;
  [CEReactions, Reflect] attribute unsigned long hspace;
  [CEReactions] attribute long loop;
  [CEReactions, Reflect, ReflectDefault=6] attribute unsigned long scrollAmount;
  [CEReactions, Reflect, ReflectDefault=85] attribute unsigned long scrollDelay;
  [CEReactions, Reflect] attribute boolean trueSpeed;
  [CEReactions, Reflect] attribute unsigned long vspace;
  [CEReactions, Reflect] attribute DOMString width;

  undefined start();
  undefined stop();
};
```

A `marquee` element can be turned on or turned off. When it is created, it is [turned on](https://html.spec.whatwg.org/multipage/obsolete.html#concept-marquee-on).

When the `start()` method is called, the `marquee` element must be [turned on](https://html.spec.whatwg.org/multipage/obsolete.html#concept-marquee-on).

When the `stop()` method is called, the `marquee` element must be [turned off](https://html.spec.whatwg.org/multipage/obsolete.html#concept-marquee-off).

* * *

The `behavior` content attribute on `marquee` elements is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states (all non-conforming):

| Keyword | State |
| --- | --- |
| `scroll` | scroll |
| `slide` | slide |
| `alternate` | alternate |

* * *

The `direction` content attribute on `marquee` elements is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states (all non-conforming):

| Keyword | State |
| --- | --- |
| `left` | left |
| `right` | right |
| `up` | up |
| `down` | down |

* * *

The `truespeed` content attribute on `marquee` elements is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute).

* * *

A `marquee` element has a marquee scroll interval, which is obtained as follows:

1.   If the element has a `scrolldelay` attribute, and parsing its value using the [rules for parsing non-negative integers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-non-negative-integers) does not return an error, then let delay be the parsed value. Otherwise, let delay be 85.

2.   If the element does not have a `truespeed` attribute, and the delay value is less than 60, then let delay be 60 instead.

3.   The [marquee scroll interval](https://html.spec.whatwg.org/multipage/obsolete.html#marquee-scroll-interval) is delay, interpreted in milliseconds.

* * *

A `marquee` element has a marquee scroll distance, which, if the element has a `scrollamount` attribute, and parsing its value using the [rules for parsing non-negative integers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-non-negative-integers) does not return an error, is the parsed value interpreted in [CSS pixels](https://drafts.csswg.org/css-values/#px), and otherwise is 6 [CSS pixels](https://drafts.csswg.org/css-values/#px).

* * *

A `marquee` element has a marquee loop count, which, if the element has a `loop` attribute, and parsing its value using the [rules for parsing integers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-integers) does not return an error or a number less than 1, is the parsed value, and otherwise is −1.

The `loop` IDL attribute, on getting, must return the element's [marquee loop count](https://html.spec.whatwg.org/multipage/obsolete.html#marquee-loop-count); and on setting, if the new value is different than the element's [marquee loop count](https://html.spec.whatwg.org/multipage/obsolete.html#marquee-loop-count) and either greater than zero or equal to −1, must set the element's `loop` content attribute (adding it if necessary) to the [valid integer](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-integer) that represents the new value. (Other values are ignored.)

A `marquee` element also has a marquee current loop index, which is zero when the element is created.

The rendering layer will occasionally increment the marquee current loop index, which must cause the following steps to be run:

1.   If the [marquee loop count](https://html.spec.whatwg.org/multipage/obsolete.html#marquee-loop-count) is −1, then return.

2.   Increment the [marquee current loop index](https://html.spec.whatwg.org/multipage/obsolete.html#marquee-current-loop-index) by one.

3.   If the [marquee current loop index](https://html.spec.whatwg.org/multipage/obsolete.html#marquee-current-loop-index) is now greater than or equal to the element's [marquee loop count](https://html.spec.whatwg.org/multipage/obsolete.html#marquee-loop-count), [turn off](https://html.spec.whatwg.org/multipage/obsolete.html#concept-marquee-off) the `marquee` element.

* * *

#### 16.3.2 Frames[](https://html.spec.whatwg.org/multipage/obsolete.html#frames)

The `frameset` element acts as [the body element](https://html.spec.whatwg.org/multipage/dom.html#the-body-element-2) in documents that use frames.

The `frameset` element must implement the `HTMLFrameSetElement` interface.

```
[Exposed=Window]
interface HTMLFrameSetElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute DOMString cols;
  [CEReactions, Reflect] attribute DOMString rows;
};
HTMLFrameSetElement includes WindowEventHandlers;
```

The `frameset` element exposes as [event handler content attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes) a number of the [event handlers](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) of the `Window` object. It also mirrors their [event handler IDL attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-idl-attributes).

The [event handlers](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) of the `Window` object named by the [`Window`-reflecting body element event handler set](https://html.spec.whatwg.org/multipage/webappapis.html#window-reflecting-body-element-event-handler-set), exposed on the `frameset` element, replace the generic [event handlers](https://html.spec.whatwg.org/multipage/webappapis.html#event-handlers) with the same names normally supported by [HTML elements](https://html.spec.whatwg.org/multipage/infrastructure.html#html-elements).

* * *

The `frame` element has a [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) similar to the `iframe` element, but rendered within a `frameset` element.

Whenever a `frame` element with a non-null [content navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#content-navigable) has its `src` attribute set, changed, or removed, the user agent must [process the `frame` attributes](https://html.spec.whatwg.org/multipage/obsolete.html#process-the-frame-attributes).

The `frame` element [potentially delays the load event](https://html.spec.whatwg.org/multipage/iframe-embed-object.html#potentially-delays-the-load-event).

The `frame` element must implement the `HTMLFrameElement` interface.

```
[Exposed=Window]
interface HTMLFrameElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute DOMString name;
  [CEReactions, Reflect] attribute DOMString scrolling;
  [CEReactions, ReflectURL] attribute USVString src;
  [CEReactions, Reflect] attribute DOMString frameBorder;
  [CEReactions, ReflectURL] attribute USVString longDesc;
  [CEReactions, Reflect] attribute boolean noResize;
  readonly attribute Document? contentDocument;
  readonly attribute WindowProxy? contentWindow;

  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString marginHeight;
  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString marginWidth;
};
```

#### 16.3.3 Other elements, attributes and APIs[](https://html.spec.whatwg.org/multipage/obsolete.html#other-elements,-attributes-and-apis)

User agents must treat `acronym` elements in a manner equivalent to `abbr` elements in terms of semantics and for purposes of rendering.

* * *

```
partial interface HTMLAnchorElement {
  [CEReactions, Reflect] attribute DOMString coords;
  [CEReactions, Reflect] attribute DOMString charset;
  [CEReactions, Reflect] attribute DOMString name;
  [CEReactions, Reflect] attribute DOMString rev;
  [CEReactions, Reflect] attribute DOMString shape;
};
```

* * *

```
partial interface HTMLAreaElement {
  [CEReactions, Reflect] attribute boolean noHref;
};
```

* * *

```
partial interface HTMLBodyElement {
  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString text;
  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString link;
  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString vLink;
  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString aLink;
  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString bgColor;
  [CEReactions, Reflect] attribute DOMString background;
};
```

The `background` IDL attribute does not use [ReflectURL](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#xattr-reflecturl) or `USVString` for historical reasons.

* * *

```
partial interface HTMLBRElement {
  [CEReactions, Reflect] attribute DOMString clear;
};
```

* * *

```
partial interface HTMLTableCaptionElement {
  [CEReactions, Reflect] attribute DOMString align;
};
```

* * *

```
partial interface HTMLTableColElement {
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect="char"] attribute DOMString ch;
  [CEReactions, Reflect="charoff"] attribute DOMString chOff;
  [CEReactions, Reflect] attribute DOMString vAlign;
  [CEReactions, Reflect] attribute DOMString width;
};
```

* * *

User agents must treat `dir` elements in a manner equivalent to `ul` elements in terms of semantics and for purposes of rendering.

The `dir` element must implement the `HTMLDirectoryElement` interface.

```
[Exposed=Window]
interface HTMLDirectoryElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute boolean compact;
};
```

* * *

```
partial interface HTMLDivElement {
  [CEReactions, Reflect] attribute DOMString align;
};
```

* * *

```
partial interface HTMLDListElement {
  [CEReactions, Reflect] attribute boolean compact;
};
```

* * *

```
partial interface HTMLEmbedElement {
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect] attribute DOMString name;
};
```

* * *

The `font` element must implement the `HTMLFontElement` interface.

```
[Exposed=Window]
interface HTMLFontElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString color;
  [CEReactions, Reflect] attribute DOMString face;
  [CEReactions, Reflect] attribute DOMString size; 
};
```

* * *

```
partial interface HTMLHeadingElement {
  [CEReactions, Reflect] attribute DOMString align;
};
```

* * *

The `profile` IDL attribute on `head` elements (with the `HTMLHeadElement` interface) is intentionally omitted. Unless so required by [another applicable specification](https://html.spec.whatwg.org/multipage/infrastructure.html#other-applicable-specifications), implementations would therefore not support this attribute. (It is mentioned here as it was defined in a previous version of DOM.)

* * *

```
partial interface HTMLHRElement {
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect] attribute DOMString color;
  [CEReactions, Reflect] attribute boolean noShade;
  [CEReactions, Reflect] attribute DOMString size;
  [CEReactions, Reflect] attribute DOMString width;
};
```

* * *

```
partial interface HTMLHtmlElement {
  [CEReactions, Reflect] attribute DOMString version;
};
```

* * *

```
partial interface HTMLIFrameElement {
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect] attribute DOMString scrolling;
  [CEReactions, Reflect] attribute DOMString frameBorder;
  [CEReactions, ReflectURL] attribute USVString longDesc;

  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString marginHeight;
  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString marginWidth;
};
```

* * *

```
partial interface HTMLImageElement {
  [CEReactions, Reflect] attribute DOMString name;
  [CEReactions, ReflectURL] attribute USVString lowsrc;
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect] attribute unsigned long hspace;
  [CEReactions, Reflect] attribute unsigned long vspace;
  [CEReactions, ReflectURL] attribute USVString longDesc;

  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString border;
};
```

* * *

```
partial interface HTMLInputElement {
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect] attribute DOMString useMap;
};
```

* * *

```
partial interface HTMLLegendElement {
  [CEReactions, Reflect] attribute DOMString align;
};
```

* * *

```
partial interface HTMLLIElement {
  [CEReactions, Reflect] attribute DOMString type;
};
```

* * *

```
partial interface HTMLLinkElement {
  [CEReactions, Reflect] attribute DOMString charset;
  [CEReactions, Reflect] attribute DOMString rev;
  [CEReactions, Reflect] attribute DOMString target;
};
```

* * *

User agents must treat `listing` elements in a manner equivalent to `pre` elements in terms of semantics and for purposes of rendering.

* * *

```
partial interface HTMLMenuElement {
  [CEReactions, Reflect] attribute boolean compact;
};
```

* * *

```
partial interface HTMLMetaElement {
  [CEReactions, Reflect] attribute DOMString scheme;
};
```

User agents may treat the `scheme` content attribute on the `meta` element as an extension of the element's `name` content attribute when processing a `meta` element with a `name` attribute whose value is one that the user agent recognizes as supporting the `scheme` attribute.

User agents are encouraged to ignore the `scheme` attribute and instead process the value given to the metadata name as if it had been specified for each expected value of the `scheme` attribute.

For example, if the user agent acts on `meta` elements with `name` attributes having the value "eGMS.subject.keyword", and knows that the `scheme` attribute is used with this metadata name, then it could take the `scheme` attribute into account, acting as if it was an extension of the `name` attribute. Thus the following two `meta` elements could be treated as two elements giving values for two different metadata names, one consisting of a combination of "eGMS.subject.keyword" and "LGCL", and the other consisting of a combination of "eGMS.subject.keyword" and "ORLY":

```
<!-- this markup is invalid -->
<meta name="eGMS.subject.keyword" scheme="LGCL" content="Abandoned vehicles">
<meta name="eGMS.subject.keyword" scheme="ORLY" content="Mah car: kthxbye">
```

The suggested processing of this markup, however, would be equivalent to the following:

```
<meta name="eGMS.subject.keyword" content="Abandoned vehicles">
<meta name="eGMS.subject.keyword" content="Mah car: kthxbye">
```

* * *

[HTMLObjectElement/useMap](https://developer.mozilla.org/en-US/docs/Web/API/HTMLObjectElement/useMap "The useMap property of the HTMLObjectElement interface returns a string that reflects the usemap HTML attribute, specifying a <map> element to use.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 6+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

```
partial interface HTMLObjectElement {
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect] attribute DOMString archive;
  [CEReactions, Reflect] attribute DOMString code;
  [CEReactions, Reflect] attribute boolean declare;
  [CEReactions, Reflect] attribute unsigned long hspace;
  [CEReactions, Reflect] attribute DOMString standby;
  [CEReactions, Reflect] attribute unsigned long vspace;
  [CEReactions, ReflectURL] attribute DOMString codeBase;
  [CEReactions, Reflect] attribute DOMString codeType;
  [CEReactions, Reflect] attribute DOMString useMap;

  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString border;
};
```

* * *

```
partial interface HTMLOListElement {
  [CEReactions, Reflect] attribute boolean compact;
};
```

* * *

```
partial interface HTMLParagraphElement {
  [CEReactions, Reflect] attribute DOMString align;
};
```

* * *

The `param` element must implement the `HTMLParamElement` interface.

```
[Exposed=Window]
interface HTMLParamElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute DOMString name;
  [CEReactions, Reflect] attribute DOMString value;
  [CEReactions, Reflect] attribute DOMString type;
  [CEReactions, Reflect] attribute DOMString valueType;
};
```

* * *

User agents must treat `plaintext` elements in a manner equivalent to `pre` elements in terms of semantics and for purposes of rendering. (The parser has special behavior for this element, though.)

* * *

```
partial interface HTMLPreElement {
  [CEReactions, Reflect] attribute long width;
};
```

* * *

```
partial interface HTMLStyleElement {
  [CEReactions, Reflect] attribute DOMString type;
};
```

* * *

```
partial interface HTMLScriptElement {
  [CEReactions, Reflect] attribute DOMString charset;
  [CEReactions, Reflect] attribute DOMString event;
  [CEReactions, Reflect="for"] attribute DOMString htmlFor;
};
```

* * *

```
partial interface HTMLTableElement {
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect] attribute DOMString border;
  [CEReactions, Reflect] attribute DOMString frame;
  [CEReactions, Reflect] attribute DOMString rules;
  [CEReactions, Reflect] attribute DOMString summary;
  [CEReactions, Reflect] attribute DOMString width;

  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString bgColor;
  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString cellPadding;
  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString cellSpacing;
};
```

* * *

```
partial interface HTMLTableSectionElement {
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect="char"] attribute DOMString ch;
  [CEReactions, Reflect="charoff"] attribute DOMString chOff;
  [CEReactions, Reflect] attribute DOMString vAlign;
};
```

* * *

```
partial interface HTMLTableCellElement {
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect] attribute DOMString axis;
  [CEReactions, Reflect] attribute DOMString height;
  [CEReactions, Reflect] attribute DOMString width;

  [CEReactions, Reflect="char"] attribute DOMString ch;
  [CEReactions, Reflect="charoff"] attribute DOMString chOff;
  [CEReactions, Reflect] attribute boolean noWrap;
  [CEReactions, Reflect] attribute DOMString vAlign;

  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString bgColor;
};
```

* * *

```
partial interface HTMLTableRowElement {
  [CEReactions, Reflect] attribute DOMString align;
  [CEReactions, Reflect="char"] attribute DOMString ch;
  [CEReactions, Reflect="charoff"] attribute DOMString chOff;
  [CEReactions, Reflect] attribute DOMString vAlign;

  [CEReactions, Reflect] attribute [LegacyNullToEmptyString] DOMString bgColor;
};
```

* * *

```
partial interface HTMLUListElement {
  [CEReactions, Reflect] attribute boolean compact;
  [CEReactions, Reflect] attribute DOMString type;
};
```

* * *

User agents must treat `xmp` elements in a manner equivalent to `pre` elements in terms of semantics and for purposes of rendering. (The parser has special behavior for this element though.)

* * *

```
partial interface Document {
  [CEReactions] attribute [LegacyNullToEmptyString] DOMString fgColor;
  [CEReactions] attribute [LegacyNullToEmptyString] DOMString linkColor;
  [CEReactions] attribute [LegacyNullToEmptyString] DOMString vlinkColor;
  [CEReactions] attribute [LegacyNullToEmptyString] DOMString alinkColor;
  [CEReactions] attribute [LegacyNullToEmptyString] DOMString bgColor;

  [SameObject] readonly attribute HTMLCollection anchors;
  [SameObject] readonly attribute HTMLCollection applets;

  undefined clear();
  undefined captureEvents();
  undefined releaseEvents();

  [SameObject] readonly attribute HTMLAllCollection all;
};
```

The attributes of the `Document` object listed in the first column of the following table must [reflect](https://html.spec.whatwg.org/multipage/common-dom-interfaces.html#reflect) the content attribute on [the body element](https://html.spec.whatwg.org/multipage/dom.html#the-body-element-2) with the name given in the corresponding cell in the second column on the same row, if [the body element](https://html.spec.whatwg.org/multipage/dom.html#the-body-element-2) is a `body` element (as opposed to a `frameset` element). When there is no [body element](https://html.spec.whatwg.org/multipage/dom.html#the-body-element-2) or if it is a `frameset` element, the attributes must instead return the empty string on getting and do nothing on setting.

| IDL attribute | Content attribute |
| --- | --- |
| `fgColor` | `text` |
| `linkColor` | `link` |
| `vlinkColor` | `vlink` |
| `alinkColor` | `alink` |
| `bgColor` | `bgcolor` |

* * *

The `anchors` attribute must return an `HTMLCollection` rooted at the `Document` node, whose filter matches only `a` elements with `name` attributes.

The `applets` attribute must return an `HTMLCollection` rooted at the `Document` node, whose filter matches nothing. (It exists for historical reasons.)

The `clear()`, `captureEvents()`, and `releaseEvents()` methods must do nothing.

* * *

The `all` attribute must return an `HTMLAllCollection` rooted at the `Document` node, whose filter matches all elements.

* * *

```
partial interface Window {
  undefined captureEvents();
  undefined releaseEvents();

  [Replaceable, SameObject] readonly attribute External external;
};
```

The `captureEvents()` and `releaseEvents()` methods must do nothing.

The `external` attribute of the `Window` interface must return an instance of the `External` interface:

```
[Exposed=Window]
interface External {
  undefined AddSearchProvider();
  undefined IsSearchProviderInstalled();
};
```

The `AddSearchProvider()` and `IsSearchProviderInstalled()` methods must do nothing.

[← 15 Rendering](https://html.spec.whatwg.org/multipage/rendering.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [17 IANA considerations →](https://html.spec.whatwg.org/multipage/iana.html)
