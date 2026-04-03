:github_url: hide



# AudioStreamPlaybackPolyphonic

**Inherits:** [AudioStreamPlayback<class_AudioStreamPlayback>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Playback instance for [AudioStreamPolyphonic<class_AudioStreamPolyphonic>].


## Description

Playback instance for [AudioStreamPolyphonic<class_AudioStreamPolyphonic>]. After setting the `stream` property of [AudioStreamPlayer<class_AudioStreamPlayer>], [AudioStreamPlayer2D<class_AudioStreamPlayer2D>], or [AudioStreamPlayer3D<class_AudioStreamPlayer3D>], the playback instance can be obtained by calling [AudioStreamPlayer.get_stream_playback()<class_AudioStreamPlayer_method_get_stream_playback>], [AudioStreamPlayer2D.get_stream_playback()<class_AudioStreamPlayer2D_method_get_stream_playback>] or [AudioStreamPlayer3D.get_stream_playback()<class_AudioStreamPlayer3D_method_get_stream_playback>] methods.


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`is_stream_playing<class_AudioStreamPlaybackPolyphonic_method_is_stream_playing>`\ (\ stream\: :ref:`int<class_int>`\ ) |const|                                                                                                                                                                                                                                                                   |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`   | :ref:`play_stream<class_AudioStreamPlaybackPolyphonic_method_play_stream>`\ (\ stream\: :ref:`AudioStream<class_AudioStream>`, from_offset\: :ref:`float<class_float>` = 0, volume_db\: :ref:`float<class_float>` = 0, pitch_scale\: :ref:`float<class_float>` = 1.0, playback_type\: :ref:`PlaybackType<enum_AudioServer_PlaybackType>` = 0, bus\: :ref:`StringName<class_StringName>` = &"Master"\ ) |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`set_stream_pitch_scale<class_AudioStreamPlaybackPolyphonic_method_set_stream_pitch_scale>`\ (\ stream\: :ref:`int<class_int>`, pitch_scale\: :ref:`float<class_float>`\ )                                                                                                                                                                                                                        |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`set_stream_volume<class_AudioStreamPlaybackPolyphonic_method_set_stream_volume>`\ (\ stream\: :ref:`int<class_int>`, volume_db\: :ref:`float<class_float>`\ )                                                                                                                                                                                                                                    |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`stop_stream<class_AudioStreamPlaybackPolyphonic_method_stop_stream>`\ (\ stream\: :ref:`int<class_int>`\ )                                                                                                                                                                                                                                                                                       |
> +-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constants



**INVALID_ID** = `-1` [🔗<class_AudioStreamPlaybackPolyphonic_constant_INVALID_ID>]

Returned by [play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>] in case it could not allocate a stream for playback.


----


## Method Descriptions



[bool<class_bool>] **is_stream_playing**\ (\ stream\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamPlaybackPolyphonic_method_is_stream_playing>]

Returns `true` if the stream associated with the given integer ID is still playing. Check [play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>] for information on when this ID becomes invalid.


----



[int<class_int>] **play_stream**\ (\ stream\: [AudioStream<class_AudioStream>], from_offset\: [float<class_float>] = 0, volume_db\: [float<class_float>] = 0, pitch_scale\: [float<class_float>] = 1.0, playback_type\: [PlaybackType<enum_AudioServer_PlaybackType>] = 0, bus\: [StringName<class_StringName>] = &"Master"\ ) [🔗<class_AudioStreamPlaybackPolyphonic_method_play_stream>]

Play an [AudioStream<class_AudioStream>] at a given offset, volume, pitch scale, playback type, and bus. Playback starts immediately.

The return value is a unique integer ID that is associated to this playback stream and which can be used to control it.

This ID becomes invalid when the stream ends (if it does not loop), when the **AudioStreamPlaybackPolyphonic** is stopped, or when [stop_stream()<class_AudioStreamPlaybackPolyphonic_method_stop_stream>] is called.

This function returns [INVALID_ID<class_AudioStreamPlaybackPolyphonic_constant_INVALID_ID>] if the amount of streams currently playing equals [AudioStreamPolyphonic.polyphony<class_AudioStreamPolyphonic_property_polyphony>]. If you need a higher amount of maximum polyphony, raise this value.


----



|void| **set_stream_pitch_scale**\ (\ stream\: [int<class_int>], pitch_scale\: [float<class_float>]\ ) [🔗<class_AudioStreamPlaybackPolyphonic_method_set_stream_pitch_scale>]

Change the stream pitch scale. The `stream` argument is an integer ID returned by [play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>].


----



|void| **set_stream_volume**\ (\ stream\: [int<class_int>], volume_db\: [float<class_float>]\ ) [🔗<class_AudioStreamPlaybackPolyphonic_method_set_stream_volume>]

Change the stream volume (in db). The `stream` argument is an integer ID returned by [play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>].


----



|void| **stop_stream**\ (\ stream\: [int<class_int>]\ ) [🔗<class_AudioStreamPlaybackPolyphonic_method_stop_stream>]

Stop a stream. The `stream` argument is an integer ID returned by [play_stream()<class_AudioStreamPlaybackPolyphonic_method_play_stream>], which becomes invalid after calling this function.

