:github_url: hide



# AudioEffectPhaser

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Adds a phaser audio effect to an audio bus.

Combines the original signal with a copy that is slightly out of phase with the original.


## Description

Combines phase-shifted signals with the original signal. The movement of the phase-shifted signals is controlled using a low-frequency oscillator.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`depth<class_AudioEffectPhaser_property_depth>`               | ``1.0``    |
> +---------------------------+--------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`feedback<class_AudioEffectPhaser_property_feedback>`         | ``0.7``    |
> +---------------------------+--------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`range_max_hz<class_AudioEffectPhaser_property_range_max_hz>` | ``1600.0`` |
> +---------------------------+--------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`range_min_hz<class_AudioEffectPhaser_property_range_min_hz>` | ``440.0``  |
> +---------------------------+--------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`rate_hz<class_AudioEffectPhaser_property_rate_hz>`           | ``0.5``    |
> +---------------------------+--------------------------------------------------------------------+------------+
>

----


## Property Descriptions



[float<class_float>] **depth** = `1.0` [🔗<class_AudioEffectPhaser_property_depth>]


- |void| **set_depth**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_depth**\ (\ )

Determines how high the filter frequencies sweep. Low value will primarily affect bass frequencies. High value can sweep high into the treble. Value can range from `0.1` to `4.0`.


----



[float<class_float>] **feedback** = `0.7` [🔗<class_AudioEffectPhaser_property_feedback>]


- |void| **set_feedback**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_feedback**\ (\ )

Output percent of modified sound. Value can range from 0.1 to 0.9.


----



[float<class_float>] **range_max_hz** = `1600.0` [🔗<class_AudioEffectPhaser_property_range_max_hz>]


- |void| **set_range_max_hz**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_range_max_hz**\ (\ )

Determines the maximum frequency affected by the LFO modulations, in Hz. Value can range from 10 to 10000.


----



[float<class_float>] **range_min_hz** = `440.0` [🔗<class_AudioEffectPhaser_property_range_min_hz>]


- |void| **set_range_min_hz**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_range_min_hz**\ (\ )

Determines the minimum frequency affected by the LFO modulations, in Hz. Value can range from 10 to 10000.


----



[float<class_float>] **rate_hz** = `0.5` [🔗<class_AudioEffectPhaser_property_rate_hz>]


- |void| **set_rate_hz**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_rate_hz**\ (\ )

Adjusts the rate in Hz at which the effect sweeps up and down across the frequency range.

