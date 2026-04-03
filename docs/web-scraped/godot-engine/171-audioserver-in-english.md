# AudioServer in English

# AudioServer
Inherits:Object
Server interface for low-level audio access.

## Description
AudioServeris a low-level server interface for audio access. It is in charge of creating sample data (playable audio) as well as its playback via a voice interface.

## Tutorials
- Audio buses
Audio buses
- Audio Device Changer Demo
Audio Device Changer Demo
- Audio Microphone Record Demo
Audio Microphone Record Demo
- Audio Spectrum Visualizer Demo
Audio Spectrum Visualizer Demo

## Properties

| int | bus_count | 1 |
|---|---|---|
| String | input_device | "Default" |
| String | output_device | "Default" |
| float | playback_speed_scale | 1.0 |

bus_count
String
input_device
"Default"
String
output_device
"Default"
float
playback_speed_scale

## Methods

| void | add_bus(at_position:int= -1) |
|---|---|
| void | add_bus_effect(bus_idx:int, effect:AudioEffect, at_position:int= -1) |
| AudioBusLayout | generate_bus_layout()const |
| int | get_bus_channels(bus_idx:int)const |
| AudioEffect | get_bus_effect(bus_idx:int, effect_idx:int) |
| int | get_bus_effect_count(bus_idx:int) |
| AudioEffectInstance | get_bus_effect_instance(bus_idx:int, effect_idx:int, channel:int= 0) |
| int | get_bus_index(bus_name:StringName)const |
| String | get_bus_name(bus_idx:int)const |
| float | get_bus_peak_volume_left_db(bus_idx:int, channel:int)const |
| float | get_bus_peak_volume_right_db(bus_idx:int, channel:int)const |
| StringName | get_bus_send(bus_idx:int)const |
| float | get_bus_volume_db(bus_idx:int)const |
| float | get_bus_volume_linear(bus_idx:int)const |
| String | get_driver_name()const |
| int | get_input_buffer_length_frames() |
| PackedStringArray | get_input_device_list() |
| PackedVector2Array | get_input_frames(frames:int) |
| int | get_input_frames_available() |
| float | get_input_mix_rate()const |
| float | get_mix_rate()const |
| PackedStringArray | get_output_device_list() |
| float | get_output_latency()const |
| SpeakerMode | get_speaker_mode()const |
| float | get_time_since_last_mix()const |
| float | get_time_to_next_mix()const |
| bool | is_bus_bypassing_effects(bus_idx:int)const |
| bool | is_bus_effect_enabled(bus_idx:int, effect_idx:int)const |
| bool | is_bus_mute(bus_idx:int)const |
| bool | is_bus_solo(bus_idx:int)const |
| bool | is_stream_registered_as_sample(stream:AudioStream) |
| void | lock() |
| void | move_bus(index:int, to_index:int) |
| void | register_stream_as_sample(stream:AudioStream) |
| void | remove_bus(index:int) |
| void | remove_bus_effect(bus_idx:int, effect_idx:int) |
| void | set_bus_bypass_effects(bus_idx:int, enable:bool) |
| void | set_bus_effect_enabled(bus_idx:int, effect_idx:int, enabled:bool) |
| void | set_bus_layout(bus_layout:AudioBusLayout) |
| void | set_bus_mute(bus_idx:int, enable:bool) |
| void | set_bus_name(bus_idx:int, name:String) |
| void | set_bus_send(bus_idx:int, send:StringName) |
| void | set_bus_solo(bus_idx:int, enable:bool) |
| void | set_bus_volume_db(bus_idx:int, volume_db:float) |
| void | set_bus_volume_linear(bus_idx:int, volume_linear:float) |
| void | set_enable_tagging_used_audio_streams(enable:bool) |
| Error | set_input_device_active(active:bool) |
| void | swap_bus_effects(bus_idx:int, effect_idx:int, by_effect_idx:int) |
| void | unlock() |

