# Light2D

# Light2D

Inherits:Node2D<CanvasItem<Node<Object
Inherited By:DirectionalLight2D,PointLight2D
Casts light in a 2D environment.

## Description

Casts light in a 2D environment. A light is defined as a color, an energy value, a mode (see constants), and various other parameters (range and shadows-related).

## Tutorials

- 2D lights and shadows
2D lights and shadows

## Properties

| BlendMode | blend_mode | 0 |
|---|---|---|
| Color | color | Color(1,1,1,1) |
| bool | editor_only | false |
| bool | enabled | true |
| float | energy | 1.0 |
| int | range_item_cull_mask | 1 |
| int | range_layer_max | 0 |
| int | range_layer_min | 0 |
| int | range_z_max | 1024 |
| int | range_z_min | -1024 |
| Color | shadow_color | Color(0,0,0,0) |
| bool | shadow_enabled | false |
| ShadowFilter | shadow_filter | 0 |
| float | shadow_filter_smooth | 0.0 |
| int | shadow_item_cull_mask | 1 |

BlendMode
blend_mode
Color
color
Color(1,1,1,1)
bool
editor_only
false
bool
enabled
true
float
energy
range_item_cull_mask
range_layer_max
range_layer_min
range_z_max
1024
range_z_min
-1024
Color
shadow_color
Color(0,0,0,0)
bool
shadow_enabled
false
ShadowFilter
shadow_filter
float
shadow_filter_smooth
shadow_item_cull_mask

## Methods

| float | get_height()const |
|---|---|
| void | set_height(height:float) |

float
get_height()const
void
set_height(height:float)

## Enumerations

enumShadowFilter:🔗
ShadowFilterSHADOW_FILTER_NONE=0
No filter applies to the shadow map. This provides hard shadow edges and is the fastest to render. Seeshadow_filter.
ShadowFilterSHADOW_FILTER_PCF5=1
Percentage closer filtering (5 samples) applies to the shadow map. This is slower compared to hard shadow rendering. Seeshadow_filter.
ShadowFilterSHADOW_FILTER_PCF13=2
Percentage closer filtering (13 samples) applies to the shadow map. This is the slowest shadow filtering mode, and should be used sparingly. Seeshadow_filter.
enumBlendMode:🔗
BlendModeBLEND_MODE_ADD=0
Adds the value of pixels corresponding to the Light2D to the values of pixels under it. This is the common behavior of a light.
BlendModeBLEND_MODE_SUB=1
Subtracts the value of pixels corresponding to the Light2D to the values of pixels under it, resulting in inversed light effect.
BlendModeBLEND_MODE_MIX=2
Mix the value of pixels corresponding to the Light2D to the values of pixels under it by linear interpolation.

## Property Descriptions

BlendModeblend_mode=0🔗

- voidset_blend_mode(value:BlendMode)
voidset_blend_mode(value:BlendMode)
- BlendModeget_blend_mode()
BlendModeget_blend_mode()
The Light2D's blend mode.
Colorcolor=Color(1,1,1,1)🔗
- voidset_color(value:Color)
voidset_color(value:Color)
- Colorget_color()
Colorget_color()
The Light2D'sColor.
booleditor_only=false🔗
- voidset_editor_only(value:bool)
voidset_editor_only(value:bool)
- boolis_editor_only()
boolis_editor_only()
Iftrue, Light2D will only appear when editing the scene.
boolenabled=true🔗
- voidset_enabled(value:bool)
voidset_enabled(value:bool)
- boolis_enabled()
boolis_enabled()
Iftrue, Light2D will emit light.
floatenergy=1.0🔗
- voidset_energy(value:float)
voidset_energy(value:float)
- floatget_energy()
floatget_energy()
The Light2D's energy value. The larger the value, the stronger the light.
intrange_item_cull_mask=1🔗
- voidset_item_cull_mask(value:int)
voidset_item_cull_mask(value:int)
- intget_item_cull_mask()
intget_item_cull_mask()
The layer mask. Only objects with a matchingCanvasItem.light_maskwill be affected by the Light2D. See alsoshadow_item_cull_mask, which affects which objects can cast shadows.
Note:range_item_cull_maskis ignored byDirectionalLight2D, which will always light a 2D node regardless of the 2D node'sCanvasItem.light_mask.
intrange_layer_max=0🔗
- voidset_layer_range_max(value:int)
voidset_layer_range_max(value:int)
- intget_layer_range_max()
intget_layer_range_max()
Maximum layer value of objects that are affected by the Light2D.
intrange_layer_min=0🔗
- voidset_layer_range_min(value:int)
voidset_layer_range_min(value:int)
- intget_layer_range_min()
intget_layer_range_min()
Minimum layer value of objects that are affected by the Light2D.
intrange_z_max=1024🔗
- voidset_z_range_max(value:int)
voidset_z_range_max(value:int)
- intget_z_range_max()
intget_z_range_max()
Maximumzvalue of objects that are affected by the Light2D.
intrange_z_min=-1024🔗
- voidset_z_range_min(value:int)
voidset_z_range_min(value:int)
- intget_z_range_min()
intget_z_range_min()
Minimumzvalue of objects that are affected by the Light2D.
Colorshadow_color=Color(0,0,0,0)🔗
- voidset_shadow_color(value:Color)
voidset_shadow_color(value:Color)
- Colorget_shadow_color()
Colorget_shadow_color()
Colorof shadows cast by the Light2D.
boolshadow_enabled=false🔗
- voidset_shadow_enabled(value:bool)
voidset_shadow_enabled(value:bool)
- boolis_shadow_enabled()
boolis_shadow_enabled()
Iftrue, the Light2D will cast shadows.
ShadowFiltershadow_filter=0🔗
- voidset_shadow_filter(value:ShadowFilter)
voidset_shadow_filter(value:ShadowFilter)
- ShadowFilterget_shadow_filter()
ShadowFilterget_shadow_filter()
Shadow filter type.
floatshadow_filter_smooth=0.0🔗
- voidset_shadow_smooth(value:float)
voidset_shadow_smooth(value:float)
- floatget_shadow_smooth()
floatget_shadow_smooth()
Smoothing value for shadows. Higher values will result in softer shadows, at the cost of visible streaks that can appear in shadow rendering.shadow_filter_smoothonly has an effect ifshadow_filterisSHADOW_FILTER_PCF5orSHADOW_FILTER_PCF13.
intshadow_item_cull_mask=1🔗
- voidset_item_shadow_cull_mask(value:int)
voidset_item_shadow_cull_mask(value:int)
- intget_item_shadow_cull_mask()
intget_item_shadow_cull_mask()
The shadow mask. Used withLightOccluder2Dto cast shadows. Only occluders with a matchingCanvasItem.light_maskwill cast shadows. See alsorange_item_cull_mask, which affects which objects canreceivethe light.

## Method Descriptions

floatget_height()const🔗
Returns the light's height, which is used in 2D normal mapping. SeePointLight2D.heightandDirectionalLight2D.height.
voidset_height(height:float)🔗
Sets the light's height, which is used in 2D normal mapping. SeePointLight2D.heightandDirectionalLight2D.height.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
