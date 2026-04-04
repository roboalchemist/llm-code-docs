# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageFont.html
# Path: reference/ImageFont.html

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
    * `ImageFont` module
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

[ View this page ](../_sources/reference/ImageFont.rst.txt "View this page")

# `ImageFont` module¶

The `ImageFont` module defines a class with the same name. Instances of this
class store bitmap fonts, and are used with the
[`PIL.ImageDraw.ImageDraw.text()`](ImageDraw.html#PIL.ImageDraw.ImageDraw.text
"PIL.ImageDraw.ImageDraw.text") method.

PIL uses its own font file format to store bitmap fonts, limited to 256
characters. You can use [pilfont.py](https://github.com/python-pillow/pillow-
scripts/blob/main/Scripts/pilfont.py) from [pillow-
scripts](https://pypi.org/project/pillow-scripts/) to convert BDF and PCF font
descriptors (X window font formats) to this format.

Starting with version 1.1.4, PIL can be configured to support TrueType and
OpenType fonts (as well as other font formats supported by the FreeType
library). For earlier versions, TrueType support is only available as part of
the imToolkit package.

When measuring text sizes, this module will not break at newline characters.
For multiline text, see the [`ImageDraw`](ImageDraw.html#module-PIL.ImageDraw
"PIL.ImageDraw") module.

Warning

To protect against potential DOS attacks when using arbitrary strings as text
input, Pillow will raise a
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError
"\(in Python v3.14\)") if the number of characters is over a certain limit,
`MAX_STRING_LENGTH`.

This threshold can be changed by setting `MAX_STRING_LENGTH`. It can be
disabled by setting `ImageFont.MAX_STRING_LENGTH = None`.

## Example¶

    
    
    from PIL import ImageFont, ImageDraw
    
    draw = ImageDraw.Draw(image)
    
    # use a bitmap font
    font = ImageFont.load("arial.pil")
    
    draw.text((10, 10), "hello", font=font)
    
    # use a truetype font
    font = ImageFont.truetype("arial.ttf", 15)
    
    draw.text((10, 25), "world", font=font)
    

## Functions¶

PIL.ImageFont.load(_filename :
[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.14\)")_) -> ImageFont[[source]](../_modules/PIL/ImageFont.html#load)¶

    

Load a font file. This function loads a font object from the given bitmap font
file, and returns the corresponding font object. For loading TrueType or
OpenType fonts instead, see `truetype()`.

Parameters:

    

**filename** – Name of font file.

Returns:

    

A font object.

Raises:

    

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "\(in
Python v3.14\)") – If the file could not be read.

PIL.ImageFont.load_path(_filename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_) -> ImageFont[[source]](../_modules/PIL/ImageFont.html#load_path)¶
    

Load font file. Same as `load()`, but searches for a bitmap font along the
Python path.

Parameters:

    

**filename** – Name of font file.

Returns:

    

A font object.

Raises:

    

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "\(in
Python v3.14\)") – If the file could not be read.

PIL.ImageFont.truetype(_font : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "\(in Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | [BinaryIO](https://docs.python.org/3/library/typing.html#typing.BinaryIO "\(in Python v3.14\)")_, _size : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") = 10_, _index : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 0_, _encoding : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") = ''_, _layout_engine : Layout | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> FreeTypeFont[[source]](../_modules/PIL/ImageFont.html#truetype)¶
    

Load a TrueType or OpenType font from a file or file-like object, and create a
font object. This function loads a font object from the given file or file-
like object, and creates a font object for a font of the given size. For
loading bitmap fonts instead, see `load()` and `load_path()`.

Pillow uses FreeType to open font files. On Windows, be aware that FreeType
will keep the file open as long as the FreeTypeFont object exists. Windows
limits the number of files that can be open in C at once to 512, so if many
fonts are opened simultaneously and that limit is approached, an `OSError` may
be thrown, reporting that FreeType “cannot open resource”. A workaround would
be to copy the file(s) into memory, and open that instead.

