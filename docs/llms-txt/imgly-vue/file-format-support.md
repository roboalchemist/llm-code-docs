# File Format Support

CreativeEditor SDK (CE.SDK) supports a wide range of modern file types for importing assets and exporting final content. Whether you’re working with images, videos, audio, documents, or fonts, CE.SDK provides a client-side editing environment with excellent media compatibility and performance—optimized for modern client-side hardware.

This guide outlines supported formats, codecs, and known limitations across media types.

## Importing Media[#](#importing-media)

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png`, `.jpeg`, `.jpg`, `.gif`, `.webp`, `.svg`, `.bmp` |
| **Video** | `.mp4` (H.264/AVC, H.265/HEVC), `.mov` (H.264/AVC, H.265/HEVC), `.webm` (VP8, VP9, AV1) |
| **Audio** | `.mp3`, `.m4a`, `.mp4` (AAC or MP3), `.mov` (AAC or MP3) |
| **Animation** | `.json` (Lottie) |

Need to import a format not listed here? CE.SDK allows you to create custom importers for any file type by using our Scene and Block APIs programmatically.

### SVG Limitations[#](#svg-limitations)

CE.SDK uses Skia for SVG parsing and rendering. While most SVG files render correctly, there are some important limitations to be aware of:

### Text Elements[#](#text-elements)

*   SVG text elements are not supported - any text in SVG files will not be rendered.
*   Convert text to paths in your vector editor before exporting if text is needed.

### Styling Limitations[#](#styling-limitations)

*   CSS styles included in SVGs are not supported - use presentation attributes instead.
*   RGBA color syntax is not supported - use `fill-opacity` and `stroke-opacity` attributes.
*   When exporting SVGs from design tools, choose the “presentation attributes” option.

### Unsupported SVG Elements[#](#unsupported-svg-elements)

The following SVG elements are not supported:

*   Animation elements (`<animate>`)
*   Foreign object (`<foreignObject>`)
*   Text-related elements (`<altGlyph>`, `<font>`, `<glyph>`)
*   Script elements (`<script>`)
*   Some filter elements (`<feComponentTransfer>`, `<feConvolveMatrix>`, `<feTile>`, `<feDropShadow>`)
*   Inlined SVGs via `<image>` or `<feImage>` elements

## Exporting Media[#](#exporting-media)

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png` (with transparency), `.jpeg`, `.webp`, `.tga` |
| **Video** | `.mp4` (H.264 or H.265 on supported platforms with limited transparency support) |
| **Print** | `.pdf` (supports underlayer printing and spot colors) |
| **Scene** | `.scene` (description of the scene without any assets) |
| **Archive** | `.zip` (fully self-contained archive that bundles the `.scene` file with all assets) |

Our custom cross-platform C++ based rendering and layout engine ensures consistent output quality across devices.

## Importing Templates[#](#importing-templates)

| Format | Description |
| --- | --- |
| `.idml` | InDesign |
| `.psd` | Photoshop |
| `.scene` | CE.SDK Native |

Need to import a format not listed here? CE.SDK allows you to create custom importers for any file type by using our Scene and Block APIs to generate scenes programmatically.

## Font Formats[#](#font-formats)

| Format | Description |
| --- | --- |
| `.ttf` | TrueType Font |
| `.otf` | OpenType Font |
| `.woff` | Web Open Font Format |
| `.woff2` | Compressed Web Open Font Format 2 |

Fonts should be appropriately licensed before being embedded in your application.

## Video & Audio Codecs[#](#video--audio-codecs)

CE.SDK supports the most widely adopted video and audio codecs to ensure compatibility across platforms:

### **Video Codecs**[#](#video-codecs)

*   **H.264 / AVC** (in `.mp4`)
*   **H.265 / HEVC** (in `.mp4`, may require platform-specific support)

### **Audio Codecs**[#](#audio-codecs)

*   **MP3** (in `.mp3` or within `.mp4`)
*   **AAC** (in `.m4a` or within `.mp4` or `.mov`)

## Size Limits[#](#size-limits)

### Image Resolution Limits[#](#image-resolution-limits)

| Constraint | Recommendation / Limit |
| --- | --- |
| **Input Resolution** | Maximum input resolution is **4096×4096 pixels**. Images from external sources (e.g., Unsplash) are resized to this size before rendering on the canvas. You can modify this value using the `maxImageSize` setting. |
| **Output Resolution** | There is no enforced output resolution limit. Theoretically, the editor supports output sizes up to **16,384×16,384 pixels**. However, practical limits depend on the device’s GPU capabilities and available memory. |

All image processing in CE.SDK is handled client-side, so these values depend on the **maximum texture size** supported by the user’s hardware. The default limit of 4096×4096 is a safe baseline that works universally. Higher resolutions (e.g., 8192×8192) may work on certain devices but could fail on others during export if the GPU texture size is exceeded.

To ensure consistent results across devices, it’s best to test higher output sizes on your target hardware and set conservative defaults in production.

### Video Resolution & Duration Limits[#](#video-resolution--duration-limits)

| Constraint | Recommendation / Limit |
| --- | --- |
| **Resolution** | Up to **4K UHD** is supported for **playback** and **export**, depending on the user’s hardware and available GPU resources. For **import**, CE.SDK does not impose artificial limits, but maximum video size is bounded by the **32-bit address space of WebAssembly (wasm32)** and the **browser tab’s memory cap (~2 GB)**. |
| **Frame Rate** | 30 FPS at 1080p is broadly supported; 60 FPS and high-res exports benefit from hardware acceleration |
| **Duration** | Stories and reels of up to **2 minutes** are fully supported. Longer videos are also supported, but we generally found a maximum duration of **10 minutes** to be a good balance for a smooth editing experience and a pleasant export duration of around one minute on modern hardware. |

Performance scales with client hardware. For best results with high-resolution or high-frame-rate video, modern CPUs/GPUs with hardware acceleration are recommended.

---



[Source](https:/img.ly/docs/cesdk/vue/engine-interface-6fb7cf)