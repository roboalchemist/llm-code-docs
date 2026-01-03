# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageTransform.html
# Path: reference/ImageTransform.html

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
    * [`ImageOps` module](ImageOps.html)
    * [`ImagePalette` module](ImagePalette.html)
    * [`ImagePath` module](ImagePath.html)
    * [`ImageQt` module](ImageQt.html)
    * [`ImageSequence` module](ImageSequence.html)
    * [`ImageShow` module](ImageShow.html)
    * [`ImageStat` module](ImageStat.html)
    * [`ImageText` module](ImageText.html)
    * [`ImageTk` module](ImageTk.html)
    * `ImageTransform` module
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

[ View this page ](../_sources/reference/ImageTransform.rst.txt "View this
page")

# `ImageTransform` module¶

The `ImageTransform` module contains implementations of
[`ImageTransformHandler`](Image.html#PIL.Image.ImageTransformHandler
"PIL.Image.ImageTransformHandler") for some of the builtin
[`Image.Transform`](Image.html#PIL.Image.Transform "PIL.Image.Transform")
methods.

class PIL.ImageTransform.Transform(_data :
[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence
"\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.14\)")]_)[[source]](../_modules/PIL/ImageTransform.html#Transform)¶

    

Bases: [`ImageTransformHandler`](Image.html#PIL.Image.ImageTransformHandler
"PIL.Image.ImageTransformHandler")

Base class for other transforms defined in `ImageTransform`.

getdata() -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple
"\(in Python v3.14\)")[[Transform](Image.html#PIL.Image.Transform
"PIL.Image.Transform"),
[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence
"\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")]][[source]](../_modules/PIL/ImageTransform.html#Transform.getdata)¶

    

method: [Transform](Image.html#PIL.Image.Transform "PIL.Image.Transform")¶

    

transform(_size :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]_, _image : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _** options:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageTransform.html#Transform.transform)¶

    

Perform the transform. Called from
[`Image.transform()`](Image.html#PIL.Image.Image.transform
"PIL.Image.Image.transform").

class PIL.ImageTransform.AffineTransform(_data :
[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence
"\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python
v3.14\)")]_)[[source]](../_modules/PIL/ImageTransform.html#AffineTransform)¶

    

Bases: `Transform`

Define an affine image transform.

This function takes a 6-tuple (a, b, c, d, e, f) which contain the first two
rows from the inverse of an affine transform matrix. For each pixel (x, y) in
the output image, the new value is taken from a position (a x + b y + c, d x +
e y + f) in the input image, rounded to nearest pixel.

This function can be used to scale, translate, rotate, and shear the original
image.

See [`Image.transform()`](Image.html#PIL.Image.Image.transform
"PIL.Image.Image.transform")

Parameters:

    

**matrix** – A 6-tuple (a, b, c, d, e, f) containing the first two rows from
the inverse of an affine transform matrix.

method: [Transform](Image.html#PIL.Image.Transform "PIL.Image.Transform") = 0¶

    

class PIL.ImageTransform.PerspectiveTransform(_data :
[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence
"\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python
v3.14\)")]_)[[source]](../_modules/PIL/ImageTransform.html#PerspectiveTransform)¶

    

Bases: `Transform`

Define a perspective image transform.

This function takes an 8-tuple (a, b, c, d, e, f, g, h). For each pixel (x, y)
in the output image, the new value is taken from a position ((a x + b y + c) /
(g x + h y + 1), (d x + e y + f) / (g x + h y + 1)) in the input image,
rounded to nearest pixel.

This function can be used to scale, translate, rotate, and shear the original
image.

See [`Image.transform()`](Image.html#PIL.Image.Image.transform
"PIL.Image.Image.transform")

Parameters:

    

**matrix** – An 8-tuple (a, b, c, d, e, f, g, h).

method: [Transform](Image.html#PIL.Image.Transform "PIL.Image.Transform") = 2¶

    

class PIL.ImageTransform.ExtentTransform(_data :
[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence
"\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python
v3.14\)")]_)[[source]](../_modules/PIL/ImageTransform.html#ExtentTransform)¶

    

Bases: `Transform`

Define a transform to extract a subregion from an image.

Maps a rectangle (defined by two corners) from the image to a rectangle of the
given size. The resulting image will contain data sampled from between the
corners, such that (x0, y0) in the input image will end up at (0,0) in the
output image, and (x1, y1) at size.

This method can be used to crop, stretch, shrink, or mirror an arbitrary
rectangle in the current image. It is slightly slower than crop, but about as
fast as a corresponding resize operation.

See [`Image.transform()`](Image.html#PIL.Image.Image.transform
"PIL.Image.Image.transform")

Parameters:

    

**bbox** – A 4-tuple (x0, y0, x1, y1) which specifies two points in the input
image’s coordinate system. See [Coordinate
system](../handbook/concepts.html#coordinate-system).

method: [Transform](Image.html#PIL.Image.Transform "PIL.Image.Transform") = 1¶

    

class PIL.ImageTransform.QuadTransform(_data :
[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence
"\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python
v3.14\)")]_)[[source]](../_modules/PIL/ImageTransform.html#QuadTransform)¶

    

Bases: `Transform`

Define a quad image transform.

Maps a quadrilateral (a region defined by four corners) from the image to a
rectangle of the given size.

See [`Image.transform()`](Image.html#PIL.Image.Image.transform
"PIL.Image.Image.transform")

Parameters:

    

**xy** – An 8-tuple (x0, y0, x1, y1, x2, y2, x3, y3) which contain the upper
left, lower left, lower right, and upper right corner of the source
quadrilateral.

method: [Transform](Image.html#PIL.Image.Transform "PIL.Image.Transform") = 3¶

    

class PIL.ImageTransform.MeshTransform(_data :
[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence
"\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python
v3.14\)")]_)[[source]](../_modules/PIL/ImageTransform.html#MeshTransform)¶

    

Bases: `Transform`

Define a mesh image transform. A mesh transform consists of one or more
individual quad transforms.

See [`Image.transform()`](Image.html#PIL.Image.Image.transform
"PIL.Image.Image.transform")

Parameters:

    

**data** – A list of (bbox, quad) tuples.

method: [Transform](Image.html#PIL.Image.Transform "PIL.Image.Transform") = 4¶

    

[ Next `ImageWin` module (Windows-only) ](ImageWin.html) [ Previous `ImageTk`
module ](ImageTk.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageTransform` module
    * `Transform`
      * `Transform.getdata()`
      * `Transform.method`
      * `Transform.transform()`
    * `AffineTransform`
      * `AffineTransform.method`
    * `PerspectiveTransform`
      * `PerspectiveTransform.method`
    * `ExtentTransform`
      * `ExtentTransform.method`
    * `QuadTransform`
      * `QuadTransform.method`
    * `MeshTransform`
      * `MeshTransform.method`

