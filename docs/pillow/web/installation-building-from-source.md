# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/installation/building-from-source.html
# Path: installation/building-from-source.html

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto
light/dark, in dark mode Skip to content

[Pillow (PIL Fork) 12.1.0.dev0 documentation](../index.html)

[ ![Light Logo](../_static/pillow-logo-dark-text.png) ![Dark
Logo](../_static/pillow-logo.png) Pillow (PIL Fork) 12.1.0.dev0 documentation
](../index.html)

  * [Installation](index.html)
    * [Basic installation](basic-installation.html)
    * [Python support](python-support.html)
    * [Platform support](platform-support.html)
    * Building from source
    * Old versions
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

[ View this page ](../_sources/installation/building-from-source.rst.txt "View
this page")

# Building from source¶

## External libraries¶

Note

You **do not need to install all supported external libraries** to use
Pillow’s basic features. **Zlib** and **libjpeg** are required by default.

Note

There are Dockerfiles in our [Docker images repo](https://github.com/python-
pillow/docker-images) to install the dependencies for some operating systems.

Many of Pillow’s features require external libraries:

  * **libjpeg** provides JPEG functionality.

    * Pillow has been tested with libjpeg versions **6b** , **8** , **9-9d** and libjpeg-turbo version **8**.

    * Starting with Pillow 3.0.0, libjpeg is required by default. It can be disabled with the `-C jpeg=disable` flag.

  * **zlib** provides access to compressed PNGs

    * Starting with Pillow 3.0.0, zlib is required by default. It can be disabled with the `-C zlib=disable` flag.

  * **libtiff** provides compressed TIFF functionality

    * Pillow has been tested with libtiff versions **4.0-4.7.1**

  * **libfreetype** provides type related services

  * **littlecms** provides color management

    * Pillow version 2.2.1 and below uses liblcms1, Pillow 2.3.0 and above uses liblcms2. Tested with **1.19** and **2.7-2.17**.

  * **libwebp** provides the WebP format.

  * **openjpeg** provides JPEG 2000 functionality.

    * Pillow has been tested with openjpeg **2.0.0** , **2.1.0** , **2.3.1** , **2.4.0** , **2.5.0** , **2.5.2** , **2.5.3** and **2.5.4**.

    * Pillow does **not** support the earlier **1.5** series which ships with Debian Jessie.

  * **libimagequant** provides improved color quantization

    * Pillow has been tested with libimagequant **2.6-4.4.1**

    * Libimagequant is licensed GPLv3, which is more restrictive than the Pillow license, therefore we will not be distributing binaries with libimagequant support enabled.

  * **libraqm** provides complex text layout support.

    * libraqm provides bidirectional text support (using FriBiDi), shaping (using HarfBuzz), and proper script itemization. As a result, Raqm can support most writing systems covered by Unicode.

    * libraqm depends on the following libraries: FreeType, HarfBuzz, FriBiDi, make sure that you install them before installing libraqm if not available as package in your system.

    * Setting text direction or font features is not supported without libraqm.

    * Pillow wheels since version 8.2.0 include a modified version of libraqm that loads libfribidi at runtime if it is installed. On Windows this requires compiling FriBiDi and installing `fribidi.dll` into a directory listed in the [Dynamic-link library search order (Microsoft Learn)](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order#search-order-for-unpackaged-apps) (`fribidi-0.dll` or `libfribidi-0.dll` are also detected). See Build Options to see how to build this version.

    * Previous versions of Pillow (5.0.0 to 8.1.2) linked libraqm dynamically at runtime.

  * **libxcb** provides X11 screengrab support.

  * **libavif** provides support for the AVIF format.

    * Pillow requires libavif version **1.0.0** or greater.

    * libavif is merely an API that wraps AVIF codecs. If you are compiling libavif from source, you will also need to install both an AVIF encoder and decoder, such as rav1e and dav1d, or libaom, which both encodes and decodes AVIF images.

Linux

If you didn’t build Python from source, make sure you have Python’s
development libraries installed.

In Debian or Ubuntu:

    
    
    sudo apt-get install python3-dev python3-setuptools
    

In Fedora, the command is:

    
    
    sudo dnf install python3-devel redhat-rpm-config
    

In Alpine, the command is:

    
    
    sudo apk add python3-dev py3-setuptools
    

Note

`redhat-rpm-config` is required on Fedora 23, but not earlier versions.

Prerequisites for **Ubuntu 16.04 LTS - 24.04 LTS** are installed with:

    
    
    sudo apt-get install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
        libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
        libharfbuzz-dev libfribidi-dev libxcb1-dev
    

To install libraqm, `sudo apt-get install meson` and then see
`depends/install_raqm.sh`.

Build prerequisites for libavif on Ubuntu are installed with:

    
    
    sudo apt-get install cmake ninja-build nasm
    

Then see `depends/install_libavif.sh` to build and install libavif.

Prerequisites are installed on recent **Red Hat** , **CentOS** or **Fedora**
with:

    
    
    sudo dnf install libtiff-devel libjpeg-devel openjpeg2-devel zlib-devel \
        freetype-devel lcms2-devel libwebp-devel tcl-devel tk-devel \
        harfbuzz-devel fribidi-devel libraqm-devel libimagequant-devel libxcb-devel
    

Note that the package manager may be yum or DNF, depending on the exact
distribution.

Prerequisites are installed for **Alpine** with:

    
    
    sudo apk add tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
        libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
        libxcb-dev libpng-dev
    

See also the `Dockerfile`s in the Test Infrastructure repo
(<https://github.com/python-pillow/docker-images>) for a known working install
process for other tested distros.

macOS

The Xcode command line tools are required to compile portions of Pillow. The
tools are installed by running `xcode-select --install` from the command line.
The command line tools are required even if you have the full Xcode package
installed. It may be necessary to run `sudo xcodebuild -license` to accept the
license prior to using the tools.

The easiest way to install external libraries is via
[Homebrew](https://brew.sh/). After you install Homebrew, run:

    
    
    brew install libavif libjpeg libraqm libtiff little-cms2 openjpeg webp
    

If you would like to use libavif with more codecs than just aom, then instead
of installing libavif through Homebrew directly, you can use Homebrew to
install libavif’s build dependencies:

    
    
    brew install aom dav1d rav1e svt-av1
    

Then see `depends/install_libavif.sh` to install libavif.

Windows

We recommend you use prebuilt wheels from PyPI. If you wish to compile Pillow
manually, you can use the build scripts in the `winbuild` directory used for
CI testing and development. These scripts require Visual Studio 2017 or newer
and NASM.

The scripts also install Pillow from the local copy of the source code, so the
Installing instructions will not be necessary afterwards.

Windows using MSYS2/MinGW

To build Pillow using MSYS2, make sure you run the **MSYS2 MinGW 32-bit** or
**MSYS2 MinGW 64-bit** console, _not_ **MSYS2** directly.

The following instructions target the 64-bit build, for 32-bit replace all
occurrences of `mingw-w64-x86_64-` with `mingw-w64-i686-`.

Make sure you have Python and GCC installed:

    
    
    pacman -S \
        mingw-w64-x86_64-gcc \
        mingw-w64-x86_64-python \
        mingw-w64-x86_64-python-pip \
        mingw-w64-x86_64-python-setuptools
    

Prerequisites are installed on **MSYS2 MinGW 64-bit** with:

    
    
    pacman -S \
        mingw-w64-x86_64-libjpeg-turbo \
        mingw-w64-x86_64-zlib \
        mingw-w64-x86_64-libtiff \
        mingw-w64-x86_64-freetype \
        mingw-w64-x86_64-lcms2 \
        mingw-w64-x86_64-libwebp \
        mingw-w64-x86_64-openjpeg2 \
        mingw-w64-x86_64-libimagequant \
        mingw-w64-x86_64-libraqm \
        mingw-w64-x86_64-libavif
    

FreeBSD

Note

Only FreeBSD 10 and 11 tested

Make sure you have Python’s development libraries installed:

    
    
    sudo pkg install python3
    

Prerequisites are installed on **FreeBSD 10 or 11** with:

    
    
    sudo pkg install jpeg-turbo tiff webp lcms2 freetype2 openjpeg harfbuzz fribidi libxcb libavif
    

Then see `depends/install_raqm_cmake.sh` to install libraqm.

Android

Basic Android support has been added for compilation within the Termux
environment. The dependencies can be installed by:

    
    
    pkg install -y python ndk-sysroot clang make \
        libjpeg-turbo
    

This has been tested within the Termux app on ChromeOS, on x86.

## Installing¶

Once you have installed the prerequisites, to install Pillow from the source
code on PyPI, run:

    
    
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade Pillow --no-binary :all:
    

If the prerequisites are installed in the standard library locations for your
machine (e.g. `/usr` or `/usr/local`), no additional configuration should be
required. If they are installed in a non-standard location, you may need to
configure setuptools to use those locations by editing `setup.py` or
`pyproject.toml`, or by adding environment variables on the command line:

    
    
    CFLAGS="-I/usr/pkg/include" python3 -m pip install --upgrade Pillow --no-binary :all:
    

If Pillow has been previously built without the required prerequisites, it may
be necessary to manually clear the pip cache or build without cache using the
`--no-cache-dir` option to force a build with newly installed external
libraries.

If you would like to install from a local copy of the source code instead, you
can clone from GitHub with `git clone https://github.com/python-pillow/Pillow`
or download and extract the [compressed archive from
PyPI](https://pypi.org/project/pillow/#files).

After navigating to the Pillow directory, run:

    
    
    python3 -m pip install --upgrade pip
    python3 -m pip install .
    

### Build options¶

  * Config setting: `-C parallel=n`. Can also be given with environment variable: `MAX_CONCURRENCY=n`. Pillow can use multiprocessing to build the extensions. Setting `-C parallel=n` sets the number of CPUs to use to `n`, or can disable parallel building by using a setting of 1. By default, it uses as many CPUs as are present.

  * Config settings: `-C zlib=disable`, `-C jpeg=disable`, `-C tiff=disable`, `-C freetype=disable`, `-C raqm=disable`, `-C lcms=disable`, `-C webp=disable`, `-C jpeg2000=disable`, `-C imagequant=disable`, `-C xcb=disable`, `-C avif=disable`. Disable building the corresponding feature even if the development libraries are present on the building machine.

  * Config settings: `-C zlib=enable`, `-C jpeg=enable`, `-C tiff=enable`, `-C freetype=enable`, `-C raqm=enable`, `-C lcms=enable`, `-C webp=enable`, `-C jpeg2000=enable`, `-C imagequant=enable`, `-C xcb=enable`, `-C avif=enable`. Require that the corresponding feature is built. The build will raise an exception if the libraries are not found. Tcl and Tk must be used together.

  * Config settings: `-C raqm=vendor`, `-C fribidi=vendor`. These flags are used to compile a modified version of libraqm and a shim that dynamically loads libfribidi at runtime. These are used to compile the standard Pillow wheels. Compiling libraqm requires a C99-compliant compiler.

  * Config setting: `-C platform-guessing=disable`. Skips all of the platform dependent guessing of include and library directories for automated build systems that configure the proper paths in the environment variables (e.g. Buildroot).

  * Config setting: `-C debug=true`. Adds a debugging flag to the include and library search process to dump all paths searched for and found to stdout.

Sample usage:

    
    
    python3 -m pip install --upgrade Pillow -C [feature]=enable
    

# Old versions¶

You can download old distributions from the [release history at
PyPI](https://pypi.org/project/pillow/#history) and by direct URL access eg.
<https://pypi.org/project/pillow/1.0/>.

[ Next Handbook ](../handbook/index.html) [ Previous Platform support
](platform-support.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * Building from source
    * External libraries
    * Installing
      * Build options
  * Old versions

