# Source: https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html

Title: HTML Standard

URL Source: https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html

Published Time: Mon, 16 Mar 2026 07:32:48 GMT

Markdown Content:
[![Image 1: WHATWG](https://resources.whatwg.org/logo.svg)](https://whatwg.org/)
Living Standard — Last Updated 16 March 2026

[← 8.9 System state and capabilities](https://html.spec.whatwg.org/multipage/system-state.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [9 Communication →](https://html.spec.whatwg.org/multipage/comms.html)
1.       1.   [8.10 Images](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#images-2)
        1.   [8.10.1 The `ImageData` interface](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#the-imagedata-interface)
        2.   [8.10.2 The `ImageBitmap` interface](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#the-imagebitmap-interface)

    2.   [8.11 Animation frames](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#animation-frames)

### 8.10 Images[](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#images-2)

#### 8.10.1 The `ImageData` interface[](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#the-imagedata-interface)

[ImageData](https://developer.mozilla.org/en-US/docs/Web/API/ImageData "The ImageData interface represents the underlying pixel data of an area of a <canvas> element.")

Support in all current engines.

Firefox 3.5+Safari 3.1+Chrome 1+

* * *

Opera 9+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 10.1+

```
typedef (Uint8ClampedArray or Float16Array) ImageDataArray;

enum ImageDataPixelFormat { "rgba-unorm8", "rgba-float16" };

dictionary ImageDataSettings {
  PredefinedColorSpace colorSpace;
  ImageDataPixelFormat pixelFormat = "rgba-unorm8";
};

[Exposed=(Window,Worker),
 Serializable]
interface ImageData {
  constructor(unsigned long sw, unsigned long sh, optional ImageDataSettings settings = {});
  constructor(ImageDataArray data, unsigned long sw, optional unsigned long sh, optional ImageDataSettings settings = {});

  readonly attribute unsigned long width;
  readonly attribute unsigned long height;
  readonly attribute ImageDataArray data;
  readonly attribute ImageDataPixelFormat pixelFormat;
  readonly attribute PredefinedColorSpace colorSpace;
};
```

An `ImageData` object  represents a rectanglar bitmap with width equal to the 
```
width
```
 attribute and height equal to the `height` attribute. The pixel values of this bitmap are stored in the 
```
data
```
 attribute in left-to-right order, row by row from top to bottom, starting with 0 for the top left pixel, with the order and numerical representation of the color components of each pixel determined by the `pixelFormat` attribute. The color space of the pixel values of the bitmap is determined by the `colorSpace` attribute.

`imageData = new ImageData(sw, sh [, settings])`

[ImageData/ImageData](https://developer.mozilla.org/en-US/docs/Web/API/ImageData/ImageData "The ImageData() constructor returns a newly instantiated ImageData object built from the typed array given and having the specified width and height.")

Support in all current engines.

Firefox 29+Safari 8+Chrome 36+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)14+Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns an `ImageData` object with the given dimensions and the color space indicated by settings. All the pixels in the returned object are [transparent black](https://drafts.csswg.org/css-color/#transparent-black).

Throws an ["`IndexSizeError`"](https://webidl.spec.whatwg.org/#indexsizeerror)`DOMException` if either of the width or height arguments are zero.

`imageData = new ImageData(data, sw [, sh [, settings ] ])`
Returns an `ImageData` object using the data provided in the `ImageDataArray` argument, interpreted using the given dimensions and the color space indicated by settings.

The byte length of the data needs to be a multiple of the number of bytes per pixel times the given width. If the height is provided as well, then the length needs to be exactly the number of bytes per pixel times the width times the height.

Throws an ["`IndexSizeError`"](https://webidl.spec.whatwg.org/#indexsizeerror)`DOMException` if the given data and dimensions can't be interpreted consistently, or if either dimension is zero.

`imageData.width`

[ImageData/width](https://developer.mozilla.org/en-US/docs/Web/API/ImageData/width "The readonly ImageData.width property returns the number of pixels per row in the ImageData object.")

Support in all current engines.

Firefox 3.5+Safari 3.1+Chrome 1+

* * *

Opera 9+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 10.1+

`imageData.height`

[ImageData/height](https://developer.mozilla.org/en-US/docs/Web/API/ImageData/height "The readonly ImageData.height property returns the number of rows in the ImageData object.")

Support in all current engines.

Firefox 3.5+Safari 3.1+Chrome 1+

* * *

Opera 9+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 10.1+

Returns the actual dimensions of the data in the `ImageData` object, in pixels.

`imageData.data`

[ImageData/data](https://developer.mozilla.org/en-US/docs/Web/API/ImageData/data "The readonly ImageData.data property returns a Uint8ClampedArray that contains the ImageData object's pixel data. Data is stored as a one-dimensional array in the RGBA order, with integer values between 0 and 255 (inclusive).")

Support in all current engines.

Firefox 3.5+Safari 3.1+Chrome 1+

* * *

Opera 9+Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 9+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android 37+Samsung Internet?Opera Android 10.1+

Returns the one-dimensional array containing the data in RGBA order, as integers in the range 0 to 255.

`imageData.colorSpace`
Returns the color space of the pixels.

The 
```
new
  ImageData(data, sw, sh, settings)
```
 constructor steps are:

1.   Let bytesPerPixel be 4 if settings["`pixelFormat`"] is "[rgba-unorm8](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#dom-imagedatapixelformat-rgba-unorm8)"; otherwise 8.

2.   Let length be the [buffer source byte length](https://webidl.spec.whatwg.org/#buffersource-byte-length) of data.

3.   If length is not a nonzero integral multiple of bytesPerPixel, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

4.   Let length be length divided by bytesPerPixel.

5.   If length is not an integral multiple of sw, then throw an ["`IndexSizeError`"](https://webidl.spec.whatwg.org/#indexsizeerror)`DOMException`.

At this step, the length is guaranteed to be greater than zero (otherwise the second step above would have aborted the steps), so if sw is zero, this step will throw the exception and return.

6.   Let height be length divided by sw.

7.   If sh was given and its value is not equal to height, then throw an ["`IndexSizeError`"](https://webidl.spec.whatwg.org/#indexsizeerror)`DOMException`.

8.   [Initialize](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#initialize-an-imagedata-object)[this](https://webidl.spec.whatwg.org/#this) given sw, sh, settings, and _[source](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#initialize-imagedata-source)_ set to data.

This step does not set [this](https://webidl.spec.whatwg.org/#this)'s data to a copy of data. It sets it to the actual `ImageDataArray` object passed as data.

[ImageData/colorSpace](https://developer.mozilla.org/en-US/docs/Web/API/ImageData/colorSpace "The read-only ImageData.colorSpace property is a string indicating the color space of the image data.")

Firefox No Safari 15.2+Chrome 92+

* * *

Opera?Edge 92+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

To initialize an `ImageData` object imageData, given a positive integer number of pixels per row pixelsPerRow, a positive integer number of rows rows, an `ImageDataSettings`settings, an optional `ImageDataArray`source, and an optional `PredefinedColorSpace`defaultColorSpace:

1.   If source was given:

    1.   If settings["`pixelFormat`"] equals "[rgba-unorm8](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#dom-imagedatapixelformat-rgba-unorm8)" and source is not a `Uint8ClampedArray`, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

    2.   If settings["`pixelFormat`"] is "[rgba-float16](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#dom-imagedatapixelformat-rgba-float16)" and source is not a `Float16Array`, then throw an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

    3.   Initialize the `data` attribute of imageData to source.

2.   Otherwise (source was not given):

    1.   If settings["`pixelFormat`"] is "[rgba-unorm8](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#dom-imagedatapixelformat-rgba-unorm8)", then initialize the `data` attribute of imageData to a new `Uint8ClampedArray` object. The `Uint8ClampedArray` object must use a new `ArrayBuffer` for its storage, and must have a zero byte offset and byte length equal to the length of its storage, in bytes. The storage `ArrayBuffer` must have a length of 4 × rows × pixelsPerRow bytes.

    2.   Otherwise, if settings["`pixelFormat`"] is "[rgba-float16](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#dom-imagedatapixelformat-rgba-unorm8)", then initialize the `data` attribute of imageData to a new `Float16Array` object. The `Float16Array` object must use a new `ArrayBuffer` for its storage, and must have a zero byte offset and byte length equal to the length of its storage, in bytes. The storage `ArrayBuffer` must have a length of 8 × rows × pixelsPerRow bytes.

    3.   If the storage `ArrayBuffer` could not be allocated, then rethrow the `RangeError` thrown by JavaScript, and return.

3.   Initialize the `width` attribute of imageData to pixelsPerRow.

4.   Initialize the `height` attribute of imageData to rows.

5.   Initialize the `pixelFormat` attribute of imageData to settings["`pixelFormat`"].

6.   If settings["`colorSpace`"] [exists](https://infra.spec.whatwg.org/#map-exists), then initialize the `colorSpace` attribute of imageData to settings["`colorSpace`"].

7.   Otherwise, if defaultColorSpace was given, then initialize the `colorSpace` attribute of imageData to defaultColorSpace.

8.   Otherwise, initialize the `colorSpace` attribute of imageData to "[srgb](https://html.spec.whatwg.org/multipage/canvas.html#dom-predefinedcolorspace-srgb)".

`ImageData` objects are [serializable objects](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects). Their [serialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#serialization-steps), given value and serialized, are:

1.   Set serialized.[[Data]] to the [sub-serialization](https://html.spec.whatwg.org/multipage/structured-data.html#sub-serialization) of the value of value's `data` attribute.

2.   Set serialized.[[Width]] to the value of value's `width` attribute.

3.   Set serialized.[[Height]] to the value of value's `height` attribute.

4.   Set serialized.[[ColorSpace]] to the value of value's `colorSpace` attribute.

5.   Set serialized.[[PixelFormat]] to the value of value's `pixelFormat` attribute.

Their [deserialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#deserialization-steps), given serialized, value, and targetRealm, are:

1.   Initialize value's `data` attribute to the [sub-deserialization](https://html.spec.whatwg.org/multipage/structured-data.html#sub-deserialization) of serialized.[[Data]].

2.   Initialize value's `width` attribute to serialized.[[Width]].

3.   Initialize value's `height` attribute to serialized.[[Height]].

4.   Initialize value's `colorSpace` attribute to serialized.[[ColorSpace]].

5.   Initialize value's `pixelFormat` attribute to serialized.[[PixelFormat]].

The `ImageDataPixelFormat` enumeration is used to specify type of the `data` attribute of an `ImageData` and the arrangement and numerical representation of the color components for each pixel.

The "`rgba-unorm8`" value indicates that the `data` attribute of an `ImageData` must be of type [Uint8ClampedArray](https://webidl.spec.whatwg.org/#idl-Uint8ClampedArray). The color components of each pixel must be stored in four sequential elements in the order of red, green, blue, and then alpha. Each element represents the 8-bit unsigned normalized value for that component.

The "`rgba-float16`" value indicates that the `data` attribute of an `ImageData` must be of type [Float16Array](https://webidl.spec.whatwg.org/#idl-Float16Array). The color components of each pixel must be stored in four sequential elements in the order of red, green, blue, and then alpha. Each element represents the value for that component.

#### 8.10.2 The `ImageBitmap` interface[](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#the-imagebitmap-interface)

[ImageBitmap](https://developer.mozilla.org/en-US/docs/Web/API/ImageBitmap "The ImageBitmap interface represents a bitmap image which can be drawn to a <canvas> without undue latency. It can be created from a variety of source objects using the createImageBitmap() factory method. ImageBitmap provides an asynchronous and resource efficient pathway to prepare textures for rendering in WebGL.")

Support in all current engines.

Firefox 42+Safari 15+Chrome 50+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

```
[Exposed=(Window,Worker), Serializable, Transferable]
interface ImageBitmap {
  readonly attribute unsigned long width;
  readonly attribute unsigned long height;
  undefined close();
};

typedef (CanvasImageSource or
         Blob or
         ImageData) ImageBitmapSource;

enum ImageOrientation { "from-image", "flipY" };
enum PremultiplyAlpha { "none", "premultiply", "default" };
enum ColorSpaceConversion { "none", "default" };
enum ResizeQuality { "pixelated", "low", "medium", "high" };

dictionary ImageBitmapOptions {
  ImageOrientation imageOrientation = "from-image";
  PremultiplyAlpha premultiplyAlpha = "default";
  ColorSpaceConversion colorSpaceConversion = "default";
  [EnforceRange] unsigned long resizeWidth;
  [EnforceRange] unsigned long resizeHeight;
  ResizeQuality resizeQuality = "low";
};
```

An `ImageBitmap` object represents a bitmap image that can be painted to a canvas without undue latency.

The exact judgement of what is undue latency of this is left up to the implementer, but in general if making use of the bitmap requires network I/O, or even local disk I/O, then the latency is probably undue; whereas if it only requires a blocking read from a GPU or system RAM, the latency is probably acceptable.

`promise = self.createImageBitmap(image [, options ])`

[createImageBitmap](https://developer.mozilla.org/en-US/docs/Web/API/createImageBitmap "The createImageBitmap() method creates a bitmap from a given source, optionally cropped to contain only a portion of that source. The method exists on the global scope in both windows and workers. It accepts a variety of different image sources, and returns a Promise which resolves to an ImageBitmap.")

Support in all current engines.

Firefox 42+Safari 15+Chrome 50+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

`promise = self.createImageBitmap(image, sx, sy, sw, sh [, options ])`
Takes image, which can be an `img` element, an [SVG `image`](https://svgwg.org/svg2-draft/embedded.html#ImageElement) element, a `video` element, a `canvas` element, a `Blob` object, an `ImageData` object, or another `ImageBitmap` object, and returns a promise that is resolved when a new `ImageBitmap` is created.

If no `ImageBitmap` object can be constructed, for example because the provided image data is not actually an image, then the promise is rejected instead.

If sx, sy, sw, and sh arguments are provided, the source image is cropped to the given pixels, with any pixels missing in the original replaced by [transparent black](https://drafts.csswg.org/css-color/#transparent-black). These coordinates are in the source image's pixel coordinate space, _not_ in [CSS pixels](https://drafts.csswg.org/css-values/#px).

If options is provided, the `ImageBitmap` object's bitmap data is modified according to options. For example, if the `premultiplyAlpha` option is set to "`premultiply`", the [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data)'s non-alpha color components are [premultiplied by the alpha component](https://html.spec.whatwg.org/multipage/canvas.html#concept-premultiplied-alpha).

Rejects the promise with an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` if the source image is not in a valid state (e.g., an `img` element that hasn't loaded successfully, an `ImageBitmap` object whose [[[Detached]]](https://html.spec.whatwg.org/multipage/structured-data.html#detached) internal slot value is true, an `ImageData` object whose `data` attribute value's [[ViewedArrayBuffer]] internal slot is detached, or a `Blob` whose data cannot be interpreted as a bitmap image).

Rejects the promise with a ["`SecurityError`"](https://webidl.spec.whatwg.org/#securityerror)`DOMException` if the script is not allowed to access the image data of the source image (e.g. a `video` that is [CORS-cross-origin](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#cors-cross-origin), or a `canvas` being drawn on by a script in a worker from another [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin)).

`imageBitmap.close()`

[ImageBitmap/close](https://developer.mozilla.org/en-US/docs/Web/API/ImageBitmap/close "The ImageBitmap.close() method disposes of all graphical resources associated with an ImageBitmap.")

Support in all current engines.

Firefox 46+Safari 15+Chrome 52+

* * *

Opera 37+Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android 37+

Releases imageBitmap's underlying [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data).

`imageBitmap.width`

[ImageBitmap/width](https://developer.mozilla.org/en-US/docs/Web/API/ImageBitmap/width "The read-only ImageBitmap.width property returns the ImageBitmap object's width in CSS pixels.")

Support in all current engines.

Firefox 42+Safari 15+Chrome 50+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns the [natural width](https://drafts.csswg.org/css-images/#natural-width) of the image, in [CSS pixels](https://drafts.csswg.org/css-values/#px).

`imageBitmap.height`

[ImageBitmap/height](https://developer.mozilla.org/en-US/docs/Web/API/ImageBitmap/height "The read-only ImageBitmap.height property returns the ImageBitmap object's height in CSS pixels.")

Support in all current engines.

Firefox 42+Safari 15+Chrome 50+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)?Internet Explorer No

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

Returns the [natural height](https://drafts.csswg.org/css-images/#natural-height) of the image, in [CSS pixels](https://drafts.csswg.org/css-values/#px).

An `ImageBitmap` object whose [[[Detached]]](https://html.spec.whatwg.org/multipage/structured-data.html#detached) internal slot value is false always has associated bitmap data, with a width and a height. However, it is possible for this data to be corrupted. If an `ImageBitmap` object's media data can be decoded without errors, it is said to be fully decodable.

An `ImageBitmap` object's bitmap has an [origin-clean](https://html.spec.whatwg.org/multipage/canvas.html#concept-canvas-origin-clean) flag, which indicates whether the bitmap is tainted by content from a different [origin](https://html.spec.whatwg.org/multipage/browsers.html#concept-origin). The flag is initially set to true and may be changed to false by the steps of `createImageBitmap()`.

* * *

`ImageBitmap` objects are [serializable objects](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects) and [transferable objects](https://html.spec.whatwg.org/multipage/structured-data.html#transferable-objects).

Their [deserialization steps](https://html.spec.whatwg.org/multipage/structured-data.html#deserialization-steps), given serialized, value, and targetRealm, are:

1.   Set value's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) to serialized.[[BitmapData]].

* * *

The [createImageBitmap](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#dom-createimagebitmap) method uses the bitmap task source to settle its returned Promise.

The 
```
createImageBitmap(image,
  options)
```
 and 
```
createImageBitmap(image,
  sx, sy, sw, sh, options)
```
 methods, when invoked, must run these steps:

1.   If either sw or sh is given and is 0, then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) a `RangeError`.

2.   If either options's `resizeWidth` or options's `resizeHeight` is present and is 0, then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

3.   [Check the usability of the image argument](https://html.spec.whatwg.org/multipage/canvas.html#check-the-usability-of-the-image-argument). If this throws an exception or returns _bad_, then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

4.   Let promise be a new promise.

5.   Let imageBitmap be a new `ImageBitmap` object.

6.   Switch on image:

`img`[SVG `image`](https://svgwg.org/svg2-draft/embedded.html#ImageElement)
    1.   If image's media data has no [natural dimensions](https://drafts.csswg.org/css-images/#natural-dimensions) (e.g., it's a vector graphic with no specified content size) and either options's `resizeWidth` or options's `resizeHeight` is not present, then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

    2.   If image's media data has no [natural dimensions](https://drafts.csswg.org/css-images/#natural-dimensions) (e.g., it's a vector graphic with no specified content size), it should be rendered to a bitmap of the size specified by the `resizeWidth` and the `resizeHeight` options.

    3.   Set imageBitmap's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) to a copy of image's media data, [cropped to the source rectangle with formatting](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#cropped-to-the-source-rectangle-with-formatting). If this is an animated image, imageBitmap's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) must only be taken from the default image of the animation (the one that the format defines is to be used when animation is not supported or is disabled), or, if there is no such image, the first frame of the animation.

    4.   If image[is not origin-clean](https://html.spec.whatwg.org/multipage/canvas.html#the-image-argument-is-not-origin-clean), then set the [origin-clean](https://html.spec.whatwg.org/multipage/canvas.html#concept-canvas-origin-clean) flag of imageBitmap's bitmap to false.

    5.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task), using the [bitmap task source](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#bitmap-task-source), to resolve promise with imageBitmap.

`video`
    1.   If image's `networkState` attribute is `NETWORK_EMPTY`, then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

    2.   Set imageBitmap's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) to a copy of the frame at the [current playback position](https://html.spec.whatwg.org/multipage/media.html#current-playback-position), at the [media resource](https://html.spec.whatwg.org/multipage/media.html#media-resource)'s [natural width](https://html.spec.whatwg.org/multipage/media.html#concept-video-intrinsic-width) and [natural height](https://html.spec.whatwg.org/multipage/media.html#concept-video-intrinsic-height) (i.e., after any aspect-ratio correction has been applied), [cropped to the source rectangle with formatting](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#cropped-to-the-source-rectangle-with-formatting).

    3.   If image[is not origin-clean](https://html.spec.whatwg.org/multipage/canvas.html#the-image-argument-is-not-origin-clean), then set the [origin-clean](https://html.spec.whatwg.org/multipage/canvas.html#concept-canvas-origin-clean) flag of imageBitmap's bitmap to false.

    4.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task), using the [bitmap task source](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#bitmap-task-source), to resolve promise with imageBitmap.

`canvas`
    1.   Set imageBitmap's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) to a copy of image's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data), [cropped to the source rectangle with formatting](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#cropped-to-the-source-rectangle-with-formatting).

    2.   Set the [origin-clean](https://html.spec.whatwg.org/multipage/canvas.html#concept-canvas-origin-clean) flag of the imageBitmap's bitmap to the same value as the [origin-clean](https://html.spec.whatwg.org/multipage/canvas.html#concept-canvas-origin-clean) flag of image's bitmap.

    3.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task), using the [bitmap task source](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#bitmap-task-source), to resolve promise with imageBitmap.

`Blob`
Run these steps [in parallel](https://html.spec.whatwg.org/multipage/infrastructure.html#in-parallel):

    1.   Let imageData be the result of reading image's data. If an [error occurs during reading of the object](https://html.spec.whatwg.org/multipage/infrastructure.html#file-error-read), then [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task), using the [bitmap task source](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#bitmap-task-source), to reject promise with an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` and abort these steps.

    2.   Apply the [image sniffing rules](https://mimesniff.spec.whatwg.org/#rules-for-sniffing-images-specifically) to determine the file format of imageData, with MIME type of image (as given by image's `type` attribute) giving the official type.

    3.   If imageData is not in a supported image file format (e.g., it's not an image at all), or if imageData is corrupted in some fatal way such that the image dimensions cannot be obtained (e.g., a vector graphic with no natural size), then [queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task), using the [bitmap task source](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#bitmap-task-source), to reject promise with an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException` and abort these steps.

    4.   Set imageBitmap's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) to imageData, [cropped to the source rectangle with formatting](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#cropped-to-the-source-rectangle-with-formatting). If this is an animated image, imageBitmap's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) must only be taken from the default image of the animation (the one that the format defines is to be used when animation is not supported or is disabled), or, if there is no such image, the first frame of the animation.

    5.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task), using the [bitmap task source](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#bitmap-task-source), to resolve promise with imageBitmap.

`ImageData`
    1.   Let buffer be image's `data` attribute value's [[ViewedArrayBuffer]] internal slot.

    2.   If [IsDetachedBuffer](https://tc39.es/ecma262/#sec-isdetachedbuffer)(buffer) is true, then return [a promise rejected with](https://webidl.spec.whatwg.org/#a-promise-rejected-with) an ["`InvalidStateError`"](https://webidl.spec.whatwg.org/#invalidstateerror)`DOMException`.

    3.   Set imageBitmap's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) to image's image data, [cropped to the source rectangle with formatting](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#cropped-to-the-source-rectangle-with-formatting).

    4.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task), using the [bitmap task source](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#bitmap-task-source), to resolve promise with imageBitmap.

`ImageBitmap`
    1.   Set imageBitmap's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) to a copy of image's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data), [cropped to the source rectangle with formatting](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#cropped-to-the-source-rectangle-with-formatting).

    2.   Set the [origin-clean](https://html.spec.whatwg.org/multipage/canvas.html#concept-canvas-origin-clean) flag of imageBitmap's bitmap to the same value as the [origin-clean](https://html.spec.whatwg.org/multipage/canvas.html#concept-canvas-origin-clean) flag of image's bitmap.

    3.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task), using the [bitmap task source](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#bitmap-task-source), to resolve promise with imageBitmap.

`VideoFrame`
    1.   Set imageBitmap's [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) to a copy of image's visible pixel data, [cropped to the source rectangle with formatting](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#cropped-to-the-source-rectangle-with-formatting).

    2.   [Queue a global task](https://html.spec.whatwg.org/multipage/webappapis.html#queue-a-global-task), using the [bitmap task source](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#bitmap-task-source), to resolve promise with imageBitmap.

7.   Return promise.

When the steps above require that the user agent crop bitmap data to the source rectangle with formatting, the user agent must run the following steps:

1.   Let input be the [bitmap data](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-imagebitmap-bitmap-data) being transformed.

2.   If sx, sy, sw and sh are specified, let sourceRectangle be a rectangle whose corners are the four points (sx, sy), (sx+sw, sy), (sx+sw, sy+sh), (sx, sy+sh). Otherwise, let sourceRectangle be a rectangle whose corners are the four points (0, 0), (width of input, 0), (width of input, height of input), (0, height of input).

If either sw or sh are negative, then the top-left corner of this rectangle will be to the left or above the (sx, sy) point.

3.   Let outputWidth be determined as follows:

If the `resizeWidth` member of options is specified the value of the `resizeWidth` member of options If the `resizeWidth` member of options is not specified, but the `resizeHeight` member is specified the width of sourceRectangle, times the value of the `resizeHeight` member of options, divided by the height of sourceRectangle, rounded up to the nearest integer If neither `resizeWidth` nor `resizeHeight` are specified the width of sourceRectangle
4.   Let outputHeight be determined as follows:

If the `resizeHeight` member of options is specified the value of the `resizeHeight` member of options If the `resizeHeight` member of options is not specified, but the `resizeWidth` member is specified the height of sourceRectangle, times the value of the `resizeWidth` member of options, divided by the width of sourceRectangle, rounded up to the nearest integer If neither `resizeWidth` nor `resizeHeight` are specified the height of sourceRectangle
5.   Place input on an infinite [transparent black](https://drafts.csswg.org/css-color/#transparent-black) grid plane, positioned so that its top left corner is at the origin of the plane, with the x-coordinate increasing to the right, and the y-coordinate increasing down, and with each pixel in the input image data occupying a cell on the plane's grid.

6.   Let output be the rectangle on the plane denoted by sourceRectangle.

7.   Scale output to the size specified by outputWidth and outputHeight. The user agent should use the value of the `resizeQuality` option to guide the choice of scaling algorithm.

8.   If the value of the `imageOrientation` member of options is "`flipY`", output must be flipped vertically, disregarding any image orientation metadata of the source (such as EXIF metadata), if any. [[EXIF]](https://html.spec.whatwg.org/multipage/references.html#refsEXIF)

If the value is "`from-image`", no extra step is needed.

There used to be a "`none`" enum value. It was renamed to "`from-image`". In the future, "`none`" will be added back with a different meaning.

9.   If image is an `img` element or a `Blob` object, let val be the value of the `colorSpaceConversion` member of options, and then run these substeps:

    1.   If val is "`default`", the color space conversion behavior is implementation-specific, and should be chosen according to the default color space that the implementation uses for drawing images onto the canvas.

    2.   If val is "`none`", output must be decoded without performing any color space conversions. This means that the image decoding algorithm must ignore color profile metadata embedded in the source data as well as the display device color profile.

10.   Let val be the value of `premultiplyAlpha` member of options, and then run these substeps:

    1.   If val is "`default`", the alpha premultiplication behavior is implementation-specific, and should be chosen according to implementation deems optimal for drawing images onto the canvas.

    2.   If val is "`premultiply`", the output that is not premultiplied by alpha must have its color components [multiplied by alpha](https://html.spec.whatwg.org/multipage/canvas.html#convert-to-premultiplied) and that is premultiplied by alpha must be left untouched.

    3.   If val is "`none`", the output that is not premultiplied by alpha must be left untouched and that is premultiplied by alpha must have its color components [divided by alpha](https://html.spec.whatwg.org/multipage/canvas.html#convert-from-premultiplied).

11.   Return output.

The `ResizeQuality` enumeration is used to express a preference for the interpolation quality to use when scaling images.

The "`pixelated`" value indicates a preference for scaling the image to preserve the pixelation of the original as much as possible, with minor smoothing as necessary to avoid distorting the image when the target size is not a clean multiple of the original.

To implement "`pixelated`", for each axis independently, first determine the integer multiple of its natural size that puts it closest to the target size and is greater than zero. Scale it to this integer-multiple-size using nearest neighbor, then scale it the rest of the way to the target size using bilinear interpolation.

The "`low`" value indicates a preference for a low level of image interpolation quality. Low-quality image interpolation may be more computationally efficient than higher settings.

The "`medium`" value indicates a preference for a medium level of image interpolation quality.

The "`high`" value indicates a preference for a high level of image interpolation quality. High-quality image interpolation may be more computationally expensive than lower settings.

Bilinear scaling is an example of a relatively fast, lower-quality image-smoothing algorithm. Bicubic or Lanczos scaling are examples of image-scaling algorithms that produce higher-quality output. This specification does not mandate that specific interpolation algorithms be used, except for "`pixelated`" as described above.

Using this API, a sprite sheet can be precut and prepared:

```
var sprites = {};
function loadMySprites() {
  var image = new Image();
  image.src = 'mysprites.png';
  var resolver;
  var promise = new Promise(function (arg) { resolver = arg });
  image.onload = function () {
    resolver(Promise.all([
      createImageBitmap(image,  0,  0, 40, 40).then(function (image) { sprites.person = image }),
      createImageBitmap(image, 40,  0, 40, 40).then(function (image) { sprites.grass  = image }),
      createImageBitmap(image, 80,  0, 40, 40).then(function (image) { sprites.tree   = image }),
      createImageBitmap(image,  0, 40, 40, 40).then(function (image) { sprites.hut    = image }),
      createImageBitmap(image, 40, 40, 40, 40).then(function (image) { sprites.apple  = image }),
      createImageBitmap(image, 80, 40, 40, 40).then(function (image) { sprites.snake  = image })
    ]));
  };
  return promise;
}

function runDemo() {
  var canvas = document.querySelector('canvas#demo');
  var context = canvas.getContext('2d');
  context.drawImage(sprites.tree, 30, 10);
  context.drawImage(sprites.snake, 70, 10);
}

loadMySprites().then(runDemo);
```

### 8.11 Animation frames[](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#animation-frames)

Some objects include the `AnimationFrameProvider` interface mixin.

```
callback FrameRequestCallback = undefined (DOMHighResTimeStamp time);

interface mixin AnimationFrameProvider {
  unsigned long requestAnimationFrame(FrameRequestCallback callback);
  undefined cancelAnimationFrame(unsigned long handle);
};
Window includes AnimationFrameProvider;
DedicatedWorkerGlobalScope includes AnimationFrameProvider;
```

Each [target object](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-animationframeprovider-target-object) has a map of animation frame callbacks, which is an [ordered map](https://infra.spec.whatwg.org/#ordered-map) that must be initially empty, and an animation frame callback identifier, which is a number that must initially be zero.

* * *

[Window/requestAnimationFrame](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame "The window.requestAnimationFrame() method tells the browser that you wish to perform an animation and requests that the browser calls a specified function to update an animation right before the next repaint. The method takes a callback as an argument to be invoked before the repaint.")

Support in all current engines.

Firefox 23+Safari 7+Chrome 24+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android 23+Safari iOS?Chrome Android?WebView Android 4.4+Samsung Internet?Opera Android?

The `requestAnimationFrame(callback)` method steps are:

1.   If [this](https://webidl.spec.whatwg.org/#this) is not [supported](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-animationframeprovider-supported), then throw a ["`NotSupportedError`"](https://webidl.spec.whatwg.org/#notsupportederror)`DOMException`.

2.   Let target be [this](https://webidl.spec.whatwg.org/#this)'s [target object](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-animationframeprovider-target-object).

3.   Increment target's [animation frame callback identifier](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#animation-frame-callback-identifier) by one, and let handle be the result.

4.   Let callbacks be target's [map of animation frame callbacks](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#list-of-animation-frame-callbacks).

5.   [Set](https://infra.spec.whatwg.org/#map-set)callbacks[handle] to callback.

6.   Return handle.

[Window/cancelAnimationFrame](https://developer.mozilla.org/en-US/docs/Web/API/Window/cancelAnimationFrame "The window.cancelAnimationFrame() method cancels an animation frame request previously scheduled through a call to window.requestAnimationFrame().")

Support in all current engines.

Firefox 23+Safari 7+Chrome 24+

* * *

Opera?Edge 79+

* * *

Edge (Legacy)12+Internet Explorer 10+

* * *

Firefox Android?Safari iOS?Chrome Android?WebView Android?Samsung Internet?Opera Android?

To run the animation frame callbacks for a [target object](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#concept-animationframeprovider-target-object)target with a timestamp now:

1.   Let callbacks be target's [map of animation frame callbacks](https://html.spec.whatwg.org/multipage/imagebitmap-and-animations.html#list-of-animation-frame-callbacks).

2.   Let callbackHandles be the result of [getting the keys](https://infra.spec.whatwg.org/#map-getting-the-keys) of callbacks.

3.   [For each](https://infra.spec.whatwg.org/#list-iterate)handle in callbackHandles, if handle[exists](https://infra.spec.whatwg.org/#map-exists) in callbacks:

    1.   Let callback be callbacks[handle].

    2.   [Remove](https://infra.spec.whatwg.org/#map-remove)callbacks[handle].

    3.   [Invoke](https://webidl.spec.whatwg.org/#invoke-a-callback-function)callback with « now » and "`report`".

Inside workers, `requestAnimationFrame()` can be used together with an `OffscreenCanvas` transferred from a `canvas` element. First, in the document, transfer control to the worker:

```
const offscreenCanvas = document.getElementById("c").transferControlToOffscreen();
worker.postMessage(offscreenCanvas, [offscreenCanvas]);
```

Then, in the worker, the following code will draw a rectangle moving from left to right:

```
let ctx, pos = 0;
function draw(dt) {
  ctx.clearRect(0, 0, 100, 100);
  ctx.fillRect(pos, 0, 10, 10);
  pos += 10 * dt;
  requestAnimationFrame(draw);
}

self.onmessage = function(ev) {
  const transferredCanvas = ev.data;
  ctx = transferredCanvas.getContext("2d");
  draw();
};
```

[← 8.9 System state and capabilities](https://html.spec.whatwg.org/multipage/system-state.html) — [Table of Contents](https://html.spec.whatwg.org/multipage/) — [9 Communication →](https://html.spec.whatwg.org/multipage/comms.html)
