:github_url: hide



# GLTFLight

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Represents a glTF light.


## Description

Represents a light as defined by the `KHR_lights_punctual` glTF extension.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)

- [KHR_lights_punctual glTF extension spec ](https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_lights_punctual)_


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`Color<class_Color>`   | :ref:`color<class_GLTFLight_property_color>`                       | ``Color(1, 1, 1, 1)`` |
> +-----------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`   | :ref:`inner_cone_angle<class_GLTFLight_property_inner_cone_angle>` | ``0.0``               |
> +-----------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`   | :ref:`intensity<class_GLTFLight_property_intensity>`               | ``1.0``               |
> +-----------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`String<class_String>` | :ref:`light_type<class_GLTFLight_property_light_type>`             | ``""``                |
> +-----------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`   | :ref:`outer_cone_angle<class_GLTFLight_property_outer_cone_angle>` | ``0.7853982``         |
> +-----------------------------+--------------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`   | :ref:`range<class_GLTFLight_property_range>`                       | ``inf``               |
> +-----------------------------+--------------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFLight<class_GLTFLight>`   | :ref:`from_dictionary<class_GLTFLight_method_from_dictionary>`\ (\ dictionary\: :ref:`Dictionary<class_Dictionary>`\ ) |static|                                                     |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GLTFLight<class_GLTFLight>`   | :ref:`from_node<class_GLTFLight_method_from_node>`\ (\ light_node\: :ref:`Light3D<class_Light3D>`\ ) |static|                                                                       |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`       | :ref:`get_additional_data<class_GLTFLight_method_get_additional_data>`\ (\ extension_name\: :ref:`StringName<class_StringName>`\ )                                                  |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                              | :ref:`set_additional_data<class_GLTFLight_method_set_additional_data>`\ (\ extension_name\: :ref:`StringName<class_StringName>`, additional_data\: :ref:`Variant<class_Variant>`\ ) |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>` | :ref:`to_dictionary<class_GLTFLight_method_to_dictionary>`\ (\ ) |const|                                                                                                            |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Light3D<class_Light3D>`       | :ref:`to_node<class_GLTFLight_method_to_node>`\ (\ ) |const|                                                                                                                        |
> +-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Color<class_Color>] **color** = `Color(1, 1, 1, 1)` [🔗<class_GLTFLight_property_color>]


- |void| **set_color**\ (\ value\: [Color<class_Color>]\ )
- [Color<class_Color>] **get_color**\ (\ )

The [Color<class_Color>] of the light in linear space. Defaults to white. A black color causes the light to have no effect.

This value is linear to match glTF, but will be converted to nonlinear sRGB when creating a Godot [Light3D<class_Light3D>] node upon import, or converted to linear when exporting a Godot [Light3D<class_Light3D>] to glTF.


----



[float<class_float>] **inner_cone_angle** = `0.0` [🔗<class_GLTFLight_property_inner_cone_angle>]


- |void| **set_inner_cone_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_inner_cone_angle**\ (\ )

The inner angle of the cone in a spotlight. Must be less than or equal to the outer cone angle.

Within this angle, the light is at full brightness. Between the inner and outer cone angles, there is a transition from full brightness to zero brightness. When creating a Godot [SpotLight3D<class_SpotLight3D>], the ratio between the inner and outer cone angles is used to calculate the attenuation of the light.


----



[float<class_float>] **intensity** = `1.0` [🔗<class_GLTFLight_property_intensity>]


- |void| **set_intensity**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_intensity**\ (\ )

The intensity of the light. This is expressed in candelas (lumens per steradian) for point and spot lights, and lux (lumens per m²) for directional lights. When creating a Godot light, this value is converted to a unitless multiplier.


----



[String<class_String>] **light_type** = `""` [🔗<class_GLTFLight_property_light_type>]


- |void| **set_light_type**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_light_type**\ (\ )

The type of the light. The values accepted by Godot are "point", "spot", and "directional", which correspond to Godot's [OmniLight3D<class_OmniLight3D>], [SpotLight3D<class_SpotLight3D>], and [DirectionalLight3D<class_DirectionalLight3D>] respectively.


----



[float<class_float>] **outer_cone_angle** = `0.7853982` [🔗<class_GLTFLight_property_outer_cone_angle>]


- |void| **set_outer_cone_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_outer_cone_angle**\ (\ )

The outer angle of the cone in a spotlight. Must be greater than or equal to the inner angle.

At this angle, the light drops off to zero brightness. Between the inner and outer cone angles, there is a transition from full brightness to zero brightness. If this angle is a half turn, then the spotlight emits in all directions. When creating a Godot [SpotLight3D<class_SpotLight3D>], the outer cone angle is used as the angle of the spotlight.


----



[float<class_float>] **range** = `inf` [🔗<class_GLTFLight_property_range>]


- |void| **set_range**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_range**\ (\ )

The range of the light, beyond which the light has no effect. glTF lights with no range defined behave like physical lights (which have infinite range). When creating a Godot light, the range is clamped to `4096.0`.


----


## Method Descriptions



[GLTFLight<class_GLTFLight>] **from_dictionary**\ (\ dictionary\: [Dictionary<class_Dictionary>]\ ) |static| [🔗<class_GLTFLight_method_from_dictionary>]

Creates a new GLTFLight instance by parsing the given [Dictionary<class_Dictionary>].


----



[GLTFLight<class_GLTFLight>] **from_node**\ (\ light_node\: [Light3D<class_Light3D>]\ ) |static| [🔗<class_GLTFLight_method_from_node>]

Create a new GLTFLight instance from the given Godot [Light3D<class_Light3D>] node.


----



[Variant<class_Variant>] **get_additional_data**\ (\ extension_name\: [StringName<class_StringName>]\ ) [🔗<class_GLTFLight_method_get_additional_data>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_additional_data**\ (\ extension_name\: [StringName<class_StringName>], additional_data\: [Variant<class_Variant>]\ ) [🔗<class_GLTFLight_method_set_additional_data>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Dictionary<class_Dictionary>] **to_dictionary**\ (\ ) |const| [🔗<class_GLTFLight_method_to_dictionary>]

Serializes this GLTFLight instance into a [Dictionary<class_Dictionary>].


----



[Light3D<class_Light3D>] **to_node**\ (\ ) |const| [🔗<class_GLTFLight_method_to_node>]

Converts this GLTFLight instance into a Godot [Light3D<class_Light3D>] node.