This function requires the _imagingft service.

Parameters:

    

  * **font** – 

A filename or file-like object containing a TrueType font. If the file is not
found in this filename, the loader may also search in other directories, such
as:

    * The `fonts/` directory on Windows,

    * `/Library/Fonts/`, `/System/Library/Fonts/` and `~/Library/Fonts/` on macOS.

    * `~/.local/share/fonts`, `/usr/local/share/fonts`, and `/usr/share/fonts` on Linux; or those specified by the `XDG_DATA_HOME` and `XDG_DATA_DIRS` environment variables for user-installed and system-wide fonts, respectively.

  * **size** – The requested size, in pixels.

  * **index** – Which font face to load (default is first available face).

  * **encoding** – 

Which font encoding to use (default is Unicode). Possible encodings include
(see the FreeType documentation for more information):

    * ”unic” (Unicode)

    * ”symb” (Microsoft Symbol)

    * ”ADOB” (Adobe Standard)

    * ”ADBE” (Adobe Expert)

    * ”ADBC” (Adobe Custom)

    * ”armn” (Apple Roman)

    * ”sjis” (Shift JIS)

    * ”gb “ (PRC)

    * ”big5”

    * ”wans” (Extended Wansung)

    * ”joha” (Johab)

    * ”lat1” (Latin-1)

This specifies the character set to use. It does not alter the encoding of any
text provided in subsequent operations.

  * **layout_engine** – 

Which layout engine to use, if available: `ImageFont.Layout.BASIC` or
`ImageFont.Layout.RAQM`. If it is available, Raqm layout will be used by
default. Otherwise, basic layout will be used.

Raqm layout is recommended for all non-English text. If Raqm layout is not
required, basic layout will have better performance.

You can check support for Raqm layout using
[`PIL.features.check_feature()`](features.html#PIL.features.check_feature
"PIL.features.check_feature") with `feature="raqm"`.

Added in version 4.2.0.

Returns:

    

A font object.

Raises:

    

  * [**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "\(in Python v3.14\)") – If the file could not be read.

  * [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "\(in Python v3.14\)") – If the font size is not greater than zero.

