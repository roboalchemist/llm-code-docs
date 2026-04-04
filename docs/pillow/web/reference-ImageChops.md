# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageChops.html
# Path: reference/ImageChops.html

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto
light/dark, in dark mode Skip to content

[Pillow (PIL Fork) 12.1.0.dev0 documentation](../index.html)

[ ![Light Logo](../_static/pillow-logo-dark-text.png) ![Dark
Logo](../_static/pillow-logo.png) Pillow (PIL Fork) 12.1.0.dev0 documentation
](../index.html)

  * [Installation](../installation/index.html)
    * [Basic installation](../installation/basic-installation.html)
    * [Python support](../installation/python-support.html)
    * [Platform support](../installation/platform-support.html)
    * [Building from source](../installation/building-from-source.html)
    * [Old versions](../installation/building-from-source.html#old-versions)
  * [Handbook](../handbook/index.html)
    * [Overview](../handbook/overview.html)
    * [Tutorial](../handbook/tutorial.html)
    * [Concepts](../handbook/concepts.html)
    * [Appendices](../handbook/appendices.html)
      * [Image file formats](../handbook/image-file-formats.html)
      * [Text anchors](../handbook/text-anchors.html)
      * [Third-party plugins](../handbook/third-party-plugins.html)
      * [Writing your own image plugin](../handbook/writing-your-own-image-plugin.html)
      * [Decoders](../handbook/writing-your-own-image-plugin.html#decoders)
      * [Writing your own file codec in C](../handbook/writing-your-own-image-plugin.html#writing-your-own-file-codec-in-c)
      * [Writing your own file codec in Python](../handbook/writing-your-own-image-plugin.html#writing-your-own-file-codec-in-python)
  * [Reference](index.html)
    * [`Image` module](Image.html)
    * `ImageChops` (“channel operations”) module
    * [`ImageCms` module](ImageCms.html)
    * [`ImageColor` module](ImageColor.html)
    * [`ImageDraw` module](ImageDraw.html)
    * [`ImageEnhance` module](ImageEnhance.html)
    * [`ImageFile` module](ImageFile.html)
    * [`ImageFilter` module](ImageFilter.html)
    * [`ImageFont` module](ImageFont.html)
    * [`ImageGrab` module](ImageGrab.html)
    * [`ImageMath` module](ImageMath.html)
    * [`ImageMorph` module](ImageMorph.html)
    * [`ImageOps` module](ImageOps.html)
    * [`ImagePalette` module](ImagePalette.html)
    * [`ImagePath` module](ImagePath.html)
    * [`ImageQt` module](ImageQt.html)
    * [`ImageSequence` module](ImageSequence.html)
    * [`ImageShow` module](ImageShow.html)
    * [`ImageStat` module](ImageStat.html)
    * [`ImageText` module](ImageText.html)
    * [`ImageTk` module](ImageTk.html)
    * [`ImageTransform` module](ImageTransform.html)
    * [`ImageWin` module (Windows-only)](ImageWin.html)
    * [`ExifTags` module](ExifTags.html)
    * [`TiffTags` module](TiffTags.html)
    * [`JpegPresets` module](JpegPresets.html)
    * [`PSDraw` module](PSDraw.html)
    * [`PixelAccess` class](PixelAccess.html)
    * [`features` module](features.html)
    * [PIL package (autodoc of remaining modules)](../PIL.html)
    * [Plugin reference](plugins.html)
    * [Internal reference](internal_design.html)
      * [File handling in Pillow](open_files.html)
      * [Limits](limits.html)
      * [Block allocator](block_allocator.html)
      * [Internal modules](internal_modules.html)
      * [C extension debugging on Linux, with GBD/Valgrind](c_extension_debugging.html)
      * [Arrow support](arrow_support.html)
  * [Porting](../porting.html)
  * [About](../about.html)
  * [Release notes](../releasenotes/index.html)
    * [Versioning](../releasenotes/versioning.html)
    * [12.1.0 (unreleased)](../releasenotes/12.1.0.html)
    * [12.0.0 (2025-10-15)](../releasenotes/12.0.0.html)
    * [11.3.0 (2025-07-01)](../releasenotes/11.3.0.html)
    * [11.2.1 (2025-04-12)](../releasenotes/11.2.1.html)
    * [11.1.0 (2025-01-02)](../releasenotes/11.1.0.html)
    * [11.0.0 (2024-10-15)](../releasenotes/11.0.0.html)
    * [10.4.0 (2024-07-01)](../releasenotes/10.4.0.html)
    * [10.3.0 (2024-04-01)](../releasenotes/10.3.0.html)
    * [10.2.0 (2024-01-02)](../releasenotes/10.2.0.html)
    * [10.1.0 (2023-10-15)](../releasenotes/10.1.0.html)
    * [10.0.1 (2023-09-15)](../releasenotes/10.0.1.html)
    * [10.0.0 (2023-07-01)](../releasenotes/10.0.0.html)
    * [9.5.0 (2023-04-01)](../releasenotes/9.5.0.html)
    * [9.4.0 (2023-01-02)](../releasenotes/9.4.0.html)
    * [9.3.0 (2022-10-29)](../releasenotes/9.3.0.html)
    * [9.2.0 (2022-07-01)](../releasenotes/9.2.0.html)
    * [9.1.1 (2022-05-17)](../releasenotes/9.1.1.html)
    * [9.1.0 (2022-04-01)](../releasenotes/9.1.0.html)
    * [9.0.1 (2022-02-03)](../releasenotes/9.0.1.html)
    * [9.0.0 (2022-01-02)](../releasenotes/9.0.0.html)
    * [8.4.0 (2021-10-15)](../releasenotes/8.4.0.html)
    * [8.3.2 (2021-09-02)](../releasenotes/8.3.2.html)
    * [8.3.1 (2021-07-06)](../releasenotes/8.3.1.html)
    * [8.3.0 (2021-07-01)](../releasenotes/8.3.0.html)
    * [8.2.0 (2021-04-01)](../releasenotes/8.2.0.html)
    * [8.1.2 (2021-03-06)](../releasenotes/8.1.2.html)
    * [8.1.1 (2021-03-01)](../releasenotes/8.1.1.html)
    * [8.1.0 (2021-01-02)](../releasenotes/8.1.0.html)
    * [8.0.1 (2020-10-22)](../releasenotes/8.0.1.html)
    * [8.0.0 (2020-10-14)](../releasenotes/8.0.0.html)
    * [7.2.0 (2020-06-30)](../releasenotes/7.2.0.html)
    * [7.1.2 (2020-04-25)](../releasenotes/7.1.2.html)
    * [7.1.1 (2020-04-02)](../releasenotes/7.1.1.html)
    * [7.1.0 (2020-04-01)](../releasenotes/7.1.0.html)
    * [7.0.0 (2020-01-02)](../releasenotes/7.0.0.html)
    * [6.2.2 (2020-01-02)](../releasenotes/6.2.2.html)
    * [6.2.1 (2019-10-20)](../releasenotes/6.2.1.html)
    * [6.2.0 (2019-10-01)](../releasenotes/6.2.0.html)
    * [6.1.0 (2019-07-02)](../releasenotes/6.1.0.html)
    * [6.0.0 (2019-04-02)](../releasenotes/6.0.0.html)
    * [5.4.1 (2019-01-06)](../releasenotes/5.4.1.html)
    * [5.4.0 (2019-01-01)](../releasenotes/5.4.0.html)
    * [5.3.0 (2018-10-01)](../releasenotes/5.3.0.html)
    * [5.2.0 (2018-07-01)](../releasenotes/5.2.0.html)
    * [5.1.0 (2018-04-02)](../releasenotes/5.1.0.html)
    * [5.0.0 (2018-01-01)](../releasenotes/5.0.0.html)
    * [4.3.0 (2017-10-02)](../releasenotes/4.3.0.html)
    * [4.2.1 (2017-07-06)](../releasenotes/4.2.1.html)
    * [4.2.0 (2017-07-01)](../releasenotes/4.2.0.html)
    * [4.1.1 (2017-04-28)](../releasenotes/4.1.1.html)
    * [4.1.0 (2017-04-03)](../releasenotes/4.1.0.html)
    * [4.0.0 (2017-01-01)](../releasenotes/4.0.0.html)
    * [3.4.0 (2016-10-03)](../releasenotes/3.4.0.html)
    * [3.3.2 (2016-09-29)](../releasenotes/3.3.2.html)
    * [3.3.0 (2016-07-01)](../releasenotes/3.3.0.html)
    * [3.2.0 (2016-04-01)](../releasenotes/3.2.0.html)
    * [3.1.2 (2016-04-01)](../releasenotes/3.1.2.html)
    * [3.1.1 (2016-02-04)](../releasenotes/3.1.1.html)
    * [3.1.0 (2016-01-04)](../releasenotes/3.1.0.html)
    * [3.0.0 (2015-10-01)](../releasenotes/3.0.0.html)
    * [2.8.0 (2015-04-01)](../releasenotes/2.8.0.html)
    * [2.7.0 (2014-12-31)](../releasenotes/2.7.0.html)
    * [2.6.0 (2014-10-01)](../releasenotes/2.6.0.html)
    * [2.5.2 (2014-08-12)](../releasenotes/2.5.2.html)
    * [2.3.2 (2014-08-12)](../releasenotes/2.3.2.html)
    * [2.3.1 (2014-03-14)](../releasenotes/2.3.1.html)
  * [Deprecations and removals](../deprecations.html)

Back to top

[ View this page ](../_sources/reference/ImageChops.rst.txt "View this page")

# `ImageChops` (“channel operations”) module¶

The `ImageChops` module contains a number of arithmetical image operations,
called channel operations (“chops”). These can be used for various purposes,
including special effects, image compositions, algorithmic painting, and more.

For more pre-made operations, see [`ImageOps`](ImageOps.html#module-
PIL.ImageOps "PIL.ImageOps").

At this time, most channel operations are only implemented for 8-bit images
(e.g. “L” and “RGB”).

## Functions¶

Most channel operations take one or two image arguments and returns a new
image. Unless otherwise noted, the result of a channel operation is always
clipped to the range 0 to MAX (which is 255 for all modes supported by the
operations in this module).

PIL.ImageChops.add(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _scale :
[float](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.14\)") = 1.0_, _offset :
[float](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.14\)") = 0_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#add)¶

    

Adds two images, dividing the result by scale and adding the offset. If
omitted, scale defaults to 1.0, and offset to 0.0.

    
    
    out = ((image1 + image2) / scale + offset)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.add_modulo(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#add_modulo)¶

    

Add two images, without clipping the result.

    
    
    out = ((image1 + image2) % MAX)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.blend(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _alpha :
[float](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.14\)")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#blend)¶

    

Blend images using constant transparency weight. Alias for
[`PIL.Image.blend()`](Image.html#PIL.Image.blend "PIL.Image.blend").

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.composite(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _mask : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#composite)¶

    

Create composite using transparency mask. Alias for
[`PIL.Image.composite()`](Image.html#PIL.Image.composite
"PIL.Image.composite").

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.constant(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _value :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#constant)¶

    

Fill a channel with a given gray level.

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.darker(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#darker)¶

    

Compares the two images, pixel by pixel, and returns a new image containing
the darker values.

    
    
    out = min(image1, image2)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.difference(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#difference)¶

    

Returns the absolute value of the pixel-by-pixel difference between the two
images.

    
    
    out = abs(image1 - image2)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.duplicate(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#duplicate)¶

    

Copy a channel. Alias for
[`PIL.Image.Image.copy()`](Image.html#PIL.Image.Image.copy
"PIL.Image.Image.copy").

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.invert(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#invert)¶

    

Invert an image (channel).

    
    
    out = MAX - image
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.lighter(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#lighter)¶

    

Compares the two images, pixel by pixel, and returns a new image containing
the lighter values.

    
    
    out = max(image1, image2)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.logical_and(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#logical_and)¶

    

Logical AND between two images.

Both of the images must have mode “1”. If you would like to perform a logical
AND on an image with a mode other than “1”, try `multiply()` instead, using a
black-and-white mask as the second image.

    
    
    out = ((image1 and image2) % MAX)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.logical_or(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#logical_or)¶

    

Logical OR between two images.

Both of the images must have mode “1”.

    
    
    out = ((image1 or image2) % MAX)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.logical_xor(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#logical_xor)¶

    

Logical XOR between two images.

Both of the images must have mode “1”.

    
    
    out = ((bool(image1) != bool(image2)) % MAX)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.multiply(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#multiply)¶

    

Superimposes two images on top of each other.

If you multiply an image with a solid black image, the result is black. If you
multiply with a solid white image, the image is unaffected.

    
    
    out = image1 * image2 / MAX
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.soft_light(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#soft_light)¶

    

Superimposes two images on top of each other using the Soft Light algorithm

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.hard_light(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#hard_light)¶

    

Superimposes two images on top of each other using the Hard Light algorithm

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.overlay(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#overlay)¶

    

Superimposes two images on top of each other using the Overlay algorithm

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.offset(_image : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _xoffset : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")_, _yoffset : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#offset)¶
    

Returns a copy of the image where data has been offset by the given distances.
Data wraps around the edges. If `yoffset` is omitted, it is assumed to be
equal to `xoffset`.

Parameters:

    

  * **image** – Input image.

  * **xoffset** – The horizontal distance.

  * **yoffset** – The vertical distance. If omitted, both distances are set to the same value.

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.screen(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#screen)¶

    

Superimposes two inverted images on top of each other.

    
    
    out = MAX - ((MAX - image1) * (MAX - image2) / MAX)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.subtract(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _scale :
[float](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.14\)") = 1.0_, _offset :
[float](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.14\)") = 0_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#subtract)¶

    

Subtracts two images, dividing the result by scale and adding the offset. If
omitted, scale defaults to 1.0, and offset to 0.0.

    
    
    out = ((image1 - image2) / scale + offset)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

PIL.ImageChops.subtract_modulo(_image1 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _image2 : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageChops.html#subtract_modulo)¶

    

Subtract two images, without clipping the result.

    
    
    out = ((image1 - image2) % MAX)
    

Return type:

    

[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

[ Next `ImageCms` module ](ImageCms.html) [ Previous `Image` module
](Image.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageChops` (“channel operations”) module
    * Functions
      * `add()`
      * `add_modulo()`
      * `blend()`
      * `composite()`
      * `constant()`
      * `darker()`
      * `difference()`
      * `duplicate()`
      * `invert()`
      * `lighter()`
      * `logical_and()`
      * `logical_or()`
      * `logical_xor()`
      * `multiply()`
      * `soft_light()`
      * `hard_light()`
      * `overlay()`
      * `offset()`
      * `screen()`
      * `subtract()`
      * `subtract_modulo()`

