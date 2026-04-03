:github_url: hide



# AudioEffectEQ

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [AudioEffectEQ10<class_AudioEffectEQ10>], [AudioEffectEQ21<class_AudioEffectEQ21>], [AudioEffectEQ6<class_AudioEffectEQ6>]

Base class for audio equalizers. Gives you control over frequencies.

Use it to create a custom equalizer if [AudioEffectEQ6<class_AudioEffectEQ6>], [AudioEffectEQ10<class_AudioEffectEQ10>] or [AudioEffectEQ21<class_AudioEffectEQ21>] don't fit your needs.


## Description

AudioEffectEQ gives you control over frequencies. Use it to compensate for existing deficiencies in audio. AudioEffectEQs are useful on the Master bus to completely master a mix and give it more character. They are also useful when a game is run on a mobile device, to adjust the mix to that kind of speakers (it can be added but disabled when headphones are plugged).


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`     | :ref:`get_band_count<class_AudioEffectEQ_method_get_band_count>`\ (\ ) |const|                                                                      |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_band_gain_db<class_AudioEffectEQ_method_get_band_gain_db>`\ (\ band_idx\: :ref:`int<class_int>`\ ) |const|                                |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_band_gain_db<class_AudioEffectEQ_method_set_band_gain_db>`\ (\ band_idx\: :ref:`int<class_int>`, volume_db\: :ref:`float<class_float>`\ ) |
> +---------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **get_band_count**\ (\ ) |const| [🔗<class_AudioEffectEQ_method_get_band_count>]

Returns the number of bands of the equalizer.


----



[float<class_float>] **get_band_gain_db**\ (\ band_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioEffectEQ_method_get_band_gain_db>]

Returns the band's gain at the specified index, in dB.


----



|void| **set_band_gain_db**\ (\ band_idx\: [int<class_int>], volume_db\: [float<class_float>]\ ) [🔗<class_AudioEffectEQ_method_set_band_gain_db>]

Sets band's gain at the specified index, in dB.

