:github_url: hide



# AudioStreamInteractive

**Inherits:** [AudioStream<class_AudioStream>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Audio stream that can playback music interactively, combining clips and a transition table.


## Description

This is an audio stream that can playback music interactively, combining clips and a transition table. Clips must be added first, and then the transition rules via the [add_transition()<class_AudioStreamInteractive_method_add_transition>]. Additionally, this stream exports a property parameter to control the playback via [AudioStreamPlayer<class_AudioStreamPlayer>], [AudioStreamPlayer2D<class_AudioStreamPlayer2D>], or [AudioStreamPlayer3D<class_AudioStreamPlayer3D>].

The way this is used is by filling a number of clips, then configuring the transition table. From there, clips are selected for playback and the music will smoothly go from the current to the new one while using the corresponding transition rule defined in the transition table.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+-------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`clip_count<class_AudioStreamInteractive_property_clip_count>`     | ``0`` |
> +-----------------------+-------------------------------------------------------------------------+-------+
> | :ref:`int<class_int>` | :ref:`initial_clip<class_AudioStreamInteractive_property_initial_clip>` | ``0`` |
> +-----------------------+-------------------------------------------------------------------------+-------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                    | :ref:`add_transition<class_AudioStreamInteractive_method_add_transition>`\ (\ from_clip\: :ref:`int<class_int>`, to_clip\: :ref:`int<class_int>`, from_time\: :ref:`TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>`, to_time\: :ref:`TransitionToTime<enum_AudioStreamInteractive_TransitionToTime>`, fade_mode\: :ref:`FadeMode<enum_AudioStreamInteractive_FadeMode>`, fade_beats\: :ref:`float<class_float>`, use_filler_clip\: :ref:`bool<class_bool>` = false, filler_clip\: :ref:`int<class_int>` = -1, hold_previous\: :ref:`bool<class_bool>` = false\ ) |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                    | :ref:`erase_transition<class_AudioStreamInteractive_method_erase_transition>`\ (\ from_clip\: :ref:`int<class_int>`, to_clip\: :ref:`int<class_int>`\ )                                                                                                                                                                                                                                                                                                                                                                                                                              |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>`       | :ref:`get_clip_auto_advance<class_AudioStreamInteractive_method_get_clip_auto_advance>`\ (\ clip_index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                     | :ref:`get_clip_auto_advance_next_clip<class_AudioStreamInteractive_method_get_clip_auto_advance_next_clip>`\ (\ clip_index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                        |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                                       | :ref:`get_clip_name<class_AudioStreamInteractive_method_get_clip_name>`\ (\ clip_index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStream<class_AudioStream>`                                     | :ref:`get_clip_stream<class_AudioStreamInteractive_method_get_clip_stream>`\ (\ clip_index\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                                 | :ref:`get_transition_fade_beats<class_AudioStreamInteractive_method_get_transition_fade_beats>`\ (\ from_clip\: :ref:`int<class_int>`, to_clip\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                    |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`FadeMode<enum_AudioStreamInteractive_FadeMode>`                     | :ref:`get_transition_fade_mode<class_AudioStreamInteractive_method_get_transition_fade_mode>`\ (\ from_clip\: :ref:`int<class_int>`, to_clip\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                      |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                                     | :ref:`get_transition_filler_clip<class_AudioStreamInteractive_method_get_transition_filler_clip>`\ (\ from_clip\: :ref:`int<class_int>`, to_clip\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                  |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>` | :ref:`get_transition_from_time<class_AudioStreamInteractive_method_get_transition_from_time>`\ (\ from_clip\: :ref:`int<class_int>`, to_clip\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                      |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedInt32Array<class_PackedInt32Array>`                           | :ref:`get_transition_list<class_AudioStreamInteractive_method_get_transition_list>`\ (\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`TransitionToTime<enum_AudioStreamInteractive_TransitionToTime>`     | :ref:`get_transition_to_time<class_AudioStreamInteractive_method_get_transition_to_time>`\ (\ from_clip\: :ref:`int<class_int>`, to_clip\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                          |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                   | :ref:`has_transition<class_AudioStreamInteractive_method_has_transition>`\ (\ from_clip\: :ref:`int<class_int>`, to_clip\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                                                          |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                   | :ref:`is_transition_holding_previous<class_AudioStreamInteractive_method_is_transition_holding_previous>`\ (\ from_clip\: :ref:`int<class_int>`, to_clip\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                          |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                                   | :ref:`is_transition_using_filler_clip<class_AudioStreamInteractive_method_is_transition_using_filler_clip>`\ (\ from_clip\: :ref:`int<class_int>`, to_clip\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                                                                                                                                        |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                    | :ref:`set_clip_auto_advance<class_AudioStreamInteractive_method_set_clip_auto_advance>`\ (\ clip_index\: :ref:`int<class_int>`, mode\: :ref:`AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>`\ )                                                                                                                                                                                                                                                                                                                                                                        |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                    | :ref:`set_clip_auto_advance_next_clip<class_AudioStreamInteractive_method_set_clip_auto_advance_next_clip>`\ (\ clip_index\: :ref:`int<class_int>`, auto_advance_next_clip\: :ref:`int<class_int>`\ )                                                                                                                                                                                                                                                                                                                                                                                |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                    | :ref:`set_clip_name<class_AudioStreamInteractive_method_set_clip_name>`\ (\ clip_index\: :ref:`int<class_int>`, name\: :ref:`StringName<class_StringName>`\ )                                                                                                                                                                                                                                                                                                                                                                                                                        |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                                    | :ref:`set_clip_stream<class_AudioStreamInteractive_method_set_clip_stream>`\ (\ clip_index\: :ref:`int<class_int>`, stream\: :ref:`AudioStream<class_AudioStream>`\ )                                                                                                                                                                                                                                                                                                                                                                                                                |
> +---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **TransitionFromTime**: [🔗<enum_AudioStreamInteractive_TransitionFromTime>]



[TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>] **TRANSITION_FROM_TIME_IMMEDIATE** = `0`

Start transition as soon as possible, don't wait for any specific time position.



[TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>] **TRANSITION_FROM_TIME_NEXT_BEAT** = `1`

Transition when the clip playback position reaches the next beat.



[TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>] **TRANSITION_FROM_TIME_NEXT_BAR** = `2`

Transition when the clip playback position reaches the next bar.



[TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>] **TRANSITION_FROM_TIME_END** = `3`

Transition when the current clip finished playing.


----



enum **TransitionToTime**: [🔗<enum_AudioStreamInteractive_TransitionToTime>]



[TransitionToTime<enum_AudioStreamInteractive_TransitionToTime>] **TRANSITION_TO_TIME_SAME_POSITION** = `0`

Transition to the same position in the destination clip. This is useful when both clips have exactly the same length and the music should fade between them.



[TransitionToTime<enum_AudioStreamInteractive_TransitionToTime>] **TRANSITION_TO_TIME_START** = `1`

Transition to the start of the destination clip.


----



enum **FadeMode**: [🔗<enum_AudioStreamInteractive_FadeMode>]



[FadeMode<enum_AudioStreamInteractive_FadeMode>] **FADE_DISABLED** = `0`

Do not use fade for the transition. This is useful when transitioning from a clip-end to clip-beginning, and each clip has their begin/end.



[FadeMode<enum_AudioStreamInteractive_FadeMode>] **FADE_IN** = `1`

Use a fade-in in the next clip, let the current clip finish.



[FadeMode<enum_AudioStreamInteractive_FadeMode>] **FADE_OUT** = `2`

Use a fade-out in the current clip, the next clip will start by itself.



[FadeMode<enum_AudioStreamInteractive_FadeMode>] **FADE_CROSS** = `3`

Use a cross-fade between clips.



[FadeMode<enum_AudioStreamInteractive_FadeMode>] **FADE_AUTOMATIC** = `4`

Use automatic fade logic depending on the transition from/to. It is recommended to use this by default.


----



enum **AutoAdvanceMode**: [🔗<enum_AudioStreamInteractive_AutoAdvanceMode>]



[AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>] **AUTO_ADVANCE_DISABLED** = `0`

Disable auto-advance (default).



[AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>] **AUTO_ADVANCE_ENABLED** = `1`

Enable auto-advance, a clip must be specified.



[AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>] **AUTO_ADVANCE_RETURN_TO_HOLD** = `2`

Enable auto-advance, but instead of specifying a clip, the playback will return to hold (see [add_transition()<class_AudioStreamInteractive_method_add_transition>]).


----


## Constants



**CLIP_ANY** = `-1` [🔗<class_AudioStreamInteractive_constant_CLIP_ANY>]

This constant describes that any clip is valid for a specific transition as either source or destination.


----


## Property Descriptions



[int<class_int>] **clip_count** = `0` [🔗<class_AudioStreamInteractive_property_clip_count>]


- |void| **set_clip_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_clip_count**\ (\ )

Amount of clips contained in this interactive player.


----



[int<class_int>] **initial_clip** = `0` [🔗<class_AudioStreamInteractive_property_initial_clip>]


- |void| **set_initial_clip**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_initial_clip**\ (\ )

Index of the initial clip, which will be played first when this stream is played.


----


## Method Descriptions



|void| **add_transition**\ (\ from_clip\: [int<class_int>], to_clip\: [int<class_int>], from_time\: [TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>], to_time\: [TransitionToTime<enum_AudioStreamInteractive_TransitionToTime>], fade_mode\: [FadeMode<enum_AudioStreamInteractive_FadeMode>], fade_beats\: [float<class_float>], use_filler_clip\: [bool<class_bool>] = false, filler_clip\: [int<class_int>] = -1, hold_previous\: [bool<class_bool>] = false\ ) [🔗<class_AudioStreamInteractive_method_add_transition>]

Add a transition between two clips. Provide the indices of the source and destination clips, or use the [CLIP_ANY<class_AudioStreamInteractive_constant_CLIP_ANY>] constant to indicate that transition happens to/from any clip to this one.

\* `from_time` indicates the moment in the current clip the transition will begin after triggered.

\* `to_time` indicates the time in the next clip that the playback will start from.

\* `fade_mode` indicates how the fade will happen between clips. If unsure, just use [FADE_AUTOMATIC<class_AudioStreamInteractive_constant_FADE_AUTOMATIC>] which uses the most common type of fade for each situation.

\* `fade_beats` indicates how many beats the fade will take. Using decimals is allowed.

\* `use_filler_clip` indicates that there will be a filler clip used between the source and destination clips.

\* `filler_clip` the index of the filler clip.

\* If `hold_previous` is used, then this clip will be remembered. This can be used together with [AUTO_ADVANCE_RETURN_TO_HOLD<class_AudioStreamInteractive_constant_AUTO_ADVANCE_RETURN_TO_HOLD>] to return to this clip after another is done playing.


----



|void| **erase_transition**\ (\ from_clip\: [int<class_int>], to_clip\: [int<class_int>]\ ) [🔗<class_AudioStreamInteractive_method_erase_transition>]

Erase a transition by providing `from_clip` and `to_clip` clip indices. [CLIP_ANY<class_AudioStreamInteractive_constant_CLIP_ANY>] can be used for either argument or both.


----



[AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>] **get_clip_auto_advance**\ (\ clip_index\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_get_clip_auto_advance>]

Return whether a clip has auto-advance enabled. See [set_clip_auto_advance()<class_AudioStreamInteractive_method_set_clip_auto_advance>].


----



[int<class_int>] **get_clip_auto_advance_next_clip**\ (\ clip_index\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_get_clip_auto_advance_next_clip>]

Return the clip towards which the clip referenced by `clip_index` will auto-advance to.


----



[StringName<class_StringName>] **get_clip_name**\ (\ clip_index\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_get_clip_name>]

Return the name of a clip.


----



[AudioStream<class_AudioStream>] **get_clip_stream**\ (\ clip_index\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_get_clip_stream>]

Return the [AudioStream<class_AudioStream>] associated with a clip.


----



[float<class_float>] **get_transition_fade_beats**\ (\ from_clip\: [int<class_int>], to_clip\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_get_transition_fade_beats>]

Return the time (in beats) for a transition (see [add_transition()<class_AudioStreamInteractive_method_add_transition>]).


----



[FadeMode<enum_AudioStreamInteractive_FadeMode>] **get_transition_fade_mode**\ (\ from_clip\: [int<class_int>], to_clip\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_get_transition_fade_mode>]

Return the mode for a transition (see [add_transition()<class_AudioStreamInteractive_method_add_transition>]).


----



[int<class_int>] **get_transition_filler_clip**\ (\ from_clip\: [int<class_int>], to_clip\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_get_transition_filler_clip>]

Return the filler clip for a transition (see [add_transition()<class_AudioStreamInteractive_method_add_transition>]).


----



[TransitionFromTime<enum_AudioStreamInteractive_TransitionFromTime>] **get_transition_from_time**\ (\ from_clip\: [int<class_int>], to_clip\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_get_transition_from_time>]

Return the source time position for a transition (see [add_transition()<class_AudioStreamInteractive_method_add_transition>]).


----



[PackedInt32Array<class_PackedInt32Array>] **get_transition_list**\ (\ ) |const| [🔗<class_AudioStreamInteractive_method_get_transition_list>]

Return the list of transitions (from, to interleaved).


----



[TransitionToTime<enum_AudioStreamInteractive_TransitionToTime>] **get_transition_to_time**\ (\ from_clip\: [int<class_int>], to_clip\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_get_transition_to_time>]

Return the destination time position for a transition (see [add_transition()<class_AudioStreamInteractive_method_add_transition>]).


----



[bool<class_bool>] **has_transition**\ (\ from_clip\: [int<class_int>], to_clip\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_has_transition>]

Returns `true` if a given transition exists (was added via [add_transition()<class_AudioStreamInteractive_method_add_transition>]).


----



[bool<class_bool>] **is_transition_holding_previous**\ (\ from_clip\: [int<class_int>], to_clip\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_is_transition_holding_previous>]

Return whether a transition uses the *hold previous* functionality (see [add_transition()<class_AudioStreamInteractive_method_add_transition>]).


----



[bool<class_bool>] **is_transition_using_filler_clip**\ (\ from_clip\: [int<class_int>], to_clip\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamInteractive_method_is_transition_using_filler_clip>]

Return whether a transition uses the *filler clip* functionality (see [add_transition()<class_AudioStreamInteractive_method_add_transition>]).


----



|void| **set_clip_auto_advance**\ (\ clip_index\: [int<class_int>], mode\: [AutoAdvanceMode<enum_AudioStreamInteractive_AutoAdvanceMode>]\ ) [🔗<class_AudioStreamInteractive_method_set_clip_auto_advance>]

Set whether a clip will auto-advance by changing the auto-advance mode.


----



|void| **set_clip_auto_advance_next_clip**\ (\ clip_index\: [int<class_int>], auto_advance_next_clip\: [int<class_int>]\ ) [🔗<class_AudioStreamInteractive_method_set_clip_auto_advance_next_clip>]

Set the index of the next clip towards which this clip will auto advance to when finished. If the clip being played loops, then auto-advance will be ignored.


----



|void| **set_clip_name**\ (\ clip_index\: [int<class_int>], name\: [StringName<class_StringName>]\ ) [🔗<class_AudioStreamInteractive_method_set_clip_name>]

Set the name of the current clip (for easier identification).


----



|void| **set_clip_stream**\ (\ clip_index\: [int<class_int>], stream\: [AudioStream<class_AudioStream>]\ ) [🔗<class_AudioStreamInteractive_method_set_clip_stream>]

Set the [AudioStream<class_AudioStream>] associated with the current clip.

