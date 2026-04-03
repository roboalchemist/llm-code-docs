:github_url: hide



# OpenXRDpadBindingModifier

**Inherits:** [OpenXRIPBindingModifier<class_OpenXRIPBindingModifier>] **<** [OpenXRBindingModifier<class_OpenXRBindingModifier>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

The DPad binding modifier converts an axis input to a dpad output.


## Description

The DPad binding modifier converts an axis input to a dpad output, emulating a DPad. New input paths for each dpad direction will be added to the interaction profile. When bound to actions the DPad emulation will be activated. You should **not** combine dpad inputs with normal inputs in the same action set for the same control, this will result in an error being returned when suggested bindings are submitted to OpenXR.

See [XR_EXT_dpad_binding ](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_EXT_dpad_binding)_ for in-depth details.

\ **Note:** If the DPad binding modifier extension is enabled, all dpad binding paths will be available in the action map. Adding the modifier to an interaction profile allows you to further customize the behavior.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+----------------------------------------------------------------------------------------+---------------+
> | :ref:`OpenXRActionSet<class_OpenXRActionSet>`   | :ref:`action_set<class_OpenXRDpadBindingModifier_property_action_set>`                 |               |
> +-------------------------------------------------+----------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`                       | :ref:`center_region<class_OpenXRDpadBindingModifier_property_center_region>`           | ``0.1``       |
> +-------------------------------------------------+----------------------------------------------------------------------------------------+---------------+
> | :ref:`String<class_String>`                     | :ref:`input_path<class_OpenXRDpadBindingModifier_property_input_path>`                 | ``""``        |
> +-------------------------------------------------+----------------------------------------------------------------------------------------+---------------+
> | :ref:`bool<class_bool>`                         | :ref:`is_sticky<class_OpenXRDpadBindingModifier_property_is_sticky>`                   | ``false``     |
> +-------------------------------------------------+----------------------------------------------------------------------------------------+---------------+
> | :ref:`OpenXRHapticBase<class_OpenXRHapticBase>` | :ref:`off_haptic<class_OpenXRDpadBindingModifier_property_off_haptic>`                 |               |
> +-------------------------------------------------+----------------------------------------------------------------------------------------+---------------+
> | :ref:`OpenXRHapticBase<class_OpenXRHapticBase>` | :ref:`on_haptic<class_OpenXRDpadBindingModifier_property_on_haptic>`                   |               |
> +-------------------------------------------------+----------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`                       | :ref:`threshold<class_OpenXRDpadBindingModifier_property_threshold>`                   | ``0.6``       |
> +-------------------------------------------------+----------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`                       | :ref:`threshold_released<class_OpenXRDpadBindingModifier_property_threshold_released>` | ``0.4``       |
> +-------------------------------------------------+----------------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`                       | :ref:`wedge_angle<class_OpenXRDpadBindingModifier_property_wedge_angle>`               | ``1.5707964`` |
> +-------------------------------------------------+----------------------------------------------------------------------------------------+---------------+
>

----


## Property Descriptions



[OpenXRActionSet<class_OpenXRActionSet>] **action_set** [🔗<class_OpenXRDpadBindingModifier_property_action_set>]


- |void| **set_action_set**\ (\ value\: [OpenXRActionSet<class_OpenXRActionSet>]\ )
- [OpenXRActionSet<class_OpenXRActionSet>] **get_action_set**\ (\ )

Action set for which this dpad binding modifier is active.


----



[float<class_float>] **center_region** = `0.1` [🔗<class_OpenXRDpadBindingModifier_property_center_region>]


- |void| **set_center_region**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_center_region**\ (\ )

Center region in which our center position of our dpad return `true`.


----



[String<class_String>] **input_path** = `""` [🔗<class_OpenXRDpadBindingModifier_property_input_path>]


- |void| **set_input_path**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_input_path**\ (\ )

Input path for this dpad binding modifier.


----



[bool<class_bool>] **is_sticky** = `false` [🔗<class_OpenXRDpadBindingModifier_property_is_sticky>]


- |void| **set_is_sticky**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_is_sticky**\ (\ )

If `false`, when the joystick enters a new dpad zone this becomes `true`.

If `true`, when the joystick remains in active dpad zone, this remains `true` even if we overlap with another zone.


----



[OpenXRHapticBase<class_OpenXRHapticBase>] **off_haptic** [🔗<class_OpenXRDpadBindingModifier_property_off_haptic>]


- |void| **set_off_haptic**\ (\ value\: [OpenXRHapticBase<class_OpenXRHapticBase>]\ )
- [OpenXRHapticBase<class_OpenXRHapticBase>] **get_off_haptic**\ (\ )

Haptic pulse to emit when the user releases the input.


----



[OpenXRHapticBase<class_OpenXRHapticBase>] **on_haptic** [🔗<class_OpenXRDpadBindingModifier_property_on_haptic>]


- |void| **set_on_haptic**\ (\ value\: [OpenXRHapticBase<class_OpenXRHapticBase>]\ )
- [OpenXRHapticBase<class_OpenXRHapticBase>] **get_on_haptic**\ (\ )

Haptic pulse to emit when the user presses the input.


----



[float<class_float>] **threshold** = `0.6` [🔗<class_OpenXRDpadBindingModifier_property_threshold>]


- |void| **set_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_threshold**\ (\ )

When our input value is equal or larger than this value, our dpad in that direction becomes `true`. It stays `true` until it falls under the [threshold_released<class_OpenXRDpadBindingModifier_property_threshold_released>] value.


----



[float<class_float>] **threshold_released** = `0.4` [🔗<class_OpenXRDpadBindingModifier_property_threshold_released>]


- |void| **set_threshold_released**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_threshold_released**\ (\ )

When our input value falls below this, our output becomes `false`.


----



[float<class_float>] **wedge_angle** = `1.5707964` [🔗<class_OpenXRDpadBindingModifier_property_wedge_angle>]


- |void| **set_wedge_angle**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_wedge_angle**\ (\ )

The angle of each wedge that identifies the 4 directions of the emulated dpad.

