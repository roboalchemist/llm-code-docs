:github_url: hide



# AudioEffectCapture

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Captures audio from an audio bus in real-time.


## Description

AudioEffectCapture is an AudioEffect which copies all audio frames from the attached audio effect bus into its internal ring buffer.

Application code should consume these audio frames from this ring buffer using [get_buffer()<class_AudioEffectCapture_method_get_buffer>] and process it as needed, for example to capture data from an [AudioStreamMicrophone<class_AudioStreamMicrophone>], implement application-defined effects, or to transmit audio over the network. When capturing audio data from a microphone, the format of the samples will be stereo 32-bit floating-point PCM.

Unlike [AudioEffectRecord<class_AudioEffectRecord>], this effect only returns the raw audio samples instead of encoding them into an [AudioStream<class_AudioStream>].


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Properties

> **TABLE**
> :widths: auto
>
> +---------------------------+-----------------------------------------------------------------------+---------+
> | :ref:`float<class_float>` | :ref:`buffer_length<class_AudioEffectCapture_property_buffer_length>` | ``0.1`` |
> +---------------------------+-----------------------------------------------------------------------+---------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                             | :ref:`can_get_buffer<class_AudioEffectCapture_method_can_get_buffer>`\ (\ frames\: :ref:`int<class_int>`\ ) |const| |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
> | |void|                                              | :ref:`clear_buffer<class_AudioEffectCapture_method_clear_buffer>`\ (\ )                                             |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>` | :ref:`get_buffer<class_AudioEffectCapture_method_get_buffer>`\ (\ frames\: :ref:`int<class_int>`\ )                 |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_buffer_length_frames<class_AudioEffectCapture_method_get_buffer_length_frames>`\ (\ ) |const|             |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_discarded_frames<class_AudioEffectCapture_method_get_discarded_frames>`\ (\ ) |const|                     |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_frames_available<class_AudioEffectCapture_method_get_frames_available>`\ (\ ) |const|                     |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                               | :ref:`get_pushed_frames<class_AudioEffectCapture_method_get_pushed_frames>`\ (\ ) |const|                           |
> +-----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[float<class_float>] **buffer_length** = `0.1` [🔗<class_AudioEffectCapture_property_buffer_length>]


- |void| **set_buffer_length**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_buffer_length**\ (\ )

Length of the internal ring buffer, in seconds. Setting the buffer length will have no effect if already initialized.


----


## Method Descriptions



[bool<class_bool>] **can_get_buffer**\ (\ frames\: [int<class_int>]\ ) |const| [🔗<class_AudioEffectCapture_method_can_get_buffer>]

Returns `true` if at least `frames` audio frames are available to read in the internal ring buffer.


----



|void| **clear_buffer**\ (\ ) [🔗<class_AudioEffectCapture_method_clear_buffer>]

Clears the internal ring buffer.

\ **Note:** Calling this during a capture can cause the loss of samples which causes popping in the playback.


----



[PackedVector2Array<class_PackedVector2Array>] **get_buffer**\ (\ frames\: [int<class_int>]\ ) [🔗<class_AudioEffectCapture_method_get_buffer>]

Gets the next `frames` audio samples from the internal ring buffer.

Returns a [PackedVector2Array<class_PackedVector2Array>] containing exactly `frames` audio samples if available, or an empty [PackedVector2Array<class_PackedVector2Array>] if insufficient data was available.

The samples are signed floating-point PCM between `-1` and `1`. You will have to scale them if you want to use them as 8 or 16-bit integer samples. (`v = 0x7fff * samples[0].x`)


----



[int<class_int>] **get_buffer_length_frames**\ (\ ) |const| [🔗<class_AudioEffectCapture_method_get_buffer_length_frames>]

Returns the total size of the internal ring buffer in frames.


----



[int<class_int>] **get_discarded_frames**\ (\ ) |const| [🔗<class_AudioEffectCapture_method_get_discarded_frames>]

Returns the number of audio frames discarded from the audio bus due to full buffer.


----



[int<class_int>] **get_frames_available**\ (\ ) |const| [🔗<class_AudioEffectCapture_method_get_frames_available>]

Returns the number of frames available to read using [get_buffer()<class_AudioEffectCapture_method_get_buffer>].


----



[int<class_int>] **get_pushed_frames**\ (\ ) |const| [🔗<class_AudioEffectCapture_method_get_pushed_frames>]

Returns the number of audio frames inserted from the audio bus.

