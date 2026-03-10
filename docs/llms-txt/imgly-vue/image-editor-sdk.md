# Image Editor SDK

The CreativeEditor SDK (CE.SDK) offers powerful image editing capabilities designed for seamless integration into your application. You can give your users full control through an intuitive user interface or implement fully automated workflows via the SDK’s programmatic API.

Image editing with CE.SDK is fully client-side, ensuring fast performance, data privacy, and offline compatibility. Whether you’re building a photo editor, design tool, or automation workflow, CE.SDK provides everything you need—plus the flexibility to integrate AI tools for tasks like adding or removing objects, swapping backgrounds, or creating variants.

[Launch Web Demo](https://img.ly/showcases/cesdk)[

Get Started

](vue/get-started/overview-e18f40/)

## Core Capabilities[#](#core-capabilities)

CE.SDK includes a wide range of image editing features accessible both through the UI and programmatically. Key capabilities include:

*   **Transformations**: Crop, rotate, resize, scale, and flip images.
*   **Adjustments and effects**: Apply filters, control brightness and contrast, add vignettes, pixelization, and more.
*   **Background removal**: Automatically remove backgrounds from images using plugin integrations.
*   **Color tools**: Replace colors, apply gradients, adjust palettes, and convert to black and white.
*   **Vectorization**: Convert raster images into vector format (SVG).
*   **Programmatic editing**: Make all edits via API—ideal for automation and bulk processing.

All operations are optimized for in-app performance and align with real-time editing needs.

## AI-powered Editing[#](#ai-powered-editing)

CE.SDK allows you to easily integrate AI tools directly into your editing workflow. Users can generate or edit images from simple prompts — all from within the editor’s task bar, without switching tools or uploading external assets.

[

Launch AI Editor Demo

](https://img.ly/showcases/cesdk/ai-editor/web)

Typical AI use cases include:

*   **Text-to-image**: Generate visuals from user prompts.
*   **Background removal**: Automatically extract subjects from photos.
*   **Style transfer**: Apply the look of one image to another.
*   **Variant generation**: Create multiple versions of a design or product image.
*   **Text-to-graphics**: Render typographic compositions from plain text.
*   **Object add/remove**: Modify compositions by adding or erasing visual elements.

You can bring your own models or third-party APIs with minimal setup. AI tools can be added as standalone plugins, contextual buttons, or task bar actions.

## Supported Input Formats[#](#supported-input-formats)

The SDK supports a broad range of image input types:

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png`, `.jpeg`, `.jpg`, `.gif`, `.webp`, `.svg`, `.bmp` |
| **Video** | `.mp4` (H.264/AVC, H.265/HEVC), `.mov` (H.264/AVC, H.265/HEVC), `.webm` (VP8, VP9, AV1) |
| **Audio** | `.mp3`, `.m4a`, `.mp4` (AAC or MP3), `.mov` (AAC or MP3) |
| **Animation** | `.json` (Lottie) |

Need to import a format not listed here? CE.SDK allows you to create custom importers for any file type by using our Scene and Block APIs programmatically.

## Output and export options[#](#output-and-export-options)

Export edited images in the following formats:

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png` (with transparency), `.jpeg`, `.webp`, `.tga` |
| **Video** | `.mp4` (H.264 or H.265 on supported platforms with limited transparency support) |
| **Print** | `.pdf` (supports underlayer printing and spot colors) |
| **Scene** | `.scene` (description of the scene without any assets) |
| **Archive** | `.zip` (fully self-contained archive that bundles the `.scene` file with all assets) |

Our custom cross-platform C++ based rendering and layout engine ensures consistent output quality across devices.

You can define export resolution, compression level, and file metadata. CE.SDK also supports exporting with transparent backgrounds, underlayers, or color masks.

## UI-Based vs. Programmatic Editing[#](#ui-based-vs-programmatic-editing)

CE.SDK provides two equally powerful ways to perform image edits:

*   **UI-based editing**: The built-in editor includes a customizable toolbar, side panels, and inspector views. End users can directly manipulate elements through the visual interface.
*   **Programmatic editing**: Every image transformation, effect, or layout operation can be executed via the SDK’s API. This is ideal for bulk operations, automated design workflows, or serverless rendering.

You can freely combine both approaches in a single application.

## Customization[#](#customization)

The CE.SDK image editor is fully customizable:

*   **Tool configuration**: Enable, disable, or reorder individual editing tools.
*   **Panel visibility**: Show or hide interface elements like inspectors, docks, and canvas menus.
*   **Themes and styling**: Customize the UI appearance with brand colors, fonts, and icons.
*   **Localization**: Translate all interface text via the internationalization API.

You can also add custom buttons, inject quick actions, or build your own interface on top of the engine using the headless mode.

---



[Source](https:/img.ly/docs/cesdk/vue/edit-image/add-watermark-679de0)