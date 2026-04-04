:github_url: hide



# AudioEffectChorus

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Adds a chorus audio effect.


## Description

Adds a chorus audio effect. The effect applies a filter with voices to duplicate the audio source and manipulate it through the filter.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`dry<class_AudioEffectChorus_property_dry>`                             | ``1.0``    |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/1/cutoff_hz<class_AudioEffectChorus_property_voice/1/cutoff_hz>` | ``8000.0`` |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/1/delay_ms<class_AudioEffectChorus_property_voice/1/delay_ms>`   | ``15.0``   |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/1/depth_ms<class_AudioEffectChorus_property_voice/1/depth_ms>`   | ``2.0``    |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/1/level_db<class_AudioEffectChorus_property_voice/1/level_db>`   | ``0.0``    |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/1/pan<class_AudioEffectChorus_property_voice/1/pan>`             | ``-0.5``   |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/1/rate_hz<class_AudioEffectChorus_property_voice/1/rate_hz>`     | ``0.8``    |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/2/cutoff_hz<class_AudioEffectChorus_property_voice/2/cutoff_hz>` | ``8000.0`` |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/2/delay_ms<class_AudioEffectChorus_property_voice/2/delay_ms>`   | ``20.0``   |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/2/depth_ms<class_AudioEffectChorus_property_voice/2/depth_ms>`   | ``3.0``    |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/2/level_db<class_AudioEffectChorus_property_voice/2/level_db>`   | ``0.0``    |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/2/pan<class_AudioEffectChorus_property_voice/2/pan>`             | ``0.5``    |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/2/rate_hz<class_AudioEffectChorus_property_voice/2/rate_hz>`     | ``1.2``    |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/3/cutoff_hz<class_AudioEffectChorus_property_voice/3/cutoff_hz>` |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/3/delay_ms<class_AudioEffectChorus_property_voice/3/delay_ms>`   |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/3/depth_ms<class_AudioEffectChorus_property_voice/3/depth_ms>`   |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/3/level_db<class_AudioEffectChorus_property_voice/3/level_db>`   |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/3/pan<class_AudioEffectChorus_property_voice/3/pan>`             |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/3/rate_hz<class_AudioEffectChorus_property_voice/3/rate_hz>`     |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/4/cutoff_hz<class_AudioEffectChorus_property_voice/4/cutoff_hz>` |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/4/delay_ms<class_AudioEffectChorus_property_voice/4/delay_ms>`   |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/4/depth_ms<class_AudioEffectChorus_property_voice/4/depth_ms>`   |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/4/level_db<class_AudioEffectChorus_property_voice/4/level_db>`   |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/4/pan<class_AudioEffectChorus_property_voice/4/pan>`             |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`voice/4/rate_hz<class_AudioEffectChorus_property_voice/4/rate_hz>`     |            |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`int<class_int>`     | :ref:`voice_count<class_AudioEffectChorus_property_voice_count>`             | ``2``      |
> +---------------------------+------------------------------------------------------------------------------+------------+
> | :ref:`float<class_float>` | :ref:`wet<class_AudioEffectChorus_property_wet>`                             | ``0.5``    |
> +---------------------------+------------------------------------------------------------------------------+------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_voice_cutoff_hz<class_AudioEffectChorus_method_get_voice_cutoff_hz>`\ (\ voice_idx\: :ref:`int<class_int>`\ ) |const|                                |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_voice_delay_ms<class_AudioEffectChorus_method_get_voice_delay_ms>`\ (\ voice_idx\: :ref:`int<class_int>`\ ) |const|                                  |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_voice_depth_ms<class_AudioEffectChorus_method_get_voice_depth_ms>`\ (\ voice_idx\: :ref:`int<class_int>`\ ) |const|                                  |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_voice_level_db<class_AudioEffectChorus_method_get_voice_level_db>`\ (\ voice_idx\: :ref:`int<class_int>`\ ) |const|                                  |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_voice_pan<class_AudioEffectChorus_method_get_voice_pan>`\ (\ voice_idx\: :ref:`int<class_int>`\ ) |const|                                            |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>` | :ref:`get_voice_rate_hz<class_AudioEffectChorus_method_get_voice_rate_hz>`\ (\ voice_idx\: :ref:`int<class_int>`\ ) |const|                                    |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_voice_cutoff_hz<class_AudioEffectChorus_method_set_voice_cutoff_hz>`\ (\ voice_idx\: :ref:`int<class_int>`, cutoff_hz\: :ref:`float<class_float>`\ ) |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_voice_delay_ms<class_AudioEffectChorus_method_set_voice_delay_ms>`\ (\ voice_idx\: :ref:`int<class_int>`, delay_ms\: :ref:`float<class_float>`\ )    |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_voice_depth_ms<class_AudioEffectChorus_method_set_voice_depth_ms>`\ (\ voice_idx\: :ref:`int<class_int>`, depth_ms\: :ref:`float<class_float>`\ )    |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_voice_level_db<class_AudioEffectChorus_method_set_voice_level_db>`\ (\ voice_idx\: :ref:`int<class_int>`, level_db\: :ref:`float<class_float>`\ )    |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_voice_pan<class_AudioEffectChorus_method_set_voice_pan>`\ (\ voice_idx\: :ref:`int<class_int>`, pan\: :ref:`float<class_float>`\ )                   |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                    | :ref:`set_voice_rate_hz<class_AudioEffectChorus_method_set_voice_rate_hz>`\ (\ voice_idx\: :ref:`int<class_int>`, rate_hz\: :ref:`float<class_float>`\ )       |
> +---------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **dry** = `1.0` [🔗<class_AudioEffectChorus_property_dry>]


