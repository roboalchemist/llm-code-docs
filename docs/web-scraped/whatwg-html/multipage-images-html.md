# Source: https://html.spec.whatwg.org/multipage/images.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/images.html

Published Time: Mon, 16 Mar 2026 07:32:47 GMT

Markdown Content:
HTML

Living Standard — Last Updated 16 March 2026

← 4.8 Embedded content — Table of Contents — 4.8.5 The iframe element →
4.8.4 Images
4.8.4.1 Introduction
4.8.4.1.1 Adaptive images
4.8.4.2 Attributes common to source, img, and link elements
4.8.4.2.1 Srcset attributes
4.8.4.2.2 Sizes attributes
4.8.4.3 Processing model
4.8.4.3.1 When to obtain images
4.8.4.3.2 Reacting to DOM mutations
4.8.4.3.3 The list of available images
4.8.4.3.4 Decoding images
4.8.4.3.5 Updating the image data
4.8.4.3.6 Preparing an image for presentation
4.8.4.3.7 Selecting an image source
4.8.4.3.8 Creating a source set from attributes
4.8.4.3.9 Updating the source set
4.8.4.3.10 Parsing a srcset attribute
4.8.4.3.11 Parsing a sizes attribute
4.8.4.3.12 Normalizing the source densities
4.8.4.3.13 Reacting to environment changes
4.8.4.4 Requirements for providing text to act as an alternative for images
4.8.4.4.1 General guidelines
4.8.4.4.2 A link or button containing nothing but the image
4.8.4.4.3 A phrase or paragraph with an alternative graphical representation: charts, diagrams, graphs, maps, illustrations
4.8.4.4.4 A short phrase or label with an alternative graphical representation: icons, logos
4.8.4.4.5 Text that has been rendered to a graphic for typographical effect
4.8.4.4.6 A graphical representation of some of the surrounding text
4.8.4.4.7 Ancillary images
4.8.4.4.8 A purely decorative image that doesn't add any information
4.8.4.4.9 A group of images that form a single larger picture with no links
4.8.4.4.10 A group of images that form a single larger picture with links
4.8.4.4.11 A key part of the content
4.8.4.4.12 An image not intended for the user
4.8.4.4.13 An image in an email or private document intended for a specific person who is known to be able to view images
4.8.4.4.14 Guidance for markup generators
4.8.4.4.15 Guidance for conformance checkers
4.8.4 Images
4.8.4.1 Introduction

This section is non-normative.

To embed an image in HTML, when there is only a single image resource, use the img element and its src attribute.

<h2>From today's featured article</h2>
<img src="/uploads/100-marie-lloyd.jpg" alt="" width="100" height="150">
<p><b><a href="/wiki/Marie_Lloyd">Marie Lloyd</a></b> (1870–1922)
was an English <a href="/wiki/Music_hall">music hall</a> singer, ...

However, there are a number of situations for which the author might wish to use multiple image resources that the user agent can choose from:

Different users might have different environmental characteristics:

The users' physical screen size might be different from one another.

A mobile phone's screen might be 4 inches diagonally, while a laptop's screen might be 14 inches diagonally.

4″
14″

This is only relevant when an image's rendered size depends on the viewport size.

The users' screen pixel density might be different from one another.

A mobile phone's screen might have three times as many physical pixels per inch compared to another mobile phone's screen, regardless of their physical screen size.

1x
3x

The users' zoom level might be different from one another, or might change for a single user over time.

A user might zoom in to a particular image to be able to get a more detailed look.

The zoom level and the screen pixel density (the previous point) can both affect the number of physical screen pixels per CSS pixel. This ratio is usually referred to as device-pixel-ratio.

The users' screen orientation might be different from one another, or might change for a single user over time.

A tablet can be held upright or rotated 90 degrees, so that the screen is either "portrait" or "landscape".

Portrait
Landscape

The users' network speed, network latency and bandwidth cost might be different from one another, or might change for a single user over time.

A user might be on a fast, low-latency and constant-cost connection while at work, on a slow, low-latency and constant-cost connection while at home, and on a variable-speed, high-latency and variable-cost connection anywhere else.

Authors might want to show the same image content but with different rendered size depending on, usually, the width of the viewport. This is usually referred to as viewport-based selection.

A web page might have a banner at the top that always spans the entire viewport width. In this case, the rendered size of the image depends on the physical size of the screen (assuming a maximised browser window).

Another web page might have images in columns, with a single column for screens with a small physical size, two columns for screens with medium physical size, and three columns for screens with big physical size, with the images varying in rendered size in each case to fill up the viewport. In this case, the rendered size of an image might be bigger in the one-column layout compared to the two-column layout, despite the screen being smaller.

Narrow, 1 column
Medium, 2 columns
Wide, 3 columns

Authors might want to show different image content depending on the rendered size of the image. This is usually referred to as art direction.

When a web page is viewed on a screen with a large physical size (assuming a maximised browser window), the author might wish to include some less relevant parts surrounding the critical part of the image. When the same web page is viewed on a screen with a small physical size, the author might wish to show only the critical part of the image.

Authors might want to show the same image content but using different image formats, depending on which image formats the user agent supports. This is usually referred to as image format-based selection.

A web page might have some images in the JPEG, WebP and JPEG XR image formats, with the latter two having better compression abilities compared to JPEG. Since different user agents can support different image formats, with some formats offering better compression ratios, the author would like to serve the better formats to user agents that support them, while providing JPEG fallback for user agents that don't.

The above situations are not mutually exclusive. For example, it is reasonable to combine different resources for different device-pixel-ratio with different resources for art direction.

While it is possible to solve these problems using scripting, doing so introduces some other problems:

Some user agents aggressively download images specified in the HTML markup, before scripts have had a chance to run, so that web pages complete loading sooner. If a script changes which image to download, the user agent will potentially start two separate downloads, which can instead cause worse page loading performance.

If the author avoids specifying any image in the HTML markup and instead instantiates a single download from script, that avoids the double download problem above but then no image will be downloaded at all for users with scripting disabled and the aggressive image downloading optimization will also be disabled.

With this in mind, this specification introduces a number of features to address the above problems in a declarative manner.

Device-pixel-ratio-based selection when the rendered size of the image is fixed

The src and srcset attributes on the img element can be used, using the x descriptor, to provide multiple images that only vary in their size (the smaller image is a scaled-down version of the bigger image).

The x descriptor is not appropriate when the rendered size of the image depends on the viewport width (viewport-based selection), but can be used together with art direction.

<h2>From today's featured article</h2>
<img src="/uploads/100-marie-lloyd.jpg"
     srcset="/uploads/150-marie-lloyd.jpg 1.5x, /uploads/200-marie-lloyd.jpg 2x"
     alt="" width="100" height="150">
<p><b><a href="/wiki/Marie_Lloyd">Marie Lloyd</a></b> (1870–1922)
was an English <a href="/wiki/Music_hall">music hall</a> singer, ...

The user agent can choose any of the given resources depending on the user's screen's pixel density, zoom level, and possibly other factors such as the user's network conditions.

For backwards compatibility with older user agents that don't yet understand the srcset attribute, one of the URLs is specified in the img element's src attribute. This will result in something useful (though perhaps lower-resolution than the user would like) being displayed even in older user agents. For new user agents, the src attribute participates in the resource selection, as if it was specified in srcset with a 1x descriptor.

The image's rendered size is given in the width and height attributes, which allows the user agent to allocate space for the image before it is downloaded.

Viewport-based selection

The srcset and sizes attributes can be used, using the w descriptor, to provide multiple images that only vary in their size (the smaller image is a scaled-down version of the bigger image).

In this example, a banner image takes up the entire viewport width (using appropriate CSS).

<h1><img sizes="100vw" srcset="wolf-400.jpg 400w, wolf-800.jpg 800w, wolf-1600.jpg 1600w"
     src="wolf-400.jpg" alt="The rad wolf"></h1>

The user agent will calculate the effective pixel density of each image from the specified w descriptors and the specified rendered size in the sizes attribute. It can then choose any of the given resources depending on the user's screen's pixel density, zoom level, and possibly other factors such as the user's network conditions.

If the user's screen is 320 CSS pixels wide, this is equivalent to specifying wolf-400.jpg 1.25x, wolf-800.jpg 2.5x, wolf-1600.jpg 5x. On the other hand, if the user's screen is 1200 CSS pixels wide, this is equivalent to specifying wolf-400.jpg 0.33x, wolf-800.jpg 0.67x, wolf-1600.jpg 1.33x. By using the w descriptors and the sizes attribute, the user agent can choose the correct image source to download regardless of how large the user's device is.

For backwards compatibility, one of the URLs is specified in the img element's src attribute. In new user agents, the src attribute is ignored when the srcset attribute uses w descriptors.

In this example, the web page has three layouts depending on the width of the viewport. The narrow layout has one column of images (the width of each image is about 100%), the middle layout has two columns of images (the width of each image is about 50%), and the widest layout has three columns of images, and some page margin (the width of each image is about 33%). It breaks between these layouts when the viewport is 30em wide and 50em wide, respectively.

<img sizes="(max-width: 30em) 100vw, (max-width: 50em) 50vw, calc(33vw - 100px)"
     srcset="swing-200.jpg 200w, swing-400.jpg 400w, swing-800.jpg 800w, swing-1600.jpg 1600w"
     src="swing-400.jpg" alt="Kettlebell Swing">

The sizes attribute sets up the layout breakpoints at 30em and 50em, and declares the image sizes between these breakpoints to be 100vw, 50vw, or calc(33vw - 100px). These sizes do not necessarily have to match up exactly with the actual image width as specified in the CSS.

The user agent will pick a width from the sizes attribute, using the first item with a <media-condition> (the part in parentheses) that evaluates to true, or using the last item (calc(33vw - 100px)) if they all evaluate to false.

For example, if the viewport width is 29em, then (max-width: 30em) evaluates to true and 100vw is used, so the image size, for the purpose of resource selection, is 29em. If the viewport width is instead 32em, then (max-width: 30em) evaluates to false, but (max-width: 50em) evaluates to true and 50vw is used, so the image size, for the purpose of resource selection, is 16em (half the viewport width). Notice that the slightly wider viewport results in a smaller image because of the different layout.

