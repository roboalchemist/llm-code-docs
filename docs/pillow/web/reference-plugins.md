# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/plugins.html
# Path: reference/plugins.html

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
    * [`features` module](features.html)
    * [PIL package (autodoc of remaining modules)](../PIL.html)
    * Plugin reference
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

[ View this page ](../_sources/reference/plugins.rst.txt "View this page")

# Plugin reference¶

## `AvifImagePlugin` module¶

class PIL.AvifImagePlugin.AvifImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/AvifImagePlugin.html#AvifImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'AVIF'¶

    

format_description = 'AVIF image'¶

    

load() -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/AvifImagePlugin.html#AvifImageFile.load)¶
    

Load image data based on tile list

load_seek(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/AvifImagePlugin.html#AvifImageFile.load_seek)¶

    

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/AvifImagePlugin.html#AvifImageFile.seek)¶

    

Seeks to the given frame in this sequence file. If you seek beyond the end of
the sequence, the method raises an `EOFError` exception. When a sequence file
is opened, the library automatically seeks to frame 0.

See [`tell()`](Image.html#PIL.Image.Image.tell "PIL.Image.Image.tell").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Parameters:

    

**frame** – Frame number, starting at 0.

Raises:

    

[**EOFError**](https://docs.python.org/3/library/exceptions.html#EOFError
"\(in Python v3.14\)") – If the call attempts to seek beyond the end of the
sequence.

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/AvifImagePlugin.html#AvifImageFile.tell)¶

    

Returns the current frame number. See
[`seek()`](Image.html#PIL.Image.Image.seek "PIL.Image.Image.seek").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Returns:

    

Frame number, starting with 0.

PIL.AvifImagePlugin.get_codec_version(_codec_name : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/AvifImagePlugin.html#get_codec_version)¶
    

## `BmpImagePlugin` module¶

class PIL.BmpImagePlugin.BmpImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/BmpImagePlugin.html#BmpImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

Image plugin for the Windows Bitmap format (BMP)

BITFIELDS = 3¶

    

COMPRESSIONS = {'BITFIELDS': 3, 'JPEG': 4, 'PNG': 5, 'RAW': 0, 'RLE4': 2,
'RLE8': 1}¶

    

JPEG = 4¶

    

PNG = 5¶

    

RAW = 0¶

    

RLE4 = 2¶

    

RLE8 = 1¶

    

format = 'BMP'¶

    

format_description = 'Windows Bitmap'¶

    

k = 'PNG'¶

    

v = 5¶

    

class PIL.BmpImagePlugin.BmpRleDecoder(_mode :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_, _* args:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_)[[source]](../_modules/PIL/BmpImagePlugin.html#BmpRleDecoder)¶

    

Bases: [`PyDecoder`](ImageFile.html#PIL.ImageFile.PyDecoder
"PIL.ImageFile.PyDecoder")

decode(_buffer : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [SupportsArrayInterface](Image.html#PIL.Image.SupportsArrayInterface "PIL.Image.SupportsArrayInterface")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/BmpImagePlugin.html#BmpRleDecoder.decode)¶
    

Override to perform the decoding process.

Parameters:

    

**buffer** – A bytes object with the data to be decoded.

Returns:

    

A tuple of `(bytes consumed, errcode)`. If finished with decoding return -1
for the bytes consumed. Err codes are from
[`ImageFile.ERRORS`](ImageFile.html#PIL.ImageFile.ERRORS
"PIL.ImageFile.ERRORS").

class PIL.BmpImagePlugin.DibImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/BmpImagePlugin.html#DibImageFile)¶
    

Bases: `BmpImageFile`

format = 'DIB'¶

    

format_description = 'Windows Bitmap'¶

    

## `BufrStubImagePlugin` module¶

class PIL.BufrStubImagePlugin.BufrStubImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/BufrStubImagePlugin.html#BufrStubImageFile)¶
    

Bases: [`StubImageFile`](ImageFile.html#PIL.ImageFile.StubImageFile
"PIL.ImageFile.StubImageFile")

format = 'BUFR'¶

    

format_description = 'BUFR'¶

    

PIL.BufrStubImagePlugin.register_handler(_handler : [StubHandler](ImageFile.html#PIL.ImageFile.StubHandler "PIL.ImageFile.StubHandler") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/BufrStubImagePlugin.html#register_handler)¶
    

Install application-specific BUFR image handler.

Parameters:

    

**handler** – Handler object.

## `CurImagePlugin` module¶

class PIL.CurImagePlugin.CurImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/CurImagePlugin.html#CurImageFile)¶
    

Bases: `BmpImageFile`

format = 'CUR'¶

    

format_description = 'Windows Cursor'¶

    

## `DcxImagePlugin` module¶

class PIL.DcxImagePlugin.DcxImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/DcxImagePlugin.html#DcxImageFile)¶
    

Bases: `PcxImageFile`

format = 'DCX'¶

    

format_description = 'Intel DCX'¶

    

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/DcxImagePlugin.html#DcxImageFile.seek)¶

    

Seeks to the given frame in this sequence file. If you seek beyond the end of
the sequence, the method raises an `EOFError` exception. When a sequence file
is opened, the library automatically seeks to frame 0.

See [`tell()`](Image.html#PIL.Image.Image.tell "PIL.Image.Image.tell").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Parameters:

    

**frame** – Frame number, starting at 0.

Raises:

    

[**EOFError**](https://docs.python.org/3/library/exceptions.html#EOFError
"\(in Python v3.14\)") – If the call attempts to seek beyond the end of the
sequence.

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/DcxImagePlugin.html#DcxImageFile.tell)¶

    

Returns the current frame number. See
[`seek()`](Image.html#PIL.Image.Image.seek "PIL.Image.Image.seek").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Returns:

    

Frame number, starting with 0.

## `DdsImagePlugin` module¶

A Pillow plugin for .dds files (S3TC-compressed aka DXTC) Jerome Leclanche
<[jerome@leclan.ch](mailto:jerome%40leclan.ch)>

Documentation:
<https://web.archive.org/web/20170802060935/http://oss.sgi.com/projects/ogl-
sample/registry/EXT/texture_compression_s3tc.txt>

The contents of this file are hereby released in the public domain (CC0) Full
text of the CC0 license: <https://creativecommons.org/publicdomain/zero/1.0/>

class PIL.DdsImagePlugin.D3DFMT(_*
values_)[[source]](../_modules/PIL/DdsImagePlugin.html#D3DFMT)¶

    

Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum
"\(in Python v3.14\)")

A1 = 118¶

    

A16B16G16R16 = 36¶

    

A16B16G16R16F = 113¶

    

A1R5G5B5 = 25¶

    

A2B10G10R10 = 31¶

    

A2B10G10R10_XR_BIAS = 119¶

    

A2R10G10B10 = 35¶

    

A2W10V10U10 = 67¶

    

A32B32G32R32F = 116¶

    

A4L4 = 52¶

    

A4R4G4B4 = 26¶

    

A8 = 28¶

    

A8B8G8R8 = 32¶

    

A8L8 = 51¶

    

A8P8 = 40¶

    

A8R3G3B2 = 29¶

    

A8R8G8B8 = 21¶

    

ATI1 = 826889281¶

    

ATI2 = 843666497¶

    

BC4S = 1395934018¶

    

BC4U = 1429488450¶

    

BC5S = 1395999554¶

    

BC5U = 1429553986¶

    

BINARYBUFFER = 199¶

    

CxV8U8 = 117¶

    

D15S1 = 73¶

    

D16 = 80¶

    

D16_LOCKABLE = 70¶

    

D24FS8 = 83¶

    

D24S8 = 75¶

    

D24X4S4 = 79¶

    

D24X8 = 77¶

    

D32 = 71¶

    

D32F_LOCKABLE = 82¶

    

D32_LOCKABLE = 84¶

    

DX10 = 808540228¶

    

DXT1 = 827611204¶

    

DXT2 = 844388420¶

    

DXT3 = 861165636¶

    

DXT4 = 877942852¶

    

DXT5 = 894720068¶

    

G16R16 = 34¶

    

G16R16F = 112¶

    

G32R32F = 115¶

    

G8R8_G8B8 = 1111970375¶

    

INDEX16 = 101¶

    

INDEX32 = 102¶

    

L16 = 81¶

    

L6V5U5 = 61¶

    

L8 = 50¶

    

MULTI2_ARGB8 = 827606349¶

    

P8 = 41¶

    

Q16W16V16U16 = 110¶

    

Q8W8V8U8 = 63¶

    

R16F = 111¶

    

R32F = 114¶

    

R3G3B2 = 27¶

    

R5G6B5 = 23¶

    

R8G8B8 = 20¶

    

R8G8_B8G8 = 1195525970¶

    

S8_LOCKABLE = 85¶

    

UNKNOWN = 0¶

    

UYVY = 1498831189¶

    

V16U16 = 64¶

    

V8U8 = 60¶

    

VERTEXDATA = 100¶

    

X1R5G5B5 = 24¶

    

X4R4G4B4 = 30¶

    

X8B8G8R8 = 33¶

    

X8L8V8U8 = 62¶

    

X8R8G8B8 = 22¶

    

YUY2 = 844715353¶

    

class PIL.DdsImagePlugin.DDPF(_*
values_)[[source]](../_modules/PIL/DdsImagePlugin.html#DDPF)¶

    

Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag
"\(in Python v3.14\)")

ALPHA = 2¶

    

ALPHAPIXELS = 1¶

    

FOURCC = 4¶

    

LUMINANCE = 131072¶

    

PALETTEINDEXED8 = 32¶

    

RGB = 64¶

    

class PIL.DdsImagePlugin.DDSCAPS(_*
values_)[[source]](../_modules/PIL/DdsImagePlugin.html#DDSCAPS)¶

    

Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag
"\(in Python v3.14\)")

COMPLEX = 8¶

    

MIPMAP = 4194304¶

    

TEXTURE = 4096¶

    

class PIL.DdsImagePlugin.DDSCAPS2(_*
values_)[[source]](../_modules/PIL/DdsImagePlugin.html#DDSCAPS2)¶

    

Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag
"\(in Python v3.14\)")

CUBEMAP = 512¶

    

CUBEMAP_NEGATIVEX = 2048¶

    

CUBEMAP_NEGATIVEY = 8192¶

    

CUBEMAP_NEGATIVEZ = 32768¶

    

CUBEMAP_POSITIVEX = 1024¶

    

CUBEMAP_POSITIVEY = 4096¶

    

CUBEMAP_POSITIVEZ = 16384¶

    

VOLUME = 2097152¶

    

class PIL.DdsImagePlugin.DDSD(_*
values_)[[source]](../_modules/PIL/DdsImagePlugin.html#DDSD)¶

    

Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag
"\(in Python v3.14\)")

CAPS = 1¶

    

DEPTH = 8388608¶

    

HEIGHT = 2¶

    

LINEARSIZE = 524288¶

    

MIPMAPCOUNT = 131072¶

    

PITCH = 8¶

    

PIXELFORMAT = 4096¶

    

WIDTH = 4¶

    

class PIL.DdsImagePlugin.DXGI_FORMAT(_*
values_)[[source]](../_modules/PIL/DdsImagePlugin.html#DXGI_FORMAT)¶

    

Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum
"\(in Python v3.14\)")

A8P8 = 114¶

    

A8_UNORM = 65¶

    

AI44 = 111¶

    

AYUV = 100¶

    

B4G4R4A4_UNORM = 115¶

    

B5G5R5A1_UNORM = 86¶

    

B5G6R5_UNORM = 85¶

    

B8G8R8A8_TYPELESS = 90¶

    

B8G8R8A8_UNORM = 87¶

    

B8G8R8A8_UNORM_SRGB = 91¶

    

B8G8R8X8_TYPELESS = 92¶

    

B8G8R8X8_UNORM = 88¶

    

B8G8R8X8_UNORM_SRGB = 93¶

    

BC1_TYPELESS = 70¶

    

BC1_UNORM = 71¶

    

BC1_UNORM_SRGB = 72¶

    

BC2_TYPELESS = 73¶

    

BC2_UNORM = 74¶

    

BC2_UNORM_SRGB = 75¶

    

BC3_TYPELESS = 76¶

    

BC3_UNORM = 77¶

    

BC3_UNORM_SRGB = 78¶

    

BC4_SNORM = 81¶

    

BC4_TYPELESS = 79¶

    

BC4_UNORM = 80¶

    

BC5_SNORM = 84¶

    

BC5_TYPELESS = 82¶

    

BC5_UNORM = 83¶

    

BC6H_SF16 = 96¶

    

BC6H_TYPELESS = 94¶

    

BC6H_UF16 = 95¶

    

BC7_TYPELESS = 97¶

    

BC7_UNORM = 98¶

    

BC7_UNORM_SRGB = 99¶

    

D16_UNORM = 55¶

    

D24_UNORM_S8_UINT = 45¶

    

D32_FLOAT = 40¶

    

D32_FLOAT_S8X24_UINT = 20¶

    

G8R8_G8B8_UNORM = 69¶

    

IA44 = 112¶

    

NV11 = 110¶

    

NV12 = 103¶

    

OPAQUE_420 = 106¶

    

P010 = 104¶

    

P016 = 105¶

    

P208 = 130¶

    

P8 = 113¶

    

R10G10B10A2_TYPELESS = 23¶

    

R10G10B10A2_UINT = 25¶

    

R10G10B10A2_UNORM = 24¶

    

R10G10B10_XR_BIAS_A2_UNORM = 89¶

    

R11G11B10_FLOAT = 26¶

    

R16G16B16A16_FLOAT = 10¶

    

R16G16B16A16_SINT = 14¶

    

R16G16B16A16_SNORM = 13¶

    

R16G16B16A16_TYPELESS = 9¶

    

R16G16B16A16_UINT = 12¶

    

R16G16B16A16_UNORM = 11¶

    

R16G16_FLOAT = 34¶

    

R16G16_SINT = 38¶

    

R16G16_SNORM = 37¶

    

R16G16_TYPELESS = 33¶

    

R16G16_UINT = 36¶

    

R16G16_UNORM = 35¶

    

R16_FLOAT = 54¶

    

R16_SINT = 59¶

    

R16_SNORM = 58¶

    

R16_TYPELESS = 53¶

    

R16_UINT = 57¶

    

R16_UNORM = 56¶

    

R1_UNORM = 66¶

    

R24G8_TYPELESS = 44¶

    

R24_UNORM_X8_TYPELESS = 46¶

    

R32G32B32A32_FLOAT = 2¶

    

R32G32B32A32_SINT = 4¶

    

R32G32B32A32_TYPELESS = 1¶

    

R32G32B32A32_UINT = 3¶

    

R32G32B32_FLOAT = 6¶

    

R32G32B32_SINT = 8¶

    

R32G32B32_TYPELESS = 5¶

    

R32G32B32_UINT = 7¶

    

R32G32_FLOAT = 16¶

    

R32G32_SINT = 18¶

    

R32G32_TYPELESS = 15¶

    

R32G32_UINT = 17¶

    

R32G8X24_TYPELESS = 19¶

    

R32_FLOAT = 41¶

    

R32_FLOAT_X8X24_TYPELESS = 21¶

    

R32_SINT = 43¶

    

R32_TYPELESS = 39¶

    

R32_UINT = 42¶

    

R8G8B8A8_SINT = 32¶

    

R8G8B8A8_SNORM = 31¶

    

R8G8B8A8_TYPELESS = 27¶

    

R8G8B8A8_UINT = 30¶

    

R8G8B8A8_UNORM = 28¶

    

R8G8B8A8_UNORM_SRGB = 29¶

    

R8G8_B8G8_UNORM = 68¶

    

R8G8_SINT = 52¶

    

R8G8_SNORM = 51¶

    

R8G8_TYPELESS = 48¶

    

R8G8_UINT = 50¶

    

R8G8_UNORM = 49¶

    

R8_SINT = 64¶

    

R8_SNORM = 63¶

    

R8_TYPELESS = 60¶

    

R8_UINT = 62¶

    

R8_UNORM = 61¶

    

R9G9B9E5_SHAREDEXP = 67¶

    

SAMPLER_FEEDBACK_MIN_MIP_OPAQUE = 189¶

    

SAMPLER_FEEDBACK_MIP_REGION_USED_OPAQUE = 190¶

    

UNKNOWN = 0¶

    

V208 = 131¶

    

V408 = 132¶

    

X24_TYPELESS_G8_UINT = 47¶

    

X32_TYPELESS_G8X24_UINT = 22¶

    

Y210 = 108¶

    

Y216 = 109¶

    

Y410 = 101¶

    

Y416 = 102¶

    

YUY2 = 107¶

    

class PIL.DdsImagePlugin.DdsImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/DdsImagePlugin.html#DdsImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'DDS'¶

    

format_description = 'DirectDraw Surface'¶

    

load_seek(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/DdsImagePlugin.html#DdsImageFile.load_seek)¶

    

class PIL.DdsImagePlugin.DdsRgbDecoder(_mode :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_, _* args:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_)[[source]](../_modules/PIL/DdsImagePlugin.html#DdsRgbDecoder)¶

    

Bases: [`PyDecoder`](ImageFile.html#PIL.ImageFile.PyDecoder
"PIL.ImageFile.PyDecoder")

decode(_buffer : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [SupportsArrayInterface](Image.html#PIL.Image.SupportsArrayInterface "PIL.Image.SupportsArrayInterface")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/DdsImagePlugin.html#DdsRgbDecoder.decode)¶
    

Override to perform the decoding process.

Parameters:

    

**buffer** – A bytes object with the data to be decoded.

Returns:

    

A tuple of `(bytes consumed, errcode)`. If finished with decoding return -1
for the bytes consumed. Err codes are from
[`ImageFile.ERRORS`](ImageFile.html#PIL.ImageFile.ERRORS
"PIL.ImageFile.ERRORS").

## `EpsImagePlugin` module¶

class PIL.EpsImagePlugin.EpsImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/EpsImagePlugin.html#EpsImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

EPS File Parser for the Python Imaging Library

format = 'EPS'¶

    

format_description = 'Encapsulated Postscript'¶

    

load(_scale : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 1_, _transparency : [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = False_) -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/EpsImagePlugin.html#EpsImageFile.load)¶
    

Load image data based on tile list

load_seek(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/EpsImagePlugin.html#EpsImageFile.load_seek)¶

    

mode_map = {1: 'L', 2: 'LAB', 3: 'RGB', 4: 'CMYK'}¶

    

PIL.EpsImagePlugin.Ghostscript(_tile :
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[ImageFile._Tile](ImageFile.html#PIL.ImageFile._Tile
"PIL.ImageFile._Tile")]_, _size :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]_, _fp :
IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")]_, _scale :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 1_, _transparency :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = False_) ->
[Image.core.ImagingCore](internal_modules.html#PIL.Image.core.ImagingCore
"PIL.Image.core.ImagingCore")[[source]](../_modules/PIL/EpsImagePlugin.html#Ghostscript)¶

    

Render an image using Ghostscript

PIL.EpsImagePlugin.has_ghostscript() ->
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)")[[source]](../_modules/PIL/EpsImagePlugin.html#has_ghostscript)¶

    

## `FitsImagePlugin` module¶

class PIL.FitsImagePlugin.FitsGzipDecoder(_mode :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_, _* args:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_)[[source]](../_modules/PIL/FitsImagePlugin.html#FitsGzipDecoder)¶

    

Bases: [`PyDecoder`](ImageFile.html#PIL.ImageFile.PyDecoder
"PIL.ImageFile.PyDecoder")

decode(_buffer : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [SupportsArrayInterface](Image.html#PIL.Image.SupportsArrayInterface "PIL.Image.SupportsArrayInterface")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/FitsImagePlugin.html#FitsGzipDecoder.decode)¶
    

Override to perform the decoding process.

Parameters:

    

**buffer** – A bytes object with the data to be decoded.

Returns:

    

A tuple of `(bytes consumed, errcode)`. If finished with decoding return -1
for the bytes consumed. Err codes are from
[`ImageFile.ERRORS`](ImageFile.html#PIL.ImageFile.ERRORS
"PIL.ImageFile.ERRORS").

class PIL.FitsImagePlugin.FitsImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/FitsImagePlugin.html#FitsImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'FITS'¶

    

format_description = 'FITS'¶

    

## `FliImagePlugin` module¶

class PIL.FliImagePlugin.FliImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/FliImagePlugin.html#FliImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'FLI'¶

    

format_description = 'Autodesk FLI/FLC Animation'¶

    

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/FliImagePlugin.html#FliImageFile.seek)¶

    

Seeks to the given frame in this sequence file. If you seek beyond the end of
the sequence, the method raises an `EOFError` exception. When a sequence file
is opened, the library automatically seeks to frame 0.

See [`tell()`](Image.html#PIL.Image.Image.tell "PIL.Image.Image.tell").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Parameters:

    

**frame** – Frame number, starting at 0.

Raises:

    

[**EOFError**](https://docs.python.org/3/library/exceptions.html#EOFError
"\(in Python v3.14\)") – If the call attempts to seek beyond the end of the
sequence.

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/FliImagePlugin.html#FliImageFile.tell)¶

    

Returns the current frame number. See
[`seek()`](Image.html#PIL.Image.Image.seek "PIL.Image.Image.seek").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Returns:

    

Frame number, starting with 0.

## `FpxImagePlugin` module¶

class PIL.FpxImagePlugin.FpxImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/FpxImagePlugin.html#FpxImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

close() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python
v3.14\)")[[source]](../_modules/PIL/FpxImagePlugin.html#FpxImageFile.close)¶

    

Closes the file pointer, if possible.

This operation will destroy the image core and release its memory. The image
data will be unusable afterward.

This function is required to close images that have multiple frames or have
not had their file read and closed by the
[`load()`](Image.html#PIL.Image.Image.load "PIL.Image.Image.load") method. See
[File handling in Pillow](open_files.html#file-handling) for more information.

format = 'FPX'¶

    

format_description = 'FlashPix'¶

    

load() -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/FpxImagePlugin.html#FpxImageFile.load)¶
    

Load image data based on tile list

## `GbrImagePlugin` module¶

class PIL.GbrImagePlugin.GbrImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/GbrImagePlugin.html#GbrImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'GBR'¶

    

format_description = 'GIMP brush file'¶

    

load() -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/GbrImagePlugin.html#GbrImageFile.load)¶
    

Load image data based on tile list

## `GifImagePlugin` module¶

class PIL.GifImagePlugin.GifImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/GifImagePlugin.html#GifImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

data() -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/GifImagePlugin.html#GifImageFile.data)¶
    

format = 'GIF'¶

    

format_description = 'Compuserve GIF'¶

    

global_palette = None¶

    

property is_animated:
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)")[[source]](../_modules/PIL/GifImagePlugin.html#GifImageFile.is_animated)¶

    

load_end() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/GifImagePlugin.html#GifImageFile.load_end)¶

    

load_prepare() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/GifImagePlugin.html#GifImageFile.load_prepare)¶

    

property n_frames: [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")¶

    

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/GifImagePlugin.html#GifImageFile.seek)¶

    

Seeks to the given frame in this sequence file. If you seek beyond the end of
the sequence, the method raises an `EOFError` exception. When a sequence file
is opened, the library automatically seeks to frame 0.

See [`tell()`](Image.html#PIL.Image.Image.tell "PIL.Image.Image.tell").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Parameters:

    

**frame** – Frame number, starting at 0.

Raises:

    

[**EOFError**](https://docs.python.org/3/library/exceptions.html#EOFError
"\(in Python v3.14\)") – If the call attempts to seek beyond the end of the
sequence.

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/GifImagePlugin.html#GifImageFile.tell)¶

    

Returns the current frame number. See
[`seek()`](Image.html#PIL.Image.Image.seek "PIL.Image.Image.seek").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Returns:

    

Frame number, starting with 0.

PIL.GifImagePlugin.LOADING_STRATEGY = LoadingStrategy.RGB_AFTER_FIRST¶

    

Added in version 9.1.0.

class PIL.GifImagePlugin.LoadingStrategy(_*
values_)[[source]](../_modules/PIL/GifImagePlugin.html#LoadingStrategy)¶

    

Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum
"\(in Python v3.14\)")

Added in version 9.1.0.

RGB_AFTER_DIFFERENT_PALETTE_ONLY = 1¶

    

RGB_AFTER_FIRST = 0¶

    

RGB_ALWAYS = 2¶

    

PIL.GifImagePlugin.get_interlace(_im : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) ->
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")[[source]](../_modules/PIL/GifImagePlugin.html#get_interlace)¶

    

PIL.GifImagePlugin.getdata(_im : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _offset :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")] = (0, 0)_, _** params:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_) -> [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")][[source]](../_modules/PIL/GifImagePlugin.html#getdata)¶

    

Legacy Method

Return a list of strings representing this image. The first string is a local
image header, the rest contains encoded image data.

To specify duration, add the time in milliseconds, e.g. `getdata(im_frame,
duration=1000)`

Parameters:

    

  * **im** – Image object

  * **offset** – Tuple of (x, y) pixels. Defaults to (0, 0)

  * ****params** – e.g. duration or other encoder info parameters

Returns:

    

List of bytes containing GIF encoded frame data

PIL.GifImagePlugin.getheader(_im : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _palette : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "\(in Python v3.14\)") | [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | [ImagePalette](ImagePalette.html#PIL.ImagePalette.ImagePalette "PIL.ImagePalette.ImagePalette") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _info : [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")], [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")][[source]](../_modules/PIL/GifImagePlugin.html#getheader)¶
    

Legacy Method to get Gif data from image.

Warning:: May modify image data.

Parameters:

    

  * **im** – Image object

  * **palette** – bytes object containing the source palette, or ….

  * **info** – encoderinfo

Returns:

    

tuple of(list of header items, optimized palette)

## `GribStubImagePlugin` module¶

class PIL.GribStubImagePlugin.GribStubImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/GribStubImagePlugin.html#GribStubImageFile)¶
    

Bases: [`StubImageFile`](ImageFile.html#PIL.ImageFile.StubImageFile
"PIL.ImageFile.StubImageFile")

format = 'GRIB'¶

    

format_description = 'GRIB'¶

    

PIL.GribStubImagePlugin.register_handler(_handler : [StubHandler](ImageFile.html#PIL.ImageFile.StubHandler "PIL.ImageFile.StubHandler") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/GribStubImagePlugin.html#register_handler)¶
    

Install application-specific GRIB image handler.

Parameters:

    

**handler** – Handler object.

## `Hdf5StubImagePlugin` module¶

class PIL.Hdf5StubImagePlugin.HDF5StubImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/Hdf5StubImagePlugin.html#HDF5StubImageFile)¶
    

Bases: [`StubImageFile`](ImageFile.html#PIL.ImageFile.StubImageFile
"PIL.ImageFile.StubImageFile")

format = 'HDF5'¶

    

format_description = 'HDF5'¶

    

PIL.Hdf5StubImagePlugin.register_handler(_handler : [StubHandler](ImageFile.html#PIL.ImageFile.StubHandler "PIL.ImageFile.StubHandler") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/Hdf5StubImagePlugin.html#register_handler)¶
    

Install application-specific HDF5 image handler.

Parameters:

    

**handler** – Handler object.

## `IcnsImagePlugin` module¶

class PIL.IcnsImagePlugin.IcnsFile(_fobj :
[IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]_)[[source]](../_modules/PIL/IcnsImagePlugin.html#IcnsFile)¶

    

Bases: [`object`](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.14\)")

SIZES = {(16, 16, 1): [(b'icp4', <function read_png_or_jpeg2000>), (b'is32',
<function read_32>), (b's8mk', <function read_mk>)], (16, 16, 2): [(b'ic11',
<function read_png_or_jpeg2000>)], (32, 32, 1): [(b'icp5', <function
read_png_or_jpeg2000>), (b'il32', <function read_32>), (b'l8mk', <function
read_mk>)], (32, 32, 2): [(b'ic12', <function read_png_or_jpeg2000>)], (48,
48, 1): [(b'ih32', <function read_32>), (b'h8mk', <function read_mk>)], (64,
64, 1): [(b'icp6', <function read_png_or_jpeg2000>)], (128, 128, 1):
[(b'ic07', <function read_png_or_jpeg2000>), (b'it32', <function read_32t>),
(b't8mk', <function read_mk>)], (128, 128, 2): [(b'ic13', <function
read_png_or_jpeg2000>)], (256, 256, 1): [(b'ic08', <function
read_png_or_jpeg2000>)], (256, 256, 2): [(b'ic14', <function
read_png_or_jpeg2000>)], (512, 512, 1): [(b'ic09', <function
read_png_or_jpeg2000>)], (512, 512, 2): [(b'ic10', <function
read_png_or_jpeg2000>)]}¶

    

bestsize() -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple
"\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")][[source]](../_modules/PIL/IcnsImagePlugin.html#IcnsFile.bestsize)¶

    

dataforsize(_size :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]_) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)"), [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")][[source]](../_modules/PIL/IcnsImagePlugin.html#IcnsFile.dataforsize)¶

    

Get an icon resource as {channel: array}. Note that the arrays are bottom-up
like windows bitmaps and will likely need to be flipped or transposed in some
way.

getimage(_size : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image")[[source]](../_modules/PIL/IcnsImagePlugin.html#IcnsFile.getimage)¶
    

itersizes() -> [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in
Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")]][[source]](../_modules/PIL/IcnsImagePlugin.html#IcnsFile.itersizes)¶

    

class PIL.IcnsImagePlugin.IcnsImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/IcnsImagePlugin.html#IcnsImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

PIL image support for Mac OS .icns files. Chooses the best resolution, but
will possibly load a different size image if you mutate the size attribute
before calling ‘load’.

The info dictionary has a key ‘sizes’ that is a list of sizes that the icns
file has.

format = 'ICNS'¶

    

format_description = 'Mac OS icns resource'¶

    

load(_scale : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/IcnsImagePlugin.html#IcnsImageFile.load)¶
    

Load image data based on tile list

property size: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple
"\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]¶

    

PIL.IcnsImagePlugin.nextheader(_fobj :
[IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python
v3.14\)")][[source]](../_modules/PIL/IcnsImagePlugin.html#nextheader)¶

    

PIL.IcnsImagePlugin.read_32(_fobj :
[IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]_, _start_length :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]_, _size :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]_) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)"), [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")][[source]](../_modules/PIL/IcnsImagePlugin.html#read_32)¶

    

Read a 32bit RGB icon resource. Seems to be either uncompressed or an RLE
packbits-like scheme.

PIL.IcnsImagePlugin.read_32t(_fobj :
[IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]_, _start_length :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]_, _size :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]_) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)"), [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")][[source]](../_modules/PIL/IcnsImagePlugin.html#read_32t)¶

    

PIL.IcnsImagePlugin.read_mk(_fobj :
[IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]_, _start_length :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]_, _size :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]_) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)"), [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")][[source]](../_modules/PIL/IcnsImagePlugin.html#read_mk)¶

    

PIL.IcnsImagePlugin.read_png_or_jpeg2000(_fobj :
[IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]_, _start_length :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]_, _size :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]_) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)"), [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")][[source]](../_modules/PIL/IcnsImagePlugin.html#read_png_or_jpeg2000)¶

    

## `IcoImagePlugin` module¶

class PIL.IcoImagePlugin.IcoFile(_buf :
[IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]_)[[source]](../_modules/PIL/IcoImagePlugin.html#IcoFile)¶

    

Bases: [`object`](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.14\)")

frame(_idx : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/IcoImagePlugin.html#IcoFile.frame)¶

    

Get an image from frame idx

getentryindex(_size : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]_, _bpp : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = False_) -> [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")[[source]](../_modules/PIL/IcoImagePlugin.html#IcoFile.getentryindex)¶
    

getimage(_size : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]_, _bpp : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = False_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image")[[source]](../_modules/PIL/IcoImagePlugin.html#IcoFile.getimage)¶
    

Get an image from the icon

sizes() -> [set](https://docs.python.org/3/library/stdtypes.html#set "\(in
Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple
"\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python
v3.14\)")]][[source]](../_modules/PIL/IcoImagePlugin.html#IcoFile.sizes)¶

    

Get a set of all available icon sizes and color depths.

class PIL.IcoImagePlugin.IcoImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/IcoImagePlugin.html#IcoImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

PIL read-only image support for Microsoft Windows .ico files.

By default the largest resolution image in the file will be loaded. This can
be changed by altering the ‘size’ attribute before calling ‘load’.

The info dictionary has a key ‘sizes’ that is a list of the sizes available in
the icon file.

Handles classic, XP and Vista icon formats.

When saving, PNG compression is used. Support for this was only added in
Windows Vista. If you are unable to view the icon in Windows, convert the
image to “RGBA” mode before saving.

This plugin is a refactored version of Win32IconImagePlugin by Bryan Davis
<[casadebender@gmail.com](mailto:casadebender%40gmail.com)>.
<https://code.google.com/archive/p/casadebender/wikis/Win32IconImagePlugin.wiki>

format = 'ICO'¶

    

format_description = 'Windows Icon'¶

    

load() -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/IcoImagePlugin.html#IcoImageFile.load)¶
    

Load image data based on tile list

load_seek(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/IcoImagePlugin.html#IcoImageFile.load_seek)¶

    

property size: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple
"\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]¶

    

class PIL.IcoImagePlugin.IconHeader(_width_ , _height_ , _nb_color_ ,
_reserved_ , _planes_ , _bpp_ , _size_ , _offset_ , _dim_ , _square_ ,
_color_depth_)[[source]](../_modules/PIL/IcoImagePlugin.html#IconHeader)¶

    

Bases:
[`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple
"\(in Python v3.14\)")

bpp: [int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")¶

    

Alias for field number 5

color_depth: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

Alias for field number 10

dim: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in
Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]¶

    

Alias for field number 8

height: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

Alias for field number 1

nb_color: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

Alias for field number 2

offset: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

Alias for field number 7

planes: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

Alias for field number 4

reserved: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

Alias for field number 3

size: [int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")¶

    

Alias for field number 6

square: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

Alias for field number 9

width: [int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")¶

    

Alias for field number 0

## `ImImagePlugin` module¶

class PIL.ImImagePlugin.ImImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/ImImagePlugin.html#ImImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'IM'¶

    

format_description = 'IFUNC Image Memory'¶

    

property is_animated:
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)")¶

    

property n_frames: [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")¶

    

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/ImImagePlugin.html#ImImageFile.seek)¶

    

Seeks to the given frame in this sequence file. If you seek beyond the end of
the sequence, the method raises an `EOFError` exception. When a sequence file
is opened, the library automatically seeks to frame 0.

See [`tell()`](Image.html#PIL.Image.Image.tell "PIL.Image.Image.tell").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Parameters:

    

**frame** – Frame number, starting at 0.

Raises:

    

[**EOFError**](https://docs.python.org/3/library/exceptions.html#EOFError
"\(in Python v3.14\)") – If the call attempts to seek beyond the end of the
sequence.

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/ImImagePlugin.html#ImImageFile.tell)¶

    

Returns the current frame number. See
[`seek()`](Image.html#PIL.Image.Image.seek "PIL.Image.Image.seek").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Returns:

    

Frame number, starting with 0.

PIL.ImImagePlugin.number(_s :
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_) -> [float](https://docs.python.org/3/library/functions.html#float
"\(in Python v3.14\)")[[source]](../_modules/PIL/ImImagePlugin.html#number)¶

    

## `ImtImagePlugin` module¶

class PIL.ImtImagePlugin.ImtImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/ImtImagePlugin.html#ImtImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'IMT'¶

    

format_description = 'IM Tools'¶

    

## `IptcImagePlugin` module¶

class PIL.IptcImagePlugin.IptcImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/IptcImagePlugin.html#IptcImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

field() -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/IptcImagePlugin.html#IptcImageFile.field)¶
    

format = 'IPTC'¶

    

format_description = 'IPTC/NAA'¶

    

getint(_key : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple
"\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")]_) ->
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")[[source]](../_modules/PIL/IptcImagePlugin.html#IptcImageFile.getint)¶

    

load() -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/IptcImagePlugin.html#IptcImageFile.load)¶
    

Load image data based on tile list

PIL.IptcImagePlugin.getiptcinfo(_im : [ImageFile](ImageFile.html#PIL.ImageFile.ImageFile "PIL.ImageFile.ImageFile")_) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")], [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/IptcImagePlugin.html#getiptcinfo)¶
    

Get IPTC information from TIFF, JPEG, or IPTC file.

Parameters:

    

**im** – An image containing IPTC data.

Returns:

    

A dictionary containing IPTC information, or None if no IPTC information block
was found.

## `JpegImagePlugin` module¶

PIL.JpegImagePlugin.APP(_self : JpegImageFile_, _marker :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python v3.14\)")[[source]](../_modules/PIL/JpegImagePlugin.html#APP)¶

    

PIL.JpegImagePlugin.COM(_self : JpegImageFile_, _marker :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python v3.14\)")[[source]](../_modules/PIL/JpegImagePlugin.html#COM)¶

    

PIL.JpegImagePlugin.DQT(_self : JpegImageFile_, _marker :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python v3.14\)")[[source]](../_modules/PIL/JpegImagePlugin.html#DQT)¶

    

class PIL.JpegImagePlugin.JpegImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/JpegImagePlugin.html#JpegImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

draft(_mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")_, _size : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/JpegImagePlugin.html#JpegImageFile.draft)¶
    

Configures the image file loader so it returns a version of the image that as
closely as possible matches the given mode and size. For example, you can use
this method to convert a color JPEG to grayscale while loading it.

If any changes are made, returns a tuple with the chosen `mode` and `box` with
coordinates of the original image within the altered one.

Note that this method modifies the [`Image`](Image.html#PIL.Image.Image
"PIL.Image.Image") object in place. If the image has already been loaded, this
method has no effect.

Note: This method is not implemented for most images. It is currently
implemented only for JPEG and MPO images.

Parameters:

    

  * **mode** – The requested mode.

  * **size** – The requested size in pixels, as a 2-tuple: (width, height).

format = 'JPEG'¶

    

format_description = 'JPEG (ISO 10918)'¶

    

load_djpeg() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/JpegImagePlugin.html#JpegImageFile.load_djpeg)¶

    

load_read(_read_bytes :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/JpegImagePlugin.html#JpegImageFile.load_read)¶

    

internal: read more image data For premature EOF and LOAD_TRUNCATED_IMAGES
adds EOI marker so libjpeg can finish decoding

PIL.JpegImagePlugin.SOF(_self : JpegImageFile_, _marker :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python v3.14\)")[[source]](../_modules/PIL/JpegImagePlugin.html#SOF)¶

    

PIL.JpegImagePlugin.Skip(_self : JpegImageFile_, _marker :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python v3.14\)")[[source]](../_modules/PIL/JpegImagePlugin.html#Skip)¶

    

PIL.JpegImagePlugin.get_sampling(_im : [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_) ->
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")[[source]](../_modules/PIL/JpegImagePlugin.html#get_sampling)¶

    

PIL.JpegImagePlugin.jpeg_factory(_fp : IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> JpegImageFile | MpoImageFile[[source]](../_modules/PIL/JpegImagePlugin.html#jpeg_factory)¶
    

## `Jpeg2KImagePlugin` module¶

class PIL.Jpeg2KImagePlugin.BoxReader(_fp :
IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")]_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = -1_)[[source]](../_modules/PIL/Jpeg2KImagePlugin.html#BoxReader)¶

    

Bases: [`object`](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.14\)")

A small helper class to read fields stored in JPEG2000 header boxes and to
easily step into and read sub-boxes.

has_next_box() -> [bool](https://docs.python.org/3/library/functions.html#bool
"\(in Python
v3.14\)")[[source]](../_modules/PIL/Jpeg2KImagePlugin.html#BoxReader.has_next_box)¶

    

next_box_type() ->
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")[[source]](../_modules/PIL/Jpeg2KImagePlugin.html#BoxReader.next_box_type)¶

    

read_boxes() ->
BoxReader[[source]](../_modules/PIL/Jpeg2KImagePlugin.html#BoxReader.read_boxes)¶

    

read_fields(_field_format : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)"), ...][[source]](../_modules/PIL/Jpeg2KImagePlugin.html#BoxReader.read_fields)¶
    

class PIL.Jpeg2KImagePlugin.Jpeg2KImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/Jpeg2KImagePlugin.html#Jpeg2KImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'JPEG2000'¶

    

format_description = 'JPEG 2000 (ISO 15444)'¶

    

load() -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/Jpeg2KImagePlugin.html#Jpeg2KImageFile.load)¶
    

Load image data based on tile list

property reduce: Callable[[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")], [Image.Image](Image.html#PIL.Image.Image "PIL.Image.Image")] | [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")¶
    

Returns a copy of the image reduced `factor` times. If the size of the image
is not dividable by `factor`, the resulting size will be rounded up.

Parameters:

    

  * **factor** – A greater than 0 integer or tuple of two integers for width and height separately.

  * **box** – An optional 4-tuple of ints providing the source image region to be reduced. The values must be within `(0, 0, width, height)` rectangle. If omitted or `None`, the entire source is used.

## `McIdasImagePlugin` module¶

class PIL.McIdasImagePlugin.McIdasImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/McIdasImagePlugin.html#McIdasImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'MCIDAS'¶

    

format_description = 'McIdas area file'¶

    

## `MicImagePlugin` module¶

class PIL.MicImagePlugin.MicImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/MicImagePlugin.html#MicImageFile)¶
    

Bases: `TiffImageFile`

close() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python
v3.14\)")[[source]](../_modules/PIL/MicImagePlugin.html#MicImageFile.close)¶

    

Closes the file pointer, if possible.

This operation will destroy the image core and release its memory. The image
data will be unusable afterward.

This function is required to close images that have multiple frames or have
not had their file read and closed by the
[`load()`](Image.html#PIL.Image.Image.load "PIL.Image.Image.load") method. See
[File handling in Pillow](open_files.html#file-handling) for more information.

format = 'MIC'¶

    

format_description = 'Microsoft Image Composer'¶

    

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/MicImagePlugin.html#MicImageFile.seek)¶

    

Select a given frame as current image

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/MicImagePlugin.html#MicImageFile.tell)¶

    

Return the current frame number

## `MpegImagePlugin` module¶

class PIL.MpegImagePlugin.BitStream(_fp :
[SupportsRead](internal_modules.html#PIL._typing.SupportsRead
"PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")]_)[[source]](../_modules/PIL/MpegImagePlugin.html#BitStream)¶

    

Bases: [`object`](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.14\)")

next() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/MpegImagePlugin.html#BitStream.next)¶

    

peek(_bits : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")[[source]](../_modules/PIL/MpegImagePlugin.html#BitStream.peek)¶

    

read(_bits : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")[[source]](../_modules/PIL/MpegImagePlugin.html#BitStream.read)¶

    

skip(_bits : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/MpegImagePlugin.html#BitStream.skip)¶

    

class PIL.MpegImagePlugin.MpegImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/MpegImagePlugin.html#MpegImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'MPEG'¶

    

format_description = 'MPEG'¶

    

## `MpoImagePlugin` module¶

class PIL.MpoImagePlugin.MpoImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/MpoImagePlugin.html#MpoImageFile)¶
    

Bases: `JpegImageFile`

static adopt(_jpeg_instance : JpegImageFile_, _mpheader : [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> MpoImageFile[[source]](../_modules/PIL/MpoImagePlugin.html#MpoImageFile.adopt)¶
    

Transform the instance of JpegImageFile into an instance of MpoImageFile.
After the call, the JpegImageFile is extended to be an MpoImageFile.

This is essentially useful when opening a JPEG file that reveals itself as an
MPO, to avoid double call to _open.

format = 'MPO'¶

    

format_description = 'MPO (CIPA DC-007)'¶

    

load_seek(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/MpoImagePlugin.html#MpoImageFile.load_seek)¶

    

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/MpoImagePlugin.html#MpoImageFile.seek)¶

    

Seeks to the given frame in this sequence file. If you seek beyond the end of
the sequence, the method raises an `EOFError` exception. When a sequence file
is opened, the library automatically seeks to frame 0.

See [`tell()`](Image.html#PIL.Image.Image.tell "PIL.Image.Image.tell").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Parameters:

    

**frame** – Frame number, starting at 0.

Raises:

    

[**EOFError**](https://docs.python.org/3/library/exceptions.html#EOFError
"\(in Python v3.14\)") – If the call attempts to seek beyond the end of the
sequence.

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/MpoImagePlugin.html#MpoImageFile.tell)¶

    

Returns the current frame number. See
[`seek()`](Image.html#PIL.Image.Image.seek "PIL.Image.Image.seek").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Returns:

    

Frame number, starting with 0.

## `MspImagePlugin` module¶

class PIL.MspImagePlugin.MspDecoder(_mode :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_, _* args:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_)[[source]](../_modules/PIL/MspImagePlugin.html#MspDecoder)¶

    

Bases: [`PyDecoder`](ImageFile.html#PIL.ImageFile.PyDecoder
"PIL.ImageFile.PyDecoder")

decode(_buffer : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [SupportsArrayInterface](Image.html#PIL.Image.SupportsArrayInterface "PIL.Image.SupportsArrayInterface")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/MspImagePlugin.html#MspDecoder.decode)¶
    

Override to perform the decoding process.

Parameters:

    

**buffer** – A bytes object with the data to be decoded.

Returns:

    

A tuple of `(bytes consumed, errcode)`. If finished with decoding return -1
for the bytes consumed. Err codes are from
[`ImageFile.ERRORS`](ImageFile.html#PIL.ImageFile.ERRORS
"PIL.ImageFile.ERRORS").

class PIL.MspImagePlugin.MspImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/MspImagePlugin.html#MspImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'MSP'¶

    

format_description = 'Windows Paint'¶

    

## `PalmImagePlugin` module¶

PIL.PalmImagePlugin.build_prototype_image() ->
[Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/PalmImagePlugin.html#build_prototype_image)¶

    

## `PcdImagePlugin` module¶

class PIL.PcdImagePlugin.PcdImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/PcdImagePlugin.html#PcdImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'PCD'¶

    

format_description = 'Kodak PhotoCD'¶

    

load_end() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PcdImagePlugin.html#PcdImageFile.load_end)¶

    

load_prepare() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PcdImagePlugin.html#PcdImageFile.load_prepare)¶

    

## `PcxImagePlugin` module¶

class PIL.PcxImagePlugin.PcxImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/PcxImagePlugin.html#PcxImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'PCX'¶

    

format_description = 'Paintbrush'¶

    

## `PdfImagePlugin` module¶

## `PixarImagePlugin` module¶

class PIL.PixarImagePlugin.PixarImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/PixarImagePlugin.html#PixarImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'PIXAR'¶

    

format_description = 'PIXAR raster image'¶

    

## `PngImagePlugin` module¶

class PIL.PngImagePlugin.Blend(_*
values_)[[source]](../_modules/PIL/PngImagePlugin.html#Blend)¶

    

Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum
"\(in Python v3.14\)")

OP_OVER = 1¶

    

This frame should be alpha composited with the previous output image contents.
See [Saving APNG sequences](../handbook/image-file-formats.html#apng-saving).

OP_SOURCE = 0¶

    

All color components of this frame, including alpha, overwrite the previous
output image contents. See [Saving APNG sequences](../handbook/image-file-
formats.html#apng-saving).

class PIL.PngImagePlugin.ChunkStream(_fp :
[IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python
v3.14\)")]_)[[source]](../_modules/PIL/PngImagePlugin.html#ChunkStream)¶

    

Bases: [`object`](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.14\)")

call(_cid : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python v3.14\)")_, _pos :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#ChunkStream.call)¶

    

Call the appropriate chunk handler

close() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#ChunkStream.close)¶

    

crc(_cid : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")_, _data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#ChunkStream.crc)¶

    

Read and verify checksum

crc_skip(_cid : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python v3.14\)")_, _data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#ChunkStream.crc_skip)¶

    

Read checksum

push(_cid : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python v3.14\)")_, _pos :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#ChunkStream.push)¶

    

read() -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in
Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")][[source]](../_modules/PIL/PngImagePlugin.html#ChunkStream.read)¶

    

Fetch a new chunk. Returns header information.

verify(_endchunk :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)") = b'IEND'_) ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python
v3.14\)")][[source]](../_modules/PIL/PngImagePlugin.html#ChunkStream.verify)¶

    

fp: [IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

queue: [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

class PIL.PngImagePlugin.Disposal(_*
values_)[[source]](../_modules/PIL/PngImagePlugin.html#Disposal)¶

    

Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum
"\(in Python v3.14\)")

OP_BACKGROUND = 1¶

    

This frame’s modified region is cleared to fully transparent black before
rendering the next frame. See [Saving APNG sequences](../handbook/image-file-
formats.html#apng-saving).

OP_NONE = 0¶

    

No disposal is done on this frame before rendering the next frame. See [Saving
APNG sequences](../handbook/image-file-formats.html#apng-saving).

OP_PREVIOUS = 2¶

    

This frame’s modified region is reverted to the previous frame’s contents
before rendering the next frame. See [Saving APNG
sequences](../handbook/image-file-formats.html#apng-saving).

class PIL.PngImagePlugin.PngImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/PngImagePlugin.html#PngImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

getexif() -> [Exif](Image.html#PIL.Image.Exif
"PIL.Image.Exif")[[source]](../_modules/PIL/PngImagePlugin.html#PngImageFile.getexif)¶

    

Gets EXIF data from the image.

Returns:

    

an [`Exif`](Image.html#PIL.Image.Exif "PIL.Image.Exif") object.

load_end() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngImageFile.load_end)¶

    

internal: finished reading image data

load_prepare() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngImageFile.load_prepare)¶

    

internal: prepare to read PNG file

load_read(_read_bytes :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngImageFile.load_read)¶

    

internal: read more image data

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngImageFile.seek)¶

    

Seeks to the given frame in this sequence file. If you seek beyond the end of
the sequence, the method raises an `EOFError` exception. When a sequence file
is opened, the library automatically seeks to frame 0.

See [`tell()`](Image.html#PIL.Image.Image.tell "PIL.Image.Image.tell").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Parameters:

    

**frame** – Frame number, starting at 0.

Raises:

    

[**EOFError**](https://docs.python.org/3/library/exceptions.html#EOFError
"\(in Python v3.14\)") – If the call attempts to seek beyond the end of the
sequence.

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngImageFile.tell)¶

    

Returns the current frame number. See
[`seek()`](Image.html#PIL.Image.Image.seek "PIL.Image.Image.seek").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Returns:

    

Frame number, starting with 0.

verify() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngImageFile.verify)¶

    

Verify PNG file

format = 'PNG'¶

    

format_description = 'Portable network graphics'¶

    

property text: [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)"), [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [iTXt](../PIL.html#PIL.PngImagePlugin.iTXt "PIL.PngImagePlugin.iTXt")]¶
    

class PIL.PngImagePlugin.PngStream(_fp :
[IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]_)[[source]](../_modules/PIL/PngImagePlugin.html#PngStream)¶

    

Bases: `ChunkStream`

check_text_memory(_chunklen :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.check_text_memory)¶

    

chunk_IDAT(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) ->
NoReturn[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_IDAT)¶

    

chunk_IEND(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) ->
NoReturn[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_IEND)¶

    

chunk_IHDR(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_IHDR)¶

    

chunk_PLTE(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_PLTE)¶

    

chunk_acTL(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_acTL)¶

    

chunk_cHRM(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_cHRM)¶

    

chunk_eXIf(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_eXIf)¶

    

chunk_fcTL(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_fcTL)¶

    

chunk_fdAT(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_fdAT)¶

    

chunk_gAMA(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_gAMA)¶

    

chunk_iCCP(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_iCCP)¶

    

chunk_iTXt(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_iTXt)¶

    

chunk_pHYs(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_pHYs)¶

    

chunk_sRGB(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_sRGB)¶

    

chunk_tEXt(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_tEXt)¶

    

chunk_tRNS(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_tRNS)¶

    

chunk_zTXt(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _length :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.chunk_zTXt)¶

    

rewind() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.rewind)¶

    

save_rewind() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#PngStream.save_rewind)¶

    

im_custom_mimetype: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

im_info: [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")], Any]¶
    

im_n_frames: [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

im_palette: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)"), [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

im_text: [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)"), [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [iTXt](../PIL.html#PIL.PngImagePlugin.iTXt "PIL.PngImagePlugin.iTXt")]¶
    

im_tile: [list](https://docs.python.org/3/library/stdtypes.html#list "\(in
Python v3.14\)")[[ImageFile._Tile](ImageFile.html#PIL.ImageFile._Tile
"PIL.ImageFile._Tile")]¶

    

PIL.PngImagePlugin.getchunks(_im : [Image.Image](Image.html#PIL.Image.Image
"PIL.Image.Image")_, _** params: Any_) ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in
Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python v3.14\)"),
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)"), [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]][[source]](../_modules/PIL/PngImagePlugin.html#getchunks)¶

    

Return a list of PNG chunks representing this image.

PIL.PngImagePlugin.is_cid(_string_ , _pos =0_, _endpos =9223372036854775807_)¶

    

Matches zero or more characters at the beginning of the string.

PIL.PngImagePlugin.putchunk(_fp :
[IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]_, _cid :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _* data:
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/PngImagePlugin.html#putchunk)¶

    

Write a PNG chunk (including CRC field)

PIL.PngImagePlugin.MAX_TEXT_CHUNK = 1048576¶

    

Maximum decompressed size for a iTXt or zTXt chunk. Eliminates decompression
bombs where compressed chunks can expand 1000x. See [Text in PNG File
Format](../handbook/image-file-formats.html#png-text).

PIL.PngImagePlugin.MAX_TEXT_MEMORY = 67108864¶

    

Set the maximum total text chunk size. See [Text in PNG File
Format](../handbook/image-file-formats.html#png-text).

## `PpmImagePlugin` module¶

class PIL.PpmImagePlugin.PpmDecoder(_mode :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_, _* args:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_)[[source]](../_modules/PIL/PpmImagePlugin.html#PpmDecoder)¶

    

Bases: [`PyDecoder`](ImageFile.html#PIL.ImageFile.PyDecoder
"PIL.ImageFile.PyDecoder")

decode(_buffer : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [SupportsArrayInterface](Image.html#PIL.Image.SupportsArrayInterface "PIL.Image.SupportsArrayInterface")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/PpmImagePlugin.html#PpmDecoder.decode)¶
    

Override to perform the decoding process.

Parameters:

    

**buffer** – A bytes object with the data to be decoded.

Returns:

    

A tuple of `(bytes consumed, errcode)`. If finished with decoding return -1
for the bytes consumed. Err codes are from
[`ImageFile.ERRORS`](ImageFile.html#PIL.ImageFile.ERRORS
"PIL.ImageFile.ERRORS").

class PIL.PpmImagePlugin.PpmImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/PpmImagePlugin.html#PpmImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'PPM'¶

    

format_description = 'Pbmplus image'¶

    

class PIL.PpmImagePlugin.PpmPlainDecoder(_mode :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_, _* args:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_)[[source]](../_modules/PIL/PpmImagePlugin.html#PpmPlainDecoder)¶

    

Bases: [`PyDecoder`](ImageFile.html#PIL.ImageFile.PyDecoder
"PIL.ImageFile.PyDecoder")

decode(_buffer : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [SupportsArrayInterface](Image.html#PIL.Image.SupportsArrayInterface "PIL.Image.SupportsArrayInterface")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/PpmImagePlugin.html#PpmPlainDecoder.decode)¶
    

Override to perform the decoding process.

Parameters:

    

**buffer** – A bytes object with the data to be decoded.

Returns:

    

A tuple of `(bytes consumed, errcode)`. If finished with decoding return -1
for the bytes consumed. Err codes are from
[`ImageFile.ERRORS`](ImageFile.html#PIL.ImageFile.ERRORS
"PIL.ImageFile.ERRORS").

## `PsdImagePlugin` module¶

class PIL.PsdImagePlugin.PsdImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/PsdImagePlugin.html#PsdImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'PSD'¶

    

format_description = 'Adobe Photoshop'¶

    

property is_animated:
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)")¶

    

property layers: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in
Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.14\)"),
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in
Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")],
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[_Tile](ImageFile.html#PIL.ImageFile._Tile
"PIL.ImageFile._Tile")]]][[source]](../_modules/PIL/PsdImagePlugin.html#PsdImageFile.layers)¶

    

property n_frames: [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")¶

    

seek(_layer : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/PsdImagePlugin.html#PsdImageFile.seek)¶

    

Seeks to the given frame in this sequence file. If you seek beyond the end of
the sequence, the method raises an `EOFError` exception. When a sequence file
is opened, the library automatically seeks to frame 0.

See [`tell()`](Image.html#PIL.Image.Image.tell "PIL.Image.Image.tell").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Parameters:

    

**frame** – Frame number, starting at 0.

Raises:

    

[**EOFError**](https://docs.python.org/3/library/exceptions.html#EOFError
"\(in Python v3.14\)") – If the call attempts to seek beyond the end of the
sequence.

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/PsdImagePlugin.html#PsdImageFile.tell)¶

    

Returns the current frame number. See
[`seek()`](Image.html#PIL.Image.Image.seek "PIL.Image.Image.seek").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Returns:

    

Frame number, starting with 0.

## `SgiImagePlugin` module¶

class PIL.SgiImagePlugin.SGI16Decoder(_mode :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_, _* args:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_)[[source]](../_modules/PIL/SgiImagePlugin.html#SGI16Decoder)¶

    

Bases: [`PyDecoder`](ImageFile.html#PIL.ImageFile.PyDecoder
"PIL.ImageFile.PyDecoder")

decode(_buffer : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [SupportsArrayInterface](Image.html#PIL.Image.SupportsArrayInterface "PIL.Image.SupportsArrayInterface")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/SgiImagePlugin.html#SGI16Decoder.decode)¶
    

Override to perform the decoding process.

Parameters:

    

**buffer** – A bytes object with the data to be decoded.

Returns:

    

A tuple of `(bytes consumed, errcode)`. If finished with decoding return -1
for the bytes consumed. Err codes are from
[`ImageFile.ERRORS`](ImageFile.html#PIL.ImageFile.ERRORS
"PIL.ImageFile.ERRORS").

class PIL.SgiImagePlugin.SgiImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/SgiImagePlugin.html#SgiImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'SGI'¶

    

format_description = 'SGI Image File Format'¶

    

## `SpiderImagePlugin` module¶

class PIL.SpiderImagePlugin.SpiderImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/SpiderImagePlugin.html#SpiderImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

convert2byte(_depth :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 255_) -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/SpiderImagePlugin.html#SpiderImageFile.convert2byte)¶

    

format = 'SPIDER'¶

    

format_description = 'Spider 2D image'¶

    

property is_animated:
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)")¶

    

property n_frames: [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")¶

    

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/SpiderImagePlugin.html#SpiderImageFile.seek)¶

    

Seeks to the given frame in this sequence file. If you seek beyond the end of
the sequence, the method raises an `EOFError` exception. When a sequence file
is opened, the library automatically seeks to frame 0.

See [`tell()`](Image.html#PIL.Image.Image.tell "PIL.Image.Image.tell").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Parameters:

    

**frame** – Frame number, starting at 0.

Raises:

    

[**EOFError**](https://docs.python.org/3/library/exceptions.html#EOFError
"\(in Python v3.14\)") – If the call attempts to seek beyond the end of the
sequence.

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/SpiderImagePlugin.html#SpiderImageFile.tell)¶

    

Returns the current frame number. See
[`seek()`](Image.html#PIL.Image.Image.seek "PIL.Image.Image.seek").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Returns:

    

Frame number, starting with 0.

tkPhotoImage() -> [ImageTk.PhotoImage](ImageTk.html#PIL.ImageTk.PhotoImage
"PIL.ImageTk.PhotoImage")[[source]](../_modules/PIL/SpiderImagePlugin.html#SpiderImageFile.tkPhotoImage)¶

    

PIL.SpiderImagePlugin.isInt(_f :
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_) -> [int](https://docs.python.org/3/library/functions.html#int
"\(in Python
v3.14\)")[[source]](../_modules/PIL/SpiderImagePlugin.html#isInt)¶

    

PIL.SpiderImagePlugin.isSpiderHeader(_t :
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.14\)"), ...]_) ->
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")[[source]](../_modules/PIL/SpiderImagePlugin.html#isSpiderHeader)¶

    

PIL.SpiderImagePlugin.isSpiderImage(_filename :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_) -> [int](https://docs.python.org/3/library/functions.html#int
"\(in Python
v3.14\)")[[source]](../_modules/PIL/SpiderImagePlugin.html#isSpiderImage)¶

    

PIL.SpiderImagePlugin.loadImageSeries(_filelist : [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[Image](Image.html#PIL.Image.Image "PIL.Image.Image")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/SpiderImagePlugin.html#loadImageSeries)¶
    

create a list of [`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")
objects for use in a montage

PIL.SpiderImagePlugin.makeSpiderHeader(_im :
[Image](Image.html#PIL.Image.Image "PIL.Image.Image")_) ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python
v3.14\)")][[source]](../_modules/PIL/SpiderImagePlugin.html#makeSpiderHeader)¶

    

## `SunImagePlugin` module¶

class PIL.SunImagePlugin.SunImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/SunImagePlugin.html#SunImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'SUN'¶

    

format_description = 'Sun Raster File'¶

    

## `TgaImagePlugin` module¶

class PIL.TgaImagePlugin.TgaImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/TgaImagePlugin.html#TgaImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'TGA'¶

    

format_description = 'Targa'¶

    

load_end() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TgaImagePlugin.html#TgaImageFile.load_end)¶

    

## `TiffImagePlugin` module¶

class PIL.TiffImagePlugin.AppendingTiffWriter(_fn : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _new : [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = False_)[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter)¶
    

Bases: [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "\(in
Python v3.14\)")

Tags = {273, 288, 324, 519, 520, 521}¶

    

close() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.close)¶

    

Disable all I/O operations.

f: [IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python v3.14\)")]¶

    

fieldSizes = [0, 1, 1, 2, 4, 8, 1, 1, 2, 4, 8, 4, 8, 4, 2, 4, 8]¶

    

finalize() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.finalize)¶

    

fixIFD() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.fixIFD)¶

    

fixOffsets(_count : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _isShort :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = False_, _isLong :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = False_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.fixOffsets)¶

    

goToEnd() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.goToEnd)¶

    

newFrame() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.newFrame)¶

    

readLong() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.readLong)¶

    

readShort() -> [int](https://docs.python.org/3/library/functions.html#int
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.readShort)¶

    

rewriteLastLong(_value :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.rewriteLastLong)¶

    

rewriteLastShort(_value :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.rewriteLastShort)¶

    

rewriteLastShortToLong(_value :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.rewriteLastShortToLong)¶

    

seek(_offset : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_, _whence :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)") = 0_) -> [int](https://docs.python.org/3/library/functions.html#int
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.seek)¶

    

Parameters:

    

  * **offset** – Distance to seek.

  * **whence** – Whether the distance is relative to the start, end or current position.

Returns:

    

The resulting position, relative to the start.

setEndian(_endian : [str](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.setEndian)¶

    

setup() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.setup)¶

    

skipIFDs() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.skipIFDs)¶

    

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.tell)¶

    

Current file position, an integer.

write(_data : [Buffer](internal_modules.html#PIL._typing.Buffer
"PIL._typing.Buffer")_, _/_) ->
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.write)¶

    

Write bytes to file.

Return the number of bytes written.

writeLong(_value : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.writeLong)¶

    

writeShort(_value : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#AppendingTiffWriter.writeShort)¶

    

class PIL.TiffImagePlugin.IFDRational(_value : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [Fraction](https://docs.python.org/3/library/fractions.html#fractions.Fraction "\(in Python v3.14\)") | IFDRational_, _denominator : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 1_)[[source]](../_modules/PIL/TiffImagePlugin.html#IFDRational)¶
    

Bases:
[`Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational
"\(in Python v3.14\)")

Implements a rational class where 0/0 is a legal value to match the in the
wild use of exif rationals.

e.g., DigitalZoomRatio - 0.00/0.00 indicates that no digital zoom was used

property denominator:
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")¶

    

limit_rational(_max_denominator :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple
"\(in Python
v3.14\)")[[IntegralLike](internal_modules.html#PIL._typing.IntegralLike
"PIL._typing.IntegralLike"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")][[source]](../_modules/PIL/TiffImagePlugin.html#IFDRational.limit_rational)¶

    

Parameters:

    

**max_denominator** – Integer, the maximum denominator value

Returns:

    

Tuple of (numerator, denominator)

property numerator:
[IntegralLike](internal_modules.html#PIL._typing.IntegralLike
"PIL._typing.IntegralLike")¶

    

PIL.TiffImagePlugin.ImageFileDirectory¶

    

alias of `ImageFileDirectory_v1`

class PIL.TiffImagePlugin.ImageFileDirectory_v1(_* args:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_, _** kwargs:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_)[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v1)¶

    

Bases: `ImageFileDirectory_v2`

This class represents the **legacy** interface to a TIFF tag directory.

Exposes a dictionary interface of the tags in the directory:

    
    
    ifd = ImageFileDirectory_v1()
    ifd[key] = 'Some Data'
    ifd.tagtype[key] = TiffTags.ASCII
    print(ifd[key])
    ('Some Data',)
    

Also contains a dictionary of tag types as read from the tiff image file,
`tagtype`.

Values are returned as a tuple.

Deprecated since version 3.0.0.

classmethod from_v2(_original : ImageFileDirectory_v2_) ->
ImageFileDirectory_v1[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v1.from_v2)¶

    

Returns an `ImageFileDirectory_v1` instance with the same data as is contained
in the original `ImageFileDirectory_v2` instance.

Returns:

    

`ImageFileDirectory_v1`

property tagdata¶

    

property tags¶

    

tagtype: [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in
Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]¶

    

Dictionary of tag types

to_v2() ->
ImageFileDirectory_v2[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v1.to_v2)¶

    

Returns an `ImageFileDirectory_v2` instance with the same data as is contained
in the original `ImageFileDirectory_v1` instance.

Returns:

    

`ImageFileDirectory_v2`

class PIL.TiffImagePlugin.ImageFileDirectory_v2(_ifh : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") = b'II*\x00\x00\x00\x00\x00'_, _prefix : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _group : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2)¶
    

Bases:
[`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping
"\(in Python v3.14\)")

This class represents a TIFF tag directory. To speed things up, we don’t
decode tags unless they’re asked for.

Exposes a dictionary interface of the tags in the directory:

    
    
    ifd = ImageFileDirectory_v2()
    ifd[key] = 'Some Data'
    ifd.tagtype[key] = TiffTags.ASCII
    print(ifd[key])
    'Some Data'
    

Individual values are returned as the strings or numbers, sequences are
returned as tuples of the values.

The tiff metadata type of each item is stored in a dictionary of tag types in
`tagtype`. The types are read from a tiff file, guessed from the type added,
or added manually.

Data Structures:

>   * `self.tagtype = {}`
>
>     * Key: numerical TIFF tag number
>
>     * Value: integer corresponding to the data type from
> [`TiffTags.TYPES`](TiffTags.html#PIL.TiffTags.PIL.TiffTags.TYPES
> "PIL.TiffTags.PIL.TiffTags.TYPES")
>
> Added in version 3.0.0.
>
>

‘Internal’ data structures:

>   * `self._tags_v2 = {}`
>
>     * Key: numerical TIFF tag number
>
>     * Value: decoded data, as tuple for multiple values
>
>   * `self._tagdata = {}`
>
>     * Key: numerical TIFF tag number
>
>     * Value: undecoded byte string from file
>
>   * `self._tags_v1 = {}`
>
>     * Key: numerical TIFF tag number
>
>     * Value: decoded data in the v1 format
>
>

Tags will be found in the private attributes `self._tagdata`, and in
`self._tags_v2` once decoded.

`self.legacy_api` is a value for internal use, and shouldn’t be changed from
outside code. In cooperation with `ImageFileDirectory_v1`, if `legacy_api` is
true, then decoded tags will be populated into both `_tags_v1` and `_tags_v2`.
`_tags_v2` will be used if this IFD is used in the TIFF save routine. Tags
should be read from `_tags_v1` if `legacy_api == true`.

property legacy_api:
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)")¶

    

load(_fp : [IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in
Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python v3.14\)")]_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.load)¶

    

load_byte(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.load_byte)¶

    

load_double(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.14\)"), ...]¶

    

load_float(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.14\)"), ...]¶

    

load_long(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.14\)"), ...]¶

    

load_long8(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.14\)"), ...]¶

    

load_rational(_data : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _legacy_api : [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = True_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | IFDRational, ...][[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.load_rational)¶
    

load_short(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.14\)"), ...]¶

    

load_signed_byte(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.14\)"), ...]¶

    

load_signed_long(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.14\)"), ...]¶

    

load_signed_rational(_data : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _legacy_api : [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = True_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | IFDRational, ...][[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.load_signed_rational)¶
    

load_signed_short(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.14\)"), ...]¶

    

load_string(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.load_string)¶

    

load_undefined(_data :
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")_, _legacy_api :
[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.14\)") = True_) ->
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.load_undefined)¶

    

named() -> [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in
Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.14\)"),
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")][[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.named)¶

    

Returns:

    

dict of name|key: value

Returns the complete tag dictionary, with named tags where possible.

property offset¶

    

property prefix¶

    

reset() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.reset)¶

    

save(_fp : [IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in
Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python v3.14\)")]_) ->
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.save)¶

    

tagtype: [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in
Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")]¶

    

Dictionary of tag types

tobytes(_offset : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)") = 0_) ->
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.tobytes)¶

    

write_byte(_data : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | IFDRational_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.write_byte)¶
    

write_double(_* values_)¶

    

write_float(_* values_)¶

    

write_long(_* values_)¶

    

write_long8(_* values_)¶

    

write_rational(_* values: IFDRational_) ->
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.write_rational)¶

    

write_short(_* values_)¶

    

write_signed_byte(_* values_)¶

    

write_signed_long(_* values_)¶

    

write_signed_rational(_* values: IFDRational_) ->
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.write_signed_rational)¶

    

write_signed_short(_* values_)¶

    

write_string(_value : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.write_string)¶
    

write_undefined(_value : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | IFDRational_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#ImageFileDirectory_v2.write_undefined)¶
    

class PIL.TiffImagePlugin.TiffImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/TiffImagePlugin.html#TiffImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'TIFF'¶

    

format_description = 'Adobe TIFF'¶

    

get_photoshop_blocks() ->
[dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [dict](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)"),
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")]][[source]](../_modules/PIL/TiffImagePlugin.html#TiffImageFile.get_photoshop_blocks)¶

    

Returns a dictionary of Photoshop “Image Resource Blocks”. The keys are the
image resource ID. For more information, see <https://www.adobe.com/devnet-
apps/photoshop/fileformatashtml/#50577409_pgfId-1037727>

Returns:

    

Photoshop “Image Resource Blocks” in a dictionary.

load() -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#TiffImageFile.load)¶
    

Load image data based on tile list

load_end() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#TiffImageFile.load_end)¶

    

load_prepare() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#TiffImageFile.load_prepare)¶

    

property n_frames: [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")¶

    

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#TiffImageFile.seek)¶

    

Select a given frame as current image

tag: ImageFileDirectory_v1¶

    

Legacy tag entries

tag_v2: ImageFileDirectory_v2¶

    

Image file directory (tag dictionary)

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/TiffImagePlugin.html#TiffImageFile.tell)¶

    

Return the current frame number

## `WebPImagePlugin` module¶

class PIL.WebPImagePlugin.WebPImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/WebPImagePlugin.html#WebPImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'WEBP'¶

    

format_description = 'WebP image'¶

    

load() -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/WebPImagePlugin.html#WebPImageFile.load)¶
    

Load image data based on tile list

load_seek(_pos : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/WebPImagePlugin.html#WebPImageFile.load_seek)¶

    

seek(_frame : [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/WebPImagePlugin.html#WebPImageFile.seek)¶

    

Seeks to the given frame in this sequence file. If you seek beyond the end of
the sequence, the method raises an `EOFError` exception. When a sequence file
is opened, the library automatically seeks to frame 0.

See [`tell()`](Image.html#PIL.Image.Image.tell "PIL.Image.Image.tell").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Parameters:

    

**frame** – Frame number, starting at 0.

Raises:

    

[**EOFError**](https://docs.python.org/3/library/exceptions.html#EOFError
"\(in Python v3.14\)") – If the call attempts to seek beyond the end of the
sequence.

tell() -> [int](https://docs.python.org/3/library/functions.html#int "\(in
Python
v3.14\)")[[source]](../_modules/PIL/WebPImagePlugin.html#WebPImageFile.tell)¶

    

Returns the current frame number. See
[`seek()`](Image.html#PIL.Image.Image.seek "PIL.Image.Image.seek").

If defined, [`n_frames`](Image.html#PIL.Image.Image.n_frames
"PIL.Image.Image.n_frames") refers to the number of available frames.

Returns:

    

Frame number, starting with 0.

## `WmfImagePlugin` module¶

class PIL.WmfImagePlugin.WmfStubImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/WmfImagePlugin.html#WmfStubImageFile)¶
    

Bases: [`StubImageFile`](ImageFile.html#PIL.ImageFile.StubImageFile
"PIL.ImageFile.StubImageFile")

format = 'WMF'¶

    

format_description = 'Windows Metafile'¶

    

load(_dpi : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/WmfImagePlugin.html#WmfStubImageFile.load)¶
    

Load image data based on tile list

PIL.WmfImagePlugin.register_handler(_handler : [StubHandler](ImageFile.html#PIL.ImageFile.StubHandler "PIL.ImageFile.StubHandler") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/WmfImagePlugin.html#register_handler)¶
    

Install application-specific WMF image handler.

Parameters:

    

**handler** – Handler object.

## `XVThumbImagePlugin` module¶

class PIL.XVThumbImagePlugin.XVThumbImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/XVThumbImagePlugin.html#XVThumbImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'XVThumb'¶

    

format_description = 'XV thumbnail image'¶

    

## `XbmImagePlugin` module¶

class PIL.XbmImagePlugin.XbmImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/XbmImagePlugin.html#XbmImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'XBM'¶

    

format_description = 'X11 Bitmap'¶

    

## `XpmImagePlugin` module¶

class PIL.XpmImagePlugin.XpmDecoder(_mode :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_, _* args:
[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.14\)")_)[[source]](../_modules/PIL/XpmImagePlugin.html#XpmDecoder)¶

    

Bases: [`PyDecoder`](ImageFile.html#PIL.ImageFile.PyDecoder
"PIL.ImageFile.PyDecoder")

decode(_buffer : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [SupportsArrayInterface](Image.html#PIL.Image.SupportsArrayInterface "PIL.Image.SupportsArrayInterface")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/XpmImagePlugin.html#XpmDecoder.decode)¶
    

Override to perform the decoding process.

Parameters:

    

**buffer** – A bytes object with the data to be decoded.

Returns:

    

A tuple of `(bytes consumed, errcode)`. If finished with decoding return -1
for the bytes consumed. Err codes are from
[`ImageFile.ERRORS`](ImageFile.html#PIL.ImageFile.ERRORS
"PIL.ImageFile.ERRORS").

class PIL.XpmImagePlugin.XpmImageFile(_fp : [StrOrBytesPath](internal_modules.html#PIL._typing.StrOrBytesPath "PIL._typing.StrOrBytesPath") | IO[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")]_, _filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/XpmImagePlugin.html#XpmImageFile)¶
    

Bases: [`ImageFile`](ImageFile.html#PIL.ImageFile.ImageFile
"PIL.ImageFile.ImageFile")

format = 'XPM'¶

    

format_description = 'X11 Pixel Map'¶

    

load_read(_read_bytes :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/XpmImagePlugin.html#XpmImageFile.load_read)¶

    

[ Next Internal reference ](internal_design.html) [ Previous PIL package
(autodoc of remaining modules) ](../PIL.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * Plugin reference
    * `AvifImagePlugin` module
      * `AvifImageFile`
        * `AvifImageFile.format`
        * `AvifImageFile.format_description`
        * `AvifImageFile.load()`
        * `AvifImageFile.load_seek()`
        * `AvifImageFile.seek()`
        * `AvifImageFile.tell()`
      * `get_codec_version()`
    * `BmpImagePlugin` module
      * `BmpImageFile`
        * `BmpImageFile.BITFIELDS`
        * `BmpImageFile.COMPRESSIONS`
        * `BmpImageFile.JPEG`
        * `BmpImageFile.PNG`
        * `BmpImageFile.RAW`
        * `BmpImageFile.RLE4`
        * `BmpImageFile.RLE8`
        * `BmpImageFile.format`
        * `BmpImageFile.format_description`
        * `BmpImageFile.k`
        * `BmpImageFile.v`
      * `BmpRleDecoder`
        * `BmpRleDecoder.decode()`
      * `DibImageFile`
        * `DibImageFile.format`
        * `DibImageFile.format_description`
    * `BufrStubImagePlugin` module
      * `BufrStubImageFile`
        * `BufrStubImageFile.format`
        * `BufrStubImageFile.format_description`
      * `register_handler()`
    * `CurImagePlugin` module
      * `CurImageFile`
        * `CurImageFile.format`
        * `CurImageFile.format_description`
    * `DcxImagePlugin` module
      * `DcxImageFile`
        * `DcxImageFile.format`
        * `DcxImageFile.format_description`
        * `DcxImageFile.seek()`
        * `DcxImageFile.tell()`
    * `DdsImagePlugin` module
      * `D3DFMT`
        * `D3DFMT.A1`
        * `D3DFMT.A16B16G16R16`
        * `D3DFMT.A16B16G16R16F`
        * `D3DFMT.A1R5G5B5`
        * `D3DFMT.A2B10G10R10`
        * `D3DFMT.A2B10G10R10_XR_BIAS`
        * `D3DFMT.A2R10G10B10`
        * `D3DFMT.A2W10V10U10`
        * `D3DFMT.A32B32G32R32F`
        * `D3DFMT.A4L4`
        * `D3DFMT.A4R4G4B4`
        * `D3DFMT.A8`
        * `D3DFMT.A8B8G8R8`
        * `D3DFMT.A8L8`
        * `D3DFMT.A8P8`
        * `D3DFMT.A8R3G3B2`
        * `D3DFMT.A8R8G8B8`
        * `D3DFMT.ATI1`
        * `D3DFMT.ATI2`
        * `D3DFMT.BC4S`
        * `D3DFMT.BC4U`
        * `D3DFMT.BC5S`
        * `D3DFMT.BC5U`
        * `D3DFMT.BINARYBUFFER`
        * `D3DFMT.CxV8U8`
        * `D3DFMT.D15S1`
        * `D3DFMT.D16`
        * `D3DFMT.D16_LOCKABLE`
        * `D3DFMT.D24FS8`
        * `D3DFMT.D24S8`
        * `D3DFMT.D24X4S4`
        * `D3DFMT.D24X8`
        * `D3DFMT.D32`
        * `D3DFMT.D32F_LOCKABLE`
        * `D3DFMT.D32_LOCKABLE`
        * `D3DFMT.DX10`
        * `D3DFMT.DXT1`
        * `D3DFMT.DXT2`
        * `D3DFMT.DXT3`
        * `D3DFMT.DXT4`
        * `D3DFMT.DXT5`
        * `D3DFMT.G16R16`
        * `D3DFMT.G16R16F`
        * `D3DFMT.G32R32F`
        * `D3DFMT.G8R8_G8B8`
        * `D3DFMT.INDEX16`
        * `D3DFMT.INDEX32`
        * `D3DFMT.L16`
        * `D3DFMT.L6V5U5`
        * `D3DFMT.L8`
        * `D3DFMT.MULTI2_ARGB8`
        * `D3DFMT.P8`
        * `D3DFMT.Q16W16V16U16`
        * `D3DFMT.Q8W8V8U8`
        * `D3DFMT.R16F`
        * `D3DFMT.R32F`
        * `D3DFMT.R3G3B2`
        * `D3DFMT.R5G6B5`
        * `D3DFMT.R8G8B8`
        * `D3DFMT.R8G8_B8G8`
        * `D3DFMT.S8_LOCKABLE`
        * `D3DFMT.UNKNOWN`
        * `D3DFMT.UYVY`
        * `D3DFMT.V16U16`
        * `D3DFMT.V8U8`
        * `D3DFMT.VERTEXDATA`
        * `D3DFMT.X1R5G5B5`
        * `D3DFMT.X4R4G4B4`
        * `D3DFMT.X8B8G8R8`
        * `D3DFMT.X8L8V8U8`
        * `D3DFMT.X8R8G8B8`
        * `D3DFMT.YUY2`
      * `DDPF`
        * `DDPF.ALPHA`
        * `DDPF.ALPHAPIXELS`
        * `DDPF.FOURCC`
        * `DDPF.LUMINANCE`
        * `DDPF.PALETTEINDEXED8`
        * `DDPF.RGB`
      * `DDSCAPS`
        * `DDSCAPS.COMPLEX`
        * `DDSCAPS.MIPMAP`
        * `DDSCAPS.TEXTURE`
      * `DDSCAPS2`
        * `DDSCAPS2.CUBEMAP`
        * `DDSCAPS2.CUBEMAP_NEGATIVEX`
        * `DDSCAPS2.CUBEMAP_NEGATIVEY`
        * `DDSCAPS2.CUBEMAP_NEGATIVEZ`
        * `DDSCAPS2.CUBEMAP_POSITIVEX`
        * `DDSCAPS2.CUBEMAP_POSITIVEY`
        * `DDSCAPS2.CUBEMAP_POSITIVEZ`
        * `DDSCAPS2.VOLUME`
      * `DDSD`
        * `DDSD.CAPS`
        * `DDSD.DEPTH`
        * `DDSD.HEIGHT`
        * `DDSD.LINEARSIZE`
        * `DDSD.MIPMAPCOUNT`
        * `DDSD.PITCH`
        * `DDSD.PIXELFORMAT`
        * `DDSD.WIDTH`
      * `DXGI_FORMAT`
        * `DXGI_FORMAT.A8P8`
        * `DXGI_FORMAT.A8_UNORM`
        * `DXGI_FORMAT.AI44`
        * `DXGI_FORMAT.AYUV`
        * `DXGI_FORMAT.B4G4R4A4_UNORM`
        * `DXGI_FORMAT.B5G5R5A1_UNORM`
        * `DXGI_FORMAT.B5G6R5_UNORM`
        * `DXGI_FORMAT.B8G8R8A8_TYPELESS`
        * `DXGI_FORMAT.B8G8R8A8_UNORM`
        * `DXGI_FORMAT.B8G8R8A8_UNORM_SRGB`
        * `DXGI_FORMAT.B8G8R8X8_TYPELESS`
        * `DXGI_FORMAT.B8G8R8X8_UNORM`
        * `DXGI_FORMAT.B8G8R8X8_UNORM_SRGB`
        * `DXGI_FORMAT.BC1_TYPELESS`
        * `DXGI_FORMAT.BC1_UNORM`
        * `DXGI_FORMAT.BC1_UNORM_SRGB`
        * `DXGI_FORMAT.BC2_TYPELESS`
        * `DXGI_FORMAT.BC2_UNORM`
        * `DXGI_FORMAT.BC2_UNORM_SRGB`
        * `DXGI_FORMAT.BC3_TYPELESS`
        * `DXGI_FORMAT.BC3_UNORM`
        * `DXGI_FORMAT.BC3_UNORM_SRGB`
        * `DXGI_FORMAT.BC4_SNORM`
        * `DXGI_FORMAT.BC4_TYPELESS`
        * `DXGI_FORMAT.BC4_UNORM`
        * `DXGI_FORMAT.BC5_SNORM`
        * `DXGI_FORMAT.BC5_TYPELESS`
        * `DXGI_FORMAT.BC5_UNORM`
        * `DXGI_FORMAT.BC6H_SF16`
        * `DXGI_FORMAT.BC6H_TYPELESS`
        * `DXGI_FORMAT.BC6H_UF16`
        * `DXGI_FORMAT.BC7_TYPELESS`
        * `DXGI_FORMAT.BC7_UNORM`
        * `DXGI_FORMAT.BC7_UNORM_SRGB`
        * `DXGI_FORMAT.D16_UNORM`
        * `DXGI_FORMAT.D24_UNORM_S8_UINT`
        * `DXGI_FORMAT.D32_FLOAT`
        * `DXGI_FORMAT.D32_FLOAT_S8X24_UINT`
        * `DXGI_FORMAT.G8R8_G8B8_UNORM`
        * `DXGI_FORMAT.IA44`
        * `DXGI_FORMAT.NV11`
        * `DXGI_FORMAT.NV12`
        * `DXGI_FORMAT.OPAQUE_420`
        * `DXGI_FORMAT.P010`
        * `DXGI_FORMAT.P016`
        * `DXGI_FORMAT.P208`
        * `DXGI_FORMAT.P8`
        * `DXGI_FORMAT.R10G10B10A2_TYPELESS`
        * `DXGI_FORMAT.R10G10B10A2_UINT`
        * `DXGI_FORMAT.R10G10B10A2_UNORM`
        * `DXGI_FORMAT.R10G10B10_XR_BIAS_A2_UNORM`
        * `DXGI_FORMAT.R11G11B10_FLOAT`
        * `DXGI_FORMAT.R16G16B16A16_FLOAT`
        * `DXGI_FORMAT.R16G16B16A16_SINT`
        * `DXGI_FORMAT.R16G16B16A16_SNORM`
        * `DXGI_FORMAT.R16G16B16A16_TYPELESS`
        * `DXGI_FORMAT.R16G16B16A16_UINT`
        * `DXGI_FORMAT.R16G16B16A16_UNORM`
        * `DXGI_FORMAT.R16G16_FLOAT`
        * `DXGI_FORMAT.R16G16_SINT`
        * `DXGI_FORMAT.R16G16_SNORM`
        * `DXGI_FORMAT.R16G16_TYPELESS`
        * `DXGI_FORMAT.R16G16_UINT`
        * `DXGI_FORMAT.R16G16_UNORM`
        * `DXGI_FORMAT.R16_FLOAT`
        * `DXGI_FORMAT.R16_SINT`
        * `DXGI_FORMAT.R16_SNORM`
        * `DXGI_FORMAT.R16_TYPELESS`
        * `DXGI_FORMAT.R16_UINT`
        * `DXGI_FORMAT.R16_UNORM`
        * `DXGI_FORMAT.R1_UNORM`
        * `DXGI_FORMAT.R24G8_TYPELESS`
        * `DXGI_FORMAT.R24_UNORM_X8_TYPELESS`
        * `DXGI_FORMAT.R32G32B32A32_FLOAT`
        * `DXGI_FORMAT.R32G32B32A32_SINT`
        * `DXGI_FORMAT.R32G32B32A32_TYPELESS`
        * `DXGI_FORMAT.R32G32B32A32_UINT`
        * `DXGI_FORMAT.R32G32B32_FLOAT`
        * `DXGI_FORMAT.R32G32B32_SINT`
        * `DXGI_FORMAT.R32G32B32_TYPELESS`
        * `DXGI_FORMAT.R32G32B32_UINT`
        * `DXGI_FORMAT.R32G32_FLOAT`
        * `DXGI_FORMAT.R32G32_SINT`
        * `DXGI_FORMAT.R32G32_TYPELESS`
        * `DXGI_FORMAT.R32G32_UINT`
        * `DXGI_FORMAT.R32G8X24_TYPELESS`
        * `DXGI_FORMAT.R32_FLOAT`
        * `DXGI_FORMAT.R32_FLOAT_X8X24_TYPELESS`
        * `DXGI_FORMAT.R32_SINT`
        * `DXGI_FORMAT.R32_TYPELESS`
        * `DXGI_FORMAT.R32_UINT`
        * `DXGI_FORMAT.R8G8B8A8_SINT`
        * `DXGI_FORMAT.R8G8B8A8_SNORM`
        * `DXGI_FORMAT.R8G8B8A8_TYPELESS`
        * `DXGI_FORMAT.R8G8B8A8_UINT`
        * `DXGI_FORMAT.R8G8B8A8_UNORM`
        * `DXGI_FORMAT.R8G8B8A8_UNORM_SRGB`
        * `DXGI_FORMAT.R8G8_B8G8_UNORM`
        * `DXGI_FORMAT.R8G8_SINT`
        * `DXGI_FORMAT.R8G8_SNORM`
        * `DXGI_FORMAT.R8G8_TYPELESS`
        * `DXGI_FORMAT.R8G8_UINT`
        * `DXGI_FORMAT.R8G8_UNORM`
        * `DXGI_FORMAT.R8_SINT`
        * `DXGI_FORMAT.R8_SNORM`
        * `DXGI_FORMAT.R8_TYPELESS`
        * `DXGI_FORMAT.R8_UINT`
        * `DXGI_FORMAT.R8_UNORM`
        * `DXGI_FORMAT.R9G9B9E5_SHAREDEXP`
        * `DXGI_FORMAT.SAMPLER_FEEDBACK_MIN_MIP_OPAQUE`
        * `DXGI_FORMAT.SAMPLER_FEEDBACK_MIP_REGION_USED_OPAQUE`
        * `DXGI_FORMAT.UNKNOWN`
        * `DXGI_FORMAT.V208`
        * `DXGI_FORMAT.V408`
        * `DXGI_FORMAT.X24_TYPELESS_G8_UINT`
        * `DXGI_FORMAT.X32_TYPELESS_G8X24_UINT`
        * `DXGI_FORMAT.Y210`
        * `DXGI_FORMAT.Y216`
        * `DXGI_FORMAT.Y410`
        * `DXGI_FORMAT.Y416`
        * `DXGI_FORMAT.YUY2`
      * `DdsImageFile`
        * `DdsImageFile.format`
        * `DdsImageFile.format_description`
        * `DdsImageFile.load_seek()`
      * `DdsRgbDecoder`
        * `DdsRgbDecoder.decode()`
    * `EpsImagePlugin` module
      * `EpsImageFile`
        * `EpsImageFile.format`
        * `EpsImageFile.format_description`
        * `EpsImageFile.load()`
        * `EpsImageFile.load_seek()`
        * `EpsImageFile.mode_map`
      * `Ghostscript()`
      * `has_ghostscript()`
    * `FitsImagePlugin` module
      * `FitsGzipDecoder`
        * `FitsGzipDecoder.decode()`
      * `FitsImageFile`
        * `FitsImageFile.format`
        * `FitsImageFile.format_description`
    * `FliImagePlugin` module
      * `FliImageFile`
        * `FliImageFile.format`
        * `FliImageFile.format_description`
        * `FliImageFile.seek()`
        * `FliImageFile.tell()`
    * `FpxImagePlugin` module
      * `FpxImageFile`
        * `FpxImageFile.close()`
        * `FpxImageFile.format`
        * `FpxImageFile.format_description`
        * `FpxImageFile.load()`
    * `GbrImagePlugin` module
      * `GbrImageFile`
        * `GbrImageFile.format`
        * `GbrImageFile.format_description`
        * `GbrImageFile.load()`
    * `GifImagePlugin` module
      * `GifImageFile`
        * `GifImageFile.data()`
        * `GifImageFile.format`
        * `GifImageFile.format_description`
        * `GifImageFile.global_palette`
        * `GifImageFile.is_animated`
        * `GifImageFile.load_end()`
        * `GifImageFile.load_prepare()`
        * `GifImageFile.n_frames`
        * `GifImageFile.seek()`
        * `GifImageFile.tell()`
      * `LOADING_STRATEGY`
      * `LoadingStrategy`
        * `LoadingStrategy.RGB_AFTER_DIFFERENT_PALETTE_ONLY`
        * `LoadingStrategy.RGB_AFTER_FIRST`
        * `LoadingStrategy.RGB_ALWAYS`
      * `get_interlace()`
      * `getdata()`
      * `getheader()`
    * `GribStubImagePlugin` module
      * `GribStubImageFile`
        * `GribStubImageFile.format`
        * `GribStubImageFile.format_description`
      * `register_handler()`
    * `Hdf5StubImagePlugin` module
      * `HDF5StubImageFile`
        * `HDF5StubImageFile.format`
        * `HDF5StubImageFile.format_description`
      * `register_handler()`
    * `IcnsImagePlugin` module
      * `IcnsFile`
        * `IcnsFile.SIZES`
        * `IcnsFile.bestsize()`
        * `IcnsFile.dataforsize()`
        * `IcnsFile.getimage()`
        * `IcnsFile.itersizes()`
      * `IcnsImageFile`
        * `IcnsImageFile.format`
        * `IcnsImageFile.format_description`
        * `IcnsImageFile.load()`
        * `IcnsImageFile.size`
      * `nextheader()`
      * `read_32()`
      * `read_32t()`
      * `read_mk()`
      * `read_png_or_jpeg2000()`
    * `IcoImagePlugin` module
      * `IcoFile`
        * `IcoFile.frame()`
        * `IcoFile.getentryindex()`
        * `IcoFile.getimage()`
        * `IcoFile.sizes()`
      * `IcoImageFile`
        * `IcoImageFile.format`
        * `IcoImageFile.format_description`
        * `IcoImageFile.load()`
        * `IcoImageFile.load_seek()`
        * `IcoImageFile.size`
      * `IconHeader`
        * `IconHeader.bpp`
        * `IconHeader.color_depth`
        * `IconHeader.dim`
        * `IconHeader.height`
        * `IconHeader.nb_color`
        * `IconHeader.offset`
        * `IconHeader.planes`
        * `IconHeader.reserved`
        * `IconHeader.size`
        * `IconHeader.square`
        * `IconHeader.width`
    * `ImImagePlugin` module
      * `ImImageFile`
        * `ImImageFile.format`
        * `ImImageFile.format_description`
        * `ImImageFile.is_animated`
        * `ImImageFile.n_frames`
        * `ImImageFile.seek()`
        * `ImImageFile.tell()`
      * `number()`
    * `ImtImagePlugin` module
      * `ImtImageFile`
        * `ImtImageFile.format`
        * `ImtImageFile.format_description`
    * `IptcImagePlugin` module
      * `IptcImageFile`
        * `IptcImageFile.field()`
        * `IptcImageFile.format`
        * `IptcImageFile.format_description`
        * `IptcImageFile.getint()`
        * `IptcImageFile.load()`
      * `getiptcinfo()`
    * `JpegImagePlugin` module
      * `APP()`
      * `COM()`
      * `DQT()`
      * `JpegImageFile`
        * `JpegImageFile.draft()`
        * `JpegImageFile.format`
        * `JpegImageFile.format_description`
        * `JpegImageFile.load_djpeg()`
        * `JpegImageFile.load_read()`
      * `SOF()`
      * `Skip()`
      * `get_sampling()`
      * `jpeg_factory()`
    * `Jpeg2KImagePlugin` module
      * `BoxReader`
        * `BoxReader.has_next_box()`
        * `BoxReader.next_box_type()`
        * `BoxReader.read_boxes()`
        * `BoxReader.read_fields()`
      * `Jpeg2KImageFile`
        * `Jpeg2KImageFile.format`
        * `Jpeg2KImageFile.format_description`
        * `Jpeg2KImageFile.load()`
        * `Jpeg2KImageFile.reduce`
    * `McIdasImagePlugin` module
      * `McIdasImageFile`
        * `McIdasImageFile.format`
        * `McIdasImageFile.format_description`
    * `MicImagePlugin` module
      * `MicImageFile`
        * `MicImageFile.close()`
        * `MicImageFile.format`
        * `MicImageFile.format_description`
        * `MicImageFile.seek()`
        * `MicImageFile.tell()`
    * `MpegImagePlugin` module
      * `BitStream`
        * `BitStream.next()`
        * `BitStream.peek()`
        * `BitStream.read()`
        * `BitStream.skip()`
      * `MpegImageFile`
        * `MpegImageFile.format`
        * `MpegImageFile.format_description`
    * `MpoImagePlugin` module
      * `MpoImageFile`
        * `MpoImageFile.adopt()`
        * `MpoImageFile.format`
        * `MpoImageFile.format_description`
        * `MpoImageFile.load_seek()`
        * `MpoImageFile.seek()`
        * `MpoImageFile.tell()`
    * `MspImagePlugin` module
      * `MspDecoder`
        * `MspDecoder.decode()`
      * `MspImageFile`
        * `MspImageFile.format`
        * `MspImageFile.format_description`
    * `PalmImagePlugin` module
      * `build_prototype_image()`
    * `PcdImagePlugin` module
      * `PcdImageFile`
        * `PcdImageFile.format`
        * `PcdImageFile.format_description`
        * `PcdImageFile.load_end()`
        * `PcdImageFile.load_prepare()`
    * `PcxImagePlugin` module
      * `PcxImageFile`
        * `PcxImageFile.format`
        * `PcxImageFile.format_description`
    * `PdfImagePlugin` module
    * `PixarImagePlugin` module
      * `PixarImageFile`
        * `PixarImageFile.format`
        * `PixarImageFile.format_description`
    * `PngImagePlugin` module
      * `Blend`
        * `Blend.OP_OVER`
        * `Blend.OP_SOURCE`
      * `ChunkStream`
        * `ChunkStream.call()`
        * `ChunkStream.close()`
        * `ChunkStream.crc()`
        * `ChunkStream.crc_skip()`
        * `ChunkStream.push()`
        * `ChunkStream.read()`
        * `ChunkStream.verify()`
        * `ChunkStream.fp`
        * `ChunkStream.queue`
      * `Disposal`
        * `Disposal.OP_BACKGROUND`
        * `Disposal.OP_NONE`
        * `Disposal.OP_PREVIOUS`
      * `PngImageFile`
        * `PngImageFile.getexif()`
        * `PngImageFile.load_end()`
        * `PngImageFile.load_prepare()`
        * `PngImageFile.load_read()`
        * `PngImageFile.seek()`
        * `PngImageFile.tell()`
        * `PngImageFile.verify()`
        * `PngImageFile.format`
        * `PngImageFile.format_description`
        * `PngImageFile.text`
      * `PngStream`
        * `PngStream.check_text_memory()`
        * `PngStream.chunk_IDAT()`
        * `PngStream.chunk_IEND()`
        * `PngStream.chunk_IHDR()`
        * `PngStream.chunk_PLTE()`
        * `PngStream.chunk_acTL()`
        * `PngStream.chunk_cHRM()`
        * `PngStream.chunk_eXIf()`
        * `PngStream.chunk_fcTL()`
        * `PngStream.chunk_fdAT()`
        * `PngStream.chunk_gAMA()`
        * `PngStream.chunk_iCCP()`
        * `PngStream.chunk_iTXt()`
        * `PngStream.chunk_pHYs()`
        * `PngStream.chunk_sRGB()`
        * `PngStream.chunk_tEXt()`
        * `PngStream.chunk_tRNS()`
        * `PngStream.chunk_zTXt()`
        * `PngStream.rewind()`
        * `PngStream.save_rewind()`
        * `PngStream.im_custom_mimetype`
        * `PngStream.im_info`
        * `PngStream.im_n_frames`
        * `PngStream.im_palette`
        * `PngStream.im_text`
        * `PngStream.im_tile`
      * `getchunks()`
      * `is_cid()`
      * `putchunk()`
      * `MAX_TEXT_CHUNK`
      * `MAX_TEXT_MEMORY`
    * `PpmImagePlugin` module
      * `PpmDecoder`
        * `PpmDecoder.decode()`
      * `PpmImageFile`
        * `PpmImageFile.format`
        * `PpmImageFile.format_description`
      * `PpmPlainDecoder`
        * `PpmPlainDecoder.decode()`
    * `PsdImagePlugin` module
      * `PsdImageFile`
        * `PsdImageFile.format`
        * `PsdImageFile.format_description`
        * `PsdImageFile.is_animated`
        * `PsdImageFile.layers`
        * `PsdImageFile.n_frames`
        * `PsdImageFile.seek()`
        * `PsdImageFile.tell()`
    * `SgiImagePlugin` module
      * `SGI16Decoder`
        * `SGI16Decoder.decode()`
      * `SgiImageFile`
        * `SgiImageFile.format`
        * `SgiImageFile.format_description`
    * `SpiderImagePlugin` module
      * `SpiderImageFile`
        * `SpiderImageFile.convert2byte()`
        * `SpiderImageFile.format`
        * `SpiderImageFile.format_description`
        * `SpiderImageFile.is_animated`
        * `SpiderImageFile.n_frames`
        * `SpiderImageFile.seek()`
        * `SpiderImageFile.tell()`
        * `SpiderImageFile.tkPhotoImage()`
      * `isInt()`
      * `isSpiderHeader()`
      * `isSpiderImage()`
      * `loadImageSeries()`
      * `makeSpiderHeader()`
    * `SunImagePlugin` module
      * `SunImageFile`
        * `SunImageFile.format`
        * `SunImageFile.format_description`
    * `TgaImagePlugin` module
      * `TgaImageFile`
        * `TgaImageFile.format`
        * `TgaImageFile.format_description`
        * `TgaImageFile.load_end()`
    * `TiffImagePlugin` module
      * `AppendingTiffWriter`
        * `AppendingTiffWriter.Tags`
        * `AppendingTiffWriter.close()`
        * `AppendingTiffWriter.f`
        * `AppendingTiffWriter.fieldSizes`
        * `AppendingTiffWriter.finalize()`
        * `AppendingTiffWriter.fixIFD()`
        * `AppendingTiffWriter.fixOffsets()`
        * `AppendingTiffWriter.goToEnd()`
        * `AppendingTiffWriter.newFrame()`
        * `AppendingTiffWriter.readLong()`
        * `AppendingTiffWriter.readShort()`
        * `AppendingTiffWriter.rewriteLastLong()`
        * `AppendingTiffWriter.rewriteLastShort()`
        * `AppendingTiffWriter.rewriteLastShortToLong()`
        * `AppendingTiffWriter.seek()`
        * `AppendingTiffWriter.setEndian()`
        * `AppendingTiffWriter.setup()`
        * `AppendingTiffWriter.skipIFDs()`
        * `AppendingTiffWriter.tell()`
        * `AppendingTiffWriter.write()`
        * `AppendingTiffWriter.writeLong()`
        * `AppendingTiffWriter.writeShort()`
      * `IFDRational`
        * `IFDRational.denominator`
        * `IFDRational.limit_rational()`
        * `IFDRational.numerator`
      * `ImageFileDirectory`
      * `ImageFileDirectory_v1`
        * `ImageFileDirectory_v1.from_v2()`
        * `ImageFileDirectory_v1.tagdata`
        * `ImageFileDirectory_v1.tags`
        * `ImageFileDirectory_v1.tagtype`
        * `ImageFileDirectory_v1.to_v2()`
      * `ImageFileDirectory_v2`
        * `ImageFileDirectory_v2.legacy_api`
        * `ImageFileDirectory_v2.load()`
        * `ImageFileDirectory_v2.load_byte()`
        * `ImageFileDirectory_v2.load_double()`
        * `ImageFileDirectory_v2.load_float()`
        * `ImageFileDirectory_v2.load_long()`
        * `ImageFileDirectory_v2.load_long8()`
        * `ImageFileDirectory_v2.load_rational()`
        * `ImageFileDirectory_v2.load_short()`
        * `ImageFileDirectory_v2.load_signed_byte()`
        * `ImageFileDirectory_v2.load_signed_long()`
        * `ImageFileDirectory_v2.load_signed_rational()`
        * `ImageFileDirectory_v2.load_signed_short()`
        * `ImageFileDirectory_v2.load_string()`
        * `ImageFileDirectory_v2.load_undefined()`
        * `ImageFileDirectory_v2.named()`
        * `ImageFileDirectory_v2.offset`
        * `ImageFileDirectory_v2.prefix`
        * `ImageFileDirectory_v2.reset()`
        * `ImageFileDirectory_v2.save()`
        * `ImageFileDirectory_v2.tagtype`
        * `ImageFileDirectory_v2.tobytes()`
        * `ImageFileDirectory_v2.write_byte()`
        * `ImageFileDirectory_v2.write_double()`
        * `ImageFileDirectory_v2.write_float()`
        * `ImageFileDirectory_v2.write_long()`
        * `ImageFileDirectory_v2.write_long8()`
        * `ImageFileDirectory_v2.write_rational()`
        * `ImageFileDirectory_v2.write_short()`
        * `ImageFileDirectory_v2.write_signed_byte()`
        * `ImageFileDirectory_v2.write_signed_long()`
        * `ImageFileDirectory_v2.write_signed_rational()`
        * `ImageFileDirectory_v2.write_signed_short()`
        * `ImageFileDirectory_v2.write_string()`
        * `ImageFileDirectory_v2.write_undefined()`
      * `TiffImageFile`
        * `TiffImageFile.format`
        * `TiffImageFile.format_description`
        * `TiffImageFile.get_photoshop_blocks()`
        * `TiffImageFile.load()`
        * `TiffImageFile.load_end()`
        * `TiffImageFile.load_prepare()`
        * `TiffImageFile.n_frames`
        * `TiffImageFile.seek()`
        * `TiffImageFile.tag`
        * `TiffImageFile.tag_v2`
        * `TiffImageFile.tell()`
    * `WebPImagePlugin` module
      * `WebPImageFile`
        * `WebPImageFile.format`
        * `WebPImageFile.format_description`
        * `WebPImageFile.load()`
        * `WebPImageFile.load_seek()`
        * `WebPImageFile.seek()`
        * `WebPImageFile.tell()`
    * `WmfImagePlugin` module
      * `WmfStubImageFile`
        * `WmfStubImageFile.format`
        * `WmfStubImageFile.format_description`
        * `WmfStubImageFile.load()`
      * `register_handler()`
    * `XVThumbImagePlugin` module
      * `XVThumbImageFile`
        * `XVThumbImageFile.format`
        * `XVThumbImageFile.format_description`
    * `XbmImagePlugin` module
      * `XbmImageFile`
        * `XbmImageFile.format`
        * `XbmImageFile.format_description`
    * `XpmImagePlugin` module
      * `XpmDecoder`
        * `XpmDecoder.decode()`
      * `XpmImageFile`
        * `XpmImageFile.format`
        * `XpmImageFile.format_description`
        * `XpmImageFile.load_read()`

  *[/]: Positional-only parameter separator (PEP 570)

