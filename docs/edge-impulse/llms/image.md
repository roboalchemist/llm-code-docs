# Source: https://docs.edgeimpulse.com/studio/projects/processing-blocks/blocks/image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Image

The **Image** block is dedicated to computer vision applications. It normalizes image data, and optionally reduce the color depth.

GitHub repository containing all DSP block code: [edgeimpulse/processing-blocks](https://github.com/edgeimpulse/processing-blocks).

## Image parameters

* Color depth: Color depth to use (RGB or grayscale)

## How does the image block work?

The **Image** performs normalization, converting each pixel's channel of the image to a float value between 0 and 1. If *Grayscale* is selected, each pixel is converted to a single value following the [ITU-R BT.601 conversion](https://en.wikipedia.org/wiki/YCbCr#ITU-R_BT.601_conversion) (Y' component only).


Built with [Mintlify](https://mintlify.com).