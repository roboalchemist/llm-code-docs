# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageFile.html
# Path: reference/ImageFile.html

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
    * `ImageFile` module
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

[ View this page ](../_sources/reference/ImageFile.rst.txt "View this page")

# `ImageFile` module¶

The `ImageFile` module provides support functions for the image open and save
functions.

In addition, it provides a `Parser` class which can be used to decode an image
piece by piece (e.g. while receiving it over a network connection). This class
implements the same consumer interface as the standard **sgmllib** and
**xmllib** modules.

## Example: Parse an image¶

    
    
    from PIL import ImageFile
    
    fp = open("hopper.ppm", "rb")
    
    p = ImageFile.Parser()
    
    while 1:
        s = fp.read(1024)
        if not s:
            break
        p.feed(s)
    
    im = p.close()
    
    im.save("copy.jpg")
    

## Classes¶

class PIL.ImageFile._Tile[[source]](../_modules/PIL/ImageFile.html#_Tile)¶

    

Bases:
[`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple
"\(in Python v3.14\)")

_Tile(codec_name, extents, offset, args)

codec_name: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)")¶

    

Alias for field number 0

extents: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

Alias for field number 1

offset: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

Alias for field number 2

args: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)"), ...] | [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

Alias for field number 3

class PIL.ImageFile.Parser[[source]](../_modules/PIL/ImageFile.html#Parser)¶

    

Incremental image parser. This class implements the standard feed/close
consumer interface.

close() -> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageFile.html#Parser.close)¶

    

(Consumer) Close the stream.

Returns:

    

An image object.

Raises:

    

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "\(in
Python v3.14\)") – If the parser failed to parse the image file either because
it cannot be identified or cannot be decoded.

feed(_data : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python v3.14\)")_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageFile.html#Parser.feed)¶

    

(Consumer) Feed data to the parser.

Parameters:

    

**data** – A string buffer.

Raises:

    

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "\(in
Python v3.14\)") – If the parser failed to parse the image file.

reset() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python v3.14\)")[[source]](../_modules/PIL/ImageFile.html#Parser.reset)¶

    

(Consumer) Reset the parser. Note that you can only call this method
immediately after you’ve created a parser; parser instances cannot be reused.

class PIL.ImageFile.PyCodec[[source]](../_modules/PIL/ImageFile.html#PyCodec)¶

    

cleanup() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageFile.html#PyCodec.cleanup)¶

    

Override to perform codec specific cleanup

Returns:

    

None

init(_args : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple
"\(in Python
v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.14\)"), ...]_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageFile.html#PyCodec.init)¶

    

Override to perform codec specific initialization

Parameters:

    

**args** – Tuple of arg items from the tile entry

Returns:

    

None

setfd(_fd : [IO](https://docs.python.org/3/library/typing.html#typing.IO "\(in
Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python v3.14\)")]_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageFile.html#PyCodec.setfd)¶

    

Called from ImageFile to set the Python file-like object

Parameters:

    

**fd** – A Python file-like object

Returns:

    

None

setimage(_im : [Image.core.ImagingCore](internal_modules.html#PIL.Image.core.ImagingCore "PIL.Image.core.ImagingCore")_, _extents : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageFile.html#PyCodec.setimage)¶
    

Called from ImageFile to set the core output image for the codec

Parameters:

    

  * **im** – A core image object

  * **extents** – a 4 tuple of (x0, y0, x1, y1) defining the rectangle for this tile

Returns:

    

None

class
PIL.ImageFile.PyDecoder[[source]](../_modules/PIL/ImageFile.html#PyDecoder)¶

    

Bases: `PyCodec`

Python implementation of a format decoder. Override this class and add the
decoding logic in the `decode()` method.

See [Writing Your Own File Codec in Python](../handbook/writing-your-own-
image-plugin.html#file-codecs-py)

decode(_buffer : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [SupportsArrayInterface](Image.html#PIL.Image.SupportsArrayInterface "PIL.Image.SupportsArrayInterface")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/ImageFile.html#PyDecoder.decode)¶
    

Override to perform the decoding process.

Parameters:

    

**buffer** – A bytes object with the data to be decoded.

Returns:

    

A tuple of `(bytes consumed, errcode)`. If finished with decoding return -1
for the bytes consumed. Err codes are from `ImageFile.ERRORS`.

set_as_raw(_data : [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _rawmode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _extra : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)"), ...] = ()_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageFile.html#PyDecoder.set_as_raw)¶
    

Convenience method to set the internal image from a stream of raw data

Parameters:

    

  * **data** – Bytes to be set

  * **rawmode** – The rawmode to be used for the decoder. If not specified, it will default to the mode of the image

  * **extra** – Extra arguments for the decoder.

Returns:

    

None

class
PIL.ImageFile.PyEncoder[[source]](../_modules/PIL/ImageFile.html#PyEncoder)¶

    

Bases: `PyCodec`

Python implementation of a format encoder. Override this class and add the
decoding logic in the `encode()` method.

See [Writing Your Own File Codec in Python](../handbook/writing-your-own-
image-plugin.html#file-codecs-py)

encode(_bufsize : [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")_) ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)"),
[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python
v3.14\)")][[source]](../_modules/PIL/ImageFile.html#PyEncoder.encode)¶

    

Override to perform the encoding process.

Parameters:

    

**bufsize** – Buffer size.

Returns:

    

A tuple of `(bytes encoded, errcode, bytes)`. If finished with encoding return
1 for the error code. Err codes are from `ImageFile.ERRORS`.

encode_to_file(_fh :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_, _bufsize :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) -> [int](https://docs.python.org/3/library/functions.html#int
"\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageFile.html#PyEncoder.encode_to_file)¶

    

Parameters:

    

  * **fh** – File handle.

  * **bufsize** – Buffer size.

Returns:

    

If finished successfully, return 0. Otherwise, return an error code. Err codes
are from `ImageFile.ERRORS`.

encode_to_pyfd() ->
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python
v3.14\)")][[source]](../_modules/PIL/ImageFile.html#PyEncoder.encode_to_pyfd)¶

    

If `pushes_fd` is `True`, then this method will be used, and `encode()` will
only be called once.

Returns:

    

A tuple of `(bytes consumed, errcode)`. Err codes are from `ImageFile.ERRORS`.

class
PIL.ImageFile.ImageFile[[source]](../_modules/PIL/ImageFile.html#ImageFile)¶

    

Bases: [`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")

Base class for image file format handlers.

custom_mimetype: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

tile: [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[_Tile]¶

    

A list of tile descriptors

decoderconfig: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple
"\(in Python v3.14\)")[Any, ...]¶

    

close() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python v3.14\)")[[source]](../_modules/PIL/ImageFile.html#ImageFile.close)¶

    

Closes the file pointer, if possible.

This operation will destroy the image core and release its memory. The image
data will be unusable afterward.

This function is required to close images that have multiple frames or have
not had their file read and closed by the
[`load()`](Image.html#PIL.Image.Image.load "PIL.Image.Image.load") method. See
[File handling in Pillow](open_files.html#file-handling) for more information.

get_child_images() ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[ImageFile][[source]](../_modules/PIL/ImageFile.html#ImageFile.get_child_images)¶

    

get_format_mimetype() -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageFile.html#ImageFile.get_format_mimetype)¶
    

verify() -> [None](https://docs.python.org/3/library/constants.html#None "\(in
Python v3.14\)")[[source]](../_modules/PIL/ImageFile.html#ImageFile.verify)¶

    

Check file integrity

load() -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageFile.html#ImageFile.load)¶
    

Load image data based on tile list

load_prepare() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageFile.html#ImageFile.load_prepare)¶

    

load_end() -> [None](https://docs.python.org/3/library/constants.html#None
"\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageFile.html#ImageFile.load_end)¶

    

class
PIL.ImageFile.StubHandler[[source]](../_modules/PIL/ImageFile.html#StubHandler)¶

    

Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC "\(in Python
v3.14\)")

class
PIL.ImageFile.StubImageFile[[source]](../_modules/PIL/ImageFile.html#StubImageFile)¶

    

Bases: `ImageFile`

Base class for stub image loaders.

A stub loader is an image loader that can identify files of a certain format,
but relies on external code to load the file.

load() -> [Image.core.PixelAccess](PixelAccess.html#PixelAccess "PIL.Image.core.PixelAccess") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageFile.html#StubImageFile.load)¶
    

Load image data based on tile list

## Constants¶

PIL.ImageFile.LOAD_TRUNCATED_IMAGES = False¶

    

Whether or not to load truncated image files. User code may change this.

PIL.ImageFile.MAXBLOCK = 65536¶

    

By default, Pillow processes image data in blocks. This helps to prevent
excessive use of resources. Codecs may disable this behaviour with `_pulls_fd`
or `_pushes_fd`.

When reading an image, this is the number of bytes to read at once.

When writing an image, this is the number of bytes to write at once. If the
image width times 4 is greater, then that will be used instead. Plugins may
also set a greater number.

User code may set this to another number.

PIL.ImageFile.ERRORS¶

    

Dict of known error codes returned from `PyDecoder.decode()`,
`PyEncoder.encode()` `PyEncoder.encode_to_pyfd()` and
`PyEncoder.encode_to_file()`.

[ Next `ImageFilter` module ](ImageFilter.html) [ Previous `ImageEnhance`
module ](ImageEnhance.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageFile` module
    * Example: Parse an image
    * Classes
      * `_Tile`
        * `_Tile.codec_name`
        * `_Tile.extents`
        * `_Tile.offset`
        * `_Tile.args`
      * `Parser`
        * `Parser.close()`
        * `Parser.feed()`
        * `Parser.reset()`
      * `PyCodec`
        * `PyCodec.cleanup()`
        * `PyCodec.init()`
        * `PyCodec.setfd()`
        * `PyCodec.setimage()`
      * `PyDecoder`
        * `PyDecoder.decode()`
        * `PyDecoder.set_as_raw()`
      * `PyEncoder`
        * `PyEncoder.encode()`
        * `PyEncoder.encode_to_file()`
        * `PyEncoder.encode_to_pyfd()`
      * `ImageFile`
        * `ImageFile.custom_mimetype`
        * `ImageFile.tile`
        * `ImageFile.decoderconfig`
        * `ImageFile.close()`
        * `ImageFile.get_child_images()`
        * `ImageFile.get_format_mimetype()`
        * `ImageFile.verify()`
        * `ImageFile.load()`
        * `ImageFile.load_prepare()`
        * `ImageFile.load_end()`
      * `StubHandler`
      * `StubImageFile`
        * `StubImageFile.load()`
    * Constants
      * `LOAD_TRUNCATED_IMAGES`
      * `MAXBLOCK`
      * `ERRORS`