void
add_bus(at_position:int= -1)
void
add_bus_effect(bus_idx:int, effect:AudioEffect, at_position:int= -1)
AudioBusLayout
generate_bus_layout()const
get_bus_channels(bus_idx:int)const
AudioEffect
get_bus_effect(bus_idx:int, effect_idx:int)
get_bus_effect_count(bus_idx:int)
AudioEffectInstance
get_bus_effect_instance(bus_idx:int, effect_idx:int, channel:int= 0)
get_bus_index(bus_name:StringName)const
String
get_bus_name(bus_idx:int)const
float
get_bus_peak_volume_left_db(bus_idx:int, channel:int)const
float
get_bus_peak_volume_right_db(bus_idx:int, channel:int)const
StringName
get_bus_send(bus_idx:int)const
float
get_bus_volume_db(bus_idx:int)const
float
get_bus_volume_linear(bus_idx:int)const
String
get_driver_name()const
get_input_buffer_length_frames()
PackedStringArray
get_input_device_list()
PackedVector2Array
get_input_frames(frames:int)
get_input_frames_available()
float
get_input_mix_rate()const
float
get_mix_rate()const
PackedStringArray
get_output_device_list()
float
get_output_latency()const
SpeakerMode
get_speaker_mode()const
float
get_time_since_last_mix()const
float
get_time_to_next_mix()const
bool
is_bus_bypassing_effects(bus_idx:int)const
bool
is_bus_effect_enabled(bus_idx:int, effect_idx:int)const
bool
is_bus_mute(bus_idx:int)const
bool
is_bus_solo(bus_idx:int)const
bool
is_stream_registered_as_sample(stream:AudioStream)
void
lock()
void
move_bus(index:int, to_index:int)
void
register_stream_as_sample(stream:AudioStream)
void
remove_bus(index:int)
void
remove_bus_effect(bus_idx:int, effect_idx:int)
void
set_bus_bypass_effects(bus_idx:int, enable:bool)
void
set_bus_effect_enabled(bus_idx:int, effect_idx:int, enabled:bool)
void
set_bus_layout(bus_layout:AudioBusLayout)
void
set_bus_mute(bus_idx:int, enable:bool)
void
set_bus_name(bus_idx:int, name:String)
void
set_bus_send(bus_idx:int, send:StringName)
void
set_bus_solo(bus_idx:int, enable:bool)
void
set_bus_volume_db(bus_idx:int, volume_db:float)
void
set_bus_volume_linear(bus_idx:int, volume_linear:float)
void
set_enable_tagging_used_audio_streams(enable:bool)
Error
set_input_device_active(active:bool)
void
swap_bus_effects(bus_idx:int, effect_idx:int, by_effect_idx:int)
void
unlock()

## Signals
bus_layout_changed()🔗
Emitted when an audio bus is added, deleted, or moved.
bus_renamed(bus_index:int, old_name:StringName, new_name:StringName)🔗
Emitted when the audio bus atbus_indexis renamed fromold_nametonew_name.

## Enumerations
enumSpeakerMode:🔗
SpeakerModeSPEAKER_MODE_STEREO=0
Two or fewer speakers were detected.
SpeakerModeSPEAKER_SURROUND_31=1
A 3.1 channel surround setup was detected.
SpeakerModeSPEAKER_SURROUND_51=2
A 5.1 channel surround setup was detected.
SpeakerModeSPEAKER_SURROUND_71=3
A 7.1 channel surround setup was detected.
enumPlaybackType:🔗
PlaybackTypePLAYBACK_TYPE_DEFAULT=0
Experimental:This constant may be changed or removed in future versions.
The playback will be considered of the type declared atProjectSettings.audio/general/default_playback_type.
PlaybackTypePLAYBACK_TYPE_STREAM=1
Experimental:This constant may be changed or removed in future versions.
Force the playback to be considered as a stream.
PlaybackTypePLAYBACK_TYPE_SAMPLE=2
Experimental:This constant may be changed or removed in future versions.
Force the playback to be considered as a sample. This can provide lower latency and more stable playback (with less risk of audio crackling), at the cost of having less flexibility.
Note:Only currently supported on the web platform.
Note:AudioEffects are not supported when playback is considered as a sample.
PlaybackTypePLAYBACK_TYPE_MAX=3
Experimental:This constant may be changed or removed in future versions.
Represents the size of thePlaybackTypeenum.

