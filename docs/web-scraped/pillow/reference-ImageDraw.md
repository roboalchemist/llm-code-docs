# Pillow Documentation
# Source: https://pillow.readthedocs.io/en/latest/reference/ImageDraw.html
# Path: reference/ImageDraw.html

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
    * `ImageDraw` module
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

[ View this page ](../_sources/reference/ImageDraw.rst.txt "View this page")

# `ImageDraw` module¶

The `ImageDraw` module provides simple 2D graphics for
[`Image`](Image.html#PIL.Image.Image "PIL.Image.Image") objects. You can use
this module to create new images, annotate or retouch existing images, and to
generate graphics on the fly for web use.

For a more advanced drawing library for PIL, see the [aggdraw
module](https://github.com/pytroll/aggdraw).

## Example: Draw a gray cross over an image¶

    
    
    import sys
    from PIL import Image, ImageDraw
    
    with Image.open("hopper.jpg") as im:
    
        draw = ImageDraw.Draw(im)
        draw.line((0, 0) + im.size, fill=128)
        draw.line((0, im.size[1], im.size[0], 0), fill=128)
    
        # write to stdout
        im.save(sys.stdout, "PNG")
    

## Concepts¶

### Coordinates¶

The graphics interface uses the same coordinate system as PIL itself, with (0,
0) in the upper left corner. Any pixels drawn outside of the image bounds will
be discarded.

### Colors¶

To specify colors, you can use numbers or tuples just as you would use with
[`PIL.Image.new()`](Image.html#PIL.Image.new "PIL.Image.new"). See
[Colors](../handbook/concepts.html#colors) for more information.

For palette images (mode “P”), use integers as color indexes. In 1.1.4 and
later, you can also use RGB 3-tuples or color names (see below). The drawing
layer will automatically assign color indexes, as long as you don’t draw with
more than 256 colors.

### Color names¶

See [Color names](ImageColor.html#color-names) for the color names supported
by Pillow.

### Alpha channel¶

By default, when drawing onto an existing image, the image’s pixel values are
simply replaced by the new color:

    
    
    im = Image.new("RGBA", (1, 1), (255, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1, 1), (0, 255, 0, 127))
    assert im.getpixel((0, 0)) == (0, 255, 0, 127)
    
    # Alpha channel values have no effect when drawing with RGB mode
    im = Image.new("RGB", (1, 1), (255, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1, 1), (0, 255, 0, 127))
    assert im.getpixel((0, 0)) == (0, 255, 0)
    

If you would like to combine translucent color with an RGB image, then
initialize the ImageDraw instance with the RGBA mode:

    
    
    from PIL import Image, ImageDraw
    im = Image.new("RGB", (1, 1), (255, 0, 0))
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle((0, 0, 1, 1), (0, 255, 0, 127))
    assert im.getpixel((0, 0)) == (128, 127, 0)
    

If you would like to combine translucent color with an RGBA image underneath,
you will need to combine multiple images:

    
    
    from PIL import Image, ImageDraw
    im = Image.new("RGBA", (1, 1), (255, 0, 0, 255))
    im2 = Image.new("RGBA", (1, 1))
    d = ImageDraw.Draw(im2)
    d.rectangle((0, 0, 1, 1), (0, 255, 0, 127))
    im.paste(im2.convert("RGB"), mask=im2)
    assert im.getpixel((0, 0)) == (128, 127, 0, 255)
    

### Fonts¶

PIL can use bitmap fonts or OpenType/TrueType fonts.

Bitmap fonts are stored in PIL’s own format, where each font typically
consists of two files, one named .pil and the other usually named .pbm. The
former contains font metrics, the latter raster data.

To load a bitmap font, use the load functions in the
[`ImageFont`](ImageFont.html#module-PIL.ImageFont "PIL.ImageFont") module.

To load a OpenType/TrueType font, use the truetype function in the
[`ImageFont`](ImageFont.html#module-PIL.ImageFont "PIL.ImageFont") module.
Note that this function depends on third-party libraries, and may not
available in all PIL builds.

## Example: Draw partial opacity text¶

    
    
    from PIL import Image, ImageDraw, ImageFont
    
    # get an image
    with Image.open("Pillow/Tests/images/hopper.png").convert("RGBA") as base:
    
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    
        # get a font
        fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
        # get a drawing context
        d = ImageDraw.Draw(txt)
    
        # draw text, half opacity
        d.text((10, 10), "Hello", font=fnt, fill=(255, 255, 255, 128))
        # draw text, full opacity
        d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 255))
    
        out = Image.alpha_composite(base, txt)
    
        out.show()
    

## Example: Draw multiline text¶

    
    
    from PIL import Image, ImageDraw, ImageFont
    
    # create an image
    out = Image.new("RGB", (150, 100), (255, 255, 255))
    
    # get a font
    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    # get a drawing context
    d = ImageDraw.Draw(out)
    
    # draw multiline text
    d.multiline_text((10, 10), "Hello\nWorld", font=fnt, fill=(0, 0, 0))
    
    out.show()
    

## Functions¶

PIL.ImageDraw.Draw(_im_ , _mode
=None_)[[source]](../_modules/PIL/ImageDraw.html#Draw)¶

    

Creates an object that can be used to draw in the given image.

Note that the image will be modified in place.

Parameters:

    

  * **im** – The image to draw in.

  * **mode** – Optional mode to use for color values. For RGB images, this argument can be RGB or RGBA (to blend the drawing into the image). For all other modes, this argument must be the same as the image mode. If omitted, the mode defaults to the mode of the image.

## Attributes¶

ImageDraw.fill: [bool](https://docs.python.org/3/library/functions.html#bool
"\(in Python v3.14\)") = False¶

    

Selects whether `ImageDraw.ink` should be used as a fill or outline color.

ImageDraw.font¶

    

The current default font.

Can be set per instance:

    
    
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(image)
    draw.font = ImageFont.truetype("Tests/fonts/FreeMono.ttf")
    

Or globally for all future ImageDraw instances:

    
    
    from PIL import ImageDraw, ImageFont
    ImageDraw.ImageDraw.font = ImageFont.truetype("Tests/fonts/FreeMono.ttf")
    

ImageDraw.fontmode¶

    

The current font drawing mode.

Set to `"1"` to disable antialiasing or `"L"` to enable it.

ImageDraw.ink: [int](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.14\)")¶

    

The internal representation of the current default color.

## Methods¶

ImageDraw.getfont()[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.getfont)¶

    

Get the current default font, `ImageDraw.font`.

If the current default font is `None`, it is initialized with
[`ImageFont.load_default()`](ImageFont.html#PIL.ImageFont.load_default
"PIL.ImageFont.load_default").

Returns:

    

An image font.

ImageDraw.arc(_xy_ , _start_ , _end_ , _fill =None_, _width
=0_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.arc)¶

    

Draws an arc (a portion of a circle outline) between the start and end angles,
inside the given bounding box.

Parameters:

    

  * **xy** – Two points to define the bounding box. Sequence of `[(x0, y0), (x1, y1)]` or `[x0, y0, x1, y1]`, where `x1 >= x0` and `y1 >= y0`.

  * **start** – Starting angle, in degrees. Angles are measured from 3 o’clock, increasing clockwise.

  * **end** – Ending angle, in degrees.

  * **fill** – Color to use for the arc.

  * **width** – 

The line width, in pixels.

Added in version 5.3.0.

ImageDraw.bitmap(_xy_ , _bitmap_ , _fill
=None_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.bitmap)¶

    

Draws a bitmap (mask) at the given position, using the current fill color for
the non-zero portions. The bitmap should be a valid transparency mask (mode
“1”) or matte (mode “L” or “RGBA”).

This is equivalent to doing `image.paste(xy, color, bitmap)`.

To paste pixel data into an image, use the
[`paste()`](Image.html#PIL.Image.Image.paste "PIL.Image.Image.paste") method
on the image itself.

ImageDraw.chord(_xy_ , _start_ , _end_ , _fill =None_, _outline =None_, _width
=1_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.chord)¶

    

Same as `arc()`, but connects the end points with a straight line.

Parameters:

    

  * **xy** – Two points to define the bounding box. Sequence of `[(x0, y0), (x1, y1)]` or `[x0, y0, x1, y1]`, where `x1 >= x0` and `y1 >= y0`.

  * **outline** – Color to use for the outline.

  * **fill** – Color to use for the fill.

  * **width** – 

The line width, in pixels.

Added in version 5.3.0.

ImageDraw.circle(_xy_ , _radius_ , _fill =None_, _outline =None_, _width
=1_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.circle)¶

    

Draws a circle with a given radius centering on a point.

Added in version 10.4.0.

Parameters:

    

  * **xy** – The point for the center of the circle, e.g. `(x, y)`.

  * **radius** – Radius of the circle.

  * **outline** – Color to use for the outline.

  * **fill** – Color to use for the fill.

  * **width** – The line width, in pixels.

ImageDraw.ellipse(_xy_ , _fill =None_, _outline =None_, _width
=1_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.ellipse)¶

    

Draws an ellipse inside the given bounding box.

Parameters:

    

  * **xy** – Two points to define the bounding box. Sequence of either `[(x0, y0), (x1, y1)]` or `[x0, y0, x1, y1]`, where `x1 >= x0` and `y1 >= y0`.

  * **outline** – Color to use for the outline.

  * **fill** – Color to use for the fill.

  * **width** – 

The line width, in pixels.

Added in version 5.3.0.

ImageDraw.line(_xy_ , _fill =None_, _width =0_, _joint
=None_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.line)¶

    

Draws a line between the coordinates in the `xy` list. The coordinate pixels
are included in the drawn line.

Parameters:

    

  * **xy** – Sequence of either 2-tuples like `[(x, y), (x, y), ...]` or numeric values like `[x, y, x, y, ...]`.

  * **fill** – Color to use for the line.

  * **width** – 

The line width, in pixels.

Added in version 1.1.5.

Note

This option was broken until version 1.1.6.

  * **joint** – 

Joint type between a sequence of lines. It can be `"curve"`, for rounded
edges, or [`None`](https://docs.python.org/3/library/constants.html#None "\(in
Python v3.14\)").

Added in version 5.3.0.

ImageDraw.pieslice(_xy_ , _start_ , _end_ , _fill =None_, _outline =None_,
_width =1_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.pieslice)¶

    

Same as arc, but also draws straight lines between the end points and the
center of the bounding box.

Parameters:

    

  * **xy** – Two points to define the bounding box. Sequence of `[(x0, y0), (x1, y1)]` or `[x0, y0, x1, y1]`, where `x1 >= x0` and `y1 >= y0`.

  * **start** – Starting angle, in degrees. Angles are measured from 3 o’clock, increasing clockwise.

  * **end** – Ending angle, in degrees.

  * **fill** – Color to use for the fill.

  * **outline** – Color to use for the outline.

  * **width** – 

The line width, in pixels.

Added in version 5.3.0.

ImageDraw.point(_xy_ , _fill
=None_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.point)¶

    

Draws points (individual pixels) at the given coordinates.

Parameters:

    

  * **xy** – Sequence of either 2-tuples like `[(x, y), (x, y), ...]` or numeric values like `[x, y, x, y, ...]`.

  * **fill** – Color to use for the point.

ImageDraw.polygon(_xy_ , _fill =None_, _outline =None_, _width
=1_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.polygon)¶

    

Draws a polygon.

The polygon outline consists of straight lines between the given coordinates,
plus a straight line between the last and the first coordinate. The coordinate
pixels are included in the drawn polygon.

Parameters:

    

  * **xy** – Sequence of either 2-tuples like `[(x, y), (x, y), ...]` or numeric values like `[x, y, x, y, ...]`.

  * **fill** – Color to use for the fill.

  * **outline** – Color to use for the outline.

  * **width** – The line width, in pixels.

ImageDraw.regular_polygon(_bounding_circle_ , _n_sides_ , _rotation =0_, _fill
=None_, _outline =None_, _width
=1_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.regular_polygon)¶

    

Draws a regular polygon inscribed in `bounding_circle`, with `n_sides`, and
rotation of `rotation` degrees.

Parameters:

    

  * **bounding_circle** – The bounding circle is a tuple defined by a point and radius. (e.g. `bounding_circle=(x, y, r)` or `((x, y), r)`). The polygon is inscribed in this circle.

  * **n_sides** – Number of sides (e.g. `n_sides=3` for a triangle, `6` for a hexagon).

  * **rotation** – Apply an arbitrary rotation to the polygon (e.g. `rotation=90`, applies a 90 degree rotation).

  * **fill** – Color to use for the fill.

  * **outline** – Color to use for the outline.

  * **width** – The line width, in pixels.

ImageDraw.rectangle(_xy_ , _fill =None_, _outline =None_, _width
=1_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.rectangle)¶

    

Draws a rectangle.

Parameters:

    

  * **xy** – Two points to define the bounding box. Sequence of either `[(x0, y0), (x1, y1)]` or `[x0, y0, x1, y1]`, where `x1 >= x0` and `y1 >= y0`. The bounding box is inclusive of both endpoints.

  * **fill** – Color to use for the fill.

  * **outline** – Color to use for the outline.

  * **width** – 

The line width, in pixels.

Added in version 5.3.0.

ImageDraw.rounded_rectangle(_xy_ , _radius =0_, _fill =None_, _outline =None_,
_width =1_, _corners
=None_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.rounded_rectangle)¶

    

Draws a rounded rectangle.

Parameters:

    

  * **xy** – Two points to define the bounding box. Sequence of either `[(x0, y0), (x1, y1)]` or `[x0, y0, x1, y1]`, where `x1 >= x0` and `y1 >= y0`. The bounding box is inclusive of both endpoints.

  * **radius** – Radius of the corners.

  * **fill** – Color to use for the fill.

  * **outline** – Color to use for the outline.

  * **width** – The line width, in pixels.

  * **corners** – A tuple of whether to round each corner, `(top_left, top_right, bottom_right, bottom_left)`. Keyword-only argument.

Added in version 8.2.0.

ImageDraw.shape(_shape_ , _fill =None_, _outline
=None_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.shape)¶

    

Warning

This method is experimental.

Draw a shape.

ImageDraw.text(_xy_ , _text_ , _fill =None_, _font =None_, _anchor =None_,
_spacing =4_, _align ='left'_, _direction =None_, _features =None_, _language
=None_, _stroke_width =0_, _stroke_fill =None_, _embedded_color =False_,
_font_size =None_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.text)¶

    

Draws the string at the given position.

Parameters:

    

  * **xy** – The anchor coordinates of the text.

  * **text** – String to be drawn. If it contains any newline characters, the text is passed on to `multiline_text()`.

  * **fill** – Color to use for the text.

  * **font** – An [`ImageFont`](ImageFont.html#PIL.ImageFont.ImageFont "PIL.ImageFont.ImageFont") instance.

  * **anchor** – 

The text anchor alignment. Determines the relative location of the anchor to
the text. The default alignment is top left, specifically `la` for horizontal
text and `lt` for vertical text. See [Text anchors](../handbook/text-
anchors.html#text-anchors) for details. This parameter is ignored for non-
TrueType fonts.

> Note
>
> This parameter was present in earlier versions of Pillow, but implemented
> only in version 8.0.0.

  * **spacing** – If the text is passed on to `multiline_text()`, the number of pixels between lines.

  * **align** – 

If the text is passed on to `multiline_text()`, `"left"`, `"center"`,
`"right"` or `"justify"`. Determines the relative alignment of lines. Use the
`anchor` parameter to specify the alignment to `xy`.

Added in version 11.2.1: `"justify"`

  * **direction** – 

Direction of the text. It can be `"rtl"` (right to left), `"ltr"` (left to
right) or `"ttb"` (top to bottom). Requires libraqm.

Added in version 4.2.0.

  * **features** – 

A list of OpenType font features to be used during text layout. This is
usually used to turn on optional font features that are not enabled by
default, for example `"dlig"` or `"ss01"`, but can be also used to turn off
default font features, for example `"-liga"` to disable ligatures or `"-kern"`
to disable kerning. To get all supported features, see [OpenType
docs](https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist).
Requires libraqm.

Added in version 4.2.0.

  * **language** – 

Language of the text. Different languages may use different glyph shapes or
ligatures. This parameter tells the font which language the text is in, and to
apply the correct substitutions as appropriate, if available. It should be a
[BCP 47 language code](https://www.w3.org/International/articles/language-
tags/). Requires libraqm.

Added in version 6.0.0.

  * **stroke_width** – 

The width of the text stroke.

Added in version 6.2.0.

  * **stroke_fill** – 

Color to use for the text stroke. If not given, will default to the `fill`
parameter.

Added in version 6.2.0.

  * **embedded_color** – 

Whether to use font embedded color glyphs (COLR, CBDT, SBIX).

Added in version 8.0.0.

  * **font_size** – 

If `font` is not provided, then the size to use for the default

    

font. Keyword-only argument.

Added in version 10.1.0.

ImageDraw.multiline_text(_xy_ , _text_ , _fill =None_, _font =None_, _anchor
=None_, _spacing =4_, _align ='left'_, _direction =None_, _features =None_,
_language =None_, _stroke_width =0_, _stroke_fill =None_, _embedded_color
=False_, _font_size
=None_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.multiline_text)¶

    

Draws the string at the given position.

Parameters:

    

  * **xy** – The anchor coordinates of the text.

  * **text** – String to be drawn.

  * **fill** – Color to use for the text.

  * **font** – An [`ImageFont`](ImageFont.html#PIL.ImageFont.ImageFont "PIL.ImageFont.ImageFont") instance.

  * **anchor** – 

The text anchor alignment. Determines the relative location of the anchor to
the text. The default alignment is top left, specifically `la` for horizontal
text and `lt` for vertical text. See [Text anchors](../handbook/text-
anchors.html#text-anchors) for details. This parameter is ignored for non-
TrueType fonts.

> Note
>
> This parameter was present in earlier versions of Pillow, but implemented
> only in version 8.0.0.

  * **spacing** – The number of pixels between lines.

  * **align** – 

`"left"`, `"center"`, `"right"` or `"justify"`. Determines the relative
alignment of lines. Use the `anchor` parameter to specify the alignment to
`xy`.

Added in version 11.2.1: `"justify"`

  * **direction** – 

Direction of the text. It can be `"rtl"` (right to left), `"ltr"` (left to
right) or `"ttb"` (top to bottom). Requires libraqm.

Added in version 4.2.0.

  * **features** – 

A list of OpenType font features to be used during text layout. This is
usually used to turn on optional font features that are not enabled by
default, for example `"dlig"` or `"ss01"`, but can be also used to turn off
default font features, for example `"-liga"` to disable ligatures or `"-kern"`
to disable kerning. To get all supported features, see [OpenType
docs](https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist).
Requires libraqm.

Added in version 4.2.0.

  * **language** – 

Language of the text. Different languages may use different glyph shapes or
ligatures. This parameter tells the font which language the text is in, and to
apply the correct substitutions as appropriate, if available. It should be a
[BCP 47 language code](https://www.w3.org/International/articles/language-
tags/). Requires libraqm.

Added in version 6.0.0.

  * **stroke_width** – 

The width of the text stroke.

Added in version 6.2.0.

  * **stroke_fill** – 

Color to use for the text stroke. If not given, will default to

    

the `fill` parameter.

Added in version 6.2.0.

  * **embedded_color** – 

Whether to use font embedded color glyphs (COLR, CBDT, SBIX).

Added in version 8.0.0.

  * **font_size** – 

If `font` is not provided, then the size to use for the default

    

font. Keyword-only argument.

Added in version 10.1.0.

ImageDraw.textlength(_text_ , _font =None_, _direction =None_, _features
=None_, _language =None_, _embedded_color =False_, _font_size
=None_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.textlength)¶

    

Returns length (in pixels with 1/64 precision) of given text when rendered in
font with provided direction, features, and language.

This is the amount by which following text should be offset. Text bounding box
may extend past the length in some fonts, e.g. when using italics or accents.

The result is returned as a float; it is a whole number if using basic layout.

Note that the sum of two lengths may not equal the length of a concatenated
string due to kerning. If you need to adjust for kerning, include the
following character and subtract its length.

For example, instead of

    
    
    hello = draw.textlength("Hello", font)
    world = draw.textlength("World", font)
    hello_world = hello + world  # not adjusted for kerning
    assert hello_world == draw.textlength("HelloWorld", font)  # may fail
    

use

    
    
    hello = draw.textlength("HelloW", font) - draw.textlength(
        "W", font
    )  # adjusted for kerning
    world = draw.textlength("World", font)
    hello_world = hello + world  # adjusted for kerning
    assert hello_world == draw.textlength("HelloWorld", font)  # True
    

or disable kerning with (requires libraqm)

    
    
    hello = draw.textlength("Hello", font, features=["-kern"])
    world = draw.textlength("World", font, features=["-kern"])
    hello_world = hello + world  # kerning is disabled, no need to adjust
    assert hello_world == draw.textlength("HelloWorld", font, features=["-kern"])  # True
    

See also

[`PIL.ImageText.Text.get_length()`](ImageText.html#PIL.ImageText.Text.get_length
"PIL.ImageText.Text.get_length")

Added in version 8.0.0.

Parameters:

    

  * **text** – Text to be measured. May not contain any newline characters.

  * **font** – An [`ImageFont`](ImageFont.html#PIL.ImageFont.ImageFont "PIL.ImageFont.ImageFont") instance.

  * **direction** – Direction of the text. It can be `"rtl"` (right to left), `"ltr"` (left to right) or `"ttb"` (top to bottom). Requires libraqm.

  * **features** – A list of OpenType font features to be used during text layout. This is usually used to turn on optional font features that are not enabled by default, for example `"dlig"` or `"ss01"`, but can be also used to turn off default font features, for example `"-liga"` to disable ligatures or `"-kern"` to disable kerning. To get all supported features, see [OpenType docs](https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist). Requires libraqm.

  * **language** – Language of the text. Different languages may use different glyph shapes or ligatures. This parameter tells the font which language the text is in, and to apply the correct substitutions as appropriate, if available. It should be a [BCP 47 language code](https://www.w3.org/International/articles/language-tags/). Requires libraqm.

  * **embedded_color** – Whether to use font embedded color glyphs (COLR, CBDT, SBIX).

  * **font_size** – 

If `font` is not provided, then the size to use for the default

    

font. Keyword-only argument.

Added in version 10.1.0.

Returns:

    

Either width for horizontal text, or height for vertical text.

ImageDraw.textbbox(_xy_ , _text_ , _font =None_, _anchor =None_, _spacing =4_,
_align ='left'_, _direction =None_, _features =None_, _language =None_,
_stroke_width =0_, _embedded_color =False_, _font_size
=None_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.textbbox)¶

    

Returns bounding box (in pixels) of given text relative to given anchor when
rendered in font with provided direction, features, and language. Only
supported for TrueType fonts.

Use `textlength()` to get the offset of following text with 1/64 pixel
precision. The bounding box includes extra margins for some fonts, e.g.
italics or accents.

Added in version 8.0.0.

Parameters:

    

  * **xy** – The anchor coordinates of the text.

  * **text** – Text to be measured. If it contains any newline characters, the text is passed on to `multiline_textbbox()`.

  * **font** – A [`FreeTypeFont`](ImageFont.html#PIL.ImageFont.FreeTypeFont "PIL.ImageFont.FreeTypeFont") instance.

  * **anchor** – The text anchor alignment. Determines the relative location of the anchor to the text. The default alignment is top left, specifically `la` for horizontal text and `lt` for vertical text. See [Text anchors](../handbook/text-anchors.html#text-anchors) for details. This parameter is ignored for non-TrueType fonts.

  * **spacing** – If the text is passed on to `multiline_textbbox()`, the number of pixels between lines.

  * **align** – 

If the text is passed on to `multiline_textbbox()`, `"left"`, `"center"`,
`"right"` or `"justify"`. Determines the relative alignment of lines. Use the
`anchor` parameter to specify the alignment to `xy`.

Added in version 11.2.1: `"justify"`

  * **direction** – Direction of the text. It can be `"rtl"` (right to left), `"ltr"` (left to right) or `"ttb"` (top to bottom). Requires libraqm.

  * **features** – A list of OpenType font features to be used during text layout. This is usually used to turn on optional font features that are not enabled by default, for example `"dlig"` or `"ss01"`, but can be also used to turn off default font features, for example `"-liga"` to disable ligatures or `"-kern"` to disable kerning. To get all supported features, see [OpenType docs](https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist). Requires libraqm.

  * **language** – Language of the text. Different languages may use different glyph shapes or ligatures. This parameter tells the font which language the text is in, and to apply the correct substitutions as appropriate, if available. It should be a [BCP 47 language code](https://www.w3.org/International/articles/language-tags/). Requires libraqm.

  * **stroke_width** – The width of the text stroke.

  * **embedded_color** – Whether to use font embedded color glyphs (COLR, CBDT, SBIX).

  * **font_size** – 

If `font` is not provided, then the size to use for the default

    

font. Keyword-only argument.

Added in version 10.1.0.

Returns:

    

`(left, top, right, bottom)` bounding box

ImageDraw.multiline_textbbox(_xy_ , _text_ , _font =None_, _anchor =None_,
_spacing =4_, _align ='left'_, _direction =None_, _features =None_, _language
=None_, _stroke_width =0_, _embedded_color =False_, _font_size
=None_)[[source]](../_modules/PIL/ImageDraw.html#ImageDraw.multiline_textbbox)¶

    

Returns bounding box (in pixels) of given text relative to given anchor when
rendered in font with provided direction, features, and language. Only
supported for TrueType fonts.

Use `textlength()` to get the offset of following text with 1/64 pixel
precision. The bounding box includes extra margins for some fonts, e.g.
italics or accents.

See also

[`PIL.ImageText.Text.get_bbox()`](ImageText.html#PIL.ImageText.Text.get_bbox
"PIL.ImageText.Text.get_bbox")

Added in version 8.0.0.

Parameters:

    

  * **xy** – The anchor coordinates of the text.

  * **text** – Text to be measured.

  * **font** – A [`FreeTypeFont`](ImageFont.html#PIL.ImageFont.FreeTypeFont "PIL.ImageFont.FreeTypeFont") instance.

  * **anchor** – The text anchor alignment. Determines the relative location of the anchor to the text. The default alignment is top left, specifically `la` for horizontal text and `lt` for vertical text. See [Text anchors](../handbook/text-anchors.html#text-anchors) for details. This parameter is ignored for non-TrueType fonts.

  * **spacing** – The number of pixels between lines.

  * **align** – 

`"left"`, `"center"`, `"right"` or `"justify"`. Determines the relative
alignment of lines. Use the `anchor` parameter to specify the alignment to
`xy`.

Added in version 11.2.1: `"justify"`

  * **direction** – Direction of the text. It can be `"rtl"` (right to left), `"ltr"` (left to right) or `"ttb"` (top to bottom). Requires libraqm.

  * **features** – A list of OpenType font features to be used during text layout. This is usually used to turn on optional font features that are not enabled by default, for example `"dlig"` or `"ss01"`, but can be also used to turn off default font features, for example `"-liga"` to disable ligatures or `"-kern"` to disable kerning. To get all supported features, see [OpenType docs](https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist). Requires libraqm.

  * **language** – Language of the text. Different languages may use different glyph shapes or ligatures. This parameter tells the font which language the text is in, and to apply the correct substitutions as appropriate, if available. It should be a [BCP 47 language code](https://www.w3.org/International/articles/language-tags/). Requires libraqm.

  * **stroke_width** – The width of the text stroke.

  * **embedded_color** – Whether to use font embedded color glyphs (COLR, CBDT, SBIX).

  * **font_size** – 

If `font` is not provided, then the size to use for the default

    

font. Keyword-only argument.

Added in version 10.1.0.

Returns:

    

`(left, top, right, bottom)` bounding box

PIL.ImageDraw.getdraw(_im =None_, _hints
=None_)[[source]](../_modules/PIL/ImageDraw.html#getdraw)¶

    

Warning

This method is experimental.

A more advanced 2D drawing interface for PIL images, based on the WCK
interface.

Parameters:

    

  * **im** – The image to draw in.

  * **hints** – An optional list of hints.

Returns:

    

A (drawing context, drawing resource factory) tuple.

PIL.ImageDraw.floodfill(_image : [Image](Image.html#PIL.Image.Image "PIL.Image.Image")_, _xy : [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)")]_, _value : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), ...]_, _border : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.14\)")[[int](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), ...] | [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)") = None_, _thresh : [float](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") = 0_) -> [None](https://docs.python.org/3/library/constants.html#None "\(in Python v3.14\)")[[source]](../_modules/PIL/ImageDraw.html#floodfill)¶
    

Warning

This method is experimental.

Fills a bounded region with a given color.

Parameters:

    

  * **image** – Target image.

  * **xy** – Seed position (a 2-item coordinate tuple). See [Coordinate system](../handbook/concepts.html#coordinate-system).

  * **value** – Fill color.

  * **border** – Optional border value. If given, the region consists of pixels with a color different from the border color. If not given, the region consists of pixels having the same color as the seed pixel.

  * **thresh** – Optional threshold value which specifies a maximum tolerable difference of a pixel value from the ‘background’ in order for it to be replaced. Useful for filling regions of non-homogeneous, but similar, colors.

[ Next `ImageEnhance` module ](ImageEnhance.html) [ Previous `ImageColor`
module ](ImageColor.html)

Copyright (C) 1995-2011 Fredrik Lundh and contributors, 2010 Jeffrey A. Clark
and contributors.

Made with [Sphinx](https://www.sphinx-doc.org/) and
[@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)

On this page

  * `ImageDraw` module
    * Example: Draw a gray cross over an image
    * Concepts
      * Coordinates
      * Colors
      * Color names
      * Alpha channel
      * Fonts
    * Example: Draw partial opacity text
    * Example: Draw multiline text
    * Functions
      * `Draw()`
    * Attributes
      * `ImageDraw.fill`
      * `ImageDraw.font`
      * `ImageDraw.fontmode`
      * `ImageDraw.ink`
    * Methods
      * `ImageDraw.getfont()`
      * `ImageDraw.arc()`
      * `ImageDraw.bitmap()`
      * `ImageDraw.chord()`
      * `ImageDraw.circle()`
      * `ImageDraw.ellipse()`
      * `ImageDraw.line()`
      * `ImageDraw.pieslice()`
      * `ImageDraw.point()`
      * `ImageDraw.polygon()`
      * `ImageDraw.regular_polygon()`
      * `ImageDraw.rectangle()`
      * `ImageDraw.rounded_rectangle()`
      * `ImageDraw.shape()`
      * `ImageDraw.text()`
      * `ImageDraw.multiline_text()`
      * `ImageDraw.textlength()`
      * `ImageDraw.textbbox()`
      * `ImageDraw.multiline_textbbox()`
      * `getdraw()`
      * `floodfill()`

