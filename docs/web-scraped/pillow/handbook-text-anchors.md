# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/handbook/text-anchors.html
# Path: handbook/text-anchors.html

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
      * Text anchors
      * [Third-party plugins](third-party-plugins.html)
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

[ View this page ](../_sources/handbook/text-anchors.rst.txt "View this page")

# Text anchors¶

The `anchor` parameter determines the alignment of drawn text relative to the
`xy` parameter. The default alignment is top left, specifically `la` (left-
ascender) for horizontal text and `lt` (left-top) for vertical text.

This parameter is only supported by OpenType/TrueType fonts. Other fonts may
ignore the parameter and use the default (top left) alignment.

## Specifying an anchor¶

An anchor is specified with a two-character string. The first character is the
horizontal alignment, the second character is the vertical alignment. For
example, the default value of `la` for horizontal text means left-ascender
aligned text.

When drawing text with
[`PIL.ImageDraw.ImageDraw.text()`](../reference/ImageDraw.html#PIL.ImageDraw.ImageDraw.text
"PIL.ImageDraw.ImageDraw.text") with a specific anchor, the text will be
placed such that the specified anchor point is at the `xy` coordinates.

For example, in the following image, the text is `ms` (middle-baseline)
aligned, with `xy` at the intersection of the two lines:

![ms \(middle-baseline\) aligned text.](../_images/test_anchor_quick_ms.png)

    
    
    from PIL import Image, ImageDraw, ImageFont
    
    font = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", 48)
    im = Image.new("RGB", (200, 200), "white")
    d = ImageDraw.Draw(im)
    d.line(((0, 100), (200, 100)), "gray")
    d.line(((100, 0), (100, 200)), "gray")
    d.text((100, 100), "Quick", fill="black", anchor="ms", font=font)
    

  

## Quick reference¶

![Horizontal text](../_images/anchor_horizontal.svg) ![Vertical
text](../_images/anchor_vertical.svg)

## Horizontal anchor alignment¶

`l` — left

    

Anchor is to the left of the text.

For _horizontal_ text this is the origin of the first glyph, as shown in the
[FreeType tutorial](https://freetype.org/freetype2/docs/tutorial/step2.html).

`m` — middle

    

Anchor is horizontally centered with the text.

For _vertical_ text it is recommended to use `s` (baseline) alignment instead,
as it does not change based on the specific glyphs of the given text.

`r` — right

    

Anchor is to the right of the text.

For _horizontal_ text this is the advanced origin of the last glyph, as shown
in the [FreeType
tutorial](https://freetype.org/freetype2/docs/tutorial/step2.html).

`s` — baseline _(vertical text only)_

    

Anchor is at the baseline (middle) of the text. The exact alignment depends on
the font.

For _vertical_ text this is the recommended alignment, as it does not change
based on the specific glyphs of the given text (see image for vertical text
above).

## Vertical anchor alignment¶

`a` — ascender / top _(horizontal text only)_

    

Anchor is at the ascender line (top) of the first line of text, as defined by
the font.

See [Font metrics on
Wikipedia](https://en.wikipedia.org/wiki/Typeface#Font_metrics) for more
information.

`t` — top _(single-line text only)_

    

Anchor is at the top of the text.

For _vertical_ text this is the origin of the first glyph, as shown in the
[FreeType tutorial](https://freetype.org/freetype2/docs/tutorial/step2.html).

For _horizontal_ text it is recommended to use `a` (ascender) alignment
instead, as it does not change based on the specific glyphs of the given text.

`m` — middle

    

Anchor is vertically centered with the text.

For _horizontal_ text this is the midpoint of the first ascender line and the
last descender line.

`s` — baseline _(horizontal text only)_

    

Anchor is at the baseline (bottom) of the first line of text, only descenders
extend below the anchor.

See [Font metrics on
Wikipedia](https://en.wikipedia.org/wiki/Typeface#Font_metrics) for more
information.

`b` — bottom _(single-line text only)_

    

Anchor is at the bottom of the text.

For _vertical_ text this is the advanced origin of the last glyph, as shown in
the [FreeType
tutorial](https://freetype.org/freetype2/docs/tutorial/step2.html).

For _horizontal_ text it is recommended to use `d` (descender) alignment
instead, as it does not change based on the specific glyphs of the given text.

`d` — descender / bottom _(horizontal text only)_

    

Anchor is at the descender line (bottom) of the last line of text, as defined
by the font.

See [Font metrics on
Wikipedia](https://en.wikipedia.org/wiki/Typeface#Font_metrics) for more
information.

## Examples¶

The following image shows several examples of anchors for horizontal text. In
each section the `xy` parameter was set to the center shown by the
intersection of the two lines.

![Text anchor examples](../_images/anchors.webp)

[ Next Third-party plugins ](third-party-plugins.html) [ Previous Image file
formats ](image-file-formats.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * Text anchors
    * Specifying an anchor
    * Quick reference
    * Horizontal anchor alignment
    * Vertical anchor alignment
    * Examples

