:github_url: hide



# AudioEffectDelay

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Adds a delay audio effect to an audio bus. Plays input signal back after a period of time.

Two tap delay and feedback options.


## Description

Plays input signal back after a period of time. The delayed signal may be played back multiple times to create the sound of a repeating, decaying echo. Delay effects range from a subtle echo effect to a pronounced blending of previous sounds with new sounds.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>` | :ref:`dry<class_AudioEffectDelay_property_dry>`                             | ``1.0``     |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`bool<class_bool>`   | :ref:`feedback_active<class_AudioEffectDelay_property_feedback_active>`     | ``false``   |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>` | :ref:`feedback_delay_ms<class_AudioEffectDelay_property_feedback_delay_ms>` | ``340.0``   |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>` | :ref:`feedback_level_db<class_AudioEffectDelay_property_feedback_level_db>` | ``-6.0``    |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>` | :ref:`feedback_lowpass<class_AudioEffectDelay_property_feedback_lowpass>`   | ``16000.0`` |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`bool<class_bool>`   | :ref:`tap1_active<class_AudioEffectDelay_property_tap1_active>`             | ``true``    |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>` | :ref:`tap1_delay_ms<class_AudioEffectDelay_property_tap1_delay_ms>`         | ``250.0``   |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>` | :ref:`tap1_level_db<class_AudioEffectDelay_property_tap1_level_db>`         | ``-6.0``    |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>` | :ref:`tap1_pan<class_AudioEffectDelay_property_tap1_pan>`                   | ``0.2``     |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`bool<class_bool>`   | :ref:`tap2_active<class_AudioEffectDelay_property_tap2_active>`             | ``true``    |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>` | :ref:`tap2_delay_ms<class_AudioEffectDelay_property_tap2_delay_ms>`         | ``500.0``   |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>` | :ref:`tap2_level_db<class_AudioEffectDelay_property_tap2_level_db>`         | ``-12.0``   |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
> | :ref:`float<class_float>` | :ref:`tap2_pan<class_AudioEffectDelay_property_tap2_pan>`                   | ``-0.4``    |
> +---------------------------+-----------------------------------------------------------------------------+-------------+
>

----


## Property Descriptions



[float<class_float>] **dry** = `1.0` [🔗<class_AudioEffectDelay_property_dry>]


- |void| **set_dry**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_dry**\ (\ )

Output percent of original sound. At 0, only delayed sounds are output. Value can range from 0 to 1.


----



[bool<class_bool>] **feedback_active** = `false` [🔗<class_AudioEffectDelay_property_feedback_active>]


- |void| **set_feedback_active**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_feedback_active**\ (\ )

If `true`, feedback is enabled.


----



[float<class_float>] **feedback_delay_ms** = `340.0` [🔗<class_AudioEffectDelay_property_feedback_delay_ms>]


- |void| **set_feedback_delay_ms**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_feedback_delay_ms**\ (\ )

Feedback delay time in milliseconds.


----



[float<class_float>] **feedback_level_db** = `-6.0` [🔗<class_AudioEffectDelay_property_feedback_level_db>]


- |void| **set_feedback_level_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_feedback_level_db**\ (\ )

Sound level for feedback.


----



[float<class_float>] **feedback_lowpass** = `16000.0` [🔗<class_AudioEffectDelay_property_feedback_lowpass>]


- |void| **set_feedback_lowpass**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_feedback_lowpass**\ (\ )

Low-pass filter for feedback, in Hz. Frequencies below this value are filtered out of the source signal.


----



[bool<class_bool>] **tap1_active** = `true` [🔗<class_AudioEffectDelay_property_tap1_active>]


- |void| **set_tap1_active**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_tap1_active**\ (\ )

If `true`, the first tap will be enabled.


----



[float<class_float>] **tap1_delay_ms** = `250.0` [🔗<class_AudioEffectDelay_property_tap1_delay_ms>]


- |void| **set_tap1_delay_ms**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_tap1_delay_ms**\ (\ )

First tap delay time in milliseconds.


----



[float<class_float>] **tap1_level_db** = `-6.0` [🔗<class_AudioEffectDelay_property_tap1_level_db>]


- |void| **set_tap1_level_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_tap1_level_db**\ (\ )

Sound level for the first tap.


----



[float<class_float>] **tap1_pan** = `0.2` [🔗<class_AudioEffectDelay_property_tap1_pan>]


- |void| **set_tap1_pan**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_tap1_pan**\ (\ )

Pan position for the first tap. Value can range from -1 (fully left) to 1 (fully right).


----



[bool<class_bool>] **tap2_active** = `true` [🔗<class_AudioEffectDelay_property_tap2_active>]


- |void| **set_tap2_active**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_tap2_active**\ (\ )

If `true`, the second tap will be enabled.


----



[float<class_float>] **tap2_delay_ms** = `500.0` [🔗<class_AudioEffectDelay_property_tap2_delay_ms>]


- |void| **set_tap2_delay_ms**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_tap2_delay_ms**\ (\ )

Second tap delay time in milliseconds.


----



[float<class_float>] **tap2_level_db** = `-12.0` [🔗<class_AudioEffectDelay_property_tap2_level_db>]


- |void| **set_tap2_level_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_tap2_level_db**\ (\ )

Sound level for the second tap.


----



[float<class_float>] **tap2_pan** = `-0.4` [🔗<class_AudioEffectDelay_property_tap2_pan>]


- |void| **set_tap2_pan**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_tap2_pan**\ (\ )

Pan position for the second tap. Value can range from -1 (fully left) to 1 (fully right).

