# Audio

The **CreativeEditor (CE.SDK)** provides different **audio features** you can leverage in web-based apps. This section covers how to **add audio blocks**, **extract** audio from videos, control **playback**, generate **waveforms**, and manage **multi-track audio**.

## Use Cases[#](#use-cases)

Use the CE.SDK audio features when you need to create:

*   Background music
*   Voice-overs
*   Sound effects
*   Podcasts

## How Audio Works in the CE.SDK[#](#how-audio-works-in-the-cesdk)

The CE.SDK represents audio as audio blocks.

Each block has:

*   Source (file or extracted track)
    
*   Playback properties (time, speed, volume, mute)
    
*   Timeline properties (offset, duration, trim length)
    
*   Optional waveform thumbnails for UI visualization
    

### What Are the Timeline Properties[#](#what-are-the-timeline-properties)

Each audio block has properties that determine when and how much of the sound plays:

*   **Offset:** the delay before an audio block begins playing inside the scene timeline.
    
*   **Trim length**: cuts the audio to keep only a specific part of it.
    
*   **Duration**: defines how long the audio plays.
    

### What Are Waveforms[#](#what-are-waveforms)

Waveforms are **visual representations** of the audio signal over time. They show the amplitude (volume level) of the sound at each moment, using peaks and valleys.

The CE.SDK can generate sampled waveform data that you can render in your UI. This is especially helpful for editing tools.

### When to Create VS. Extract Audio[#](#when-to-create-vs-extract-audio)

The CE.SDK allows you to either create a blank audio block or extract the audio from a video.

*   **Create an empty audio block** when you want to add external or standalone audio that doesn’t come from a video.
    
*   **Extract the audio** when it comes from a video block already in your scene.
    

## CE.SDK Audio Features Overview[#](#cesdk-audio-features-overview)

The table below summarizes the main audio-related capabilities in CE.SDK.  
Each feature is related to an example further down the page.

| **Category** | **Action** | **API Name** | **Notes** |
| --- | --- | --- | --- |
| **Create Audio Blocks** | Create empty audio block | `create` | Creates an audio block with no source. |
|  | Extract audio from video | `createAudioFromVideo` | Requires a video block ID and track index. |
| **Playback Control** | Set playback position | `setPlaybackTime` | Time in seconds. |
|  | Volume | `setVolume` | Range `0.0–1.0`. |
|  | Mute | `setMuted` | Boolean. |
|  | Playback speed | `setPlaybackSpeed` | Range `0.25–3.0`. |
| **Timeline Management** | Offset | `setTimeOffset` | To move the playback starting point in the scene timeline. |
|  | Duration | `setDuration` | Total length (seconds). |
|  | Trim length | `setTrimLength` | Cuts content to a defined length. |
| **Replace Audio Source** | Reload edited scene | `scene.loadFromString` | Used when replacing audio at runtime. |
| **Waveforms** | Generate thumbnails | `generateAudioThumbnailSequence` | Produces waveform sample data for UI. |
| **Export Audio** | Export WAV | `exportAudio` | MIME type: `audio/wav`. |
|  | Export MP4 | `exportAudio` | MIME type: `audio/mp4`. |

## Examples[#](#examples)

Find in the following list of examples different API calls listed in the preceding table.

### Create Audio[#](#create-audio)

