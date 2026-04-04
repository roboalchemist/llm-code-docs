:github_url: hide



# AudioStreamPolyphonic

**Inherits:** [AudioStream<class_AudioStream>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.


## Description

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.

Playback control is done via the [AudioStreamPlaybackPolyphonic<class_AudioStreamPlaybackPolyphonic>] instance set inside the player, which can be obtained via [AudioStreamPlayer.get_stream_playback()<class_AudioStreamPlayer_method_get_stream_playback>], [AudioStreamPlayer2D.get_stream_playback()<class_AudioStreamPlayer2D_method_get_stream_playback>] or [AudioStreamPlayer3D.get_stream_playback()<class_AudioStreamPlayer3D_method_get_stream_playback>] methods. Obtaining the playback instance is only valid after the `stream` property is set as an **AudioStreamPolyphonic** in those players.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------+------------------------------------------------------------------+--------+
> | :ref:`int<class_int>` | :ref:`polyphony<class_AudioStreamPolyphonic_property_polyphony>` | ``32`` |
> +-----------------------+------------------------------------------------------------------+--------+
>

----


## Property Descriptions



[int<class_int>] **polyphony** = `32` [🔗<class_AudioStreamPolyphonic_property_polyphony>]


- |void| **set_polyphony**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_polyphony**\ (\ )

Maximum amount of simultaneous streams that can be played.

