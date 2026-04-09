# Crate image 
Source 
## Re-exports§
`pub use crate::error::ImageError;``pub use crate::error::ImageResult;`
## Modules§
bufferIterators and other auxiliary structure for the `ImageBuffer` type.codecsEncoding and decoding for various image file formats.errorContains detailed error representation.flatImage representations for ffi.hooksThis module provides a way to register decoding hooks for image formats not directly supported
by this crate.imageopsImage Processing FunctionsioDeprecated io module the original io module has been renamed to `image_reader`.
This is going to be internal.
Input and output of images.mathMathematical helper functions and types.metadataTypes describing image metadata
## Structs§
ConvertColorOptionsInputs to `ImageBuffer::copy_from_color_space`.DelayThe delay of a frame relative to the previous one.FlatSamplesA flat buffer over a (multi channel) image.FrameA single animation frameFramesAn implementation dependent iterator, reading the frames as requestedImageBufferGeneric image bufferImageReaderA multi-format image reader.LimitSupportSet of supported strict limits for a decoder.LimitsResource limits for decoding.LumaGrayscale colors.LumaAGrayscale colors + alpha channelPixelsImmutable pixel iteratorRgbRGB colors.RgbaRGB colors + alpha channelSubImageA View into another image
## Enums§
ColorTypeAn enumeration over supported color types and bit depthsDynamicImageA Dynamic ImageExtendedColorTypeAn enumeration of color types encountered in image formats.ImageFormatAn enumeration of supported image formats.
Not all formats support both encoding and decoding.
## Traits§
AnimationDecoder`AnimationDecoder` traitEncodableLayoutTypes which are safe to treat as an immutable byte slice in a pixel layout
for image encoding.GenericImageA trait for manipulating images.GenericImageViewTrait to inspect an image.ImageDecoderThe trait that all decoders implementImageDecoderRectSpecialized image decoding not be supported by all formatsImageEncoderThe trait all encoders implementPixelA generalized pixel.PixelWithColorTypeThe pixel with an associated `ColorType`.
Not all possible pixels represent one of the predefined `ColorType`s.PrimitiveThe type of each channel in a pixel. For example, this can be `u8`, `u16`, `f32`.
## Functions§
guess_formatGuess image format from memory blockimage_dimensionsRead a tuple containing the (width, height) of the image located at the specified path.
This is faster than fully loading the image and then getting its dimensions.loadCreate a new image from a Reader.load_from_memoryCreate a new image from a byte sliceload_from_memory_with_formatCreate a new image from a byte sliceopenOpen the image located at the path specified.
The image’s format is determined from the path’s file extension.save_bufferSaves the supplied buffer to a file at the path specified.save_buffer_with_formatSaves the supplied buffer to a file given the path and desired format.write_buffer_with_formatWrites the supplied buffer to a writer in the specified format.
## Type Aliases§
GrayAlphaImageSendable grayscale + alpha channel image bufferGrayImageSendable grayscale image bufferRgb32FImageAn image buffer for 32-bit float RGB pixels,
where the backing container is a flattened vector of floats.RgbImageSendable Rgb image bufferRgba32FImageAn image buffer for 32-bit float RGBA pixels,
where the backing container is a flattened vector of floats.RgbaImageSendable Rgb + alpha channel image buffer