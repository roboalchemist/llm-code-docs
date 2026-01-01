# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageOps.html
# Path: reference/ImageOps.html

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
    * [`ImageFilter` module](ImageFilter.html)
    * [`ImageFont` module](ImageFont.html)
    * [`ImageGrab` module](ImageGrab.html)
    * [`ImageMath` module](ImageMath.html)
    * [`ImageMorph` module](ImageMorph.html)
    * `ImageOps` module
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

[ View this page ](../_sources/reference/ImageOps.rst.txt "View this page")

# `ImageOps` module¶

The `ImageOps` module contains a number of ‘ready-made’ image processing
operations. This module is somewhat experimental, and most operators only work
on L and RGB images.

Added in version 1.1.3.

PIL.ImageOps.autocontrast(_image : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _cutoff : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")] = 0_, _ignore : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _mask : [Image](Image.html#PIL.Image.Image "PIL.Image.Image") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _preserve_tone : [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = False_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#autocontrast)¶
    

Maximize (normalize) image contrast. This function calculates a histogram of
the input image (or mask region), removes `cutoff` percent of the lightest and
darkest pixels from the histogram, and remaps the image so that the darkest
pixel becomes black (0), and the lightest becomes white (255).

Parameters:

    

  * **image** – The image to process.

  * **cutoff** – The percent to cut off from the histogram on the low and high ends. Either a tuple of (low, high), or a single number for both.

  * **ignore** – The background pixel value (use None for no background).

  * **mask** – Histogram used in contrast operation is computed using pixels within the mask. If no mask is given the entire image is used for histogram computation.

  * **preserve_tone** – 

Preserve image tone in Photoshop-like style autocontrast.

Added in version 8.2.0.

Returns:

    

An image.

PIL.ImageOps.colorize(_image : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _black : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), ...]_, _white : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), ...]_, _mid : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), ...] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _blackpoint : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 0_, _whitepoint : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 255_, _midpoint : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 127_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#colorize)¶
    

Colorize grayscale image. This function calculates a color wedge which maps
all black pixels in the source image to the first color and all white pixels
to the second color. If `mid` is specified, it uses three-color mapping. The
`black` and `white` arguments should be RGB tuples or color names; optionally
you can use three-color mapping by also specifying `mid`. Mapping positions
for any of the colors can be specified (e.g. `blackpoint`), where these
parameters are the integer value corresponding to where the corresponding
color should be mapped. These parameters must have logical order, such that
`blackpoint <= midpoint <= whitepoint` (if `mid` is specified).

Parameters:

    

  * **image** – The image to colorize.

  * **black** – The color to use for black input pixels.

  * **white** – The color to use for white input pixels.

  * **mid** – The color to use for midtone input pixels.

  * **blackpoint** – an int value [0, 255] for the black mapping.

  * **whitepoint** – an int value [0, 255] for the white mapping.

  * **midpoint** – an int value [0, 255] for the midtone mapping.

Returns:

    

An image.

