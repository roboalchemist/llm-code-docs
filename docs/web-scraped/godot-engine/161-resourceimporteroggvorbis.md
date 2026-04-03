# ResourceImporterOggVorbis

# ResourceImporterOggVorbis

Inherits:ResourceImporter<RefCounted<Object
Imports an Ogg Vorbis audio file for playback.

## Description

Ogg Vorbis is a lossy audio format, with better audio quality compared toResourceImporterMP3at a given bitrate.
In most cases, it's recommended to use Ogg Vorbis over MP3. However, if you're using an MP3 sound source with no higher quality source available, then it's recommended to use the MP3 file directly to avoid double lossy compression.
Ogg Vorbis requires more CPU to decode thanResourceImporterWAV. If you need to play a lot of simultaneous sounds, it's recommended to use WAV for those sounds instead, especially if targeting low-end devices.

## Tutorials

- Importing audio samples
Importing audio samples

## Properties

| int | bar_beats | 4 |
|---|---|---|
| int | beat_count | 0 |
| float | bpm | 0 |
| bool | loop | false |
| float | loop_offset | 0 |

bar_beats
beat_count
float
bool
loop
false
float
loop_offset

## Methods

| AudioStreamOggVorbis | load_from_buffer(stream_data:PackedByteArray)static |
|---|---|
| AudioStreamOggVorbis | load_from_file(path:String)static |

AudioStreamOggVorbis
load_from_buffer(stream_data:PackedByteArray)static
AudioStreamOggVorbis
load_from_file(path:String)static

## Property Descriptions

intbar_beats=4🔗
The number of bars within a single beat in the audio track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.
A more convenient editor forbar_beatsis provided in theAdvanced Import Settingsdialog, as it lets you preview your changes without having to reimport the audio.
intbeat_count=0🔗
The beat count of the audio track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.
A more convenient editor forbeat_countis provided in theAdvanced Import Settingsdialog, as it lets you preview your changes without having to reimport the audio.
floatbpm=0🔗
The beats per minute of the audio track. This should match the BPM measure that was used to compose the track. This is only relevant for music that wishes to make use of interactive music functionality, not sound effects.
A more convenient editor forbpmis provided in theAdvanced Import Settingsdialog, as it lets you preview your changes without having to reimport the audio.
boolloop=false🔗
If enabled, the audio will begin playing at the beginning after playback ends by reaching the end of the audio.
Note:InAudioStreamPlayer, theAudioStreamPlayer.finishedsignal won't be emitted for looping audio when it reaches the end of the audio file, as the audio will keep playing indefinitely.
floatloop_offset=0🔗
Determines where audio will start to loop after playback reaches the end of the audio. This can be used to only loop a part of the audio file, which is useful for some ambient sounds or music. The value is determined in seconds relative to the beginning of the audio. A value of0.0will loop the entire audio file.
Only has an effect ifloopistrue.
A more convenient editor forloop_offsetis provided in theAdvanced Import Settingsdialog, as it lets you preview your changes without having to reimport the audio.

## Method Descriptions

AudioStreamOggVorbisload_from_buffer(stream_data:PackedByteArray)static🔗
Deprecated:UseAudioStreamOggVorbis.load_from_buffer()instead.
Creates a newAudioStreamOggVorbisinstance from the given buffer. The buffer must contain Ogg Vorbis data.
AudioStreamOggVorbisload_from_file(path:String)static🔗
Deprecated:UseAudioStreamOggVorbis.load_from_file()instead.
Creates a newAudioStreamOggVorbisinstance from the given file path. The file must be in Ogg Vorbis format.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
