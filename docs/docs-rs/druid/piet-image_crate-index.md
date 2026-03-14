druid::piet

# Crate image_crate

Source

## Modules§

bufferIterators and other auxiliary structure for the `ImageBuffer` type.codecsEncoding and decoding for various image file formats.errorContains detailed error representation.flatImage representations for ffi.imageopsImage Processing FunctionsioInput and output of images.mathMathematical helper functions and types.

## Structs§

DelayThe delay of a frame relative to the previous one.FlatSamplesA flat buffer over a (multi channel) image.FrameA single animation frameFramesAn implementation dependent iterator, reading the frames as requestedImageBufferGeneric image bufferLumaGrayscale colors.LumaAGrayscale colors + alpha channelPixelsImmutable pixel iteratorProgressRepresents the progress of an image operation.RgbRGB colors.RgbaRGB colors + alpha channelSubImageA View into another image

## Enums§

ColorTypeAn enumeration over supported color types and bit depthsDynamicImageA Dynamic ImageExtendedColorTypeAn enumeration of color types encountered in image formats.ImageErrorThe generic error type for image operations.ImageFormatAn enumeration of supported image formats.
Not all formats support both encoding and decoding.ImageOutputFormatAn enumeration of supported image formats for encoding.

## Traits§

AnimationDecoderAnimationDecoder traitEncodableLayoutTypes which are safe to treat as an immutable byte slice in a pixel layout
for image encoding.GenericImageA trait for manipulating images.GenericImageViewTrait to inspect an image.ImageDecoderThe trait that all decoders implementImageDecoderRectSpecialized image decoding not be supported by all formatsImageEncoderThe trait all encoders implementPixelA generalized pixel.PixelWithColorTypeThe pixel with an associated `ColorType`.
Not all possible pixels represent one of the predefined `ColorType`s.PrimitiveThe type of each channel in a pixel. For example, this can be `u8`, `u16`, `f32`.

## Functions§

guess_formatGuess image format from memory blockimage_dimensionsRead a tuple containing the (width, height) of the image located at the specified path.
This is faster than fully loading the image and then getting its dimensions.loadCreate a new image from a Reader.load_from_memoryCreate a new image from a byte sliceload_from_memory_with_formatCreate a new image from a byte sliceopenOpen the image located at the path specified.
The image’s format is determined from the path’s file extension.save_bufferSaves the supplied buffer to a file at the path specified.save_buffer_with_formatSaves the supplied buffer to a file at the path specified
in the specified format.write_buffer_with_formatWrites the supplied buffer to a writer in the specified format.

## Type Aliases§

GrayAlphaImageSendable grayscale + alpha channel image bufferGrayImageSendable grayscale image bufferImageResultResult of an image decoding/encoding processRgb32FImageAn image buffer for 32-bit float RGB pixels,
where the backing container is a flattened vector of floats.RgbImageSendable Rgb image bufferRgba32FImageAn image buffer for 32-bit float RGBA pixels,
where the backing container is a flattened vector of floats.RgbaImageSendable Rgb + alpha channel image buffer
