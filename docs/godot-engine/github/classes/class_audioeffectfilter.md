:github_url: hide



# AudioEffectFilter

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [AudioEffectBandLimitFilter<class_AudioEffectBandLimitFilter>], [AudioEffectBandPassFilter<class_AudioEffectBandPassFilter>], [AudioEffectHighPassFilter<class_AudioEffectHighPassFilter>], [AudioEffectHighShelfFilter<class_AudioEffectHighShelfFilter>], [AudioEffectLowPassFilter<class_AudioEffectLowPassFilter>], [AudioEffectLowShelfFilter<class_AudioEffectLowShelfFilter>], [AudioEffectNotchFilter<class_AudioEffectNotchFilter>]

Adds a filter to the audio bus.


## Description

Allows frequencies other than the [cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>] to pass.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +--------------------------------------------------+--------------------------------------------------------------+------------+
> | :ref:`float<class_float>`                        | :ref:`cutoff_hz<class_AudioEffectFilter_property_cutoff_hz>` | ``2000.0`` |
> +--------------------------------------------------+--------------------------------------------------------------+------------+
> | :ref:`FilterDB<enum_AudioEffectFilter_FilterDB>` | :ref:`db<class_AudioEffectFilter_property_db>`               | ``0``      |
> +--------------------------------------------------+--------------------------------------------------------------+------------+
> | :ref:`float<class_float>`                        | :ref:`gain<class_AudioEffectFilter_property_gain>`           | ``1.0``    |
> +--------------------------------------------------+--------------------------------------------------------------+------------+
> | :ref:`float<class_float>`                        | :ref:`resonance<class_AudioEffectFilter_property_resonance>` | ``0.5``    |
> +--------------------------------------------------+--------------------------------------------------------------+------------+
>

----


## Enumerations



enum **FilterDB**: [🔗<enum_AudioEffectFilter_FilterDB>]



[FilterDB<enum_AudioEffectFilter_FilterDB>] **FILTER_6DB** = `0`

Cutting off at 6dB per octave.



[FilterDB<enum_AudioEffectFilter_FilterDB>] **FILTER_12DB** = `1`

Cutting off at 12dB per octave.



[FilterDB<enum_AudioEffectFilter_FilterDB>] **FILTER_18DB** = `2`

Cutting off at 18dB per octave.



[FilterDB<enum_AudioEffectFilter_FilterDB>] **FILTER_24DB** = `3`

Cutting off at 24dB per octave.


----


## Property Descriptions



[float<class_float>] **cutoff_hz** = `2000.0` [🔗<class_AudioEffectFilter_property_cutoff_hz>]


- |void| **set_cutoff**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_cutoff**\ (\ )

Threshold frequency for the filter, in Hz.


----



[FilterDB<enum_AudioEffectFilter_FilterDB>] **db** = `0` [🔗<class_AudioEffectFilter_property_db>]


- |void| **set_db**\ (\ value\: [FilterDB<enum_AudioEffectFilter_FilterDB>]\ )
- [FilterDB<enum_AudioEffectFilter_FilterDB>] **get_db**\ (\ )

Steepness of the cutoff curve in dB per octave, also known as the order of the filter. Higher orders have a more aggressive cutoff.


----



[float<class_float>] **gain** = `1.0` [🔗<class_AudioEffectFilter_property_gain>]


- |void| **set_gain**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_gain**\ (\ )

Gain amount of the frequencies after the filter.


----



[float<class_float>] **resonance** = `0.5` [🔗<class_AudioEffectFilter_property_resonance>]


- |void| **set_resonance**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_resonance**\ (\ )

Amount of boost in the frequency range near the cutoff frequency.

