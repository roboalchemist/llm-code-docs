# AudioStreamGeneratorPlayback

# AudioStreamGeneratorPlayback

Inherits:AudioStreamPlaybackResampled<AudioStreamPlayback<RefCounted<Object
Plays back audio generated usingAudioStreamGenerator.

## Description

This class is meant to be used withAudioStreamGeneratorto play back the generated audio in real-time.

## Tutorials

- Audio Generator Demo
Audio Generator Demo
- Godot 3.2 will get new audio features
Godot 3.2 will get new audio features

## Methods

| bool | can_push_buffer(amount:int)const |
|---|---|
| void | clear_buffer() |
| int | get_frames_available()const |
| int | get_skips()const |
| bool | push_buffer(frames:PackedVector2Array) |
| bool | push_frame(frame:Vector2) |

bool
can_push_buffer(amount:int)const
void
clear_buffer()
get_frames_available()const
get_skips()const
bool
push_buffer(frames:PackedVector2Array)
bool
push_frame(frame:Vector2)

## Method Descriptions

boolcan_push_buffer(amount:int)const🔗
Returnstrueif a buffer of the sizeamountcan be pushed to the audio sample data buffer without overflowing it,falseotherwise.
voidclear_buffer()🔗
Clears the audio sample data buffer.
intget_frames_available()const🔗
Returns the number of frames that can be pushed to the audio sample data buffer without overflowing it. If the result is0, the buffer is full.
intget_skips()const🔗
Returns the number of times the playback skipped due to a buffer underrun in the audio sample data. This value is reset at the start of the playback.
boolpush_buffer(frames:PackedVector2Array)🔗
Pushes several audio data frames to the buffer. This is usually more efficient thanpush_frame()in C# and compiled languages via GDExtension, butpush_buffer()may belessefficient in GDScript.
boolpush_frame(frame:Vector2)🔗
Pushes a single audio data frame to the buffer. This is usually less efficient thanpush_buffer()in C# and compiled languages via GDExtension, butpush_frame()may bemoreefficient in GDScript.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
