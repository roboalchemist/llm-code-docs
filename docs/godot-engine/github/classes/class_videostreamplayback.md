:github_url: hide



# VideoStreamPlayback

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Internal class used by [VideoStream<class_VideoStream>] to manage playback state when played from a [VideoStreamPlayer<class_VideoStreamPlayer>].


## Description

This class is intended to be overridden by video decoder extensions with custom implementations of [VideoStream<class_VideoStream>].


## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`             | :ref:`_get_channels<class_VideoStreamPlayback_private_method__get_channels>`\ (\ ) |virtual| |const|                                                                                                                            |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`         | :ref:`_get_length<class_VideoStreamPlayback_private_method__get_length>`\ (\ ) |virtual| |const|                                                                                                                                |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`             | :ref:`_get_mix_rate<class_VideoStreamPlayback_private_method__get_mix_rate>`\ (\ ) |virtual| |const|                                                                                                                            |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`         | :ref:`_get_playback_position<class_VideoStreamPlayback_private_method__get_playback_position>`\ (\ ) |virtual| |const|                                                                                                          |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Texture2D<class_Texture2D>` | :ref:`_get_texture<class_VideoStreamPlayback_private_method__get_texture>`\ (\ ) |virtual| |const|                                                                                                                              |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`_is_paused<class_VideoStreamPlayback_private_method__is_paused>`\ (\ ) |virtual| |const|                                                                                                                                  |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`           | :ref:`_is_playing<class_VideoStreamPlayback_private_method__is_playing>`\ (\ ) |virtual| |const|                                                                                                                                |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`_play<class_VideoStreamPlayback_private_method__play>`\ (\ ) |virtual|                                                                                                                                                    |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`_seek<class_VideoStreamPlayback_private_method__seek>`\ (\ time\: :ref:`float<class_float>`\ ) |virtual|                                                                                                                  |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`_set_audio_track<class_VideoStreamPlayback_private_method__set_audio_track>`\ (\ idx\: :ref:`int<class_int>`\ ) |virtual|                                                                                                 |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`_set_paused<class_VideoStreamPlayback_private_method__set_paused>`\ (\ paused\: :ref:`bool<class_bool>`\ ) |virtual|                                                                                                      |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`_stop<class_VideoStreamPlayback_private_method__stop>`\ (\ ) |virtual|                                                                                                                                                    |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                            | :ref:`_update<class_VideoStreamPlayback_private_method__update>`\ (\ delta\: :ref:`float<class_float>`\ ) |virtual| |required|                                                                                                  |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`             | :ref:`mix_audio<class_VideoStreamPlayback_method_mix_audio>`\ (\ num_frames\: :ref:`int<class_int>`, buffer\: :ref:`PackedFloat32Array<class_PackedFloat32Array>` = PackedFloat32Array(), offset\: :ref:`int<class_int>` = 0\ ) |
> +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **_get_channels**\ (\ ) |virtual| |const| [🔗<class_VideoStreamPlayback_private_method__get_channels>]

Returns the number of audio channels.


----



[float<class_float>] **_get_length**\ (\ ) |virtual| |const| [🔗<class_VideoStreamPlayback_private_method__get_length>]

Returns the video duration in seconds, if known, or 0 if unknown.


----



[int<class_int>] **_get_mix_rate**\ (\ ) |virtual| |const| [🔗<class_VideoStreamPlayback_private_method__get_mix_rate>]

Returns the audio sample rate used for mixing.


----



[float<class_float>] **_get_playback_position**\ (\ ) |virtual| |const| [🔗<class_VideoStreamPlayback_private_method__get_playback_position>]

Return the current playback timestamp. Called in response to the [VideoStreamPlayer.stream_position<class_VideoStreamPlayer_property_stream_position>] getter.


----



[Texture2D<class_Texture2D>] **_get_texture**\ (\ ) |virtual| |const| [🔗<class_VideoStreamPlayback_private_method__get_texture>]

Allocates a [Texture2D<class_Texture2D>] in which decoded video frames will be drawn.


----



[bool<class_bool>] **_is_paused**\ (\ ) |virtual| |const| [🔗<class_VideoStreamPlayback_private_method__is_paused>]

Returns the paused status, as set by [_set_paused()<class_VideoStreamPlayback_private_method__set_paused>].


----



[bool<class_bool>] **_is_playing**\ (\ ) |virtual| |const| [🔗<class_VideoStreamPlayback_private_method__is_playing>]

Returns the playback state, as determined by calls to [_play()<class_VideoStreamPlayback_private_method__play>] and [_stop()<class_VideoStreamPlayback_private_method__stop>].


----



|void| **_play**\ (\ ) |virtual| [🔗<class_VideoStreamPlayback_private_method__play>]

Called in response to [VideoStreamPlayer.autoplay<class_VideoStreamPlayer_property_autoplay>] or [VideoStreamPlayer.play()<class_VideoStreamPlayer_method_play>]. Note that manual playback may also invoke [_stop()<class_VideoStreamPlayback_private_method__stop>] multiple times before this method is called. [_is_playing()<class_VideoStreamPlayback_private_method__is_playing>] should return `true` once playing.


----



|void| **_seek**\ (\ time\: [float<class_float>]\ ) |virtual| [🔗<class_VideoStreamPlayback_private_method__seek>]

Seeks to `time` seconds. Called in response to the [VideoStreamPlayer.stream_position<class_VideoStreamPlayer_property_stream_position>] setter.


----



|void| **_set_audio_track**\ (\ idx\: [int<class_int>]\ ) |virtual| [🔗<class_VideoStreamPlayback_private_method__set_audio_track>]

Select the audio track `idx`. Called when playback starts, and in response to the [VideoStreamPlayer.audio_track<class_VideoStreamPlayer_property_audio_track>] setter.


----



|void| **_set_paused**\ (\ paused\: [bool<class_bool>]\ ) |virtual| [🔗<class_VideoStreamPlayback_private_method__set_paused>]

Set the paused status of video playback. [_is_paused()<class_VideoStreamPlayback_private_method__is_paused>] must return `paused`. Called in response to the [VideoStreamPlayer.paused<class_VideoStreamPlayer_property_paused>] setter.


----



|void| **_stop**\ (\ ) |virtual| [🔗<class_VideoStreamPlayback_private_method__stop>]

Stops playback. May be called multiple times before [_play()<class_VideoStreamPlayback_private_method__play>], or in response to [VideoStreamPlayer.stop()<class_VideoStreamPlayer_method_stop>]. [_is_playing()<class_VideoStreamPlayback_private_method__is_playing>] should return `false` once stopped.


----



|void| **_update**\ (\ delta\: [float<class_float>]\ ) |virtual| |required| [🔗<class_VideoStreamPlayback_private_method__update>]

Ticks video playback for `delta` seconds. Called every frame as long as both [_is_paused()<class_VideoStreamPlayback_private_method__is_paused>] and [_is_playing()<class_VideoStreamPlayback_private_method__is_playing>] return `true`.


----



[int<class_int>] **mix_audio**\ (\ num_frames\: [int<class_int>], buffer\: [PackedFloat32Array<class_PackedFloat32Array>] = PackedFloat32Array(), offset\: [int<class_int>] = 0\ ) [🔗<class_VideoStreamPlayback_method_mix_audio>]

Render `num_frames` audio frames (of [_get_channels()<class_VideoStreamPlayback_private_method__get_channels>] floats each) from `buffer`, starting from index `offset` in the array. Returns the number of audio frames rendered, or -1 on error.