- |void| **set_dry**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_dry**\ (\ )

The effect's raw signal.


----



[float<class_float>] **voice/1/cutoff_hz** = `8000.0` [🔗<class_AudioEffectChorus_property_voice/1/cutoff_hz>]


- |void| **set_voice_cutoff_hz**\ (\ voice_idx\: [int<class_int>], cutoff_hz\: [float<class_float>]\ )
- [float<class_float>] **get_voice_cutoff_hz**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's cutoff frequency.


----



[float<class_float>] **voice/1/delay_ms** = `15.0` [🔗<class_AudioEffectChorus_property_voice/1/delay_ms>]


- |void| **set_voice_delay_ms**\ (\ voice_idx\: [int<class_int>], delay_ms\: [float<class_float>]\ )
- [float<class_float>] **get_voice_delay_ms**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's signal delay.


----



[float<class_float>] **voice/1/depth_ms** = `2.0` [🔗<class_AudioEffectChorus_property_voice/1/depth_ms>]


- |void| **set_voice_depth_ms**\ (\ voice_idx\: [int<class_int>], depth_ms\: [float<class_float>]\ )
- [float<class_float>] **get_voice_depth_ms**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice filter's depth.


----



[float<class_float>] **voice/1/level_db** = `0.0` [🔗<class_AudioEffectChorus_property_voice/1/level_db>]


- |void| **set_voice_level_db**\ (\ voice_idx\: [int<class_int>], level_db\: [float<class_float>]\ )
- [float<class_float>] **get_voice_level_db**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's volume.


----



[float<class_float>] **voice/1/pan** = `-0.5` [🔗<class_AudioEffectChorus_property_voice/1/pan>]


- |void| **set_voice_pan**\ (\ voice_idx\: [int<class_int>], pan\: [float<class_float>]\ )
- [float<class_float>] **get_voice_pan**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's pan level.


----



[float<class_float>] **voice/1/rate_hz** = `0.8` [🔗<class_AudioEffectChorus_property_voice/1/rate_hz>]


- |void| **set_voice_rate_hz**\ (\ voice_idx\: [int<class_int>], rate_hz\: [float<class_float>]\ )
- [float<class_float>] **get_voice_rate_hz**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's filter rate.


----



[float<class_float>] **voice/2/cutoff_hz** = `8000.0` [🔗<class_AudioEffectChorus_property_voice/2/cutoff_hz>]


- |void| **set_voice_cutoff_hz**\ (\ voice_idx\: [int<class_int>], cutoff_hz\: [float<class_float>]\ )
- [float<class_float>] **get_voice_cutoff_hz**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's cutoff frequency.


