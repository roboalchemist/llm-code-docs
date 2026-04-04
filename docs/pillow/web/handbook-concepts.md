# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/handbook/concepts.html
# Path: handbook/concepts.html

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
  * [Handbook](index.html)
    * [Overview](overview.html)
    * [Tutorial](tutorial.html)
    * Concepts
    * [Appendices](appendices.html)
      * [Image file formats](image-file-formats.html)
      * [Text anchors](text-anchors.html)
      * [Third-party plugins](third-party-plugins.html)
      * [Writing your own image plugin](writing-your-own-image-plugin.html)
      * [Decoders](writing-your-own-image-plugin.html#decoders)
      * [Writing your own file codec in C](writing-your-own-image-plugin.html#writing-your-own-file-codec-in-c)
      * [Writing your own file codec in Python](writing-your-own-image-plugin.html#writing-your-own-file-codec-in-python)
  * [Reference](../reference/index.html)
    * [`Image` module](../reference/Image.html)
    * [`ImageChops` (“channel operations”) module](../reference/ImageChops.html)
    * [`ImageCms` module](../reference/ImageCms.html)
    * [`ImageColor` module](../reference/ImageColor.html)
    * [`ImageDraw` module](../reference/ImageDraw.html)
    * [`ImageEnhance` module](../reference/ImageEnhance.html)
    * [`ImageFile` module](../reference/ImageFile.html)
    * [`ImageFilter` module](../reference/ImageFilter.html)
    * [`ImageFont` module](../reference/ImageFont.html)
    * [`ImageGrab` module](../reference/ImageGrab.html)
    * [`ImageMath` module](../reference/ImageMath.html)
    * [`ImageMorph` module](../reference/ImageMorph.html)
    * [`ImageOps` module](../reference/ImageOps.html)
    * [`ImagePalette` module](../reference/ImagePalette.html)
    * [`ImagePath` module](../reference/ImagePath.html)
    * [`ImageQt` module](../reference/ImageQt.html)
    * [`ImageSequence` module](../reference/ImageSequence.html)
    * [`ImageShow` module](../reference/ImageShow.html)
    * [`ImageStat` module](../reference/ImageStat.html)
    * [`ImageText` module](../reference/ImageText.html)
    * [`ImageTk` module](../reference/ImageTk.html)
    * [`ImageTransform` module](../reference/ImageTransform.html)
    * [`ImageWin` module (Windows-only)](../reference/ImageWin.html)
    * [`ExifTags` module](../reference/ExifTags.html)
    * [`TiffTags` module](../reference/TiffTags.html)
    * [`JpegPresets` module](../reference/JpegPresets.html)
    * [`PSDraw` module](../reference/PSDraw.html)
    * [`PixelAccess` class](../reference/PixelAccess.html)
    * [`features` module](../reference/features.html)
    * [PIL package (autodoc of remaining modules)](../PIL.html)
    * [Plugin reference](../reference/plugins.html)
    * [Internal reference](../reference/internal_design.html)
      * [File handling in Pillow](../reference/open_files.html)
      * [Limits](../reference/limits.html)
      * [Block allocator](../reference/block_allocator.html)
      * [Internal modules](../reference/internal_modules.html)
      * [C extension debugging on Linux, with GBD/Valgrind](../reference/c_extension_debugging.html)
      * [Arrow support](../reference/arrow_support.html)
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

[ View this page ](../_sources/handbook/concepts.rst.txt "View this page")

# Concepts¶

The Python Imaging Library handles _raster images_ ; that is, rectangles of
pixel data.

## Bands¶

An image can consist of one or more bands of data. The Python Imaging Library
allows you to store several bands in a single image, provided they all have
the same dimensions and depth. For example, a PNG image might have ‘R’, ‘G’,
‘B’, and ‘A’ bands for the red, green, blue, and alpha transparency values.
Many operations act on each band separately, e.g., histograms. It is often
useful to think of each pixel as having one value per band.

To get the number and names of bands in an image, use the
[`getbands()`](../reference/Image.html#PIL.Image.Image.getbands
"PIL.Image.Image.getbands") method.

## Modes¶

The `mode` of an image is a string which defines the type and depth of a pixel
in the image. Each pixel uses the full range of the bit depth. So a 1-bit
pixel has a range of 0-1, an 8-bit pixel has a range of 0-255, a 32-signed
integer pixel has the range of INT32 and a 32-bit floating point pixel has the
range of FLOAT32. The current release supports the following standard modes:

  * `1` (1-bit pixels, black and white, stored with one pixel per byte)

  * `L` (8-bit pixels, grayscale)

  * `P` (8-bit pixels, mapped to any other mode using a color palette)

  * `RGB` (3x8-bit pixels, true color)

  * `RGBA` (4x8-bit pixels, true color with transparency mask)

  * `CMYK` (4x8-bit pixels, color separation)

  * `YCbCr` (3x8-bit pixels, color video format)

    * Note that this refers to the JPEG, and not the ITU-R BT.2020, standard

  * `LAB` (3x8-bit pixels, the L*a*b color space)

  * `HSV` (3x8-bit pixels, Hue, Saturation, Value color space)

    * Hue’s range of 0-255 is a scaled version of 0 degrees <= Hue < 360 degrees

  * `I` (32-bit signed integer pixels)

  * `F` (32-bit floating point pixels)

Pillow also provides limited support for a few additional modes, including:

  * `LA` (L with alpha)

  * `PA` (P with alpha)

  * `RGBX` (true color with padding)

  * `RGBa` (true color with premultiplied alpha)

  * `La` (L with premultiplied alpha)

  * `I;16` (16-bit unsigned integer pixels)

  * `I;16L` (16-bit little endian unsigned integer pixels)

  * `I;16B` (16-bit big endian unsigned integer pixels)

  * `I;16N` (16-bit native endian unsigned integer pixels)

Premultiplied alpha is where the values for each other channel have been
multiplied by the alpha. For example, an RGBA pixel of `(10, 20, 30, 127)`
would convert to an RGBa pixel of `(5, 10, 15, 127)`. The values of the R, G
and B channels are halved as a result of the half transparency in the alpha
channel.

Apart from these additional modes, Pillow doesn’t yet support multichannel
images with a depth of more than 8 bits per channel.

Pillow also doesn’t support user-defined modes; if you need to handle band
combinations that are not listed above, use a sequence of Image objects.

You can read the mode of an image through the
[`mode`](../reference/Image.html#PIL.Image.Image.mode "PIL.Image.Image.mode")
attribute. This is a string containing one of the above values.

## Size¶

You can read the image size through the
[`size`](../reference/Image.html#PIL.Image.Image.size "PIL.Image.Image.size")
attribute. This is a 2-tuple, containing the horizontal and vertical size in
pixels.

## Coordinate system¶

The Python Imaging Library uses a Cartesian pixel coordinate system, with
(0,0) in the upper left corner. Note that the coordinates refer to the implied
pixel corners; the centre of a pixel addressed as (0, 0) actually lies at
(0.5, 0.5).

Coordinates are usually passed to the library as 2-tuples (x, y). Rectangles
are represented as 4-tuples, (x1, y1, x2, y2), with the upper left corner
given first.

## Palette¶

The palette mode (`P`) uses a color palette to define the actual color for
each pixel.

## Colors¶

To specify colors, you can use tuples with a value for each channel in the
image, e.g. `Image.new("RGB", (1, 1), (255, 0, 0))`.

If an image has a single channel, you can use a single number instead, e.g.
`Image.new("L", (1, 1), 255)`. For “F” mode images, floating point values are
also accepted. In the case of “P” mode images, these will be indexes for the
color palette.

If a single value is used for an image with more than one channel, it will
still be parsed:

    
    
    >>> from PIL import Image
    >>> im = Image.new("RGBA", (1, 1), 0x04030201)
    >>> im.getpixel((0, 0))
    (1, 2, 3, 4)
    

Some methods accept other forms, such as color names. See [Color
names](../reference/ImageColor.html#color-names).

## Info¶

You can attach auxiliary information to an image using the
[`info`](../reference/Image.html#PIL.Image.Image.info "PIL.Image.Image.info")
attribute. This is a dictionary object.

How such information is handled when loading and saving image files is up to
the file format handler (see the chapter on [Image file formats](image-file-
formats.html#image-file-formats)). Most handlers add properties to the
[`info`](../reference/Image.html#PIL.Image.Image.info "PIL.Image.Image.info")
attribute when loading an image, but ignore it when saving images.

## Transparency¶

If an image does not have an alpha band, transparency may be specified in the
[`info`](../reference/Image.html#PIL.Image.Image.info "PIL.Image.Image.info")
attribute with a “transparency” key.

Most of the time, the “transparency” value is a single integer, describing
which pixel value is transparent in a “1”, “L”, “I” or “P” mode image.
However, PNG images may have three values, one for each channel in an “RGB”
mode image, or can have a byte string for a “P” mode image, to specify the
alpha value for each palette entry.

## Orientation¶

A common element of the [`info`](../reference/Image.html#PIL.Image.Image.info
"PIL.Image.Image.info") attribute for JPG and TIFF images is the EXIF
orientation tag. This is an instruction for how the image data should be
oriented. For example, it may instruct an image to be rotated by 90 degrees,
or to be mirrored. To apply this information to an image,
[`exif_transpose()`](../reference/ImageOps.html#PIL.ImageOps.exif_transpose
"PIL.ImageOps.exif_transpose") can be used.

## Filters¶

For geometry operations that may map multiple input pixels to a single output
pixel, the Python Imaging Library provides different resampling _filters_.

Resampling.NEAREST

    

Pick one nearest pixel from the input image. Ignore all other input pixels.

Resampling.BOX

    

Each pixel of source image contributes to one pixel of the destination image
with identical weights. For upscaling is equivalent of
[`Resampling.NEAREST`](../reference/Image.html#PIL.Image.Resampling.NEAREST
"PIL.Image.Resampling.NEAREST"). This filter can only be used with the
[`resize()`](../reference/Image.html#PIL.Image.Image.resize
"PIL.Image.Image.resize") and
[`thumbnail()`](../reference/Image.html#PIL.Image.Image.thumbnail
"PIL.Image.Image.thumbnail") methods.

Added in version 3.4.0.

Resampling.BILINEAR

    

For resize calculate the output pixel value using linear interpolation on all
pixels that may contribute to the output value. For other transformations
linear interpolation over a 2x2 environment in the input image is used.

Resampling.HAMMING

    

Produces a sharper image than
[`Resampling.BILINEAR`](../reference/Image.html#PIL.Image.Resampling.BILINEAR
"PIL.Image.Resampling.BILINEAR"), doesn’t have dislocations on local level
like with [`Resampling.BOX`](../reference/Image.html#PIL.Image.Resampling.BOX
"PIL.Image.Resampling.BOX"). This filter can only be used with the
[`resize()`](../reference/Image.html#PIL.Image.Image.resize
"PIL.Image.Image.resize") and
[`thumbnail()`](../reference/Image.html#PIL.Image.Image.thumbnail
"PIL.Image.Image.thumbnail") methods.

Added in version 3.4.0.

Resampling.BICUBIC

    

For resize calculate the output pixel value using cubic interpolation on all
pixels that may contribute to the output value. For other transformations
cubic interpolation over a 4x4 environment in the input image is used.

Resampling.LANCZOS

    

Calculate the output pixel value using a high-quality Lanczos filter (a
truncated sinc) on all pixels that may contribute to the output value. This
filter can only be used with the
[`resize()`](../reference/Image.html#PIL.Image.Image.resize
"PIL.Image.Image.resize") and
[`thumbnail()`](../reference/Image.html#PIL.Image.Image.thumbnail
"PIL.Image.Image.thumbnail") methods.

Added in version 1.1.3.

### Filters comparison table¶

Filter | Downscaling quality | Upscaling quality | Performance  
---|---|---|---  
[`Resampling.NEAREST`](../reference/Image.html#PIL.Image.Resampling.NEAREST "PIL.Image.Resampling.NEAREST") |  |  | ⭐⭐⭐⭐⭐  
[`Resampling.BOX`](../reference/Image.html#PIL.Image.Resampling.BOX "PIL.Image.Resampling.BOX") | ⭐ |  | ⭐⭐⭐⭐  
[`Resampling.BILINEAR`](../reference/Image.html#PIL.Image.Resampling.BILINEAR "PIL.Image.Resampling.BILINEAR") | ⭐ | ⭐ | ⭐⭐⭐  
[`Resampling.HAMMING`](../reference/Image.html#PIL.Image.Resampling.HAMMING "PIL.Image.Resampling.HAMMING") | ⭐⭐ |  | ⭐⭐⭐  
[`Resampling.BICUBIC`](../reference/Image.html#PIL.Image.Resampling.BICUBIC "PIL.Image.Resampling.BICUBIC") | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐  
[`Resampling.LANCZOS`](../reference/Image.html#PIL.Image.Resampling.LANCZOS "PIL.Image.Resampling.LANCZOS") | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐  
  
[ Next Appendices ](appendices.html) [ Previous Tutorial ](tutorial.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * Concepts
    * Bands
    * Modes
    * Size
    * Coordinate system
    * Palette
    * Colors
    * Info
    * Transparency
    * Orientation
    * Filters
      * Filters comparison table