The user agent can then calculate the effective pixel density and choose an appropriate resource similarly to the previous example.

This example is the same as the previous example, but the image is lazy-loaded. In this case, the sizes attribute can use the auto keyword, and the user agent will use the width attribute (or the width specified in CSS) for the source size.

<img loading="lazy" width="200" height="200" sizes="auto"
     srcset="swing-200.jpg 200w, swing-400.jpg 400w, swing-800.jpg 800w, swing-1600.jpg 1600w"
     src="swing-400.jpg" alt="Kettlebell Swing">

For better backwards-compatibility with legacy user agents that don't support the auto keyword, fallback sizes can be specified if desired.

<img loading="lazy" width="200" height="200"
     sizes="auto, (max-width: 30em) 100vw, (max-width: 50em) 50vw, calc(33vw - 100px)"
     srcset="swing-200.jpg 200w, swing-400.jpg 400w, swing-800.jpg 800w, swing-1600.jpg 1600w"
     src="swing-400.jpg" alt="Kettlebell Swing">
Art direction-based selection

The picture element and the source element, together with the media attribute, can be used to provide multiple images that vary the image content (for instance the smaller image might be a cropped version of the bigger image).

<picture>
  <source media="(min-width: 45em)" srcset="large.jpg">
  <source media="(min-width: 32em)" srcset="med.jpg">
  <img src="small.jpg" alt="The wolf runs through the snow.">
</picture>

The user agent will choose the first source element for which the media query in the media attribute matches, and then choose an appropriate URL from its srcset attribute.

The rendered size of the image varies depending on which resource is chosen. To specify dimensions that the user agent can use before having downloaded the image, CSS can be used.

img { width: 300px; height: 300px }
@media (min-width: 32em) { img { width: 500px; height:300px } }
@media (min-width: 45em) { img { width: 700px; height:400px } }

This example combines art direction- and device-pixel-ratio-based selection. A banner that takes half the viewport is provided in two versions, one for wide screens and one for narrow screens.

<h1>
 <picture>
  <source media="(max-width: 500px)" srcset="banner-phone.jpeg, banner-phone-HD.jpeg 2x">
  <img src="banner.jpeg" srcset="banner-HD.jpeg 2x" alt="The Breakfast Combo">
 </picture>
</h1>
Image format-based selection

The type attribute on the source element can be used to provide multiple images in different formats.

<h2>From today's featured article</h2>
<picture>
 <source srcset="/uploads/100-marie-lloyd.webp" type="image/webp">
 <source srcset="/uploads/100-marie-lloyd.jxr" type="image/vnd.ms-photo">
 <img src="/uploads/100-marie-lloyd.jpg" alt="" width="100" height="150">
</picture>
<p><b><a href="/wiki/Marie_Lloyd">Marie Lloyd</a></b> (1870–1922)
was an English <a href="/wiki/Music_hall">music hall</a> singer, ...

In this example, the user agent will choose the first source that has a type attribute with a supported MIME type. If the user agent supports WebP images, the first source element will be chosen. If not, but the user agent does support JPEG XR images, the second source element will be chosen. If neither of those formats are supported, the img element will be chosen.

4.8.4.1.1 Adaptive images

This section is non-normative.

CSS and media queries can be used to construct graphical page layouts that adapt dynamically to the user's environment, in particular to different viewport dimensions and pixel densities. For content, however, CSS does not help; instead, we have the img element's srcset attribute and the picture element. This section walks through a sample case showing how to use these features.

Consider a situation where on wide screens (wider than 600 CSS pixels) a 300×150 image named a-rectangle.png is to be used, but on smaller screens (600 CSS pixels and less), a smaller 100×100 image called a-square.png is to be used. The markup for this would look like this:

<figure>
 <picture>
  <source srcset="a-square.png" media="(max-width: 600px)">
  <img src="a-rectangle.png" alt="Barney Frank wears a suit and glasses.">
 </picture>
 <figcaption>Barney Frank, 2011</figcaption>
</figure>

For details on what to put in the alt attribute, see the Requirements for providing text to act as an alternative for images section.

The problem with this is that the user agent does not necessarily know what dimensions to use for the image when the image is loading. To avoid the layout having to be reflowed multiple times as the page is loading, CSS and CSS media queries can be used to provide the dimensions:

