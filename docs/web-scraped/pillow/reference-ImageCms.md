# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageCms.html
# Path: reference/ImageCms.html

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
    * `ImageCms` module
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

[ View this page ](../_sources/reference/ImageCms.rst.txt "View this page")

# `ImageCms` module¶

The `ImageCms` module provides color profile management support using the
LittleCMS2 color management engine, based on Kevin Cazabon’s PyCMS library.

class PIL.ImageCms.ImageCmsProfile(_profile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile_)[[source]](../_modules/PIL/ImageCms.html#ImageCmsProfile)¶
    

__init__(_profile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#ImageCmsProfile.__init__)¶
    

Parameters:

    

**profile** – Either a string representing a filename, a file like object
containing a profile or a low-level profile object

tobytes() -> [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python
v3.14\)")[[source]](../_modules/PIL/ImageCms.html#ImageCmsProfile.tobytes)¶

    

Returns the profile in a format suitable for embedding in saved images.

Returns:

    

a bytes object containing the ICC profile.

class PIL.ImageCms.ImageCmsTransform(_input : ImageCmsProfile_, _output : ImageCmsProfile_, _input_mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_, _output_mode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_, _intent : Intent = Intent.PERCEPTUAL_, _proof : ImageCmsProfile | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _proof_intent : Intent = Intent.ABSOLUTE_COLORIMETRIC_, _flags : Flags = <Flags.NONE: 0>_)[[source]](../_modules/PIL/ImageCms.html#ImageCmsTransform)¶
    

Bases: [`ImagePointHandler`](Image.html#PIL.Image.ImagePointHandler
"PIL.Image.ImagePointHandler")

Transform. This can be used with the procedural API, or with the standard
[`point()`](Image.html#PIL.Image.Image.point "PIL.Image.Image.point") method.

Will return the output profile in the `output.info['icc_profile']`.

apply(_im : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _imOut : [Image](Image.html#PIL.Image.Image "PIL.Image.Image") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image")[[source]](../_modules/PIL/ImageCms.html#ImageCmsTransform.apply)¶
    

apply_in_place(_im : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_)
-> [Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageCms.html#ImageCmsTransform.apply_in_place)¶

    

point(_im : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_) ->
[Image](Image.html#PIL.Image.Image
"PIL.Image.Image")[[source]](../_modules/PIL/ImageCms.html#ImageCmsTransform.point)¶

    

exception
PIL.ImageCms.PyCMSError[[source]](../_modules/PIL/ImageCms.html#PyCMSError)¶

    

(pyCMS) Exception class. This is used for all errors in the pyCMS API.

## Constants¶

class PIL.ImageCms.Intent(_*
values_)[[source]](../_modules/PIL/ImageCms.html#Intent)¶

    

Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum
"\(in Python v3.14\)")

PERCEPTUAL = 0¶

    

RELATIVE_COLORIMETRIC = 1¶

    

SATURATION = 2¶

    

ABSOLUTE_COLORIMETRIC = 3¶

    

class PIL.ImageCms.Direction(_*
values_)[[source]](../_modules/PIL/ImageCms.html#Direction)¶

    

Bases: [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum
"\(in Python v3.14\)")

INPUT = 0¶

    

OUTPUT = 1¶

    

PROOF = 2¶

    

class PIL.ImageCms.Flags(_*
values_)[[source]](../_modules/PIL/ImageCms.html#Flags)¶

    

Bases: [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag
"\(in Python v3.14\)")

Flags and documentation are taken from `lcms2.h`.

NONE = 0¶

    

NOCACHE = 64¶

    

Inhibit 1-pixel cache

NOOPTIMIZE = 256¶

    

Inhibit optimizations

NULLTRANSFORM = 512¶

    

Don’t transform anyway

GAMUTCHECK = 4096¶

    

Out of Gamut alarm

SOFTPROOFING = 16384¶

    

Do softproofing

BLACKPOINTCOMPENSATION = 8192¶

    

NOWHITEONWHITEFIXUP = 4¶

    

Don’t fix scum dot

HIGHRESPRECALC = 1024¶

    

Use more memory to give better accuracy

LOWRESPRECALC = 2048¶

    

Use less memory to minimize resources

USE_8BITS_DEVICELINK = 8¶

    

Create 8 bits devicelinks

GUESSDEVICECLASS = 32¶

    

Guess device class (for `transform2devicelink`)

KEEP_SEQUENCE = 128¶

    

Keep profile sequence for devicelink creation

FORCE_CLUT = 2¶

    

Force CLUT optimization

CLUT_POST_LINEARIZATION = 1¶

    

create postlinearization tables if possible

CLUT_PRE_LINEARIZATION = 16¶

    

create prelinearization tables if possible

NONEGATIVES = 32768¶

    

Prevent negative numbers in floating point transforms

COPY_ALPHA = 67108864¶

    

Alpha channels are copied on `cmsDoTransform()`

NODEFAULTRESOURCEDEF = 16777216¶

    

static GRIDPOINTS(_n :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_) ->
Flags[[source]](../_modules/PIL/ImageCms.html#Flags.GRIDPOINTS)¶

    

Fine-tune control over number of gridpoints

Parameters:

    

**n** – [`int`](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)") in range `0 <= n <= 255`

## Functions¶

PIL.ImageCms.applyTransform(_im : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _transform : ImageCmsTransform_, _inPlace : [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = False_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#applyTransform)¶
    

(pyCMS) Applies a transform to a given image.

If `im.mode != transform.input_mode`, a `PyCMSError` is raised.

If `inPlace` is `True` and `transform.input_mode != transform.output_mode`, a
`PyCMSError` is raised.

If `im.mode`, `transform.input_mode` or `transform.output_mode` is not
supported by pyCMSdll or the profiles you used for the transform, a
`PyCMSError` is raised.

If an error occurs while the transform is being applied, a `PyCMSError` is
raised.

This function applies a pre-calculated transform (from
ImageCms.buildTransform() or ImageCms.buildTransformFromOpenProfiles()) to an
image. The transform can be used for multiple images, saving considerable
calculation time if doing the same conversion multiple times.

If you want to modify im in-place instead of receiving a new image as the
return value, set `inPlace` to `True`. This can only be done if
`transform.input_mode` and `transform.output_mode` are the same, because we
can’t change the mode in-place (the buffer sizes for some modes are
different). The default behavior is to return a new
[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image") object of the same
dimensions in mode `transform.output_mode`.

Parameters:

    

  * **im** – An [`Image`](Image.html#PIL.Image.Image "PIL.Image.Image") object, and `im.mode` must be the same as the `input_mode` supported by the transform.

  * **transform** – A valid CmsTransform class object

  * **inPlace** – Bool. If `True`, `im` is modified in place and `None` is returned, if `False`, a new [`Image`](Image.html#PIL.Image.Image "PIL.Image.Image") object with the transform applied is returned (and `im` is not changed). The default is `False`.

Returns:

    

Either `None`, or a new [`Image`](Image.html#PIL.Image.Image
"PIL.Image.Image") object, depending on the value of `inPlace`. The profile
will be returned in the image’s `info['icc_profile']`.

Raises:

    

**PyCMSError** –

PIL.ImageCms.buildProofTransform(_inputProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _outputProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _proofProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _inMode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_, _outMode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_, _renderingIntent : Intent = Intent.PERCEPTUAL_, _proofRenderingIntent : Intent = Intent.ABSOLUTE_COLORIMETRIC_, _flags : Flags = <Flags.SOFTPROOFING: 16384>_) -> ImageCmsTransform[[source]](../_modules/PIL/ImageCms.html#buildProofTransform)¶
    

(pyCMS) Builds an ICC transform mapping from the `inputProfile` to the
`outputProfile`, but tries to simulate the result that would be obtained on
the `proofProfile` device.

If the input, output, or proof profiles specified are not valid filenames, a
`PyCMSError` will be raised.

If an error occurs during creation of the transform, a `PyCMSError` will be
raised.

If `inMode` or `outMode` are not a mode supported by the `outputProfile` (or
by pyCMS), a `PyCMSError` will be raised.

This function builds and returns an ICC transform from the `inputProfile` to
the `outputProfile`, but tries to simulate the result that would be obtained
on the `proofProfile` device using `renderingIntent` and
`proofRenderingIntent` to determine what to do with out-of-gamut colors. This
is known as “soft-proofing”. It will ONLY work for converting images that are
in `inMode` to images that are in outMode color format (PIL mode, i.e. “RGB”,
“RGBA”, “CMYK”, etc.).

Usage of the resulting transform object is exactly the same as with
ImageCms.buildTransform().

Proof profiling is generally used when using an output device to get a good
idea of what the final printed/displayed image would look like on the
`proofProfile` device when it’s quicker and easier to use the output device
for judging color. Generally, this means that the output device is a monitor,
or a dye-sub printer (etc.), and the simulated device is something more
expensive, complicated, or time consuming (making it difficult to make a real
print for color judgement purposes).

Soft-proofing basically functions by adjusting the colors on the output device
to match the colors of the device being simulated. However, when the simulated
device has a much wider gamut than the output device, you may obtain marginal
results.

Parameters:

    

  * **inputProfile** – String, as a valid filename path to the ICC input profile you wish to use for this transform, or a profile object

  * **outputProfile** – String, as a valid filename path to the ICC output (monitor, usually) profile you wish to use for this transform, or a profile object

  * **proofProfile** – String, as a valid filename path to the ICC proof profile you wish to use for this transform, or a profile object

  * **inMode** – String, as a valid PIL mode that the appropriate profile also supports (i.e. “RGB”, “RGBA”, “CMYK”, etc.)

  * **outMode** – String, as a valid PIL mode that the appropriate profile also supports (i.e. “RGB”, “RGBA”, “CMYK”, etc.)

  * **renderingIntent** – 

Integer (0-3) specifying the rendering intent you wish to use for the
input->proof (simulated) transform

> ImageCms.Intent.PERCEPTUAL = 0 (DEFAULT)
> ImageCms.Intent.RELATIVE_COLORIMETRIC = 1 ImageCms.Intent.SATURATION = 2
> ImageCms.Intent.ABSOLUTE_COLORIMETRIC = 3

see the pyCMS documentation for details on rendering intents and what they do.

  * **proofRenderingIntent** – 

Integer (0-3) specifying the rendering intent you wish to use for
proof->output transform

> ImageCms.Intent.PERCEPTUAL = 0 (DEFAULT)
> ImageCms.Intent.RELATIVE_COLORIMETRIC = 1 ImageCms.Intent.SATURATION = 2
> ImageCms.Intent.ABSOLUTE_COLORIMETRIC = 3

see the pyCMS documentation for details on rendering intents and what they do.

  * **flags** – Integer (0-…) specifying additional flags

Returns:

    

A CmsTransform class object.

Raises:

    

**PyCMSError** –

PIL.ImageCms.buildProofTransformFromOpenProfiles(_inputProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _outputProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _proofProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _inMode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_, _outMode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_, _renderingIntent : Intent = Intent.PERCEPTUAL_, _proofRenderingIntent : Intent = Intent.ABSOLUTE_COLORIMETRIC_, _flags : Flags = <Flags.SOFTPROOFING: 16384>_) -> ImageCmsTransform¶
    

(pyCMS) Builds an ICC transform mapping from the `inputProfile` to the
`outputProfile`, but tries to simulate the result that would be obtained on
the `proofProfile` device.

If the input, output, or proof profiles specified are not valid filenames, a
`PyCMSError` will be raised.

If an error occurs during creation of the transform, a `PyCMSError` will be
raised.

If `inMode` or `outMode` are not a mode supported by the `outputProfile` (or
by pyCMS), a `PyCMSError` will be raised.

This function builds and returns an ICC transform from the `inputProfile` to
the `outputProfile`, but tries to simulate the result that would be obtained
on the `proofProfile` device using `renderingIntent` and
`proofRenderingIntent` to determine what to do with out-of-gamut colors. This
is known as “soft-proofing”. It will ONLY work for converting images that are
in `inMode` to images that are in outMode color format (PIL mode, i.e. “RGB”,
“RGBA”, “CMYK”, etc.).

Usage of the resulting transform object is exactly the same as with
ImageCms.buildTransform().

Proof profiling is generally used when using an output device to get a good
idea of what the final printed/displayed image would look like on the
`proofProfile` device when it’s quicker and easier to use the output device
for judging color. Generally, this means that the output device is a monitor,
or a dye-sub printer (etc.), and the simulated device is something more
expensive, complicated, or time consuming (making it difficult to make a real
print for color judgement purposes).

Soft-proofing basically functions by adjusting the colors on the output device
to match the colors of the device being simulated. However, when the simulated
device has a much wider gamut than the output device, you may obtain marginal
results.

Parameters:

    

  * **inputProfile** – String, as a valid filename path to the ICC input profile you wish to use for this transform, or a profile object

  * **outputProfile** – String, as a valid filename path to the ICC output (monitor, usually) profile you wish to use for this transform, or a profile object

  * **proofProfile** – String, as a valid filename path to the ICC proof profile you wish to use for this transform, or a profile object

  * **inMode** – String, as a valid PIL mode that the appropriate profile also supports (i.e. “RGB”, “RGBA”, “CMYK”, etc.)

  * **outMode** – String, as a valid PIL mode that the appropriate profile also supports (i.e. “RGB”, “RGBA”, “CMYK”, etc.)

  * **renderingIntent** – 

Integer (0-3) specifying the rendering intent you wish to use for the
input->proof (simulated) transform

> ImageCms.Intent.PERCEPTUAL = 0 (DEFAULT)
> ImageCms.Intent.RELATIVE_COLORIMETRIC = 1 ImageCms.Intent.SATURATION = 2
> ImageCms.Intent.ABSOLUTE_COLORIMETRIC = 3

see the pyCMS documentation for details on rendering intents and what they do.

  * **proofRenderingIntent** – 

Integer (0-3) specifying the rendering intent you wish to use for
proof->output transform

> ImageCms.Intent.PERCEPTUAL = 0 (DEFAULT)
> ImageCms.Intent.RELATIVE_COLORIMETRIC = 1 ImageCms.Intent.SATURATION = 2
> ImageCms.Intent.ABSOLUTE_COLORIMETRIC = 3

see the pyCMS documentation for details on rendering intents and what they do.

  * **flags** – Integer (0-…) specifying additional flags

Returns:

    

A CmsTransform class object.

Raises:

    

**PyCMSError** –

PIL.ImageCms.buildTransform(_inputProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _outputProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _inMode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_, _outMode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_, _renderingIntent : Intent = Intent.PERCEPTUAL_, _flags : Flags = <Flags.NONE: 0>_) -> ImageCmsTransform[[source]](../_modules/PIL/ImageCms.html#buildTransform)¶
    

(pyCMS) Builds an ICC transform mapping from the `inputProfile` to the
`outputProfile`. Use applyTransform to apply the transform to a given image.

If the input or output profiles specified are not valid filenames, a
`PyCMSError` will be raised. If an error occurs during creation of the
transform, a `PyCMSError` will be raised.

If `inMode` or `outMode` are not a mode supported by the `outputProfile` (or
by pyCMS), a `PyCMSError` will be raised.

This function builds and returns an ICC transform from the `inputProfile` to
the `outputProfile` using the `renderingIntent` to determine what to do with
out-of-gamut colors. It will ONLY work for converting images that are in
`inMode` to images that are in `outMode` color format (PIL mode, i.e. “RGB”,
“RGBA”, “CMYK”, etc.).

Building the transform is a fair part of the overhead in
ImageCms.profileToProfile(), so if you’re planning on converting multiple
images using the same input/output settings, this can save you time. Once you
have a transform object, it can be used with ImageCms.applyProfile() to
convert images without the need to re-compute the lookup table for the
transform.

The reason pyCMS returns a class object rather than a handle directly to the
transform is that it needs to keep track of the PIL input/output modes that
the transform is meant for. These attributes are stored in the `inMode` and
`outMode` attributes of the object (which can be manually overridden if you
really want to, but I don’t know of any time that would be of use, or would
even work).

Parameters:

    

  * **inputProfile** – String, as a valid filename path to the ICC input profile you wish to use for this transform, or a profile object

  * **outputProfile** – String, as a valid filename path to the ICC output profile you wish to use for this transform, or a profile object

  * **inMode** – String, as a valid PIL mode that the appropriate profile also supports (i.e. “RGB”, “RGBA”, “CMYK”, etc.)

  * **outMode** – String, as a valid PIL mode that the appropriate profile also supports (i.e. “RGB”, “RGBA”, “CMYK”, etc.)

  * **renderingIntent** – 

Integer (0-3) specifying the rendering intent you wish to use for the
transform

> ImageCms.Intent.PERCEPTUAL = 0 (DEFAULT)
> ImageCms.Intent.RELATIVE_COLORIMETRIC = 1 ImageCms.Intent.SATURATION = 2
> ImageCms.Intent.ABSOLUTE_COLORIMETRIC = 3

see the pyCMS documentation for details on rendering intents and what they do.

  * **flags** – Integer (0-…) specifying additional flags

Returns:

    

A CmsTransform class object.

Raises:

    

**PyCMSError** –

PIL.ImageCms.buildTransformFromOpenProfiles(_inputProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _outputProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _inMode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_, _outMode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")_, _renderingIntent : Intent = Intent.PERCEPTUAL_, _flags : Flags = <Flags.NONE: 0>_) -> ImageCmsTransform¶
    

(pyCMS) Builds an ICC transform mapping from the `inputProfile` to the
`outputProfile`. Use applyTransform to apply the transform to a given image.

If the input or output profiles specified are not valid filenames, a
`PyCMSError` will be raised. If an error occurs during creation of the
transform, a `PyCMSError` will be raised.

If `inMode` or `outMode` are not a mode supported by the `outputProfile` (or
by pyCMS), a `PyCMSError` will be raised.

This function builds and returns an ICC transform from the `inputProfile` to
the `outputProfile` using the `renderingIntent` to determine what to do with
out-of-gamut colors. It will ONLY work for converting images that are in
`inMode` to images that are in `outMode` color format (PIL mode, i.e. “RGB”,
“RGBA”, “CMYK”, etc.).

Building the transform is a fair part of the overhead in
ImageCms.profileToProfile(), so if you’re planning on converting multiple
images using the same input/output settings, this can save you time. Once you
have a transform object, it can be used with ImageCms.applyProfile() to
convert images without the need to re-compute the lookup table for the
transform.

The reason pyCMS returns a class object rather than a handle directly to the
transform is that it needs to keep track of the PIL input/output modes that
the transform is meant for. These attributes are stored in the `inMode` and
`outMode` attributes of the object (which can be manually overridden if you
really want to, but I don’t know of any time that would be of use, or would
even work).

Parameters:

    

  * **inputProfile** – String, as a valid filename path to the ICC input profile you wish to use for this transform, or a profile object

  * **outputProfile** – String, as a valid filename path to the ICC output profile you wish to use for this transform, or a profile object

  * **inMode** – String, as a valid PIL mode that the appropriate profile also supports (i.e. “RGB”, “RGBA”, “CMYK”, etc.)

  * **outMode** – String, as a valid PIL mode that the appropriate profile also supports (i.e. “RGB”, “RGBA”, “CMYK”, etc.)

  * **renderingIntent** – 

Integer (0-3) specifying the rendering intent you wish to use for the
transform

> ImageCms.Intent.PERCEPTUAL = 0 (DEFAULT)
> ImageCms.Intent.RELATIVE_COLORIMETRIC = 1 ImageCms.Intent.SATURATION = 2
> ImageCms.Intent.ABSOLUTE_COLORIMETRIC = 3

see the pyCMS documentation for details on rendering intents and what they do.

  * **flags** – Integer (0-…) specifying additional flags

Returns:

    

A CmsTransform class object.

Raises:

    

**PyCMSError** –

PIL.ImageCms.createProfile(_colorSpace :
[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "\(in
Python v3.14\)")['LAB', 'XYZ', 'sRGB']_, _colorTemp :
[SupportsFloat](https://docs.python.org/3/library/typing.html#typing.SupportsFloat
"\(in Python v3.14\)") = 0_) ->
CmsProfile[[source]](../_modules/PIL/ImageCms.html#createProfile)¶

    

(pyCMS) Creates a profile.

If colorSpace not in `["LAB", "XYZ", "sRGB"]`, a `PyCMSError` is raised.

If using LAB and `colorTemp` is not a positive integer, a `PyCMSError` is
raised.

If an error occurs while creating the profile, a `PyCMSError` is raised.

Use this function to create common profiles on-the-fly instead of having to
supply a profile on disk and knowing the path to it. It returns a normal
CmsProfile object that can be passed to
ImageCms.buildTransformFromOpenProfiles() to create a transform to apply to
images.

Parameters:

    

  * **colorSpace** – String, the color space of the profile you wish to create. Currently only “LAB”, “XYZ”, and “sRGB” are supported.

  * **colorTemp** – Positive number for the white point for the profile, in degrees Kelvin (i.e. 5000, 6500, 9600, etc.). The default is for D50 illuminant if omitted (5000k). colorTemp is ONLY applied to LAB profiles, and is ignored for XYZ and sRGB.

Returns:

    

A CmsProfile class object

Raises:

    

**PyCMSError** –

PIL.ImageCms.getDefaultIntent(_profile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_) -> [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#getDefaultIntent)¶
    

(pyCMS) Gets the default intent name for the given profile.

If `profile` isn’t a valid CmsProfile object or filename to a profile, a
`PyCMSError` is raised.

If an error occurs while trying to obtain the default intent, a `PyCMSError`
is raised.

Use this function to determine the default (and usually best optimized)
rendering intent for this profile. Most profiles support multiple rendering
intents, but are intended mostly for one type of conversion. If you wish to
use a different intent than returned, use ImageCms.isIntentSupported() to
verify it will work first.

Parameters:

    

**profile** – EITHER a valid CmsProfile object, OR a string of the filename of
an ICC profile.

Returns:

    

Integer 0-3 specifying the default rendering intent for this profile.

> ImageCms.Intent.PERCEPTUAL = 0 (DEFAULT)
> ImageCms.Intent.RELATIVE_COLORIMETRIC = 1 ImageCms.Intent.SATURATION = 2
> ImageCms.Intent.ABSOLUTE_COLORIMETRIC = 3

see the pyCMS documentation for details on rendering intents and what

    

they do.

Raises:

    

**PyCMSError** –

PIL.ImageCms.getOpenProfile(_profileFilename : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile_) -> ImageCmsProfile[[source]](../_modules/PIL/ImageCms.html#getOpenProfile)¶
    

(pyCMS) Opens an ICC profile file.

The PyCMSProfile object can be passed back into pyCMS for use in creating
transforms and such (as in ImageCms.buildTransformFromOpenProfiles()).

If `profileFilename` is not a valid filename for an ICC profile, a
`PyCMSError` will be raised.

Parameters:

    

**profileFilename** – String, as a valid filename path to the ICC profile you
wish to open, or a file-like object.

Returns:

    

A CmsProfile class object.

Raises:

    

**PyCMSError** –

PIL.ImageCms.getProfileCopyright(_profile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#getProfileCopyright)¶
    

(pyCMS) Gets the copyright for the given profile.

If `profile` isn’t a valid CmsProfile object or filename to a profile, a
`PyCMSError` is raised.

If an error occurs while trying to obtain the copyright tag, a `PyCMSError` is
raised.

Use this function to obtain the information stored in the profile’s copyright
tag.

Parameters:

    

**profile** – EITHER a valid CmsProfile object, OR a string of the filename of
an ICC profile.

Returns:

    

A string containing the internal profile information stored in an ICC tag.

Raises:

    

**PyCMSError** –

PIL.ImageCms.getProfileDescription(_profile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#getProfileDescription)¶
    

(pyCMS) Gets the description for the given profile.

If `profile` isn’t a valid CmsProfile object or filename to a profile, a
`PyCMSError` is raised.

If an error occurs while trying to obtain the description tag, a `PyCMSError`
is raised.

Use this function to obtain the information stored in the profile’s
description tag.

Parameters:

    

**profile** – EITHER a valid CmsProfile object, OR a string of the filename of
an ICC profile.

Returns:

    

A string containing the internal profile information stored in an ICC tag.

Raises:

    

**PyCMSError** –

PIL.ImageCms.getProfileInfo(_profile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#getProfileInfo)¶
    

(pyCMS) Gets the internal product information for the given profile.

If `profile` isn’t a valid CmsProfile object or filename to a profile, a
`PyCMSError` is raised.

If an error occurs while trying to obtain the info tag, a `PyCMSError` is
raised.

Use this function to obtain the information stored in the profile’s info tag.
This often contains details about the profile, and how it was created, as
supplied by the creator.

Parameters:

    

**profile** – EITHER a valid CmsProfile object, OR a string of the filename of
an ICC profile.

Returns:

    

A string containing the internal profile information stored in an ICC tag.

Raises:

    

**PyCMSError** –

PIL.ImageCms.getProfileManufacturer(_profile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#getProfileManufacturer)¶
    

(pyCMS) Gets the manufacturer for the given profile.

If `profile` isn’t a valid CmsProfile object or filename to a profile, a
`PyCMSError` is raised.

If an error occurs while trying to obtain the manufacturer tag, a `PyCMSError`
is raised.

Use this function to obtain the information stored in the profile’s
manufacturer tag.

Parameters:

    

**profile** – EITHER a valid CmsProfile object, OR a string of the filename of
an ICC profile.

Returns:

    

A string containing the internal profile information stored in an ICC tag.

Raises:

    

**PyCMSError** –

PIL.ImageCms.getProfileModel(_profile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#getProfileModel)¶
    

(pyCMS) Gets the model for the given profile.

If `profile` isn’t a valid CmsProfile object or filename to a profile, a
`PyCMSError` is raised.

If an error occurs while trying to obtain the model tag, a `PyCMSError` is
raised.

Use this function to obtain the information stored in the profile’s model tag.

Parameters:

    

**profile** – EITHER a valid CmsProfile object, OR a string of the filename of
an ICC profile.

Returns:

    

A string containing the internal profile information stored in an ICC tag.

Raises:

    

**PyCMSError** –

PIL.ImageCms.getProfileName(_profile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_) -> [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#getProfileName)¶
    

(pyCMS) Gets the internal product name for the given profile.

If `profile` isn’t a valid CmsProfile object or filename to a profile, a
`PyCMSError` is raised If an error occurs while trying to obtain the name tag,
a `PyCMSError` is raised.

Use this function to obtain the INTERNAL name of the profile (stored in an ICC
tag in the profile itself), usually the one used when the profile was
originally created. Sometimes this tag also contains additional information
supplied by the creator.

Parameters:

    

**profile** – EITHER a valid CmsProfile object, OR a string of the filename of
an ICC profile.

Returns:

    

A string containing the internal name of the profile as stored in an ICC tag.

Raises:

    

**PyCMSError** –

PIL.ImageCms.get_display_profile(_handle : [SupportsInt](https://docs.python.org/3/library/typing.html#typing.SupportsInt "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_) -> ImageCmsProfile | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#get_display_profile)¶
    

(experimental) Fetches the profile for the current display device.

Returns:

    

`None` if the profile is not known.

PIL.ImageCms.isIntentSupported(_profile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _intent : Intent_, _direction : Direction_) -> [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "\(in Python v3.14\)")[-1, 1][[source]](../_modules/PIL/ImageCms.html#isIntentSupported)¶
    

(pyCMS) Checks if a given intent is supported.

Use this function to verify that you can use your desired `intent` with
`profile`, and that `profile` can be used for the input/output/proof profile
as you desire.

Some profiles are created specifically for one “direction”, can cannot be used
for others. Some profiles can only be used for certain rendering intents, so
it’s best to either verify this before trying to create a transform with them
(using this function), or catch the potential `PyCMSError` that will occur if
they don’t support the modes you select.

Parameters:

    

  * **profile** – EITHER a valid CmsProfile object, OR a string of the filename of an ICC profile.

  * **intent** – 

Integer (0-3) specifying the rendering intent you wish to use with this
profile

> ImageCms.Intent.PERCEPTUAL = 0 (DEFAULT)
> ImageCms.Intent.RELATIVE_COLORIMETRIC = 1 ImageCms.Intent.SATURATION = 2
> ImageCms.Intent.ABSOLUTE_COLORIMETRIC = 3

see the pyCMS documentation for details on rendering intents and what

    

they do.

  * **direction** – 

Integer specifying if the profile is to be used for input, output, or proof

> INPUT = 0 (or use ImageCms.Direction.INPUT) OUTPUT = 1 (or use
> ImageCms.Direction.OUTPUT) PROOF = 2 (or use ImageCms.Direction.PROOF)

Returns:

    

1 if the intent/direction are supported, -1 if they are not.

Raises:

    

**PyCMSError** –

PIL.ImageCms.profileToProfile(_im : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _inputProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _outputProfile : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [SupportsRead](internal_modules.html#PIL._typing.SupportsRead "PIL._typing.SupportsRead")[[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "\(in Python v3.14\)")] | CmsProfile | ImageCmsProfile_, _renderingIntent : Intent = Intent.PERCEPTUAL_, _outputMode : [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _inPlace : [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") = False_, _flags : Flags = <Flags.NONE: 0>_) -> [Image](Image.html#PIL.Image.Image "PIL.Image.Image") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageCms.html#profileToProfile)¶
    

(pyCMS) Applies an ICC transformation to a given image, mapping from
`inputProfile` to `outputProfile`.

If the input or output profiles specified are not valid filenames, a
`PyCMSError` will be raised. If `inPlace` is `True` and `outputMode !=
im.mode`, a `PyCMSError` will be raised. If an error occurs during application
of the profiles, a `PyCMSError` will be raised. If `outputMode` is not a mode
supported by the `outputProfile` (or by pyCMS), a `PyCMSError` will be raised.

This function applies an ICC transformation to im from `inputProfile`’s color
space to `outputProfile`’s color space using the specified rendering intent to
decide how to handle out-of-gamut colors.

`outputMode` can be used to specify that a color mode conversion is to be done
using these profiles, but the specified profiles must be able to handle that
mode. I.e., if converting im from RGB to CMYK using profiles, the input
profile must handle RGB data, and the output profile must handle CMYK data.

Parameters:

    

  * **im** – An open [`Image`](Image.html#PIL.Image.Image "PIL.Image.Image") object (i.e. Image.new(…) or Image.open(…), etc.)

  * **inputProfile** – String, as a valid filename path to the ICC input profile you wish to use for this image, or a profile object

  * **outputProfile** – String, as a valid filename path to the ICC output profile you wish to use for this image, or a profile object

  * **renderingIntent** – 

Integer (0-3) specifying the rendering intent you wish to use for the
transform

> ImageCms.Intent.PERCEPTUAL = 0 (DEFAULT)
> ImageCms.Intent.RELATIVE_COLORIMETRIC = 1 ImageCms.Intent.SATURATION = 2
> ImageCms.Intent.ABSOLUTE_COLORIMETRIC = 3

see the pyCMS documentation for details on rendering intents and what they do.

  * **outputMode** – A valid PIL mode for the output image (i.e. “RGB”, “CMYK”, etc.). Note: if rendering the image “inPlace”, outputMode MUST be the same mode as the input, or omitted completely. If omitted, the outputMode will be the same as the mode of the input image (im.mode)

  * **inPlace** – Boolean. If `True`, the original image is modified in-place, and `None` is returned. If `False` (default), a new [`Image`](Image.html#PIL.Image.Image "PIL.Image.Image") object is returned with the transform applied.

  * **flags** – Integer (0-…) specifying additional flags

Returns:

    

Either None or a new [`Image`](Image.html#PIL.Image.Image "PIL.Image.Image")
object, depending on the value of `inPlace`

Raises:

    

**PyCMSError** –

## CmsProfile¶

The ICC color profiles are wrapped in an instance of the class `CmsProfile`.
The specification ICC.1:2010 contains more information about the meaning of
the values in ICC profiles.

For convenience, all XYZ-values are also given as xyY-values (so they can be
easily displayed in a chromaticity diagram, for example).

class PIL.ImageCms.core.CmsProfile¶

    

creation_date: [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

Date and time this profile was first created (see 7.2.1 of ICC.1:2010).

version: [float](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.14\)")¶

    

The version number of the ICC standard that this profile follows (e.g. `2.0`).

icc_version: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

Same as `version`, but in encoded format (see 7.2.4 of ICC.1:2010).

device_class: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)")¶

    

4-character string identifying the profile class. One of `scnr`, `mntr`,
`prtr`, `link`, `spac`, `abst`, `nmcl` (see 7.2.5 of ICC.1:2010 for details).

xcolor_space: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)")¶

    

4-character string (padded with whitespace) identifying the color space, e.g.
`XYZ␣`, `RGB␣` or `CMYK` (see 7.2.6 of ICC.1:2010 for details).

connection_space: [str](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.14\)")¶

    

4-character string (padded with whitespace) identifying the color space on the
B-side of the transform (see 7.2.7 of ICC.1:2010 for details).

header_flags: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

The encoded header flags of the profile (see 7.2.11 of ICC.1:2010 for
details).

header_manufacturer: [str](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.14\)")¶

    

4-character string (padded with whitespace) identifying the device
manufacturer, which shall match the signature contained in the appropriate
section of the ICC signature registry found at www.color.org (see 7.2.12 of
ICC.1:2010).

header_model: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)")¶

    

4-character string (padded with whitespace) identifying the device model,
which shall match the signature contained in the appropriate section of the
ICC signature registry found at www.color.org (see 7.2.13 of ICC.1:2010).

attributes: [int](https://docs.python.org/3/library/functions.html#int "\(in
Python v3.14\)")¶

    

Flags used to identify attributes unique to the particular device setup for
which the profile is applicable (see 7.2.14 of ICC.1:2010 for details).

rendering_intent: [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")¶

    

The rendering intent to use when combining this profile with another profile
(usually overridden at run-time, but provided here for DeviceLink and embedded
source profiles, see 7.2.15 of ICC.1:2010).

One of `ImageCms.Intent.ABSOLUTE_COLORIMETRIC`, `ImageCms.Intent.PERCEPTUAL`,
`ImageCms.Intent.RELATIVE_COLORIMETRIC` and `ImageCms.Intent.SATURATION`.

profile_id: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes
"\(in Python v3.14\)")¶

    

A sequence of 16 bytes identifying the profile (via a specially constructed
MD5 sum), or 16 binary zeroes if the profile ID has not been calculated (see
7.2.18 of ICC.1:2010).

copyright: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The text copyright information for the profile (see 9.2.21 of ICC.1:2010).

manufacturer: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The (English) display string for the device manufacturer (see 9.2.22 of
ICC.1:2010).

model: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The (English) display string for the device model of the device for which this
profile is created (see 9.2.23 of ICC.1:2010).

profile_description: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The (English) display string for the profile description (see 9.2.41 of
ICC.1:2010).

target: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The name of the registered characterization data set, or the measurement data
for a characterization target (see 9.2.14 of ICC.1:2010).

red_colorant: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The first column in the matrix used in matrix/TRC transforms (see 9.2.44 of
ICC.1:2010).

The value is in the format `((X, Y, Z), (x, y, Y))`, if available.

green_colorant: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The second column in the matrix used in matrix/TRC transforms (see 9.2.30 of
ICC.1:2010).

The value is in the format `((X, Y, Z), (x, y, Y))`, if available.

blue_colorant: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The third column in the matrix used in matrix/TRC transforms (see 9.2.4 of
ICC.1:2010).

The value is in the format `((X, Y, Z), (x, y, Y))`, if available.

luminance: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The absolute luminance of emissive devices in candelas per square metre as
described by the Y channel (see 9.2.32 of ICC.1:2010).

The value is in the format `((X, Y, Z), (x, y, Y))`, if available.

chromaticity: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The data of the phosphor/colorant chromaticity set used (red, green and blue
channels, see 9.2.16 of ICC.1:2010).

The value is in the format `((x, y, Y), (x, y, Y), (x, y, Y))`, if available.

chromatic_adaption: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The chromatic adaption matrix converts a color measured using the actual
illumination conditions and relative to the actual adopted white, to a color
relative to the PCS adopted white, with complete adaptation from the actual
adopted white chromaticity to the PCS adopted white chromaticity (see 9.2.15
of ICC.1:2010).

Two 3-tuples of floats are returned in a 2-tuple, one in (X, Y, Z) space and
one in (x, y, Y) space.

colorant_table: [list](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)")]¶

    

This tag identifies the colorants used in the profile by a unique name and set
of PCSXYZ or PCSLAB values (see 9.2.19 of ICC.1:2010).

colorant_table_out:
[list](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.14\)")[[str](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.14\)")]¶

    

This tag identifies the colorants used in the profile by a unique name and set
of PCSLAB values (for DeviceLink profiles only, see 9.2.19 of ICC.1:2010).

colorimetric_intent: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

4-character string (padded with whitespace) identifying the image state of PCS
colorimetry produced using the colorimetric intent transforms (see 9.2.20 of
ICC.1:2010 for details).

perceptual_rendering_intent_gamut: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

4-character string (padded with whitespace) identifying the (one) standard
reference medium gamut (see 9.2.37 of ICC.1:2010 for details).

saturation_rendering_intent_gamut: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

4-character string (padded with whitespace) identifying the (one) standard
reference medium gamut (see 9.2.37 of ICC.1:2010 for details).

technology: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

4-character string (padded with whitespace) identifying the device technology
(see 9.2.47 of ICC.1:2010 for details).

media_black_point: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

This tag specifies the media black point and is used for generating absolute
colorimetry.

This tag was available in ICC 3.2, but it is removed from version 4.

The value is in the format `((X, Y, Z), (x, y, Y))`, if available.

media_white_point: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

This tag specifies the media white point and is used for generating absolute
colorimetry.

The value is in the format `((X, Y, Z), (x, y, Y))`, if available.

media_white_point_temperature: [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

Calculates the white point temperature (see the LCMS documentation for more
information).

viewing_condition: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The (English) display string for the viewing conditions (see 9.2.48 of
ICC.1:2010).

screening_description: [str](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)") | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The (English) display string for the screening conditions.

This tag was available in ICC 3.2, but it is removed from version 4.

red_primary: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The XYZ-transformed of the RGB primary color red (1, 0, 0).

The value is in the format `((X, Y, Z), (x, y, Y))`, if available.

green_primary: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The XYZ-transformed of the RGB primary color green (0, 1, 0).

The value is in the format `((X, Y, Z), (x, y, Y))`, if available.

blue_primary: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")], [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

The XYZ-transformed of the RGB primary color blue (0, 0, 1).

The value is in the format `((X, Y, Z), (x, y, Y))`, if available.

is_matrix_shaper: [bool](https://docs.python.org/3/library/functions.html#bool
"\(in Python v3.14\)")¶

    

True if this profile is implemented as a matrix shaper (see documentation on
LCMS).

clut: [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)"), [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)"), [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

Returns a dictionary of all supported intents and directions for the CLUT
model.

The dictionary is indexed by intents (`ImageCms.Intent.ABSOLUTE_COLORIMETRIC`,
`ImageCms.Intent.PERCEPTUAL`, `ImageCms.Intent.RELATIVE_COLORIMETRIC` and
`ImageCms.Intent.SATURATION`).

The values are 3-tuples indexed by directions (`ImageCms.Direction.INPUT`,
`ImageCms.Direction.OUTPUT`, `ImageCms.Direction.PROOF`).

The elements of the tuple are booleans. If the value is `True`, that intent is
supported for that direction.

intent_supported: [dict](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)"), [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)"), [bool](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)")]] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")¶
    

Returns a dictionary of all supported intents and directions.

The dictionary is indexed by intents (`ImageCms.Intent.ABSOLUTE_COLORIMETRIC`,
`ImageCms.Intent.PERCEPTUAL`, `ImageCms.Intent.RELATIVE_COLORIMETRIC` and
`ImageCms.Intent.SATURATION`).

The values are 3-tuples indexed by directions (`ImageCms.Direction.INPUT`,
`ImageCms.Direction.OUTPUT`, `ImageCms.Direction.PROOF`).

The elements of the tuple are booleans. If the value is `True`, that intent is
supported for that direction.

There is one function defined on the class:

is_intent_supported(_intent :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_, _direction :
[int](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.14\)")_, _/_)¶

    

Returns if the intent is supported for the given direction.

Note that you can also get this information for all intents and directions
with `intent_supported`.

Parameters:

    

  * **intent** – One of `ImageCms.Intent.ABSOLUTE_COLORIMETRIC`, `ImageCms.Intent.PERCEPTUAL`, `ImageCms.Intent.RELATIVE_COLORIMETRIC` and `ImageCms.Intent.SATURATION`.

  * **direction** – One of `ImageCms.Direction.INPUT`, `ImageCms.Direction.OUTPUT` and `ImageCms.Direction.PROOF`

Returns:

    

Boolean if the intent and direction is supported.

[ Next `ImageColor` module ](ImageColor.html) [ Previous `ImageChops`
(“channel operations”) module ](ImageChops.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageCms` module
    * `ImageCmsProfile`
      * `ImageCmsProfile.__init__()`
      * `ImageCmsProfile.tobytes()`
    * `ImageCmsTransform`
      * `ImageCmsTransform.apply()`
      * `ImageCmsTransform.apply_in_place()`
      * `ImageCmsTransform.point()`
    * `PyCMSError`
    * Constants
      * `Intent`
        * `Intent.PERCEPTUAL`
        * `Intent.RELATIVE_COLORIMETRIC`
        * `Intent.SATURATION`
        * `Intent.ABSOLUTE_COLORIMETRIC`
      * `Direction`
        * `Direction.INPUT`
        * `Direction.OUTPUT`
        * `Direction.PROOF`
      * `Flags`
        * `Flags.NONE`
        * `Flags.NOCACHE`
        * `Flags.NOOPTIMIZE`
        * `Flags.NULLTRANSFORM`
        * `Flags.GAMUTCHECK`
        * `Flags.SOFTPROOFING`
        * `Flags.BLACKPOINTCOMPENSATION`
        * `Flags.NOWHITEONWHITEFIXUP`
        * `Flags.HIGHRESPRECALC`
        * `Flags.LOWRESPRECALC`
        * `Flags.USE_8BITS_DEVICELINK`
        * `Flags.GUESSDEVICECLASS`
        * `Flags.KEEP_SEQUENCE`
        * `Flags.FORCE_CLUT`
        * `Flags.CLUT_POST_LINEARIZATION`
        * `Flags.CLUT_PRE_LINEARIZATION`
        * `Flags.NONEGATIVES`
        * `Flags.COPY_ALPHA`
        * `Flags.NODEFAULTRESOURCEDEF`
        * `Flags.GRIDPOINTS()`
    * Functions
      * `applyTransform()`
      * `buildProofTransform()`
      * `buildProofTransformFromOpenProfiles()`
      * `buildTransform()`
      * `buildTransformFromOpenProfiles()`
      * `createProfile()`
      * `getDefaultIntent()`
      * `getOpenProfile()`
      * `getProfileCopyright()`
      * `getProfileDescription()`
      * `getProfileInfo()`
      * `getProfileManufacturer()`
      * `getProfileModel()`
      * `getProfileName()`
      * `get_display_profile()`
      * `isIntentSupported()`
      * `profileToProfile()`
    * CmsProfile
      * `CmsProfile`
        * `CmsProfile.creation_date`
        * `CmsProfile.version`
        * `CmsProfile.icc_version`
        * `CmsProfile.device_class`
        * `CmsProfile.xcolor_space`
        * `CmsProfile.connection_space`
        * `CmsProfile.header_flags`
        * `CmsProfile.header_manufacturer`
        * `CmsProfile.header_model`
        * `CmsProfile.attributes`
        * `CmsProfile.rendering_intent`
        * `CmsProfile.profile_id`
        * `CmsProfile.copyright`
        * `CmsProfile.manufacturer`
        * `CmsProfile.model`
        * `CmsProfile.profile_description`
        * `CmsProfile.target`
        * `CmsProfile.red_colorant`
        * `CmsProfile.green_colorant`
        * `CmsProfile.blue_colorant`
        * `CmsProfile.luminance`
        * `CmsProfile.chromaticity`
        * `CmsProfile.chromatic_adaption`
        * `CmsProfile.colorant_table`
        * `CmsProfile.colorant_table_out`
        * `CmsProfile.colorimetric_intent`
        * `CmsProfile.perceptual_rendering_intent_gamut`
        * `CmsProfile.saturation_rendering_intent_gamut`
        * `CmsProfile.technology`
        * `CmsProfile.media_black_point`
        * `CmsProfile.media_white_point`
        * `CmsProfile.media_white_point_temperature`
        * `CmsProfile.viewing_condition`
        * `CmsProfile.screening_description`
        * `CmsProfile.red_primary`
        * `CmsProfile.green_primary`
        * `CmsProfile.blue_primary`
        * `CmsProfile.is_matrix_shaper`
        * `CmsProfile.clut`
        * `CmsProfile.intent_supported`
        * `CmsProfile.is_intent_supported()`

  *[/]: Positional-only parameter separator (PEP 570)