----



[float<class_float>] **voice/2/delay_ms** = `20.0` [🔗<class_AudioEffectChorus_property_voice/2/delay_ms>]


- |void| **set_voice_delay_ms**\ (\ voice_idx\: [int<class_int>], delay_ms\: [float<class_float>]\ )
- [float<class_float>] **get_voice_delay_ms**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's signal delay.


----



[float<class_float>] **voice/2/depth_ms** = `3.0` [🔗<class_AudioEffectChorus_property_voice/2/depth_ms>]


- |void| **set_voice_depth_ms**\ (\ voice_idx\: [int<class_int>], depth_ms\: [float<class_float>]\ )
- [float<class_float>] **get_voice_depth_ms**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice filter's depth.


----



[float<class_float>] **voice/2/level_db** = `0.0` [🔗<class_AudioEffectChorus_property_voice/2/level_db>]


- |void| **set_voice_level_db**\ (\ voice_idx\: [int<class_int>], level_db\: [float<class_float>]\ )
- [float<class_float>] **get_voice_level_db**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's volume.


----



[float<class_float>] **voice/2/pan** = `0.5` [🔗<class_AudioEffectChorus_property_voice/2/pan>]


- |void| **set_voice_pan**\ (\ voice_idx\: [int<class_int>], pan\: [float<class_float>]\ )
- [float<class_float>] **get_voice_pan**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's pan level.


----



[float<class_float>] **voice/2/rate_hz** = `1.2` [🔗<class_AudioEffectChorus_property_voice/2/rate_hz>]


- |void| **set_voice_rate_hz**\ (\ voice_idx\: [int<class_int>], rate_hz\: [float<class_float>]\ )
- [float<class_float>] **get_voice_rate_hz**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's filter rate.


----



[float<class_float>] **voice/3/cutoff_hz** [🔗<class_AudioEffectChorus_property_voice/3/cutoff_hz>]


- |void| **set_voice_cutoff_hz**\ (\ voice_idx\: [int<class_int>], cutoff_hz\: [float<class_float>]\ )
- [float<class_float>] **get_voice_cutoff_hz**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's cutoff frequency.


----



[float<class_float>] **voice/3/delay_ms** [🔗<class_AudioEffectChorus_property_voice/3/delay_ms>]


- |void| **set_voice_delay_ms**\ (\ voice_idx\: [int<class_int>], delay_ms\: [float<class_float>]\ )
- [float<class_float>] **get_voice_delay_ms**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's signal delay.


----



[float<class_float>] **voice/3/depth_ms** [🔗<class_AudioEffectChorus_property_voice/3/depth_ms>]


- |void| **set_voice_depth_ms**\ (\ voice_idx\: [int<class_int>], depth_ms\: [float<class_float>]\ )
- [float<class_float>] **get_voice_depth_ms**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice filter's depth.


----



[float<class_float>] **voice/3/level_db** [🔗<class_AudioEffectChorus_property_voice/3/level_db>]


- |void| **set_voice_level_db**\ (\ voice_idx\: [int<class_int>], level_db\: [float<class_float>]\ )
- [float<class_float>] **get_voice_level_db**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's volume.


----



[float<class_float>] **voice/3/pan** [🔗<class_AudioEffectChorus_property_voice/3/pan>]


- |void| **set_voice_pan**\ (\ voice_idx\: [int<class_int>], pan\: [float<class_float>]\ )
- [float<class_float>] **get_voice_pan**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's pan level.


----



[float<class_float>] **voice/3/rate_hz** [🔗<class_AudioEffectChorus_property_voice/3/rate_hz>]


- |void| **set_voice_rate_hz**\ (\ voice_idx\: [int<class_int>], rate_hz\: [float<class_float>]\ )
- [float<class_float>] **get_voice_rate_hz**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's filter rate.


----



[float<class_float>] **voice/4/cutoff_hz** [🔗<class_AudioEffectChorus_property_voice/4/cutoff_hz>]


- |void| **set_voice_cutoff_hz**\ (\ voice_idx\: [int<class_int>], cutoff_hz\: [float<class_float>]\ )
- [float<class_float>] **get_voice_cutoff_hz**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's cutoff frequency.


