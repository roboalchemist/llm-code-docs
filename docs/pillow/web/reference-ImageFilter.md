# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageFilter.html
# Path: reference/ImageFilter.html

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
    * [`ImageChops` (“channel operations”) module](ImageChops.html)
    * [`ImageCms` module](ImageCms.html)
    * [`ImageColor` module](ImageColor.html)
    * [`ImageDraw` module](ImageDraw.html)
    * [`ImageEnhance` module](ImageEnhance.html)
    * [`ImageFile` module](ImageFile.html)
    * `ImageFilter` module
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

[ View this page ](../_sources/reference/ImageFilter.rst.txt "View this page")

# `ImageFilter` module¶

The `ImageFilter` module contains definitions for a pre-defined set of
filters, which can be be used with the
[`Image.filter()`](Image.html#PIL.Image.Image.filter "PIL.Image.Image.filter")
method.

## Example: Filter an image¶

    
    
    from PIL import ImageFilter
    
    im1 = im.filter(ImageFilter.BLUR)
    
    im2 = im.filter(ImageFilter.MinFilter(3))
    im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
    

## Filters¶

Pillow provides the following set of predefined image enhancement filters:

  * **BLUR**

  * **CONTOUR**

  * **DETAIL**

  * **EDGE_ENHANCE**

  * **EDGE_ENHANCE_MORE**

  * **EMBOSS**

  * **FIND_EDGES**

  * **SHARPEN**

  * **SMOOTH**

  * **SMOOTH_MORE**

class PIL.ImageFilter.Color3DLUT(_size : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]_, _table : Sequence[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")] | Sequence[Sequence[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]] | [NumpyArray](internal_modules.html#PIL._typing.NumpyArray "PIL._typing.NumpyArray")_, _channels : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 3_, _target_mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _** kwargs: [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)")_)[[source]](../_modules/PIL/ImageFilter.html#Color3DLUT)¶
    

Three-dimensional color lookup table.

Transforms 3-channel pixels using the values of the channels as coordinates in
the 3D lookup table and interpolating the nearest elements.

This method allows you to apply almost any color transformation in constant
time by using pre-calculated decimated tables.

Added in version 5.2.0.

Parameters:

    

  * **size** – Size of the table. One int or tuple of (int, int, int). Minimal size in any dimension is 2, maximum is 65.

  * **table** – Flat lookup table. A list of `channels * size**3` float elements or a list of `size**3` channels-sized tuples with floats. Channels are changed first, then first dimension, then second, then third. Value 0.0 corresponds lowest value of output, 1.0 highest.

  * **channels** – Number of channels in the table. Could be 3 or 4. Default is 3.

  * **target_mode** – A mode for the result image. Should have not less than `channels` channels. Default is `None`, which means that mode wouldn’t be changed.

classmethod generate(_size : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]_, _callback : Callable[[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), ...]]_, _channels : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 3_, _target_mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> Color3DLUT[[source]](../_modules/PIL/ImageFilter.html#Color3DLUT.generate)¶
    

Generates new LUT using provided callback.

Parameters:

    

  * **size** – Size of the table. Passed to the constructor.

  * **callback** – Function with three parameters which correspond three color channels. Will be called `size**3` times with values from 0.0 to 1.0 and should return a tuple with `channels` elements.

  * **channels** – The number of channels which should return callback.

  * **target_mode** – Passed to the constructor of the resulting lookup table.

transform(_callback : Callable[..., [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), ...]]_, _with_normals : [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = False_, _channels : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _target_mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> Color3DLUT[[source]](../_modules/PIL/ImageFilter.html#Color3DLUT.transform)¶
    

Transforms the table values using provided callback and returns a new LUT with
altered values.

Parameters:

    

  * **callback** – A function which takes old lookup table values and returns a new set of values. The number of arguments which function should take is `self.channels` or `3 + self.channels` if `with_normals` flag is set. Should return a tuple of `self.channels` or `channels` elements if it is set.

  * **with_normals** – If true, `callback` will be called with coordinates in the color cube as the first three arguments. Otherwise, `callback` will be called only with actual color values.

  * **channels** – The number of channels in the resulting lookup table.

  * **target_mode** – Passed to the constructor of the resulting lookup table.

class PIL.ImageFilter.BoxBlur(_radius : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]_)[[source]](../_modules/PIL/ImageFilter.html#BoxBlur)¶
    

Blurs the image by setting each pixel to the average value of the pixels in a
square box extending radius pixels in each direction. Supports float radius of
arbitrary size. Uses an optimized implementation which runs in linear time
relative to the size of the image for any radius value.

Parameters:

    

**radius** –

Size of the box in a direction. Either a sequence of two numbers for x and y,
or a single number for both.

Radius 0 does not blur, returns an identical image. Radius 1 takes 1 pixel in
each direction, i.e. 9 pixels in total.

class PIL.ImageFilter.GaussianBlur(_radius : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")] = 2_)[[source]](../_modules/PIL/ImageFilter.html#GaussianBlur)¶
    

Blurs the image with a sequence of extended box filters, which approximates a
Gaussian kernel. For details on accuracy see <<https://www.mia.uni-
saarland.de/Publications/gwosdek-ssvm11.pdf>>

Parameters:

    

**radius** – Standard deviation of the Gaussian kernel. Either a sequence of
two numbers for x and y, or a single number for both.

class PIL.ImageFilter.UnsharpMask(_radius :
[float](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.14\)") = 2_, _percent :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 150_, _threshold :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 3_)[[source]](../_modules/PIL/ImageFilter.html#UnsharpMask)¶

    

Unsharp mask filter.

See Wikipedia’s entry on [digital unsharp
masking](https://en.wikipedia.org/wiki/Unsharp_masking#Digital_unsharp_masking)
for an explanation of the parameters.

Parameters:

    

  * **radius** – Blur Radius

  * **percent** – Unsharp strength, in percent

  * **threshold** – Threshold controls the minimum brightness change that will be sharpened

class PIL.ImageFilter.Kernel(_size : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]_, _kernel : [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]_, _scale : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _offset : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") = 0_)[[source]](../_modules/PIL/ImageFilter.html#Kernel)¶
    

Create a convolution kernel. This only supports 3x3 and 5x5 integer and
floating point kernels.

Kernels can only be applied to “L” and “RGB” images.

Parameters:

    

  * **size** – Kernel size, given as (width, height). This must be (3,3) or (5,5).

  * **kernel** – A sequence containing kernel weights. The kernel will be flipped vertically before being applied to the image.

  * **scale** – Scale factor. If given, the result for each pixel is divided by this value. The default is the sum of the kernel weights.

  * **offset** – Offset. If given, this value is added to the result, after it has been divided by the scale factor.

class PIL.ImageFilter.RankFilter(_size :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_, _rank : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python
v3.14\)")_)[[source]](../_modules/PIL/ImageFilter.html#RankFilter)¶

    

Create a rank filter. The rank filter sorts all pixels in a window of the
given size, and returns the `rank`’th value.

Parameters:

    

  * **size** – The kernel size, in pixels.

  * **rank** – What pixel value to pick. Use 0 for a min filter, `size * size / 2` for a median filter, `size * size - 1` for a max filter, etc.

class PIL.ImageFilter.MedianFilter(_size :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 3_)[[source]](../_modules/PIL/ImageFilter.html#MedianFilter)¶

    

Create a median filter. Picks the median pixel value in a window with the
given size.

Parameters:

    

**size** – The kernel size, in pixels.

class PIL.ImageFilter.MinFilter(_size :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 3_)[[source]](../_modules/PIL/ImageFilter.html#MinFilter)¶

    

Create a min filter. Picks the lowest pixel value in a window with the given
size.

Parameters:

    

**size** – The kernel size, in pixels.

class PIL.ImageFilter.MaxFilter(_size :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 3_)[[source]](../_modules/PIL/ImageFilter.html#MaxFilter)¶

    

Create a max filter. Picks the largest pixel value in a window with the given
size.

Parameters:

    

**size** – The kernel size, in pixels.

class PIL.ImageFilter.ModeFilter(_size :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 3_)[[source]](../_modules/PIL/ImageFilter.html#ModeFilter)¶

    

Create a mode filter. Picks the most frequent pixel value in a box with the
given size. Pixel values that occur only once or twice are ignored; if no
pixel value occurs more than twice, the original pixel value is preserved.

Parameters:

    

**size** – The kernel size, in pixels.

class
PIL.ImageFilter.Filter[[source]](../_modules/PIL/ImageFilter.html#Filter)¶

    

An abstract mixin used for filtering images (for use with
[`filter()`](Image.html#PIL.Image.Image.filter "PIL.Image.Image.filter")).

Implementors must provide the following method:

filter(_self_ ,
_image_)[[source]](../_modules/PIL/ImageFilter.html#Filter.filter)¶

    

Applies a filter to a single-band image, or a single band of an image.

Returns:

    

A filtered copy of the image.

class
PIL.ImageFilter.MultibandFilter[[source]](../_modules/PIL/ImageFilter.html#MultibandFilter)¶

    

An abstract mixin used for filtering multi-band images (for use with
[`filter()`](Image.html#PIL.Image.Image.filter "PIL.Image.Image.filter")).

Implementors must provide the following method:

filter(_self_ , _image_)¶

    

Applies a filter to a multi-band image.

Returns:

    

A filtered copy of the image.

[ Next `ImageFont` module ](ImageFont.html) [ Previous `ImageFile` module
](ImageFile.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageFilter` module
    * Example: Filter an image
    * Filters
      * `Color3DLUT`
        * `Color3DLUT.generate()`
        * `Color3DLUT.transform()`
      * `BoxBlur`
      * `GaussianBlur`
      * `UnsharpMask`
      * `Kernel`
      * `RankFilter`
      * `MedianFilter`
      * `MinFilter`
      * `MaxFilter`
      * `ModeFilter`
      * `Filter`
        * `Filter.filter()`
      * `MultibandFilter`
        * `MultibandFilter.filter()`

