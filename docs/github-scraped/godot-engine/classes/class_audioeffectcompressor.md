:github_url: hide



# AudioEffectCompressor

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Adds a compressor audio effect to an audio bus.

Reduces sounds that exceed a certain threshold level, smooths out the dynamics and increases the overall volume.


## Description

Dynamic range compressor reduces the level of the sound when the amplitude goes over a certain threshold in Decibels. One of the main uses of a compressor is to increase the dynamic range by clipping as little as possible (when sound goes over 0dB).

Compressor has many uses in the mix:

- In the Master bus to compress the whole output (although an [AudioEffectHardLimiter<class_AudioEffectHardLimiter>] is probably better).

- In voice channels to ensure they sound as balanced as possible.

- Sidechained. This can reduce the sound level sidechained with another audio bus for threshold detection. This technique is common in video game mixing to the level of music and SFX while voices are being heard.

- Accentuates transients by using a wider attack, making effects sound more punchy.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`           | :ref:`attack_us<class_AudioEffectCompressor_property_attack_us>`   | ``20.0``  |
> +-------------------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`           | :ref:`gain<class_AudioEffectCompressor_property_gain>`             | ``0.0``   |
> +-------------------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`           | :ref:`mix<class_AudioEffectCompressor_property_mix>`               | ``1.0``   |
> +-------------------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`           | :ref:`ratio<class_AudioEffectCompressor_property_ratio>`           | ``4.0``   |
> +-------------------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`           | :ref:`release_ms<class_AudioEffectCompressor_property_release_ms>` | ``250.0`` |
> +-------------------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`StringName<class_StringName>` | :ref:`sidechain<class_AudioEffectCompressor_property_sidechain>`   | ``&""``   |
> +-------------------------------------+--------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`           | :ref:`threshold<class_AudioEffectCompressor_property_threshold>`   | ``0.0``   |
> +-------------------------------------+--------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[float<class_float>] **attack_us** = `20.0` [🔗<class_AudioEffectCompressor_property_attack_us>]


- |void| **set_attack_us**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_attack_us**\ (\ )

Compressor's reaction time when the signal exceeds the threshold, in microseconds. Value can range from 20 to 2000.


----



[float<class_float>] **gain** = `0.0` [🔗<class_AudioEffectCompressor_property_gain>]


- |void| **set_gain**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_gain**\ (\ )

Gain applied to the output signal.


----



[float<class_float>] **mix** = `1.0` [🔗<class_AudioEffectCompressor_property_mix>]


- |void| **set_mix**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_mix**\ (\ )

Balance between original signal and effect signal. Value can range from 0 (totally dry) to 1 (totally wet).


----



[float<class_float>] **ratio** = `4.0` [🔗<class_AudioEffectCompressor_property_ratio>]


- |void| **set_ratio**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_ratio**\ (\ )

Amount of compression applied to the audio once it passes the threshold level. The higher the ratio, the more the loud parts of the audio will be compressed. Value can range from 1 to 48.


----



[float<class_float>] **release_ms** = `250.0` [🔗<class_AudioEffectCompressor_property_release_ms>]


- |void| **set_release_ms**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_release_ms**\ (\ )

Compressor's delay time to stop reducing the signal after the signal level falls below the threshold, in milliseconds. Value can range from 20 to 2000.


----



[StringName<class_StringName>] **sidechain** = `&""` [🔗<class_AudioEffectCompressor_property_sidechain>]


- |void| **set_sidechain**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_sidechain**\ (\ )

Reduce the sound level using another audio bus for threshold detection.


----



[float<class_float>] **threshold** = `0.0` [🔗<class_AudioEffectCompressor_property_threshold>]


- |void| **set_threshold**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_threshold**\ (\ )

The level above which compression is applied to the audio. Value can range from -60 to 0.

