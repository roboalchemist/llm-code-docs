# Insert Videos

Insert videos into your CE.SDK scenes using either the convenience API or manual block creation with video fills.

![Insert Videos example showing the CE.SDK editor with video insertion buttons](/docs/cesdk/_astro/browser.hero.CRoxG2l5_2eCaNO.webp)

8 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-insert-media-videos-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-insert-media-videos-browser)

Videos in CE.SDK are graphic blocks with video fills. Two approaches exist: the `addVideo()` method for Video mode scenes, and manual block creation with video fills which works in any scene mode.

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Insert Videos Guide * * Demonstrates inserting videos into a CE.SDK scene: * - Using the addVideo() convenience API (Video mode only) * - Using graphic blocks with video fills (works in any mode) * - Configuring trim offset and trim length */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (cesdk == null) {      throw new Error('CE.SDK instance is required for this plugin');    }
    cesdk.feature.enable('ly.img.video');    await cesdk.createVideoScene();
    const engine = cesdk.engine;
    // Videos from the ly.img.video demo asset source    const surferVideoUrl =      'https://cdn.img.ly/assets/demo/v3/ly.img.video/videos/pexels-drone-footage-of-a-surfer-barrelling-a-wave-12715991.mp4';    const laptopVideoUrl =      'https://cdn.img.ly/assets/demo/v3/ly.img.video/videos/pexels-tony-schnagl-5528015.mp4';
    const page = engine.scene.getCurrentPage();    if (page == null) return;
    // Get page dimensions for responsive layout    const pageWidth = engine.block.getWidth(page);    const pageHeight = engine.block.getHeight(page);
    // Layout: videos span width with margins, each takes half height    const margin = 40;    const gap = 20;    const videoWidth = pageWidth - margin * 2;    const videoHeight = (pageHeight - margin * 2 - gap) / 2;
    const videoBlock = await engine.block.addVideo(      surferVideoUrl,      videoWidth,      videoHeight    );    engine.block.setPositionX(videoBlock, margin);    engine.block.setPositionY(videoBlock, margin);
    const block = engine.block.create('graphic');    engine.block.setShape(block, engine.block.createShape('rect'));    const fill = engine.block.createFill('video');    engine.block.setString(fill, 'fill/video/fileURI', laptopVideoUrl);    engine.block.setFill(block, fill);
    engine.block.setWidth(block, videoWidth);    engine.block.setHeight(block, videoHeight);    engine.block.setPositionX(block, margin);    engine.block.setPositionY(block, margin + videoHeight + gap);    engine.block.appendChild(page, block);
    // Force load the first video's resource for thumbnails    const videoBlockFill = engine.block.getFill(videoBlock);    await engine.block.forceLoadAVResource(videoBlockFill);
    await engine.block.forceLoadAVResource(fill);    engine.block.setTrimOffset(fill, 2.0);    engine.block.setTrimLength(fill, 5.0);
    const duration = engine.block.getAVResourceTotalDuration(fill);    console.log(`Video duration: ${duration}s, playing 2-7s`);
    // Set playback time to 1 second for hero image capture    engine.block.setPlaybackTime(page, 1.0);
    // Wait a moment for thumbnails to generate    await new Promise((resolve) => setTimeout(resolve, 1000));
    // Enable zoom auto-fit to keep the page in view    engine.scene.enableZoomAutoFit(page, 'Both', 40, 40, 40, 40);
    // Select the page for a cleaner hero image    engine.block.select(page);  }}
