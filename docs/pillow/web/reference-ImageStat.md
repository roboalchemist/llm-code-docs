# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageStat.html
# Path: reference/ImageStat.html

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
    * `ImageStat` module
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

[ View this page ](../_sources/reference/ImageStat.rst.txt "View this page")

# `ImageStat` module¶

The `ImageStat` module calculates global statistics for an image, or for a
region of an image.

class PIL.ImageStat.Stat(_image_or_list : [Image](Image.html#PIL.Image.Image "PIL.Image.Image") | [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]_, _mask : [Image](Image.html#PIL.Image.Image "PIL.Image.Image") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/ImageStat.html#Stat)¶
    

__init__(_image_or_list : [Image](Image.html#PIL.Image.Image "PIL.Image.Image") | [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]_, _mask : [Image](Image.html#PIL.Image.Image "PIL.Image.Image") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageStat.html#Stat.__init__)¶
    

Calculate statistics for the given image. If a mask is included, only the
regions covered by that mask are included in the statistics. You can also pass
in a previously calculated histogram.

Parameters:

    

  * **image** – 

A PIL image, or a precalculated histogram.

Note

For a PIL image, calculations rely on the
[`histogram()`](Image.html#PIL.Image.Image.histogram
"PIL.Image.Image.histogram") method. The pixel counts are grouped into 256
bins, even if the image has more than 8 bits per channel. So `I` and `F` mode
images have a maximum `mean`, `median` and `rms` of 255, and cannot have an
`extrema` maximum of more than 255.

  * **mask** – An optional mask.

property count: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")][[source]](../_modules/PIL/ImageStat.html#Stat.count)¶

    

Total number of pixels for each band in the image.

property extrema: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in
Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]][[source]](../_modules/PIL/ImageStat.html#Stat.extrema)¶

    

Min/max values for each band in the image.

Note

This relies on the [`histogram()`](Image.html#PIL.Image.Image.histogram
"PIL.Image.Image.histogram") method, and simply returns the low and high bins
used. This is correct for images with 8 bits per channel, but fails for other
modes such as `I` or `F`. Instead, use
[`getextrema()`](Image.html#PIL.Image.Image.getextrema
"PIL.Image.Image.getextrema") to return per-band extrema for the image. This
is more correct and efficient because, for non-8-bit modes, the histogram
method uses [`getextrema()`](Image.html#PIL.Image.Image.getextrema
"PIL.Image.Image.getextrema") to determine the bins used.

property mean: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.14\)")][[source]](../_modules/PIL/ImageStat.html#Stat.mean)¶

    

Average (arithmetic mean) pixel level for each band in the image.

property median: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")][[source]](../_modules/PIL/ImageStat.html#Stat.median)¶

    

Median pixel level for each band in the image.

property rms: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.14\)")][[source]](../_modules/PIL/ImageStat.html#Stat.rms)¶

    

RMS (root-mean-square) for each band in the image.

property stddev: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.14\)")][[source]](../_modules/PIL/ImageStat.html#Stat.stddev)¶

    

Standard deviation for each band in the image.

property sum: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.14\)")][[source]](../_modules/PIL/ImageStat.html#Stat.sum)¶

    

Sum of all pixels for each band in the image.

property sum2: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.14\)")][[source]](../_modules/PIL/ImageStat.html#Stat.sum2)¶

    

Squared sum of all pixels for each band in the image.

property var: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.14\)")][[source]](../_modules/PIL/ImageStat.html#Stat.var)¶

    

Variance for each band in the image.

[ Next `ImageText` module ](ImageText.html) [ Previous `ImageShow` module
](ImageShow.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageStat` module
    * `Stat`
      * `Stat.__init__()`
      * `Stat.count`
      * `Stat.extrema`
      * `Stat.mean`
      * `Stat.median`
      * `Stat.rms`
      * `Stat.stddev`
      * `Stat.sum`
      * `Stat.sum2`
      * `Stat.var`

