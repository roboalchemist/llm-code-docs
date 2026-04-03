# AudioStreamPlayback in English

# AudioStreamPlayback
Inherits:RefCounted<Object
Inherited By:AudioStreamPlaybackInteractive,AudioStreamPlaybackPlaylist,AudioStreamPlaybackPolyphonic,AudioStreamPlaybackResampled,AudioStreamPlaybackSynchronized
Meta class for playing back audio.

## Description
Can play, loop, pause a scroll through audio. SeeAudioStreamandAudioStreamOggVorbisfor usage.

## Tutorials
- Audio Generator Demo
Audio Generator Demo

## Methods

| int | _get_loop_count()virtualconst |
|---|---|
| Variant | _get_parameter(name:StringName)virtualconst |
| float | _get_playback_position()virtualrequiredconst |
| bool | _is_playing()virtualrequiredconst |
| int | _mix(buffer:AudioFrame*, rate_scale:float, frames:int)virtualrequired |
| void | _seek(position:float)virtual |
| void | _set_parameter(name:StringName, value:Variant)virtual |
| void | _start(from_pos:float)virtualrequired |
| void | _stop()virtualrequired |
| void | _tag_used_streams()virtual |
| int | get_loop_count()const |
| float | get_playback_position()const |
| AudioSamplePlayback | get_sample_playback()const |
| bool | is_playing()const |
| PackedVector2Array | mix_audio(rate_scale:float, frames:int) |
| void | seek(time:float= 0.0) |
| void | set_sample_playback(playback_sample:AudioSamplePlayback) |
| void | start(from_pos:float= 0.0) |
| void | stop() |

_get_loop_count()virtualconst
Variant
_get_parameter(name:StringName)virtualconst
float
_get_playback_position()virtualrequiredconst
bool
_is_playing()virtualrequiredconst
_mix(buffer:AudioFrame*, rate_scale:float, frames:int)virtualrequired
void
_seek(position:float)virtual
void
_set_parameter(name:StringName, value:Variant)virtual
void
_start(from_pos:float)virtualrequired
void
_stop()virtualrequired
void
_tag_used_streams()virtual
get_loop_count()const
float
get_playback_position()const
AudioSamplePlayback
get_sample_playback()const
bool
is_playing()const
PackedVector2Array
mix_audio(rate_scale:float, frames:int)
void
seek(time:float= 0.0)
void
set_sample_playback(playback_sample:AudioSamplePlayback)
void
start(from_pos:float= 0.0)
void
stop()

## Method Descriptions
int_get_loop_count()virtualconst🔗
Overridable method. Should return how many times this audio stream has looped. Most built-in playbacks always return0.
Variant_get_parameter(name:StringName)virtualconst🔗
Return the current value of a playback parameter by name (seeAudioStream._get_parameter_list()).
float_get_playback_position()virtualrequiredconst🔗
Overridable method. Should return the current progress along the audio stream, in seconds.
bool_is_playing()virtualrequiredconst🔗
Overridable method. Should returntrueif this playback is active and playing its audio stream.
int_mix(buffer:AudioFrame*, rate_scale:float, frames:int)virtualrequired🔗
Override this method to customize how the audio stream is mixed. This method is called even if the playback is not active.
Note:It is not useful to override this method in GDScript or C#. Only GDExtension can take advantage of it.
void_seek(position:float)virtual🔗
Override this method to customize what happens when seeking this audio stream at the givenposition, such as by callingAudioStreamPlayer.seek().
void_set_parameter(name:StringName, value:Variant)virtual🔗
Set the current value of a playback parameter by name (seeAudioStream._get_parameter_list()).
void_start(from_pos:float)virtualrequired🔗
Override this method to customize what happens when the playback starts at the given position, such as by callingAudioStreamPlayer.play().
void_stop()virtualrequired🔗
Override this method to customize what happens when the playback is stopped, such as by callingAudioStreamPlayer.stop().
void_tag_used_streams()virtual🔗
Overridable method. Called whenever the audio stream is mixed if the playback is active andAudioServer.set_enable_tagging_used_audio_streams()has been set totrue. Editor plugins may use this method to "tag" the current position along the audio stream and display it in a preview.
intget_loop_count()const🔗
Returns the number of times the stream has looped.
floatget_playback_position()const🔗
Returns the current position in the stream, in seconds.
AudioSamplePlaybackget_sample_playback()const🔗
Experimental:This method may be changed or removed in future versions.
Returns theAudioSamplePlaybackassociated with thisAudioStreamPlaybackfor playing back the audio sample of this stream.
boolis_playing()const🔗
Returnstrueif the stream is playing.
PackedVector2Arraymix_audio(rate_scale:float, frames:int)🔗
Mixes up toframesof audio from the stream from the current position, at a rate ofrate_scale, advancing the stream.
Returns aPackedVector2Arraywhere each element holds the left and right channel volume levels of each frame.
Note:Can return fewer frames than requested, make sure to use the size of the return value.
voidseek(time:float= 0.0)🔗
Seeks the stream at the giventime, in seconds.
voidset_sample_playback(playback_sample:AudioSamplePlayback)🔗
Experimental:This method may be changed or removed in future versions.
AssociatesAudioSamplePlaybackto thisAudioStreamPlaybackfor playing back the audio sample of this stream.
voidstart(from_pos:float= 0.0)🔗
Starts the stream from the givenfrom_pos, in seconds.
voidstop()🔗
Stops the stream.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.