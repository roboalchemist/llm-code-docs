:github_url: hide

> **META**
	:keywords: sound, music, song



# AudioStreamPlayer

**Inherits:** [Node<class_Node>] **<** [Object<class_Object>]

A node for audio playback.


## Description

The **AudioStreamPlayer** node plays an audio stream non-positionally. It is ideal for user interfaces, menus, or background music.

To use this node, [stream<class_AudioStreamPlayer_property_stream>] needs to be set to a valid [AudioStream<class_AudioStream>] resource. Playing more than one sound at the same time is also supported, see [max_polyphony<class_AudioStreamPlayer_property_max_polyphony>].

If you need to play audio at a specific position, use [AudioStreamPlayer2D<class_AudioStreamPlayer2D>] or [AudioStreamPlayer3D<class_AudioStreamPlayer3D>] instead.


## Tutorials

- [../tutorials/audio/audio_streams](Audio streams .md)

- [2D Dodge The Creeps Demo ](https://godotengine.org/asset-library/asset/2712)_

- [Audio Device Changer Demo ](https://godotengine.org/asset-library/asset/2758)_

- [Audio Generator Demo ](https://godotengine.org/asset-library/asset/2759)_

- [Audio Microphone Record Demo ](https://godotengine.org/asset-library/asset/2760)_

- [Audio Spectrum Visualizer Demo ](https://godotengine.org/asset-library/asset/2762)_


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`bool<class_bool>`                            | :ref:`autoplay<class_AudioStreamPlayer_property_autoplay>`           | ``false``     |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`StringName<class_StringName>`                | :ref:`bus<class_AudioStreamPlayer_property_bus>`                     | ``&"Master"`` |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`int<class_int>`                              | :ref:`max_polyphony<class_AudioStreamPlayer_property_max_polyphony>` | ``1``         |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`MixTarget<enum_AudioStreamPlayer_MixTarget>` | :ref:`mix_target<class_AudioStreamPlayer_property_mix_target>`       | ``0``         |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`                          | :ref:`pitch_scale<class_AudioStreamPlayer_property_pitch_scale>`     | ``1.0``       |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`PlaybackType<enum_AudioServer_PlaybackType>` | :ref:`playback_type<class_AudioStreamPlayer_property_playback_type>` | ``0``         |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`bool<class_bool>`                            | :ref:`playing<class_AudioStreamPlayer_property_playing>`             | ``false``     |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`AudioStream<class_AudioStream>`              | :ref:`stream<class_AudioStreamPlayer_property_stream>`               |               |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`bool<class_bool>`                            | :ref:`stream_paused<class_AudioStreamPlayer_property_stream_paused>` | ``false``     |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`                          | :ref:`volume_db<class_AudioStreamPlayer_property_volume_db>`         | ``0.0``       |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`                          | :ref:`volume_linear<class_AudioStreamPlayer_property_volume_linear>` |               |
> +----------------------------------------------------+----------------------------------------------------------------------+---------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_playback_position<class_AudioStreamPlayer_method_get_playback_position>`\ (\ )                |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamPlayback<class_AudioStreamPlayback>` | :ref:`get_stream_playback<class_AudioStreamPlayer_method_get_stream_playback>`\ (\ )                    |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`has_stream_playback<class_AudioStreamPlayer_method_has_stream_playback>`\ (\ )                    |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`play<class_AudioStreamPlayer_method_play>`\ (\ from_position\: :ref:`float<class_float>` = 0.0\ ) |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`seek<class_AudioStreamPlayer_method_seek>`\ (\ to_position\: :ref:`float<class_float>`\ )         |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`stop<class_AudioStreamPlayer_method_stop>`\ (\ )                                                  |
> +-------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
>

----


## Signals



**finished**\ (\ ) [🔗<class_AudioStreamPlayer_signal_finished>]

Emitted when a sound finishes playing without interruptions. This signal is *not* emitted when calling [stop()<class_AudioStreamPlayer_method_stop>], or when exiting the tree while sounds are playing.


----


## Enumerations



enum **MixTarget**: [🔗<enum_AudioStreamPlayer_MixTarget>]



[MixTarget<enum_AudioStreamPlayer_MixTarget>] **MIX_TARGET_STEREO** = `0`

The audio will be played only on the first channel. This is the default.



[MixTarget<enum_AudioStreamPlayer_MixTarget>] **MIX_TARGET_SURROUND** = `1`

The audio will be played on all surround channels.



[MixTarget<enum_AudioStreamPlayer_MixTarget>] **MIX_TARGET_CENTER** = `2`

The audio will be played on the second channel, which is usually the center.


----


## Property Descriptions



[bool<class_bool>] **autoplay** = `false` [🔗<class_AudioStreamPlayer_property_autoplay>]


- |void| **set_autoplay**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_autoplay_enabled**\ (\ )

If `true`, this node calls [play()<class_AudioStreamPlayer_method_play>] when entering the tree.


----



[StringName<class_StringName>] **bus** = `&"Master"` [🔗<class_AudioStreamPlayer_property_bus>]


- |void| **set_bus**\ (\ value\: [StringName<class_StringName>]\ )
- [StringName<class_StringName>] **get_bus**\ (\ )

The target bus name. All sounds from this node will be playing on this bus.

\ **Note:** At runtime, if no bus with the given name exists, all sounds will fall back on `"Master"`. See also [AudioServer.get_bus_name()<class_AudioServer_method_get_bus_name>].


----



[int<class_int>] **max_polyphony** = `1` [🔗<class_AudioStreamPlayer_property_max_polyphony>]


- |void| **set_max_polyphony**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_max_polyphony**\ (\ )

The maximum number of sounds this node can play at the same time. Calling [play()<class_AudioStreamPlayer_method_play>] after this value is reached will cut off the oldest sounds.


----



[MixTarget<enum_AudioStreamPlayer_MixTarget>] **mix_target** = `0` [🔗<class_AudioStreamPlayer_property_mix_target>]


- |void| **set_mix_target**\ (\ value\: [MixTarget<enum_AudioStreamPlayer_MixTarget>]\ )
- [MixTarget<enum_AudioStreamPlayer_MixTarget>] **get_mix_target**\ (\ )

The mix target channels. Has no effect when two speakers or less are detected (see [SpeakerMode<enum_AudioServer_SpeakerMode>]).


----



[float<class_float>] **pitch_scale** = `1.0` [🔗<class_AudioStreamPlayer_property_pitch_scale>]


- |void| **set_pitch_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_pitch_scale**\ (\ )

The audio's pitch and tempo, as a multiplier of the [stream<class_AudioStreamPlayer_property_stream>]'s sample rate. A value of `2.0` doubles the audio's pitch, while a value of `0.5` halves the pitch.


----



[PlaybackType<enum_AudioServer_PlaybackType>] **playback_type** = `0` [🔗<class_AudioStreamPlayer_property_playback_type>]


- |void| **set_playback_type**\ (\ value\: [PlaybackType<enum_AudioServer_PlaybackType>]\ )
- [PlaybackType<enum_AudioServer_PlaybackType>] **get_playback_type**\ (\ )

**Experimental:** This property may be changed or removed in future versions.

The playback type of the stream player. If set other than to the default value, it will force that playback type.


----



[bool<class_bool>] **playing** = `false` [🔗<class_AudioStreamPlayer_property_playing>]


- |void| **set_playing**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_playing**\ (\ )

If `true`, this node is playing sounds. Setting this property has the same effect as [play()<class_AudioStreamPlayer_method_play>] and [stop()<class_AudioStreamPlayer_method_stop>].


----



[AudioStream<class_AudioStream>] **stream** [🔗<class_AudioStreamPlayer_property_stream>]


- |void| **set_stream**\ (\ value\: [AudioStream<class_AudioStream>]\ )
- [AudioStream<class_AudioStream>] **get_stream**\ (\ )

The [AudioStream<class_AudioStream>] resource to be played. Setting this property stops all currently playing sounds. If left empty, the **AudioStreamPlayer** does not work.


----



[bool<class_bool>] **stream_paused** = `false` [🔗<class_AudioStreamPlayer_property_stream_paused>]


- |void| **set_stream_paused**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **get_stream_paused**\ (\ )

If `true`, the sounds are paused. Setting [stream_paused<class_AudioStreamPlayer_property_stream_paused>] to `false` resumes all sounds.

\ **Note:** This property is automatically changed when exiting or entering the tree, or this node is paused (see [Node.process_mode<class_Node_property_process_mode>]).


----



[float<class_float>] **volume_db** = `0.0` [🔗<class_AudioStreamPlayer_property_volume_db>]


- |void| **set_volume_db**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_volume_db**\ (\ )

Volume of sound, in decibels. This is an offset of the [stream<class_AudioStreamPlayer_property_stream>]'s volume.

\ **Note:** To convert between decibel and linear energy (like most volume sliders do), use [volume_linear<class_AudioStreamPlayer_property_volume_linear>], or [@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>] and [@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>].


----



[float<class_float>] **volume_linear** [🔗<class_AudioStreamPlayer_property_volume_linear>]


- |void| **set_volume_linear**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_volume_linear**\ (\ )

Volume of sound, as a linear value.

\ **Note:** This member modifies [volume_db<class_AudioStreamPlayer_property_volume_db>] for convenience. The returned value is equivalent to the result of [@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>] on [volume_db<class_AudioStreamPlayer_property_volume_db>]. Setting this member is equivalent to setting [volume_db<class_AudioStreamPlayer_property_volume_db>] to the result of [@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>] on a value.


----


## Method Descriptions



[float<class_float>] **get_playback_position**\ (\ ) [🔗<class_AudioStreamPlayer_method_get_playback_position>]

Returns the position in the [AudioStream<class_AudioStream>] of the latest sound, in seconds. Returns `0.0` if no sounds are playing.

\ **Note:** The position is not always accurate, as the [AudioServer<class_AudioServer>] does not mix audio every processed frame. To get more accurate results, add [AudioServer.get_time_since_last_mix()<class_AudioServer_method_get_time_since_last_mix>] to the returned position.

\ **Note:** This method always returns `0.0` if the [stream<class_AudioStreamPlayer_property_stream>] is an [AudioStreamInteractive<class_AudioStreamInteractive>], since it can have multiple clips playing at once.


----



[AudioStreamPlayback<class_AudioStreamPlayback>] **get_stream_playback**\ (\ ) [🔗<class_AudioStreamPlayer_method_get_stream_playback>]

Returns the latest [AudioStreamPlayback<class_AudioStreamPlayback>] of this node, usually the most recently created by [play()<class_AudioStreamPlayer_method_play>]. If no sounds are playing, this method fails and returns an empty playback.


----



[bool<class_bool>] **has_stream_playback**\ (\ ) [🔗<class_AudioStreamPlayer_method_has_stream_playback>]

Returns `true` if any sound is active, even if [stream_paused<class_AudioStreamPlayer_property_stream_paused>] is set to `true`. See also [playing<class_AudioStreamPlayer_property_playing>] and [get_stream_playback()<class_AudioStreamPlayer_method_get_stream_playback>].


----



|void| **play**\ (\ from_position\: [float<class_float>] = 0.0\ ) [🔗<class_AudioStreamPlayer_method_play>]

Plays a sound from the beginning, or the given `from_position` in seconds.


----



|void| **seek**\ (\ to_position\: [float<class_float>]\ ) [🔗<class_AudioStreamPlayer_method_seek>]

Restarts all sounds to be played from the given `to_position`, in seconds. Does nothing if no sounds are playing.


----



|void| **stop**\ (\ ) [🔗<class_AudioStreamPlayer_method_stop>]

Stops all sounds from this node.

