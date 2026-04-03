:github_url: hide



# VisualShaderNodeFloatParameter

**Inherits:** [VisualShaderNodeParameter<class_VisualShaderNodeParameter>] **<** [VisualShaderNode<class_VisualShaderNode>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A scalar float parameter to be used within the visual shader graph.


## Description

Translated to `uniform float` in the shader language.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                             | :ref:`default_value<class_VisualShaderNodeFloatParameter_property_default_value>`                 | ``0.0``   |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                               | :ref:`default_value_enabled<class_VisualShaderNodeFloatParameter_property_default_value_enabled>` | ``false`` |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------+
> | :ref:`Hint<enum_VisualShaderNodeFloatParameter_Hint>` | :ref:`hint<class_VisualShaderNodeFloatParameter_property_hint>`                                   | ``0``     |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                             | :ref:`max<class_VisualShaderNodeFloatParameter_property_max>`                                     | ``1.0``   |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                             | :ref:`min<class_VisualShaderNodeFloatParameter_property_min>`                                     | ``0.0``   |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                             | :ref:`step<class_VisualShaderNodeFloatParameter_property_step>`                                   | ``0.1``   |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------+
>

----


## Enumerations



enum **Hint**: [🔗<enum_VisualShaderNodeFloatParameter_Hint>]



[Hint<enum_VisualShaderNodeFloatParameter_Hint>] **HINT_NONE** = `0`

No hint used.



[Hint<enum_VisualShaderNodeFloatParameter_Hint>] **HINT_RANGE** = `1`

A range hint for scalar value, which limits possible input values between [min<class_VisualShaderNodeFloatParameter_property_min>] and [max<class_VisualShaderNodeFloatParameter_property_max>]. Translated to `hint_range(min, max)` in shader code.



[Hint<enum_VisualShaderNodeFloatParameter_Hint>] **HINT_RANGE_STEP** = `2`

A range hint for scalar value with step, which limits possible input values between [min<class_VisualShaderNodeFloatParameter_property_min>] and [max<class_VisualShaderNodeFloatParameter_property_max>], with a step (increment) of [step<class_VisualShaderNodeFloatParameter_property_step>]). Translated to `hint_range(min, max, step)` in shader code.



[Hint<enum_VisualShaderNodeFloatParameter_Hint>] **HINT_MAX** = `3`

Represents the size of the [Hint<enum_VisualShaderNodeFloatParameter_Hint>] enum.


----


## Property Descriptions



[float<class_float>] **default_value** = `0.0` [🔗<class_VisualShaderNodeFloatParameter_property_default_value>]


- |void| **set_default_value**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_default_value**\ (\ )

A default value to be assigned within the shader.


----



[bool<class_bool>] **default_value_enabled** = `false` [🔗<class_VisualShaderNodeFloatParameter_property_default_value_enabled>]


- |void| **set_default_value_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_default_value_enabled**\ (\ )

Enables usage of the [default_value<class_VisualShaderNodeFloatParameter_property_default_value>].


----



[Hint<enum_VisualShaderNodeFloatParameter_Hint>] **hint** = `0` [🔗<class_VisualShaderNodeFloatParameter_property_hint>]


- |void| **set_hint**\ (\ value\: [Hint<enum_VisualShaderNodeFloatParameter_Hint>]\ )
- [Hint<enum_VisualShaderNodeFloatParameter_Hint>] **get_hint**\ (\ )

A hint applied to the uniform, which controls the values it can take when set through the Inspector.


----



[float<class_float>] **max** = `1.0` [🔗<class_VisualShaderNodeFloatParameter_property_max>]


- |void| **set_max**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_max**\ (\ )

Minimum value for range hints. Used if [hint<class_VisualShaderNodeFloatParameter_property_hint>] is set to [HINT_RANGE<class_VisualShaderNodeFloatParameter_constant_HINT_RANGE>] or [HINT_RANGE_STEP<class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP>].


----



[float<class_float>] **min** = `0.0` [🔗<class_VisualShaderNodeFloatParameter_property_min>]


- |void| **set_min**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_min**\ (\ )

Maximum value for range hints. Used if [hint<class_VisualShaderNodeFloatParameter_property_hint>] is set to [HINT_RANGE<class_VisualShaderNodeFloatParameter_constant_HINT_RANGE>] or [HINT_RANGE_STEP<class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP>].


----



[float<class_float>] **step** = `0.1` [🔗<class_VisualShaderNodeFloatParameter_property_step>]


- |void| **set_step**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_step**\ (\ )

Step (increment) value for the range hint with step. Used if [hint<class_VisualShaderNodeFloatParameter_property_hint>] is set to [HINT_RANGE_STEP<class_VisualShaderNodeFloatParameter_constant_HINT_RANGE_STEP>].

