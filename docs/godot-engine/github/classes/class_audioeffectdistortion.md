:github_url: hide



# AudioEffectDistortion

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Adds a distortion audio effect to an Audio bus.

Modifies the sound to make it distorted.


## Description

Different types are available: clip, tan, lo-fi (bit crushing), overdrive, or waveshape.

By distorting the waveform the frequency content changes, which will often make the sound "crunchy" or "abrasive". For games, it can simulate sound coming from some saturated device or speaker very efficiently.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------+--------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>`                    | :ref:`drive<class_AudioEffectDistortion_property_drive>`           | ``0.0``     |
> +----------------------------------------------+--------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>`                    | :ref:`keep_hf_hz<class_AudioEffectDistortion_property_keep_hf_hz>` | ``16000.0`` |
> +----------------------------------------------+--------------------------------------------------------------------+-------------+
> | :ref:`Mode<enum_AudioEffectDistortion_Mode>` | :ref:`mode<class_AudioEffectDistortion_property_mode>`             | ``0``       |
> +----------------------------------------------+--------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>`                    | :ref:`post_gain<class_AudioEffectDistortion_property_post_gain>`   | ``0.0``     |
> +----------------------------------------------+--------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>`                    | :ref:`pre_gain<class_AudioEffectDistortion_property_pre_gain>`     | ``0.0``     |
> +----------------------------------------------+--------------------------------------------------------------------+-------------+
>

----


## Enumerations



enum **Mode**: [🔗<enum_AudioEffectDistortion_Mode>]



[Mode<enum_AudioEffectDistortion_Mode>] **MODE_CLIP** = `0`

Digital distortion effect which cuts off peaks at the top and bottom of the waveform.



[Mode<enum_AudioEffectDistortion_Mode>] **MODE_ATAN** = `1`

> **CONTAINER**
>
	There is currently no description for this enum. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!





[Mode<enum_AudioEffectDistortion_Mode>] **MODE_LOFI** = `2`

Low-resolution digital distortion effect (bit depth reduction). You can use it to emulate the sound of early digital audio devices.



[Mode<enum_AudioEffectDistortion_Mode>] **MODE_OVERDRIVE** = `3`

Emulates the warm distortion produced by a field effect transistor, which is commonly used in solid-state musical instrument amplifiers. The [drive<class_AudioEffectDistortion_property_drive>] property has no effect in this mode.



[Mode<enum_AudioEffectDistortion_Mode>] **MODE_WAVESHAPE** = `4`

Waveshaper distortions are used mainly by electronic musicians to achieve an extra-abrasive sound.


----


## Property Descriptions



[float<class_float>] **drive** = `0.0` [🔗<class_AudioEffectDistortion_property_drive>]


- |void| **set_drive**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_drive**\ (\ )

Distortion power. Value can range from 0 to 1.


----



[float<class_float>] **keep_hf_hz** = `16000.0` [🔗<class_AudioEffectDistortion_property_keep_hf_hz>]


- |void| **set_keep_hf_hz**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_keep_hf_hz**\ (\ )

High-pass filter, in Hz. Frequencies higher than this value will not be affected by the distortion. Value can range from 1 to 20000.


----



[Mode<enum_AudioEffectDistortion_Mode>] **mode** = `0` [🔗<class_AudioEffectDistortion_property_mode>]


- |void| **set_mode**\ (\ value\: [Mode<enum_AudioEffectDistortion_Mode>]\ )
- [Mode<enum_AudioEffectDistortion_Mode>] **get_mode**\ (\ )

Distortion type.


----



[float<class_float>] **post_gain** = `0.0` [🔗<class_AudioEffectDistortion_property_post_gain>]


- |void| **set_post_gain**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_post_gain**\ (\ )

Increases or decreases the volume after the effect, in decibels. Value can range from -80 to 24.


----



[float<class_float>] **pre_gain** = `0.0` [🔗<class_AudioEffectDistortion_property_pre_gain>]


- |void| **set_pre_gain**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pre_gain**\ (\ )

Increases or decreases the volume before the effect, in decibels. Value can range from -60 to 60.

