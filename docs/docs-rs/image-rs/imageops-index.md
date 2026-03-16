image
# Module imageops 
Source 
## Re-exports§
`pub use self::sample::FilterType::CatmullRom;``pub use self::sample::FilterType::Gaussian;``pub use self::sample::FilterType::Lanczos3;``pub use self::sample::FilterType::Nearest;``pub use self::sample::FilterType::Triangle;``pub use self::colorops::brighten;``pub use self::colorops::contrast;``pub use self::colorops::dither;``pub use self::colorops::grayscale;``pub use self::colorops::grayscale_alpha;``pub use self::colorops::grayscale_with_type;``pub use self::colorops::grayscale_with_type_alpha;``pub use self::colorops::huerotate;``pub use self::colorops::index_colors;``pub use self::colorops::invert;``pub use self::colorops::BiLevel;``pub use self::colorops::ColorMap;`
## Modules§
coloropsFunctions for altering and converting the color of pixelbufs
## Structs§
GaussianBlurParametersHolds analytical gaussian blur representation
## Enums§
FilterTypeAvailable Sampling Filters.
## Functions§
blurPerforms a Gaussian blur on the supplied image.blur_advancedPerforms a Gaussian blur on the supplied image.cropReturn a mutable view into an image
The coordinates set the position of the top left corner of the crop.crop_immReturn an immutable view into an image
The coordinates set the position of the top left corner of the crop.fast_blurApproximation of Gaussian blur.filter3x3Perform a 3x3 box filter on the supplied image.flip_horizontalAffine transformations
Flip an image horizontallyflip_horizontal_inAffine transformations
Flip an image horizontally and put the result into the destination `ImageBuffer`.flip_horizontal_in_placeAffine transformations
Flip an image horizontally in place.flip_verticalAffine transformations
Flip an image verticallyflip_vertical_inAffine transformations
Flip an image vertically and put the result into the destination `ImageBuffer`.flip_vertical_in_placeAffine transformations
Flip an image vertically in place.horizontal_gradientFill the image with a linear horizontal gradientinterpolate_bilinearLinearly sample from an image using coordinates in [0, w-1] and [0, h-1].interpolate_nearestSample from an image using coordinates in [0, w-1] and [0, h-1], taking the
nearest pixel.overlayOverlay an image at a given coordinate (x, y)overlay_boundsCalculate the region that can be copied from top to bottom.replaceReplace the contents of an image at a given coordinate (x, y)resizeResize the supplied image to the specified dimensions.rotate90Affine transformations
Rotate an image 90 degrees clockwise.rotate90_inAffine transformations
Rotate an image 90 degrees clockwise and put the result into the destination `ImageBuffer`.rotate180Affine transformations
Rotate an image 180 degrees clockwise.rotate270Affine transformations
Rotate an image 270 degrees clockwise.rotate180_inAffine transformations
Rotate an image 180 degrees clockwise and put the result into the destination `ImageBuffer`.rotate180_in_placeAffine transformations
Rotate an image 180 degrees clockwise in place.rotate270_inAffine transformations
Rotate an image 270 degrees clockwise and put the result into the destination `ImageBuffer`.sample_bilinearLinearly sample from an image using coordinates in [0, 1].sample_nearestSample from an image using coordinates in [0, 1], taking the nearest coordinate.thumbnailResize the supplied image to the specific dimensions.tileTile an image by repeating it multiple timesunsharpenPerforms an unsharpen mask on the supplied image.vertical_gradientFill the image with a linear vertical gradient