:github_url: hide



# ResourceImporterOggVorbis

**Inherits:** [ResourceImporter<class_ResourceImporter>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Imports an Ogg Vorbis audio file for playback.


## Description

Ogg Vorbis is a lossy audio format, with better audio quality compared to [ResourceImporterMP3<class_ResourceImporterMP3>] at a given bitrate.

In most cases, it's recommended to use Ogg Vorbis over MP3. However, if you're using an MP3 sound source with no higher quality source available, then it's recommended to use the MP3 file directly to avoid double lossy compression.

Ogg Vorbis requires more CPU to decode than [ResourceImporterWAV<class_ResourceImporterWAV>]. If you need to play a lot of simultaneous sounds, it's recommended to use WAV for those sounds instead, especially if targeting low-end devices.


## Tutorials

- [../tutorials/assets_pipeline/importing_audio_samples](Importing audio samples .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`     | :ref:`bar_beats<class_ResourceImporterOggVorbis_property_bar_beats>`     | ``4``     |
> +---------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`     | :ref:`beat_count<class_ResourceImporterOggVorbis_property_beat_count>`   | ``0``     |
> +---------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`bpm<class_ResourceImporterOggVorbis_property_bpm>`                 | ``0``     |
> +---------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`   | :ref:`loop<class_ResourceImporterOggVorbis_property_loop>`               | ``false`` |
> +---------------------------+--------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>` | :ref:`loop_offset<class_ResourceImporterOggVorbis_property_loop_offset>` | ``0``     |
> +---------------------------+--------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamOggVorbis<class_AudioStreamOggVorbis>` | :ref:`load_from_buffer<class_ResourceImporterOggVorbis_method_load_from_buffer>`\ (\ stream_data\: :ref:`PackedByteArray<class_PackedByteArray>`\ ) |static| |
> +---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamOggVorbis<class_AudioStreamOggVorbis>` | :ref:`load_from_file<class_ResourceImporterOggVorbis_method_load_from_file>`\ (\ path\: :ref:`String<class_String>`\ ) |static|                              |
> +---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **bar_beats** = `4` [🔗<class_ResourceImporterOggVorbis_property_bar_beats>]

The number of bars within a single beat in the audio track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for [bar_beats<class_ResourceImporterOggVorbis_property_bar_beats>] is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.


----



[int<class_int>] **beat_count** = `0` [🔗<class_ResourceImporterOggVorbis_property_beat_count>]

The beat count of the audio track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for [beat_count<class_ResourceImporterOggVorbis_property_beat_count>] is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.


----



[float<class_float>] **bpm** = `0` [🔗<class_ResourceImporterOggVorbis_property_bpm>]

The beats per minute of the audio track. This should match the BPM measure that was used to compose the track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.

A more convenient editor for [bpm<class_ResourceImporterOggVorbis_property_bpm>] is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.


----



[bool<class_bool>] **loop** = `false` [🔗<class_ResourceImporterOggVorbis_property_loop>]

If enabled, the audio will begin playing at the beginning after playback ends by reaching the end of the audio.

\ **Note:** In [AudioStreamPlayer<class_AudioStreamPlayer>], the [AudioStreamPlayer.finished<class_AudioStreamPlayer_signal_finished>] signal won't be emitted for looping audio when it reaches the end of the audio file, as the audio will keep playing indefinitely.


----



[float<class_float>] **loop_offset** = `0` [🔗<class_ResourceImporterOggVorbis_property_loop_offset>]

Determines where audio will start to loop after playback reaches the end of the audio. This can be used to only loop a part of the audio file, which is useful for some ambient sounds or music. The value is determined in seconds relative to the beginning of the audio. A value of `0.0` will loop the entire audio file.

Only has an effect if [loop<class_ResourceImporterOggVorbis_property_loop>] is `true`.

A more convenient editor for [loop_offset<class_ResourceImporterOggVorbis_property_loop_offset>] is provided in the **Advanced Import Settings** dialog, as it lets you preview your changes without having to reimport the audio.


----


## Method Descriptions



[AudioStreamOggVorbis<class_AudioStreamOggVorbis>] **load_from_buffer**\ (\ stream_data\: [PackedByteArray<class_PackedByteArray>]\ ) |static| [🔗<class_ResourceImporterOggVorbis_method_load_from_buffer>]

**Deprecated:** Use [AudioStreamOggVorbis.load_from_buffer()<class_AudioStreamOggVorbis_method_load_from_buffer>] instead.

Creates a new [AudioStreamOggVorbis<class_AudioStreamOggVorbis>] instance from the given buffer. The buffer must contain Ogg Vorbis data.


----



[AudioStreamOggVorbis<class_AudioStreamOggVorbis>] **load_from_file**\ (\ path\: [String<class_String>]\ ) |static| [🔗<class_ResourceImporterOggVorbis_method_load_from_file>]

**Deprecated:** Use [AudioStreamOggVorbis.load_from_file()<class_AudioStreamOggVorbis_method_load_from_file>] instead.

Creates a new [AudioStreamOggVorbis<class_AudioStreamOggVorbis>] instance from the given file path. The file must be in Ogg Vorbis format.

