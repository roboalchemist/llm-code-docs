# Insert Audio

Add audio files to video projects using CE.SDK’s audio block system for background music, sound effects, and voiceovers.

![Insert Audio example showing audio block in the timeline](/docs/cesdk/_astro/browser.hero.CIePCc9t_1WzYPC.webp)

8 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-insert-media-audio-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-insert-media-audio-browser)

Audio blocks are timeline elements that play sound alongside video content. Unlike video fills that attach to graphic blocks, audio blocks exist independently on the timeline with their own duration, position, and volume controls. Audio requires Video scene mode.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Insert Audio Guide * * Demonstrates adding audio to video projects: * - Creating audio blocks programmatically * - Setting audio source URIs * - Configuring timeline position and duration * - Adjusting audio volume, mute, and loop settings * - Querying and managing audio blocks */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Initialize CE.SDK with Video mode for audio support    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Video',      withUploadAssetSources: true    });    await cesdk.createVideoScene();
    const engine = cesdk.engine;    const page = engine.scene.getCurrentPage();    if (page == null) {      throw new Error('No page found in scene');    }
    // Set page dimensions for video (16:9)    engine.block.setWidth(page, 1920);    engine.block.setHeight(page, 1080);
    // Set page duration for timeline    engine.block.setDuration(page, 30);
    // Create an audio block and set source    const audioUri =      'https://cdn.img.ly/assets/demo/v3/ly.img.audio/audios/far_from_home.m4a';    const audioBlock = engine.block.create('audio');    engine.block.setString(audioBlock, 'audio/fileURI', audioUri);    engine.block.appendChild(page, audioBlock);
    // Load audio resource to access duration    await engine.block.forceLoadAVResource(audioBlock);    const totalDuration = engine.block.getAVResourceTotalDuration(audioBlock);    console.log('Audio total duration:', totalDuration, 'seconds');
    engine.block.setTimeOffset(audioBlock, 0);    engine.block.setDuration(audioBlock, Math.min(totalDuration, 30));
    engine.block.setVolume(audioBlock, 0.8);    const currentVolume = engine.block.getVolume(audioBlock);    console.log('Audio volume:', currentVolume);
    engine.block.setMuted(audioBlock, false);    const isMuted = engine.block.isMuted(audioBlock);    console.log('Audio muted:', isMuted);
    engine.block.setLooping(audioBlock, false);    const isLooping = engine.block.isLooping(audioBlock);    console.log('Audio looping:', isLooping);
    const allAudioBlocks = engine.block.findByType('audio');    console.log('Total audio blocks:', allAudioBlocks.length);
    // Log information about each audio block    allAudioBlocks.forEach((block, index) => {      const uri = engine.block.getString(block, 'audio/fileURI');      const timeOffset = engine.block.getTimeOffset(block);      const duration = engine.block.getDuration(block);      const volume = engine.block.getVolume(block);
      console.log(`Audio block ${index + 1}:`, {        uri: uri.split('/').pop(),        timeOffset: `${timeOffset}s`,        duration: `${duration}s`,        volume: `${(volume * 100).toFixed(0)}%`      });    });
    // Create a second audio block to demonstrate removal    const tempAudioBlock = engine.block.create('audio');    engine.block.appendChild(page, tempAudioBlock);
    engine.block.destroy(tempAudioBlock);
    console.log(      'Insert Audio guide initialized. Open the timeline to see audio tracks.'    );  }}
export default Example;
```

This guide covers creating audio blocks, configuring timeline properties, controlling playback settings, and managing audio blocks in your scene.

## Creating an Audio Block[#](#creating-an-audio-block)

We create audio blocks using `engine.block.create('audio')` and set the source file with the `audio/fileURI` property. Audio blocks must be appended to a page to appear on the timeline.

```
const audioBlock = engine.block.create('audio');engine.block.setString(audioBlock, 'audio/fileURI', audioUri);engine.block.appendChild(page, audioBlock);
```

CE.SDK supports WAV and MP4 audio formats (including `.m4a` files). The source URI can point to any accessible URL.

## Configuring Timeline Position[#](#configuring-timeline-position)

Audio blocks have timeline properties that control when and how long they play. We use `setTimeOffset()` for the start position and `setDuration()` for playback length.

```
engine.block.setTimeOffset(audioBlock, 0);engine.block.setDuration(audioBlock, Math.min(totalDuration, 30));
```

The `forceLoadAVResource()` method loads the audio file so we can access its total duration. Use `getAVResourceTotalDuration()` to get the full length of the source audio for timeline calculations.

## Adjusting Volume[#](#adjusting-volume)

We set volume using `setVolume()` with values from 0.0 (silent) to 1.0 (full volume). This affects both preview playback and the final exported output.

```
engine.block.setVolume(audioBlock, 0.8);const currentVolume = engine.block.getVolume(audioBlock);
```

## Muting Audio[#](#muting-audio)

To temporarily silence audio without removing it, use `setMuted()`. This preserves all other properties while stopping sound output.

```
engine.block.setMuted(audioBlock, false);const isMuted = engine.block.isMuted(audioBlock);
```

## Looping Audio[#](#looping-audio)

Enable continuous playback with `setLooping()`. When enabled, the audio repeats until the end of the block’s duration on the timeline.

```
engine.block.setLooping(audioBlock, false);const isLooping = engine.block.isLooping(audioBlock);
```

## Finding Audio Blocks[#](#finding-audio-blocks)

Use `findByType('audio')` to retrieve all audio blocks in the scene. This is useful for building audio management interfaces or performing batch operations.

```
const allAudioBlocks = engine.block.findByType('audio');
```

## Removing Audio[#](#removing-audio)

To remove an audio block, call `destroy()`. This removes the block from the scene and frees its resources.

```
engine.block.destroy(tempAudioBlock);
```

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.block.create('audio')` | Create a new audio block |
| `engine.block.setString(block, 'audio/fileURI', uri)` | Set the audio source file |
| `engine.block.appendChild(parent, child)` | Add audio block to page/timeline |
| `engine.block.forceLoadAVResource(block)` | Force load the audio file |
| `engine.block.getAVResourceTotalDuration(block)` | Get total audio duration in seconds |
| `engine.block.setTimeOffset(block, seconds)` | Set timeline start position |
| `engine.block.setDuration(block, seconds)` | Set playback duration |
| `engine.block.setVolume(block, volume)` | Set volume (0.0-1.0) |
| `engine.block.getVolume(block)` | Get current volume |
| `engine.block.setMuted(block, muted)` | Mute or unmute audio |
| `engine.block.isMuted(block)` | Check if audio is muted |
| `engine.block.setLooping(block, loop)` | Enable/disable looping |
| `engine.block.isLooping(block)` | Check if looping is enabled |
| `engine.block.findByType('audio')` | Find all audio blocks |
| `engine.block.destroy(block)` | Remove audio block from scene |

## Next Steps[#](#next-steps)

[Insert Media Overview](sveltekit/overview-491658/) \- Learn about adding different media types to your projects

[Split Video](sveltekit/edit-video/split-464167/) \- Split video clips on the timeline

[Load Scene](sveltekit/open-the-editor/load-scene-478833/) \- Save and reload your scenes with audio

[Store Custom Metadata](sveltekit/export-save-publish/store-custom-metadata-337248/) \- Save custom data with your scenes

---



[Source](https:/img.ly/docs/cesdk/sveltekit/prebuilt-solutions/t-shirt-designer-02b48f)