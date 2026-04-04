:github_url: hide



# AudioStreamMP3

**Inherits:** [AudioStream<class_AudioStream>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

MP3 audio stream driver.


## Description

MP3 audio stream driver. See [data<class_AudioStreamMP3_property_data>] if you want to load an MP3 file at run-time.

\ **Note:** This class can optionally support legacy MP1 and MP2 formats, provided that the engine is compiled with the `minimp3_extra_formats=yes` SCons option. These extra formats are not enabled by default.


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                         | :ref:`bar_beats<class_AudioStreamMP3_property_bar_beats>`     | ``4``                 |
> +-----------------------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                         | :ref:`beat_count<class_AudioStreamMP3_property_beat_count>`   | ``0``                 |
> +-----------------------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                     | :ref:`bpm<class_AudioStreamMP3_property_bpm>`                 | ``0.0``               |
> +-----------------------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`data<class_AudioStreamMP3_property_data>`               | ``PackedByteArray()`` |
> +-----------------------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                       | :ref:`loop<class_AudioStreamMP3_property_loop>`               | ``false``             |
> +-----------------------------------------------+---------------------------------------------------------------+-----------------------+
> | :ref:`float<class_float>`                     | :ref:`loop_offset<class_AudioStreamMP3_property_loop_offset>` | ``0.0``               |
> +-----------------------------------------------+---------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamMP3<class_AudioStreamMP3>` | :ref:`load_from_buffer<class_AudioStreamMP3_method_load_from_buffer>`\ (\ stream_data\: :ref:`PackedByteArray<class_PackedByteArray>`\ ) |static| |
> +---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamMP3<class_AudioStreamMP3>` | :ref:`load_from_file<class_AudioStreamMP3_method_load_from_file>`\ (\ path\: :ref:`String<class_String>`\ ) |static|                              |
> +---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[int<class_int>] **bar_beats** = `4` [🔗<class_AudioStreamMP3_property_bar_beats>]


- |void| **set_bar_beats**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_bar_beats**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[int<class_int>] **beat_count** = `0` [🔗<class_AudioStreamMP3_property_beat_count>]


- |void| **set_beat_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_beat_count**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[float<class_float>] **bpm** = `0.0` [🔗<class_AudioStreamMP3_property_bpm>]


- |void| **set_bpm**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_bpm**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[PackedByteArray<class_PackedByteArray>] **data** = `PackedByteArray()` [🔗<class_AudioStreamMP3_property_data>]


- |void| **set_data**\ (\ value\: [PackedByteArray<class_PackedByteArray>]\ )
- [PackedByteArray<class_PackedByteArray>] **get_data**\ (\ )

Contains the audio data in bytes.

You can load a file without having to import it beforehand using the code snippet below. Keep in mind that this snippet loads the whole file into memory and may not be ideal for huge files (hundreds of megabytes or more).


> **TABS**
>

    func load_mp3(path):
        var file = FileAccess.open(path, FileAccess.READ)
        var sound = AudioStreamMP3.new()
        sound.data = file.get_buffer(file.get_length())
        return sound


    public AudioStreamMP3 LoadMP3(string path)
    {
        using var file = FileAccess.Open(path, FileAccess.ModeFlags.Read);
        var sound = new AudioStreamMP3();
        sound.Data = file.GetBuffer(file.GetLength());
        return sound;
    }



**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray<class_PackedByteArray>] for more details.


----



[bool<class_bool>] **loop** = `false` [🔗<class_AudioStreamMP3_property_loop>]


- |void| **set_loop**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **has_loop**\ (\ )

If `true`, the stream will automatically loop when it reaches the end.


----



[float<class_float>] **loop_offset** = `0.0` [🔗<class_AudioStreamMP3_property_loop_offset>]


- |void| **set_loop_offset**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_loop_offset**\ (\ )

Time in seconds at which the stream starts after being looped.


----


## Method Descriptions



[AudioStreamMP3<class_AudioStreamMP3>] **load_from_buffer**\ (\ stream_data\: [PackedByteArray<class_PackedByteArray>]\ ) |static| [🔗<class_AudioStreamMP3_method_load_from_buffer>]

Creates a new **AudioStreamMP3** instance from the given buffer. The buffer must contain MP3 data.


----



[AudioStreamMP3<class_AudioStreamMP3>] **load_from_file**\ (\ path\: [String<class_String>]\ ) |static| [🔗<class_AudioStreamMP3_method_load_from_file>]

Creates a new **AudioStreamMP3** instance from the given file path. The file must be in MP3 format.