[

Create Audio

](#tab-panel-281)[

Extract Audio from a Video

](#tab-panel-282)[

Add Audio Sources

](#tab-panel-283)[

Export

](#tab-panel-284)

To create an empty audio block, use:

```
const blockId = engine.block.create('audio');
```

Use `engine.block.createAudioFromVideo(blockId, trackIndex: number);`.

This example:

1.  Extracts the first audio track (1) from a video.
2.  Appends it to the page for further manipulation.

`videoBlockId` and `pageId` must refer to existing blocks.

```
const audioBlockId = engine.block.createAudioFromVideo(videoBlockId, 0);// Attach to the page so it’s part of the sceneengine.block.appendChild(pageId, audioBlockId);
```

This example:

1.  Creates an audio block.
2.  Attaches the audio block to the page.
3.  Sets the source for the audio from a remote URL.

`pageId` must refer to an existing page.

```
// Create an audio block  const audioBlockId = engine.block.create('audio');  await engine.block.appendChild(pageId, audioBlockId);  engine.block.setString(    audioBlockId,    'audio/fileURI',    'https://cdn.img.ly/assets/demo/v1/ly.img.audio/audios/far_from_home.m4a'  );
```

For details on loading sources, check [the dedicated guide](sveltekit/import-media/from-remote-source/unsplash-8f31f0/) .

This example exports the audio block in **mp4** format:

`blockId` must refer to an existing audio block.

```
engine.block.exportAudio(blockId, {  mymeType: 'audio/mp4'  });
```

This example exports the audio in **wav** format:

```
const audioData = await engine.block.exportAudio(blockId, {  mimeType: 'audio/wav'  });
```

### Control Audio Playback[#](#control-audio-playback)

[

Basic Playback Control

](#tab-panel-277)[

Volume

](#tab-panel-278)[

Mute

](#tab-panel-279)[

Speed

](#tab-panel-280)

Use `engine.block.setPlaybackTime(blockId, time: number)`.

This example sets the current playback at 3 seconds:

```
engine.block.setPlaybackTime(blockId, 3)
```

Use `engine.block.setVolume(blockId, volume: number);`.

This example sets the volume at 1 (max value):

```
engine.block.setVolume(blockId, 1);
```

Use `engine.block.setMuted(blockId, muted: boolean);`.

This example mutes the audio of the block:

```
engine.block.setMuted(blockId, true);
```

Use `engine.block.setPlaybackSpeed(blockId, speed: number);`.

This example multiplies the speed by 0.25:

```
engine.block.setPlaybackSpeed(blockId, 0.25);
```

### Manage Audio Timeline[#](#manage-audio-timeline)

[

Offset

](#tab-panel-285)[

Duration

](#tab-panel-286)[

Trimming

](#tab-panel-287)[

Generate Audio Thumbnails

](#tab-panel-288)

If the audio has an offset of:

*   0 s → It plays immediately when the scene starts.
    
*   2 s → The CE.SDK waits 2 seconds before playing it.
    
*   10 s → The audio only starts at the 10-second mark.
    

Use `engine.block.setTimeOffset(blockId, offset: number)`.

This example starts the audio at 2 s on the timeline:

```
engine.block.setTimeOffset(blockId, 2);
```

Use `engine.block.setDuration(blockId, duration: number)`.

This example sets the audio duration for 300 seconds:

```
engine.block.setDuration(blockId, 300)
```

Use `engine.block.setTrimLength(blockId, length: number);`.

This example creates a new trim that:

1.  Starts at the second 2 of the audio content.
2.  Plays for 10 seconds.

```
engine.block.setTrimOffset(blockId, 2)engine.block.setTrimLength(blockId, 10);
```

Use:

```
engine.block.generateAudioThumbnailSequence(  blockId,  samplesPerChunk: number,  timeBegin: number,  timeEnd: number,  numberOfSamples: number,  numberOfChannels: number)
```

This example generates 1 audio sample that:

*   Produces 3 chunks of this sample.
*   Start at second 8.
*   End at second 18.
*   Is stereo audio (1 for mono, 2 for stereo)

`audioBlockId` must refer to an existing block.

```
const audioThumbnail = engine.block.generateAudioThumbnailSequence(  audioBlockId,  3,   // samplesPerChunk  8,   // timeBegin  18,  // timeEnd  1,   // numberOfSamples  2,   // numberOfChannels  // Return the result  (chunkIndex, result) => {    if (result instanceof Error) {    console.error('Thumbnail chunk failed', result);    audioThumbnail();    return;    }    console.log(`Chunk ${chunkIndex}`, result);  });
```

Once generated, integrate the waveform into your UI.

## Next Steps[#](#next-steps)

For each feature’s detailed instructions and options:

*   Explore the [CE.SDK API options](sveltekit/api-reference/overview-8f24e1/) .
*   Check the dedicated guides in the audio section.

---



[Source](https:/img.ly/docs/cesdk/sveltekit/conversion/to-png-f1660c)