<style>
 #a { width: 300px; height: 150px; }
 @media (max-width: 600px) { #a { width: 100px; height: 100px; } }
</style>
<figure>
 <picture>
  <source srcset="a-square.png" media="(max-width: 600px)">
  <img src="a-rectangle.png" alt="Barney Frank wears a suit and glasses." id="a">
 </picture>
 <figcaption>Barney Frank, 2011</figcaption>
</figure>

Alternatively, the width and height attributes can be used on the source and img elements to provide the width and height:

<figure>
 <picture>
  <source srcset="a-square.png" media="(max-width: 600px)" width="100" height="100">
  <img src="a-rectangle.png" width="300" height="150"
  alt="Barney Frank wears a suit and glasses.">
 </picture>
 <figcaption>Barney Frank, 2011</figcaption>
</figure>


The img element is used with the src attribute, which gives the URL of the image to use for legacy user agents that do not support the picture element. This leads to a question of which image to provide in the src attribute.

If the author wants the biggest image in legacy user agents, the markup could be as follows:

<picture>
 <source srcset="pear-mobile.jpeg" media="(max-width: 720px)">
 <source srcset="pear-tablet.jpeg" media="(max-width: 1280px)">
 <img src="pear-desktop.jpeg" alt="The pear is juicy.">
</picture>

However, if legacy mobile user agents are more important, one can list all three images in the source elements, overriding the src attribute entirely.

<picture>
 <source srcset="pear-mobile.jpeg" media="(max-width: 720px)">
 <source srcset="pear-tablet.jpeg" media="(max-width: 1280px)">
 <source srcset="pear-desktop.jpeg">
 <img src="pear-mobile.jpeg" alt="The pear is juicy.">
</picture>

Since at this point the src attribute is actually being ignored entirely by picture-supporting user agents, the src attribute can default to any image, including one that is neither the smallest nor biggest:

<picture>
 <source srcset="pear-mobile.jpeg" media="(max-width: 720px)">
 <source srcset="pear-tablet.jpeg" media="(max-width: 1280px)">
 <source srcset="pear-desktop.jpeg">
 <img src="pear-tablet.jpeg" alt="The pear is juicy.">
</picture>

Above the max-width media feature is used, giving the maximum (viewport) dimensions that an image is intended for. It is also possible to use min-width instead.

<picture>
 <source srcset="pear-desktop.jpeg" media="(min-width: 1281px)">
 <source srcset="pear-tablet.jpeg" media="(min-width: 721px)">
 <img src="pear-mobile.jpeg" alt="The pear is juicy.">
</picture>
4.8.4.2 Attributes common to source, img, and link elements
4.8.4.2.1 Srcset attributes

A srcset attribute is an attribute with requirements defined in this section.

If present, its value must consist of one or more image candidate strings, each separated from the next by a U+002C COMMA character (,). If an image candidate string contains no descriptors and no ASCII whitespace after the URL, the following image candidate string, if there is one, must begin with one or more ASCII whitespace.

An image candidate string consists of the following components, in order, with the further restrictions described below this list:

Zero or more ASCII whitespace.

A valid non-empty URL that does not start or end with a U+002C COMMA character (,), referencing a non-interactive, optionally animated, image resource that is neither paged nor scripted.

Zero or more ASCII whitespace.

Zero or one of the following:

A width descriptor, consisting of: ASCII whitespace, a valid non-negative integer giving a number greater than zero representing the width descriptor value, and a U+0077 LATIN SMALL LETTER W character.

A pixel density descriptor, consisting of: ASCII whitespace, a valid floating-point number giving a number greater than zero representing the pixel density descriptor value, and a U+0078 LATIN SMALL LETTER X character.

Zero or more ASCII whitespace.

There must not be an image candidate string for an element that has the same width descriptor value as another image candidate string's width descriptor value for the same element.

There must not be an image candidate string for an element that has the same pixel density descriptor value as another image candidate string's pixel density descriptor value for the same element. For the purpose of this requirement, an image candidate string with no descriptors is equivalent to an image candidate string with a 1x descriptor.

If an image candidate string for an element has the width descriptor specified, all other image candidate strings for that element must also have the width descriptor specified.

The specified width in an image candidate string's width descriptor must match the natural width in the resource given by the image candidate string's URL, if it has a natural width.

If an element has a sizes attribute present, all image candidate strings for that element must have the width descriptor specified.

4.8.4.2.2 Sizes attributes

A sizes attribute is an attribute with requirements defined in this section.

If present, the value must be a valid source size list.

A valid source size list is a string that matches the following grammar: [CSSVALUES] [MQ]

<source-size-list> = <source-size>#? , <source-size-value>
<source-size> = <media-condition> <source-size-value> | auto
<source-size-value> = <length> | auto

A <source-size-value> that is a <length> must not be negative, and must not use CSS functions other than the math functions.

The keyword auto is a width that is computed in parse a sizes attribute. If present, it must be the first entry and the entire <source-size-list> value must either be the string "auto" (ASCII case-insensitive) or start with the string "auto," (ASCII case-insensitive).

If the img element that initiated the image loading (with the update the image data or react to environment changes algorithms) allows auto-sizes and is being rendered, then auto is the concrete object size width. Otherwise, the auto value is ignored and the next source size is used instead, if any.

The auto keyword may be specified in the sizes attribute of source elements and sizes attribute of img elements, if the following conditions are met. Otherwise, auto must not be specified.

The element is a source element with a following sibling img element.

The element is an img element.

The img element referenced in either condition above allows auto-sizes.

In addition, it is strongly encouraged to specify dimensions using the width and height attributes or with CSS. Without specified dimensions, the image will likely render with 300x150 dimensions because sizes="auto" implies contain-intrinsic-size: 300px 150px in the Rendering section.

The <source-size-value> gives the intended layout width of the image. The author can specify different widths for different environments with <media-condition>s.

Percentages are not allowed in a <source-size-value>, to avoid confusion about what it would be relative to. The 'vw' unit can be used for sizes relative to the viewport width.

4.8.4.3 Processing model

An img element has a current request and a pending request. The current request is initially set to a new image request. The pending request is initially set to null.

An image request has a state, current URL, and image data.

An image request's state is one of the following:

Unavailable
The user agent hasn't obtained any image data, or has obtained some or all of the image data but hasn't yet decoded enough of the image to get the image dimensions.
Partially available
The user agent has obtained some of the image data and at least the image dimensions are available.
Completely available
The user agent has obtained all of the image data and at least the image dimensions are available.
Broken
The user agent has obtained all of the image data that it can, but it cannot even decode the image enough to get the image dimensions (e.g. the image is corrupted, or the format is not supported, or no data could be obtained).

An image request's current URL is initially the empty string.

An image request's image data is the decoded image data.

When an image request's state is either partially available or completely available, the image request is said to be available.

When an img element's current request's state is completely available and the user agent can decode the media data without errors, then the img element is said to be fully decodable.

An image request's state is initially unavailable.

When an img element's current request is available, the img element provides a paint source whose width is the image's density-corrected natural width (if any), whose height is the image's density-corrected natural height (if any), and whose appearance is the natural appearance of the image.

An img element is said to use srcset or picture if it has a srcset attribute specified or if it has a parent that is a picture element.

Each img element has a last selected source, which must initially be null.

Each image request has a current pixel density, which must initially be 1.

Each image request has preferred density-corrected dimensions, which is either a struct consisting of a width and a height or is null. It must initially be null.

To determine the density-corrected natural width and height of an img element img:

Let dim be img's current request's preferred density-corrected dimensions.

The preferred density-corrected dimensions are set in the prepare an image for presentation algorithm based on meta information in the image.

If dim is null, set dim to img's natural dimensions.

Set dim's width to dim's width divided by img's current request's current pixel density.

Set dim's height to dim's height divided by img's current request's current pixel density.

Return dim.

For example, if the current pixel density is 3.125, that means that there are 300 device pixels per CSS inch, and thus if the image data is 300x600, it has density-corrected natural width and height of 96 CSS pixels by 192 CSS pixels.

All img and link elements are associated with a source set.

A source set is an ordered set of zero or more image sources and a source size.

An image source is a URL, and optionally either a pixel density descriptor, or a width descriptor.

A source size is a <source-size-value>. When a source size has a unit relative to the viewport, it must be interpreted relative to the img element's node document's viewport. Other units must be interpreted the same as in Media Queries. [MQ]

A parse error for algorithms in this section indicates a non-fatal mismatch between input and requirements. User agents are encouraged to expose parse errors somehow.

Whether the image is fetched successfully or not (e.g. whether the response status was an ok status) must be ignored when determining the image's type and whether it is a valid image.

This allows servers to return images with error responses, and have them displayed.

The user agent should apply the image sniffing rules to determine the type of the image, with the image's associated Content-Type headers giving the official type. If these rules are not applied, then the type of the image must be the type given by the image's associated Content-Type headers.

User agents must not support non-image resources with the img element (e.g. XML files whose document element is an HTML element). User agents must not run executable code (e.g. scripts) embedded in the image resource. User agents must only display the first page of a multipage resource (e.g. a PDF file). User agents must not allow the resource to act in an interactive fashion, but should honour any animation in the resource.

This specification does not specify which image types are to be supported.

4.8.4.3.1 When to obtain images

By default, images are obtained immediately. User agents may provide users with the option to instead obtain them on-demand. (The on-demand option might be used by bandwidth-constrained users, for example.)

When obtaining images immediately, the user agent must synchronously update the image data of the img element, with the restart animation flag set if so stated, whenever that element is created or has experienced relevant mutations.

When obtaining images on demand, the user agent must update the image data of an img element whenever it needs the image data (i.e., on demand), but only if the img element's current request's state is unavailable. When an img element has experienced relevant mutations, if the user agent only obtains images on demand, the img element's current request's state must return to unavailable.

4.8.4.3.2 Reacting to DOM mutations

The relevant mutations for an img element are as follows:

The element's src, srcset, width, or sizes attributes are set, changed, or removed.

The element's src attribute is set to the same value as the previous value. This must set the restart animation flag for the update the image data algorithm.

The element's crossorigin attribute's state is changed.

The element's referrerpolicy attribute's state is changed.

The img or source HTML element insertion steps, HTML element removing steps, and HTML element moving steps count the mutation as a relevant mutation.

The element's parent is a picture element and a source element that is a previous sibling has its srcset, sizes, media, type, width or height attributes set, changed, or removed.

The element's adopting steps are run.

If the element allows auto-sizes: the element starts or stops being rendered, or its concrete object size width changes. This must set the maybe omit events flag for the update the image data algorithm.

4.8.4.3.3 The list of available images

Each Document object must have a list of available images. Each image in this list is identified by a tuple consisting of an absolute URL, a CORS settings attribute mode, and, if the mode is not No CORS, an origin. Each image furthermore has an ignore higher-layer caching flag. User agents may copy entries from one Document object's list of available images to another at any time (e.g. when the Document is created, user agents can add to it all the images that are loaded in other Documents), but must not change the keys of entries copied in this way when doing so, and must unset the ignore higher-layer caching flag for the copied entry. User agents may also remove images from such lists at any time (e.g. to save memory). User agents must remove entries in the list of available images as appropriate given higher-layer caching semantics for the resource (e.g. the HTTP `Cache-Control` response header) when the ignore higher-layer caching flag is unset.

The list of available images is intended to enable synchronous switching when changing the src attribute to a URL that has previously been loaded, and to avoid re-downloading images in the same document even when they don't allow caching per HTTP. It is not used to avoid re-downloading the same image while the previous image is still loading.

The user agent can also store the image data separately from the list of available images.

For example, if a resource has the HTTP response header `Cache-Control: must-revalidate`, and its ignore higher-layer caching flag is unset, the user agent would remove it from the list of available images but could keep the image data separately, and use that if the server responds with a 304 Not Modified status.

4.8.4.3.4 Decoding images

Image data is usually encoded in order to reduce file size. This means that in order for the user agent to present the image to the screen, the data needs to be decoded. Decoding is the process which converts an image's media data into a bitmap form, suitable for presentation to the screen. Note that this process can be slow relative to other processes involved in presenting content. Thus, the user agent can choose when to perform decoding, in order to create the best user experience.

Image decoding is said to be synchronous if it prevents presentation of other content until it is finished. Typically, this has an effect of atomically presenting the image and any other content at the same time. However, this presentation is delayed by the amount of time it takes to perform the decode.

Image decoding is said to be asynchronous if it does not prevent presentation of other content. This has an effect of presenting non-image content faster. However, the image content is missing on screen until the decode finishes. Once the decode is finished, the screen is updated with the image.

In both synchronous and asynchronous decoding modes, the final content is presented to screen after the same amount of time has elapsed. The main difference is whether the user agent presents non-image content ahead of presenting the final content.

In order to aid the user agent in deciding whether to perform synchronous or asynchronous decode, the decoding attribute can be set on img elements. The possible values of the decoding attribute are the following image decoding hint keywords:

Keyword	State	Description
sync	Sync	Indicates a preference to decode this image synchronously for atomic presentation with other content.
async	Async	Indicates a preference to decode this image asynchronously to avoid delaying presentation of other content.
auto	Auto	Indicates no preference in decoding mode (the default).

When decoding an image, the user agent should respect the preference indicated by the decoding attribute's state. If the state indicated is Auto, then the user agent is free to choose any decoding behavior.

It is also possible to control the decoding behavior using the decode() method. Since the decode() method performs decoding independently from the process responsible for presenting content to screen, it is unaffected by the decoding attribute.

4.8.4.3.5 Updating the image data

This algorithm cannot be called from steps running in parallel. If a user agent needs to call this algorithm from steps running in parallel, it needs to queue a task to do so.

When the user agent is to update the image data of an img element, optionally with the restart animation flag set, optionally with the maybe omit events flag set, it must run the following steps:

If the element's node document is not fully active, then:

Continue running this algorithm in parallel.

Wait until the element's node document is fully active.

If another instance of this algorithm for this img element was started after this instance (even if it aborted and is no longer running), then return.

Queue a microtask to continue this algorithm.

If the user agent cannot support images, or its support for images has been disabled, then abort the image request for the current request and the pending request, set the current request's state to unavailable, set the pending request to null, and return.

Let previousURL be the current request's current URL.

Let selected source be null and selected pixel density be undefined.

If the element does not use srcset or picture and it has a src attribute specified whose value is not the empty string, then set selected source to the value of the element's src attribute and set selected pixel density to 1.0.

Set the element's last selected source to selected source.

If selected source is not null, then:

Let urlString be the result of encoding-parsing-and-serializing a URL given selected source, relative to the element's node document.

If urlString is failure, then abort this inner set of steps.

Let key be a tuple consisting of urlString, the img element's crossorigin attribute's mode, and, if that mode is not No CORS, the node document's origin.

If the list of available images contains an entry for key, then:

Set the ignore higher-layer caching flag for that entry.

Abort the image request for the current request and the pending request.

Set the pending request to null.

Set the current request to a new image request whose image data is that of the entry and whose state is completely available.

Prepare the current request for presentation given the img element.

Set the current request's current pixel density to selected pixel density.

Queue an element task on the DOM manipulation task source given the img element and the following steps:

If restart animation is set, then restart the animation.

Set the current request's current URL to urlString.

If maybe omit events is not set or previousURL is not equal to urlString, then fire an event named load at the img element.

Abort the update the image data algorithm.

Queue a microtask to perform the rest of this algorithm, allowing the task that invoked this algorithm to continue.

If another instance of this algorithm for this img element was started after this instance (even if it aborted and is no longer running), then return.

Only the last instance takes effect, to avoid multiple requests when, for example, the src, srcset, and crossorigin attributes are all set in succession.

Let selected source and selected pixel density be the URL and pixel density that results from selecting an image source, respectively.

If selected source is null, then:

Set the current request's state to broken, abort the image request for the current request and the pending request, and set the pending request to null.

Queue an element task on the DOM manipulation task source given the img element and the following steps:

Change the current request's current URL to the empty string.

If all of the following are true:

the element has a src attribute or it uses srcset or picture; and

maybe omit events is not set or previousURL is not the empty string,

then fire an event named error at the img element.

Return.

Let urlString be the result of encoding-parsing-and-serializing a URL given selected source, relative to the element's node document.

If urlString is failure, then:

Abort the image request for the current request and the pending request.

Set the current request's state to broken.

Set the pending request to null.

Queue an element task on the DOM manipulation task source given the img element and the following steps:

Change the current request's current URL to selected source.

If maybe omit events is not set or previousURL is not equal to selected source, then fire an event named error at the img element.

Return.

If the pending request is not null and urlString is the same as the pending request's current URL, then return.

If urlString is the same as the current request's current URL and the current request's state is partially available, then abort the image request for the pending request, queue an element task on the DOM manipulation task source given the img element to restart the animation if restart animation is set, and return.

Abort the image request for the pending request.

Set image request to a new image request whose current URL is urlString.

If the current request's state is unavailable or broken, then set the current request to image request. Otherwise, set the pending request to image request.

Let request be the result of creating a potential-CORS request given urlString, "image", and the current state of the element's crossorigin content attribute.

Set request's client to the element's node document's relevant settings object.

If the element uses srcset or picture, set request's initiator to "imageset".

Set request's referrer policy to the current state of the element's referrerpolicy attribute.

Set request's priority to the current state of the element's fetchpriority attribute.

Let delay load event be true if the img's lazy loading attribute is in the Eager state, or if scripting is disabled for the img, and false otherwise.

If the will lazy load element steps given the img return true, then:

Set the img's lazy load resumption steps to the rest of this algorithm starting with the step labeled fetch the image.

Start intersection-observing a lazy loading element for the img element.

Return.

Fetch the image: Fetch request. Return from this algorithm, and run the remaining steps as part of the fetch's processResponse for the response response.

The resource obtained in this fashion, if any, is image request's image data. It can be either CORS-same-origin or CORS-cross-origin; this affects the image's interaction with other APIs (e.g., when used on a canvas).

When delay load event is true, fetching the image must delay the load event of the element's node document until the task that is queued by the networking task source once the resource has been fetched (defined below) has been run.

This, unfortunately, can be used to perform a rudimentary port scan of the user's local network (especially in conjunction with scripting, though scripting isn't actually necessary to carry out such an attack). User agents may implement cross-origin access control policies that are stricter than those described above to mitigate this attack, but unfortunately such policies are typically not compatible with existing web content.

