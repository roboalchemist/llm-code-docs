:github_url: hide



# OpenXRAnalogThresholdModifier

**Inherits:** [OpenXRActionBindingModifier<class_OpenXRActionBindingModifier>] **<** [OpenXRBindingModifier<class_OpenXRBindingModifier>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.


## Description

The analog threshold binding modifier can modify a float input to a boolean input with specified thresholds.

See [XR_VALVE_analog_threshold ](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html#XR_VALVE_analog_threshold)_ for in-depth details.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------+----------------------------------------------------------------------------------+---------+
> | :ref:`OpenXRHapticBase<class_OpenXRHapticBase>` | :ref:`off_haptic<class_OpenXRAnalogThresholdModifier_property_off_haptic>`       |         |
> +-------------------------------------------------+----------------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>`                       | :ref:`off_threshold<class_OpenXRAnalogThresholdModifier_property_off_threshold>` | ``0.4`` |
> +-------------------------------------------------+----------------------------------------------------------------------------------+---------+
> | :ref:`OpenXRHapticBase<class_OpenXRHapticBase>` | :ref:`on_haptic<class_OpenXRAnalogThresholdModifier_property_on_haptic>`         |         |
> +-------------------------------------------------+----------------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>`                       | :ref:`on_threshold<class_OpenXRAnalogThresholdModifier_property_on_threshold>`   | ``0.6`` |
> +-------------------------------------------------+----------------------------------------------------------------------------------+---------+
>

----


## Property Descriptions



[OpenXRHapticBase<class_OpenXRHapticBase>] **off_haptic** [🔗<class_OpenXRAnalogThresholdModifier_property_off_haptic>]


- |void| **set_off_haptic**\ (\ value\: [OpenXRHapticBase<class_OpenXRHapticBase>]\ )
- [OpenXRHapticBase<class_OpenXRHapticBase>] **get_off_haptic**\ (\ )

Haptic pulse to emit when the user releases the input.


----



[float<class_float>] **off_threshold** = `0.4` [🔗<class_OpenXRAnalogThresholdModifier_property_off_threshold>]


- |void| **set_off_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_off_threshold**\ (\ )

When our input value falls below this, our output becomes `false`.


----



[OpenXRHapticBase<class_OpenXRHapticBase>] **on_haptic** [🔗<class_OpenXRAnalogThresholdModifier_property_on_haptic>]


- |void| **set_on_haptic**\ (\ value\: [OpenXRHapticBase<class_OpenXRHapticBase>]\ )
- [OpenXRHapticBase<class_OpenXRHapticBase>] **get_on_haptic**\ (\ )

Haptic pulse to emit when the user presses the input.


----



[float<class_float>] **on_threshold** = `0.6` [🔗<class_OpenXRAnalogThresholdModifier_property_on_threshold>]


- |void| **set_on_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_on_threshold**\ (\ )

When our input value is equal or larger than this value, our output becomes `true`. It stays `true` until it falls under the [off_threshold<class_OpenXRAnalogThresholdModifier_property_off_threshold>] value.

