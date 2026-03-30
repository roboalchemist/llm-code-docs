# Video and Audio Timeline Web Editor

The CreativeEditor SDK (CE.SDK) offers features for editing the video timeline, the horizontal layout where you arrange video, audio, and effects in the sequence they play. This tutorial will help you create advanced video editing tools for high-quality video exports.

This tutorial focuses on the user interface components. For programmatic timeline manipulation, refer to the [Video Overview](vue/create-video/overview-b06512/) guide.

## When to Use[#](#when-to-use)

Use the CE.SDK timeline features in web applications that incorporate the following tools:

*   Video montages
*   Marketing video editing
*   Social media content creation

## What You’ll Learn[#](#what-youll-learn)

This tutorial will show you how to:

*   The video timeline works.
*   To create video scenes.
*   To manage video layers (tracks).
*   To edit a clip’s duration and offset.
*   To manage video playback.
*   To generate and display video thumbnails.

## How the Timeline Works[#](#how-the-timeline-works)

This tutorial refers to the timeline, which is the horizontal area below the video editing canvas. The video timeline displays:

*   All clips on parallel tracks
*   A playhead for navigation
*   Controls for playback and editing

 ![Default CE.SDK Editor on Video Mode](/docs/cesdk/_astro/browser-cesdk-video-mode.CH_BlHSH_Z1Stxl4.png)

Use the visual timeline for editing actions like:

*   Arranging clips along a time axis to control when each element **appears**.
*   Trimming clips to change their duration.
*   Layer content visually.

### Activate CE.SDK Video Mode[#](#activate-cesdk-video-mode)

To work with the CE.SDK Editor in video mode, specify the scene’s design as follows:

```
cesdk.addDefaultAssetSources(),cesdk.addDemoAssetSources({ sceneMode: 'Video' }),await cesdk.createVideoScene();
```

This tells the CreativeEditor:

*   To use the Video editing mode (rather than the Design one).
*   To load demo video assets to test the editor.
*   To create a video scene, ready for editing.

### Open/Close the Timeline Editing area[#](#openclose-the-timeline-editing-area)

The default CreativeEditor settings display the timeline when launching the UI.

Close it to increase canvas space when the scene doesn’t need timeline editing. To close it, click the **Timeline** toggle:

 ![CE.SDK timeline UI with collapse toggle highlighted](/docs/cesdk/_astro/browser-collapse-timeline.DEja8UsZ_Z1SUePY.png)

To open it and access the visual timeline editing tools, click the same toggle:

 ![CE.SDK timeline UI with expanded toggle highlighted](/docs/cesdk/_astro/browser-expand-timeline.C8cUt1iq_Z10IQko.png)

### Timeline Structure[#](#timeline-structure)

The timeline’s structure in the CE.SDK is the following:

1.  Scene (root block)
2.  Pages (as video segments)
3.  Tracks (as parallel layers)
4.  Clips (as graphic blocks)

### Track Structure[#](#track-structure)

The track is a container that handles the content layer. The timeline organizes content into three track types:

*   Clip tracks (for video content)
*   Overlay track (for text and graphics over the video)
*   Audio tracks

 ![Two clips layered over audio and text](/docs/cesdk/_astro/browser-tracks.DX8QdV-Q_pOhht.png)

The order in which track appears determines its position in the scene:

*   Moving a track to the top brings it to the front of the scene.
*   Moving a track to the bottom of the timeline sends the content the back of the scene.

 ![Clip 3 on top of clip 1 and clip 2 and behind the title](/docs/cesdk/_astro/browser-layering.DF1AxLA8_1OVs34.png)

### Control the Content Position[#](#control-the-content-position)

You can adjust the position of the content using the vertical playhead line, which indicates the current playhead time. The playhead moves along the timeline, displaying the time code.

Change the playhead position (when the clip starts playing) by either:

*   Clicking on any area in the time ruler.
*   Dragging the playhead with your cursor.

 ![Current play time, dragged playhead and dragging zone](/docs/cesdk/_astro/browser-timeline-drag.rjT8vWhl_Z1SQsMz.png)

### Scroll and Zoom on the Timeline[#](#scroll-and-zoom-on-the-timeline)

Adjust the time scale to increase the level of details per frame:

1.  Click anywhere in the timeline area.
2.  Zoom into the timeline using:
    *   Keyboard shortcuts
    *   A mouse
    *   A trackpad

