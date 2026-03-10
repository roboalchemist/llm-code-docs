# Control Audio and Video

Play, pause, seek, and preview audio and video content programmatically using CE.SDK’s playback control APIs.

![Control Audio and Video example showing video playback controls](/docs/cesdk/_astro/browser.hero.C8vI--wL_Z8VMo3.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-create-video-control-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-create-video-control-browser)

CE.SDK provides playback control for audio and video through the Block API. Playback state, seeking, and solo preview are controlled programmatically. Resources must be loaded before accessing metadata like duration and dimensions.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
class Example implements EditorPlugin {  name = packageJson.name;  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Video',      withUploadAssetSources: true    });
    // Create a video scene    await cesdk.createVideoScene();
    const engine = cesdk.engine;
    // Get the page and set to 16:9 landscape for video    const page = engine.block.findByType('page')[0]!;    engine.block.setWidth(page, 1920);    engine.block.setHeight(page, 1080);
    // Create a track for video blocks    const track = engine.block.create('track');    engine.block.appendChild(page, track);
    // Create a video block and add it to the track    const videoUri = 'https://img.ly/static/ubq_video_samples/bbb.mp4';    const videoBlock = engine.block.create('graphic');    engine.block.setShape(videoBlock, engine.block.createShape('rect'));    engine.block.setWidth(videoBlock, 1920);    engine.block.setHeight(videoBlock, 1080);
    // Create and configure video fill    const videoFill = engine.block.createFill('video');    engine.block.setString(videoFill, 'fill/video/fileURI', videoUri);    engine.block.setFill(videoBlock, videoFill);
    // Add to track and set duration    engine.block.appendChild(track, videoBlock);    engine.block.setDuration(videoBlock, 10);
    await engine.block.forceLoadAVResource(videoFill);
    const videoWidth = engine.block.getVideoWidth(videoFill);    const videoHeight = engine.block.getVideoHeight(videoFill);    const totalDuration = engine.block.getAVResourceTotalDuration(videoFill);    console.log(`Video dimensions: ${videoWidth}x${videoHeight}`);    console.log(`Total duration: ${totalDuration}s`);
    if (engine.block.supportsPlaybackControl(page)) {      console.log(`Is playing: ${engine.block.isPlaying(page)}`);      engine.block.setPlaying(page, true);    }
    if (engine.block.supportsPlaybackTime(page)) {      engine.block.setPlaybackTime(page, 1.0);      console.log(`Playback time: ${engine.block.getPlaybackTime(page)}s`);    }
    console.log(      `Visible at current time: ${engine.block.isVisibleAtCurrentPlaybackTime(videoBlock)}`    );
    engine.block.setSoloPlaybackEnabled(videoFill, true);    console.log(      `Solo enabled: ${engine.block.isSoloPlaybackEnabled(videoFill)}`    );    engine.block.setSoloPlaybackEnabled(videoFill, false);
    // Select the video block for inspection    engine.block.select(videoBlock);  }}
export default Example;
```

This guide covers how to play and pause media, seek to specific positions, preview individual blocks with solo mode, check visibility at playback time, and access video resource metadata.

## Force Loading Resources[#](#force-loading-resources)

Media resource metadata is unavailable until the resource is loaded. Call `forceLoadAVResource` on the video fill to ensure dimensions and duration are accessible.

```
await engine.block.forceLoadAVResource(videoFill);
```

Without loading the resource first, accessing properties like duration or dimensions throws an error.

## Getting Video Metadata[#](#getting-video-metadata)

Once the resource is loaded, query the video dimensions and total duration.

```
const videoWidth = engine.block.getVideoWidth(videoFill);const videoHeight = engine.block.getVideoHeight(videoFill);const totalDuration = engine.block.getAVResourceTotalDuration(videoFill);
```

The `getVideoWidth` and `getVideoHeight` methods return the original video dimensions in pixels. The `getAVResourceTotalDuration` method returns the full duration of the source media in seconds.

## Playing and Pausing[#](#playing-and-pausing)

Check if the block supports playback control using `supportsPlaybackControl`, then start or stop playback with `setPlaying`.

```
if (engine.block.supportsPlaybackControl(page)) {  console.log(`Is playing: ${engine.block.isPlaying(page)}`);  engine.block.setPlaying(page, true);}
```

The `isPlaying` method returns the current playback state.

## Seeking[#](#seeking)

To jump to a specific position in the timeline, use `setPlaybackTime`. First, check if the block supports playback time with `supportsPlaybackTime`.

```
if (engine.block.supportsPlaybackTime(page)) {  engine.block.setPlaybackTime(page, 1.0);  console.log(`Playback time: ${engine.block.getPlaybackTime(page)}s`);}
```

Playback time is specified in seconds. The `getPlaybackTime` method returns the current position.

## Visibility at Current Time[#](#visibility-at-current-time)

Check if a block is visible at the current playback position using `isVisibleAtCurrentPlaybackTime`. This is useful when blocks have different time offsets or durations.

```
console.log(  `Visible at current time: ${engine.block.isVisibleAtCurrentPlaybackTime(videoBlock)}`);
```

## Solo Playback[#](#solo-playback)

Solo playback allows you to preview an individual block while the rest of the scene stays frozen. Enable it on a video fill or audio block with `setSoloPlaybackEnabled`.

```
engine.block.setSoloPlaybackEnabled(videoFill, true);console.log(  `Solo enabled: ${engine.block.isSoloPlaybackEnabled(videoFill)}`);engine.block.setSoloPlaybackEnabled(videoFill, false);
```

Enabling solo on one block automatically disables it on all others. This is useful for previewing a specific clip without affecting the overall scene playback.

## Troubleshooting[#](#troubleshooting)

### Properties Unavailable Before Resource Load[#](#properties-unavailable-before-resource-load)

**Symptom**: Accessing duration, dimensions, or trim values throws an error.

**Cause**: Media resource not yet loaded.

**Solution**: Always `await engine.block.forceLoadAVResource()` before accessing these properties.

### Block Not Playing[#](#block-not-playing)

**Symptom**: Calling `setPlaying(true)` has no effect.

**Cause**: Block doesn’t support playback control or scene not in playback mode.

**Solution**: Check `supportsPlaybackControl()` returns true; ensure scene playback is active.

### Solo Playback Not Working[#](#solo-playback-not-working)

**Symptom**: Enabling solo doesn’t isolate the block.

**Cause**: Solo applied to wrong block type or block not visible.

**Solution**: Apply solo to video fills or audio blocks, ensure block is at current playback time.

## Next Steps[#](#next-steps)

*   [Trim Video and Audio](sveltekit/edit-video/trim-4f688b/) \- Control which portion of source media plays
*   [Loop Audio](sveltekit/create-audio/audio/loop-937be7/) \- Enable repeating playback for audio blocks
*   [Adjust Volume](sveltekit/create-video/audio/adjust-volume-7ecc4a/) \- Control audio volume and muting
*   [Adjust Speed](sveltekit/create-video/audio/adjust-speed-908d57/) \- Change playback speed for audio
*   [Video Timeline Overview](sveltekit/create-video/timeline-editor-912252/) \- Timeline editing system

---



[Source](https:/img.ly/docs/cesdk/sveltekit/create-templates/overview-4ebe30)