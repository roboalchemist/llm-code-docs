# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/handbook/third-party-plugins.html
# Path: handbook/third-party-plugins.html

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
    * [Concepts](concepts.html)
    * [Appendices](appendices.html)
      * [Image file formats](image-file-formats.html)
      * [Text anchors](text-anchors.html)
      * Third-party plugins
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

[ View this page ](../_sources/handbook/third-party-plugins.rst.txt "View this
page")

# Third-party plugins¶

Pillow uses a plugin model which allows users to add their own decoders and
encoders to the library, without any changes to the library itself.

Here is a list of PyPI projects that offer additional plugins:

  * [DjvuRleImagePlugin](https://pypi.org/project/DjvuRleImagePlugin/): Plugin for the DjVu RLE image format as defined in the DjVuLibre docs.

  * [heif-image-plugin](https://pypi.org/project/heif-image-plugin/): Simple HEIF/HEIC images plugin, based on the pyheif library.

  * [jxlpy](https://pypi.org/project/jxlpy/): Introduces reading and writing support for JPEG XL.

  * [pillow-heif](https://pypi.org/project/pillow-heif/): Python bindings to libheif for working with HEIF images.

  * [pillow-jpls](https://pypi.org/project/pillow-jpls/): Plugin for the JPEG-LS codec, based on the Charls JPEG-LS implementation. Python bindings implemented using pybind11.

  * [pillow-jxl-plugin](https://pypi.org/project/pillow-jxl-plugin/): Plugin for JPEG-XL, using Rust for bindings.

  * [pillow-mbm](https://pypi.org/project/pillow-mbm/): Adds support for KSP’s proprietary MBM texture format.

  * [pillow-svg](https://pypi.org/project/pillow-svg/): Implements basic SVG read support. Supports basic paths, shapes, and text.

  * [raw-pillow-opener](https://pypi.org/project/raw-pillow-opener/): Simple camera raw opener, based on the rawpy library.

[ Next Writing your own image plugin ](writing-your-own-image-plugin.html) [
Previous Text anchors ](text-anchors.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