When zoomed in, the clip stretches visually—each pixel now represents fewer milliseconds—so you can fine-tune edits frame by frame.

 ![Unzoomed timeline VS zoomed timeline](/docs/cesdk/_astro/browser-zoom.DH0XgN7J_16HwOu.png)

## Control How the Clips Play[#](#control-how-the-clips-play)

### Play/Pause the Scene[#](#playpause-the-scene)

The playback bar contains:

*   The **play/pause button** that plays the clip from the current playhead position.
*   A **loop toggle** that repeats the video when activated.
*   The **current timestamp**

 ![CE.SDK playback bar](/docs/cesdk/_astro/browser-play-bar.C73i1VUz_ZQmi6v.png)

The scene plays while synchronizing:

*   All videos
*   Overlays
*   Audio

### Preview Frames[#](#preview-frames)

Drag and drop (scrub) the playhead back and forth to preview frames without playing the clip in real time. This allows you to quickly find the exact moment you want to edit.

 ![Frame preview at 0:4:8](/docs/cesdk/_astro/browser-timeline-scrub.66cQ7f97_2qgKIJ.png)

The timestamp is the current playhead time in HH:MM:SS:FF format.

 ![Frame preview at 0:4:8](/docs/cesdk/_astro/browser-timeline-scrub-timestamp.CP8roXss_ZEmUyb.png)

## Edit Video Clips[#](#edit-video-clips)

The CreativeEditor’s timeline allows users to visually edit clips and scenes in the browser. This section lists all timeline editing features.

### Select Clips[#](#select-clips)

Before editing any clip, you need to select it to apply modifications to it. To **select a clip**, click it either:

*   From the page
*   From the timeline

 ![Clip selected in CE.SDK UI](/docs/cesdk/_astro/browser-clip-select.kNn7LUDr_2c5A5x.png)

Selecting multiple clips at once is available either:

*   With cursor clicks on each clip while holding modifier keys.
*   By drawing a frame in the scene with the cursor.

Selecting a clip reveals editing handles to:

*   Crop the clip.
*   Flip the clip.
*   Trim the clip.

 ![2 clips selected at once](/docs/cesdk/_astro/browser-multiselect.VlsjTgoc_Z1F7I7g.png)

### Edit Clip’s Duration[#](#edit-clips-duration)

In the timeline, selected clips show drag handles at their beginning and end. Use these handles based on your goals:

*   Trim the clip from the beginning: use the left handle (at the start of the clip).
*   Trim the clip from the end: use the right handle (at the end of the clip).

This operation is called **“trimming” a clip**. As you move the clip, its position on the timeline automatically updates. Trimming shortens the clip, and the cut portions:

*   Don’t play anymore.
*   Disappear from the timeline.

### Split Clips[#](#split-clips)

The Split Control splits the selected clip into two separate clips at the playhead.

 ![Clip split in 2 separate clips](/docs/cesdk/_astro/browser-timeline-split.ciC14j-1_1do0N0.png)

Each resulting clip is then independently editable. **Splitting doesn’t remove any part of the original content.**

## Add Content to the Scene[#](#add-content-to-the-scene)

Once you’ve edited the clips, you can add more elements to the scene to customize it further, such as:

*   Additional clips
*   Audio tracks
*   Graphics and text

### Add Another Clip[#](#add-another-clip)

The web version of the CreativeEditor allows you to add more clips to the scene in two ways:

*   By clicking the “Add Clip” button:
    
    1.  Opens the video assets gallery.
    2.  Automatically adds any selected clips from the gallery to the timeline.
*   By dragging and dropping from your computer to either:
    
    1.  The page
    2.  The timeline

Dragging the clip highlights the zone before dropping it.

 ![Clip being dragged to the page and clip being dragged to the timeline in the CE.SDK Editor UI](/docs/cesdk/_astro/browser-drag-n-drop.CiKsL8r1_ZMsdtz.png)

The choice of the zone makes no difference: the clip’s position is automatically set at the beginning of the timeline. You can then reposition and edit it as needed.

### Add Audio and Overlays[#](#add-audio-and-overlays)

Furthermore, there are two types of content that you can incorporate into the setting:

*   Overlays (text, images, stickers)
*   Audio

**Add the new content** to the scene by either:

*   Clicking the kind of content to add from the **lateral menu**.
*   Using the **drag and drop** feature from your computer or another source.

 ![Lateral menu highlighting Uploads, Images, Audio, Text and Stickers](/docs/cesdk/_astro/browser-add-content.Du0Z9An7_Z2rMo7E.png)

