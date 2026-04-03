:github_url: hide



# AudioEffectReverb

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Adds a reverberation audio effect to an Audio bus.


## Description

Simulates the sound of acoustic environments such as rooms, concert halls, caverns, or an open spaces.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)

- [Third Person Shooter (TPS) Demo ](https://godotengine.org/asset-library/asset/2710)_


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`damping<class_AudioEffectReverb_property_damping>`                     | ``0.5``   |
> +---------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`dry<class_AudioEffectReverb_property_dry>`                             | ``1.0``   |
> +---------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`hipass<class_AudioEffectReverb_property_hipass>`                       | ``0.0``   |
> +---------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`predelay_feedback<class_AudioEffectReverb_property_predelay_feedback>` | ``0.4``   |
> +---------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`predelay_msec<class_AudioEffectReverb_property_predelay_msec>`         | ``150.0`` |
> +---------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`room_size<class_AudioEffectReverb_property_room_size>`                 | ``0.8``   |
> +---------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`spread<class_AudioEffectReverb_property_spread>`                       | ``1.0``   |
> +---------------------------+------------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`wet<class_AudioEffectReverb_property_wet>`                             | ``0.5``   |
> +---------------------------+------------------------------------------------------------------------------+-----------+
>

----


## Property Descriptions



[float<class_float>] **damping** = `0.5` [🔗<class_AudioEffectReverb_property_damping>]


- |void| **set_damping**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_damping**\ (\ )

Defines how reflective the imaginary room's walls are. Value can range from 0 to 1.


----



[float<class_float>] **dry** = `1.0` [🔗<class_AudioEffectReverb_property_dry>]


- |void| **set_dry**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_dry**\ (\ )

Output percent of original sound. At 0, only modified sound is outputted. Value can range from 0 to 1.


----



[float<class_float>] **hipass** = `0.0` [🔗<class_AudioEffectReverb_property_hipass>]


- |void| **set_hpf**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_hpf**\ (\ )

High-pass filter passes signals with a frequency higher than a certain cutoff frequency and attenuates signals with frequencies lower than the cutoff frequency. Value can range from 0 to 1.


----



[float<class_float>] **predelay_feedback** = `0.4` [🔗<class_AudioEffectReverb_property_predelay_feedback>]


- |void| **set_predelay_feedback**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_predelay_feedback**\ (\ )

Output percent of predelay. Value can range from 0 to 1.


----



[float<class_float>] **predelay_msec** = `150.0` [🔗<class_AudioEffectReverb_property_predelay_msec>]


- |void| **set_predelay_msec**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_predelay_msec**\ (\ )

Time between the original signal and the early reflections of the reverb signal, in milliseconds.


----



[float<class_float>] **room_size** = `0.8` [🔗<class_AudioEffectReverb_property_room_size>]


- |void| **set_room_size**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_room_size**\ (\ )

Dimensions of simulated room. Bigger means more echoes. Value can range from 0 to 1.


----



[float<class_float>] **spread** = `1.0` [🔗<class_AudioEffectReverb_property_spread>]


- |void| **set_spread**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_spread**\ (\ )

Widens or narrows the stereo image of the reverb tail. 1 means fully widens. Value can range from 0 to 1.


----



[float<class_float>] **wet** = `0.5` [🔗<class_AudioEffectReverb_property_wet>]


- |void| **set_wet**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_wet**\ (\ )

Output percent of modified sound. At 0, only original sound is outputted. Value can range from 0 to 1.

