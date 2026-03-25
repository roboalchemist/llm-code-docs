druid

# Crate piet

Source

## Modules§

d2dConvenience wrappers for Direct2D objects.d3ddwriteConvenience wrappers for DirectWrite objects.image_crateOverviewkurbo2D geometry, with a focus on curves.utilutilities shared by various backends
Code useful for multiple backends

## Structs§

BitmapTargetA struct provides a `RenderContext` and then can have its bitmap extracted.D2DDeviceA Direct2D device.D2DDeviceContextThe main context that takes drawing operations.D2DFactoryA Direct2D factory object.D2DLoadedFontsThe set of loaded fonts, shared between `D2DText` instances.D2DRenderContextD2DTextD2DTextLayoutD2DTextLayoutBuilderDeviceA struct that can be used to create bitmap render contexts.DwriteFactoryThis struct is public only to use for system integration in piet_common and druid-shell. It is not intended
that end-users directly use this struct.FixedLinearGradientSpecification of a linear gradient.FixedRadialGradientSpecification of a radial gradient in image-space.FontFamilyA reference to a font family.FontWeightA font weight, represented as a value in the range 1..=1000.GradientStopSpecification of a gradient stop.HitTestPointResult of hit testing a point in a `TextLayout`.HitTestPositionResult of hit testing a text position in a `TextLayout`.ImageBufAn in-memory pixel buffer.LineMetricMetadata about each line in a text layout.LinearGradientA description of a linear gradient in the unit rect, which can be resolved
to a fixed gradient.RadialGradientA description of a radial gradient in the unit rect, which can be resolved
to a fixed gradient.StrokeDashA type that represents an alternating pattern of drawn and undrawn segments.StrokeStyleOptions for drawing stroked lines.UnitPointA representation of a point relative to a unit rectangle.

## Enums§

ColorA datatype representing color.ColorParseErrorErrors that can occur when parsing a hex color.ErrorAn error that can occur while rendering 2D graphics.FixedGradientAny fixed gradient.FontStyleA font style, which may be italic or regular.ImageFormatThe pixel format for bitmap images.InterpolationModeA requested interpolation mode for drawing images.LineCapOptions for the cap of stroked lines.LineJoinOptions for angled joins in strokes.PaintBrushA color or a gradient.ScaleModeMappings from the unit square into a non-square rectangle.TextAlignmentThe alignment of text in a `TextLayout`.TextAttributeAttributes that can be applied to text.

## Traits§

GradientStopsA flexible, ergonomic way to describe gradient stops.ImageA trait for a backend’s bitmap image type.IntoBrushA trait for various types that can be used as brushes.RenderContextThe main trait for rendering graphics.RoundFromA trait for types that can be converted with precision loss.RoundIntoThe companion to `RoundFrom`.TextThe Piet text API.TextLayoutA drawable text object.TextLayoutBuilderA trait for laying out text.TextStorageA type that stores text.

## Type Aliases§

BrushThe associated brush type for this backend.PietThe `RenderContext` for the Direct2D backend, which is selected.PietImageThe associated image type for this backend.PietTextThe associated text factory for this backend.PietTextLayoutThe associated text layout type for this backend.PietTextLayoutBuilderThe associated text layout builder for this backend.
