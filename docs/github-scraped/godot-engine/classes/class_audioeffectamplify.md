:github_url: hide



# AudioEffectAmplify

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Adds an amplifying audio effect to an audio bus.


## Description

Increases or decreases the volume being routed through the audio bus.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`volume_db<class_AudioEffectAmplify_property_volume_db>`         | ``0.0`` |
> +---------------------------+-----------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`volume_linear<class_AudioEffectAmplify_property_volume_linear>` |         |
> +---------------------------+-----------------------------------------------------------------------+---------+
>

----


## Property Descriptions



[float<class_float>] **volume_db** = `0.0` [🔗<class_AudioEffectAmplify_property_volume_db>]


- |void| **set_volume_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_volume_db**\ (\ )

Amount of amplification in decibels. Positive values make the sound louder, negative values make it quieter. Value can range from -80 to 24.


----



[float<class_float>] **volume_linear** [🔗<class_AudioEffectAmplify_property_volume_linear>]


- |void| **set_volume_linear**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_volume_linear**\ (\ )

Amount of amplification as a linear value.

\ **Note:** This member modifies [volume_db<class_AudioEffectAmplify_property_volume_db>] for convenience. The returned value is equivalent to the result of [@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>] on [volume_db<class_AudioEffectAmplify_property_volume_db>]. Setting this member is equivalent to setting [volume_db<class_AudioEffectAmplify_property_volume_db>] to the result of [@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>] on a value.