As soon as possible, jump to the first applicable entry from the following list:

If the resource type is multipart/x-mixed-replace

The next task that is queued by the networking task source while the image is being fetched must run the following steps:

If image request is the pending request and at least one body part has been completely decoded, abort the image request for the current request, and upgrade the pending request to the current request.

Otherwise, if image request is the pending request and the user agent is able to determine that image request's image is corrupted in some fatal way such that the image dimensions cannot be obtained, abort the image request for the current request, upgrade the pending request to the current request, and set the current request's state to broken.

Otherwise, if image request is the current request, its state is unavailable, and the user agent is able to determine image request's image's width and height, set the current request's state to partially available.

Otherwise, if image request is the current request, its state is unavailable, and the user agent is able to determine that image request's image is corrupted in some fatal way such that the image dimensions cannot be obtained, set the current request's state to broken.

Each task that is queued by the networking task source while the image is being fetched must update the presentation of the image, but as each new body part comes in, if the user agent is able to determine the image's width and height, it must prepare the img element's current request for presentation given the img element and replace the previous image. Once one body part has been completely decoded, perform the following steps:

Set the img element's current request's state to completely available.

If maybe omit events is not set or previousURL is not equal to urlString, then queue an element task on the DOM manipulation task source given the img element to fire an event named load at the img element.

If the resource type and data corresponds to a supported image format, as described below

The next task that is queued by the networking task source while the image is being fetched must run the following steps:

If the user agent is able to determine image request's image's width and height, and image request is the pending request, set image request's state to partially available.

Otherwise, if the user agent is able to determine image request's image's width and height, and image request is the current request, prepare image request for presentation given the img element and set image request's state to partially available.

Otherwise, if the user agent is able to determine that image request's image is corrupted in some fatal way such that the image dimensions cannot be obtained, and image request is the pending request:

Abort the image request for the current request and the pending request.

Upgrade the pending request to the current request.

Set the current request's state to broken.

Fire an event named error at the img element.

Otherwise, if the user agent is able to determine that image request's image is corrupted in some fatal way such that the image dimensions cannot be obtained, and image request is the current request:

Abort the image request for image request.

If maybe omit events is not set or previousURL is not equal to urlString, then fire an event named error at the img element.

That task, and each subsequent task, that is queued by the networking task source while the image is being fetched, if image request is the current request, must update the presentation of the image appropriately (e.g., if the image is a progressive JPEG, each packet can improve the resolution of the image).

Furthermore, the last task that is queued by the networking task source once the resource has been fetched must additionally run these steps:

If image request is the pending request, abort the image request for the current request, upgrade the pending request to the current request, and prepare image request for presentation given the img element.

Set image request to the completely available state.

Add the image to the list of available images using the key key, with the ignore higher-layer caching flag set.

If maybe omit events is not set or previousURL is not equal to urlString, then fire an event named load at the img element.

Otherwise

The image data is not in a supported file format; the user agent must set image request's state to broken, abort the image request for the current request and the pending request, upgrade the pending request to the current request if image request is the pending request, and then, if maybe omit events is not set or previousURL is not equal to urlString, queue an element task on the DOM manipulation task source given the img element to fire an event named error at the img element.

While a user agent is running the above algorithm for an element x, there must be a strong reference from the element's node document to the element x, even if that element is not connected.

To abort the image request for an image request or null image request means to run the following steps:

If image request is null, then return.

Forget image request's image data, if any.

Abort any instance of the fetching algorithm for image request, discarding any pending tasks generated by that algorithm.

To upgrade the pending request to the current request for an img element means to run the following steps:

Set the img element's current request to the pending request.

Set the img element's pending request to null.

4.8.4.3.6 Preparing an image for presentation

To prepare an image for presentation for an image request req given image element img:

Let exifTagMap be the EXIF tags obtained from req's image data, as defined by the relevant codec. [EXIF]

Let physicalWidth and physicalHeight be the width and height obtained from req's image data, as defined by the relevant codec.

Let dimX be the value of exifTagMap's tag 0xA002 (PixelXDimension).

Let dimY be the value of exifTagMap's tag 0xA003 (PixelYDimension).

Let resX be the value of exifTagMap's tag 0x011A (XResolution).

Let resY be the value of exifTagMap's tag 0x011B (YResolution).

Let resUnit be the value of exifTagMap's tag 0x0128 (ResolutionUnit).

If all the following are true:

dimX is a positive integer;

dimY is a positive integer;

resX is a positive floating-point number;

resY is a positive floating-point number;

physicalWidth × 72 / resX is dimX;

physicalHeight × 72 / resY is dimY;

resUnit is 2 (Inch),

then:

If req's image data is CORS-cross-origin, then set img's natural dimensions to dimX and dimY, and scale img's pixel data accordingly.

Otherwise, set req's preferred density-corrected dimensions to a struct with its width set to dimX and its height set to dimY.

Update req's img element's presentation appropriately.

Resolution in EXIF is equivalent to CSS points per inch, therefore 72 is the base for computing size from resolution.

It is not yet specified what would be the case if EXIF arrives after the image is already presented. See issue #4929.

4.8.4.3.7 Selecting an image source

To select an image source given an img element el:

Update the source set for el.

If el's source set is empty, return null as the URL and undefined as the pixel density.

Return the result of selecting an image from el's source set.

To select an image source from a source set given a source set sourceSet:

If an entry b in sourceSet has the same associated pixel density descriptor as an earlier entry a in sourceSet, then remove entry b. Repeat this step until none of the entries in sourceSet have the same associated pixel density descriptor as an earlier entry.

In an implementation-defined manner, choose one image source from sourceSet. Let selectedSource be this choice.

Return selectedSource and its associated pixel density.

4.8.4.3.8 Creating a source set from attributes

When asked to create a source set given a string default source, a string srcset, a string sizes, and an element or null img:

Let source set be an empty source set.

If srcset is not an empty string, then set source set to the result of parsing srcset.

Set source set's source size to the result of parsing sizes with img.

If default source is not the empty string and source set does not contain an image source with a pixel density descriptor value of 1, and no image source with a width descriptor, append default source to source set.

Normalize the source densities of source set.

Return source set.

4.8.4.3.9 Updating the source set

When asked to update the source set for a given img or link element el, user agents must do the following:

Set el's source set to an empty source set.

Let elements be « el ».

If el is an img element whose parent node is a picture element, then replace the contents of elements with el's parent node's child elements, retaining relative order.

Let img be el if el is an img element, otherwise null.

For each child in elements:

If child is el:

Let default source be the empty string.

Let srcset be the empty string.

Let sizes be the empty string.

If el is an img element that has a srcset attribute, then set srcset to that attribute's value.

Otherwise, if el is a link element that has an imagesrcset attribute, then set srcset to that attribute's value.

If el is an img element that has a sizes attribute, then set sizes to that attribute's value.

Otherwise, if el is a link element that has an imagesizes attribute, then set sizes to that attribute's value.

If el is an img element that has a src attribute, then set default source to that attribute's value.

Otherwise, if el is a link element that has an href attribute, then set default source to that attribute's value.

Set el's source set to the result of creating a source set given default source, srcset, sizes, and img.

Return.

If el is a link element, then elements contains only el, so this step will be reached immediately and the rest of the algorithm will not run.

If child is not a source element, then continue.

If child does not have a srcset attribute, continue to the next child.

Parse child's srcset attribute and let source set be the returned source set.

