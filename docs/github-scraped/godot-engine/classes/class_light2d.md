:github_url: hide



# Light2D

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

**Inherited By:** [DirectionalLight2D<class_DirectionalLight2D>], [PointLight2D<class_PointLight2D>]

Casts light in a 2D environment.


## Description

Casts light in a 2D environment. A light is defined as a color, an energy value, a mode (see constants), and various other parameters (range and shadows-related).


## Tutorials

- [../tutorials/2d/2d_lights_and_shadows](2D lights and shadows .md)


## Properties

> **TABLE**
> :widths: auto
>
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`BlendMode<enum_Light2D_BlendMode>`       | :ref:`blend_mode<class_Light2D_property_blend_mode>`                       | ``0``                 |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`                      | :ref:`color<class_Light2D_property_color>`                                 | ``Color(1, 1, 1, 1)`` |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                        | :ref:`editor_only<class_Light2D_property_editor_only>`                     | ``false``             |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                        | :ref:`enabled<class_Light2D_property_enabled>`                             | ``true``              |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                      | :ref:`energy<class_Light2D_property_energy>`                               | ``1.0``               |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                          | :ref:`range_item_cull_mask<class_Light2D_property_range_item_cull_mask>`   | ``1``                 |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                          | :ref:`range_layer_max<class_Light2D_property_range_layer_max>`             | ``0``                 |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                          | :ref:`range_layer_min<class_Light2D_property_range_layer_min>`             | ``0``                 |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                          | :ref:`range_z_max<class_Light2D_property_range_z_max>`                     | ``1024``              |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                          | :ref:`range_z_min<class_Light2D_property_range_z_min>`                     | ``-1024``             |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`                      | :ref:`shadow_color<class_Light2D_property_shadow_color>`                   | ``Color(0, 0, 0, 0)`` |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                        | :ref:`shadow_enabled<class_Light2D_property_shadow_enabled>`               | ``false``             |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`ShadowFilter<enum_Light2D_ShadowFilter>` | :ref:`shadow_filter<class_Light2D_property_shadow_filter>`                 | ``0``                 |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                      | :ref:`shadow_filter_smooth<class_Light2D_property_shadow_filter_smooth>`   | ``0.0``               |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                          | :ref:`shadow_item_cull_mask<class_Light2D_property_shadow_item_cull_mask>` | ``1``                 |
> +------------------------------------------------+----------------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_height<class_Light2D_method_get_height>`\ (\ ) |const|                             |
> +---------------------------+----------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_height<class_Light2D_method_set_height>`\ (\ height\: :ref:`float<class_float>`\ ) |
> +---------------------------+----------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **ShadowFilter**: [🔗<enum_Light2D_ShadowFilter>]



[ShadowFilter<enum_Light2D_ShadowFilter>] **SHADOW_FILTER_NONE** = `0`

No filter applies to the shadow map. This provides hard shadow edges and is the fastest to render. See [shadow_filter<class_Light2D_property_shadow_filter>].



[ShadowFilter<enum_Light2D_ShadowFilter>] **SHADOW_FILTER_PCF5** = `1`

Percentage closer filtering (5 samples) applies to the shadow map. This is slower compared to hard shadow rendering. See [shadow_filter<class_Light2D_property_shadow_filter>].



[ShadowFilter<enum_Light2D_ShadowFilter>] **SHADOW_FILTER_PCF13** = `2`

Percentage closer filtering (13 samples) applies to the shadow map. This is the slowest shadow filtering mode, and should be used sparingly. See [shadow_filter<class_Light2D_property_shadow_filter>].


----



enum **BlendMode**: [🔗<enum_Light2D_BlendMode>]



[BlendMode<enum_Light2D_BlendMode>] **BLEND_MODE_ADD** = `0`

Adds the value of pixels corresponding to the Light2D to the values of pixels under it. This is the common behavior of a light.



[BlendMode<enum_Light2D_BlendMode>] **BLEND_MODE_SUB** = `1`

Subtracts the value of pixels corresponding to the Light2D to the values of pixels under it, resulting in inversed light effect.



[BlendMode<enum_Light2D_BlendMode>] **BLEND_MODE_MIX** = `2`

Mix the value of pixels corresponding to the Light2D to the values of pixels under it by linear interpolation.


----


## Property Descriptions



[BlendMode<enum_Light2D_BlendMode>] **blend_mode** = `0` [🔗<class_Light2D_property_blend_mode>]


- |void| **set_blend_mode**\ (\ value\: [BlendMode<enum_Light2D_BlendMode>]\ )
- [BlendMode<enum_Light2D_BlendMode>] **get_blend_mode**\ (\ )

The Light2D's blend mode.


----



[Color<class_Color>] **color** = `Color(1, 1, 1, 1)` [🔗<class_Light2D_property_color>]


- |void| **set_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_color**\ (\ )

The Light2D's [Color<class_Color>].


----



[bool<class_bool>] **editor_only** = `false` [🔗<class_Light2D_property_editor_only>]


- |void| **set_editor_only**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_editor_only**\ (\ )

