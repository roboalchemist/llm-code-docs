# Source: https://html.spec.whatwg.org/multipage/embedded-content.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/embedded-content.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 4.7 Edits](https://html.spec.whatwg.org/multipage/edits.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.8.4 Images →](https://html.spec.whatwg.org/multipage/images.html)
1.       1.   [4.8 Embedded content](https://html.spec.whatwg.org/multipage/embedded-content.html#embedded-content)
        1.   [4.8.1 The `picture` element](https://html.spec.whatwg.org/multipage/embedded-content.html#the-picture-element)
        2.   [4.8.2 The `source` element](https://html.spec.whatwg.org/multipage/embedded-content.html#the-source-element)
        3.   [4.8.3 The `img` element](https://html.spec.whatwg.org/multipage/embedded-content.html#the-img-element)

### 4.8 Embedded content[](https://html.spec.whatwg.org/multipage/embedded-content.html#embedded-content)

#### 4.8.1 The `picture` element[](https://html.spec.whatwg.org/multipage/embedded-content.html#the-picture-element)

[Element/picture](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture "The <picture> HTML element contains zero or more <source> elements and one <img> element to offer alternative versions of an image for different display/device scenarios.")

Support in all current engines.

Firefox 38+Safari 9.1+Chrome 38+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)13+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLPictureElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLPictureElement "The HTMLPictureElement interface represents a <picture> HTML element. It doesn't implement specific properties or methods.")

Support in all current engines.

Firefox 38+Safari 9.1+Chrome 38+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)13+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):Zero or more `source` elements, followed by one `img` element, optionally intermixed with [script-supporting elements](https://html.spec.whatwg.org/multipage/dom.html#script-supporting-elements-2).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)[Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-picture).[For implementers](https://w3c.github.io/html-aam/#el-picture).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLPictureElement : HTMLElement {
  [HTMLConstructor] constructor();
};
```

The `picture` element is a container which provides multiple sources to its contained `img` element to allow authors to declaratively control or give hints to the user agent about which image resource to use, based on the screen pixel density, [viewport](https://drafts.csswg.org/css2/#viewport) size, image format, and other factors. It [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) its children.

The `picture` element is somewhat different from the similar-looking `video` and `audio` elements. While all of them contain `source` elements, the `source` element's `src` attribute has no meaning when the element is nested within a `picture` element, and the resource selection algorithm is different. Also, the `picture` element itself does not display anything; it merely provides a context for its contained `img` element that enables it to choose from multiple [URLs](https://url.spec.whatwg.org/#concept-url).

#### 4.8.2 The `source` element[](https://html.spec.whatwg.org/multipage/embedded-content.html#the-source-element)

[Element/source](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source "The <source> HTML element specifies multiple media resources for the <picture>, the <audio> element, or the <video> element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for image file formats and media file formats.")

Support in all current engines.

Firefox 3.5+Safari 3.1+Chrome 3+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLSourceElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSourceElement "The HTMLSourceElement interface provides special properties (beyond the regular HTMLElement object interface it also has available to it by inheritance) for manipulating <source> elements.")

Support in all current engines.

Firefox 3.5+Safari 3.1+Chrome 3+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):None.[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):As a child of a `picture` element, before the `img` element.As a child of a [media element](https://html.spec.whatwg.org/multipage/media.html#media-element), before any [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) or `track` elements.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Nothing](https://html.spec.whatwg.org/multipage/dom.html#concept-content-nothing).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):No [end tag](https://html.spec.whatwg.org/multipage/syntax.html#syntax-end-tag).[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`type` — Type of embedded resource `media` — Applicable media `src` (in `audio` or `video`) — Address of the resource `srcset` (in `picture`) — Images to use in different situations, e.g., high-resolution displays, small monitors, etc. `sizes` (in `picture`) — Image sizes for different page layouts `width` (in `picture`) — Horizontal dimension `height` (in `picture`) — Vertical dimension [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-source).[For implementers](https://w3c.github.io/html-aam/#el-source).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLSourceElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, ReflectURL] attribute USVString src;
  [CEReactions, Reflect] attribute DOMString type;
  [CEReactions, Reflect] attribute USVString srcset;
  [CEReactions, Reflect] attribute DOMString sizes;
  [CEReactions, Reflect] attribute DOMString media;
  [CEReactions, Reflect] attribute unsigned long width;
  [CEReactions, Reflect] attribute unsigned long height;
};
```

