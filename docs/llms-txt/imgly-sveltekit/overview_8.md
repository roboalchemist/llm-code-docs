# Overview

In CE.SDK, assets are the building blocks of your creative workflow—whether they’re images, videos, audio, fonts, or templates. They power everything from basic image edits to dynamic, template-driven design generation.

This guide gives you a high-level understanding of how to bring assets into CE.SDK, where they can come from, and how to decide on the right strategy for your application. Whether you’re working with local uploads, remote storage, or third-party sources, this guide will help you navigate your options and build an efficient import pipeline.

[Launch Web Demo](https://img.ly/showcases/cesdk)[

Get Started

](sveltekit/get-started/overview-e18f40/)

## What is an Asset?[#](#what-is-an-asset)

In CE.SDK, an _asset_ refers to any external media that can be inserted into a design scene. Assets are referenced via URIs, and are not stored or hosted by CE.SDK itself.

Supported asset types include:

*   **Images** – JPEG, PNG, WebP, SVG, etc.
*   **Video** – MP4, MOV
*   **Audio / Music** – MP3, AAC
*   **Fonts** – Custom or system fonts
*   **Stickers** – SVG or PNG elements
*   **Templates** – Design presets or prebuilt scenes
*   **Custom Media** – Any content with a valid URI and supported format

See a [full list of supported file formats](sveltekit/file-format-support-3c4b2a/) .

Assets are used throughout the editor to fill shapes, provide visual or audio decoration, or serve as core scene content.

## Asset Sources in CE.SDK[#](#asset-sources-in-cesdk)

CE.SDK supports a range of asset sources, allowing developers to import media from:

*   **Local Sources**  
    Assets directly uploaded by the user (e.g., from their device).
*   **Remote Sources**  
    Media served via external servers or your own backend (e.g., S3, CDN).
*   **Third-Party Sources**  
    Create custom integrations with Unsplash, Getty, Airtable, etc.
*   **Dynamic Sources**  
    Assets created or fetched on demand (e.g., generative AI images).

**Note:** When a user opens the editor, CE.SDK downloads any referenced assets to the local environment for use within the editing session.

### When to Use Each Asset Source[#](#when-to-use-each-asset-source)

| Use Case | Recommended Source Type |
| --- | --- |
| End-users upload personal media | Local Source |
| Use your company’s asset library | Remote Source |
| Enable searchable stock assets | Third-Party Source |
| Fetch real-time AI-generated content | Dynamic Source |

With **Local Asset Sources**, CE.SDK powers search functionality directly in the browser. For **Remote Asset Sources**, searching and indexing are typically offloaded to the server to ensure scalability and performance.

**Performance Tip:** If you’re managing **thousands of assets**, it’s best to offload search and filtering to a **remote backend** to avoid performance bottlenecks in the browser.

## Asset Storage and Management in CE.SDK[#](#asset-storage-and-management-in-cesdk)

### No Built-In Storage Provided[#](#no-built-in-storage-provided)

CE.SDK does **not** host or store assets. You must handle storage using your infrastructure:

*   Amazon S3
*   Google Cloud Storage
*   Firebase
*   Your own custom backend

### How It Works[#](#how-it-works)

*   Assets are referenced via **URIs**—not embedded or stored internally.
*   You implement a **custom asset source**, which returns references to assets via CE.SDK’s API.
*   Assets are then made available in the **Asset Library** or loaded programmatically.

### Custom Asset Libraries[#](#custom-asset-libraries)

CE.SDK is fully modular. You define how assets are fetched, filtered, categorized, and presented. This works for all asset types: images, videos, audio, and even uploads.

### Uploading Assets[#](#uploading-assets)

CE.SDK supports upload workflows using your own infrastructure:

*   Use `onUpload` callbacks to trigger uploads.
*   Refresh asset lists after uploads with `refetchAssetSources`.

### Best Practices[#](#best-practices)

Work with your backend team to:

*   Define where assets are stored and how they’re indexed.
*   Ensure secure, performant delivery of media files.
*   Implement custom asset source logic based on CE.SDK’s source API.

## Using and Customizing the Asset Library[#](#using-and-customizing-the-asset-library)

The built-in Asset Library gives users a way to browse and insert assets visually.

You can:

*   Add or remove asset categories (images, stickers, audio, etc.).
*   Customize the layout, filters, and tab order.
*   Show assets from your own remote sources.
*   Dynamically refresh asset lists when new files are uploaded.

## Default Assets[#](#default-assets)

CE.SDK includes a set of default assets (images, templates, stickers, etc.) for testing or bootstrapping a demo.

You can:

*   Use them in development for fast prototyping.
*   Customize or remove them entirely for production apps.

Use `addDefaultAssetSources()` to populate the default library.

## Third-Party Asset Integrations[#](#third-party-asset-integrations)

CE.SDK supports integrations with popular content platforms:

*   **Unsplash** – High-quality free stock images
*   **Pexels** – Free photos and videos
*   **Getty Images** – Licensed, premium content
*   **Airtable** – Structured media from database rows
*   **Soundstripe** – Music and audio tracks for video scenes

You can also integrate any other source using a custom asset source and the standard asset source API.

## File Type Support[#](#file-type-support)

CreativeEditor SDK (CE.SDK) supports importing high-resolution images, video, and audio content.

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png`, `.jpeg`, `.jpg`, `.gif`, `.webp`, `.svg`, `.bmp` |
| **Video** | `.mp4` (H.264/AVC, H.265/HEVC), `.mov` (H.264/AVC, H.265/HEVC), `.webm` (VP8, VP9, AV1) |
| **Audio** | `.mp3`, `.m4a`, `.mp4` (AAC or MP3), `.mov` (AAC or MP3) |
| **Animation** | `.json` (Lottie) |

Need to import a format not listed here? CE.SDK allows you to create custom importers for any file type by using our Scene and Block APIs programmatically.

## Media Constraints[#](#media-constraints)

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



[Source](https:/img.ly/docs/cesdk/sveltekit/import-media/from-remote-source-b65faf)