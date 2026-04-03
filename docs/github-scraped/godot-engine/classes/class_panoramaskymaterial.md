:github_url: hide



# PanoramaSkyMaterial

**Inherits:** [Material<class_Material>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A material that provides a special texture to a [Sky<class_Sky>], usually an HDR panorama.


## Description

A resource referenced in a [Sky<class_Sky>] that is used to draw a background. **PanoramaSkyMaterial** functions similar to skyboxes in other engines, except it uses an equirectangular sky map instead of a [Cubemap<class_Cubemap>].

Using an HDR panorama is strongly recommended for accurate, high-quality reflections. Godot supports the Radiance HDR (`.hdr`) and OpenEXR (`.exr`) image formats for this purpose.

You can use [this tool ](https://danilw.github.io/GLSL-howto/cubemap_to_panorama_js/cubemap_to_panorama.html)_ to convert a cubemap to an equirectangular sky map.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>`         | :ref:`energy_multiplier<class_PanoramaSkyMaterial_property_energy_multiplier>` | ``1.0``  |
> +-----------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`bool<class_bool>`           | :ref:`filter<class_PanoramaSkyMaterial_property_filter>`                       | ``true`` |
> +-----------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`panorama<class_PanoramaSkyMaterial_property_panorama>`                   |          |
> +-----------------------------------+--------------------------------------------------------------------------------+----------+
>

----


## Property Descriptions



[float<class_float>] **energy_multiplier** = `1.0` [🔗<class_PanoramaSkyMaterial_property_energy_multiplier>]


- |void| **set_energy_multiplier**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_energy_multiplier**\ (\ )

The sky's overall brightness multiplier. Higher values result in a brighter sky.


----



[bool<class_bool>] **filter** = `true` [🔗<class_PanoramaSkyMaterial_property_filter>]


- |void| **set_filtering_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_filtering_enabled**\ (\ )

A boolean value to determine if the background texture should be filtered or not.


----



[Texture2D<class_Texture2D>] **panorama** [🔗<class_PanoramaSkyMaterial_property_panorama>]


- |void| **set_panorama**\ (\ value\: [Texture2D<class_Texture2D>]\ )
- [Texture2D<class_Texture2D>] **get_panorama**\ (\ )

[Texture2D<class_Texture2D>] to be applied to the **PanoramaSkyMaterial**.

