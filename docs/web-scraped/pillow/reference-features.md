# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/features.html
# Path: reference/features.html

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
    * [`ImageTransform` module](ImageTransform.html)
    * [`ImageWin` module (Windows-only)](ImageWin.html)
    * [`ExifTags` module](ExifTags.html)
    * [`TiffTags` module](TiffTags.html)
    * [`JpegPresets` module](JpegPresets.html)
    * [`PSDraw` module](PSDraw.html)
    * [`PixelAccess` class](PixelAccess.html)
    * `features` module
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

[ View this page ](../_sources/reference/features.rst.txt "View this page")

# `features` module¶

The `PIL.features` module can be used to detect which Pillow features are
available on your system.

PIL.features.pilinfo(_out : [IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _supported_formats : [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = True_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/features.html#pilinfo)¶
    

Prints information about this installation of Pillow. This function can be
called with `python3 -m PIL`. It can also be called with `python3 -m
PIL.report` or `python3 -m PIL --report` to have “supported_formats” set to
`False`, omitting the list of all supported image file formats.

Parameters:

    

  * **out** – The output stream to print to. Defaults to `sys.stdout` if `None`.

  * **supported_formats** – If `True`, a list of all supported image file formats will be printed.

PIL.features.check(_feature : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_) -> [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/features.html#check)¶
    

Parameters:

    

**feature** – A module, codec, or feature name.

Returns:

    

`True` if the module, codec, or feature is available, `False` or `None`
otherwise.

PIL.features.version(_feature : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/features.html#version)¶
    

Parameters:

    

**feature** – The module, codec, or feature to check for.

Returns:

    

The version number as a string, or `None` if unknown or not available.

PIL.features.get_supported() ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)")][[source]](../_modules/PIL/features.html#get_supported)¶

    

Returns:

    

A list of all supported modules, features, and codecs.

## Modules¶

Support for the following modules can be checked:

  * `pil`: The Pillow core module, required for all functionality.

  * `tkinter`: Tkinter support.

  * `freetype2`: FreeType font support via [`PIL.ImageFont.truetype()`](ImageFont.html#PIL.ImageFont.truetype "PIL.ImageFont.truetype").

  * `littlecms2`: LittleCMS 2 support via [`PIL.ImageCms`](ImageCms.html#module-PIL.ImageCms "PIL.ImageCms").

  * `webp`: WebP image support.

  * `avif`: AVIF image support.

PIL.features.check_module(_feature :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_) -> [bool](https://docs.python.org/3/library/functions.html#bool
"\(in Python v3.14\)")[[source]](../_modules/PIL/features.html#check_module)¶

    

Checks if a module is available.

Parameters:

    

**feature** – The module to check for.

Returns:

    

`True` if available, `False` otherwise.

Raises:

    

[**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError
"\(in Python v3.14\)") – If the module is not defined in this version of
Pillow.

PIL.features.version_module(_feature : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/features.html#version_module)¶
    

Parameters:

    

**feature** – The module to check for.

Returns:

    

The loaded version number as a string, or `None` if unknown or not available.

Raises:

    

[**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError
"\(in Python v3.14\)") – If the module is not defined in this version of
Pillow.

PIL.features.get_supported_modules() ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python
v3.14\)")][[source]](../_modules/PIL/features.html#get_supported_modules)¶

    

Returns:

    

A list of all supported modules.

## Codecs¶

Support for these is only checked during Pillow compilation. If the required
library was uninstalled from the system, the `pil` core module may fail to
load instead. Except for `jpg`, the version number is checked at run-time.

Support for the following codecs can be checked:

  * `jpg`: (compile time) Libjpeg support, required for JPEG based image formats. Only compile time version number is available.

  * `jpg_2000`: (compile time) OpenJPEG support, required for JPEG 2000 image formats.

  * `zlib`: (compile time) Zlib support, required for zlib compressed formats, such as PNG.

  * `libtiff`: (compile time) LibTIFF support, required for TIFF based image formats.

PIL.features.check_codec(_feature :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_) -> [bool](https://docs.python.org/3/library/functions.html#bool
"\(in Python v3.14\)")[[source]](../_modules/PIL/features.html#check_codec)¶

    

Checks if a codec is available.

Parameters:

    

**feature** – The codec to check for.

Returns:

    

`True` if available, `False` otherwise.

Raises:

    

[**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError
"\(in Python v3.14\)") – If the codec is not defined in this version of
Pillow.

PIL.features.version_codec(_feature : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/features.html#version_codec)¶
    

Parameters:

    

**feature** – The codec to check for.

Returns:

    

The version number as a string, or `None` if not available. Checked at compile
time for `jpg`, run-time otherwise.

Raises:

    

[**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError
"\(in Python v3.14\)") – If the codec is not defined in this version of
Pillow.

PIL.features.get_supported_codecs() ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python
v3.14\)")][[source]](../_modules/PIL/features.html#get_supported_codecs)¶

    

Returns:

    

A list of all supported codecs.

## Features¶

Some of these are only checked during Pillow compilation. If the required
library was uninstalled from the system, the relevant module may fail to load
instead. Feature version numbers are available only where stated.

Support for the following features can be checked:

  * `libjpeg_turbo`: (compile time) Whether Pillow was compiled against the libjpeg-turbo version of libjpeg. Compile-time version number is available.

  * `mozjpeg`: (compile time) Whether Pillow was compiled against the MozJPEG version of libjpeg. Compile-time version number is available.

  * `zlib_ng`: (compile time) Whether Pillow was compiled against the zlib-ng version of zlib. Compile-time version number is available.

  * `raqm`: Raqm library, required for `ImageFont.Layout.RAQM` in [`PIL.ImageFont.truetype()`](ImageFont.html#PIL.ImageFont.truetype "PIL.ImageFont.truetype"). Run-time version number is available for Raqm 0.7.0 or newer.

  * `libimagequant`: (compile time) ImageQuant quantization support in [`PIL.Image.Image.quantize()`](Image.html#PIL.Image.Image.quantize "PIL.Image.Image.quantize"). Run-time version number is available.

  * `xcb`: (compile time) Support for X11 in [`PIL.ImageGrab.grab()`](ImageGrab.html#PIL.ImageGrab.grab "PIL.ImageGrab.grab") via the XCB library.

PIL.features.check_feature(_feature : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_) -> [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/features.html#check_feature)¶
    

Checks if a feature is available.

Parameters:

    

**feature** – The feature to check for.

Returns:

    

`True` if available, `False` if unavailable, `None` if unknown.

Raises:

    

[**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError
"\(in Python v3.14\)") – If the feature is not defined in this version of
Pillow.

PIL.features.version_feature(_feature : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/features.html#version_feature)¶
    

Parameters:

    

**feature** – The feature to check for.

Returns:

    

The version number as a string, or `None` if not available.

Raises:

    

[**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError
"\(in Python v3.14\)") – If the feature is not defined in this version of
Pillow.

PIL.features.get_supported_features() ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python
v3.14\)")][[source]](../_modules/PIL/features.html#get_supported_features)¶

    

Returns:

    

A list of all supported features.

[ Next PIL package (autodoc of remaining modules) ](../PIL.html) [ Previous
`PixelAccess` class ](PixelAccess.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `features` module
    * `pilinfo()`
    * `check()`
    * `version()`
    * `get_supported()`
    * Modules
      * `check_module()`
      * `version_module()`
      * `get_supported_modules()`
    * Codecs
      * `check_codec()`
      * `version_codec()`
      * `get_supported_codecs()`
    * Features
      * `check_feature()`
      * `version_feature()`
      * `get_supported_features()`

