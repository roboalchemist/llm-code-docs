:github_url: hide



# PhysicalSkyMaterial

**Inherits:** [Material<class_Material>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A material that defines a sky for a [Sky<class_Sky>] resource by a set of physical properties.


## Description

The **PhysicalSkyMaterial** uses the Preetham analytic daylight model to draw a sky based on physical properties. This results in a substantially more realistic sky than the [ProceduralSkyMaterial<class_ProceduralSkyMaterial>], but it is slightly slower and less flexible.

The **PhysicalSkyMaterial** only supports one sun. The color, energy, and direction of the sun are taken from the first [DirectionalLight3D<class_DirectionalLight3D>] in the scene tree.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`float<class_float>`         | :ref:`energy_multiplier<class_PhysicalSkyMaterial_property_energy_multiplier>`       | ``1.0``                          |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`ground_color<class_PhysicalSkyMaterial_property_ground_color>`                 | ``Color(0.1, 0.07, 0.034, 1)``   |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`float<class_float>`         | :ref:`mie_coefficient<class_PhysicalSkyMaterial_property_mie_coefficient>`           | ``0.005``                        |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`mie_color<class_PhysicalSkyMaterial_property_mie_color>`                       | ``Color(0.69, 0.729, 0.812, 1)`` |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`float<class_float>`         | :ref:`mie_eccentricity<class_PhysicalSkyMaterial_property_mie_eccentricity>`         | ``0.8``                          |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`night_sky<class_PhysicalSkyMaterial_property_night_sky>`                       |                                  |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`float<class_float>`         | :ref:`rayleigh_coefficient<class_PhysicalSkyMaterial_property_rayleigh_coefficient>` | ``2.0``                          |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`Color<class_Color>`         | :ref:`rayleigh_color<class_PhysicalSkyMaterial_property_rayleigh_color>`             | ``Color(0.3, 0.405, 0.6, 1)``    |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`float<class_float>`         | :ref:`sun_disk_scale<class_PhysicalSkyMaterial_property_sun_disk_scale>`             | ``1.0``                          |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`float<class_float>`         | :ref:`turbidity<class_PhysicalSkyMaterial_property_turbidity>`                       | ``10.0``                         |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`use_debanding<class_PhysicalSkyMaterial_property_use_debanding>`               | ``true``                         |
> +-----------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
>

----


## Property Descriptions



[float<class_float>] **energy_multiplier** = `1.0` [🔗<class_PhysicalSkyMaterial_property_energy_multiplier>]


- |void| **set_energy_multiplier**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_energy_multiplier**\ (\ )

The sky's overall brightness multiplier. Higher values result in a brighter sky.


----



[Color<class_Color>] **ground_color** = `Color(0.1, 0.07, 0.034, 1)` [🔗<class_PhysicalSkyMaterial_property_ground_color>]


- |void| **set_ground_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_ground_color**\ (\ )

Modulates the [Color<class_Color>] on the bottom half of the sky to represent the ground.


----



[float<class_float>] **mie_coefficient** = `0.005` [🔗<class_PhysicalSkyMaterial_property_mie_coefficient>]


- |void| **set_mie_coefficient**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_mie_coefficient**\ (\ )

Controls the strength of [Mie scattering ](https://en.wikipedia.org/wiki/Mie_scattering)_ for the sky. Mie scattering results from light colliding with larger particles (like water). On earth, Mie scattering results in a whitish color around the sun and horizon.


----



[Color<class_Color>] **mie_color** = `Color(0.69, 0.729, 0.812, 1)` [🔗<class_PhysicalSkyMaterial_property_mie_color>]


- |void| **set_mie_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_mie_color**\ (\ )

Controls the [Color<class_Color>] of the [Mie scattering ](https://en.wikipedia.org/wiki/Mie_scattering)_ effect. While not physically accurate, this allows for the creation of alien-looking planets.


----



[float<class_float>] **mie_eccentricity** = `0.8` [🔗<class_PhysicalSkyMaterial_property_mie_eccentricity>]


- |void| **set_mie_eccentricity**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_mie_eccentricity**\ (\ )

Controls the direction of the [Mie scattering ](https://en.wikipedia.org/wiki/Mie_scattering)_. A value of `1` means that when light hits a particle it's passing through straight forward. A value of `-1` means that all light is scatter backwards.


----



[Texture2D<class_Texture2D>] **night_sky** [🔗<class_PhysicalSkyMaterial_property_night_sky>]


- |void| **set_night_sky**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_night_sky**\ (\ )

[Texture2D<class_Texture2D>] for the night sky. This is added to the sky, so if it is bright enough, it may be visible during the day.


----



[float<class_float>] **rayleigh_coefficient** = `2.0` [🔗<class_PhysicalSkyMaterial_property_rayleigh_coefficient>]


- |void| **set_rayleigh_coefficient**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_rayleigh_coefficient**\ (\ )

Controls the strength of the [Rayleigh scattering ](https://en.wikipedia.org/wiki/Rayleigh_scattering)_. Rayleigh scattering results from light colliding with small particles. It is responsible for the blue color of the sky.


----



[Color<class_Color>] **rayleigh_color** = `Color(0.3, 0.405, 0.6, 1)` [🔗<class_PhysicalSkyMaterial_property_rayleigh_color>]


- |void| **set_rayleigh_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_rayleigh_color**\ (\ )

Controls the [Color<class_Color>] of the [Rayleigh scattering ](https://en.wikipedia.org/wiki/Rayleigh_scattering)_. While not physically accurate, this allows for the creation of alien-looking planets. For example, setting this to a red [Color<class_Color>] results in a Mars-looking atmosphere with a corresponding blue sunset.


----



[float<class_float>] **sun_disk_scale** = `1.0` [🔗<class_PhysicalSkyMaterial_property_sun_disk_scale>]


- |void| **set_sun_disk_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_sun_disk_scale**\ (\ )

Sets the size of the sun disk. Default value is based on Sol's perceived size from Earth.


----



[float<class_float>] **turbidity** = `10.0` [🔗<class_PhysicalSkyMaterial_property_turbidity>]


- |void| **set_turbidity**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_turbidity**\ (\ )

Sets the thickness of the atmosphere. High turbidity creates a foggy-looking atmosphere, while a low turbidity results in a clearer atmosphere.


----



[bool<class_bool>] **use_debanding** = `true` [🔗<class_PhysicalSkyMaterial_property_use_debanding>]


- |void| **set_use_debanding**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_use_debanding**\ (\ )

If `true`, enables debanding. Debanding adds a small amount of noise which helps reduce banding that appears from the smooth changes in color in the sky.

