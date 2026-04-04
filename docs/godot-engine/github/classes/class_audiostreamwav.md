:github_url: hide



# AudioStreamWAV

**Inherits:** [AudioStream<class_AudioStream>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Stores audio data loaded from WAV files.


## Description

AudioStreamWAV stores sound samples loaded from WAV files. To play the stored sound, use an [AudioStreamPlayer<class_AudioStreamPlayer>] (for non-positional audio) or [AudioStreamPlayer2D<class_AudioStreamPlayer2D>]/[AudioStreamPlayer3D<class_AudioStreamPlayer3D>] (for positional audio). The sound can be looped.

This class can also be used to store dynamically-generated PCM audio data. See also [AudioStreamGenerator<class_AudioStreamGenerator>] for procedural audio generation.


## Tutorials

- [../tutorials/io/runtime_file_loading_and_saving](Runtime file loading and saving .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------+-------------------------------------------------------------+-----------------------+
> | :ref:`PackedByteArray<class_PackedByteArray>` | :ref:`data<class_AudioStreamWAV_property_data>`             | ``PackedByteArray()`` |
> +-----------------------------------------------+-------------------------------------------------------------+-----------------------+
> | :ref:`Format<enum_AudioStreamWAV_Format>`     | :ref:`format<class_AudioStreamWAV_property_format>`         | ``0``                 |
> +-----------------------------------------------+-------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                         | :ref:`loop_begin<class_AudioStreamWAV_property_loop_begin>` | ``0``                 |
> +-----------------------------------------------+-------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                         | :ref:`loop_end<class_AudioStreamWAV_property_loop_end>`     | ``0``                 |
> +-----------------------------------------------+-------------------------------------------------------------+-----------------------+
> | :ref:`LoopMode<enum_AudioStreamWAV_LoopMode>` | :ref:`loop_mode<class_AudioStreamWAV_property_loop_mode>`   | ``0``                 |
> +-----------------------------------------------+-------------------------------------------------------------+-----------------------+
> | :ref:`int<class_int>`                         | :ref:`mix_rate<class_AudioStreamWAV_property_mix_rate>`     | ``44100``             |
> +-----------------------------------------------+-------------------------------------------------------------+-----------------------+
> | :ref:`bool<class_bool>`                       | :ref:`stereo<class_AudioStreamWAV_property_stereo>`         | ``false``             |
> +-----------------------------------------------+-------------------------------------------------------------+-----------------------+
> | :ref:`Dictionary<class_Dictionary>`           | :ref:`tags<class_AudioStreamWAV_property_tags>`             | ``{}``                |
> +-----------------------------------------------+-------------------------------------------------------------+-----------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamWAV<class_AudioStreamWAV>` | :ref:`load_from_buffer<class_AudioStreamWAV_method_load_from_buffer>`\ (\ stream_data\: :ref:`PackedByteArray<class_PackedByteArray>`, options\: :ref:`Dictionary<class_Dictionary>` = {}\ ) |static| |
> +---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioStreamWAV<class_AudioStreamWAV>` | :ref:`load_from_file<class_AudioStreamWAV_method_load_from_file>`\ (\ path\: :ref:`String<class_String>`, options\: :ref:`Dictionary<class_Dictionary>` = {}\ ) |static|                              |
> +---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`       | :ref:`save_to_wav<class_AudioStreamWAV_method_save_to_wav>`\ (\ path\: :ref:`String<class_String>`\ )                                                                                                 |
> +---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Enumerations



enum **Format**: [🔗<enum_AudioStreamWAV_Format>]



[Format<enum_AudioStreamWAV_Format>] **FORMAT_8_BITS** = `0`

8-bit PCM audio codec.



[Format<enum_AudioStreamWAV_Format>] **FORMAT_16_BITS** = `1`

16-bit PCM audio codec.



[Format<enum_AudioStreamWAV_Format>] **FORMAT_IMA_ADPCM** = `2`

Audio is lossily compressed as IMA ADPCM.



[Format<enum_AudioStreamWAV_Format>] **FORMAT_QOA** = `3`

Audio is lossily compressed as [Quite OK Audio ](https://qoaformat.org/)_.


----



enum **LoopMode**: [🔗<enum_AudioStreamWAV_LoopMode>]



[LoopMode<enum_AudioStreamWAV_LoopMode>] **LOOP_DISABLED** = `0`

Audio does not loop.



[LoopMode<enum_AudioStreamWAV_LoopMode>] **LOOP_FORWARD** = `1`

Audio loops the data between [loop_begin<class_AudioStreamWAV_property_loop_begin>] and [loop_end<class_AudioStreamWAV_property_loop_end>], playing forward only.



[LoopMode<enum_AudioStreamWAV_LoopMode>] **LOOP_PINGPONG** = `2`

Audio loops the data between [loop_begin<class_AudioStreamWAV_property_loop_begin>] and [loop_end<class_AudioStreamWAV_property_loop_end>], playing back and forth.



[LoopMode<enum_AudioStreamWAV_LoopMode>] **LOOP_BACKWARD** = `3`

Audio loops the data between [loop_begin<class_AudioStreamWAV_property_loop_begin>] and [loop_end<class_AudioStreamWAV_property_loop_end>], playing backward only.


----


## Property Descriptions



[PackedByteArray<class_PackedByteArray>] **data** = `PackedByteArray()` [🔗<class_AudioStreamWAV_property_data>]


- |void| **set_data**\ (\ value\: [PackedByteArray<class_PackedByteArray>]\ )
- [PackedByteArray<class_PackedByteArray>] **get_data**\ (\ )

Contains the audio data in bytes.

\ **Note:** If [format<class_AudioStreamWAV_property_format>] is set to [FORMAT_8_BITS<class_AudioStreamWAV_constant_FORMAT_8_BITS>], this property expects signed 8-bit PCM data. To convert from unsigned 8-bit PCM, subtract 128 from each byte.

\ **Note:** If [format<class_AudioStreamWAV_property_format>] is set to [FORMAT_QOA<class_AudioStreamWAV_constant_FORMAT_QOA>], this property expects data from a full QOA file.

**Note:** The returned array is *copied* and any changes to it will not update the original property value. See [PackedByteArray<class_PackedByteArray>] for more details.


----



[Format<enum_AudioStreamWAV_Format>] **format** = `0` [🔗<class_AudioStreamWAV_property_format>]


- |void| **set_format**\ (\ value\: [Format<enum_AudioStreamWAV_Format>]\ )
- [Format<enum_AudioStreamWAV_Format>] **get_format**\ (\ )

Audio format.


----



[int<class_int>] **loop_begin** = `0` [🔗<class_AudioStreamWAV_property_loop_begin>]


- |void| **set_loop_begin**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_loop_begin**\ (\ )

The loop start point (in number of samples, relative to the beginning of the stream).


----



[int<class_int>] **loop_end** = `0` [🔗<class_AudioStreamWAV_property_loop_end>]


- |void| **set_loop_end**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_loop_end**\ (\ )

The loop end point (in number of samples, relative to the beginning of the stream).


----



[LoopMode<enum_AudioStreamWAV_LoopMode>] **loop_mode** = `0` [🔗<class_AudioStreamWAV_property_loop_mode>]


- |void| **set_loop_mode**\ (\ value\: [LoopMode<enum_AudioStreamWAV_LoopMode>]\ )
- [LoopMode<enum_AudioStreamWAV_LoopMode>] **get_loop_mode**\ (\ )

The loop mode.


----



[int<class_int>] **mix_rate** = `44100` [🔗<class_AudioStreamWAV_property_mix_rate>]


- |void| **set_mix_rate**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_mix_rate**\ (\ )

The sample rate for mixing this audio. Higher values require more storage space, but result in better quality.

In games, common sample rates in use are `11025`, `16000`, `22050`, `32000`, `44100`, and `48000`.

According to the [Nyquist-Shannon sampling theorem ](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem)_, there is no quality difference to human hearing when going past 40,000 Hz (since most humans can only hear up to ~20,000 Hz, often less). If you are using lower-pitched sounds such as voices, lower sample rates such as `32000` or `22050` may be usable with no loss in quality.


----



[bool<class_bool>] **stereo** = `false` [🔗<class_AudioStreamWAV_property_stereo>]


- |void| **set_stereo**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_stereo**\ (\ )

If `true`, audio is stereo.


----



[Dictionary<class_Dictionary>] **tags** = `{}` [🔗<class_AudioStreamWAV_property_tags>]


- |void| **set_tags**\ (\ value\: [Dictionary<class_Dictionary>]\ )
- [Dictionary<class_Dictionary>] **get_tags**\ (\ )

Contains user-defined tags if found in the WAV data.

Commonly used tags include `title`, `artist`, `album`, `tracknumber`, and `date` (`date` does not have a standard date format).

\ **Note:** No tag is *guaranteed* to be present in every file, so make sure to account for the keys not always existing.

\ **Note:** Only WAV files using a `LIST` chunk with an identifier of `INFO` to encode the tags are currently supported.


----


## Method Descriptions



[AudioStreamWAV<class_AudioStreamWAV>] **load_from_buffer**\ (\ stream_data\: [PackedByteArray<class_PackedByteArray>], options\: [Dictionary<class_Dictionary>] = {}\ ) |static| [🔗<class_AudioStreamWAV_method_load_from_buffer>]

Creates a new **AudioStreamWAV** instance from the given buffer. The buffer must contain WAV data.

The keys and values of `options` match the properties of [ResourceImporterWAV<class_ResourceImporterWAV>]. The usage of `options` is identical to [load_from_file()<class_AudioStreamWAV_method_load_from_file>].


----



[AudioStreamWAV<class_AudioStreamWAV>] **load_from_file**\ (\ path\: [String<class_String>], options\: [Dictionary<class_Dictionary>] = {}\ ) |static| [🔗<class_AudioStreamWAV_method_load_from_file>]

Creates a new **AudioStreamWAV** instance from the given file path. The file must be in WAV format.

The keys and values of `options` match the properties of [ResourceImporterWAV<class_ResourceImporterWAV>].

\ **Example:** Load the first file dropped as a WAV and play it:

::

    @onready var audio_player = $AudioStreamPlayer

    func _ready():
        get_window().files_dropped.connect(_on_files_dropped)

    func _on_files_dropped(files):
        if files[0].get_extension() == "wav":
            audio_player.stream = AudioStreamWAV.load_from_file(files[0], {
                    "force/max_rate": true,
                    "force/max_rate_hz": 11025
                })
            audio_player.play()


----



[Error<enum_@GlobalScope_Error>] **save_to_wav**\ (\ path\: [String<class_String>]\ ) [🔗<class_AudioStreamWAV_method_save_to_wav>]

Saves the AudioStreamWAV as a WAV file to `path`. Samples with IMA ADPCM or Quite OK Audio formats can't be saved.

\ **Note:** A `.wav` extension is automatically appended to `path` if it is missing.