The `source` element allows authors to specify multiple alternative [source sets](https://html.spec.whatwg.org/multipage/images.html#source-set) for `img` elements or multiple alternative [media resources](https://html.spec.whatwg.org/multipage/media.html#media-resource) for [media elements](https://html.spec.whatwg.org/multipage/media.html#media-element). It does not [represent](https://html.spec.whatwg.org/multipage/dom.html#represents) anything on its own.

The `type` attribute may be present. If present, the value must be a [valid MIME type string](https://mimesniff.spec.whatwg.org/#valid-mime-type).

The `media` attribute may also be present. If present, the value must contain a [valid media query list](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-media-query-list). The user agent will skip to the next `source` element if the value does not [match the environment](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#matches-the-environment).

The `media` attribute is only evaluated once during the [resource selection algorithm](https://html.spec.whatwg.org/multipage/media.html#concept-media-load-algorithm) for [media elements](https://html.spec.whatwg.org/multipage/media.html#media-element). In contrast, when using the `picture` element, the user agent will [react to changes in the environment](https://html.spec.whatwg.org/multipage/images.html#img-environment-changes).

The remainder of the requirements depend on whether the parent is a `picture` element or a [media element](https://html.spec.whatwg.org/multipage/media.html#media-element):

The `source` element's parent is a `picture` element
The `srcset` attribute must be present, and is a [srcset attribute](https://html.spec.whatwg.org/multipage/images.html#srcset-attribute).

The `srcset` attribute contributes the [image sources](https://html.spec.whatwg.org/multipage/images.html#image-source) to the [source set](https://html.spec.whatwg.org/multipage/images.html#source-set), if the `source` element is selected.

If the `srcset` attribute has any [image candidate strings](https://html.spec.whatwg.org/multipage/images.html#image-candidate-string) using a [width descriptor](https://html.spec.whatwg.org/multipage/images.html#width-descriptor), the `sizes` attribute may also be present. If, additionally, the following sibling `img` element does not [allow auto-sizes](https://html.spec.whatwg.org/multipage/embedded-content.html#allows-auto-sizes), the `sizes` attribute must be present. The `sizes` attribute is a [sizes attribute](https://html.spec.whatwg.org/multipage/images.html#sizes-attribute), which contributes the [source size](https://html.spec.whatwg.org/multipage/images.html#source-size-2) to the [source set](https://html.spec.whatwg.org/multipage/images.html#source-set), if the `source` element is selected.

If the `img` element [allows auto-sizes](https://html.spec.whatwg.org/multipage/embedded-content.html#allows-auto-sizes), then the `sizes` attribute can be omitted on previous sibling `source` elements. In such cases, it is equivalent to specifying `auto`.

The `source` element supports [dimension attributes](https://html.spec.whatwg.org/multipage/embedded-content-other.html#dimension-attributes). The `img` element can use the `width` and `height` attributes of a `source` element, instead of those on the `img` element itself, to determine its rendered dimensions and aspect-ratio, [as defined in the Rendering section](https://html.spec.whatwg.org/multipage/rendering.html#dimRendering).

The `type` attribute gives the type of the images in the [source set](https://html.spec.whatwg.org/multipage/images.html#source-set), to allow the user agent to skip to the next `source` element if it does not support the given type.

If the `type` attribute is _not_ specified, the user agent will not select a different `source` element if it finds that it does not support the image format after fetching it.

When a `source` element has a following sibling `source` element or `img` element with a `srcset` attribute specified, it must have at least one of the following:

*   A `media` attribute specified with a value that, after [stripping leading and trailing ASCII whitespace](https://infra.spec.whatwg.org/#strip-leading-and-trailing-ascii-whitespace), is not the empty string and is not an [ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive) match for the string "`all`".

*   A `type` attribute specified.

The `src` attribute must not be present.

The `source` element's parent is a [media element](https://html.spec.whatwg.org/multipage/media.html#media-element)
The `src` attribute gives the [URL](https://url.spec.whatwg.org/#concept-url) of the [media resource](https://html.spec.whatwg.org/multipage/media.html#media-resource). The value must be a [valid non-empty URL potentially surrounded by spaces](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#valid-non-empty-url-potentially-surrounded-by-spaces). This attribute must be present.

The `type` attribute gives the type of the [media resource](https://html.spec.whatwg.org/multipage/media.html#media-resource), to help the user agent determine if it can play this [media resource](https://html.spec.whatwg.org/multipage/media.html#media-resource) before fetching it. The `codecs` parameter, which certain MIME types define, might be necessary to specify exactly how the resource is encoded. [[RFC6381]](https://html.spec.whatwg.org/multipage/references.html#refsRFC6381)

Dynamically modifying a `source` element's `src` or `type` attribute when the element is already inserted in a `video` or `audio` element will have no effect. To change what is playing, just use the `src` attribute on the [media element](https://html.spec.whatwg.org/multipage/media.html#media-element) directly, possibly making use of the `canPlayType()` method to pick from amongst available resources. Generally, manipulating `source` elements manually after the document has been parsed is an unnecessarily complicated approach.

The following list shows some examples of how to use the `codecs=` MIME parameter in the `type` attribute.

H.264 Constrained baseline profile video (main and extended video compatible) level 3 and Low-Complexity AAC audio in MP4 container`<source src='video.mp4' type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>`H.264 Extended profile video (baseline-compatible) level 3 and Low-Complexity AAC audio in MP4 container`<source src='video.mp4' type='video/mp4; codecs="avc1.58A01E, mp4a.40.2"'>`H.264 Main profile video level 3 and Low-Complexity AAC audio in MP4 container`<source src='video.mp4' type='video/mp4; codecs="avc1.4D401E, mp4a.40.2"'>`H.264 'High' profile video (incompatible with main, baseline, or extended profiles) level 3 and Low-Complexity AAC audio in MP4 container`<source src='video.mp4' type='video/mp4; codecs="avc1.64001E, mp4a.40.2"'>`MPEG-4 Visual Simple Profile Level 0 video and Low-Complexity AAC audio in MP4 container`<source src='video.mp4' type='video/mp4; codecs="mp4v.20.8, mp4a.40.2"'>`MPEG-4 Advanced Simple Profile Level 0 video and Low-Complexity AAC audio in MP4 container`<source src='video.mp4' type='video/mp4; codecs="mp4v.20.240, mp4a.40.2"'>`MPEG-4 Visual Simple Profile Level 0 video and AMR audio in 3GPP container`<source src='video.3gp' type='video/3gpp; codecs="mp4v.20.8, samr"'>`Theora video and Vorbis audio in Ogg container`<source src='video.ogv' type='video/ogg; codecs="theora, vorbis"'>`Theora video and Speex audio in Ogg container`<source src='video.ogv' type='video/ogg; codecs="theora, speex"'>`Vorbis audio alone in Ogg container`<source src='audio.ogg' type='audio/ogg; codecs=vorbis'>`Speex audio alone in Ogg container`<source src='audio.spx' type='audio/ogg; codecs=speex'>`FLAC audio alone in Ogg container`<source src='audio.oga' type='audio/ogg; codecs=flac'>`Dirac video and Vorbis audio in Ogg container`<source src='video.ogv' type='video/ogg; codecs="dirac, vorbis"'>`

The `srcset` and `sizes` attributes must not be present.

If the author isn't sure if user agents will all be able to render the media resources provided, the author can listen to the `error` event on the last `source` element and trigger fallback behavior:

```
<script>
 function fallback(video) {
   // replace <video> with its contents
   while (video.hasChildNodes()) {
     if (video.firstChild instanceof HTMLSourceElement)
       video.removeChild(video.firstChild);
     else
       video.parentNode.insertBefore(video.firstChild, video);
   }
   video.parentNode.removeChild(video);
 }
</script>
<video controls autoplay>
 <source src='video.mp4' type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
 <source src='video.ogv' type='video/ogg; codecs="theora, vorbis"'
         onerror="fallback(parentNode)">
 ...
</video>
```

#### 4.8.3 The `img` element[](https://html.spec.whatwg.org/multipage/embedded-content.html#the-img-element)

[Element/img](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img "The <img> HTML element embeds an image into the document.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLImageElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement "The HTMLImageElement interface represents an HTML <img> element, providing the properties and methods used to manipulate image elements.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 8+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

[HTMLImageElement/alt](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/alt "The HTMLImageElement property alt provides fallback (alternate) text to display when the image specified by the <img> element is not loaded.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLImageElement/srcset](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/srcset "The HTMLImageElement property srcset is a string which identifies one or more image candidate strings, separated using commas (,) each specifying image resources to use under given circumstances.")

Support in all current engines.

Firefox 38+Safari 8+Chrome 34+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLImageElement/sizes](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/sizes "The HTMLImageElement property sizes allows you to specify the layout width of the image for each of a list of media conditions. This provides the ability to automatically select among different images—even images of different orientations or aspect ratios—as the document state changes to match different media conditions.")

Support in all current engines.

Firefox 38+Safari 9.1+Chrome 38+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)13+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLImageElement/useMap](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/useMap "The useMap property on the HTMLImageElement interface reflects the value of the HTML usemap attribute, which is a string providing the name of the client-side image map to apply to the image.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLImageElement/isMap](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/isMap "The HTMLImageElement property isMap is a Boolean value which indicates that the image is to be used by a server-side image map. This may only be used on images located within an <a> element.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category).[Form-associated element](https://html.spec.whatwg.org/multipage/forms.html#form-associated-element).If the element has a `usemap` attribute: [Interactive content](https://html.spec.whatwg.org/multipage/dom.html#interactive-content-2).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category) is expected.As a child of a `picture` element, after all `source` elements.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Nothing](https://html.spec.whatwg.org/multipage/dom.html#concept-content-nothing).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):No [end tag](https://html.spec.whatwg.org/multipage/syntax.html#syntax-end-tag).[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`alt` — Replacement text for use when images are not available `src` — Address of the resource `srcset` — Images to use in different situations, e.g., high-resolution displays, small monitors, etc. `sizes` — Image sizes for different page layouts `crossorigin` — How the element handles crossorigin requests `usemap` — Name of [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map) to use `ismap` — Whether the image is a server-side image map `width` — Horizontal dimension `height` — Vertical dimension `referrerpolicy` — [Referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy) for [fetches](https://fetch.spec.whatwg.org/#concept-fetch) initiated by the element `decoding` — Decoding hint to use when processing this image for presentation `loading` — Used when determining loading deferral `fetchpriority` — Sets the [priority](https://fetch.spec.whatwg.org/#request-priority) for [fetches](https://fetch.spec.whatwg.org/#concept-fetch) initiated by the element [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):If the element has a non-empty `alt` attribute: [for authors](https://w3c.github.io/html-aria/#el-img); [for implementers](https://w3c.github.io/html-aam/#el-img).Otherwise: [for authors](https://w3c.github.io/html-aria/#el-img-empty-alt); [for implementers](https://w3c.github.io/html-aam/#el-img-empty-alt).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window,
 LegacyFactoryFunction=Image(optional unsigned long width, optional unsigned long height)]
interface HTMLImageElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute DOMString alt;
  [CEReactions, ReflectURL] attribute USVString src;
  [CEReactions, Reflect] attribute USVString srcset;
  [CEReactions, Reflect] attribute DOMString sizes;
  [CEReactions] attribute DOMString? crossOrigin;
  [CEReactions, Reflect] attribute DOMString useMap;
  [CEReactions, Reflect] attribute boolean isMap;
  [CEReactions, ReflectSetter] attribute unsigned long width;
  [CEReactions, ReflectSetter] attribute unsigned long height;
  readonly attribute unsigned long naturalWidth;
  readonly attribute unsigned long naturalHeight;
  readonly attribute boolean complete;
  readonly attribute USVString currentSrc;
  [CEReactions] attribute DOMString referrerPolicy;
  [CEReactions] attribute DOMString decoding;
  [CEReactions] attribute DOMString loading;
  [CEReactions] attribute DOMString fetchPriority;

  Promise<undefined> decode();

  // also has obsolete members
};
```

An `img` element represents an image.

An `img` element has a dimension attribute source, initially set to the element itself.

[HTMLImageElement/src](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/src "The HTMLImageElement property src, which reflects the HTML src attribute, specifies the image to display in the <img> element.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Element/img#attr-srcset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-srcset "The <img> HTML element embeds an image into the document.")

Support in all current engines.

Firefox 38+Safari 8+Chrome 34+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)≤18+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The image given by the `src` and `srcset` attributes, and any previous sibling `source` elements' `srcset` attributes if the parent is a `picture` element, is the embedded content; the value of the `alt` attribute provides equivalent content for those who cannot process images or who have image loading disabled (i.e., it is the `img` element's [fallback content](https://html.spec.whatwg.org/multipage/dom.html#fallback-content)).

The requirements on the `alt` attribute's value are described [in a separate section](https://html.spec.whatwg.org/multipage/images.html#alt).

At least one of the `src` and `srcset` attributes must be present.

If the `src` attribute is present, it must contain a [valid non-empty URL potentially surrounded by spaces](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#valid-non-empty-url-potentially-surrounded-by-spaces) referencing a non-interactive, optionally animated, image resource that is neither paged nor scripted.

The requirements above imply that images can be static bitmaps (e.g. PNGs, GIFs, JPEGs), single-page vector documents (single-page PDFs, XML files with an SVG document element), animated bitmaps (APNGs, animated GIFs), animated vector graphics (XML files with an SVG [document element](https://dom.spec.whatwg.org/#document-element) that use declarative SMIL animation), and so forth. However, these definitions preclude SVG files with script, multipage PDF files, interactive MNG files, HTML documents, plain text documents, and the like. [[PNG]](https://html.spec.whatwg.org/multipage/references.html#refsPNG)[[GIF]](https://html.spec.whatwg.org/multipage/references.html#refsGIF)[[JPEG]](https://html.spec.whatwg.org/multipage/references.html#refsJPEG)[[PDF]](https://html.spec.whatwg.org/multipage/references.html#refsPDF)[[XML]](https://html.spec.whatwg.org/multipage/references.html#refsXML)[[APNG]](https://html.spec.whatwg.org/multipage/references.html#refsAPNG)[[SVG]](https://html.spec.whatwg.org/multipage/references.html#refsSVG)[[MNG]](https://html.spec.whatwg.org/multipage/references.html#refsMNG)

The `srcset` attribute is a [srcset attribute](https://html.spec.whatwg.org/multipage/images.html#srcset-attribute).

The `srcset` attribute and the `src` attribute (if [width descriptors](https://html.spec.whatwg.org/multipage/images.html#width-descriptor) are not used) contribute the [image sources](https://html.spec.whatwg.org/multipage/images.html#image-source) to the [source set](https://html.spec.whatwg.org/multipage/images.html#source-set) (if no `source` element was selected).

If the `srcset` attribute is present and has any [image candidate strings](https://html.spec.whatwg.org/multipage/images.html#image-candidate-string) using a [width descriptor](https://html.spec.whatwg.org/multipage/images.html#width-descriptor), the `sizes` attribute must also be present. If the `srcset` attribute is _not_ specified, and the `loading` attribute is in the [Lazy](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-loading-lazy-state) state, the `sizes` attribute may be specified with the value "`auto`" ([ASCII case-insensitive](https://infra.spec.whatwg.org/#ascii-case-insensitive)). The `sizes` attribute is a [sizes attribute](https://html.spec.whatwg.org/multipage/images.html#sizes-attribute), which contributes the [source size](https://html.spec.whatwg.org/multipage/images.html#source-size-2) to the [source set](https://html.spec.whatwg.org/multipage/images.html#source-set) (if no `source` element was selected).

[Attributes/crossorigin](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin "The crossorigin attribute, valid on the <audio>, <img>, <link>, <script>, and <video> elements, provides support for CORS, defining how the element handles cross-origin requests, thereby enabling the configuration of the CORS requests for the element's fetched data. Depending on the element, the attribute can be a CORS settings attribute.")

Support in all current engines.

Firefox 8+Safari 6+Chrome 13+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `crossorigin` attribute is a [CORS settings attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cors-settings-attribute). Its purpose is to allow images from third-party sites that allow cross-origin access to be used with `canvas`.

The `referrerpolicy` attribute is a [referrer policy attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#referrer-policy-attribute). Its purpose is to set the [referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy) used when [fetching](https://fetch.spec.whatwg.org/#concept-fetch) the image. [[REFERRERPOLICY]](https://html.spec.whatwg.org/multipage/references.html#refsREFERRERPOLICY)

The `decoding` attribute indicates the preferred method to [decode](https://html.spec.whatwg.org/multipage/images.html#img-decoding-process) this image. The attribute, if present, must be an [image decoding hint](https://html.spec.whatwg.org/multipage/images.html#image-decoding-hint). This attribute's _[missing value default](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#missing-value-default)_ and _[invalid value default](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#invalid-value-default)_ are both the [Auto](https://html.spec.whatwg.org/multipage/images.html#attr-img-decoding-auto-state) state.

[HTMLImageElement/fetchPriority](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/fetchPriority "The fetchPriority property of the HTMLImageElement interface represents a hint given to the browser on how it should prioritize the fetch of the image relative to other images.")

Firefox No Safari🔰 preview+Chrome 102+

* * *

Opera?Edge 102+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

The `fetchpriority` attribute is a [fetch priority attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#fetch-priority-attribute). Its purpose is to set the [priority](https://fetch.spec.whatwg.org/#request-priority) used when [fetching](https://fetch.spec.whatwg.org/#concept-fetch) the image.

The `loading` attribute is a [lazy loading attribute](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#lazy-loading-attribute). Its purpose is to indicate the policy for loading images that are outside the viewport.

```
<img src="1.jpeg" alt="1">
<img src="2.jpeg" loading=eager alt="2">
<img src="3.jpeg" loading=lazy alt="3">
<div id=very-large></div> <!-- Everything after this div is below the viewport -->
<img src="4.jpeg" alt="4">
<img src="5.jpeg" loading=lazy alt="5">
```

In the example above, the images load as follows:

`1.jpeg`, `2.jpeg`, `4.jpeg`
The images load eagerly and delay the window's load event.

`3.jpeg`
The image loads when layout is known, due to being in the viewport, however it does not delay the window's load event.

`5.jpeg`
The image loads only once scrolled into the viewport, and does not delay the window's load event.

Developers are encouraged to specify a preferred aspect ratio via `width` and `height` attributes on lazy loaded images, even if CSS sets the image's width and height properties, to prevent the page layout from shifting around after the image loads.

* * *

The `img` element must not be used as a layout tool. In particular, `img` elements should not be used to display transparent images, as such images rarely convey meaning and rarely add anything useful to the document.

* * *

What an `img` element represents depends on the `src` attribute and the `alt` attribute.

If the `src` attribute is set and the `alt` attribute is set to the empty string
The image is either decorative or supplemental to the rest of the content, redundant with some other information in the document.

If the image is [available](https://html.spec.whatwg.org/multipage/images.html#img-available) and the user agent is configured to display that image, then the element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the element's image data.

Otherwise, the element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) nothing, and may be omitted completely from the rendering. User agents may provide the user with a notification that an image is present but has been omitted from the rendering.

If the `src` attribute is set and the `alt` attribute is set to a value that isn't empty
The image is a key part of the content; the `alt` attribute gives a textual equivalent or replacement for the image.

If the image is [available](https://html.spec.whatwg.org/multipage/images.html#img-available) and the user agent is configured to display that image, then the element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the element's image data.

Otherwise, the element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the text given by the `alt` attribute. User agents may provide the user with a notification that an image is present but has been omitted from the rendering.

If the `src` attribute is set and the `alt` attribute is not
The image might be a key part of the content, and there is no textual equivalent of the image available.

In a conforming document, the absence of the `alt` attribute indicates that the image is a key part of the content but that a textual replacement for the image was not available when the image was generated.

If the image is [available](https://html.spec.whatwg.org/multipage/images.html#img-available) and the user agent is configured to display that image, then the element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the element's image data.

If the image has a `src` attribute whose value is the empty string, then the element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) nothing.

Otherwise, the user agent should display some sort of indicator that there is an image that is not being rendered, and may, if requested by the user, or if so configured, or when required to provide contextual information in response to navigation, provide caption information for the image, derived as follows:

1.   If the image has a `title` attribute whose value is not the empty string, then return the value of that attribute.

2.   If the image is a descendant of a `figure` element that has a child `figcaption` element, and, ignoring the `figcaption` element and its descendants, the `figure` element has no [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2) descendants other than [inter-element whitespace](https://html.spec.whatwg.org/multipage/dom.html#inter-element-whitespace) and the `img` element, then return the contents of the first such `figcaption` element.

3.   Return nothing. (There is no caption information.)

If the `src` attribute is not set and either the `alt` attribute is set to the empty string or the `alt` attribute is not set at all
The element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) nothing.

Otherwise
The element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) the text given by the `alt` attribute.

The `alt` attribute does not represent advisory information. User agents must not present the contents of the `alt` attribute in the same way as content of the `title` attribute.

User agents may always provide the user with the option to display any image, or to prevent any image from being displayed. User agents may also apply heuristics to help the user make use of the image when the user is unable to see it, e.g. due to a visual disability or because they are using a text terminal with no graphics capabilities. Such heuristics could include, for instance, optical character recognition (OCR) of text found within the image.

While user agents are encouraged to repair cases of missing `alt` attributes, authors must not rely on such behavior. [Requirements for providing text to act as an alternative for images](https://html.spec.whatwg.org/multipage/images.html#alt) are described in detail below.

The _contents_ of `img` elements, if any, are ignored for the purposes of rendering.

* * *

The `usemap` attribute, if present, can indicate that the image has an associated [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map).

The `ismap` attribute, when used on an element that is a descendant of an `a` element with an `href` attribute, indicates by its presence that the element provides access to a server-side image map. This affects how events are handled on the corresponding `a` element.

The `ismap` attribute is a [boolean attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#boolean-attribute). The attribute must not be specified on an element that does not have an ancestor `a` element with an `href` attribute.

The `usemap` and `ismap` attributes can result in confusing behavior when used together with `source` elements with the `media` attribute specified in a `picture` element.

The `img` element supports [dimension attributes](https://html.spec.whatwg.org/multipage/embedded-content-other.html#dimension-attributes).

[HTMLImageElement/crossOrigin](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/crossOrigin "The HTMLImageElement interface's crossOrigin attribute is a string which specifies the Cross-Origin Resource Sharing (CORS) setting to use when retrieving the image.")

Support in all current engines.

Firefox 8+Safari 6+Chrome 13+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 11

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLImageElement/referrerPolicy](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/referrerPolicy "The HTMLImageElement.referrerPolicy property reflects the HTML referrerpolicy attribute of the <img> element defining which referrer is sent when fetching the resource.")

Support in all current engines.

Firefox 50+Safari 14+Chrome 52+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLImageElement/decoding](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decoding "The decoding property of the HTMLImageElement interface represents a hint given to the browser on how it should decode the image.")

Support in all current engines.

Firefox 63+Safari 11.1+Chrome 65+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[SVGImageElement/decoding](https://developer.mozilla.org/en-US/docs/Web/API/SVGImageElement/decoding "The decoding property of the SVGImageElement interface represents a hint given to the browser on how it should decode the image.")

Firefox 63+Safari No Chrome 65+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLImageElement/loading](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/loading "The HTMLImageElement property loading is a string whose value provides a hint to the user agent on how to handle the loading of the image which is currently outside the window's visual viewport.")

Support in all current engines.

Firefox 75+Safari 15.4+Chrome 77+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

`image.width [ = value ]`

[HTMLImageElement/width](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/width "The width property of the HTMLImageElement interface indicates the width at which an image is drawn in CSS pixels if it's being drawn or rendered to any visual medium such as a screen or printer. Otherwise, it's the natural, pixel density-corrected width of the image.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

`image.height [ = value ]`

[HTMLImageElement/height](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/height "The height property of the HTMLImageElement interface indicates the height at which the image is drawn, in CSS pixels if the image is being drawn or rendered to any visual medium such as the screen or a printer; otherwise, it's the natural, pixel density corrected height of the image.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

These attributes return the actual rendered dimensions of the image, or 0 if the dimensions are not known.

They can be set, to change the corresponding content attributes.

`image.naturalWidth`

[HTMLImageElement/naturalWidth](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/naturalWidth "The HTMLImageElement interface's read-only naturalWidth property returns the intrinsic (natural), density-corrected width of the image in CSS pixels.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

`image.naturalHeight`

[HTMLImageElement/naturalHeight](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/naturalHeight "The HTMLImageElement interface's naturalHeight property is a read-only value which returns the intrinsic (natural), density-corrected height of the image in CSS pixels.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

These attributes return the natural dimensions of the image, or 0 if the dimensions are not known.

`image.complete`

[HTMLImageElement/complete](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/complete "The read-only HTMLImageElement interface's complete attribute is a Boolean value which indicates whether or not the image has completely loaded.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

Returns true if the image has been completely downloaded or if no image is specified; otherwise, returns false.

`image.currentSrc`

[HTMLImageElement/currentSrc](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/currentSrc "The read-only HTMLImageElement property currentSrc indicates the URL of the image which is currently presented in the <img> element it represents.")

Support in all current engines.

Firefox 38+Safari 9.1+Chrome 38+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)13+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns the image's [absolute URL](https://url.spec.whatwg.org/#syntax-url-absolute).

`image.decode()`

[HTMLImageElement/decode](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/decode "The decode() method of the HTMLImageElement interface returns a Promise that resolves when the image is decoded and it is safe to append the image to the DOM.")

Support in all current engines.

Firefox 68+Safari 11.1+Chrome 64+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[SVGImageElement/decode](https://developer.mozilla.org/en-US/docs/Web/API/SVGImageElement/decode "The decode() method of the SVGImageElement interface initiates asynchronous decoding of an image, returning a Promise that resolves once the image data is ready for use.")

Firefox 68+Safari No Chrome 64+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

This method causes the user agent to [decode](https://html.spec.whatwg.org/multipage/images.html#img-decoding-process) the image [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel), returning a promise that fulfills when decoding is complete.

The promise will be rejected with an ["`EncodingError`"](https://webidl.spec.whatwg.org/#encodingerror)`DOMException` if the image cannot be decoded.

`image = new Image([ width [, height ] ])`

[HTMLImageElement/Image](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/Image "The Image() constructor creates a new HTMLImageElement instance. It is functionally equivalent to document.createElement('img').")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 8+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 10.1+

Returns a new `img` element, with the `width` and `height` attributes set to the values passed in the relevant arguments, if applicable.

Since the [density-corrected natural width and height](https://html.spec.whatwg.org/multipage/images.html#density-corrected-intrinsic-width-and-height) of an image take into account any orientation specified in its metadata, `naturalWidth` and `naturalHeight` reflect the dimensions after applying any rotation needed to correctly orient the image, regardless of the value of the ['image-orientation'](https://drafts.csswg.org/css-images-3/#the-image-orientation) property.

The `complete` getter steps are:

1.   If any of the following are true:

    *   both the `src` attribute and the `srcset` attribute are omitted;

    *   the `srcset` attribute is omitted and the `src` attribute's value is the empty string;

    *   the `img` element's [current request](https://html.spec.whatwg.org/multipage/images.html#current-request)'s [state](https://html.spec.whatwg.org/multipage/images.html#img-req-state) is [completely available](https://html.spec.whatwg.org/multipage/images.html#img-all) and its [pending request](https://html.spec.whatwg.org/multipage/images.html#pending-request) is null; or

    *   the `img` element's [current request](https://html.spec.whatwg.org/multipage/images.html#current-request)'s [state](https://html.spec.whatwg.org/multipage/images.html#img-req-state) is [broken](https://html.spec.whatwg.org/multipage/images.html#img-error) and its [pending request](https://html.spec.whatwg.org/multipage/images.html#pending-request) is null,

then return true.

2.   Return false.

The `decode()` method, when invoked, must perform the following steps:

1.   Let promise be a new promise.

2.   [Queue a microtask](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-microtask) to perform the following steps:

This is done because [updating the image data](https://html.spec.whatwg.org/multipage/images.html#update-the-image-data) takes place in a microtask as well. Thus, to make code such as

```
img.src = "stars.jpg";
img.decode();
```

properly decode `stars.jpg`, we need to delay any processing by one microtask. 
    1.   Let global be [this](https://webidl.spec.whatwg.org/#this)'s [relevant global object](https://html.spec.whatwg.org/multipage/webappapis.html#concept-relevant-global).

    2.   If any of the following are true:

        *   [this](https://webidl.spec.whatwg.org/#this)'s [node document](https://dom.spec.whatwg.org/#concept-node-document) is not [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active); or

        *   [this](https://webidl.spec.whatwg.org/#this)'s [current request](https://html.spec.whatwg.org/multipage/images.html#current-request)'s [state](https://html.spec.whatwg.org/multipage/images.html#img-req-state) is [broken](https://html.spec.whatwg.org/multipage/images.html#img-error),

then reject promise with an ["`EncodingError`"](https://webidl.spec.whatwg.org/#encodingerror)`DOMException`.

    3.   Otherwise, [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel), wait for one of the following cases to occur, and perform the corresponding actions:

This `img` element's [node document](https://dom.spec.whatwg.org/#concept-node-document) stops being [fully active](https://html.spec.whatwg.org/multipage/document-sequences.html#fully-active)This `img` element's [current request](https://html.spec.whatwg.org/multipage/images.html#current-request) changes or is mutated This `img` element's [current request](https://html.spec.whatwg.org/multipage/images.html#current-request)'s [state](https://html.spec.whatwg.org/multipage/images.html#img-req-state) becomes [broken](https://html.spec.whatwg.org/multipage/images.html#img-error)
[Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) with global to reject promise with an ["`EncodingError`"](https://webidl.spec.whatwg.org/#encodingerror)`DOMException`.

This `img` element's [current request](https://html.spec.whatwg.org/multipage/images.html#current-request)'s [state](https://html.spec.whatwg.org/multipage/images.html#img-req-state) becomes [completely available](https://html.spec.whatwg.org/multipage/images.html#img-all)
[Decode](https://html.spec.whatwg.org/multipage/images.html#img-decoding-process) the image.

If decoding does not need to be performed for this image (for example because it is a vector graphic) or the decoding process completes successfully, then [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) with global to resolve promise with undefined.

If decoding fails (for example due to invalid image data), then [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task) on the [DOM manipulation task source](https://html.spec.whatwg.org/multipage/webappapis.html#dom-manipulation-task-source) with global to reject promise with an ["`EncodingError`"](https://webidl.spec.whatwg.org/#encodingerror)`DOMException`.

User agents should ensure that the decoded media data stays readily available until at least the end of the next successful [update the rendering](https://html.spec.whatwg.org/multipage/webappapis.html#update-the-rendering) step in the [event loop](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop). This is an important part of the API contract, and should not be broken if at all possible. (Typically, this would only be violated in low-memory situations that require evicting decoded image data, or when the image is too large to keep in decoded form for this period of time.)

Animated images will become [completely available](https://html.spec.whatwg.org/multipage/images.html#img-all) only after all their frames are loaded. Thus, even though an implementation could decode the first frame before that point, the above steps will not do so, instead waiting until all frames are available.

3.   Return promise.

Without the `decode()` method, the process of loading an `img` element and then displaying it might look like the following:

```
const img = new Image();
img.src = "nebula.jpg";
img.onload = () => {
    document.body.appendChild(img);
};
img.onerror = () => {
    document.body.appendChild(new Text("Could not load the nebula :("));
};
```

However, this can cause notable dropped frames, as the paint that occurs after inserting the image into the DOM causes a synchronous decode on the main thread.

This can instead be rewritten using the `decode()` method:

```
const img = new Image();
img.src = "nebula.jpg";
img.decode().then(() => {
    document.body.appendChild(img);
}).catch(() => {
    document.body.appendChild(new Text("Could not load the nebula :("));
});
```

This latter form avoids the dropped frames of the original, by allowing the user agent to decode the image [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel), and only inserting it into the DOM (and thus causing it to be painted) once the decoding process is complete.

Because the `decode()` method attempts to ensure that the decoded image data is available for at least one frame, it can be combined with the `requestAnimationFrame()` API. This means it can be used with coding styles or frameworks that ensure that all DOM modifications are batched together as [animation frame callbacks](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#list-of-animation-frame-callbacks):

```
const container = document.querySelector("#container");

const { containerWidth, containerHeight } = computeDesiredSize();
requestAnimationFrame(() => {
 container.style.width = containerWidth;
 container.style.height = containerHeight;
});

// ...

const img = new Image();
img.src = "supernova.jpg";
img.decode().then(() => {
    requestAnimationFrame(() => container.appendChild(img));
});
```

A single image can have different appropriate alternative text depending on the context.

In each of the following cases, the same image is used, yet the `alt` text is different each time. The image is the coat of arms of the Carouge municipality in the canton Geneva in Switzerland.

Here it is used as a supplementary icon:

`<p>I lived in <img src="carouge.svg" alt=""> Carouge.</p>`
Here it is used as an icon representing the town:

`<p>Home town: <img src="carouge.svg" alt="Carouge"></p>`
Here it is used as part of a text on the town:

```
<p>Carouge has a coat of arms.</p>
<p><img src="carouge.svg" alt="The coat of arms depicts a lion, sitting in front of a tree."></p>
<p>It is used as decoration all over the town.</p>
```

Here it is used as a way to support a similar text where the description is given as well as, instead of as an alternative to, the image:

```
<p>Carouge has a coat of arms.</p>
<p><img src="carouge.svg" alt=""></p>
<p>The coat of arms depicts a lion, sitting in front of a tree.
It is used as decoration all over the town.</p>
```

Here it is used as part of a story:

```
<p>She picked up the folder and a piece of paper fell out.</p>
<p><img src="carouge.svg" alt="Shaped like a shield, the paper had a
red background, a green tree, and a yellow lion with its tongue
hanging out and whose tail was shaped like an S."></p>
<p>She stared at the folder. S! The answer she had been looking for all
this time was simply the letter S! How had she not seen that before? It all
came together now. The phone call where Hector had referred to a lion's tail,
the time Maria had stuck her tongue out...</p>
```

Here it is not known at the time of publication what the image will be, only that it will be a coat of arms of some kind, and thus no replacement text can be provided, and instead only a brief caption for the image is provided, in the `title` attribute:

```
<p>The last user to have uploaded a coat of arms uploaded this one:</p>
<p><img src="last-uploaded-coat-of-arms.cgi" title="User-uploaded coat of arms."></p>
```

Ideally, the author would find a way to provide real replacement text even in this case, e.g. by asking the previous user. Not providing replacement text makes the document more difficult to use for people who are unable to view images, e.g. blind users, or users or very low-bandwidth connections or who pay by the byte, or users who are forced to use a text-only web browser.

Here are some more examples showing the same picture used in different contexts, with different appropriate alternate texts each time.

```
<article>
 <h1>My cats</h1>
 <h2>Fluffy</h2>
 <p>Fluffy is my favorite.</p>
 <img src="fluffy.jpg" alt="She likes playing with a ball of yarn.">
 <p>She's just too cute.</p>
 <h2>Miles</h2>
 <p>My other cat, Miles just eats and sleeps.</p>
</article>
```

```
<article>
 <h1>Photography</h1>
 <h2>Shooting moving targets indoors</h2>
 <p>The trick here is to know how to anticipate; to know at what speed and
 what distance the subject will pass by.</p>
 <img src="fluffy.jpg" alt="A cat flying by, chasing a ball of yarn, can be
 photographed quite nicely using this technique.">
 <h2>Nature by night</h2>
 <p>To achieve this, you'll need either an extremely sensitive film, or
 immense flash lights.</p>
</article>
```

```
<article>
 <h1>About me</h1>
 <h2>My pets</h2>
 <p>I've got a cat named Fluffy and a dog named Miles.</p>
 <img src="fluffy.jpg" alt="Fluffy, my cat, tends to keep itself busy.">
 <p>My dog Miles and I like go on long walks together.</p>
 <h2>music</h2>
 <p>After our walks, having emptied my mind, I like listening to Bach.</p>
</article>
```

```
<article>
 <h1>Fluffy and the Yarn</h1>
 <p>Fluffy was a cat who liked to play with yarn. She also liked to jump.</p>
 <aside><img src="fluffy.jpg" alt="" title="Fluffy"></aside>
 <p>She would play in the morning, she would play in the evening.</p>
</article>
```

[← 4.7 Edits](https://html.spec.whatwg.org/multipage/edits.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.8.4 Images →](https://html.spec.whatwg.org/multipage/images.html)
