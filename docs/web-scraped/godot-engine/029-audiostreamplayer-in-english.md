# AudioStreamPlayer in English

# AudioStreamPlayer
Inherits:Node<Object
A node for audio playback.

## Description
TheAudioStreamPlayernode plays an audio stream non-positionally. It is ideal for user interfaces, menus, or background music.
To use this node,streamneeds to be set to a validAudioStreamresource. Playing more than one sound at the same time is also supported, seemax_polyphony.
If you need to play audio at a specific position, useAudioStreamPlayer2DorAudioStreamPlayer3Dinstead.

## Tutorials
- Audio streams
Audio streams
- 2D Dodge The Creeps Demo
2D Dodge The Creeps Demo
- Audio Device Changer Demo
Audio Device Changer Demo
- Audio Generator Demo
Audio Generator Demo
- Audio Microphone Record Demo
Audio Microphone Record Demo
- Audio Spectrum Visualizer Demo
Audio Spectrum Visualizer Demo

## Properties

| bool | autoplay | false |
|---|---|---|
| StringName | bus | &"Master" |
| int | max_polyphony | 1 |
| MixTarget | mix_target | 0 |
| float | pitch_scale | 1.0 |
| PlaybackType | playback_type | 0 |
| bool | playing | false |
| AudioStream | stream |  |
| bool | stream_paused | false |
| float | volume_db | 0.0 |
| float | volume_linear |  |

bool
autoplay
false
StringName
&"Master"
max_polyphony
MixTarget
mix_target
float
pitch_scale
PlaybackType
playback_type
bool
playing
false
AudioStream
stream
bool
stream_paused
false
float
volume_db
float
volume_linear

## Methods

| float | get_playback_position() |
|---|---|
| AudioStreamPlayback | get_stream_playback() |
| bool | has_stream_playback() |
| void | play(from_position:float= 0.0) |
| void | seek(to_position:float) |
| void | stop() |

float
get_playback_position()
AudioStreamPlayback
get_stream_playback()
bool
has_stream_playback()
void
play(from_position:float= 0.0)
void
seek(to_position:float)
void
stop()

## Signals
finished()🔗
Emitted when a sound finishes playing without interruptions. This signal isnotemitted when callingstop(), or when exiting the tree while sounds are playing.

## Enumerations
enumMixTarget:🔗
MixTargetMIX_TARGET_STEREO=0
The audio will be played only on the first channel. This is the default.
MixTargetMIX_TARGET_SURROUND=1
The audio will be played on all surround channels.
MixTargetMIX_TARGET_CENTER=2
The audio will be played on the second channel, which is usually the center.

## Property Descriptions
boolautoplay=false🔗
- voidset_autoplay(value:bool)
voidset_autoplay(value:bool)
- boolis_autoplay_enabled()
boolis_autoplay_enabled()
Iftrue, this node callsplay()when entering the tree.
StringNamebus=&"Master"🔗
- voidset_bus(value:StringName)
voidset_bus(value:StringName)
- StringNameget_bus()
StringNameget_bus()
The target bus name. All sounds from this node will be playing on this bus.
Note:At runtime, if no bus with the given name exists, all sounds will fall back on"Master". See alsoAudioServer.get_bus_name().
intmax_polyphony=1🔗
- voidset_max_polyphony(value:int)
voidset_max_polyphony(value:int)
- intget_max_polyphony()
intget_max_polyphony()
The maximum number of sounds this node can play at the same time. Callingplay()after this value is reached will cut off the oldest sounds.
MixTargetmix_target=0🔗
- voidset_mix_target(value:MixTarget)
voidset_mix_target(value:MixTarget)
- MixTargetget_mix_target()
MixTargetget_mix_target()
The mix target channels. Has no effect when two speakers or less are detected (seeSpeakerMode).
floatpitch_scale=1.0🔗
- voidset_pitch_scale(value:float)
voidset_pitch_scale(value:float)
- floatget_pitch_scale()
floatget_pitch_scale()
The audio's pitch and tempo, as a multiplier of thestream's sample rate. A value of2.0doubles the audio's pitch, while a value of0.5halves the pitch.
PlaybackTypeplayback_type=0🔗
- voidset_playback_type(value:PlaybackType)
voidset_playback_type(value:PlaybackType)
- PlaybackTypeget_playback_type()
PlaybackTypeget_playback_type()
Experimental:This property may be changed or removed in future versions.
The playback type of the stream player. If set other than to the default value, it will force that playback type.
boolplaying=false🔗
- voidset_playing(value:bool)
voidset_playing(value:bool)
- boolis_playing()
boolis_playing()
Iftrue, this node is playing sounds. Setting this property has the same effect asplay()andstop().
AudioStreamstream🔗
- voidset_stream(value:AudioStream)
voidset_stream(value:AudioStream)
- AudioStreamget_stream()
AudioStreamget_stream()
TheAudioStreamresource to be played. Setting this property stops all currently playing sounds. If left empty, theAudioStreamPlayerdoes not work.
boolstream_paused=false🔗
- voidset_stream_paused(value:bool)
voidset_stream_paused(value:bool)
- boolget_stream_paused()
boolget_stream_paused()
Iftrue, the sounds are paused. Settingstream_pausedtofalseresumes all sounds.
Note:This property is automatically changed when exiting or entering the tree, or this node is paused (seeNode.process_mode).
floatvolume_db=0.0🔗
- voidset_volume_db(value:float)
voidset_volume_db(value:float)
- floatget_volume_db()
floatget_volume_db()
Volume of sound, in decibels. This is an offset of thestream's volume.
Note:To convert between decibel and linear energy (like most volume sliders do), usevolume_linear, or@GlobalScope.db_to_linear()and@GlobalScope.linear_to_db().
floatvolume_linear🔗
- voidset_volume_linear(value:float)
voidset_volume_linear(value:float)
- floatget_volume_linear()
floatget_volume_linear()
Volume of sound, as a linear value.
Note:This member modifiesvolume_dbfor convenience. The returned value is equivalent to the result of@GlobalScope.db_to_linear()onvolume_db. Setting this member is equivalent to settingvolume_dbto the result of@GlobalScope.linear_to_db()on a value.

## Method Descriptions
floatget_playback_position()🔗
Returns the position in theAudioStreamof the latest sound, in seconds. Returns0.0if no sounds are playing.
Note:The position is not always accurate, as theAudioServerdoes not mix audio every processed frame. To get more accurate results, addAudioServer.get_time_since_last_mix()to the returned position.
Note:This method always returns0.0if thestreamis anAudioStreamInteractive, since it can have multiple clips playing at once.
AudioStreamPlaybackget_stream_playback()🔗
Returns the latestAudioStreamPlaybackof this node, usually the most recently created byplay(). If no sounds are playing, this method fails and returns an empty playback.
boolhas_stream_playback()🔗
Returnstrueif any sound is active, even ifstream_pausedis set totrue. See alsoplayingandget_stream_playback().
voidplay(from_position:float= 0.0)🔗
Plays a sound from the beginning, or the givenfrom_positionin seconds.
voidseek(to_position:float)🔗
Restarts all sounds to be played from the givento_position, in seconds. Does nothing if no sounds are playing.
voidstop()🔗
Stops all sounds from this node.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.