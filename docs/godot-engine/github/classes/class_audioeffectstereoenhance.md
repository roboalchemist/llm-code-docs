:github_url: hide



# AudioEffectStereoEnhance

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

An audio effect that can be used to adjust the intensity of stereo panning.


## Description

An audio effect that can be used to adjust the intensity of stereo panning.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+---------------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`pan_pullout<class_AudioEffectStereoEnhance_property_pan_pullout>`         | ``1.0`` |
> +---------------------------+---------------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`surround<class_AudioEffectStereoEnhance_property_surround>`               | ``0.0`` |
> +---------------------------+---------------------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`time_pullout_ms<class_AudioEffectStereoEnhance_property_time_pullout_ms>` | ``0.0`` |
> +---------------------------+---------------------------------------------------------------------------------+---------+
>

----


## Property Descriptions



[float<class_float>] **pan_pullout** = `1.0` [🔗<class_AudioEffectStereoEnhance_property_pan_pullout>]


- |void| **set_pan_pullout**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pan_pullout**\ (\ )

Amplifies the difference between stereo channels, increasing or decreasing existing panning. A value of 0.0 will downmix stereo to mono. Does not affect a mono signal.


----



[float<class_float>] **surround** = `0.0` [🔗<class_AudioEffectStereoEnhance_property_surround>]


- |void| **set_surround**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_surround**\ (\ )

Widens sound stage through phase shifting in conjunction with [time_pullout_ms<class_AudioEffectStereoEnhance_property_time_pullout_ms>]. Just pans sound to the left channel if [time_pullout_ms<class_AudioEffectStereoEnhance_property_time_pullout_ms>] is 0.


----



[float<class_float>] **time_pullout_ms** = `0.0` [🔗<class_AudioEffectStereoEnhance_property_time_pullout_ms>]


- |void| **set_time_pullout**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_time_pullout**\ (\ )

Widens sound stage through phase shifting in conjunction with [surround<class_AudioEffectStereoEnhance_property_surround>]. Just delays the right channel if [surround<class_AudioEffectStereoEnhance_property_surround>] is 0.

