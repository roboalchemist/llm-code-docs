:github_url: hide



# AudioEffectSpectrumAnalyzerInstance

**Inherits:** [AudioEffectInstance<class_AudioEffectInstance>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Queryable instance of an [AudioEffectSpectrumAnalyzer<class_AudioEffectSpectrumAnalyzer>].


## Description

The runtime part of an [AudioEffectSpectrumAnalyzer<class_AudioEffectSpectrumAnalyzer>], which can be used to query the magnitude of a frequency range on its host bus.

An instance of this class can be obtained with [AudioServer.get_bus_effect_instance()<class_AudioServer_method_get_bus_effect_instance>].


## Tutorials

- [Audio Spectrum Visualizer Demo ](https://godotengine.org/asset-library/asset/2762)_


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_magnitude_for_frequency_range<class_AudioEffectSpectrumAnalyzerInstance_method_get_magnitude_for_frequency_range>`\ (\ from_hz\: :ref:`float<class_float>`, to_hz\: :ref:`float<class_float>`, mode\: :ref:`MagnitudeMode<enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode>` = 1\ ) |const| |
> +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **MagnitudeMode**: [🔗<enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode>]



[MagnitudeMode<enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode>] **MAGNITUDE_AVERAGE** = `0`

Use the average value across the frequency range as magnitude.



[MagnitudeMode<enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode>] **MAGNITUDE_MAX** = `1`

Use the maximum value of the frequency range as magnitude.


----


## Method Descriptions



[Vector2<class_Vector2>] **get_magnitude_for_frequency_range**\ (\ from_hz\: [float<class_float>], to_hz\: [float<class_float>], mode\: [MagnitudeMode<enum_AudioEffectSpectrumAnalyzerInstance_MagnitudeMode>] = 1\ ) |const| [🔗<class_AudioEffectSpectrumAnalyzerInstance_method_get_magnitude_for_frequency_range>]

Returns the magnitude of the frequencies from `from_hz` to `to_hz` in linear energy as a Vector2. The `x` component of the return value represents the left stereo channel, and `y` represents the right channel.

\ `mode` determines how the frequency range will be processed.