PIL.ImageFont.load_default(_size : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> FreeTypeFont | ImageFont[[source]](../_modules/PIL/ImageFont.html#load_default)¶
    

If FreeType support is available, load a version of Aileron Regular,
<https://dotcolon.net/fonts/aileron>, with a more limited character set.

Otherwise, load a “better than nothing” font.

Added in version 1.1.4.

Parameters:

    

**size** –

The font size of Aileron Regular.

Added in version 10.1.0.

Returns:

    

A font object.

PIL.ImageFont.load_default_imagefont() ->
ImageFont[[source]](../_modules/PIL/ImageFont.html#load_default_imagefont)¶

    

## Methods¶

class
PIL.ImageFont.ImageFont[[source]](../_modules/PIL/ImageFont.html#ImageFont)¶

    

PIL font wrapper

getbbox(_text : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "\(in Python v3.14\)")_, _* args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)")_, _** kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")][[source]](../_modules/PIL/ImageFont.html#ImageFont.getbbox)¶
    

Returns bounding box (in pixels) of given text.

Added in version 9.2.0.

Parameters:

    

**text** – Text to render.

Returns:

    

`(left, top, right, bottom)` bounding box

getlength(_text : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray "\(in Python v3.14\)")_, _* args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)")_, _** kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)")_) -> [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageFont.html#ImageFont.getlength)¶
    

Returns length (in pixels) of given text. This is the amount by which
following text should be offset.

Added in version 9.2.0.

getmask(_text : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") = ''_, _* args: Any_, _** kwargs: Any_) -> [Image.core.ImagingCore](internal_modules.html#PIL.Image.core.ImagingCore "PIL.Image.core.ImagingCore")[[source]](../_modules/PIL/ImageFont.html#ImageFont.getmask)¶
    

Create a bitmap for the text.

If the font uses antialiasing, the bitmap should have mode `L` and use a
maximum value of 255. Otherwise, it should have mode `1`.

Parameters:

    

  * **text** – Text to render.

  * **mode** – 

Used by some graphics drivers to indicate what mode the driver prefers; if
empty, the renderer may return either mode. Note that the mode is always a
string, to simplify C-level implementations.

Added in version 1.1.5.

Returns:

    

An internal PIL storage memory instance as defined by the
[`PIL.Image.core`](internal_modules.html#module-PIL.Image.core
"PIL.Image.core") interface module.

class PIL.ImageFont.FreeTypeFont(_font : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "\(in Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | [BinaryIO](https://docs.python.org/3/library/typing.html#typing.BinaryIO "\(in Python v3.14\)")_, _size : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") = 10_, _index : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 0_, _encoding : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") = ''_, _layout_engine : Layout | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/ImageFont.html#FreeTypeFont)¶
    

FreeType font wrapper (requires _imagingft service)

font_variant(_font : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [PathLike](https://docs.python.org/3/library/os.html#os.PathLike "\(in Python v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | [BinaryIO](https://docs.python.org/3/library/typing.html#typing.BinaryIO "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _size : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _index : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _encoding : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _layout_engine : Layout | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> FreeTypeFont[[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.font_variant)¶
    

Create a copy of this FreeTypeFont object, using any specified arguments to
override the settings.

Parameters are identical to the parameters used to initialize this object.

Returns:

    

A FreeTypeFont object.

get_variation_axes() ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[Axis][[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.get_variation_axes)¶

    

Returns:

    

A list of the axes in a variation font.

Raises:

    

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "\(in
Python v3.14\)") – If the font is not a variation font.

get_variation_names() ->
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in
Python
v3.14\)")][[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.get_variation_names)¶

    

Returns:

    

A list of the named styles in a variation font.

Raises:

    

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "\(in
Python v3.14\)") – If the font is not a variation font.

getbbox(_text : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") = ''_, _direction : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _features : [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _language : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _stroke_width : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") = 0_, _anchor : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")][[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.getbbox)¶
    

Returns bounding box (in pixels) of given text relative to given anchor when
rendered in font with provided direction, features, and language.

Use `getlength()` to get the offset of following text with 1/64 pixel
precision. The bounding box includes extra margins for some fonts, e.g.
italics or accents.

Added in version 8.0.0.

Parameters:

    

  * **text** – Text to render.

  * **mode** – Used by some graphics drivers to indicate what mode the driver prefers; if empty, the renderer may return either mode. Note that the mode is always a string, to simplify C-level implementations.

  * **direction** – Direction of the text. It can be ‘rtl’ (right to left), ‘ltr’ (left to right) or ‘ttb’ (top to bottom). Requires libraqm.

  * **features** – A list of OpenType font features to be used during text layout. This is usually used to turn on optional font features that are not enabled by default, for example ‘dlig’ or ‘ss01’, but can be also used to turn off default font features for example ‘-liga’ to disable ligatures or ‘-kern’ to disable kerning. To get all supported features, see <https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist> Requires libraqm.

  * **language** – Language of the text. Different languages may use different glyph shapes or ligatures. This parameter tells the font which language the text is in, and to apply the correct substitutions as appropriate, if available. It should be a [BCP 47 language code](https://www.w3.org/International/articles/language-tags/) Requires libraqm.

  * **stroke_width** – The width of the text stroke.

  * **anchor** – The text anchor alignment. Determines the relative location of the anchor to the text. The default alignment is top left, specifically `la` for horizontal text and `lt` for vertical text. See [Text anchors](../handbook/text-anchors.html#text-anchors) for details.

Returns:

    

`(left, top, right, bottom)` bounding box

getlength(_text : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") = ''_, _direction : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _features : [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _language : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.getlength)¶
    

Returns length (in pixels with 1/64 precision) of given text when rendered in
font with provided direction, features, and language.

This is the amount by which following text should be offset. Text bounding box
may extend past the length in some fonts, e.g. when using italics or accents.

The result is returned as a float; it is a whole number if using basic layout.

Note that the sum of two lengths may not equal the length of a concatenated
string due to kerning. If you need to adjust for kerning, include the
following character and subtract its length.

For example, instead of

    
    
    hello = font.getlength("Hello")
    world = font.getlength("World")
    hello_world = hello + world  # not adjusted for kerning
    assert hello_world == font.getlength("HelloWorld")  # may fail
    

use

    
    
    hello = font.getlength("HelloW") - font.getlength("W")  # adjusted for kerning
    world = font.getlength("World")
    hello_world = hello + world  # adjusted for kerning
    assert hello_world == font.getlength("HelloWorld")  # True
    

or disable kerning with (requires libraqm)

    
    
    hello = draw.textlength("Hello", font, features=["-kern"])
    world = draw.textlength("World", font, features=["-kern"])
    hello_world = hello + world  # kerning is disabled, no need to adjust
    assert hello_world == draw.textlength("HelloWorld", font, features=["-kern"])
    

Added in version 8.0.0.

Parameters:

    

  * **text** – Text to measure.

  * **mode** – Used by some graphics drivers to indicate what mode the driver prefers; if empty, the renderer may return either mode. Note that the mode is always a string, to simplify C-level implementations.

  * **direction** – Direction of the text. It can be ‘rtl’ (right to left), ‘ltr’ (left to right) or ‘ttb’ (top to bottom). Requires libraqm.

  * **features** – A list of OpenType font features to be used during text layout. This is usually used to turn on optional font features that are not enabled by default, for example ‘dlig’ or ‘ss01’, but can be also used to turn off default font features for example ‘-liga’ to disable ligatures or ‘-kern’ to disable kerning. To get all supported features, see <https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist> Requires libraqm.

  * **language** – 

Language of the text. Different languages may use different glyph shapes or
ligatures. This parameter tells the font which language the text is in, and to
apply the correct substitutions as appropriate, if available. It should be a
[BCP 47 language code](https://www.w3.org/International/articles/language-
tags/) Requires libraqm.

Returns:

    

Either width for horizontal text, or height for vertical text.

getmask(_text : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") = ''_, _direction : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _features : [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _language : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _stroke_width : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") = 0_, _anchor : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _ink : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 0_, _start : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [Image.core.ImagingCore](internal_modules.html#PIL.Image.core.ImagingCore "PIL.Image.core.ImagingCore")[[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.getmask)¶
    

Create a bitmap for the text.

If the font uses antialiasing, the bitmap should have mode `L` and use a
maximum value of 255. If the font has embedded color data, the bitmap should
have mode `RGBA`. Otherwise, it should have mode `1`.

Parameters:

    

  * **text** – Text to render.

  * **mode** – 

Used by some graphics drivers to indicate what mode the driver prefers; if
empty, the renderer may return either mode. Note that the mode is always a
string, to simplify C-level implementations.

Added in version 1.1.5.

  * **direction** – 

Direction of the text. It can be ‘rtl’ (right to left), ‘ltr’ (left to right)
or ‘ttb’ (top to bottom). Requires libraqm.

Added in version 4.2.0.

  * **features** – 

A list of OpenType font features to be used during text layout. This is
usually used to turn on optional font features that are not enabled by
default, for example ‘dlig’ or ‘ss01’, but can be also used to turn off
default font features for example ‘-liga’ to disable ligatures or ‘-kern’ to
disable kerning. To get all supported features, see
<https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist>
Requires libraqm.

Added in version 4.2.0.

  * **language** – 

Language of the text. Different languages may use different glyph shapes or
ligatures. This parameter tells the font which language the text is in, and to
apply the correct substitutions as appropriate, if available. It should be a
[BCP 47 language code](https://www.w3.org/International/articles/language-
tags/) Requires libraqm.

Added in version 6.0.0.

  * **stroke_width** – 

The width of the text stroke.

Added in version 6.2.0.

  * **anchor** – 

The text anchor alignment. Determines the relative location of the anchor to
the text. The default alignment is top left, specifically `la` for horizontal
text and `lt` for vertical text. See [Text anchors](../handbook/text-
anchors.html#text-anchors) for details.

> Added in version 8.0.0.

  * **ink** – 

Foreground ink for rendering in RGBA mode.

Added in version 8.0.0.

  * **start** – 

Tuple of horizontal and vertical offset, as text may render differently when
starting at fractional coordinates.

> Added in version 9.4.0.

Returns:

    

An internal PIL storage memory instance as defined by the
[`PIL.Image.core`](internal_modules.html#module-PIL.Image.core
"PIL.Image.core") interface module.

getmask2(_text : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") = ''_, _direction : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _features : [list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _language : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _stroke_width : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") = 0_, _anchor : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _ink : [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") = 0_, _start : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _* args: Any_, _** kwargs: Any_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[Image.core.ImagingCore](internal_modules.html#PIL.Image.core.ImagingCore "PIL.Image.core.ImagingCore"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]][[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.getmask2)¶
    

Create a bitmap for the text.

If the font uses antialiasing, the bitmap should have mode `L` and use a
maximum value of 255. If the font has embedded color data, the bitmap should
have mode `RGBA`. Otherwise, it should have mode `1`.

Parameters:

    

  * **text** – Text to render.

  * **mode** – 

Used by some graphics drivers to indicate what mode the driver prefers; if
empty, the renderer may return either mode. Note that the mode is always a
string, to simplify C-level implementations.

Added in version 1.1.5.

  * **direction** – 

Direction of the text. It can be ‘rtl’ (right to left), ‘ltr’ (left to right)
or ‘ttb’ (top to bottom). Requires libraqm.

Added in version 4.2.0.

  * **features** – 

A list of OpenType font features to be used during text layout. This is
usually used to turn on optional font features that are not enabled by
default, for example ‘dlig’ or ‘ss01’, but can be also used to turn off
default font features for example ‘-liga’ to disable ligatures or ‘-kern’ to
disable kerning. To get all supported features, see
<https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist>
Requires libraqm.

Added in version 4.2.0.

  * **language** – 

Language of the text. Different languages may use different glyph shapes or
ligatures. This parameter tells the font which language the text is in, and to
apply the correct substitutions as appropriate, if available. It should be a
[BCP 47 language code](https://www.w3.org/International/articles/language-
tags/) Requires libraqm.

Added in version 6.0.0.

  * **stroke_width** – 

The width of the text stroke.

Added in version 6.2.0.

  * **anchor** – 

The text anchor alignment. Determines the relative location of the anchor to
the text. The default alignment is top left, specifically `la` for horizontal
text and `lt` for vertical text. See [Text anchors](../handbook/text-
anchors.html#text-anchors) for details.

> Added in version 8.0.0.

  * **ink** – 

Foreground ink for rendering in RGBA mode.

Added in version 8.0.0.

  * **start** – 

Tuple of horizontal and vertical offset, as text may render differently when
starting at fractional coordinates.

> Added in version 9.4.0.

Returns:

    

A tuple of an internal PIL storage memory instance as defined by the
[`PIL.Image.core`](internal_modules.html#module-PIL.Image.core
"PIL.Image.core") interface module, and the text offset, the gap between the
starting coordinate and the first marking

getmetrics() -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple
"\(in Python
v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int
"\(in Python
v3.14\)")][[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.getmetrics)¶

    

Returns:

    

A tuple of the font ascent (the distance from the baseline to the highest
outline point) and descent (the distance from the baseline to the lowest
outline point, a negative value)

getname() -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)"), [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")][[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.getname)¶
    

Returns:

    

A tuple of the font family (e.g. Helvetica) and the font style (e.g. Bold)

set_variation_by_axes(_axes :
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.14\)")]_) ->
[None](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.set_variation_by_axes)¶

    

Parameters:

    

**axes** – A list of values for each axis.

Raises:

    

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "\(in
Python v3.14\)") – If the font is not a variation font.

set_variation_by_name(_name : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageFont.html#FreeTypeFont.set_variation_by_name)¶
    

Parameters:

    

**name** – The name of the style.

Raises:

    

[**OSError**](https://docs.python.org/3/library/exceptions.html#OSError "\(in
Python v3.14\)") – If the font is not a variation font.

class PIL.ImageFont.TransposedFont(_font : ImageFont | FreeTypeFont_, _orientation : [Transpose](Image.html#PIL.Image.Transpose "PIL.Image.Transpose") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_)[[source]](../_modules/PIL/ImageFont.html#TransposedFont)¶
    

Wrapper for writing rotated or mirrored text

getbbox(_text : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _* args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)")_, _** kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)")_) -> [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")][[source]](../_modules/PIL/ImageFont.html#TransposedFont.getbbox)¶
    

getlength(_text : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _* args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)")_, _** kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python v3.14\)")_) -> [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageFont.html#TransposedFont.getlength)¶
    

getmask(_text : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")_, _mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") = ''_, _* args: Any_, _** kwargs: Any_) -> [Image.core.ImagingCore](internal_modules.html#PIL.Image.core.ImagingCore "PIL.Image.core.ImagingCore")[[source]](../_modules/PIL/ImageFont.html#TransposedFont.getmask)¶
    

## Constants¶

class PIL.ImageFont.Layout[[source]](../_modules/PIL/ImageFont.html#Layout)¶

    

BASIC¶

    

Use basic text layout for TrueType font. Advanced features such as text
direction are not supported.

RAQM¶

    

Use Raqm text layout for TrueType font. Advanced features are supported.

Requires Raqm, you can check support using
[`PIL.features.check_feature()`](features.html#PIL.features.check_feature
"PIL.features.check_feature") with `feature="raqm"`.

PIL.ImageFont.MAX_STRING_LENGTH¶

    

Set to 1,000,000, to protect against potential DOS attacks. Pillow will raise
a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError
"\(in Python v3.14\)") if the number of characters is over this limit. The
check can be disabled by setting `ImageFont.MAX_STRING_LENGTH = None`.

## Dictionaries¶

class PIL.ImageFont.Axis[[source]](../_modules/PIL/ImageFont.html#Axis)¶

    

Bases:
[`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict
"\(in Python v3.14\)")

default: [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

maximum: [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

minimum: [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

name: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

[ Next `ImageGrab` module ](ImageGrab.html) [ Previous `ImageFilter` module
](ImageFilter.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageFont` module
    * Example
    * Functions
      * `load()`
      * `load_path()`
      * `truetype()`
      * `load_default()`
      * `load_default_imagefont()`
    * Methods
      * `ImageFont`
        * `ImageFont.getbbox()`
        * `ImageFont.getlength()`
        * `ImageFont.getmask()`
      * `FreeTypeFont`
        * `FreeTypeFont.font_variant()`
        * `FreeTypeFont.get_variation_axes()`
        * `FreeTypeFont.get_variation_names()`
        * `FreeTypeFont.getbbox()`
        * `FreeTypeFont.getlength()`
        * `FreeTypeFont.getmask()`
        * `FreeTypeFont.getmask2()`
        * `FreeTypeFont.getmetrics()`
        * `FreeTypeFont.getname()`
        * `FreeTypeFont.set_variation_by_axes()`
        * `FreeTypeFont.set_variation_by_name()`
      * `TransposedFont`
        * `TransposedFont.getbbox()`
        * `TransposedFont.getlength()`
        * `TransposedFont.getmask()`
    * Constants
      * `Layout`
        * `Layout.BASIC`
        * `Layout.RAQM`
      * `MAX_STRING_LENGTH`
    * Dictionaries
      * `Axis`
        * `Axis.default`
        * `Axis.maximum`
        * `Axis.minimum`
        * `Axis.name`