----



[float<class_float>] **voice/4/delay_ms** [🔗<class_AudioEffectChorus_property_voice/4/delay_ms>]


- |void| **set_voice_delay_ms**\ (\ voice_idx\: [int<class_int>], delay_ms\: [float<class_float>]\ )
- [float<class_float>] **get_voice_delay_ms**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's signal delay.


----



[float<class_float>] **voice/4/depth_ms** [🔗<class_AudioEffectChorus_property_voice/4/depth_ms>]


- |void| **set_voice_depth_ms**\ (\ voice_idx\: [int<class_int>], depth_ms\: [float<class_float>]\ )
- [float<class_float>] **get_voice_depth_ms**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice filter's depth.


----



[float<class_float>] **voice/4/level_db** [🔗<class_AudioEffectChorus_property_voice/4/level_db>]


- |void| **set_voice_level_db**\ (\ voice_idx\: [int<class_int>], level_db\: [float<class_float>]\ )
- [float<class_float>] **get_voice_level_db**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's volume.


----



[float<class_float>] **voice/4/pan** [🔗<class_AudioEffectChorus_property_voice/4/pan>]


- |void| **set_voice_pan**\ (\ voice_idx\: [int<class_int>], pan\: [float<class_float>]\ )
- [float<class_float>] **get_voice_pan**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's pan level.


----



[float<class_float>] **voice/4/rate_hz** [🔗<class_AudioEffectChorus_property_voice/4/rate_hz>]


- |void| **set_voice_rate_hz**\ (\ voice_idx\: [int<class_int>], rate_hz\: [float<class_float>]\ )
- [float<class_float>] **get_voice_rate_hz**\ (\ voice_idx\: [int<class_int>]\ ) |const|

The voice's filter rate.


----



[int<class_int>] **voice_count** = `2` [🔗<class_AudioEffectChorus_property_voice_count>]


- |void| **set_voice_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_voice_count**\ (\ )

The number of voices in the effect.


----



[float<class_float>] **wet** = `0.5` [🔗<class_AudioEffectChorus_property_wet>]


- |void| **set_wet**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_wet**\ (\ )

The effect's processed signal.


----


## Method Descriptions



[float<class_float>] **get_voice_cutoff_hz**\ (\ voice_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioEffectChorus_method_get_voice_cutoff_hz>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **get_voice_delay_ms**\ (\ voice_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioEffectChorus_method_get_voice_delay_ms>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **get_voice_depth_ms**\ (\ voice_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioEffectChorus_method_get_voice_depth_ms>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **get_voice_level_db**\ (\ voice_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioEffectChorus_method_get_voice_level_db>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **get_voice_pan**\ (\ voice_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioEffectChorus_method_get_voice_pan>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **get_voice_rate_hz**\ (\ voice_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioEffectChorus_method_get_voice_rate_hz>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_voice_cutoff_hz**\ (\ voice_idx\: [int<class_int>], cutoff_hz\: [float<class_float>]\ ) [🔗<class_AudioEffectChorus_method_set_voice_cutoff_hz>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_voice_delay_ms**\ (\ voice_idx\: [int<class_int>], delay_ms\: [float<class_float>]\ ) [🔗<class_AudioEffectChorus_method_set_voice_delay_ms>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_voice_depth_ms**\ (\ voice_idx\: [int<class_int>], depth_ms\: [float<class_float>]\ ) [🔗<class_AudioEffectChorus_method_set_voice_depth_ms>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_voice_level_db**\ (\ voice_idx\: [int<class_int>], level_db\: [float<class_float>]\ ) [🔗<class_AudioEffectChorus_method_set_voice_level_db>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_voice_pan**\ (\ voice_idx\: [int<class_int>], pan\: [float<class_float>]\ ) [🔗<class_AudioEffectChorus_method_set_voice_pan>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **set_voice_rate_hz**\ (\ voice_idx\: [int<class_int>], rate_hz\: [float<class_float>]\ ) [🔗<class_AudioEffectChorus_method_set_voice_rate_hz>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

