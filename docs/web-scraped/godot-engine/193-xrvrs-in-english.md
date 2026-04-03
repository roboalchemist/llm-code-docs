# XRVRS in English

# XRVRS
Inherits:Object
Helper class for XR interfaces that generates VRS images.

## Description
This class is used by various XR interfaces to generate VRS textures that can be used to speed up rendering.

## Properties

| float | vrs_min_radius | 20.0 |
|---|---|---|
| Rect2i | vrs_render_region | Rect2i(0,0,0,0) |
| float | vrs_strength | 1.0 |

float
vrs_min_radius
20.0
Rect2i
vrs_render_region
Rect2i(0,0,0,0)
float
vrs_strength

## Methods

| RID | make_vrs_texture(target_size:Vector2, eye_foci:PackedVector2Array) |

make_vrs_texture(target_size:Vector2, eye_foci:PackedVector2Array)

## Property Descriptions
floatvrs_min_radius=20.0🔗
- voidset_vrs_min_radius(value:float)
voidset_vrs_min_radius(value:float)
- floatget_vrs_min_radius()
floatget_vrs_min_radius()
The minimum radius around the focal point where full quality is guaranteed if VRS is used as a percentage of screen size.
Rect2ivrs_render_region=Rect2i(0,0,0,0)🔗
- voidset_vrs_render_region(value:Rect2i)
voidset_vrs_render_region(value:Rect2i)
- Rect2iget_vrs_render_region()
Rect2iget_vrs_render_region()
The render region that the VRS texture will be scaled to when generated.
floatvrs_strength=1.0🔗
- voidset_vrs_strength(value:float)
voidset_vrs_strength(value:float)
- floatget_vrs_strength()
floatget_vrs_strength()
The strength used to calculate the VRS density map. The greater this value, the more noticeable VRS is.

## Method Descriptions
RIDmake_vrs_texture(target_size:Vector2, eye_foci:PackedVector2Array)🔗
Generates the VRS texture based on a rendertarget_sizeadjusted by our VRS tile size. For each eyes focal point passed ineye_focia layer is created. Focal point should be in NDC.
The result will be cached, requesting a VRS texture with unchanged parameters and settings will return the cached RID.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.