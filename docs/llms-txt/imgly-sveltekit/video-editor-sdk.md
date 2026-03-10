# Video Editor SDK

Use CreativeEditor SDK (CE.SDK) to build robust video editing experiences directly in your app. CE.SDK supports both video and audio editing — including trimming, joining, adding text, annotating, and more — all performed client-side without requiring a server. Developers can integrate editing functionality using a built-in UI or programmatically via the SDK API.

CE.SDK also supports music and sound effects alongside video editing. You can integrate custom or third-party AI models to streamline creative workflows, such as converting image to video or generating clips from text.

[Launch Web Demo](https://img.ly/showcases/cesdk)[

Get Started

](sveltekit/get-started/overview-e18f40/)

## Core Capabilities[#](#core-capabilities)

CreativeEditor SDK includes a comprehensive set of video editing tools, accessible through both a UI and programmatic interface. Supported editing actions include:

*   **Trim, Split, Join, and Arrange**: Modify clips, reorder segments, and stitch together content.
*   **Transform**: Crop, rotate, resize, scale, and flip.
*   **Audio Editing**: Add, adjust, and synchronize audio including music and effects.
*   **Programmatic Editing**: Control all editing features via API.

CE.SDK is well-suited for scenarios like short-form content, reels, promotional videos, and other linear video workflows.

## Timeline Editor[#](#timeline-editor)

The built-in timeline editor provides a familiar video editing experience for users. It supports:

*   Layered tracks for video and audio
*   Drag-and-drop sequencing with snapping
*   Trim handles, in/out points, and time offsets
*   Real-time preview updates

The timeline is the main control for video editing:

![The editor timeline control.](/docs/cesdk/_astro/video_mode_timeline.BkrXFlTn_2e2pv5.webp)

## AI-Powered Editing[#](#ai-powered-editing)

CE.SDK allows you to easily integrate AI tools directly into your video editing workflow. Users can generate images, videos, and audio from simple prompts — all from within the editor’s task bar, without switching tools or uploading external assets.

[

Launch AI Editor Demo

](https://img.ly/showcases/cesdk/ai-editor/web)

You can bring your own models or third-party APIs with minimal setup. AI tools can be added as standalone plugins, contextual buttons, or task bar actions.

## Supported Input Formats and Codecs[#](#supported-input-formats-and-codecs)

CE.SDK supports a wide range of video input formats and encodings, including:

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png`, `.jpeg`, `.jpg`, `.gif`, `.webp`, `.svg`, `.bmp` |
| **Video** | `.mp4` (H.264/AVC, H.265/HEVC), `.mov` (H.264/AVC, H.265/HEVC), `.webm` (VP8, VP9, AV1) |
| **Audio** | `.mp3`, `.m4a`, `.mp4` (AAC or MP3), `.mov` (AAC or MP3) |
| **Animation** | `.json` (Lottie) |

Need to import a format not listed here? CE.SDK allows you to create custom importers for any file type by using our Scene and Block APIs programmatically.

CE.SDK supports the most widely adopted video and audio codecs to ensure compatibility across platforms:

### **Video Codecs**[#](#video-codecs)

*   **H.264 / AVC** (in `.mp4`)
*   **H.265 / HEVC** (in `.mp4`, may require platform-specific support)

### **Audio Codecs**[#](#audio-codecs)

*   **MP3** (in `.mp3` or within `.mp4`)
*   **AAC** (in `.m4a` or within `.mp4` or `.mov`)

## Output and Export Options[#](#output-and-export-options)

You can export edited videos in several formats, with control over resolution, encoding, and file size:

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png` (with transparency), `.jpeg`, `.webp`, `.tga` |
| **Video** | `.mp4` (H.264 or H.265 on supported platforms with limited transparency support) |
| **Print** | `.pdf` (supports underlayer printing and spot colors) |
| **Scene** | `.scene` (description of the scene without any assets) |
| **Archive** | `.zip` (fully self-contained archive that bundles the `.scene` file with all assets) |

Our custom cross-platform C++ based rendering and layout engine ensures consistent output quality across devices.

## UI-Based vs. Programmatic Editing[#](#ui-based-vs-programmatic-editing)

CE.SDK offers a fully interactive editor with intuitive UI tools for creators. At the same time, developers can build workflows entirely programmatically using the SDK API.

*   Use the UI to let users trim, arrange, and caption videos manually
*   Use the API to automate the assembly or editing of videos at scale

## Customization[#](#customization)

You can tailor the editor to match your product’s design and user needs:

*   Show or hide tools
*   Reorder UI elements and dock items
*   Apply custom themes, colors, or typography
*   Add additional plugin components

## Performance and File Size Considerations[#](#performance-and-file-size-considerations)

All editing operations are performed client-side. While this ensures user privacy and responsiveness, it introduces some limits:

| Constraint | Recommendation / Limit |
| --- | --- |
| **Resolution** | Up to **4K UHD** is supported for **playback** and **export**, depending on the user’s hardware and available GPU resources. For **import**, CE.SDK does not impose artificial limits, but maximum video size is bounded by the **32-bit address space of WebAssembly (wasm32)** and the **browser tab’s memory cap (~2 GB)**. |
| **Frame Rate** | 30 FPS at 1080p is broadly supported; 60 FPS and high-res exports benefit from hardware acceleration |
| **Duration** | Stories and reels of up to **2 minutes** are fully supported. Longer videos are also supported, but we generally found a maximum duration of **10 minutes** to be a good balance for a smooth editing experience and a pleasant export duration of around one minute on modern hardware. |

Performance scales with client hardware. For best results with high-resolution or high-frame-rate video, modern CPUs/GPUs with hardware acceleration are recommended.

---



[Source](https:/img.ly/docs/cesdk/sveltekit/overview-491658)