:github_url: hide



# AudioStreamGeneratorPlayback

**Inherits:** [AudioStreamPlaybackResampled<class_AudioStreamPlaybackResampled>] **<** [AudioStreamPlayback<class_AudioStreamPlayback>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Plays back audio generated using [AudioStreamGenerator<class_AudioStreamGenerator>].


## Description

This class is meant to be used with [AudioStreamGenerator<class_AudioStreamGenerator>] to play back the generated audio in real-time.


## Tutorials

- [Audio Generator Demo ](https://godotengine.org/asset-library/asset/2759)_

- [Godot 3.2 will get new audio features ](https://godotengine.org/article/godot-32-will-get-new-audio-features)_


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`can_push_buffer<class_AudioStreamGeneratorPlayback_method_can_push_buffer>`\ (\ amount\: :ref:`int<class_int>`\ ) |const|               |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`clear_buffer<class_AudioStreamGeneratorPlayback_method_clear_buffer>`\ (\ )                                                             |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`   | :ref:`get_frames_available<class_AudioStreamGeneratorPlayback_method_get_frames_available>`\ (\ ) |const|                                     |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`   | :ref:`get_skips<class_AudioStreamGeneratorPlayback_method_get_skips>`\ (\ ) |const|                                                           |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`push_buffer<class_AudioStreamGeneratorPlayback_method_push_buffer>`\ (\ frames\: :ref:`PackedVector2Array<class_PackedVector2Array>`\ ) |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`push_frame<class_AudioStreamGeneratorPlayback_method_push_frame>`\ (\ frame\: :ref:`Vector2<class_Vector2>`\ )                          |
> +-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[bool<class_bool>] **can_push_buffer**\ (\ amount\: [int<class_int>]\ ) |const| [🔗<class_AudioStreamGeneratorPlayback_method_can_push_buffer>]

Returns `true` if a buffer of the size `amount` can be pushed to the audio sample data buffer without overflowing it, `false` otherwise.


----



|void| **clear_buffer**\ (\ ) [🔗<class_AudioStreamGeneratorPlayback_method_clear_buffer>]

Clears the audio sample data buffer.


----



[int<class_int>] **get_frames_available**\ (\ ) |const| [🔗<class_AudioStreamGeneratorPlayback_method_get_frames_available>]

Returns the number of frames that can be pushed to the audio sample data buffer without overflowing it. If the result is `0`, the buffer is full.


----



[int<class_int>] **get_skips**\ (\ ) |const| [🔗<class_AudioStreamGeneratorPlayback_method_get_skips>]

Returns the number of times the playback skipped due to a buffer underrun in the audio sample data. This value is reset at the start of the playback.


----



[bool<class_bool>] **push_buffer**\ (\ frames\: [PackedVector2Array<class_PackedVector2Array>]\ ) [🔗<class_AudioStreamGeneratorPlayback_method_push_buffer>]

Pushes several audio data frames to the buffer. This is usually more efficient than [push_frame()<class_AudioStreamGeneratorPlayback_method_push_frame>] in C# and compiled languages via GDExtension, but [push_buffer()<class_AudioStreamGeneratorPlayback_method_push_buffer>] may be *less* efficient in GDScript.


----



[bool<class_bool>] **push_frame**\ (\ frame\: [Vector2<class_Vector2>]\ ) [🔗<class_AudioStreamGeneratorPlayback_method_push_frame>]

Pushes a single audio data frame to the buffer. This is usually less efficient than [push_buffer()<class_AudioStreamGeneratorPlayback_method_push_buffer>] in C# and compiled languages via GDExtension, but [push_frame()<class_AudioStreamGeneratorPlayback_method_push_frame>] may be *more* efficient in GDScript.

