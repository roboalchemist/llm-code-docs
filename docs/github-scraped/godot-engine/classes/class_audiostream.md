:github_url: hide



# AudioStream

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [AudioStreamGenerator<class_AudioStreamGenerator>], [AudioStreamInteractive<class_AudioStreamInteractive>], [AudioStreamMicrophone<class_AudioStreamMicrophone>], [AudioStreamMP3<class_AudioStreamMP3>], [AudioStreamOggVorbis<class_AudioStreamOggVorbis>], [AudioStreamPlaylist<class_AudioStreamPlaylist>], [AudioStreamPolyphonic<class_AudioStreamPolyphonic>], [AudioStreamRandomizer<class_AudioStreamRandomizer>], [AudioStreamSynchronized<class_AudioStreamSynchronized>], [AudioStreamWAV<class_AudioStreamWAV>]

Base class for audio streams.


## Description

Base class for audio streams. Audio streams are used for sound effects and music playback, and support WAV (via [AudioStreamWAV<class_AudioStreamWAV>]) and Ogg (via [AudioStreamOggVorbis<class_AudioStreamOggVorbis>]) file formats.


## Tutorials

- [../tutorials/audio/audio_streams](Audio streams .md)

- [Audio Generator Demo ](https://godotengine.org/asset-library/asset/2759)_

- [Audio Microphone Record Demo ](https://godotengine.org/asset-library/asset/2760)_

- [Audio Spectrum Visualizer Demo ](https://godotengine.org/asset-library/asset/2762)_


## Methods

> **TABLE**
> :widths: auto
>
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_get_bar_beats<class_AudioStream_private_method__get_bar_beats>`\ (\ ) |virtual| |const|                          |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                            | :ref:`_get_beat_count<class_AudioStream_private_method__get_beat_count>`\ (\ ) |virtual| |const|                        |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                        | :ref:`_get_bpm<class_AudioStream_private_method__get_bpm>`\ (\ ) |virtual| |const|                                      |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                        | :ref:`_get_length<class_AudioStream_private_method__get_length>`\ (\ ) |virtual| |const|                                |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Array<class_Array>`\[:ref:`Dictionary<class_Dictionary>`\] | :ref:`_get_parameter_list<class_AudioStream_private_method__get_parameter_list>`\ (\ ) |virtual| |const|                |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                                      | :ref:`_get_stream_name<class_AudioStream_private_method__get_stream_name>`\ (\ ) |virtual| |const|                      |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Dictionary<class_Dictionary>`                              | :ref:`_get_tags<class_AudioStream_private_method__get_tags>`\ (\ ) |virtual| |const|                                    |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_has_loop<class_AudioStream_private_method__has_loop>`\ (\ ) |virtual| |const|                                    |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamPlayback<class_AudioStreamPlayback>`            | :ref:`_instantiate_playback<class_AudioStream_private_method__instantiate_playback>`\ (\ ) |virtual| |required| |const| |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`_is_monophonic<class_AudioStream_private_method__is_monophonic>`\ (\ ) |virtual| |const|                          |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`can_be_sampled<class_AudioStream_method_can_be_sampled>`\ (\ ) |const|                                            |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioSample<class_AudioSample>`                            | :ref:`generate_sample<class_AudioStream_method_generate_sample>`\ (\ ) |const|                                          |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                                        | :ref:`get_length<class_AudioStream_method_get_length>`\ (\ ) |const|                                                    |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamPlayback<class_AudioStreamPlayback>`            | :ref:`instantiate_playback<class_AudioStream_method_instantiate_playback>`\ (\ )                                        |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_meta_stream<class_AudioStream_method_is_meta_stream>`\ (\ ) |const|                                            |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                                          | :ref:`is_monophonic<class_AudioStream_method_is_monophonic>`\ (\ ) |const|                                              |
> +------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**parameter_list_changed**\ (\ ) [🔗<class_AudioStream_signal_parameter_list_changed>]

Signal to be emitted to notify when the parameter list changed.


----


## Method Descriptions



[int<class_int>] **_get_bar_beats**\ (\ ) |virtual| |const| [🔗<class_AudioStream_private_method__get_bar_beats>]

Override this method to return the bar beats of this stream.


----



[int<class_int>] **_get_beat_count**\ (\ ) |virtual| |const| [🔗<class_AudioStream_private_method__get_beat_count>]

Overridable method. Should return the total number of beats of this audio stream. Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate ([AudioStreamWAV.mix_rate<class_AudioStreamWAV_property_mix_rate>], for example).


----



[float<class_float>] **_get_bpm**\ (\ ) |virtual| |const| [🔗<class_AudioStream_private_method__get_bpm>]

Overridable method. Should return the tempo of this audio stream, in beats per minute (BPM). Used by the engine to determine the position of every beat.

Ideally, the returned value should be based off the stream's sample rate ([AudioStreamWAV.mix_rate<class_AudioStreamWAV_property_mix_rate>], for example).


----



[float<class_float>] **_get_length**\ (\ ) |virtual| |const| [🔗<class_AudioStream_private_method__get_length>]

Override this method to customize the returned value of [get_length()<class_AudioStream_method_get_length>]. Should return the length of this audio stream, in seconds.


----



[Array<class_Array>]\[[Dictionary<class_Dictionary>]\] **_get_parameter_list**\ (\ ) |virtual| |const| [🔗<class_AudioStream_private_method__get_parameter_list>]

Return the controllable parameters of this stream. This array contains dictionaries with a property info description format (see [Object.get_property_list()<class_Object_method_get_property_list>]). Additionally, the default value for this parameter must be added tho each dictionary in "default_value" field.


----



[String<class_String>] **_get_stream_name**\ (\ ) |virtual| |const| [🔗<class_AudioStream_private_method__get_stream_name>]

Override this method to customize the name assigned to this audio stream. Unused by the engine.


----



[Dictionary<class_Dictionary>] **_get_tags**\ (\ ) |virtual| |const| [🔗<class_AudioStream_private_method__get_tags>]

Override this method to customize the tags for this audio stream. Should return a [Dictionary<class_Dictionary>] of strings with the tag as the key and its content as the value.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date`.


----



[bool<class_bool>] **_has_loop**\ (\ ) |virtual| |const| [🔗<class_AudioStream_private_method__has_loop>]

Override this method to return `true` if this stream has a loop.


----



[AudioStreamPlayback<class_AudioStreamPlayback>] **_instantiate_playback**\ (\ ) |virtual| |required| |const| [🔗<class_AudioStream_private_method__instantiate_playback>]

Override this method to customize the returned value of [instantiate_playback()<class_AudioStream_method_instantiate_playback>]. Should return a new [AudioStreamPlayback<class_AudioStreamPlayback>] created when the stream is played (such as by an [AudioStreamPlayer<class_AudioStreamPlayer>]).


----



[bool<class_bool>] **_is_monophonic**\ (\ ) |virtual| |const| [🔗<class_AudioStream_private_method__is_monophonic>]

Override this method to customize the returned value of [is_monophonic()<class_AudioStream_method_is_monophonic>]. Should return `true` if this audio stream only supports one channel.


----



[bool<class_bool>] **can_be_sampled**\ (\ ) |const| [🔗<class_AudioStream_method_can_be_sampled>]

**Experimental:** This method may be changed or removed in future versions.

Returns if the current **AudioStream** can be used as a sample. Only static streams can be sampled.


----



[AudioSample<class_AudioSample>] **generate_sample**\ (\ ) |const| [🔗<class_AudioStream_method_generate_sample>]

**Experimental:** This method may be changed or removed in future versions.

Generates an [AudioSample<class_AudioSample>] based on the current stream.


----



[float<class_float>] **get_length**\ (\ ) |const| [🔗<class_AudioStream_method_get_length>]

Returns the length of the audio stream in seconds. If this stream is an [AudioStreamRandomizer<class_AudioStreamRandomizer>], returns the length of the last played stream. If this stream has an indefinite length (such as for [AudioStreamGenerator<class_AudioStreamGenerator>] and [AudioStreamMicrophone<class_AudioStreamMicrophone>]), returns `0.0`.


----



[AudioStreamPlayback<class_AudioStreamPlayback>] **instantiate_playback**\ (\ ) [🔗<class_AudioStream_method_instantiate_playback>]

Returns a newly created [AudioStreamPlayback<class_AudioStreamPlayback>] intended to play this audio stream. Useful for when you want to extend [_instantiate_playback()<class_AudioStream_private_method__instantiate_playback>] but call [instantiate_playback()<class_AudioStream_method_instantiate_playback>] from an internally held AudioStream subresource. An example of this can be found in the source code for `AudioStreamRandomPitch::instantiate_playback`.


----



[bool<class_bool>] **is_meta_stream**\ (\ ) |const| [🔗<class_AudioStream_method_is_meta_stream>]

Returns `true` if the stream is a collection of other streams, `false` otherwise.


----



[bool<class_bool>] **is_monophonic**\ (\ ) |const| [🔗<class_AudioStream_method_is_monophonic>]

Returns `true` if this audio stream only supports one channel (*monophony*), or `false` if the audio stream supports two or more channels (*polyphony*).