export default Example;
```

This guide covers how to insert videos using the UI, add videos programmatically, and configure video properties like trim offset and length.

## Insert Videos Using the UI[#](#insert-videos-using-the-ui)

Users can upload videos through the Upload menu in the asset panel or by dragging and dropping video files directly onto the canvas. CE.SDK supports MP4 (H.264) and WebM (VP8/VP9) formats.

After inserting a video, users can move it by dragging, resize it with corner handles, trim it using timeline controls, and crop it to show specific portions.

## Setup[#](#setup)

Enable video features and create a Video mode scene. Video mode is required for the `addVideo()` convenience API.

```
cesdk.feature.enable('ly.img.video');await cesdk.createVideoScene();
```

The `createVideoScene()` method creates a scene optimized for video editing with timeline support.

## Add Videos with addVideo()[#](#add-videos-with-addvideo)

The `addVideo()` method creates a graphic block with video fill in a single call. This is the simplest approach in Video mode.

```
const videoBlock = await engine.block.addVideo(  surferVideoUrl,  videoWidth,  videoHeight);engine.block.setPositionX(videoBlock, margin);engine.block.setPositionY(videoBlock, margin);
```

Pass the video URL, width, and height as parameters. The method returns the block ID for further manipulation like positioning.

The `addVideo()` API only works in Video mode. Use manual block creation for Design mode scenes.

## Add Videos with Graphic Blocks[#](#add-videos-with-graphic-blocks)

For more control or when working in Design mode, manually create a graphic block and attach a video fill.

```
const block = engine.block.create('graphic');engine.block.setShape(block, engine.block.createShape('rect'));const fill = engine.block.createFill('video');engine.block.setString(fill, 'fill/video/fileURI', laptopVideoUrl);engine.block.setFill(block, fill);
```

Create a graphic block, attach a rectangular shape, create a video fill with the source URI, and apply the fill to the block. This pattern mirrors image fills.

## Configure Trim Settings[#](#configure-trim-settings)

Control which portion of a video plays by setting the trim offset and length. First load the video resource to access duration metadata.

```
await engine.block.forceLoadAVResource(fill);engine.block.setTrimOffset(fill, 2.0);engine.block.setTrimLength(fill, 5.0);
```

The `setTrimOffset()` method specifies where playback starts. A value of 2.0 skips the first two seconds. The `setTrimLength()` method defines how long the clip plays from that offset.

Trim operations are applied to the fill, not the block. Use `getFill()` to get the fill ID first.

## Supported Video Formats[#](#supported-video-formats)

CE.SDK supports common web video formats:

*   **MP4 (H.264 codec)** — widest browser support, recommended for most use cases
*   **WebM (VP8/VP9 codec)** — open format with good compression

For maximum compatibility, use MP4 with H.264 encoding.

## Troubleshooting[#](#troubleshooting)

### Video Not Visible[#](#video-not-visible)

*   Verify the file URI is correct and accessible
*   Ensure the video format is supported (MP4, WebM)
*   Check that the block is appended to the page with `appendChild()`
*   Confirm dimensions are set with `setWidth()` and `setHeight()`

### Trim Not Working[#](#trim-not-working)

*   Ensure you’re calling trim methods on the fill, not the block
*   Call `forceLoadAVResource()` before setting trim values
*   Verify trim offset + trim length doesn’t exceed total duration

### addVideo() Throws Error[#](#addvideo-throws-error)

*   The `addVideo()` API only works in Video mode
*   Create a video scene with `createVideoScene()` first
*   Use manual block creation for Design mode scenes

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `block.addVideo(url, width, height)` | Create video block in Video mode |
| `block.create('graphic')` | Create graphic block container |
| `block.createShape('rect')` | Create rectangular shape |
| `block.setShape(block, shape)` | Apply shape to block |
| `block.createFill('video')` | Create video fill |
| `block.setString(fill, 'fill/video/fileURI', url)` | Set video source URI |
| `block.setFill(block, fill)` | Apply fill to block |
| `block.forceLoadAVResource(fill)` | Load video metadata |
| `block.getAVResourceTotalDuration(fill)` | Get video duration in seconds |
| `block.setTrimOffset(fill, seconds)` | Set trim start point |
| `block.setTrimLength(fill, seconds)` | Set trim duration |

## Next Steps[#](#next-steps)

*   [Create video projects](sveltekit/create-video/overview-b06512/) with timeline editing
*   [Apply filters and effects](sveltekit/filters-and-effects/apply-2764e4/) to enhance appearance
*   [Export your design](sveltekit/export-save-publish/export/overview-9ed3a8/) to various formats

---



[Source](https:/img.ly/docs/cesdk/sveltekit/insert-media/shapes-or-stickers-20ac68)