Each type of content appears automatically on its own track, at the start of the timeline.

## Arrange Clips[#](#arrange-clips)

Use the CreativeEditor UI’s timeline to edit:

*   The order in which clips appear.
*   Each clip starting point.
*   Using advanced settings.

### Reorder Clips[#](#reorder-clips)

Drag clips along the horizontal axis to move them earlier or later in the timeline. This makes a clip’s order relative to the other clip change.

The CreativeEditor enhances visual clip arrangement in the timeline by:

*   Auto-adjusting positions to prevent overlapping clips on the same track.
*   Showing the clip’s predicted position using drop indicators.

 ![Timeline containing 2 clips, the second one being dragged along the horizontal axis](/docs/cesdk/_astro/browser-clips-arrange.BIEi6mag_20EOUB.png)

### Edit the Clip’s Starting Point[#](#edit-the-clips-starting-point)

Each clip’s position along the horizontal axis indicates its start time in the composition. To change the start time of a clip, drag it either:

*   Left to make it start **earlier**.
*   Right to make it start **later**.

Gaps between clips display as empty frames showing the background color when the scene plays.

 ![CE.SDK timeline showing an orange background color within a gap between 2 clips](/docs/cesdk/_astro/browser-clips-gap.CyaeN2c3_Z110uJu.png)

### Change the Background color[#](#change-the-background-color)

To change the background color, click the **Background** button on the left side of the play bar.

 ![CE.SDK timeline with background color button highlighted](/docs/cesdk/_astro/browser-background-color.DA2Gegxw_ZVl7oN.png)

This action opens a full color editing menu to customize:

*   Color settings (RGB, CMYK, Hex, Hue)
*   Transparency
*   Solid or gradients
*   Color picking from the scene

This menu provides an option to **deactivate the background** as well. Deactivating the background makes the scene play on a transparent background.

## Configure the Timeline[#](#configure-the-timeline)

### Activate/Deactivate the Timeline[#](#activatedeactivate-the-timeline)

The CreativeEditor SDK ships a UI with the timeline editor activated. To change the settings and deactivate the timeline , use the `ly.img.video.timeline` feature flag:

