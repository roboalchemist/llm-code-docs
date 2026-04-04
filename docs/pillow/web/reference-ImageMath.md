# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageMath.html
# Path: reference/ImageMath.html

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
    * `ImageMath` module
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

[ View this page ](../_sources/reference/ImageMath.rst.txt "View this page")

# `ImageMath` module¶

The `ImageMath` module can be used to evaluate “image expressions”, that can
take a number of images and generate a result.

`ImageMath` only supports single-layer images. To process multi-band images,
use the [`split()`](Image.html#PIL.Image.Image.split "PIL.Image.Image.split")
method or [`merge()`](Image.html#PIL.Image.merge "PIL.Image.merge") function.

## Example: Using the `ImageMath` module¶

    
    
    from PIL import Image, ImageMath
    
    with Image.open("image1.jpg") as im1:
        with Image.open("image2.jpg") as im2:
            out = ImageMath.lambda_eval(
              lambda args: args["convert"](args["min"](args["a"], args["b"]), 'L'),
              a=im1,
              b=im2
            )
            out = ImageMath.unsafe_eval(
              "convert(min(a, b), 'L')",
              a=im1,
              b=im2
            )
    

PIL.ImageMath.lambda_eval(_expression_ , _options_ , _**
kw_)[[source]](../_modules/PIL/ImageMath.html#lambda_eval)¶

    

Returns the result of an image function.

Parameters:

    

  * **expression** – A function that receives a dictionary.

  * **options** – Values to add to the function’s dictionary. Note that the names must be valid Python identifiers. Deprecated. You can instead use one or more keyword arguments, as shown in the above example.

  * ****kw** – Values to add to the function’s dictionary, mapping image names to Image instances.

Returns:

    

An image, an integer value, a floating point value, or a pixel tuple,
depending on the expression.

PIL.ImageMath.unsafe_eval(_expression_ , _options_ , _**
kw_)[[source]](../_modules/PIL/ImageMath.html#unsafe_eval)¶

    

Evaluates an image expression.

Danger

This uses Python’s `eval()` function to process the expression string, and
carries the security risks of doing so. It is not recommended to process
expressions without considering this. `lambda_eval()` is a more secure
alternative.

`ImageMath` only supports single-layer images. To process multi-band images,
use the [`split()`](Image.html#PIL.Image.Image.split "PIL.Image.Image.split")
method or [`merge()`](Image.html#PIL.Image.merge "PIL.Image.merge") function.

Parameters:

    

  * **expression** – A string which uses the standard Python expression syntax. In addition to the standard operators, you can also use the functions described below.

  * **options** – Values to add to the evaluation context. Note that the names must be valid Python identifiers. Deprecated. You can instead use one or more keyword arguments, as shown in the above example.

  * ****kw** – Values to add to the evaluation context, mapping image names to Image instances.

Returns:

    

An image, an integer value, a floating point value, or a pixel tuple,
depending on the expression.

## Expression syntax¶

  * `lambda_eval()` expressions are functions that receive a dictionary containing images and operators.

  * `unsafe_eval()` expressions are standard Python expressions, but they’re evaluated in a non-standard environment.

Danger

`unsafe_eval()` uses Python’s `eval()` function to process the expression
string, and carries the security risks of doing so. It is not recommended to
process expressions without considering this. `lambda_eval()` is a more secure
alternative.

### Standard operators¶

You can use standard arithmetical operators for addition (+), subtraction (-),
multiplication (*), and division (/).

The module also supports unary minus (-), modulo (%), and power (**)
operators.

Note that all operations are done with 32-bit integers or 32-bit floating
point values, as necessary. For example, if you add two 8-bit images, the
result will be a 32-bit integer image. If you add a floating point constant to
an 8-bit image, the result will be a 32-bit floating point image.

You can force conversion using the `convert()`, `float()`, and `int()`
functions described below.

### Bitwise operators¶

The module also provides operations that operate on individual bits. This
includes and (&), or (|), and exclusive or (^). You can also invert (~) all
pixel bits.

Note that the operands are converted to 32-bit signed integers before the
bitwise operation is applied. This means that you’ll get negative values if
you invert an ordinary grayscale image. You can use the and (&) operator to
mask off unwanted bits.

Bitwise operators don’t work on floating point images.

### Logical operators¶

Logical operators like `and`, `or`, and `not` work on entire images, rather
than individual pixels.

An empty image (all pixels zero) is treated as false. All other images are
treated as true.

Note that `and` and `or` return the last evaluated operand, while not always
returns a boolean value.

### Built-in functions¶

These functions are applied to each individual pixel.

abs(_image_)

    

Absolute value.

convert(_image_ , _mode_)

    

Convert image to the given mode. The mode must be given as a string constant.

float(_image_)

    

Convert image to 32-bit floating point. This is equivalent to convert(image,
“F”).

int(_image_)

    

Convert image to 32-bit integer. This is equivalent to convert(image, “I”).

Note that 1-bit and 8-bit images are automatically converted to 32-bit
integers if necessary to get a correct result.

max(_image1_ , _image2_)

    

Maximum value.

min(_image1_ , _image2_)

    

Minimum value.

[ Next `ImageMorph` module ](ImageMorph.html) [ Previous `ImageGrab` module
](ImageGrab.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageMath` module
    * Example: Using the `ImageMath` module
      * `lambda_eval()`
      * `unsafe_eval()`
    * Expression syntax
      * Standard operators
      * Bitwise operators
      * Logical operators
      * Built-in functions