PIL.ImageOps.crop(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _border :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 0_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#crop)¶

    

Remove border from image. The same amount of pixels are removed from all four
sides. This function works on all image modes.

See also

[`crop()`](Image.html#PIL.Image.Image.crop "PIL.Image.Image.crop")

Parameters:

    

  * **image** – The image to crop.

  * **border** – The number of pixels to remove.

Returns:

    

An image.

PIL.ImageOps.scale(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _factor :
[float](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.14\)")_, _resample :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = Resampling.BICUBIC_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#scale)¶

    

Returns a rescaled image by a specific factor given in parameter. A factor
greater than 1 expands the image, between 0 and 1 contracts the image.

Parameters:

    

  * **image** – The image to rescale.

  * **factor** – The expansion factor, as a float.

  * **resample** – Resampling method to use. Default is [`BICUBIC`](Image.html#PIL.Image.Resampling.BICUBIC "PIL.Image.Resampling.BICUBIC"). See [Filters](../handbook/concepts.html#concept-filters).

Returns:

    

An [`Image`](Image.html#PIL.Image.Image "PIL.Image.Image") object.

class PIL.ImageOps.SupportsGetMesh(_* args_, _**
kwargs_)[[source]](../_modules/PIL/ImageOps.html#SupportsGetMesh)¶

    

Bases:
[`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol
"\(in Python v3.14\)")

An object that supports the `getmesh` method, taking an image as an argument,
and returning a list of tuples. Each tuple contains two tuples, the source box
as a tuple of 4 integers, and a tuple of 8 integers for the final
quadrilateral, in order of top left, bottom left, bottom right, top right.

PIL.ImageOps.deform(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _deformer : SupportsGetMesh_, _resample :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = Resampling.BILINEAR_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#deform)¶

    

Deform the image.

Parameters:

    

  * **image** – The image to deform.

  * **deformer** – A deformer object. Any object that implements a `getmesh` method can be used.

  * **resample** – An optional resampling filter. Same values possible as in the PIL.Image.transform function.

Returns:

    

An image.

PIL.ImageOps.equalize(_image : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _mask : [Image](Image.html#PIL.Image.Image "PIL.Image.Image") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#equalize)¶
    

Equalize the image histogram. This function applies a non-linear mapping to
the input image, in order to create a uniform distribution of grayscale values
in the output image.

Parameters:

    

  * **image** – The image to equalize.

  * **mask** – An optional mask. If given, only the pixels selected by the mask are included in the analysis.

Returns:

    

An image.

PIL.ImageOps.expand(_image : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _border : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), ...] = 0_, _fill : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), ...] = 0_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#expand)¶
    

Add border to the image

Parameters:

    

  * **image** – The image to expand.

  * **border** – Border width, in pixels.

  * **fill** – Pixel fill value (a color value). Default is 0 (black).

Returns:

    

An image.

PIL.ImageOps.flip(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#flip)¶

    

Flip the image vertically (top to bottom).

Parameters:

    

**image** – The image to flip.

Returns:

    

An image.

PIL.ImageOps.grayscale(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#grayscale)¶

    

Convert the image to grayscale.

Parameters:

    

**image** – The image to convert.

Returns:

    

An image.

PIL.ImageOps.invert(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#invert)¶

    

Invert (negate) the image.

Parameters:

    

**image** – The image to invert.

Returns:

    

An image.

PIL.ImageOps.mirror(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#mirror)¶

    

Flip image horizontally (left to right).

Parameters:

    

**image** – The image to mirror.

Returns:

    

An image.

PIL.ImageOps.posterize(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _bits :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#posterize)¶

    

Reduce the number of bits for each color channel.

Parameters:

    

  * **image** – The image to posterize.

  * **bits** – The number of bits to keep for each channel (1-8).

Returns:

    

An image.

PIL.ImageOps.solarize(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _threshold :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 128_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#solarize)¶

    

Invert all pixel values above a threshold.

Parameters:

    

  * **image** – The image to solarize.

  * **threshold** – All pixels above this grayscale level are inverted.

Returns:

    

An image.

PIL.ImageOps.exif_transpose(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _*_ , _in_place :
[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "\(in
Python v3.14\)")[True]_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageOps.html#exif_transpose)¶

PIL.ImageOps.exif_transpose(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _*_ , _in_place :
[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "\(in
Python v3.14\)")[False] = False_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")

    

If an image has an EXIF Orientation tag, other than 1, transpose the image
accordingly, and remove the orientation data.

Parameters:

    

  * **image** – The image to transpose.

  * **in_place** – Boolean. Keyword-only argument. If `True`, the original image is modified in-place, and `None` is returned. If `False` (default), a new [`Image`](Image.html#PIL.Image.Image "PIL.Image.Image") object is returned with the transposition applied. If there is no transposition, a copy of the image will be returned.

## Resize relative to a given size¶

    
    
    from PIL import Image, ImageOps
    size = (100, 150)
    with Image.open("Tests/images/hopper.webp") as im:
        ImageOps.contain(im, size).save("imageops_contain.webp")
        ImageOps.cover(im, size).save("imageops_cover.webp")
        ImageOps.fit(im, size).save("imageops_fit.webp")
        ImageOps.pad(im, size, color="#f00").save("imageops_pad.webp")
    
        # thumbnail() can also be used,
        # but will modify the image object in place
        im.thumbnail(size)
        im.save("image_thumbnail.webp")
    

| [`thumbnail()`](Image.html#PIL.Image.Image.thumbnail "PIL.Image.Image.thumbnail") | `contain()` | `cover()` | `fit()` | `pad()`  
---|---|---|---|---|---  
Given size | `(100, 150)` | `(100, 150)` | `(100, 150)` | `(100, 150)` | `(100, 150)`  
Resulting image | ![../_images/image_thumbnail.webp](../_images/image_thumbnail.webp) | ![../_images/imageops_contain.webp](../_images/imageops_contain.webp) | ![../_images/imageops_cover.webp](../_images/imageops_cover.webp) | ![../_images/imageops_fit.webp](../_images/imageops_fit.webp) | ![../_images/imageops_pad.webp](../_images/imageops_pad.webp)  
Resulting size | `100×100` | `100×100` | `150×150` | `100×150` | `100×150`  
  
PIL.ImageOps.contain(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _size :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]_, _method :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = Resampling.BICUBIC_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#contain)¶

    

Returns a resized version of the image, set to the maximum width and height
within the requested size, while maintaining the original aspect ratio.

Parameters:

    

  * **image** – The image to resize.

  * **size** – The requested output size in pixels, given as a (width, height) tuple.

  * **method** – Resampling method to use. Default is [`BICUBIC`](Image.html#PIL.Image.Resampling.BICUBIC "PIL.Image.Resampling.BICUBIC"). See [Filters](../handbook/concepts.html#concept-filters).

Returns:

    

An image.

PIL.ImageOps.cover(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _size :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]_, _method :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = Resampling.BICUBIC_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#cover)¶

    

Returns a resized version of the image, so that the requested size is covered,
while maintaining the original aspect ratio.

Parameters:

    

  * **image** – The image to resize.

  * **size** – The requested output size in pixels, given as a (width, height) tuple.

  * **method** – Resampling method to use. Default is [`BICUBIC`](Image.html#PIL.Image.Resampling.BICUBIC "PIL.Image.Resampling.BICUBIC"). See [Filters](../handbook/concepts.html#concept-filters).

Returns:

    

An image.

PIL.ImageOps.fit(_image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _size :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]_, _method :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = Resampling.BICUBIC_, _bleed :
[float](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.14\)") = 0.0_, _centering :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.14\)"),
[float](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.14\)")] = (0.5, 0.5)_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#fit)¶

    

Returns a resized and cropped version of the image, cropped to the requested
aspect ratio and size.

This function was contributed by Kevin Cazabon.

Parameters:

    

  * **image** – The image to resize and crop.

  * **size** – The requested output size in pixels, given as a (width, height) tuple.

  * **method** – Resampling method to use. Default is [`BICUBIC`](Image.html#PIL.Image.Resampling.BICUBIC "PIL.Image.Resampling.BICUBIC"). See [Filters](../handbook/concepts.html#concept-filters).

  * **bleed** – Remove a border around the outside of the image from all four edges. The value is a decimal percentage (use 0.01 for one percent). The default value is 0 (no border). Cannot be greater than or equal to 0.5.

  * **centering** – Control the cropping position. Use (0.5, 0.5) for center cropping (e.g. if cropping the width, take 50% off of the left side, and therefore 50% off the right side). (0.0, 0.0) will crop from the top left corner (i.e. if cropping the width, take all of the crop off of the right side, and if cropping the height, take all of it off the bottom). (1.0, 0.0) will crop from the bottom left corner, etc. (i.e. if cropping the width, take all of the crop off the left side, and if cropping the height take none from the top, and therefore all off the bottom).

Returns:

    

An image.

PIL.ImageOps.pad(_image : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _size : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]_, _method : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = Resampling.BICUBIC_, _color : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), ...] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _centering : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")] = (0.5, 0.5)_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image")[[source]](../_modules/PIL/ImageOps.html#pad)¶
    

Returns a resized and padded version of the image, expanded to fill the
requested aspect ratio and size.

Parameters:

    

  * **image** – The image to resize and crop.

  * **size** – The requested output size in pixels, given as a (width, height) tuple.

  * **method** – Resampling method to use. Default is [`BICUBIC`](Image.html#PIL.Image.Resampling.BICUBIC "PIL.Image.Resampling.BICUBIC"). See [Filters](../handbook/concepts.html#concept-filters).

  * **color** – The background color of the padded image.

  * **centering** – 

Control the position of the original image within the padded version.

> (0.5, 0.5) will keep the image centered (0, 0) will keep the image aligned
> to the top left (1, 1) will keep the image aligned to the bottom right

Returns:

    

An image.

[ Next `ImagePalette` module ](ImagePalette.html) [ Previous `ImageMorph`
module ](ImageMorph.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageOps` module
    * `autocontrast()`
    * `colorize()`
    * `crop()`
    * `scale()`
    * `SupportsGetMesh`
    * `deform()`
    * `equalize()`
    * `expand()`
    * `flip()`
    * `grayscale()`
    * `invert()`
    * `mirror()`
    * `posterize()`
    * `solarize()`
    * `exif_transpose()`
    * Resize relative to a given size
      * `contain()`
      * `cover()`
      * `fit()`
      * `pad()`

  *[*]: Keyword-only parameters separator (PEP 3102)