[

Enable the timeline

](#tab-panel-365)[

Deactivate the timeline

](#tab-panel-366)[

Conditionally show the timeline

](#tab-panel-367)

```
// Enable the timeline (default for video scenes)cesdk.feature.enable('ly.img.video.timeline');
```

```
// Disable the timeline for a simplified interfacecesdk.feature.disable('ly.img.video.timeline');
```

Pass the option to selectively hide the timeline unless the scene is in **Video Mode**:

```
// Only show timeline when in Video mode (this is the default behavior)cesdk.feature.set('ly.img.video.timeline', ({ engine }) => {  return engine.scene.getMode() === 'Video';});
cesdk.feature.set('ly.img.video.controls.split', ({ engine }) => {  const selected = engine.block.findAllSelected();  return selected.length === 1;});
```

### Hide or Show Tracks[#](#hide-or-show-tracks)

Simplify the CreativeEditor interface by leveraging the track visibility settings. Hide or display tracks based on specific use cases.

[

Video tracks

](#tab-panel-368)[

Overlays tracks

](#tab-panel-369)[

Audio tracks

](#tab-panel-370)[

All

](#tab-panel-371)

**Enable** video features with:

```
cesdk.feature.enable('ly.img.video.clips');
```

**Hide** video feature with:

```
cesdk.feature.disable('ly.img.video.clips');
```

This will hide

**Display** overlays tracks with:

```
cesdk.feature.enable('ly.img.video.overlays');
```

**Hide** overlay tracks with:

```
cesdk.feature.disable('ly.img.video.overlays');
```

**Display** audio tracks with:

```
cesdk.feature.enable('ly.img.video.audio');
```

**Hide** audio tracks with:

```
cesdk.feature.disable('ly.img.video.audio');
```

**Display** all tracks with:

```
cesdk.feature.enable([  'ly.img.video.clips',  'ly.img.video.overlays',  'ly.img.video.audio']);
```

**Hide** all tracks with:

```
cesdk.feature.disable([  'ly.img.video.clips',  'ly.img.video.overlays',  'ly.img.video.audio']);
```

### Configure the Play Bar[#](#configure-the-play-bar)

Simplify the play bar by hiding or displaying controls in the UI:

[

Play bar

](#tab-panel-362)[

Loop control

](#tab-panel-363)[

Zoom

](#tab-panel-364)

**Display** the play bar with:

```
cesdk.feature.enable('ly.img.video.controls.playback');
```

**Hide** the play bar with:

```
cesdk.feature.disable('ly.img.video.controls.playback');
```

**Display** the loop control with:

```
cesdk.feature.enable('ly.img.video.controls.loop');
```

**Hide** the loop control with:

```
cesdk.feature.disable('ly.img.video.controls.loop');
```

**Display** the zoom on the timeline with:

```
cesdk.feature.enable('ly.img.video.controls.timelineZoom');
```

**Hide** the zoom into the timeline with:

```
cesdk.feature.disable('ly.img.video.controls.timelineZoom');
```

### Fine-tune Editing Actions[#](#fine-tune-editing-actions)

Restrict or allow editing actions by hiding or displaying the editing controls:

[

Split

](#tab-panel-372)[

Add Clip button

](#tab-panel-373)[

Background button

](#tab-panel-374)[

Global Settings

](#tab-panel-375)

**Hide** the split button with:

```
cesdk.feature.disable('ly.img.video.controls.split');
```

**Hide** the **Add Clip** button with:

```
cesdk.feature.disable('ly.img.video.addClip');
```

**Hide** the background button with:

```
cesdk.feature.disable('ly.img.video.controls.background');
```

**Activate** all video features at once using global patterns with `/*`:

```
// Enable all video featurescesdk.feature.enable('ly.img.video.*');
```

Or **deactivate** video features at once:

```
// Disable all video control featurescesdk.feature.disable('ly.img.video.*');
```

### Activate Features Dynamically[#](#activate-features-dynamically)

You can activate or deactivate timeline features dynamically, instead of hard-coding their **on/off** state.

The following example detects the scene state:

*   When a clip is selected, it activates the Split button.
*   When nothing is selected, it hides the Split button.

```
// Disable split control when nothing is selectedcesdk.feature.set('ly.img.video.controls.split', ({ engine }) => {  const selected = engine.block.findAllSelected();  return selected.length === 1;});
```

### Feature Reference[#](#feature-reference)

| Feature ID | Description |
| --- | --- |
| `ly.img.video.timeline` | Show or hide the entire timeline panel |
| `ly.img.video.clips` | Show or hide the video clips track |
| `ly.img.video.overlays` | Show or hide the overlay track |
| `ly.img.video.audio` | Show or hide the audio track |
| `ly.img.video.addClip` | Enable or disable adding new clips |
| `ly.img.video.controls` | Base feature for all video controls |
| `ly.img.video.controls.toggle` | Show or hide timeline collapse/expand button |
| `ly.img.video.controls.playback` | Show or hide play/pause and timestamp |
| `ly.img.video.controls.loop` | Show or hide loop toggle |
| `ly.img.video.controls.split` | Show or hide split clip control |
| `ly.img.video.controls.background` | Show or hide background color controls |
| `ly.img.video.controls.timelineZoom` | Show or hide zoom controls |

## Troubleshooting[#](#troubleshooting)

| Issue | Solution |
| --- | --- |
| Timeline not displaying | ・ Verify the scene is in video mode.  
・ Check that `ly.img.video.timeline` feature is enabled. |
| Trim handles not displaying | ・ Click the clip first to reveal handles.  
・ Check if the clip contains video/audio content. |
| Play not starting | ・ Ensure the video has loaded.  
・ Check the browser console for codec errors.  
・ Check that the playhead falls within the page duration. |
| Split not working | ・ Check that you’ve selected the clip to split.  
・ Check that the playhead is within the selected clip’s duration  
. Make sure you’ve enabled `ly.img.video.controls.split`. |

## Next Steps[#](#next-steps)

*   [Trim Video Clips](vue/edit-video/trim-4f688b/) — Detailed trimming techniques, including frame-accurate editing.
*   [Control Audio and Video](vue/create-video/control-daba54/) — Master volume, playback speed, and timing.
*   [Activate or Deactivate Features](vue/user-interface/customization/disable-or-enable-f058e2/) \- Full feature flag reference.
*   [Compress and Export the Video](vue/export-save-publish/export/compress-29105e/) .

---



[Source](https:/img.ly/docs/cesdk/vue/create-video/overview-b06512)