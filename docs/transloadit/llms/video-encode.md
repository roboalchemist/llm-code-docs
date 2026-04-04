# Source: https://transloadit.com/docs/robots/video-encode.md

The /video/encode Robot is a versatile tool for video processing that handles transcoding, resizing, and watermarking. It supports various formats including modern standards like HEVC (H.265), and provides features such as presets for common devices, custom FFmpeg parameters for powerusers, watermark positioning, and more.

## Adding text overlays with FFmpeg

You can add text overlays to videos using FFmpeg's `drawtext` filter through this Robot's `ffmpeg` parameter. Here are two examples — one with the default font and one with a custom font family name:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{
  "steps": {
    ":original": {
      "robot": "/upload/handle"
    },
    "text_overlay_default": {
      "use": ":original",
      "robot": "/video/encode",
      "preset": "empty",
      "ffmpeg_stack": "{{stacks.ffmpeg.recommended_version}}",
      "ffmpeg": {
        "codec:a": "copy",
        "vf": "drawtext=text='My text overlay':fontcolor=white:fontsize=24:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2"
      },
      "result": true
    },
    "text_overlay_custom": {
      "use": ":original",
      "robot": "/video/encode",
      "preset": "empty",
      "ffmpeg_stack": "{{stacks.ffmpeg.recommended_version}}",
      "ffmpeg": {
        "codec:a": "copy",
        "vf": "drawtext=font='Times New Roman':text='My text overlay':fontcolor=white:fontsize=24:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2"
      },
      "result": true
    }
  }
}

```

**Notes:**

* Use the `font` attribute to reference a font by family name with FFmpeg's `drawtext`
* FFmpeg font family names typically do not contain dashes (e.g. `Times New Roman`), while ImageMagick uses dashed names (e.g. `Times-New-Roman`).
* Preserve the source audio by setting `"codec:a": "copy"`.
* Position text with the `x` and `y` expressions. The example above centers the text.

See the live demo [here](/demos/video-encoding/add-text-overlay/).
