# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageMorph.html
# Path: reference/ImageMorph.html

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
    * `ImageMorph` module
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

[ View this page ](../_sources/reference/ImageMorph.rst.txt "View this page")

# `ImageMorph` module¶

The `ImageMorph` module allows
[morphology](https://en.wikipedia.org/wiki/Mathematical_morphology) operators
(“MorphOp”) to be applied to L mode images:

    
    
    from PIL import Image, ImageMorph
    img = Image.open("Tests/images/hopper.bw")
    mop = ImageMorph.MorphOp(op_name="erosion4")
    count, imgOut = mop.apply(img)
    imgOut.show()
    

In addition to applying operators, you can also analyse images.

You can inspect an image in isolation to determine which pixels are non-empty:

    
    
    print(mop.get_on_pixels(img))  # [(0, 0), (1, 0), (2, 0), ...]
    

Or you can retrieve a list of pixels that match the operator. This is the
number of pixels that will be non-empty after the operator is applied:

    
    
    coords = mop.match(img)
    print(coords)  # [(17, 1), (18, 1), (34, 1), ...]
    print(len(coords))  # 550
    
    imgOut = mop.apply(img)[1]
    print(len(mop.get_on_pixels(imgOut)))  # 550
    

If you would like more customized operators, you can pass patterns to the
MorphOp class:

    
    
    mop = ImageMorph.MorphOp(patterns=["1:(... ... ...)->0", "4:(00. 01. ...)->1"])
    

Or you can pass lookup table (“LUT”) data directly. This LUT data can be
constructed with the `LutBuilder`:

    
    
    builder = ImageMorph.LutBuilder()
    mop = ImageMorph.MorphOp(lut=builder.build_lut())
    

class PIL.ImageMorph.LutBuilder(_patterns : [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _op_name : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/ImageMorph.html#LutBuilder)¶
    

Bases: [`object`](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.14\)")

A class for building a MorphLut from a descriptive language

The input patterns is a list of a strings sequences like these:

    
    
    4:(...
       .1.
       111)->1
    

(whitespaces including linebreaks are ignored). The option 4 describes a
series of symmetry operations (in this case a 4-rotation), the pattern is
described by:

  * . or X - Ignore

  * 1 - Pixel is on

  * 0 - Pixel is off

The result of the operation is described after “->” string.

The default is to return the current pixel value, which is returned if no
other match is found.

Operations:

  * 4 - 4 way rotation

  * N - Negate

  * 1 - Dummy op for no other operation (an op must always be given)

  * M - Mirroring

Example:

    
    
    lb = LutBuilder(patterns = ["4:(... .1. 111)->1"])
    lut = lb.build_lut()
    

add_patterns(_patterns :
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)")]_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageMorph.html#LutBuilder.add_patterns)¶

    

Append to list of patterns.

Parameters:

    

**patterns** – Additional patterns.

build_default_lut() ->
[bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "\(in
Python
v3.14\)")[[source]](../_modules/PIL/ImageMorph.html#LutBuilder.build_default_lut)¶

    

Set the current LUT, and return it.

This is the default LUT that patterns will be applied against when building.

build_lut() ->
[bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "\(in
Python
v3.14\)")[[source]](../_modules/PIL/ImageMorph.html#LutBuilder.build_lut)¶

    

Compile all patterns into a morphology LUT, and return it.

This is the data to be passed into MorphOp.

get_lut() -> [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageMorph.html#LutBuilder.get_lut)¶
    

Returns the current LUT

class PIL.ImageMorph.MorphOp(_lut : [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _op_name : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _patterns : [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/ImageMorph.html#MorphOp)¶
    

Bases: [`object`](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.14\)")

A class for binary morphological operators

apply(_image : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")][[source]](../_modules/PIL/ImageMorph.html#MorphOp.apply)¶

    

Run a single morphological operation on an image.

Returns a tuple of the number of changed pixels and the morphed image.

Raises:

    

  * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "\(in Python v3.14\)") – If the current operator is None.

  * [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "\(in Python v3.14\)") – If the image is not L mode.

get_on_pixels(_image : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_)
-> [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in
Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]][[source]](../_modules/PIL/ImageMorph.html#MorphOp.get_on_pixels)¶

    

Get a list of all turned on pixels in a grayscale image

Returns a list of tuples of (x,y) coordinates of all non-empty pixels. See
[Coordinate system](../handbook/concepts.html#coordinate-system).

Parameters:

    

**image** – An L-mode image.

Raises:

    

[**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError
"\(in Python v3.14\)") – If the image is not L mode.

load_lut(_filename : [str](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageMorph.html#MorphOp.load_lut)¶

    

Load an operator from an mrl file

Parameters:

    

**filename** – The file to read from.

Raises:

    

[**Exception**](https://docs.python.org/3/library/exceptions.html#Exception
"\(in Python v3.14\)") – If the length of the file data is not 512.

match(_image : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_) ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in
Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]][[source]](../_modules/PIL/ImageMorph.html#MorphOp.match)¶

    

Get a list of coordinates matching the morphological operation on an image.

Returns a list of tuples of (x,y) coordinates of all matching pixels. See
[Coordinate system](../handbook/concepts.html#coordinate-system).

Parameters:

    

**image** – An L-mode image.

Raises:

    

  * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "\(in Python v3.14\)") – If the current operator is None.

  * [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "\(in Python v3.14\)") – If the image is not L mode.

save_lut(_filename : [str](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageMorph.html#MorphOp.save_lut)¶

    

Save an operator to an mrl file.

Parameters:

    

**filename** – The destination file.

Raises:

    

[**Exception**](https://docs.python.org/3/library/exceptions.html#Exception
"\(in Python v3.14\)") – If the current operator is None.

set_lut(_lut : [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageMorph.html#MorphOp.set_lut)¶
    

Set the LUT from an external source

Parameters:

    

**lut** – A new LUT.

[ Next `ImageOps` module ](ImageOps.html) [ Previous `ImageMath` module
](ImageMath.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageMorph` module
    * `LutBuilder`
      * `LutBuilder.add_patterns()`
      * `LutBuilder.build_default_lut()`
      * `LutBuilder.build_lut()`
      * `LutBuilder.get_lut()`
    * `MorphOp`
      * `MorphOp.apply()`
      * `MorphOp.get_on_pixels()`
      * `MorphOp.load_lut()`
      * `MorphOp.match()`
      * `MorphOp.save_lut()`
      * `MorphOp.set_lut()`

