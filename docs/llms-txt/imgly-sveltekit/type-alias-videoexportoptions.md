# Type Alias: VideoExportOptions

```
type VideoExportOptions = object;
```

Represents the options for exporting a video.

Defines the possible options for exporting a video.

*   ‘mimeType’: The MIME type of the output video file.
*   ‘onProgress’: A callback which reports on the progress of the export.
*   ‘h264Profile’: Determines the encoder feature set and in turn the quality, size and speed of the encoding process.
*   ‘h264Level’: Controls the H.264 encoding level.
*   ‘videoBitrate’: The video bitrate in bits per second.
*   ‘audioBitrate’: The audio bitrate in bits per second.
*   ‘timeOffset’: The time offset in seconds of the scene’s timeline from which the video will start.
*   ‘duration’: The duration in seconds of the final video.
*   ‘framerate’: The target framerate of the exported video in Hz.
*   ‘targetWidth’: An optional target width used in conjunction with target height.
*   ‘targetHeight’: An optional target height used in conjunction with target width.
*   ‘abortSignal’: An abort signal that can be used to cancel the export.

## Properties[#](#properties)

| Property | Type | Default value | Description |
| --- | --- | --- | --- |
| `mimeType?` | [`VideoMimeType`](https://img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/videomimetype/) | `'video/mp4'` | The MIME type of the output video file. |
| `onProgress?` | (`numberOfRenderedFrames`, `numberOfEncodedFrames`, `totalNumberOfFrames`) => `void` | `undefined` | A callback which reports on the progress of the export. |
| `h264Profile?` | `number` | `77 (Main)` | Determines the encoder feature set and in turn the quality, size and speed of the encoding process. |
| `h264Level?` | `number` | `52` | Controls the H.264 encoding level. This relates to parameters used by the encoder such as bit rate, timings and motion vectors. Defined by the spec are levels 1.0 up to 6.2. To arrive at an integer value, the level is multiplied by ten. E.g. to get level 5.2, pass a value of 52. |
| `videoBitrate?` | `number` | `undefined` | The video bitrate in bits per second. Maximum bitrate is determined by h264Profile and h264Level. If the value is 0, the bitrate is automatically determined by the engine. |
| `audioBitrate?` | `number` | `undefined` | The audio bitrate in bits per second. If the value is 0, the bitrate is automatically determined by the engine (128kbps for stereo AAC stream). |
| `timeOffset?` | `number` | `0` | The time offset in seconds of the scene’s timeline from which the video will start. |
| `duration?` | `number` | `The duration of the scene.` | The duration in seconds of the final video. |
| `framerate?` | `number` | `30` | The target framerate of the exported video in Hz. |
| `targetWidth?` | `number` | `undefined` | An optional target width used in conjunction with target height. If used, the block will be rendered large enough, that it fills the target size entirely while maintaining its aspect ratio. |
| `targetHeight?` | `number` | `undefined` | An optional target height used in conjunction with target width. If used, the block will be rendered large enough, that it fills the target size entirely while maintaining its aspect ratio. |
| `allowTextOverhang?` | `boolean` | `false` | If true, the export will include text bounding boxes that account for glyph overhangs. When enabled, text blocks with glyphs that extend beyond their frame (e.g., decorative fonts with swashes) will be exported with the full glyph bounds visible, preventing text clipping. |
| `abortSignal?` | `AbortSignal` | `undefined` | An abortsignal that can be used to cancel the export. |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/verticalblockalignment)