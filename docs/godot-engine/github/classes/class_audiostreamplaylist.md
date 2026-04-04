:github_url: hide



# AudioStreamPlaylist

**Inherits:** [AudioStream<class_AudioStream>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

[AudioStream<class_AudioStream>] that includes sub-streams and plays them back like a playlist.


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+----------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`fade_time<class_AudioStreamPlaylist_property_fade_time>`       | ``0.3``   |
> +---------------------------+----------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`loop<class_AudioStreamPlaylist_property_loop>`                 | ``true``  |
> +---------------------------+----------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`shuffle<class_AudioStreamPlaylist_property_shuffle>`           | ``false`` |
> +---------------------------+----------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`     | :ref:`stream_count<class_AudioStreamPlaylist_property_stream_count>` | ``0``     |
> +---------------------------+----------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`             | :ref:`get_bpm<class_AudioStreamPlaylist_method_get_bpm>`\ (\ ) |const|                                                                                                     |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStream<class_AudioStream>` | :ref:`get_list_stream<class_AudioStreamPlaylist_method_get_list_stream>`\ (\ stream_index\: :ref:`int<class_int>`\ ) |const|                                               |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                | :ref:`set_list_stream<class_AudioStreamPlaylist_method_set_list_stream>`\ (\ stream_index\: :ref:`int<class_int>`, audio_stream\: :ref:`AudioStream<class_AudioStream>`\ ) |
> +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Constants



**MAX_STREAMS** = `64` [🔗<class_AudioStreamPlaylist_constant_MAX_STREAMS>]

Maximum amount of streams supported in the playlist.


----


## Property Descriptions



[float<class_float>] **fade_time** = `0.3` [🔗<class_AudioStreamPlaylist_property_fade_time>]


- |void| **set_fade_time**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_fade_time**\ (\ )

Fade time used when a stream ends, when going to the next one. Streams are expected to have an extra bit of audio after the end to help with fading.


----



[bool<class_bool>] **loop** = `true` [🔗<class_AudioStreamPlaylist_property_loop>]


- |void| **set_loop**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **has_loop**\ (\ )

If `true`, the playlist will loop, otherwise the playlist will end when the last stream is finished.


----



[bool<class_bool>] **shuffle** = `false` [🔗<class_AudioStreamPlaylist_property_shuffle>]


- |void| **set_shuffle**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_shuffle**\ (\ )

If `true`, the playlist will shuffle each time playback starts and each time it loops.


----



[int<class_int>] **stream_count** = `0` [🔗<class_AudioStreamPlaylist_property_stream_count>]


- |void| **set_stream_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_stream_count**\ (\ )

Amount of streams in the playlist.


----


## Method Descriptions



[float<class_float>] **get_bpm**\ (\ ) |const| [🔗<class_AudioStreamPlaylist_method_get_bpm>]

Returns the BPM of the playlist, which can vary depending on the clip being played.


----



[AudioStream<class_AudioStream>] **get_list_stream**\ (\ stream_index\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamPlaylist_method_get_list_stream>]

Returns the stream at playback position index.


----



|void| **set_list_stream**\ (\ stream_index\: [int<class_int>], audio_stream\: [AudioStream<class_AudioStream>]\ ) [🔗<class_AudioStreamPlaylist_method_set_list_stream>]

Sets the stream at playback position index.