If source set has zero image sources, continue to the next child.

If child has a media attribute, and its value does not match the environment, continue to the next child.

Parse child's sizes attribute with img, and let source set's source size be the returned value.

If child has a type attribute, and its value is an unknown or unsupported MIME type, continue to the next child.

If child has width or height attributes, set el's dimension attribute source to child. Otherwise, set el's dimension attribute source to el.

Normalize the source densities of source set.

Set el's source set to source set.

Return.

Each img element independently considers its previous sibling source elements plus the img element itself for selecting an image source, ignoring any other (invalid) elements, including other img elements in the same picture element, or source elements that are following siblings of the relevant img element.

4.8.4.3.10 Parsing a srcset attribute

When asked to parse a srcset attribute from an element, parse the value of the element's srcset attribute as follows:

Let input be the value passed to this algorithm.

Let position be a pointer into input, initially pointing at the start of the string.

Let candidates be an initially empty source set.

Splitting loop: Collect a sequence of code points that are ASCII whitespace or U+002C COMMA characters from input given position. If any U+002C COMMA characters were collected, that is a parse error.

If position is past the end of input, return candidates.

Collect a sequence of code points that are not ASCII whitespace from input given position, and let url be the result.

Let descriptors be a new empty list.

If url ends with U+002C (,), then:

Remove all trailing U+002C COMMA characters from url. If this removed more than one character, that is a parse error.

Otherwise:

Descriptor tokenizer: Skip ASCII whitespace within input given position.

Let current descriptor be the empty string.

Let state be in descriptor.

Let c be the character at position. Do the following depending on the value of state. For the purpose of this step, "EOF" is a special character representing that position is past the end of input.

In descriptor

Do the following, depending on the value of c:

ASCII whitespace

If current descriptor is not empty, append current descriptor to descriptors and let current descriptor be the empty string. Set state to after descriptor.

U+002C COMMA (,)

Advance position to the next character in input. If current descriptor is not empty, append current descriptor to descriptors. Jump to the step labeled descriptor parser.

U+0028 LEFT PARENTHESIS (()

Append c to current descriptor. Set state to in parens.

EOF

If current descriptor is not empty, append current descriptor to descriptors. Jump to the step labeled descriptor parser.

Anything else

Append c to current descriptor.

In parens

Do the following, depending on the value of c:

U+0029 RIGHT PARENTHESIS ())

Append c to current descriptor. Set state to in descriptor.

EOF

Append current descriptor to descriptors. Jump to the step labeled descriptor parser.

Anything else

Append c to current descriptor.

After descriptor

Do the following, depending on the value of c:

ASCII whitespace

Stay in this state.

EOF

Jump to the step labeled descriptor parser.

Anything else

Set state to in descriptor. Set position to the previous character in input.

Advance position to the next character in input. Repeat this step.

In order to be compatible with future additions, this algorithm supports multiple descriptors and descriptors with parens.

Descriptor parser: Let error be no.

Let width be absent.

Let density be absent.

Let future-compat-h be absent.

For each descriptor in descriptors, run the appropriate set of steps from the following list:

If the descriptor consists of a valid non-negative integer followed by a U+0077 LATIN SMALL LETTER W character

If the user agent does not support the sizes attribute, let error be yes.

A conforming user agent will support the sizes attribute. However, user agents typically implement and ship features in an incremental manner in practice.

If width and density are not both absent, then let error be yes.

Apply the rules for parsing non-negative integers to the descriptor. If the result is 0, let error be yes. Otherwise, let width be the result.

If the descriptor consists of a valid floating-point number followed by a U+0078 LATIN SMALL LETTER X character

If width, density and future-compat-h are not all absent, then let error be yes.

Apply the rules for parsing floating-point number values to the descriptor. If the result is less than 0, let error be yes. Otherwise, let density be the result.

If density is 0, the natural dimensions will be infinite. User agents are expected to have limits in how big images can be rendered.

If the descriptor consists of a valid non-negative integer followed by a U+0068 LATIN SMALL LETTER H character

This is a parse error.

If future-compat-h and density are not both absent, then let error be yes.

Apply the rules for parsing non-negative integers to the descriptor. If the result is 0, let error be yes. Otherwise, let future-compat-h be the result.

Anything else

Let error be yes.

If future-compat-h is not absent and width is absent, let error be yes.

If error is still no, then append a new image source to candidates whose URL is url, associated with a width width if not absent and a pixel density density if not absent. Otherwise, there is a parse error.

Return to the step labeled splitting loop.

4.8.4.3.11 Parsing a sizes attribute

When asked to parse a sizes attribute from an element element, with an img element or null img:

Let unparsed sizes list be the result of parsing a comma-separated list of component values from the value of element's sizes attribute (or the empty string, if the attribute is absent). [CSSSYNTAX]

Let size be null.

For each unparsed size in unparsed sizes list:

Remove all consecutive <whitespace-token>s from the end of unparsed size. If unparsed size is now empty, then that is a parse error; continue.

If the last component value in unparsed size is a valid non-negative <source-size-value>, then set size to its value and remove the component value from unparsed size. Any CSS function other than the math functions is invalid. Otherwise, there is a parse error; continue.

If size is auto, and img is not null, and img is being rendered, and img allows auto-sizes, then set size to the concrete object size width of img, in CSS pixels.

If size is still auto, then it will be ignored.

Remove all consecutive <whitespace-token>s from the end of unparsed size. If unparsed size is now empty:

If this was not the last item in unparsed sizes list, that is a parse error.

If size is not auto, then return size. Otherwise, continue.

Parse the remaining component values in unparsed size as a <media-condition>. If it does not parse correctly, or it does parse correctly but the <media-condition> evaluates to false, continue. [MQ]

If size is not auto, then return size. Otherwise, continue.

Return 100vw.

It is invalid to use a bare <source-size-value> that is a <length> (without an accompanying <media-condition>) as an entry in the <source-size-list> that is not the last entry. However, the parsing algorithm allows it at any point in the <source-size-list>, and will accept it immediately as the size if the preceding entries in the list weren't used. This is to enable future extensions, and protect against simple author errors such as a final trailing comma. A bare auto keyword is allowed to have other entries following it to provide a fallback for legacy user agents.

4.8.4.3.12 Normalizing the source densities

An image source can have a pixel density descriptor, a width descriptor, or no descriptor at all accompanying its URL. Normalizing a source set gives every image source a pixel density descriptor.

When asked to normalize the source densities of a source set source set, the user agent must do the following:

Let source size be source set's source size.

For each image source in source set:

If the image source has a pixel density descriptor, continue to the next image source.

Otherwise, if the image source has a width descriptor, replace the width descriptor with a pixel density descriptor with a value of the width descriptor value divided by source size and a unit of x.

If the source size is 0, then the density would be infinity, which results in the natural dimensions being 0 by 0.

Otherwise, give the image source a pixel density descriptor of 1x.

4.8.4.3.13 Reacting to environment changes

The user agent may at any time run the following algorithm to update an img element's image in order to react to changes in the environment. (User agents are not required to ever run this algorithm; for example, if the user is not looking at the page any more, the user agent might want to wait until the user has returned to the page before determining which image to use, in case the environment changes again in the meantime.)

User agents are encouraged to run this algorithm in particular when the user changes the viewport's size (e.g. by resizing the window or changing the page zoom), and when an img element is inserted into a document, so that the density-corrected natural width and height match the new viewport, and so that the correct image is chosen when art direction is involved.

Await a stable state. The synchronous section consists of all the remaining steps of this algorithm until the algorithm says the synchronous section has ended. (Steps in synchronous sections are marked with ⌛.)

⌛ If the img element does not use srcset or picture, its node document is not fully active, it has image data whose resource type is multipart/x-mixed-replace, or its pending request is not null, then return.

⌛ Let selected source and selected pixel density be the URL and pixel density that results from selecting an image source, respectively.

⌛ If selected source is null, then return.

⌛ If selected source and selected pixel density are the same as the element's last selected source and current pixel density, then return.

⌛ Let urlString be the result of encoding-parsing-and-serializing a URL given selected source, relative to the element's node document.

⌛ If urlString is failure, then return.

⌛ Let corsAttributeState be the state of the element's crossorigin content attribute.

⌛ Let origin be the img element's node document's origin.

⌛ Let client be the img element's node document's relevant settings object.

⌛ Let key be a tuple consisting of urlString, corsAttributeState, and, if corsAttributeState is not No CORS, origin.

⌛ Let image request be a new image request whose current URL is urlString.

⌛ Set the element's pending request to image request.

End the synchronous section, continuing the remaining steps in parallel.

If the list of available images contains an entry for key, then set image request's image data to that of the entry. Continue to the next step.

Otherwise:

Let request be the result of creating a potential-CORS request given urlString, "image", and corsAttributeState.

Set request's client to client, set request's initiator to "imageset", and set request's synchronous flag.

Set request's referrer policy to the current state of the element's referrerpolicy attribute.

Set request's priority to the current state of the element's fetchpriority attribute.

Let response be the result of fetching request.

If response's unsafe response is a network error or if the image format is unsupported (as determined by applying the image sniffing rules, again as mentioned earlier), or if the user agent is able to determine that image request's image is corrupted in some fatal way such that the image dimensions cannot be obtained, or if the resource type is multipart/x-mixed-replace, then set the pending request to null and abort these steps.

Otherwise, response's unsafe response is image request's image data. It can be either CORS-same-origin or CORS-cross-origin; this affects the image's interaction with other APIs (e.g., when used on a canvas).

Queue an element task on the DOM manipulation task source given the img element and the following steps:

If the img element has experienced relevant mutations since this algorithm started, then set the pending request to null and abort these steps.

Set the img element's last selected source to selected source and the img element's current pixel density to selected pixel density.

Set the image request's state to completely available.

Add the image to the list of available images using the key key, with the ignore higher-layer caching flag set.

Upgrade the pending request to the current request.

Prepare image request for presentation given the img element.

Fire an event named load at the img element.

4.8.4.4 Requirements for providing text to act as an alternative for images
4.8.4.4.1 General guidelines