If `true`, Light2D will only appear when editing the scene.


----



[bool<class_bool>] **enabled** = `true` [🔗<class_Light2D_property_enabled>]


- |void| **set_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_enabled**\ (\ )

If `true`, Light2D will emit light.


----



[float<class_float>] **energy** = `1.0` [🔗<class_Light2D_property_energy>]


- |void| **set_energy**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_energy**\ (\ )

The Light2D's energy value. The larger the value, the stronger the light.


----



[int<class_int>] **range_item_cull_mask** = `1` [🔗<class_Light2D_property_range_item_cull_mask>]


- |void| **set_item_cull_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_item_cull_mask**\ (\ )

The layer mask. Only objects with a matching [CanvasItem.light_mask<class_CanvasItem_property_light_mask>] will be affected by the Light2D. See also [shadow_item_cull_mask<class_Light2D_property_shadow_item_cull_mask>], which affects which objects can cast shadows.

\ **Note:** [range_item_cull_mask<class_Light2D_property_range_item_cull_mask>] is ignored by [DirectionalLight2D<class_DirectionalLight2D>], which will always light a 2D node regardless of the 2D node's [CanvasItem.light_mask<class_CanvasItem_property_light_mask>].


----



[int<class_int>] **range_layer_max** = `0` [🔗<class_Light2D_property_range_layer_max>]


- |void| **set_layer_range_max**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_layer_range_max**\ (\ )

Maximum layer value of objects that are affected by the Light2D.


----



[int<class_int>] **range_layer_min** = `0` [🔗<class_Light2D_property_range_layer_min>]


- |void| **set_layer_range_min**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_layer_range_min**\ (\ )

Minimum layer value of objects that are affected by the Light2D.


----



[int<class_int>] **range_z_max** = `1024` [🔗<class_Light2D_property_range_z_max>]


- |void| **set_z_range_max**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_z_range_max**\ (\ )

Maximum `z` value of objects that are affected by the Light2D.


----



[int<class_int>] **range_z_min** = `-1024` [🔗<class_Light2D_property_range_z_min>]


- |void| **set_z_range_min**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_z_range_min**\ (\ )

Minimum `z` value of objects that are affected by the Light2D.


----



[Color<class_Color>] **shadow_color** = `Color(0, 0, 0, 0)` [🔗<class_Light2D_property_shadow_color>]


- |void| **set_shadow_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_shadow_color**\ (\ )

[Color<class_Color>] of shadows cast by the Light2D.


----



[bool<class_bool>] **shadow_enabled** = `false` [🔗<class_Light2D_property_shadow_enabled>]


- |void| **set_shadow_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_shadow_enabled**\ (\ )

If `true`, the Light2D will cast shadows.


----



[ShadowFilter<enum_Light2D_ShadowFilter>] **shadow_filter** = `0` [🔗<class_Light2D_property_shadow_filter>]


- |void| **set_shadow_filter**\ (\ value\: [ShadowFilter<enum_Light2D_ShadowFilter>]\ )
- [ShadowFilter<enum_Light2D_ShadowFilter>] **get_shadow_filter**\ (\ )

Shadow filter type.


----



[float<class_float>] **shadow_filter_smooth** = `0.0` [🔗<class_Light2D_property_shadow_filter_smooth>]


- |void| **set_shadow_smooth**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_shadow_smooth**\ (\ )

Smoothing value for shadows. Higher values will result in softer shadows, at the cost of visible streaks that can appear in shadow rendering. [shadow_filter_smooth<class_Light2D_property_shadow_filter_smooth>] only has an effect if [shadow_filter<class_Light2D_property_shadow_filter>] is [SHADOW_FILTER_PCF5<class_Light2D_constant_SHADOW_FILTER_PCF5>] or [SHADOW_FILTER_PCF13<class_Light2D_constant_SHADOW_FILTER_PCF13>].


----



[int<class_int>] **shadow_item_cull_mask** = `1` [🔗<class_Light2D_property_shadow_item_cull_mask>]


- |void| **set_item_shadow_cull_mask**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_item_shadow_cull_mask**\ (\ )

The shadow mask. Used with [LightOccluder2D<class_LightOccluder2D>] to cast shadows. Only occluders with a matching [CanvasItem.light_mask<class_CanvasItem_property_light_mask>] will cast shadows. See also [range_item_cull_mask<class_Light2D_property_range_item_cull_mask>], which affects which objects can *receive* the light.


----


## Method Descriptions



[float<class_float>] **get_height**\ (\ ) |const| [🔗<class_Light2D_method_get_height>]

Returns the light's height, which is used in 2D normal mapping. See [PointLight2D.height<class_PointLight2D_property_height>] and [DirectionalLight2D.height<class_DirectionalLight2D_property_height>].


----



|void| **set_height**\ (\ height\: [float<class_float>]\ ) [🔗<class_Light2D_method_set_height>]

Sets the light's height, which is used in 2D normal mapping. See [PointLight2D.height<class_PointLight2D_property_height>] and [DirectionalLight2D.height<class_DirectionalLight2D_property_height>].

