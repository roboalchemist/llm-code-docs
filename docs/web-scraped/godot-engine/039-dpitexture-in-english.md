# DPITexture in English

# DPITexture
Experimental:This class may be changed or removed in future versions.
Inherits:Texture2D<Texture<Resource<RefCounted<Object
An automatically scalableTexture2Dbased on an SVG image.

## Description
An automatically scalableTexture2Dbased on an SVG image.DPITextures are used to automatically re-rasterize icons and other texture based UI theme elements to match viewport scale and font oversampling. See alsoProjectSettings.display/window/stretch/mode("canvas_items" mode) andViewport.oversampling_override.

## Properties

| float | base_scale | 1.0 |
|---|---|---|
| Dictionary | color_map | {} |
| bool | resource_local_to_scene | false(overridesResource) |
| float | saturation | 1.0 |

float
base_scale
Dictionary
color_map
bool
resource_local_to_scene
false(overridesResource)
float
saturation

## Methods

| DPITexture | create_from_string(source:String, scale:float= 1.0, saturation:float= 1.0, color_map:Dictionary= {})static |
|---|---|
| RID | get_scaled_rid()const |
| String | get_source()const |
| void | set_size_override(size:Vector2i) |
| void | set_source(source:String) |

DPITexture
create_from_string(source:String, scale:float= 1.0, saturation:float= 1.0, color_map:Dictionary= {})static
get_scaled_rid()const
String
get_source()const
void
set_size_override(size:Vector2i)
void
set_source(source:String)

## Property Descriptions
floatbase_scale=1.0🔗
- voidset_base_scale(value:float)
voidset_base_scale(value:float)
- floatget_base_scale()
floatget_base_scale()
Texture scale.1.0is the original SVG size. Higher values result in a larger image.
Dictionarycolor_map={}🔗
- voidset_color_map(value:Dictionary)
voidset_color_map(value:Dictionary)
- Dictionaryget_color_map()
Dictionaryget_color_map()
If set, remaps texture colors according toColor-Colormap.
floatsaturation=1.0🔗
- voidset_saturation(value:float)
voidset_saturation(value:float)
- floatget_saturation()
floatget_saturation()
Overrides texture saturation.

## Method Descriptions
DPITexturecreate_from_string(source:String, scale:float= 1.0, saturation:float= 1.0, color_map:Dictionary= {})static🔗
Creates a newDPITextureand initializes it by allocating and setting the SVG data tosource.
RIDget_scaled_rid()const🔗
Returns theRIDof the texture rasterized to match the oversampling of the currently drawn canvas item.
Stringget_source()const🔗
Returns this SVG texture's source code.
voidset_size_override(size:Vector2i)🔗
Resizes the texture to the specified dimensions.
voidset_source(source:String)🔗
Sets this SVG texture's source code.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.