Except where otherwise specified, the alt attribute must be specified and its value must not be empty; the value must be an appropriate replacement for the image. The specific requirements for the alt attribute depend on what the image is intended to represent, as described in the following sections.

The most general rule to consider when writing alternative text is the following: the intent is that replacing every image with the text of its alt attribute does not change the meaning of the page.

So, in general, alternative text can be written by considering what one would have written had one not been able to include the image.

A corollary to this is that the alt attribute's value should never contain text that could be considered the image's caption, title, or legend. It is supposed to contain replacement text that could be used by users instead of the image; it is not meant to supplement the image. The title attribute can be used for supplemental information.

Another corollary is that the alt attribute's value should not repeat information that is already provided in the prose next to the image.

One way to think of alternative text is to think about how you would read the page containing the image to someone over the phone, without mentioning that there is an image present. Whatever you say instead of the image is typically a good start for writing the alternative text.

4.8.4.4.2 A link or button containing nothing but the image

When an a element that creates a hyperlink, or a button element, has no textual content but contains one or more images, the alt attributes must contain text that together convey the purpose of the link or button.

In this example, a user is asked to pick their preferred color from a list of three. Each color is given by an image, but for users who have configured their user agent not to display images, the color names are used instead:

<h1>Pick your color</h1>
<ul>
 <li><a href="green.html"><img src="green.jpeg" alt="Green"></a></li>
 <li><a href="blue.html"><img src="blue.jpeg" alt="Blue"></a></li>
 <li><a href="red.html"><img src="red.jpeg" alt="Red"></a></li>
</ul>

In this example, each button has a set of images to indicate the kind of color output desired by the user. The first image is used in each case to give the alternative text.

<button name="rgb"><img src="red" alt="RGB"><img src="green" alt=""><img src="blue" alt=""></button>
<button name="cmyk"><img src="cyan" alt="CMYK"><img src="magenta" alt=""><img src="yellow" alt=""><img src="black" alt=""></button>

Since each image represents one part of the text, it could also be written like this:

<button name="rgb"><img src="red" alt="R"><img src="green" alt="G"><img src="blue" alt="B"></button>
<button name="cmyk"><img src="cyan" alt="C"><img src="magenta" alt="M"><img src="yellow" alt="Y"><img src="black" alt="K"></button>

However, with other alternative text, this might not work, and putting all the alternative text into one image in each case might make more sense:

<button name="rgb"><img src="red" alt="sRGB profile"><img src="green" alt=""><img src="blue" alt=""></button>
<button name="cmyk"><img src="cyan" alt="CMYK profile"><img src="magenta" alt=""><img src="yellow" alt=""><img src="black" alt=""></button>
4.8.4.4.3 A phrase or paragraph with an alternative graphical representation: charts, diagrams, graphs, maps, illustrations

Sometimes something can be more clearly stated in graphical form, for example as a flowchart, a diagram, a graph, or a simple map showing directions. In such cases, an image can be given using the img element, but the lesser textual version must still be given, so that users who are unable to view the image (e.g. because they have a very slow connection, or because they are using a text-only browser, or because they are listening to the page being read out by a hands-free automobile voice web browser, or simply because they are blind) are still able to understand the message being conveyed.

The text must be given in the alt attribute, and must convey the same message as the image specified in the src attribute.

It is important to realize that the alternative text is a replacement for the image, not a description of the image.

In the following example we have a flowchart in image form, with text in the alt attribute rephrasing the flowchart in prose form:

<p>In the common case, the data handled by the tokenization stage
comes from the network, but it can also come from script.</p>
<p><img src="images/parsing-model-overview.svg" alt="The Network
passes data to the Input Stream Preprocessor, which passes it to the
Tokenizer, which passes it to the Tree Construction stage. From there,
data goes to both the DOM and to Script Execution. Script Execution is
linked to the DOM, and, using document.write(), passes data to the
Tokenizer."></p>

Here's another example, showing a good solution and a bad solution to the problem of including an image in a description.

First, here's the good solution. This sample shows how the alternative text should just be what you would have put in the prose if the image had never existed.

<!-- This is the correct way to do things. -->
<p>
 You are standing in an open field west of a house.
 <img src="house.jpeg" alt="The house is white, with a boarded front door.">
 There is a small mailbox here.
</p>

Second, here's the bad solution. In this incorrect way of doing things, the alternative text is simply a description of the image, instead of a textual replacement for the image. It's bad because when the image isn't shown, the text doesn't flow as well as in the first example.

<!-- This is the wrong way to do things. -->
<p>
 You are standing in an open field west of a house.
 <img src="house.jpeg" alt="A white house, with a boarded front door.">
 There is a small mailbox here.
</p>

Text such as "Photo of white house with boarded door" would be equally bad alternative text (though it could be suitable for the title attribute or in the figcaption element of a figure with this image).

4.8.4.4.4 A short phrase or label with an alternative graphical representation: icons, logos

A document can contain information in iconic form. The icon is intended to help users of visual browsers to recognize features at a glance.

In some cases, the icon is supplemental to a text label conveying the same meaning. In those cases, the alt attribute must be present but must be empty.

Here the icons are next to text that conveys the same meaning, so they have an empty alt attribute:

<nav>
 <p><a href="/help/"><img src="/icons/help.png" alt=""> Help</a></p>
 <p><a href="/configure/"><img src="/icons/configuration.png" alt="">
 Configuration Tools</a></p>
</nav>

In other cases, the icon has no text next to it describing what it means; the icon is supposed to be self-explanatory. In those cases, an equivalent textual label must be given in the alt attribute.

Here, posts on a news site are labeled with an icon indicating their topic.

<body>
 <article>
  <header>
   <h1>Ratatouille wins <i>Best Movie of the Year</i> award</h1>
   <p><img src="movies.png" alt="Movies"></p>
  </header>
  <p>Pixar has won yet another <i>Best Movie of the Year</i> award,
  making this its 8th win in the last 12 years.</p>
 </article>
 <article>
  <header>
   <h1>Latest TWiT episode is online</h1>
   <p><img src="podcasts.png" alt="Podcasts"></p>
  </header>
  <p>The latest TWiT episode has been posted, in which we hear
  several tech news stories as well as learning much more about the
  iPhone. This week, the panelists compare how reflective their
  iPhones' Apple logos are.</p>
 </article>
</body>

Many pages include logos, insignia, flags, or emblems, which stand for a particular entity such as a company, organization, project, band, software package, country, or some such.

If the logo is being used to represent the entity, e.g. as a page heading, the alt attribute must contain the name of the entity being represented by the logo. The alt attribute must not contain text like the word "logo", as it is not the fact that it is a logo that is being conveyed, it's the entity itself.

If the logo is being used next to the name of the entity that it represents, then the logo is supplemental, and its alt attribute must instead be empty.

If the logo is merely used as decorative material (as branding, or, for example, as a side image in an article that mentions the entity to which the logo belongs), then the entry below on purely decorative images applies. If the logo is actually being discussed, then it is being used as a phrase or paragraph (the description of the logo) with an alternative graphical representation (the logo itself), and the first entry above applies.

In the following snippets, all four of the above cases are present. First, we see a logo used to represent a company:

<h1><img src="XYZ.gif" alt="The XYZ company"></h1>

Next, we see a paragraph which uses a logo right next to the company name, and so doesn't have any alternative text:

<article>
 <h2>News</h2>
 <p>We have recently been looking at buying the <img src="alpha.gif"
 alt=""> ΑΒΓ company, a small Greek company
 specializing in our type of product.</p>

In this third snippet, we have a logo being used in an aside, as part of the larger article discussing the acquisition:

<aside><p><img src="alpha-large.gif" alt=""></p></aside>
 <p>The ΑΒΓ company has had a good quarter, and our
 pie chart studies of their accounts suggest a much bigger blue slice
 than its green and orange slices, which is always a good sign.</p>
</article>

Finally, we have an opinion piece talking about a logo, and the logo is therefore described in detail in the alternative text.

<p>Consider for a moment their logo:</p>

<p><img src="/images/logo" alt="It consists of a green circle with a
green question mark centered inside it."></p>

<p>How unoriginal can you get? I mean, oooooh, a question mark, how
<em>revolutionary</em>, how utterly <em>ground-breaking</em>, I'm
sure everyone will rush to adopt those specifications now! They could
at least have tried for some sort of, I don't know, sequence of
rounded squares with varying shades of green and bold white outlines,
at least that would look good on the cover of a blue book.</p>

This example shows how the alternative text should be written such that if the image isn't available, and the text is used instead, the text flows seamlessly into the surrounding text, as if the image had never been there in the first place.

4.8.4.4.5 Text that has been rendered to a graphic for typographical effect

Sometimes, an image just consists of text, and the purpose of the image is not to highlight the actual typographic effects used to render the text, but just to convey the text itself.

In such cases, the alt attribute must be present but must consist of the same text as written in the image itself.

Consider a graphic containing the text "Earth Day", but with the letters all decorated with flowers and plants. If the text is merely being used as a heading, to spice up the page for graphical users, then the correct alternative text is just the same text "Earth Day", and no mention need be made of the decorations:

<h1><img src="earthdayheading.png" alt="Earth Day"></h1>

An illuminated manuscript might use graphics for some of its images. The alternative text in such a situation is just the character that the image represents.

<p><img src="initials/o.svg" alt="O">nce upon a time and a long long time ago, late at
night, when it was dark, over the hills, through the woods, across a great ocean, in a land far
away, in a small house, on a hill, under a full moon...

When an image is used to represent a character that cannot otherwise be represented in Unicode, for example gaiji, itaiji, or new characters such as novel currency symbols, the alternative text should be a more conventional way of writing the same thing, e.g. using the phonetic hiragana or katakana to give the character's pronunciation.

In this example from 1997, a new-fangled currency symbol that looks like a curly E with two bars in the middle instead of one is represented using an image. The alternative text gives the character's pronunciation.

<p>Only <img src="euro.png" alt="euro ">5.99!

An image should not be used if characters would serve an identical purpose. Only when the text cannot be directly represented using text, e.g., because of decorations or because there is no appropriate character (as in the case of gaiji), would an image be appropriate.

