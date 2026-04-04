# AudioStreamPolyphonic in English

# AudioStreamPolyphonic

Inherits:AudioStream<Resource<RefCounted<Object
AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.

## Description

AudioStream that lets the user play custom streams at any time from code, simultaneously using a single player.
Playback control is done via theAudioStreamPlaybackPolyphonicinstance set inside the player, which can be obtained viaAudioStreamPlayer.get_stream_playback(),AudioStreamPlayer2D.get_stream_playback()orAudioStreamPlayer3D.get_stream_playback()methods. Obtaining the playback instance is only valid after thestreamproperty is set as anAudioStreamPolyphonicin those players.

## Properties

| int | polyphony | 32 |

polyphony

## Property Descriptions

intpolyphony=32🔗

- voidset_polyphony(value:int)
voidset_polyphony(value:int)
- intget_polyphony()
intget_polyphony()
Maximum amount of simultaneous streams that can be played.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