## Property Descriptions
intbus_count=1🔗
- voidset_bus_count(value:int)
voidset_bus_count(value:int)
- intget_bus_count()
intget_bus_count()
Number of available audio buses.
Stringinput_device="Default"🔗
- voidset_input_device(value:String)
voidset_input_device(value:String)
- Stringget_input_device()
Stringget_input_device()
Name of the current device for audio input (seeget_input_device_list()). On systems with multiple audio inputs (such as analog, USB and HDMI audio), this can be used to select the audio input device. The value"Default"will record audio on the system-wide default audio input. If an invalid device name is set, the value will be reverted back to"Default".
Note:ProjectSettings.audio/driver/enable_inputmust betruefor audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.
Stringoutput_device="Default"🔗
- voidset_output_device(value:String)
voidset_output_device(value:String)
- Stringget_output_device()
Stringget_output_device()
Name of the current device for audio output (seeget_output_device_list()). On systems with multiple audio outputs (such as analog, USB and HDMI audio), this can be used to select the audio output device. The value"Default"will play audio on the system-wide default audio output. If an invalid device name is set, the value will be reverted back to"Default".
floatplayback_speed_scale=1.0🔗
- voidset_playback_speed_scale(value:float)
voidset_playback_speed_scale(value:float)
- floatget_playback_speed_scale()
floatget_playback_speed_scale()
Scales the rate at which audio is played (i.e. setting it to0.5will make the audio be played at half its speed). See alsoEngine.time_scaleto affect the general simulation speed, which is independent fromplayback_speed_scale.