If an author is tempted to use an image because their default system font does not support a given character, then web fonts are a better solution than images.

4.8.4.4.6 A graphical representation of some of the surrounding text

In many cases, the image is actually just supplementary, and its presence merely reinforces the surrounding text. In these cases, the alt attribute must be present but its value must be the empty string.

In general, an image falls into this category if removing the image doesn't make the page any less useful, but including the image makes it a lot easier for users of visual browsers to understand the concept.

A flowchart that repeats the previous paragraph in graphical form:

<p>The Network passes data to the Input Stream Preprocessor, which
passes it to the Tokenizer, which passes it to the Tree Construction
stage. From there, data goes to both the DOM and to Script Execution.
Script Execution is linked to the DOM, and, using document.write(),
passes data to the Tokenizer.</p>
<p><img src="images/parsing-model-overview.svg" alt=""></p>

In these cases, it would be wrong to include alternative text that consists of just a caption. If a caption is to be included, then either the title attribute can be used, or the figure and figcaption elements can be used. In the latter case, the image would in fact be a phrase or paragraph with an alternative graphical representation, and would thus require alternative text.

<!-- Using the title="" attribute -->
<p>The Network passes data to the Input Stream Preprocessor, which
passes it to the Tokenizer, which passes it to the Tree Construction
stage. From there, data goes to both the DOM and to Script Execution.
Script Execution is linked to the DOM, and, using document.write(),
passes data to the Tokenizer.</p>
<p><img src="images/parsing-model-overview.svg" alt=""
        title="Flowchart representation of the parsing model."></p>
<!-- Using <figure> and <figcaption> -->
<p>The Network passes data to the Input Stream Preprocessor, which
passes it to the Tokenizer, which passes it to the Tree Construction
stage. From there, data goes to both the DOM and to Script Execution.
Script Execution is linked to the DOM, and, using document.write(),
passes data to the Tokenizer.</p>
<figure>
 <img src="images/parsing-model-overview.svg" alt="The Network leads to
 the Input Stream Preprocessor, which leads to the Tokenizer, which
 leads to the Tree Construction stage. The Tree Construction stage
 leads to two items. The first is Script Execution, which leads via
 document.write() back to the Tokenizer. The second item from which
 Tree Construction leads is the DOM. The DOM is related to the Script
 Execution.">
 <figcaption>Flowchart representation of the parsing model.</figcaption>
</figure>
<!-- This is WRONG. Do not do this. Instead, do what the above examples do. -->
<p>The Network passes data to the Input Stream Preprocessor, which
passes it to the Tokenizer, which passes it to the Tree Construction
stage. From there, data goes to both the DOM and to Script Execution.
Script Execution is linked to the DOM, and, using document.write(),
passes data to the Tokenizer.</p>
<p><img src="images/parsing-model-overview.svg"
        alt="Flowchart representation of the parsing model."></p>
<!-- Never put the image's caption in the alt="" attribute! -->

A graph that repeats the previous paragraph in graphical form:

<p>According to a study covering several billion pages,
about 62% of documents on the web in 2007 triggered the Quirks
rendering mode of web browsers, about 30% triggered the Almost
Standards mode, and about 9% triggered the Standards mode.</p>
<p><img src="rendering-mode-pie-chart.png" alt=""></p>
4.8.4.4.7 Ancillary images

Sometimes, an image is not critical to the content, but is nonetheless neither purely decorative nor entirely redundant with the text. In these cases, the alt attribute must be present, and its value should either be the empty string, or a textual representation of the information that the image conveys. If the image has a caption giving the image's title, then the alt attribute's value must not be empty (as that would be quite confusing for non-visual readers).

Consider a news article about a political figure, in which the individual's face was shown in an image. The image is not purely decorative, as it is relevant to the story. The image is not entirely redundant with the story either, as it shows what the politician looks like. Whether any alternative text need be provided is an authoring decision, decided by whether the image influences the interpretation of the prose.

In this first variant, the image is shown without context, and no alternative text is provided:

<p><img src="president.jpeg" alt=""> Ahead of today's referendum,
the President wrote an open letter to all registered voters. In it, she admitted that the country was
divided.</p>

If the picture is just a face, there might be no value in describing it. It's of no interest to the reader whether the individual has red hair or blond hair, whether the individual has white skin or black skin, whether the individual has one eye or two eyes.

However, if the picture is more dynamic, for instance showing the politician as angry, or particularly happy, or devastated, some alternative text would be useful in setting the tone of the article, a tone that might otherwise be missed:

<p><img src="president.jpeg" alt="The President is sad.">
Ahead of today's referendum, the President wrote an open letter to all
registered voters. In it, she admitted that the country was divided.
</p>
<p><img src="president.jpeg" alt="The President is happy!">
Ahead of today's referendum, the President wrote an open letter to all
registered voters. In it, she admitted that the country was divided.
</p>

Whether the individual was "sad" or "happy" makes a difference to how the rest of the paragraph is to be interpreted: is she likely saying that she is unhappy with the country being divided, or is she saying that the prospect of a divided country is good for her political career? The interpretation varies based on the image.

If the image has a caption, then including alternative text avoids leaving the non-visual user confused as to what the caption refers to.

<p>Ahead of today's referendum, the President wrote an open letter to
all registered voters. In it, she admitted that the country was divided.</p>
<figure>
 <img src="president.jpeg"
      alt="A high forehead, cheerful disposition, and dark hair round out the President's face.">
 <figcaption> The President of Ruritania. Photo © 2014 PolitiPhoto. </figcaption>
</figure>
4.8.4.4.8 A purely decorative image that doesn't add any information

If an image is decorative but isn't especially page-specific — for example an image that forms part of a site-wide design scheme — the image should be specified in the site's CSS, not in the markup of the document.

However, a decorative image that isn't discussed by the surrounding text but still has some relevance can be included in a page using the img element. Such images are decorative, but still form part of the content. In these cases, the alt attribute must be present but its value must be the empty string.

Examples where the image is purely decorative despite being relevant would include things like a photo of the Black Rock City landscape in a blog post about an event at Burning Man, or an image of a painting inspired by a poem, on a page reciting that poem. The following snippet shows an example of the latter case (only the first verse is included in this snippet):

<h1>The Lady of Shalott</h1>
<p><img src="shalott.jpeg" alt=""></p>
<p>On either side the river lie<br>
Long fields of barley and of rye,<br>
That clothe the wold and meet the sky;<br>
And through the field the road run by<br>
To many-tower'd Camelot;<br>
And up and down the people go,<br>
Gazing where the lilies blow<br>
Round an island there below,<br>
The island of Shalott.</p>
4.8.4.4.9 A group of images that form a single larger picture with no links

When a picture has been sliced into smaller image files that are then displayed together to form the complete picture again, one of the images must have its alt attribute set as per the relevant rules that would be appropriate for the picture as a whole, and then all the remaining images must have their alt attribute set to the empty string.

In the following example, a picture representing a company logo for XYZ Corp has been split into two pieces, the first containing the letters "XYZ" and the second with the word "Corp". The alternative text ("XYZ Corp") is all in the first image.

<h1><img src="logo1.png" alt="XYZ Corp"><img src="logo2.png" alt=""></h1>

In the following example, a rating is shown as three filled stars and two empty stars. While the alternative text could have been "★★★☆☆", the author has instead decided to more helpfully give the rating in the form "3 out of 5". That is the alternative text of the first image, and the rest have blank alternative text.

<p>Rating: <meter max=5 value=3><img src="1" alt="3 out of 5"
  ><img src="1" alt=""><img src="1" alt=""><img src="0" alt=""
  ><img src="0" alt=""></meter></p>
4.8.4.4.10 A group of images that form a single larger picture with links

Generally, image maps should be used instead of slicing an image for links.

However, if an image is indeed sliced and any of the components of the sliced picture are the sole contents of links, then one image per link must have alternative text in its alt attribute representing the purpose of the link.

In the following example, a picture representing the flying spaghetti monster emblem, with each of the left noodly appendages and the right noodly appendages in different images, so that the user can pick the left side or the right side in an adventure.

<h1>The Church</h1>
<p>You come across a flying spaghetti monster. Which side of His
Noodliness do you wish to reach out for?</p>
<p><a href="?go=left" ><img src="fsm-left.png"  alt="Left side. "></a
  ><img src="fsm-middle.png" alt=""
  ><a href="?go=right"><img src="fsm-right.png" alt="Right side."></a></p>
4.8.4.4.11 A key part of the content

In some cases, the image is a critical part of the content. This could be the case, for instance, on a page that is part of a photo gallery. The image is the whole point of the page containing it.

How to provide alternative text for an image that is a key part of the content depends on the image's provenance.

The general case

When it is possible for detailed alternative text to be provided, for example if the image is part of a series of screenshots in a magazine review, or part of a comic strip, or is a photograph in a blog entry about that photograph, text that can serve as a substitute for the image must be given as the contents of the alt attribute.

A screenshot in a gallery of screenshots for a new OS, with some alternative text:

<figure>
 <img src="KDE%20Light%20desktop.png"
      alt="The desktop is blue, with icons along the left hand side in
           two columns, reading System, Home, K-Mail, etc. A window is
           open showing that menus wrap to a second line if they
           cannot fit in the window. The window has a list of icons
           along the top, with an address bar below it, a list of
           icons for tabs along the left edge, a status bar on the
           bottom, and two panes in the middle. The desktop has a bar
           at the bottom of the screen with a few buttons, a pager, a
           list of open applications, and a clock.">
 <figcaption>Screenshot of a KDE desktop.</figcaption>
</figure>

A graph in a financial report:

<img src="sales.gif"
     title="Sales graph"
     alt="From 1998 to 2005, sales increased by the following percentages
     with each year: 624%, 75%, 138%, 40%, 35%, 9%, 21%">

Note that "sales graph" would be inadequate alternative text for a sales graph. Text that would be a good caption is not generally suitable as replacement text.

Images that defy a complete description

In certain cases, the nature of the image might be such that providing thorough alternative text is impractical. For example, the image could be indistinct, or could be a complex fractal, or could be a detailed topographical map.

