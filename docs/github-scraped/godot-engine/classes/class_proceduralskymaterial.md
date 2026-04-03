:github_url: hide



# ProceduralSkyMaterial

**Inherits:** [Material<class_Material>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A material that defines a simple sky for a [Sky<class_Sky>] resource.


## Description

**ProceduralSkyMaterial** provides a way to create an effective background quickly by defining procedural parameters for the sun, the sky and the ground. The sky and ground are defined by a main color, a color at the horizon, and an easing curve to interpolate between them. Suns are described by a position in the sky, a color, and a max angle from the sun at which the easing curve ends. The max angle therefore defines the size of the sun in the sky.

\ **ProceduralSkyMaterial** supports up to 4 suns, using the color, and energy, direction, and angular distance of the first four [DirectionalLight3D<class_DirectionalLight3D>] nodes in the scene. This means that the suns are defined individually by the properties of their corresponding [DirectionalLight3D<class_DirectionalLight3D>]\ s and globally by [sun_angle_max<class_ProceduralSkyMaterial_property_sun_angle_max>] and [sun_curve<class_ProceduralSkyMaterial_property_sun_curve>].

\ **ProceduralSkyMaterial** uses a lightweight shader to draw the sky and is therefore suited for real-time updates. This makes it a great option for a sky that is simple and computationally cheap, but unrealistic. If you need a more realistic procedural option, use [PhysicalSkyMaterial<class_PhysicalSkyMaterial>].


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`float<class_float>`         | :ref:`energy_multiplier<class_ProceduralSkyMaterial_property_energy_multiplier>`               | ``1.0``                              |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`ground_bottom_color<class_ProceduralSkyMaterial_property_ground_bottom_color>`           | ``Color(0.2, 0.169, 0.133, 1)``      |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`float<class_float>`         | :ref:`ground_curve<class_ProceduralSkyMaterial_property_ground_curve>`                         | ``0.02``                             |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`float<class_float>`         | :ref:`ground_energy_multiplier<class_ProceduralSkyMaterial_property_ground_energy_multiplier>` | ``1.0``                              |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`ground_horizon_color<class_ProceduralSkyMaterial_property_ground_horizon_color>`         | ``Color(0.6463, 0.6558, 0.6708, 1)`` |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`sky_cover<class_ProceduralSkyMaterial_property_sky_cover>`                               |                                      |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`sky_cover_modulate<class_ProceduralSkyMaterial_property_sky_cover_modulate>`             | ``Color(1, 1, 1, 1)``                |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`float<class_float>`         | :ref:`sky_curve<class_ProceduralSkyMaterial_property_sky_curve>`                               | ``0.15``                             |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`float<class_float>`         | :ref:`sky_energy_multiplier<class_ProceduralSkyMaterial_property_sky_energy_multiplier>`       | ``1.0``                              |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`sky_horizon_color<class_ProceduralSkyMaterial_property_sky_horizon_color>`               | ``Color(0.6463, 0.6558, 0.6708, 1)`` |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`sky_top_color<class_ProceduralSkyMaterial_property_sky_top_color>`                       | ``Color(0.385, 0.454, 0.55, 1)``     |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`float<class_float>`         | :ref:`sun_angle_max<class_ProceduralSkyMaterial_property_sun_angle_max>`                       | ``30.0``                             |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`float<class_float>`         | :ref:`sun_curve<class_ProceduralSkyMaterial_property_sun_curve>`                               | ``0.15``                             |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`use_debanding<class_ProceduralSkyMaterial_property_use_debanding>`                       | ``true``                             |
> +-----------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **energy_multiplier** = `1.0` [🔗<class_ProceduralSkyMaterial_property_energy_multiplier>]


- |void| **set_energy_multiplier**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_energy_multiplier**\ (\ )

The sky's overall brightness multiplier. Higher values result in a brighter sky.


----



[Color<class_Color>] **ground_bottom_color** = `Color(0.2, 0.169, 0.133, 1)` [🔗<class_ProceduralSkyMaterial_property_ground_bottom_color>]


- |void| **set_ground_bottom_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_ground_bottom_color**\ (\ )

Color of the ground at the bottom. Blends with [ground_horizon_color<class_ProceduralSkyMaterial_property_ground_horizon_color>].


----



[float<class_float>] **ground_curve** = `0.02` [🔗<class_ProceduralSkyMaterial_property_ground_curve>]


- |void| **set_ground_curve**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_ground_curve**\ (\ )

How quickly the [ground_horizon_color<class_ProceduralSkyMaterial_property_ground_horizon_color>] fades into the [ground_bottom_color<class_ProceduralSkyMaterial_property_ground_bottom_color>].


----



[float<class_float>] **ground_energy_multiplier** = `1.0` [🔗<class_ProceduralSkyMaterial_property_ground_energy_multiplier>]


- |void| **set_ground_energy_multiplier**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_ground_energy_multiplier**\ (\ )

Multiplier for ground color. A higher value will make the ground brighter.


----



[Color<class_Color>] **ground_horizon_color** = `Color(0.6463, 0.6558, 0.6708, 1)` [🔗<class_ProceduralSkyMaterial_property_ground_horizon_color>]


- |void| **set_ground_horizon_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_ground_horizon_color**\ (\ )

Color of the ground at the horizon. Blends with [ground_bottom_color<class_ProceduralSkyMaterial_property_ground_bottom_color>].


----



[Texture2D<class_Texture2D>] **sky_cover** [🔗<class_ProceduralSkyMaterial_property_sky_cover>]


- |void| **set_sky_cover**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_sky_cover**\ (\ )

The sky cover texture to use. This texture must use an equirectangular projection (similar to [PanoramaSkyMaterial<class_PanoramaSkyMaterial>]). The texture's colors will be *added* to the existing sky color, and will be multiplied by [sky_energy_multiplier<class_ProceduralSkyMaterial_property_sky_energy_multiplier>] and [sky_cover_modulate<class_ProceduralSkyMaterial_property_sky_cover_modulate>]. This is mainly suited to displaying stars at night, but it can also be used to display clouds at day or night (with a non-physically-accurate look).


----



[Color<class_Color>] **sky_cover_modulate** = `Color(1, 1, 1, 1)` [🔗<class_ProceduralSkyMaterial_property_sky_cover_modulate>]


- |void| **set_sky_cover_modulate**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_sky_cover_modulate**\ (\ )

The tint to apply to the [sky_cover<class_ProceduralSkyMaterial_property_sky_cover>] texture. This can be used to change the sky cover's colors or opacity independently of the sky energy, which is useful for day/night or weather transitions. Only effective if a texture is defined in [sky_cover<class_ProceduralSkyMaterial_property_sky_cover>].


----



[float<class_float>] **sky_curve** = `0.15` [🔗<class_ProceduralSkyMaterial_property_sky_curve>]


- |void| **set_sky_curve**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_sky_curve**\ (\ )

How quickly the [sky_horizon_color<class_ProceduralSkyMaterial_property_sky_horizon_color>] fades into the [sky_top_color<class_ProceduralSkyMaterial_property_sky_top_color>].


----



[float<class_float>] **sky_energy_multiplier** = `1.0` [🔗<class_ProceduralSkyMaterial_property_sky_energy_multiplier>]


- |void| **set_sky_energy_multiplier**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_sky_energy_multiplier**\ (\ )

Multiplier for sky color. A higher value will make the sky brighter.


----



[Color<class_Color>] **sky_horizon_color** = `Color(0.6463, 0.6558, 0.6708, 1)` [🔗<class_ProceduralSkyMaterial_property_sky_horizon_color>]


- |void| **set_sky_horizon_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_sky_horizon_color**\ (\ )

Color of the sky at the horizon. Blends with [sky_top_color<class_ProceduralSkyMaterial_property_sky_top_color>].


----



[Color<class_Color>] **sky_top_color** = `Color(0.385, 0.454, 0.55, 1)` [🔗<class_ProceduralSkyMaterial_property_sky_top_color>]


- |void| **set_sky_top_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_sky_top_color**\ (\ )

Color of the sky at the top. Blends with [sky_horizon_color<class_ProceduralSkyMaterial_property_sky_horizon_color>].


----



[float<class_float>] **sun_angle_max** = `30.0` [🔗<class_ProceduralSkyMaterial_property_sun_angle_max>]


- |void| **set_sun_angle_max**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_sun_angle_max**\ (\ )

Distance from center of sun where it fades out completely.


----



[float<class_float>] **sun_curve** = `0.15` [🔗<class_ProceduralSkyMaterial_property_sun_curve>]


- |void| **set_sun_curve**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_sun_curve**\ (\ )

How quickly the sun fades away between the edge of the sun disk and [sun_angle_max<class_ProceduralSkyMaterial_property_sun_angle_max>].


----



[bool<class_bool>] **use_debanding** = `true` [🔗<class_ProceduralSkyMaterial_property_use_debanding>]


- |void| **set_use_debanding**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_debanding**\ (\ )

If `true`, enables debanding. Debanding adds a small amount of noise which helps reduce banding that appears from the smooth changes in color in the sky.

