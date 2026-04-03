:github_url: hide



# AudioEffectLimiter

**Deprecated:** Use [AudioEffectHardLimiter<class_AudioEffectHardLimiter>] instead.

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Adds a soft-clip limiter audio effect to an Audio bus.


## Description

A limiter is similar to a compressor, but it's less flexible and designed to disallow sound going over a given dB threshold. Adding one in the Master bus is always recommended to reduce the effects of clipping.

Soft clipping starts to reduce the peaks a little below the threshold level and progressively increases its effect as the input level increases such that the threshold is never exceeded.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`ceiling_db<class_AudioEffectLimiter_property_ceiling_db>`           | ``-0.1`` |
> +---------------------------+---------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`soft_clip_db<class_AudioEffectLimiter_property_soft_clip_db>`       | ``2.0``  |
> +---------------------------+---------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`soft_clip_ratio<class_AudioEffectLimiter_property_soft_clip_ratio>` | ``10.0`` |
> +---------------------------+---------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`threshold_db<class_AudioEffectLimiter_property_threshold_db>`       | ``0.0``  |
> +---------------------------+---------------------------------------------------------------------------+----------+
>

----


## Property Descriptions



[float<class_float>] **ceiling_db** = `-0.1` [🔗<class_AudioEffectLimiter_property_ceiling_db>]


- |void| **set_ceiling_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_ceiling_db**\ (\ )

The waveform's maximum allowed value, in decibels. Value can range from -20 to -0.1.


----



[float<class_float>] **soft_clip_db** = `2.0` [🔗<class_AudioEffectLimiter_property_soft_clip_db>]


- |void| **set_soft_clip_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_soft_clip_db**\ (\ )

Applies a gain to the limited waves, in decibels. Value can range from 0 to 6.


----



[float<class_float>] **soft_clip_ratio** = `10.0` [🔗<class_AudioEffectLimiter_property_soft_clip_ratio>]


- |void| **set_soft_clip_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_soft_clip_ratio**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **threshold_db** = `0.0` [🔗<class_AudioEffectLimiter_property_threshold_db>]


- |void| **set_threshold_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_threshold_db**\ (\ )

Threshold from which the limiter begins to be active, in decibels. Value can range from -30 to 0.