## Method Descriptions
voidadd_bus(at_position:int= -1)🔗
Adds a bus atat_position.
voidadd_bus_effect(bus_idx:int, effect:AudioEffect, at_position:int= -1)🔗
Adds anAudioEffecteffect to the busbus_idxatat_position.
AudioBusLayoutgenerate_bus_layout()const🔗
Generates anAudioBusLayoutusing the available buses and effects.
intget_bus_channels(bus_idx:int)const🔗
Returns the number of channels of the bus at indexbus_idx.
AudioEffectget_bus_effect(bus_idx:int, effect_idx:int)🔗
Returns theAudioEffectat positioneffect_idxin busbus_idx.
intget_bus_effect_count(bus_idx:int)🔗
Returns the number of effects on the bus atbus_idx.
AudioEffectInstanceget_bus_effect_instance(bus_idx:int, effect_idx:int, channel:int= 0)🔗
Returns theAudioEffectInstanceassigned to the given bus and effect indices (and optionally channel).
intget_bus_index(bus_name:StringName)const🔗
Returns the index of the bus with the namebus_name. Returns-1if no bus with the specified name exist.
Stringget_bus_name(bus_idx:int)const🔗
Returns the name of the bus with the indexbus_idx.
floatget_bus_peak_volume_left_db(bus_idx:int, channel:int)const🔗
Returns the peak volume of the left speaker at bus indexbus_idxand channel indexchannel.
floatget_bus_peak_volume_right_db(bus_idx:int, channel:int)const🔗
Returns the peak volume of the right speaker at bus indexbus_idxand channel indexchannel.
StringNameget_bus_send(bus_idx:int)const🔗
Returns the name of the bus that the bus at indexbus_idxsends to.
floatget_bus_volume_db(bus_idx:int)const🔗
Returns the volume of the bus at indexbus_idxin dB.
floatget_bus_volume_linear(bus_idx:int)const🔗
Returns the volume of the bus at indexbus_idxas a linear value.
Note:The returned value is equivalent to the result of@GlobalScope.db_to_linear()on the result ofget_bus_volume_db().
Stringget_driver_name()const🔗
Returns the name of the current audio driver. The default usually depends on the operating system, but may be overridden via the--audio-drivercommand line argument.--headlessalso automatically sets the audio driver toDummy. See alsoProjectSettings.audio/driver/driver.
intget_input_buffer_length_frames()🔗
Experimental:This method may be changed or removed in future versions.
Returns the absolute size of the microphone input buffer. This is set to a multiple of the audio latency and can be used to estimate the minimum rate at which the frames need to be fetched.
PackedStringArrayget_input_device_list()🔗
Returns the names of all audio input devices detected on the system.
Note:ProjectSettings.audio/driver/enable_inputmust betruefor audio input to work. See also that setting's description for caveats related to permissions and operating system privacy settings.
PackedVector2Arrayget_input_frames(frames:int)🔗
Experimental:This method may be changed or removed in future versions.
Returns aPackedVector2Arraycontaining exactlyframesaudio samples from the internal microphone buffer if available, otherwise returns an emptyPackedVector2Array.
The buffer is filled at the rate ofget_input_mix_rate()frames per second whenset_input_device_active()has successfully been set totrue.
The samples are signed floating-point PCM values between-1and1.
intget_input_frames_available()🔗
Experimental:This method may be changed or removed in future versions.
Returns the number of frames available to read usingget_input_frames().
floatget_input_mix_rate()const🔗
Returns the sample rate at the input of theAudioServer.
floatget_mix_rate()const🔗
Returns the sample rate at the output of theAudioServer.
PackedStringArrayget_output_device_list()🔗
Returns the names of all audio output devices detected on the system.
floatget_output_latency()const🔗
Returns the audio driver's effective output latency. This is based onProjectSettings.audio/driver/output_latency, but the exact returned value will differ depending on the operating system and audio driver.
Note:This can be expensive; it is not recommended to callget_output_latency()every frame.
SpeakerModeget_speaker_mode()const🔗
Returns the speaker configuration.
floatget_time_since_last_mix()const🔗
Returns the relative time since the last mix occurred.
floatget_time_to_next_mix()const🔗
Returns the relative time until the next mix occurs.
boolis_bus_bypassing_effects(bus_idx:int)const🔗
Iftrue, the bus at indexbus_idxis bypassing effects.
boolis_bus_effect_enabled(bus_idx:int, effect_idx:int)const🔗
Iftrue, the effect at indexeffect_idxon the bus at indexbus_idxis enabled.
boolis_bus_mute(bus_idx:int)const🔗
Iftrue, the bus at indexbus_idxis muted.
boolis_bus_solo(bus_idx:int)const🔗
Iftrue, the bus at indexbus_idxis in solo mode.
boolis_stream_registered_as_sample(stream:AudioStream)🔗
Experimental:This method may be changed or removed in future versions.
Iftrue, the stream is registered as a sample. The engine will not have to register it before playing the sample.
Iffalse, the stream will have to be registered before playing it. To prevent lag spikes, register the stream as sample withregister_stream_as_sample().
voidlock()🔗
Locks the audio driver's main loop.
Note:Remember to unlock it afterwards.
voidmove_bus(index:int, to_index:int)🔗
Moves the bus from indexindexto indexto_index.
voidregister_stream_as_sample(stream:AudioStream)🔗
Experimental:This method may be changed or removed in future versions.
Forces the registration of a stream as a sample.
Note:Lag spikes may occur when calling this method, especially on single-threaded builds. It is suggested to call this method while loading assets, where the lag spike could be masked, instead of registering the sample right before it needs to be played.
voidremove_bus(index:int)🔗
Removes the bus at indexindex.
voidremove_bus_effect(bus_idx:int, effect_idx:int)🔗
Removes the effect at indexeffect_idxfrom the bus at indexbus_idx.
voidset_bus_bypass_effects(bus_idx:int, enable:bool)🔗
Iftrue, the bus at indexbus_idxis bypassing effects.
voidset_bus_effect_enabled(bus_idx:int, effect_idx:int, enabled:bool)🔗
Iftrue, the effect at indexeffect_idxon the bus at indexbus_idxis enabled.
voidset_bus_layout(bus_layout:AudioBusLayout)🔗
Overwrites the currently usedAudioBusLayout.
voidset_bus_mute(bus_idx:int, enable:bool)🔗
Iftrue, the bus at indexbus_idxis muted.
voidset_bus_name(bus_idx:int, name:String)🔗
Sets the name of the bus at indexbus_idxtoname.
voidset_bus_send(bus_idx:int, send:StringName)🔗
Connects the output of the bus atbus_idxto the bus namedsend.
voidset_bus_solo(bus_idx:int, enable:bool)🔗
Iftrue, the bus at indexbus_idxis in solo mode.
voidset_bus_volume_db(bus_idx:int, volume_db:float)🔗
Sets the volume in decibels of the bus at indexbus_idxtovolume_db.
voidset_bus_volume_linear(bus_idx:int, volume_linear:float)🔗
Sets the volume as a linear value of the bus at indexbus_idxtovolume_linear.
Note:Using this method is equivalent to callingset_bus_volume_db()with the result of@GlobalScope.linear_to_db()on a value.
voidset_enable_tagging_used_audio_streams(enable:bool)🔗
If set totrue, all instances ofAudioStreamPlaybackwill callAudioStreamPlayback._tag_used_streams()every mix step.
Note:This is enabled by default in the editor, as it is used by editor plugins for the audio stream previews.
Errorset_input_device_active(active:bool)🔗
Experimental:This method may be changed or removed in future versions.
Ifactiveistrue, starts the microphone input stream specified byinput_deviceor returns an error if it failed.
Ifactiveisfalse, stops the input stream if it is running.
voidswap_bus_effects(bus_idx:int, effect_idx:int, by_effect_idx:int)🔗
Swaps the position of two effects in busbus_idx.
voidunlock()🔗
Unlocks the audio driver's main loop. (After locking it, you should always unlock it.)

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.