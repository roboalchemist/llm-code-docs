:github_url: hide



# AudioServer

**Inherits:** [Object<class_Object>]

Server interface for low-level audio access.


## Description

**AudioServer** is a low-level server interface for audio access. It is in charge of creating sample data (playable audio) as well as its playback via a voice interface.


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)

- [Audio Device Changer Demo ](https://godotengine.org/asset-library/asset/2758)_

- [Audio Microphone Record Demo ](https://godotengine.org/asset-library/asset/2760)_

- [Audio Spectrum Visualizer Demo ](https://godotengine.org/asset-library/asset/2762)_


## Properties

> **TABLE**
> :widths: auto
>
> +-----------------------------+------------------------------------------------------------------------------+---------------+
> | :ref:`int<class_int>`       | :ref:`bus_count<class_AudioServer_property_bus_count>`                       | ``1``         |
> +-----------------------------+------------------------------------------------------------------------------+---------------+
> | :ref:`String<class_String>` | :ref:`input_device<class_AudioServer_property_input_device>`                 | ``"Default"`` |
> +-----------------------------+------------------------------------------------------------------------------+---------------+
> | :ref:`String<class_String>` | :ref:`output_device<class_AudioServer_property_output_device>`               | ``"Default"`` |
> +-----------------------------+------------------------------------------------------------------------------+---------------+
> | :ref:`float<class_float>`   | :ref:`playback_speed_scale<class_AudioServer_property_playback_speed_scale>` | ``1.0``       |
> +-----------------------------+------------------------------------------------------------------------------+---------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`add_bus<class_AudioServer_method_add_bus>`\ (\ at_position\: :ref:`int<class_int>` = -1\ )                                                                                                 |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`add_bus_effect<class_AudioServer_method_add_bus_effect>`\ (\ bus_idx\: :ref:`int<class_int>`, effect\: :ref:`AudioEffect<class_AudioEffect>`, at_position\: :ref:`int<class_int>` = -1\ )  |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioBusLayout<class_AudioBusLayout>`           | :ref:`generate_bus_layout<class_AudioServer_method_generate_bus_layout>`\ (\ ) |const|                                                                                                           |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`get_bus_channels<class_AudioServer_method_get_bus_channels>`\ (\ bus_idx\: :ref:`int<class_int>`\ ) |const|                                                                                |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioEffect<class_AudioEffect>`                 | :ref:`get_bus_effect<class_AudioServer_method_get_bus_effect>`\ (\ bus_idx\: :ref:`int<class_int>`, effect_idx\: :ref:`int<class_int>`\ )                                                        |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`get_bus_effect_count<class_AudioServer_method_get_bus_effect_count>`\ (\ bus_idx\: :ref:`int<class_int>`\ )                                                                                |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`AudioEffectInstance<class_AudioEffectInstance>` | :ref:`get_bus_effect_instance<class_AudioServer_method_get_bus_effect_instance>`\ (\ bus_idx\: :ref:`int<class_int>`, effect_idx\: :ref:`int<class_int>`, channel\: :ref:`int<class_int>` = 0\ ) |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`get_bus_index<class_AudioServer_method_get_bus_index>`\ (\ bus_name\: :ref:`StringName<class_StringName>`\ ) |const|                                                                       |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                           | :ref:`get_bus_name<class_AudioServer_method_get_bus_name>`\ (\ bus_idx\: :ref:`int<class_int>`\ ) |const|                                                                                        |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_bus_peak_volume_left_db<class_AudioServer_method_get_bus_peak_volume_left_db>`\ (\ bus_idx\: :ref:`int<class_int>`, channel\: :ref:`int<class_int>`\ ) |const|                         |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_bus_peak_volume_right_db<class_AudioServer_method_get_bus_peak_volume_right_db>`\ (\ bus_idx\: :ref:`int<class_int>`, channel\: :ref:`int<class_int>`\ ) |const|                       |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`StringName<class_StringName>`                   | :ref:`get_bus_send<class_AudioServer_method_get_bus_send>`\ (\ bus_idx\: :ref:`int<class_int>`\ ) |const|                                                                                        |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_bus_volume_db<class_AudioServer_method_get_bus_volume_db>`\ (\ bus_idx\: :ref:`int<class_int>`\ ) |const|                                                                              |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_bus_volume_linear<class_AudioServer_method_get_bus_volume_linear>`\ (\ bus_idx\: :ref:`int<class_int>`\ ) |const|                                                                      |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`                           | :ref:`get_driver_name<class_AudioServer_method_get_driver_name>`\ (\ ) |const|                                                                                                                   |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`get_input_buffer_length_frames<class_AudioServer_method_get_input_buffer_length_frames>`\ (\ )                                                                                             |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`     | :ref:`get_input_device_list<class_AudioServer_method_get_input_device_list>`\ (\ )                                                                                                               |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedVector2Array<class_PackedVector2Array>`   | :ref:`get_input_frames<class_AudioServer_method_get_input_frames>`\ (\ frames\: :ref:`int<class_int>`\ )                                                                                         |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                                 | :ref:`get_input_frames_available<class_AudioServer_method_get_input_frames_available>`\ (\ )                                                                                                     |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_input_mix_rate<class_AudioServer_method_get_input_mix_rate>`\ (\ ) |const|                                                                                                             |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_mix_rate<class_AudioServer_method_get_mix_rate>`\ (\ ) |const|                                                                                                                         |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`PackedStringArray<class_PackedStringArray>`     | :ref:`get_output_device_list<class_AudioServer_method_get_output_device_list>`\ (\ )                                                                                                             |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_output_latency<class_AudioServer_method_get_output_latency>`\ (\ ) |const|                                                                                                             |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SpeakerMode<enum_AudioServer_SpeakerMode>`      | :ref:`get_speaker_mode<class_AudioServer_method_get_speaker_mode>`\ (\ ) |const|                                                                                                                 |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_time_since_last_mix<class_AudioServer_method_get_time_since_last_mix>`\ (\ ) |const|                                                                                                   |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`float<class_float>`                             | :ref:`get_time_to_next_mix<class_AudioServer_method_get_time_to_next_mix>`\ (\ ) |const|                                                                                                         |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`is_bus_bypassing_effects<class_AudioServer_method_is_bus_bypassing_effects>`\ (\ bus_idx\: :ref:`int<class_int>`\ ) |const|                                                                |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`is_bus_effect_enabled<class_AudioServer_method_is_bus_effect_enabled>`\ (\ bus_idx\: :ref:`int<class_int>`, effect_idx\: :ref:`int<class_int>`\ ) |const|                                  |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`is_bus_mute<class_AudioServer_method_is_bus_mute>`\ (\ bus_idx\: :ref:`int<class_int>`\ ) |const|                                                                                          |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`is_bus_solo<class_AudioServer_method_is_bus_solo>`\ (\ bus_idx\: :ref:`int<class_int>`\ ) |const|                                                                                          |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`                               | :ref:`is_stream_registered_as_sample<class_AudioServer_method_is_stream_registered_as_sample>`\ (\ stream\: :ref:`AudioStream<class_AudioStream>`\ )                                             |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`lock<class_AudioServer_method_lock>`\ (\ )                                                                                                                                                 |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`move_bus<class_AudioServer_method_move_bus>`\ (\ index\: :ref:`int<class_int>`, to_index\: :ref:`int<class_int>`\ )                                                                        |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`register_stream_as_sample<class_AudioServer_method_register_stream_as_sample>`\ (\ stream\: :ref:`AudioStream<class_AudioStream>`\ )                                                       |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`remove_bus<class_AudioServer_method_remove_bus>`\ (\ index\: :ref:`int<class_int>`\ )                                                                                                      |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`remove_bus_effect<class_AudioServer_method_remove_bus_effect>`\ (\ bus_idx\: :ref:`int<class_int>`, effect_idx\: :ref:`int<class_int>`\ )                                                  |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_bus_bypass_effects<class_AudioServer_method_set_bus_bypass_effects>`\ (\ bus_idx\: :ref:`int<class_int>`, enable\: :ref:`bool<class_bool>`\ )                                          |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_bus_effect_enabled<class_AudioServer_method_set_bus_effect_enabled>`\ (\ bus_idx\: :ref:`int<class_int>`, effect_idx\: :ref:`int<class_int>`, enabled\: :ref:`bool<class_bool>`\ )     |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_bus_layout<class_AudioServer_method_set_bus_layout>`\ (\ bus_layout\: :ref:`AudioBusLayout<class_AudioBusLayout>`\ )                                                                   |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_bus_mute<class_AudioServer_method_set_bus_mute>`\ (\ bus_idx\: :ref:`int<class_int>`, enable\: :ref:`bool<class_bool>`\ )                                                              |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_bus_name<class_AudioServer_method_set_bus_name>`\ (\ bus_idx\: :ref:`int<class_int>`, name\: :ref:`String<class_String>`\ )                                                            |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_bus_send<class_AudioServer_method_set_bus_send>`\ (\ bus_idx\: :ref:`int<class_int>`, send\: :ref:`StringName<class_StringName>`\ )                                                    |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_bus_solo<class_AudioServer_method_set_bus_solo>`\ (\ bus_idx\: :ref:`int<class_int>`, enable\: :ref:`bool<class_bool>`\ )                                                              |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_bus_volume_db<class_AudioServer_method_set_bus_volume_db>`\ (\ bus_idx\: :ref:`int<class_int>`, volume_db\: :ref:`float<class_float>`\ )                                               |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_bus_volume_linear<class_AudioServer_method_set_bus_volume_linear>`\ (\ bus_idx\: :ref:`int<class_int>`, volume_linear\: :ref:`float<class_float>`\ )                                   |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`set_enable_tagging_used_audio_streams<class_AudioServer_method_set_enable_tagging_used_audio_streams>`\ (\ enable\: :ref:`bool<class_bool>`\ )                                             |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                 | :ref:`set_input_device_active<class_AudioServer_method_set_input_device_active>`\ (\ active\: :ref:`bool<class_bool>`\ )                                                                         |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`swap_bus_effects<class_AudioServer_method_swap_bus_effects>`\ (\ bus_idx\: :ref:`int<class_int>`, effect_idx\: :ref:`int<class_int>`, by_effect_idx\: :ref:`int<class_int>`\ )             |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                | :ref:`unlock<class_AudioServer_method_unlock>`\ (\ )                                                                                                                                             |
> +-------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Signals



**bus_layout_changed**\ (\ ) [🔗<class_AudioServer_signal_bus_layout_changed>]

Emitted when an audio bus is added, deleted, or moved.


----



**bus_renamed**\ (\ bus_index\: [int<class_int>], old_name\: [StringName<class_StringName>], new_name\: [StringName<class_StringName>]\ ) [🔗<class_AudioServer_signal_bus_renamed>]

Emitted when the audio bus at `bus_index` is renamed from `old_name` to `new_name`.


----


## Enumerations



enum **SpeakerMode**: [🔗<enum_AudioServer_SpeakerMode>]



[SpeakerMode<enum_AudioServer_SpeakerMode>] **SPEAKER_MODE_STEREO** = `0`

Two or fewer speakers were detected.



[SpeakerMode<enum_AudioServer_SpeakerMode>] **SPEAKER_SURROUND_31** = `1`

A 3.1 channel surround setup was detected.



[SpeakerMode<enum_AudioServer_SpeakerMode>] **SPEAKER_SURROUND_51** = `2`

A 5.1 channel surround setup was detected.



[SpeakerMode<enum_AudioServer_SpeakerMode>] **SPEAKER_SURROUND_71** = `3`

A 7.1 channel surround setup was detected.


----



enum **PlaybackType**: [🔗<enum_AudioServer_PlaybackType>]



[PlaybackType<enum_AudioServer_PlaybackType>] **PLAYBACK_TYPE_DEFAULT** = `0`

**Experimental:** This constant may be changed or removed in future versions.

The playback will be considered of the type declared at [ProjectSettings.audio/general/default_playback_type<class_ProjectSettings_property_audio/general/default_playback_type>].



[PlaybackType<enum_AudioServer_PlaybackType>] **PLAYBACK_TYPE_STREAM** = `1`

**Experimental:** This constant may be changed or removed in future versions.

Force the playback to be considered as a stream.



[PlaybackType<enum_AudioServer_PlaybackType>] **PLAYBACK_TYPE_SAMPLE** = `2`

**Experimental:** This constant may be changed or removed in future versions.

Force the playback to be considered as a sample. This can provide lower latency and more stable playback (with less risk of audio crackling), at the cost of having less flexibility.

\ **Note:** Only currently supported on the web platform.

\ **Note:** [AudioEffect<class_AudioEffect>]\ s are not supported when playback is considered as a sample.



[PlaybackType<enum_AudioServer_PlaybackType>] **PLAYBACK_TYPE_MAX** = `3`

**Experimental:** This constant may be changed or removed in future versions.

Represents the size of the [PlaybackType<enum_AudioServer_PlaybackType>] enum.


----


## Property Descriptions



[int<class_int>] **bus_count** = `1` [🔗<class_AudioServer_property_bus_count>]


- |void| **set_bus_count**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_bus_count**\ (\ )

Number of available audio buses.


----



[String<class_String>] **input_device** = `"Default"` [🔗<class_AudioServer_property_input_device>]


- |void| **set_input_device**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_input_device**\ (\ )

Name of the current device for audio input (see [get_input_device_list()<class_AudioServer_method_get_input_device_list>]). On systems with multiple audio inputs (such as analog, USB and HDMI audio), this can be used to select the audio input device. The value `"Default"` will record audio on the system-wide default audio input. If an invalid device name is set, the value will be reverted back to `"Default"`.

\ **Note:** [ProjectSettings.audio/driver/enable_input<class_ProjectSettings_property_audio/driver/enable_input>] must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.


----



[String<class_String>] **output_device** = `"Default"` [🔗<class_AudioServer_property_output_device>]


- |void| **set_output_device**\ (\ value\: [String<class_String>]\ )
- [String<class_String>] **get_output_device**\ (\ )

Name of the current device for audio output (see [get_output_device_list()<class_AudioServer_method_get_output_device_list>]). On systems with multiple audio outputs (such as analog, USB and HDMI audio), this can be used to select the audio output device. The value `"Default"` will play audio on the system-wide default audio output. If an invalid device name is set, the value will be reverted back to `"Default"`.


----



[float<class_float>] **playback_speed_scale** = `1.0` [🔗<class_AudioServer_property_playback_speed_scale>]


- |void| **set_playback_speed_scale**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_playback_speed_scale**\ (\ )

Scales the rate at which audio is played (i.e. setting it to `0.5` will make the audio be played at half its speed). See also [Engine.time_scale<class_Engine_property_time_scale>] to affect the general simulation speed, which is independent from [playback_speed_scale<class_AudioServer_property_playback_speed_scale>].


----


## Method Descriptions



|void| **add_bus**\ (\ at_position\: [int<class_int>] = -1\ ) [🔗<class_AudioServer_method_add_bus>]

Adds a bus at `at_position`.


----



|void| **add_bus_effect**\ (\ bus_idx\: [int<class_int>], effect\: [AudioEffect<class_AudioEffect>], at_position\: [int<class_int>] = -1\ ) [🔗<class_AudioServer_method_add_bus_effect>]

Adds an [AudioEffect<class_AudioEffect>] effect to the bus `bus_idx` at `at_position`.


----



[AudioBusLayout<class_AudioBusLayout>] **generate_bus_layout**\ (\ ) |const| [🔗<class_AudioServer_method_generate_bus_layout>]

Generates an [AudioBusLayout<class_AudioBusLayout>] using the available buses and effects.


----



[int<class_int>] **get_bus_channels**\ (\ bus_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_get_bus_channels>]

Returns the number of channels of the bus at index `bus_idx`.


----



[AudioEffect<class_AudioEffect>] **get_bus_effect**\ (\ bus_idx\: [int<class_int>], effect_idx\: [int<class_int>]\ ) [🔗<class_AudioServer_method_get_bus_effect>]

Returns the [AudioEffect<class_AudioEffect>] at position `effect_idx` in bus `bus_idx`.


----



[int<class_int>] **get_bus_effect_count**\ (\ bus_idx\: [int<class_int>]\ ) [🔗<class_AudioServer_method_get_bus_effect_count>]

Returns the number of effects on the bus at `bus_idx`.


----



[AudioEffectInstance<class_AudioEffectInstance>] **get_bus_effect_instance**\ (\ bus_idx\: [int<class_int>], effect_idx\: [int<class_int>], channel\: [int<class_int>] = 0\ ) [🔗<class_AudioServer_method_get_bus_effect_instance>]

Returns the [AudioEffectInstance<class_AudioEffectInstance>] assigned to the given bus and effect indices (and optionally channel).


----



[int<class_int>] **get_bus_index**\ (\ bus_name\: [StringName<class_StringName>]\ ) |const| [🔗<class_AudioServer_method_get_bus_index>]

Returns the index of the bus with the name `bus_name`. Returns `-1` if no bus with the specified name exist.


----



[String<class_String>] **get_bus_name**\ (\ bus_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_get_bus_name>]

Returns the name of the bus with the index `bus_idx`.


----



[float<class_float>] **get_bus_peak_volume_left_db**\ (\ bus_idx\: [int<class_int>], channel\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_get_bus_peak_volume_left_db>]

Returns the peak volume of the left speaker at bus index `bus_idx` and channel index `channel`.


----



[float<class_float>] **get_bus_peak_volume_right_db**\ (\ bus_idx\: [int<class_int>], channel\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_get_bus_peak_volume_right_db>]

Returns the peak volume of the right speaker at bus index `bus_idx` and channel index `channel`.


----



[StringName<class_StringName>] **get_bus_send**\ (\ bus_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_get_bus_send>]

Returns the name of the bus that the bus at index `bus_idx` sends to.


----



[float<class_float>] **get_bus_volume_db**\ (\ bus_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_get_bus_volume_db>]

Returns the volume of the bus at index `bus_idx` in dB.


----



[float<class_float>] **get_bus_volume_linear**\ (\ bus_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_get_bus_volume_linear>]

Returns the volume of the bus at index `bus_idx` as a linear value.

\ **Note:** The returned value is equivalent to the result of [@GlobalScope.db_to_linear()<class_@GlobalScope_method_db_to_linear>] on the result of [get_bus_volume_db()<class_AudioServer_method_get_bus_volume_db>].


----



[String<class_String>] **get_driver_name**\ (\ ) |const| [🔗<class_AudioServer_method_get_driver_name>]

Returns the name of the current audio driver. The default usually depends on the operating system, but may be overridden via the `--audio-driver` [../tutorials/editor/command_line_tutorial](command line argument .md). `--headless` also automatically sets the audio driver to `Dummy`. See also [ProjectSettings.audio/driver/driver<class_ProjectSettings_property_audio/driver/driver>].


----



[int<class_int>] **get_input_buffer_length_frames**\ (\ ) [🔗<class_AudioServer_method_get_input_buffer_length_frames>]

**Experimental:** This method may be changed or removed in future versions.

Returns the absolute size of the microphone input buffer. This is set to a multiple of the audio latency and can be used to estimate the minimum rate at which the frames need to be fetched.


----



[PackedStringArray<class_PackedStringArray>] **get_input_device_list**\ (\ ) [🔗<class_AudioServer_method_get_input_device_list>]

Returns the names of all audio input devices detected on the system.

\ **Note:** [ProjectSettings.audio/driver/enable_input<class_ProjectSettings_property_audio/driver/enable_input>] must be `true` for audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.


----



[PackedVector2Array<class_PackedVector2Array>] **get_input_frames**\ (\ frames\: [int<class_int>]\ ) [🔗<class_AudioServer_method_get_input_frames>]

**Experimental:** This method may be changed or removed in future versions.

Returns a [PackedVector2Array<class_PackedVector2Array>] containing exactly `frames` audio samples from the internal microphone buffer if available, otherwise returns an empty [PackedVector2Array<class_PackedVector2Array>].

The buffer is filled at the rate of [get_input_mix_rate()<class_AudioServer_method_get_input_mix_rate>] frames per second when [set_input_device_active()<class_AudioServer_method_set_input_device_active>] has successfully been set to `true`.

The samples are signed floating-point PCM values between `-1` and `1`.


----



[int<class_int>] **get_input_frames_available**\ (\ ) [🔗<class_AudioServer_method_get_input_frames_available>]

**Experimental:** This method may be changed or removed in future versions.

Returns the number of frames available to read using [get_input_frames()<class_AudioServer_method_get_input_frames>].


----



[float<class_float>] **get_input_mix_rate**\ (\ ) |const| [🔗<class_AudioServer_method_get_input_mix_rate>]

Returns the sample rate at the input of the **AudioServer**.


----



[float<class_float>] **get_mix_rate**\ (\ ) |const| [🔗<class_AudioServer_method_get_mix_rate>]

Returns the sample rate at the output of the **AudioServer**.


----



[PackedStringArray<class_PackedStringArray>] **get_output_device_list**\ (\ ) [🔗<class_AudioServer_method_get_output_device_list>]

Returns the names of all audio output devices detected on the system.


----



[float<class_float>] **get_output_latency**\ (\ ) |const| [🔗<class_AudioServer_method_get_output_latency>]

Returns the audio driver's effective output latency. This is based on [ProjectSettings.audio/driver/output_latency<class_ProjectSettings_property_audio/driver/output_latency>], but the exact returned value will differ depending on the operating system and audio driver.

\ **Note:** This can be expensive; it is not recommended to call [get_output_latency()<class_AudioServer_method_get_output_latency>] every frame.


----



[SpeakerMode<enum_AudioServer_SpeakerMode>] **get_speaker_mode**\ (\ ) |const| [🔗<class_AudioServer_method_get_speaker_mode>]

Returns the speaker configuration.


----



[float<class_float>] **get_time_since_last_mix**\ (\ ) |const| [🔗<class_AudioServer_method_get_time_since_last_mix>]

Returns the relative time since the last mix occurred.


----



[float<class_float>] **get_time_to_next_mix**\ (\ ) |const| [🔗<class_AudioServer_method_get_time_to_next_mix>]

Returns the relative time until the next mix occurs.


----



[bool<class_bool>] **is_bus_bypassing_effects**\ (\ bus_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_is_bus_bypassing_effects>]

If `true`, the bus at index `bus_idx` is bypassing effects.


----



[bool<class_bool>] **is_bus_effect_enabled**\ (\ bus_idx\: [int<class_int>], effect_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_is_bus_effect_enabled>]

If `true`, the effect at index `effect_idx` on the bus at index `bus_idx` is enabled.


----



[bool<class_bool>] **is_bus_mute**\ (\ bus_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_is_bus_mute>]

If `true`, the bus at index `bus_idx` is muted.


----



[bool<class_bool>] **is_bus_solo**\ (\ bus_idx\: [int<class_int>]\ ) |const| [🔗<class_AudioServer_method_is_bus_solo>]

If `true`, the bus at index `bus_idx` is in solo mode.


----



[bool<class_bool>] **is_stream_registered_as_sample**\ (\ stream\: [AudioStream<class_AudioStream>]\ ) [🔗<class_AudioServer_method_is_stream_registered_as_sample>]

**Experimental:** This method may be changed or removed in future versions.

If `true`, the stream is registered as a sample. The engine will not have to register it before playing the sample.

If `false`, the stream will have to be registered before playing it. To prevent lag spikes, register the stream as sample with [register_stream_as_sample()<class_AudioServer_method_register_stream_as_sample>].


----



|void| **lock**\ (\ ) [🔗<class_AudioServer_method_lock>]

Locks the audio driver's main loop.

\ **Note:** Remember to unlock it afterwards.


----



|void| **move_bus**\ (\ index\: [int<class_int>], to_index\: [int<class_int>]\ ) [🔗<class_AudioServer_method_move_bus>]

Moves the bus from index `index` to index `to_index`.


----



|void| **register_stream_as_sample**\ (\ stream\: [AudioStream<class_AudioStream>]\ ) [🔗<class_AudioServer_method_register_stream_as_sample>]

**Experimental:** This method may be changed or removed in future versions.

Forces the registration of a stream as a sample.

\ **Note:** Lag spikes may occur when calling this method, especially on single-threaded builds. It is suggested to call this method while loading assets, where the lag spike could be masked, instead of registering the sample right before it needs to be played.


----



|void| **remove_bus**\ (\ index\: [int<class_int>]\ ) [🔗<class_AudioServer_method_remove_bus>]

Removes the bus at index `index`.


----



|void| **remove_bus_effect**\ (\ bus_idx\: [int<class_int>], effect_idx\: [int<class_int>]\ ) [🔗<class_AudioServer_method_remove_bus_effect>]

Removes the effect at index `effect_idx` from the bus at index `bus_idx`.


----



|void| **set_bus_bypass_effects**\ (\ bus_idx\: [int<class_int>], enable\: [bool<class_bool>]\ ) [🔗<class_AudioServer_method_set_bus_bypass_effects>]

If `true`, the bus at index `bus_idx` is bypassing effects.


----



|void| **set_bus_effect_enabled**\ (\ bus_idx\: [int<class_int>], effect_idx\: [int<class_int>], enabled\: [bool<class_bool>]\ ) [🔗<class_AudioServer_method_set_bus_effect_enabled>]

If `true`, the effect at index `effect_idx` on the bus at index `bus_idx` is enabled.


----



|void| **set_bus_layout**\ (\ bus_layout\: [AudioBusLayout<class_AudioBusLayout>]\ ) [🔗<class_AudioServer_method_set_bus_layout>]

Overwrites the currently used [AudioBusLayout<class_AudioBusLayout>].


----



|void| **set_bus_mute**\ (\ bus_idx\: [int<class_int>], enable\: [bool<class_bool>]\ ) [🔗<class_AudioServer_method_set_bus_mute>]

If `true`, the bus at index `bus_idx` is muted.


----



|void| **set_bus_name**\ (\ bus_idx\: [int<class_int>], name\: [String<class_String>]\ ) [🔗<class_AudioServer_method_set_bus_name>]

Sets the name of the bus at index `bus_idx` to `name`.


----



|void| **set_bus_send**\ (\ bus_idx\: [int<class_int>], send\: [StringName<class_StringName>]\ ) [🔗<class_AudioServer_method_set_bus_send>]

Connects the output of the bus at `bus_idx` to the bus named `send`.


----



|void| **set_bus_solo**\ (\ bus_idx\: [int<class_int>], enable\: [bool<class_bool>]\ ) [🔗<class_AudioServer_method_set_bus_solo>]

If `true`, the bus at index `bus_idx` is in solo mode.


----



|void| **set_bus_volume_db**\ (\ bus_idx\: [int<class_int>], volume_db\: [float<class_float>]\ ) [🔗<class_AudioServer_method_set_bus_volume_db>]

Sets the volume in decibels of the bus at index `bus_idx` to `volume_db`.


----



|void| **set_bus_volume_linear**\ (\ bus_idx\: [int<class_int>], volume_linear\: [float<class_float>]\ ) [🔗<class_AudioServer_method_set_bus_volume_linear>]

Sets the volume as a linear value of the bus at index `bus_idx` to `volume_linear`.

\ **Note:** Using this method is equivalent to calling [set_bus_volume_db()<class_AudioServer_method_set_bus_volume_db>] with the result of [@GlobalScope.linear_to_db()<class_@GlobalScope_method_linear_to_db>] on a value.


----



|void| **set_enable_tagging_used_audio_streams**\ (\ enable\: [bool<class_bool>]\ ) [🔗<class_AudioServer_method_set_enable_tagging_used_audio_streams>]

If set to `true`, all instances of [AudioStreamPlayback<class_AudioStreamPlayback>] will call [AudioStreamPlayback._tag_used_streams()<class_AudioStreamPlayback_private_method__tag_used_streams>] every mix step.

\ **Note:** This is enabled by default in the editor, as it is used by editor plugins for the audio stream previews.


----



[Error<enum_@GlobalScope_Error>] **set_input_device_active**\ (\ active\: [bool<class_bool>]\ ) [🔗<class_AudioServer_method_set_input_device_active>]

**Experimental:** This method may be changed or removed in future versions.

If `active` is `true`, starts the microphone input stream specified by [input_device<class_AudioServer_property_input_device>] or returns an error if it failed.

If `active` is `false`, stops the input stream if it is running.


----



|void| **swap_bus_effects**\ (\ bus_idx\: [int<class_int>], effect_idx\: [int<class_int>], by_effect_idx\: [int<class_int>]\ ) [🔗<class_AudioServer_method_swap_bus_effects>]

Swaps the position of two effects in bus `bus_idx`.


----



|void| **unlock**\ (\ ) [🔗<class_AudioServer_method_unlock>]

Unlocks the audio driver's main loop. (After locking it, you should always unlock it.)

