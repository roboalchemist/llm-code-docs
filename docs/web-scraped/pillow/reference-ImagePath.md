# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImagePath.html
# Path: reference/ImagePath.html

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
    * `ImagePath` module
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

[ View this page ](../_sources/reference/ImagePath.rst.txt "View this page")

# `ImagePath` module¶

The `ImagePath` module is used to store and manipulate 2-dimensional vector
data. Path objects can be passed to the methods on the
[`ImageDraw`](ImageDraw.html#module-PIL.ImageDraw "PIL.ImageDraw") module.

class PIL.ImagePath.Path¶

    

A path object. The coordinate list can be any sequence object containing
either 2-tuples [(x, y), …] or numeric values [x, y, …].

You can also create a path object from another path object.

In 1.1.6 and later, you can also pass in any object that implements Python’s
buffer API. The buffer should provide read access, and contain C floats in
machine byte order.

The path object implements most parts of the Python sequence interface, and
behaves like a list of (x, y) pairs. You can use len(), item access, and
slicing as usual. However, this does not support slice assignment, or item and
slice deletion.

Parameters:

    

**xy** – A sequence. The sequence can contain 2-tuples [(x, y), …] or a flat
list of numbers [x, y, …].

PIL.ImagePath.Path.compact(_distance =2_)¶

    

Compacts the path, by removing points that are close to each other. This
method modifies the path in place, and returns the number of points left in
the path.

`distance` is measured as [Manhattan
distance](https://en.wikipedia.org/wiki/Manhattan_distance) and defaults to
two pixels.

PIL.ImagePath.Path.getbbox()¶

    

Gets the bounding box of the path.

Returns:

    

`(x0, y0, x1, y1)`

PIL.ImagePath.Path.map(_function_)¶

    

Maps the path through a function.

PIL.ImagePath.Path.tolist(_flat =False_)¶

    

Converts the path to a Python list [(x, y), …].

Parameters:

    

**flat** – By default, this function returns a list of 2-tuples [(x, y), …].
If this argument is `True`, it returns a flat list [x, y, …] instead.

Returns:

    

A list of coordinates. See `flat`.

PIL.ImagePath.Path.transform(_matrix_)¶

    

Transforms the path in place, using an affine transform. The matrix is a
6-tuple (a, b, c, d, e, f), and each point is mapped as follows:

    
    
    xOut = xIn * a + yIn * b + c
    yOut = xIn * d + yIn * e + f
    

[ Next `ImageQt` module ](ImageQt.html) [ Previous `ImagePalette` module
](ImagePalette.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImagePath` module
    * `PIL.ImagePath.Path`
    * `PIL.ImagePath.Path.compact()`
    * `PIL.ImagePath.Path.getbbox()`
    * `PIL.ImagePath.Path.map()`
    * `PIL.ImagePath.Path.tolist()`
    * `PIL.ImagePath.Path.transform()`

