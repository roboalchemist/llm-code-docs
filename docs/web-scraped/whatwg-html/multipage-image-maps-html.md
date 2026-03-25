# Source: https://html.spec.whatwg.org/multipage/image-maps.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/image-maps.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 4.8.8 The video element](https://html.spec.whatwg.org/multipage/media.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.8.15 MathML →](https://html.spec.whatwg.org/multipage/embedded-content-other.html)
1.       1.           1.   [4.8.12 The `map` element](https://html.spec.whatwg.org/multipage/image-maps.html#the-map-element)
        2.   [4.8.13 The `area` element](https://html.spec.whatwg.org/multipage/image-maps.html#the-area-element)
        3.   [4.8.14 Image maps](https://html.spec.whatwg.org/multipage/image-maps.html#image-maps)
            1.   [4.8.14.1 Authoring](https://html.spec.whatwg.org/multipage/image-maps.html#authoring)
            2.   [4.8.14.2 Processing model](https://html.spec.whatwg.org/multipage/image-maps.html#image-map-processing-model)

#### 4.8.12 The `map` element[](https://html.spec.whatwg.org/multipage/image-maps.html#the-map-element)

[Element/map](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map "The <map> HTML element is used with <area> elements to define an image map (a clickable link area).")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android 4+Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLMapElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMapElement "The HTMLMapElement interface provides special properties and methods (beyond those of the regular object HTMLElement interface it also has available to it by inheritance) for manipulating the layout and presentation of map elements.")

Support in all current engines.

Firefox 1+Safari 3+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS 1+Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Transparent](https://html.spec.whatwg.org/multipage/dom.html#transparent).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):Neither tag is omissible.[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`name` — Name of [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map) to [reference](https://html.spec.whatwg.org/multipage/dom.html#referenced) from the `usemap` attribute [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):[For authors](https://w3c.github.io/html-aria/#el-map).[For implementers](https://w3c.github.io/html-aam/#el-map).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLMapElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute DOMString name;
  [SameObject] readonly attribute HTMLCollection areas;
};
```

The `map` element, in conjunction with an `img` element and any `area` element descendants, defines an [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map). The element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) its children.

The `name` attribute gives the map a name so that it can be [referenced](https://html.spec.whatwg.org/multipage/dom.html#referenced). The attribute must be present and must have a non-empty value with no [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace). The value of the `name` attribute must not be equal to the value of the `name` attribute of another `map` element in the same [tree](https://dom.spec.whatwg.org/#concept-tree). If the `id` attribute is also specified, both attributes must have the same value.

`map.areas`
Returns an `HTMLCollection` of the `area` elements in the `map`.

The `areas` attribute must return an `HTMLCollection` rooted at the `map` element, whose filter matches only `area` elements.

Image maps can be defined in conjunction with other content on the page, to ease maintenance. This example is of a page with an image map at the top of the page and a corresponding set of text links at the bottom.

```
<!DOCTYPE HTML>
<HTML LANG="EN">
<TITLE>Babies™: Toys</TITLE>
<HEADER>
 <H1>Toys</H1>
 <IMG SRC="/images/menu.gif"
      ALT="Babies™ navigation menu. Select a department to go to its page."
      USEMAP="#NAV">
</HEADER>
 ...
<FOOTER>
 <MAP NAME="NAV">
  <P>
   <A HREF="/clothes/">Clothes</A>
   <AREA ALT="Clothes" COORDS="0,0,100,50" HREF="/clothes/"> |
   <A HREF="/toys/">Toys</A>
   <AREA ALT="Toys" COORDS="100,0,200,50" HREF="/toys/"> |
   <A HREF="/food/">Food</A>
   <AREA ALT="Food" COORDS="200,0,300,50" HREF="/food/"> |
   <A HREF="/books/">Books</A>
   <AREA ALT="Books" COORDS="300,0,400,50" HREF="/books/">
  </P>
 </MAP>
</FOOTER>
```

#### 4.8.13 The `area` element[](https://html.spec.whatwg.org/multipage/image-maps.html#the-area-element)

[Element/area](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area "The <area> HTML element defines an area inside an image map that has predefined clickable areas. An image map allows geometric areas on an image to be associated with hypertext links.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer Yes

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLAreaElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAreaElement "The HTMLAreaElement interface provides special properties and methods (beyond those of the regular object HTMLElement interface it also has available to it by inheritance) for manipulating the layout and presentation of <area> elements.")

Support in all current engines.

Firefox 1+Safari 1+Chrome 1+

* * *

Opera 12.1+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 5.5+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 12.1+

[HTMLAreaElement/rel](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAreaElement/rel "The HTMLAreaElement.rel property reflects the rel attribute. It is a string containing a space-separated list of link types indicating the relationship between the resource represented by the <area> element and the current document.")

Support in all current engines.

Firefox 30+Safari 9+Chrome 54+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 11

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

[HTMLAreaElement/relList](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAreaElement/relList "The HTMLAreaElement.relList read-only property reflects the rel attribute. It is a live DOMTokenList containing the set of link types indicating the relationship between the resource represented by the <area> element and the current document.")

Support in all current engines.

Firefox 30+Safari 9+Chrome 65+

* * *

Opera 41+Edge 79+

* * *

Edge (Legacy)18 Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 41+

[Categories](https://html.spec.whatwg.org/multipage/dom.html#concept-element-categories):[Flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).[Phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2).[Contexts in which this element can be used](https://html.spec.whatwg.org/multipage/dom.html#concept-element-contexts):Where [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) is expected, but only if there is a `map` element ancestor.[Content model](https://html.spec.whatwg.org/multipage/dom.html#concept-element-content-model):[Nothing](https://html.spec.whatwg.org/multipage/dom.html#concept-content-nothing).[Tag omission in text/html](https://html.spec.whatwg.org/multipage/dom.html#concept-element-tag-omission):No [end tag](https://html.spec.whatwg.org/multipage/syntax.html#syntax-end-tag).[Content attributes](https://html.spec.whatwg.org/multipage/dom.html#concept-element-attributes):[Global attributes](https://html.spec.whatwg.org/multipage/dom.html#global-attributes)`alt` — Replacement text for use when images are not available `coords` — Coordinates for the shape to be created in an [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map)`shape` — The kind of shape to be created in an [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map)`href` — Address of the [hyperlink](https://html.spec.whatwg.org/multipage/links.html#hyperlink)`target` — [Navigable](https://html.spec.whatwg.org/multipage/document-sequences.html#navigable) for [hyperlink](https://html.spec.whatwg.org/multipage/links.html#hyperlink)[navigation](https://html.spec.whatwg.org/multipage/browsing-the-web.html#navigate)`download` — Whether to download the resource instead of navigating to it, and its filename if so `ping` — [URLs](https://url.spec.whatwg.org/#concept-url) to ping `rel` — Relationship between the location in the document containing the [hyperlink](https://html.spec.whatwg.org/multipage/links.html#hyperlink) and the destination resource `referrerpolicy` — [Referrer policy](https://w3c.github.io/webappsec-referrer-policy/#referrer-policy) for [fetches](https://fetch.spec.whatwg.org/#concept-fetch) initiated by the element [Accessibility considerations](https://html.spec.whatwg.org/multipage/dom.html#concept-element-accessibility-considerations):If the element has an `href` attribute: [for authors](https://w3c.github.io/html-aria/#el-area); [for implementers](https://w3c.github.io/html-aam/#el-area).Otherwise: [for authors](https://w3c.github.io/html-aria/#el-area-no-href); [for implementers](https://w3c.github.io/html-aam/#el-area-no-href).[DOM interface](https://html.spec.whatwg.org/multipage/dom.html#concept-element-dom):
```
[Exposed=Window]
interface HTMLAreaElement : HTMLElement {
  [HTMLConstructor] constructor();

  [CEReactions, Reflect] attribute DOMString alt;
  [CEReactions, Reflect] attribute DOMString coords;
  [CEReactions, Reflect] attribute DOMString shape;
  [CEReactions, Reflect] attribute DOMString target;
  [CEReactions, Reflect] attribute DOMString download;
  [CEReactions, Reflect] attribute USVString ping;
  [CEReactions, Reflect] attribute DOMString rel;
  [SameObject, PutForwards=value, Reflect="rel"] readonly attribute DOMTokenList relList;
  [CEReactions] attribute DOMString referrerPolicy;

  // also has obsolete members
};
HTMLAreaElement includes HyperlinkElementUtils;
HTMLAreaElement includes HTMLHyperlinkElementUtils;
```

The `area` element [represents](https://html.spec.whatwg.org/multipage/dom.html#represents) either a hyperlink with some text and a corresponding area on an [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map), or a dead area on an image map.

An `area` element with a parent node must have a `map` element ancestor.

If the `area` element has an `href` attribute, then the `area` element represents a [hyperlink](https://html.spec.whatwg.org/multipage/links.html#hyperlink). In this case, the `alt` attribute must be present. It specifies the text of the hyperlink. Its value must be text that, when presented with the texts specified for the other hyperlinks of the [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map), and with the alternative text of the image, but without the image itself, provides the user with the same kind of choice as the hyperlink would when used without its text but with its shape applied to the image. The `alt` attribute may be left blank if there is another `area` element in the same [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map) that points to the same resource and has a non-blank `alt` attribute.

If the `area` element has no `href` attribute, then the area represented by the element cannot be selected, and the `alt` attribute must be omitted.

In both cases, the `shape` and `coords` attributes specify the area.

The `shape` attribute is an [enumerated attribute](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#enumerated-attribute) with the following keywords and states:

| Keyword | Conforming | State | Brief description |
| --- | --- | --- | --- |
| `circle` |  | [Circle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-circle) | Designates a circle, using exactly three integers in the `coords` attribute. |
| `circ` | No |
| `default` |  | [Default state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-default) | This area is the whole image. (The `coords` attribute is not used.) |
| `poly` |  | [Polygon state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-poly) | Designates a polygon, using at-least six integers in the `coords` attribute. |
| `polygon` | No |
| `rect` |  | [Rectangle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-rect) | Designates a rectangle, using exactly four integers in the `coords` attribute. |
| `rectangle` | No |

The `coords` attribute must, if specified, contain a [valid list of floating-point numbers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-list-of-floating-point-numbers). This attribute gives the coordinates for the shape described by the `shape` attribute. The processing for this attribute is described as part of the [image map](https://html.spec.whatwg.org/multipage/image-maps.html#image-map) processing model.

In the circle state, `area` elements must have a `coords` attribute present, with three integers, the last of which must be non-negative. The first integer must be the distance in [CSS pixels](https://drafts.csswg.org/css-values/#px) from the left edge of the image to the center of the circle, the second integer must be the distance in [CSS pixels](https://drafts.csswg.org/css-values/#px) from the top edge of the image to the center of the circle, and the third integer must be the radius of the circle, again in [CSS pixels](https://drafts.csswg.org/css-values/#px).

In the default state, `area` elements must not have a `coords` attribute. (The area is the whole image.)

In the polygon state, `area` elements must have a `coords` attribute with at least six integers, and the number of integers must be even. Each pair of integers must represent a coordinate given as the distances from the left and the top of the image in [CSS pixels](https://drafts.csswg.org/css-values/#px) respectively, and all the coordinates together must represent the points of the polygon, in order.

In the rectangle state, `area` elements must have a `coords` attribute with exactly four integers, the first of which must be less than the third, and the second of which must be less than the fourth. The four points must represent, respectively, the distance from the left edge of the image to the left side of the rectangle, the distance from the top edge to the top side, the distance from the left edge to the right side, and the distance from the top edge to the bottom side, all in [CSS pixels](https://drafts.csswg.org/css-values/#px).

When user agents allow users to [follow hyperlinks](https://html.spec.whatwg.org/multipage/links.html#following-hyperlinks-2) or [download hyperlinks](https://html.spec.whatwg.org/multipage/links.html#downloading-hyperlinks) created using the `area` element, the `href`, `target`, `download`, and `ping` attributes decide how the link is followed. The `rel` attribute may be used to indicate to the user the likely nature of the target resource before the user follows the link.

The `target`, `download`, `ping`, `rel`, and `referrerpolicy` attributes must be omitted if the `href` attribute is not present.

If the `itemprop` attribute is specified on an `area` element, then the `href` attribute must also be specified.

[HTMLAreaElement/referrerPolicy](https://developer.mozilla.org/en-US/docs/Web/API/HTMLAreaElement/referrerPolicy "The HTMLAreaElement.referrerPolicy property reflect the HTML referrerpolicy attribute of the <area> element defining which referrer is sent when fetching the resource.")

Support in all current engines.

Firefox 50+Safari 14.1+Chrome 52+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

#### 4.8.14 Image maps[](https://html.spec.whatwg.org/multipage/image-maps.html#image-maps)

An image map allows geometric areas on an image to be associated with [hyperlinks](https://html.spec.whatwg.org/multipage/links.html#hyperlink).

An image, in the form of an `img` element, may be associated with an image map (in the form of a `map` element) by specifying a `usemap` attribute on the `img` element. The `usemap` attribute, if specified, must be a [valid hash-name reference](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-hash-name-reference) to a `map` element.

Consider an image that looks as follows:

![Image 2: A line with four shapes in it, equally spaced: a red hollow box, a green circle, a blue triangle, and a yellow four-pointed star.](https://html.spec.whatwg.org/images/sample-usemap.png)

If we wanted just the colored areas to be clickable, we could do it as follows:

```
<p>
 Please select a shape:
 <img src="shapes.png" usemap="#shapes"
      alt="Four shapes are available: a red hollow box, a green circle, a blue triangle, and a yellow four-pointed star.">
 <map name="shapes">
  <area shape=rect coords="50,50,100,100"> <!-- the hole in the red box -->
  <area shape=rect coords="25,25,125,125" href="red.html" alt="Red box.">
  <area shape=circle coords="200,75,50" href="green.html" alt="Green circle.">
  <area shape=poly coords="325,25,262,125,388,125" href="blue.html" alt="Blue triangle.">
  <area shape=poly coords="450,25,435,60,400,75,435,90,450,125,465,90,500,75,465,60"
        href="yellow.html" alt="Yellow star.">
 </map>
</p>
```

##### 4.8.14.2 Processing model[](https://html.spec.whatwg.org/multipage/image-maps.html#image-map-processing-model)

If an `img` element has a `usemap` attribute specified, user agents must process it as follows:

1.   Parse the attribute's value using the [rules for parsing a hash-name reference](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-a-hash-name-reference) to a `map` element, with the element as the context node. This will return either an element (the map) or null.

2.   If that returned null, then return. The image is not associated with an image map after all.

3.   Otherwise, the user agent must collect all the `area` elements that are descendants of the map. Let areas be that list.

Having obtained the list of `area` elements that form the image map (the areas), interactive user agents must process the list in one of two ways.

If the user agent intends to show the text that the `img` element represents, then it must use the following steps:

1.   Remove all the `area` elements in areas that have no `href` attribute.

2.   Remove all the `area` elements in areas that have no `alt` attribute, or whose `alt` attribute's value is the empty string, _if_ there is another `area` element in areas with the same value in the `href` attribute and with a non-empty `alt` attribute.

3.   Each remaining `area` element in areas represents a [hyperlink](https://html.spec.whatwg.org/multipage/links.html#hyperlink). Those hyperlinks should all be made available to the user in a manner associated with the text of the `img`.

In this context, user agents may represent `area` and `img` elements with no specified `alt` attributes, or whose `alt` attributes are the empty string or some other non-visible text, in an [implementation-defined](https://infra.spec.whatwg.org/#implementation-defined) fashion intended to indicate the lack of suitable author-provided text.

If the user agent intends to show the image and allow interaction with the image to select hyperlinks, then the image must be associated with a set of layered shapes, taken from the `area` elements in areas, in reverse [tree order](https://dom.spec.whatwg.org/#concept-tree-order) (so the last specified `area` element in the map is the bottom-most shape, and the first element in the map, in [tree order](https://dom.spec.whatwg.org/#concept-tree-order), is the top-most shape).

Each `area` element in areas must be processed as follows to obtain a shape to layer onto the image:

1.   Find the state that the element's `shape` attribute represents.

2.   Use the [rules for parsing a list of floating-point numbers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-a-list-of-floating-point-numbers) to parse the element's `coords` attribute, if it is present, and let the coords list be the result. If the attribute is absent, let the coords list be the empty list.

3.   If the number of items in the coords list is less than the minimum number given for the `area` element's current state, as per the following table, then the shape is empty; return.

| State | Minimum number of items |
| --- | --- |
| [Circle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-circle) | 3 |
| [Default state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-default) | 0 |
| [Polygon state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-poly) | 6 |
| [Rectangle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-rect) | 4 |
4.   Check for excess items in the coords list as per the entry in the following list corresponding to the `shape` attribute's state:

[Circle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-circle)Drop any items in the list beyond the third.[Default state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-default)Drop all items in the list.[Polygon state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-poly)Drop the last item if there's an odd number of items.[Rectangle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-rect)Drop any items in the list beyond the fourth.
5.   If the `shape` attribute represents the [rectangle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-rect), and the first number in the list is numerically greater than the third number in the list, then swap those two numbers around.

6.   If the `shape` attribute represents the [rectangle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-rect), and the second number in the list is numerically greater than the fourth number in the list, then swap those two numbers around.

7.   If the `shape` attribute represents the [circle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-circle), and the third number in the list is less than or equal to zero, then the shape is empty; return.

8.   Now, the shape represented by the element is the one described for the entry in the list below corresponding to the state of the `shape` attribute:

[Circle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-circle)
Let x be the first number in coords, y be the second number, and r be the third number.

The shape is a circle whose center is x[CSS pixels](https://drafts.csswg.org/css-values/#px) from the left edge of the image and y[CSS pixels](https://drafts.csswg.org/css-values/#px) from the top edge of the image, and whose radius is r[CSS pixels](https://drafts.csswg.org/css-values/#px).

[Default state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-default)
The shape is a rectangle that exactly covers the entire image.

[Polygon state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-poly)
Let x i be the (2 i)th entry in coords, and y i be the (2 i+1)th entry in coords (the first entry in coords being the one with index 0).

Let the coordinates be (x i, y i), interpreted in [CSS pixels](https://drafts.csswg.org/css-values/#px) measured from the top left of the image, for all integer values of i from 0 to (N/2)-1, where N is the number of items in coords.

The shape is a polygon whose vertices are given by the coordinates, and whose interior is established using the even-odd rule. [[GRAPHICS]](https://html.spec.whatwg.org/multipage/references.html#refsGRAPHICS)

[Rectangle state](https://html.spec.whatwg.org/multipage/image-maps.html#attr-area-shape-rect)
Let x 1 be the first number in coords, y 1 be the second number, x 2 be the third number, and y 2 be the fourth number.

The shape is a rectangle whose top-left corner is given by the coordinate (x 1, y 1) and whose bottom right corner is given by the coordinate (x 2, y 2), those coordinates being interpreted as [CSS pixels](https://drafts.csswg.org/css-values/#px) from the top left corner of the image.

For historical reasons, the coordinates must be interpreted relative to the _displayed_ image after any stretching caused by the CSS ['width'](https://drafts.csswg.org/css2/#the-width-property) and ['height'](https://drafts.csswg.org/css2/#the-height-property) properties (or, for non-CSS browsers, the image element's `width` and `height` attributes — CSS browsers map those attributes to the aforementioned CSS properties).

Browser zoom features and transforms applied using CSS or SVG do not affect the coordinates.

Pointing device interaction with an image associated with a set of layered shapes per the above algorithm must result in the relevant user interaction events being first fired to the top-most shape covering the point that the pointing device indicated, if any, or to the image element itself, if there is no shape covering that point. User agents may also allow individual `area` elements representing [hyperlinks](https://html.spec.whatwg.org/multipage/links.html#hyperlink) to be selected and activated (e.g. using a keyboard).

Because a `map` element (and its `area` elements) can be associated with multiple `img` elements, it is possible for an `area` element to correspond to multiple _[focusable areas](https://html.spec.whatwg.org/multipage/interaction.html#focusable-area)_ of the document.

Image maps are [live](https://html.spec.whatwg.org/multipage/infrastructure.html#live); if the DOM is mutated, then the user agent must act as if it had rerun the algorithms for image maps.

[← 4.8.8 The video element](https://html.spec.whatwg.org/multipage/media.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.8.15 MathML →](https://html.spec.whatwg.org/multipage/embedded-content-other.html)