In these cases, the alt attribute must contain some suitable alternative text, but it may be somewhat brief.

Sometimes there simply is no text that can do justice to an image. For example, there is little that can be said to usefully describe a Rorschach inkblot test. However, a description, even if brief, is still better than nothing:

<figure>
 <img src="/commons/a/a7/Rorschach1.jpg" alt="A shape with left-right
 symmetry with indistinct edges, with a small gap in the center, two
 larger gaps offset slightly from the center, with two similar gaps
 under them. The outline is wider in the top half than the bottom
 half, with the sides extending upwards higher than the center, and
 the center extending below the sides.">
 <figcaption>A black outline of the first of the ten cards
 in the Rorschach inkblot test.</figcaption>
</figure>

Note that the following would be a very bad use of alternative text:

<!-- This example is wrong. Do not copy it. -->
<figure>
 <img src="/commons/a/a7/Rorschach1.jpg" alt="A black outline
 of the first of the ten cards in the Rorschach inkblot test.">
 <figcaption>A black outline of the first of the ten cards
 in the Rorschach inkblot test.</figcaption>
</figure>

Including the caption in the alternative text like this isn't useful because it effectively duplicates the caption for users who don't have images, taunting them twice yet not helping them any more than if they had only read or heard the caption once.

Another example of an image that defies full description is a fractal, which, by definition, is infinite in detail.

The following example shows one possible way of providing alternative text for the full view of an image of the Mandelbrot set.

<img src="ms1.jpeg" alt="The Mandelbrot set appears as a cardioid with
its cusp on the real axis in the positive direction, with a smaller
bulb aligned along the same center line, touching it in the negative
direction, and with these two shapes being surrounded by smaller bulbs
of various sizes.">

Similarly, a photograph of a person's face, for example in a biography, can be considered quite relevant and key to the content, but it can be hard to fully substitute text for:

<section class="bio">
 <h1>A Biography of Isaac Asimov</h1>
 <p>Born <b>Isaak Yudovich Ozimov</b> in 1920, Isaac was a prolific author.</p>
 <p><img src="headpics/asimov.jpeg" alt="Isaac Asimov had dark hair, a tall forehead, and wore glasses.
 Later in life, he wore long white sideburns."></p>
 <p>Asimov was born in Russia, and moved to the US when he was three years old.</p>
 <p>...</p>
</section>

In such cases it is unnecessary (and indeed discouraged) to include a reference to the presence of the image itself in the alternative text, since such text would be redundant with the browser itself reporting the presence of the image. For example, if the alternative text was "A photo of Isaac Asimov", then a conforming user agent might read that out as "(Image) A photo of Isaac Asimov" rather than the more useful "(Image) Isaac Asimov had dark hair, a tall forehead, and wore glasses...".

Images whose contents are not known

In some unfortunate cases, there might be no alternative text available at all, either because the image is obtained in some automated fashion without any associated alternative text (e.g., a webcam), or because the page is being generated by a script using user-provided images where the user did not provide suitable or usable alternative text (e.g. photograph sharing sites), or because the author does not themself know what the images represent (e.g. a blind photographer sharing an image on their blog).

In such cases, the alt attribute may be omitted, but one of the following conditions must be met as well:

The img element is in a figure element that contains a figcaption element that contains content other than inter-element whitespace, and, ignoring the figcaption element and its descendants, the figure element has no flow content descendants other than inter-element whitespace and the img element.

The title attribute is present and has a non-empty value.

Relying on the title attribute is currently discouraged as many user agents do not expose the attribute in an accessible manner as required by this specification (e.g. requiring a pointing device such as a mouse to cause a tooltip to appear, which excludes keyboard-only users and touch-only users, such as anyone with a modern phone or tablet).

Such cases are to be kept to an absolute minimum. If there is even the slightest possibility of the author having the ability to provide real alternative text, then it would not be acceptable to omit the alt attribute.

A photo on a photo-sharing site, if the site received the image with no metadata other than the caption, could be marked up as follows:

<figure>
 <img src="1100670787_6a7c664aef.jpg">
 <figcaption>Bubbles traveled everywhere with us.</figcaption>
</figure>

It would be better, however, if a detailed description of the important parts of the image obtained from the user and included on the page.

A blind user's blog in which a photo taken by the user is shown. Initially, the user might not have any idea what the photo they took shows:

<article>
 <h1>I took a photo</h1>
 <p>I went out today and took a photo!</p>
 <figure>
  <img src="photo2.jpeg">
  <figcaption>A photograph taken blindly from my front porch.</figcaption>
 </figure>
</article>

Eventually though, the user might obtain a description of the image from their friends and could then include alternative text:

<article>
 <h1>I took a photo</h1>
 <p>I went out today and took a photo!</p>
 <figure>
  <img src="photo2.jpeg" alt="The photograph shows my squirrel
  feeder hanging from the edge of my roof. It is half full, but there
  are no squirrels around. In the background, out-of-focus trees fill the
  shot. The feeder is made of wood with a metal grate, and it contains
  peanuts. The edge of the roof is wooden too, and is painted white
  with light blue streaks.">
  <figcaption>A photograph taken blindly from my front porch.</figcaption>
 </figure>
</article>

Sometimes the entire point of the image is that a textual description is not available, and the user is to provide the description. For instance, the point of a CAPTCHA image is to see if the user can literally read the graphic. Here is one way to mark up a CAPTCHA (note the title attribute):

<p><label>What does this image say?
<img src="captcha.cgi?id=8934" title="CAPTCHA">
<input type=text name=captcha></label>
(If you cannot see the image, you can use an <a
href="?audio">audio</a> test instead.)</p>

Another example would be software that displays images and asks for alternative text precisely for the purpose of then writing a page with correct alternative text. Such a page could have a table of images, like this:

<table>
 <thead>
  <tr> <th> Image <th> Description
 <tbody>
  <tr>
   <td> <img src="2421.png" title="Image 640 by 100, filename 'banner.gif'">
   <td> <input name="alt2421">
  <tr>
   <td> <img src="2422.png" title="Image 200 by 480, filename 'ad3.gif'">
   <td> <input name="alt2422">
</table>

Notice that even in this example, as much useful information as possible is still included in the title attribute.

Since some users cannot use images at all (e.g. because they have a very slow connection, or because they are using a text-only browser, or because they are listening to the page being read out by a hands-free automobile voice web browser, or simply because they are blind), the alt attribute is only allowed to be omitted rather than being provided with replacement text when no alternative text is available and none can be made available, as in the above examples. Lack of effort from the part of the author is not an acceptable reason for omitting the alt attribute.

4.8.4.4.12 An image not intended for the user

Generally authors should avoid using img elements for purposes other than showing images.

If an img element is being used for purposes other than showing an image, e.g. as part of a service to count page views, then the alt attribute must be the empty string.

In such cases, the width and height attributes should both be set to zero.

4.8.4.4.13 An image in an email or private document intended for a specific person who is known to be able to view images

This section does not apply to documents that are publicly accessible, or whose target audience is not necessarily personally known to the author, such as documents on a web site, emails sent to public mailing lists, or software documentation.

When an image is included in a private communication (such as an HTML email) aimed at a specific person who is known to be able to view images, the alt attribute may be omitted. However, even in such cases authors are strongly urged to include alternative text (as appropriate according to the kind of image involved, as described in the above entries), so that the email is still usable should the user use a mail client that does not support images, or should the document be forwarded on to other users whose abilities might not include easily seeing images.

4.8.4.4.14 Guidance for markup generators

Markup generators (such as WYSIWYG authoring tools) should, wherever possible, obtain alternative text from their users. However, it is recognized that in many cases, this will not be possible.

For images that are the sole contents of links, markup generators should examine the link target to determine the title of the target, or the URL of the target, and use information obtained in this manner as the alternative text.

For images that have captions, markup generators should use the figure and figcaption elements, or the title attribute, to provide the image's caption.

As a last resort, implementers should either set the alt attribute to the empty string, under the assumption that the image is a purely decorative image that doesn't add any information but is still specific to the surrounding content, or omit the alt attribute altogether, under the assumption that the image is a key part of the content.

Markup generators may specify a generator-unable-to-provide-required-alt attribute on img elements for which they have been unable to obtain alternative text and for which they have therefore omitted the alt attribute. The value of this attribute must be the empty string. Documents containing such attributes are not conforming, but conformance checkers will silently ignore this error.

This is intended to avoid markup generators from being pressured into replacing the error of omitting the alt attribute with the even more egregious error of providing phony alternative text, because state-of-the-art automated conformance checkers cannot distinguish phony alternative text from correct alternative text.

Markup generators should generally avoid using the image's own filename as the alternative text. Similarly, markup generators should avoid generating alternative text from any content that will be equally available to presentation user agents (e.g., web browsers).

This is because once a page is generated, it will typically not be updated, whereas the browsers that later read the page can be updated by the user, therefore the browser is likely to have more up-to-date and finely-tuned heuristics than the markup generator did when generating the page.

4.8.4.4.15 Guidance for conformance checkers

A conformance checker must report the lack of an alt attribute as an error unless one of the conditions listed below applies:

The img element is in a figure element that satisfies the conditions described above.

The img element has a title attribute with a value that is not the empty string (also as described above).

The conformance checker has been configured to assume that the document is an email or document intended for a specific person who is known to be able to view images.

The img element has a (non-conforming) generator-unable-to-provide-required-alt attribute whose value is the empty string. A conformance checker that is not reporting the lack of an alt attribute as an error must also not report the presence of the empty generator-unable-to-provide-required-alt attribute as an error. (This case does not represent a case where the document is conforming, only that the generator could not determine appropriate alternative text — validators are not required to show an error in this case, because such an error might encourage markup generators to include bogus alternative text purely in an attempt to silence validators. Naturally, conformance checkers may report the lack of an alt attribute as an error even in the presence of the generator-unable-to-provide-required-alt attribute; for example, there could be a user option to report all conformance errors even those that might be the more or less inevitable result of using a markup generator.)

← 4.8 Embedded content — Table of Contents — 4.8.5 The iframe element →
