:github_url: hide



# AudioEffectHardLimiter

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Adds a hard limiter audio effect to an Audio bus.


## Description

A limiter is an effect designed to disallow sound from going over a given dB threshold. Hard limiters predict volume peaks, and will smoothly apply gain reduction when a peak crosses the ceiling threshold to prevent clipping and distortion. It preserves the waveform and prevents it from crossing the ceiling threshold. Adding one in the Master bus is recommended as a safety measure to prevent sudden volume peaks from occurring, and to prevent distortion caused by clipping.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`ceiling_db<class_AudioEffectHardLimiter_property_ceiling_db>`   | ``-0.3`` |
> +---------------------------+-----------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`pre_gain_db<class_AudioEffectHardLimiter_property_pre_gain_db>` | ``0.0``  |
> +---------------------------+-----------------------------------------------------------------------+----------+
> | :ref:`float<class_float>` | :ref:`release<class_AudioEffectHardLimiter_property_release>`         | ``0.1``  |
> +---------------------------+-----------------------------------------------------------------------+----------+
>

----


## Property Descriptions



[float<class_float>] **ceiling_db** = `-0.3` [🔗<class_AudioEffectHardLimiter_property_ceiling_db>]


- |void| **set_ceiling_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_ceiling_db**\ (\ )

The waveform's maximum allowed value, in decibels. This value can range from `-24.0` to `0.0`.

The default value of `-0.3` prevents potential inter-sample peaks (ISP) from crossing over 0 dB, which can cause slight distortion on some older hardware.


----



[float<class_float>] **pre_gain_db** = `0.0` [🔗<class_AudioEffectHardLimiter_property_pre_gain_db>]


- |void| **set_pre_gain_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pre_gain_db**\ (\ )

Gain to apply before limiting, in decibels.


----



[float<class_float>] **release** = `0.1` [🔗<class_AudioEffectHardLimiter_property_release>]


- |void| **set_release**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_release**\ (\ )

Time it takes in seconds for the gain reduction to fully release.

