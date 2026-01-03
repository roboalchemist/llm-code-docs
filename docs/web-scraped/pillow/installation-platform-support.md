# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/installation/platform-support.html
# Path: installation/platform-support.html

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto
light/dark, in dark mode Skip to content

[Pillow (PIL Fork) 12.1.0.dev0 documentation](../index.html)

[ ![Light Logo](../_static/pillow-logo-dark-text.png) ![Dark
Logo](../_static/pillow-logo.png) Pillow (PIL Fork) 12.1.0.dev0 documentation
](../index.html)

  * [Installation](index.html)
    * [Basic installation](basic-installation.html)
    * [Python support](python-support.html)
    * Platform support
    * [Building from source](building-from-source.html)
    * [Old versions](building-from-source.html#old-versions)
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

[ View this page ](../_sources/installation/platform-support.rst.txt "View
this page")

# Platform support¶

Current platform support for Pillow. Binary distributions are contributed for
each release on a volunteer basis, but the source should compile and run
everywhere platform support is listed. In general, we aim to support all
current versions of Linux, macOS, and Windows.

## Continuous integration targets¶

These platforms are built and tested for every change.

Operating system | Tested Python versions | Tested architecture  
---|---|---  
Alpine | 3.12 | x86-64  
Amazon Linux 2 | 3.10 | x86-64  
Amazon Linux 2023 | 3.11 | x86-64  
Arch | 3.13 | x86-64  
CentOS Stream 9 | 3.10 | x86-64  
CentOS Stream 10 | 3.12 | x86-64  
Debian 12 Bookworm | 3.11 | x86, x86-64  
Debian 13 Trixie | 3.13 | x86, x86-64  
Fedora 42 | 3.13 | x86-64  
Fedora 43 | 3.14 | x86-64  
Gentoo | 3.12 | x86-64  
macOS 15 Sequoia | 3.10 | x86-64  
3.11, 3.12, 3.13, 3.14, PyPy3 | arm64  
Ubuntu Linux 22.04 LTS (Jammy) | 3.10 | x86-64  
Ubuntu Linux 24.04 LTS (Noble) | 3.10, 3.11, 3.12, 3.13, 3.14, PyPy3 | x86-64  
3.12 | arm64v8, ppc64le, s390x  
Windows Server 2022 | 3.10 | x86  
Windows Server 2025 | 3.11, 3.12, 3.13, 3.14, PyPy3 | x86-64  
3.12 (MinGW) | x86-64  
  
## Other platforms¶

These platforms have been reported to work at the versions mentioned.

Note

Contributors please test Pillow on your platform then update this document and
send a pull request.

Operating system |  Tested Python versions |  Latest tested Pillow version |  Tested processors  
---|---|---|---  
macOS 26 Tahoe | 3.10, 3.11, 3.12, 3.13, 3.14 | 12.0.0 | arm  
3.9 | 11.3.0  
macOS 15 Sequoia | 3.9, 3.10, 3.11, 3.12, 3.13 | 11.3.0 | arm  
3.8 | 10.4.0  
macOS 14 Sonoma | 3.8, 3.9, 3.10, 3.11, 3.12 | 10.4.0 | arm  
macOS 13 Ventura | 3.8, 3.9, 3.10, 3.11 | 10.0.1 | arm  
3.7 | 9.5.0  
macOS 12 Monterey | 3.7, 3.8, 3.9, 3.10, 3.11 | 9.3.0 | arm  
macOS 11 Big Sur | 3.7, 3.8, 3.9, 3.10 | 8.4.0 | arm  
3.7, 3.8, 3.9, 3.10, 3.11 | 9.4.0 | x86-64  
3.6 | 8.4.0  
macOS 10.15 Catalina | 3.6, 3.7, 3.8, 3.9 | 8.3.2 | x86-64  
3.5 | 7.2.0  
macOS 10.14 Mojave | 3.5, 3.6, 3.7, 3.8 | 7.2.0 | x86-64  
2.7 | 6.0.0  
3.4 | 5.4.1  
macOS 10.13 High Sierra | 2.7, 3.4, 3.5, 3.6 | 4.2.1 | x86-64  
macOS 10.12 Sierra | 2.7, 3.4, 3.5, 3.6 | 4.1.1 | x86-64  
Mac OS X 10.11 El Capitan | 2.7, 3.4, 3.5, 3.6, 3.7 | 5.4.1 | x86-64  
3.3 | 4.1.0  
Mac OS X 10.9 Mavericks | 2.7, 3.2, 3.3, 3.4 | 3.0.0 | x86-64  
Mac OS X 10.8 Mountain Lion | 2.6, 2.7, 3.2, 3.3 |  | x86-64  
Redhat Linux 6 | 2.6 |  | x86  
CentOS 6.3 | 2.7, 3.3 |  | x86  
CentOS 8 | 3.9 | 9.0.0 | x86-64  
Fedora 23 | 2.7, 3.4 | 3.1.0 | x86-64  
Ubuntu Linux 12.04 LTS (Precise) |  2.6, 3.2, 3.3, 3.4, 3.5 PyPy5.3.1, PyPy3 v2.4.0 | 3.4.1 | x86,x86-64  
2.7 | 4.3.0 | x86-64  
2.7, 3.2 | 3.4.1 | ppc  
Ubuntu Linux 10.04 LTS (Lucid) | 2.6 | 2.3.0 | x86,x86-64  
Debian 8.2 Jessie | 2.7, 3.4 | 3.1.0 | x86-64  
Raspbian Jessie | 2.7, 3.4 | 3.1.0 | arm  
Raspbian Stretch | 2.7, 3.5 | 4.0.0 | arm  
Raspberry Pi OS | 3.6, 3.7, 3.8, 3.9 | 8.2.0 | arm  
2.7 | 6.2.2  
Gentoo Linux | 2.7, 3.2 | 2.1.0 | x86-64  
FreeBSD 11.1 | 2.7, 3.4, 3.5, 3.6 | 4.3.0 | x86-64  
FreeBSD 10.3 | 2.7, 3.4, 3.5 | 4.2.0 | x86-64  
FreeBSD 10.2 | 2.7, 3.4 | 3.1.0 | x86-64  
Windows 11 23H2 | 3.9, 3.10, 3.11, 3.12, 3.13 | 11.0.0 | arm64  
Windows 11 Pro | 3.11, 3.12 | 10.2.0 | x86-64  
Windows 10 | 3.7 | 7.1.0 | x86-64  
Windows 10/Cygwin 3.3 | 3.6, 3.7, 3.8, 3.9 | 8.4.0 | x86-64  
Windows 8.1 Pro | 2.6, 2.7, 3.2, 3.3, 3.4 | 2.4.0 | x86,x86-64  
Windows 8 Pro | 2.6, 2.7, 3.2, 3.3, 3.4a3 | 2.2.0 | x86,x86-64  
Windows 7 Professional | 3.7 | 7.0.0 | x86,x86-64  
Windows Server 2008 R2 Enterprise | 3.3 |  | x86-64  
  
[ Next Building from source ](building-from-source.html) [ Previous Python
support ](python-support.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * Platform support
    * Continuous integration targets
    * Other platforms

