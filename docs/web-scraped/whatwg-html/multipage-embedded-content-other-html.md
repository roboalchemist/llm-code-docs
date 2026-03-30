# Source: https://html.spec.whatwg.org/multipage/embedded-content-other.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/embedded-content-other.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 4.8.12 The map element](https://html.spec.whatwg.org/multipage/image-maps.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.9 Tabular data →](https://html.spec.whatwg.org/multipage/tables.html)
1.       1.           1.   [4.8.15 MathML](https://html.spec.whatwg.org/multipage/embedded-content-other.html#mathml)
        2.   [4.8.16 SVG](https://html.spec.whatwg.org/multipage/embedded-content-other.html#svg-0)
        3.   [4.8.17 Dimension attributes](https://html.spec.whatwg.org/multipage/embedded-content-other.html#dimension-attributes)

#### 4.8.15 MathML[](https://html.spec.whatwg.org/multipage/embedded-content-other.html#mathml)

The [MathML `math`](https://w3c.github.io/mathml-core/#the-top-level-math-element) element falls into the [embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category), [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), and [palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) categories for the purposes of the content models in this specification.

When the [MathML `annotation-xml`](https://w3c.github.io/mathml-core/#dfn-annotation-xml) element contains elements from the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), such elements must all be [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).

When the MathML token elements (`mi`, `mo`, `mn`, `ms`, and `mtext`) are descendants of HTML elements, they may contain [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2) elements from the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace).

User agents must handle text other than [inter-element whitespace](https://html.spec.whatwg.org/multipage/dom.html#inter-element-whitespace) found in MathML elements whose content models do not allow straight text by pretending for the purposes of MathML content models, layout, and rendering that the text is actually wrapped in a [MathML `mtext`](https://w3c.github.io/mathml-core/#text-mtext) element. (Such text is not, however, conforming.)

User agents must act as if any MathML element whose contents does not match the element's content model was replaced, for the purposes of MathML layout and rendering, by a [MathML `merror`](https://w3c.github.io/mathml-core/#error-message-merror) element containing some appropriate error message.

The semantics of MathML elements are defined by MathML and [other applicable specifications](https://html.spec.whatwg.org/multipage/infrastructure.html#other-applicable-specifications). [[MATHML]](https://html.spec.whatwg.org/multipage/references.html#refsMATHML)

Here is an example of the use of MathML in an HTML document:

```
<!DOCTYPE html>
<html lang="en">
 <head>
  <title>The quadratic formula</title>
 </head>
 <body>
  <h1>The quadratic formula</h1>
  <p>
   <math>
    <mi>x</mi>
    <mo>=</mo>
    <mfrac>
     <mrow>
      <mo form="prefix">−</mo> <mi>b</mi>
      <mo>±</mo>
      <msqrt>
       <msup> <mi>b</mi> <mn>2</mn> </msup>
       <mo>−</mo>
       <mn>4</mn> <mo>⁢</mo> <mi>a</mi> <mo>⁢</mo> <mi>c</mi>
      </msqrt>
     </mrow>
     <mrow>
      <mn>2</mn> <mo>⁢</mo> <mi>a</mi>
     </mrow>
    </mfrac>
   </math>
  </p>
 </body>
</html>
```

#### 4.8.16 SVG[](https://html.spec.whatwg.org/multipage/embedded-content-other.html#svg-0)

[HTML/HTML5/HTML5_Parser#Inline_SVG_and_MathML_support](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/HTML5_Parser#Inline_SVG_and_MathML_support "To build websites, you should know about HTML — the fundamental technology used to define the structure of a webpage. HTML is used to specify whether your web content should be recognized as a paragraph, list, heading, link, image, multimedia player, form, or one of many other available elements or even a new element that you define.")

Support in all current engines.

Firefox 37+Safari 11.1+Chrome 7+

* * *

Opera 15+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android 37+Safari iOS 11.3+Chrome Android 18+WebView Android 4.4+Samsung Internet 4+Opera Android 15+

The [SVG `svg`](https://svgwg.org/svg2-draft/struct.html#SVGElement) element falls into the [embedded content](https://html.spec.whatwg.org/multipage/dom.html#embedded-content-category), [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2), [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2), and [palpable content](https://html.spec.whatwg.org/multipage/dom.html#palpable-content-2) categories for the purposes of the content models in this specification.

When the [SVG `foreignObject`](https://svgwg.org/svg2-draft/embedded.html#ForeignObjectElement) element contains elements from the [HTML namespace](https://infra.spec.whatwg.org/#html-namespace), such elements must all be [flow content](https://html.spec.whatwg.org/multipage/dom.html#flow-content-2).

The content model for the [SVG `title`](https://svgwg.org/svg2-draft/struct.html#TitleElement) element inside [HTML documents](https://dom.spec.whatwg.org/#html-document) is [phrasing content](https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2). (This further constrains the requirements given in SVG 2.)

The semantics of SVG elements are defined by SVG 2 and [other applicable specifications](https://html.spec.whatwg.org/multipage/infrastructure.html#other-applicable-specifications). [[SVG]](https://html.spec.whatwg.org/multipage/references.html#refsSVG)

* * *

`doc = iframe.getSVGDocument()``doc = embed.getSVGDocument()``doc = object.getSVGDocument()`
Returns the `Document` object, in the case of `iframe`, `embed`, or `object` elements being used to embed SVG.

#### 4.8.17 Dimension attributes[](https://html.spec.whatwg.org/multipage/embedded-content-other.html#dimension-attributes)

**Author requirements**: The `width` and `height` attributes on `img`, `iframe`, `embed`, `object`, `video`, `source` when the parent is a `picture` element and, when their `type` attribute is in the [Image Button](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)) state, `input` elements may be specified to give the dimensions of the visual content of the element (the width and height respectively, relative to the nominal direction of the output medium), in [CSS pixels](https://drafts.csswg.org/css-values/#px). The attributes, if specified, must have values that are [valid non-negative integers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-non-negative-integer).

The specified dimensions given may differ from the dimensions specified in the resource itself, since the resource may have a resolution that differs from the CSS pixel resolution. (On screens, [CSS pixels](https://drafts.csswg.org/css-values/#px) have a resolution of 96ppi, but in general the CSS pixel resolution depends on the reading distance.) If both attributes are specified, then one of the following statements must be true:

*   specified width - 0.5 ≤ specified height * target ratio ≤ specified width + 0.5
*   specified height - 0.5 ≤ specified width / target ratio ≤ specified height + 0.5
*   specified height = specified width = 0

The target ratio is the ratio of the [natural width](https://drafts.csswg.org/css-images/#natural-width) to the [natural height](https://drafts.csswg.org/css-images/#natural-height) in the resource. The specified width and specified height are the values of the `width` and `height` attributes respectively.

The two attributes must be omitted if the resource in question does not have both a [natural width](https://drafts.csswg.org/css-images/#natural-width) and a [natural height](https://drafts.csswg.org/css-images/#natural-height).

If the two attributes are both 0, it indicates that the element is not intended for the user (e.g. it might be a part of a service to count page views).

The dimension attributes are not intended to be used to stretch the image.

**User agent requirements**: User agents are expected to use these attributes [as hints for the rendering](https://html.spec.whatwg.org/multipage/rendering.html#dimRendering).

For `iframe`, `embed` and `object` the IDL attributes are `DOMString`; for `video` and `source` the IDL attributes are 
```
unsigned
  long
```
.

The corresponding IDL attributes for `img` and `input` elements are defined in those respective elements' sections, as they are slightly more specific to those elements' other behaviors.

[← 4.8.12 The map element](https://html.spec.whatwg.org/multipage/image-maps.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [4.9 Tabular data →](https://html.spec.whatwg.org/multipage/tables.html)
