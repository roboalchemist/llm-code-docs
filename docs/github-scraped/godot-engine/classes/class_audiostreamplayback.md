:github_url: hide



# AudioStreamPlayback

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [AudioStreamPlaybackInteractive<class_AudioStreamPlaybackInteractive>], [AudioStreamPlaybackPlaylist<class_AudioStreamPlaybackPlaylist>], [AudioStreamPlaybackPolyphonic<class_AudioStreamPlaybackPolyphonic>], [AudioStreamPlaybackResampled<class_AudioStreamPlaybackResampled>], [AudioStreamPlaybackSynchronized<class_AudioStreamPlaybackSynchronized>]

Meta class for playing back audio.


## Description

Can play, loop, pause a scroll through audio. See [AudioStream<class_AudioStream>] and [AudioStreamOggVorbis<class_AudioStreamOggVorbis>] for usage.


## Tutorials

- [Audio Generator Demo ](https://godotengine.org/asset-library/asset/2759)_


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`_get_loop_count<class_AudioStreamPlayback_private_method__get_loop_count>`\ (\ ) |virtual| |const|                                                                                |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`                         | :ref:`_get_parameter<class_AudioStreamPlayback_private_method__get_parameter>`\ (\ name\: :ref:`StringName<class_StringName>`\ ) |virtual| |const|                                      |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`_get_playback_position<class_AudioStreamPlayback_private_method__get_playback_position>`\ (\ ) |virtual| |required| |const|                                                       |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`_is_playing<class_AudioStreamPlayback_private_method__is_playing>`\ (\ ) |virtual| |required| |const|                                                                             |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`_mix<class_AudioStreamPlayback_private_method__mix>`\ (\ buffer\: ``AudioFrame*``, rate_scale\: :ref:`float<class_float>`, frames\: :ref:`int<class_int>`\ ) |virtual| |required| |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`_seek<class_AudioStreamPlayback_private_method__seek>`\ (\ position\: :ref:`float<class_float>`\ ) |virtual|                                                                      |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`_set_parameter<class_AudioStreamPlayback_private_method__set_parameter>`\ (\ name\: :ref:`StringName<class_StringName>`, value\: :ref:`Variant<class_Variant>`\ ) |virtual|       |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`_start<class_AudioStreamPlayback_private_method__start>`\ (\ from_pos\: :ref:`float<class_float>`\ ) |virtual| |required|                                                         |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`_stop<class_AudioStreamPlayback_private_method__stop>`\ (\ ) |virtual| |required|                                                                                                 |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`_tag_used_streams<class_AudioStreamPlayback_private_method__tag_used_streams>`\ (\ ) |virtual|                                                                                    |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`get_loop_count<class_AudioStreamPlayback_method_get_loop_count>`\ (\ ) |const|                                                                                                    |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_playback_position<class_AudioStreamPlayback_method_get_playback_position>`\ (\ ) |const|                                                                                      |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioSamplePlayback<class_AudioSamplePlayback>` | :ref:`get_sample_playback<class_AudioStreamPlayback_method_get_sample_playback>`\ (\ ) |const|                                                                                          |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`is_playing<class_AudioStreamPlayback_method_is_playing>`\ (\ ) |const|                                                                                                            |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>`   | :ref:`mix_audio<class_AudioStreamPlayback_method_mix_audio>`\ (\ rate_scale\: :ref:`float<class_float>`, frames\: :ref:`int<class_int>`\ )                                              |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`seek<class_AudioStreamPlayback_method_seek>`\ (\ time\: :ref:`float<class_float>` = 0.0\ )                                                                                        |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_sample_playback<class_AudioStreamPlayback_method_set_sample_playback>`\ (\ playback_sample\: :ref:`AudioSamplePlayback<class_AudioSamplePlayback>`\ )                         |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`start<class_AudioStreamPlayback_method_start>`\ (\ from_pos\: :ref:`float<class_float>` = 0.0\ )                                                                                  |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`stop<class_AudioStreamPlayback_method_stop>`\ (\ )                                                                                                                                |
> +-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[int<class_int>] **_get_loop_count**\ (\ ) |virtual| |const| [🔗<class_AudioStreamPlayback_private_method__get_loop_count>]

Overridable method. Should return how many times this audio stream has looped. Most built-in playbacks always return `0`.


----



[Variant<class_Variant>] **_get_parameter**\ (\ name\: [StringName<class_StringName>]\ ) |virtual| |const| [🔗<class_AudioStreamPlayback_private_method__get_parameter>]

Return the current value of a playback parameter by name (see [AudioStream._get_parameter_list()<class_AudioStream_private_method__get_parameter_list>]).


----



[float<class_float>] **_get_playback_position**\ (\ ) |virtual| |required| |const| [🔗<class_AudioStreamPlayback_private_method__get_playback_position>]

Overridable method. Should return the current progress along the audio stream, in seconds.


----



[bool<class_bool>] **_is_playing**\ (\ ) |virtual| |required| |const| [🔗<class_AudioStreamPlayback_private_method__is_playing>]

Overridable method. Should return `true` if this playback is active and playing its audio stream.


----



[int<class_int>] **_mix**\ (\ buffer\: `AudioFrame*`, rate_scale\: [float<class_float>], frames\: [int<class_int>]\ ) |virtual| |required| [🔗<class_AudioStreamPlayback_private_method__mix>]

Override this method to customize how the audio stream is mixed. This method is called even if the playback is not active.

\ **Note:** It is not useful to override this method in GDScript or C#. Only GDExtension can take advantage of it.


----



|void| **_seek**\ (\ position\: [float<class_float>]\ ) |virtual| [🔗<class_AudioStreamPlayback_private_method__seek>]

Override this method to customize what happens when seeking this audio stream at the given `position`, such as by calling [AudioStreamPlayer.seek()<class_AudioStreamPlayer_method_seek>].


----



|void| **_set_parameter**\ (\ name\: [StringName<class_StringName>], value\: [Variant<class_Variant>]\ ) |virtual| [🔗<class_AudioStreamPlayback_private_method__set_parameter>]

Set the current value of a playback parameter by name (see [AudioStream._get_parameter_list()<class_AudioStream_private_method__get_parameter_list>]).


----



|void| **_start**\ (\ from_pos\: [float<class_float>]\ ) |virtual| |required| [🔗<class_AudioStreamPlayback_private_method__start>]

Override this method to customize what happens when the playback starts at the given position, such as by calling [AudioStreamPlayer.play()<class_AudioStreamPlayer_method_play>].


----



|void| **_stop**\ (\ ) |virtual| |required| [🔗<class_AudioStreamPlayback_private_method__stop>]

Override this method to customize what happens when the playback is stopped, such as by calling [AudioStreamPlayer.stop()<class_AudioStreamPlayer_method_stop>].


----



|void| **_tag_used_streams**\ (\ ) |virtual| [🔗<class_AudioStreamPlayback_private_method__tag_used_streams>]

Overridable method. Called whenever the audio stream is mixed if the playback is active and [AudioServer.set_enable_tagging_used_audio_streams()<class_AudioServer_method_set_enable_tagging_used_audio_streams>] has been set to `true`. Editor plugins may use this method to "tag" the current position along the audio stream and display it in a preview.


----



[int<class_int>] **get_loop_count**\ (\ ) |const| [🔗<class_AudioStreamPlayback_method_get_loop_count>]

Returns the number of times the stream has looped.


----



[float<class_float>] **get_playback_position**\ (\ ) |const| [🔗<class_AudioStreamPlayback_method_get_playback_position>]

Returns the current position in the stream, in seconds.


----



[AudioSamplePlayback<class_AudioSamplePlayback>] **get_sample_playback**\ (\ ) |const| [🔗<class_AudioStreamPlayback_method_get_sample_playback>]

**Experimental:** This method may be changed or removed in future versions.

Returns the [AudioSamplePlayback<class_AudioSamplePlayback>] associated with this **AudioStreamPlayback** for playing back the audio sample of this stream.


----



[bool<class_bool>] **is_playing**\ (\ ) |const| [🔗<class_AudioStreamPlayback_method_is_playing>]

Returns `true` if the stream is playing.


----



[PackedVector2Array<class_PackedVector2Array>] **mix_audio**\ (\ rate_scale\: [float<class_float>], frames\: [int<class_int>]\ ) [🔗<class_AudioStreamPlayback_method_mix_audio>]

Mixes up to `frames` of audio from the stream from the current position, at a rate of `rate_scale`, advancing the stream.

Returns a [PackedVector2Array<class_PackedVector2Array>] where each element holds the left and right channel volume levels of each frame.

\ **Note:** Can return fewer frames than requested, make sure to use the size of the return value.


----



|void| **seek**\ (\ time\: [float<class_float>] = 0.0\ ) [🔗<class_AudioStreamPlayback_method_seek>]

Seeks the stream at the given `time`, in seconds.


----



|void| **set_sample_playback**\ (\ playback_sample\: [AudioSamplePlayback<class_AudioSamplePlayback>]\ ) [🔗<class_AudioStreamPlayback_method_set_sample_playback>]

**Experimental:** This method may be changed or removed in future versions.

Associates [AudioSamplePlayback<class_AudioSamplePlayback>] to this **AudioStreamPlayback** for playing back the audio sample of this stream.


----



|void| **start**\ (\ from_pos\: [float<class_float>] = 0.0\ ) [🔗<class_AudioStreamPlayback_method_start>]

Starts the stream from the given `from_pos`, in seconds.


----



|void| **stop**\ (\ ) [🔗<class_AudioStreamPlayback_method_stop>]

Stops the stream.

