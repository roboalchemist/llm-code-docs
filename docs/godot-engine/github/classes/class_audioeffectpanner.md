:github_url: hide



# AudioEffectPanner

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Adds a panner audio effect to an audio bus. Pans sound left or right.


## Description

Determines how much of an audio signal is sent to the left and right buses.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`pan<class_AudioEffectPanner_property_pan>` | ``0.0`` |
> +---------------------------+--------------------------------------------------+---------+
>

----


## Property Descriptions



[float<class_float>] **pan** = `0.0` [🔗<class_AudioEffectPanner_property_pan>]


- |void| **set_pan**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pan**\ (\ )

Pan position. Value can range from -1 (fully left) to 1 (fully right).

