:github_url: hide



# AudioStreamOggVorbis

**Inherits:** [AudioStream<class_AudioStream>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A class representing an Ogg Vorbis audio stream.


## Description

The AudioStreamOggVorbis class is a specialized [AudioStream<class_AudioStream>] for handling Ogg Vorbis file formats. It offers functionality for loading and playing back Ogg Vorbis files, as well as managing looping and other playback properties. This class is part of the audio stream system, which also supports WAV files through the [AudioStreamWAV<class_AudioStreamWAV>] class.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                             | :ref:`bar_beats<class_AudioStreamOggVorbis_property_bar_beats>`             | ``4``     |
> +---------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`int<class_int>`                             | :ref:`beat_count<class_AudioStreamOggVorbis_property_beat_count>`           | ``0``     |
> +---------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                         | :ref:`bpm<class_AudioStreamOggVorbis_property_bpm>`                         | ``0.0``   |
> +---------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`bool<class_bool>`                           | :ref:`loop<class_AudioStreamOggVorbis_property_loop>`                       | ``false`` |
> +---------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`float<class_float>`                         | :ref:`loop_offset<class_AudioStreamOggVorbis_property_loop_offset>`         | ``0.0``   |
> +---------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`OggPacketSequence<class_OggPacketSequence>` | :ref:`packet_sequence<class_AudioStreamOggVorbis_property_packet_sequence>` |           |
> +---------------------------------------------------+-----------------------------------------------------------------------------+-----------+
> | :ref:`Dictionary<class_Dictionary>`               | :ref:`tags<class_AudioStreamOggVorbis_property_tags>`                       | ``{}``    |
> +---------------------------------------------------+-----------------------------------------------------------------------------+-----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamOggVorbis<class_AudioStreamOggVorbis>` | :ref:`load_from_buffer<class_AudioStreamOggVorbis_method_load_from_buffer>`\ (\ stream_data\: :ref:`PackedByteArray<class_PackedByteArray>`\ ) |static| |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamOggVorbis<class_AudioStreamOggVorbis>` | :ref:`load_from_file<class_AudioStreamOggVorbis_method_load_from_file>`\ (\ path\: :ref:`String<class_String>`\ ) |static|                              |
> +---------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **bar_beats** = `4` [🔗<class_AudioStreamOggVorbis_property_bar_beats>]


- |void| **set_bar_beats**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_bar_beats**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **beat_count** = `0` [🔗<class_AudioStreamOggVorbis_property_beat_count>]


- |void| **set_beat_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_beat_count**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **bpm** = `0.0` [🔗<class_AudioStreamOggVorbis_property_bpm>]


- |void| **set_bpm**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_bpm**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[bool<class_bool>] **loop** = `false` [🔗<class_AudioStreamOggVorbis_property_loop>]


- |void| **set_loop**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **has_loop**\ (\ )

If `true`, the audio will play again from the specified [loop_offset<class_AudioStreamOggVorbis_property_loop_offset>] once it is done playing. Useful for ambient sounds and background music.


----



[float<class_float>] **loop_offset** = `0.0` [🔗<class_AudioStreamOggVorbis_property_loop_offset>]


- |void| **set_loop_offset**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_loop_offset**\ (\ )

Time in seconds at which the stream starts after being looped.


----



[OggPacketSequence<class_OggPacketSequence>] **packet_sequence** [🔗<class_AudioStreamOggVorbis_property_packet_sequence>]


- |void| **set_packet_sequence**\ (\ value\: [OggPacketSequence<class_OggPacketSequence>]\ )
- [OggPacketSequence<class_OggPacketSequence>] **get_packet_sequence**\ (\ )

Contains the raw Ogg data for this stream.


----



[Dictionary<class_Dictionary>] **tags** = `{}` [🔗<class_AudioStreamOggVorbis_property_tags>]


- |void| **set_tags**\ (\ value\: [Dictionary<class_Dictionary>]\ )
- [Dictionary<class_Dictionary>] **get_tags**\ (\ )

Contains user-defined tags if found in the Ogg Vorbis data.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date` (`date` does not have a standard date format).

\ **Note:** No tag is *guaranteed* to be present in every file, so make sure to account for the keys not always existing.


----


## Method Descriptions



[AudioStreamOggVorbis<class_AudioStreamOggVorbis>] **load_from_buffer**\ (\ stream_data\: [PackedByteArray<class_PackedByteArray>]\ ) |static| [🔗<class_AudioStreamOggVorbis_method_load_from_buffer>]

Creates a new **AudioStreamOggVorbis** instance from the given buffer. The buffer must contain Ogg Vorbis data.


----



[AudioStreamOggVorbis<class_AudioStreamOggVorbis>] **load_from_file**\ (\ path\: [String<class_String>]\ ) |static| [🔗<class_AudioStreamOggVorbis_method_load_from_file>]

Creates a new **AudioStreamOggVorbis** instance from the given file path. The file must be in Ogg Vorbis format.

