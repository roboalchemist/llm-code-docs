# VideoStreamPlayer

# VideoStreamPlayer

Inherits:Control<CanvasItem<Node<Object
A control used for video playback.

## Description

A control used for playback ofVideoStreamresources.
Supported video formats areOgg Theora(.ogv,VideoStreamTheora) and any format exposed via a GDExtension plugin.
Warning:On Web, video playbackwillperform poorly due to missing architecture-specific assembly optimizations.

## Tutorials

- Playing videos
Playing videos

## Properties

| int | audio_track | 0 |
|---|---|---|
| bool | autoplay | false |
| int | buffering_msec | 500 |
| StringName | bus | &"Master" |
| bool | expand | false |
| bool | loop | false |
| bool | paused | false |
| float | speed_scale | 1.0 |
| VideoStream | stream |  |
| float | stream_position |  |
| float | volume |  |
| float | volume_db | 0.0 |

audio_track
bool
autoplay
false
buffering_msec
StringName
&"Master"
bool
expand
false
bool
loop
false
bool
paused
false
float
speed_scale
VideoStream
stream
float
stream_position
float
volume
float
volume_db

## Methods

| float | get_stream_length()const |
|---|---|
| String | get_stream_name()const |
| Texture2D | get_video_texture()const |
| bool | is_playing()const |
| void | play() |
| void | stop() |

float
get_stream_length()const
String
get_stream_name()const
Texture2D
get_video_texture()const
bool
is_playing()const
void
play()
void
stop()

## Signals

finished()🔗
Emitted when playback is finished.

## Property Descriptions

intaudio_track=0🔗

- voidset_audio_track(value:int)
voidset_audio_track(value:int)
- intget_audio_track()
intget_audio_track()
The embedded audio track to play.
boolautoplay=false🔗
- voidset_autoplay(value:bool)
voidset_autoplay(value:bool)
- boolhas_autoplay()
boolhas_autoplay()
Iftrue, playback starts when the scene loads.
intbuffering_msec=500🔗
- voidset_buffering_msec(value:int)
voidset_buffering_msec(value:int)
- intget_buffering_msec()
intget_buffering_msec()
Amount of time in milliseconds to store in buffer while playing.
StringNamebus=&"Master"🔗
- voidset_bus(value:StringName)
voidset_bus(value:StringName)
- StringNameget_bus()
StringNameget_bus()
Audio bus to use for sound playback.
boolexpand=false🔗
- voidset_expand(value:bool)
voidset_expand(value:bool)
- boolhas_expand()
boolhas_expand()
Iftrue, the video scales to the control size. Otherwise, the control minimum size will be automatically adjusted to match the video stream's dimensions.
boolloop=false🔗
- voidset_loop(value:bool)
voidset_loop(value:bool)
- boolhas_loop()
boolhas_loop()
Iftrue, the video restarts when it reaches its end.
boolpaused=false🔗
- voidset_paused(value:bool)
voidset_paused(value:bool)
- boolis_paused()
boolis_paused()
Iftrue, the video is paused.
floatspeed_scale=1.0🔗
- voidset_speed_scale(value:float)
voidset_speed_scale(value:float)
- floatget_speed_scale()
floatget_speed_scale()
The stream's current speed scale.1.0is the normal speed, while2.0is double speed and0.5is half speed. A speed scale of0.0pauses the video, similar to settingpausedtotrue.
VideoStreamstream🔗
- voidset_stream(value:VideoStream)
voidset_stream(value:VideoStream)
- VideoStreamget_stream()
VideoStreamget_stream()
The assigned video stream. See description for supported formats.
floatstream_position🔗
- voidset_stream_position(value:float)
voidset_stream_position(value:float)
- floatget_stream_position()
floatget_stream_position()
The current position of the stream, in seconds.
floatvolume🔗
- voidset_volume(value:float)
voidset_volume(value:float)
- floatget_volume()
floatget_volume()
Audio volume as a linear value.
floatvolume_db=0.0🔗
- voidset_volume_db(value:float)
voidset_volume_db(value:float)
- floatget_volume_db()
floatget_volume_db()
Audio volume in dB.

## Method Descriptions

floatget_stream_length()const🔗
The length of the current stream, in seconds.
Stringget_stream_name()const🔗
Returns the video stream's name, or"<NoStream>"if no video stream is assigned.
Texture2Dget_video_texture()const🔗
Returns the current frame as aTexture2D.
boolis_playing()const🔗
Returnstrueif the video is playing.
Note:The video is still considered playing if paused during playback.
voidplay()🔗
Starts the video playback from the beginning. If the video is paused, this will not unpause the video.
voidstop()🔗
Stops the video playback and sets the stream position to 0.
Note:Although the stream position will be set to 0, the first frame of the video stream won't become the current frame.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
