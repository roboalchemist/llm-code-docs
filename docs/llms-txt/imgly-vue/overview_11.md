# Overview

CreativeEditor SDK (CE.SDK) allows you to export designs into a variety of formats, making it easy to prepare assets for web publishing, printing, storage, and other workflows.

You can trigger conversions either programmatically through the SDK’s API or manually using the built-in export options available in the UI.

[Launch Web Demo](https://img.ly/showcases/cesdk)[

Get Started

](vue/get-started/overview-e18f40/)

## Supported Input and Output Formats[#](#supported-input-and-output-formats)

CE.SDK accepts a range of input formats when working with designs, including:

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png`, `.jpeg`, `.jpg`, `.gif`, `.webp`, `.svg`, `.bmp` |
| **Video** | `.mp4` (H.264/AVC, H.265/HEVC), `.mov` (H.264/AVC, H.265/HEVC), `.webm` (VP8, VP9, AV1) |
| **Audio** | `.mp3`, `.m4a`, `.mp4` (AAC or MP3), `.mov` (AAC or MP3) |
| **Animation** | `.json` (Lottie) |

Need to import a format not listed here? CE.SDK allows you to create custom importers for any file type by using our Scene and Block APIs programmatically.

When it comes to exporting or converting designs, the SDK supports the following output formats:

| Category | Supported Formats |
| --- | --- |
| **Images** | `.png` (with transparency), `.jpeg`, `.webp`, `.tga` |
| **Video** | `.mp4` (H.264 or H.265 on supported platforms with limited transparency support) |
| **Print** | `.pdf` (supports underlayer printing and spot colors) |
| **Scene** | `.scene` (description of the scene without any assets) |
| **Archive** | `.zip` (fully self-contained archive that bundles the `.scene` file with all assets) |

Our custom cross-platform C++ based rendering and layout engine ensures consistent output quality across devices.

Each format serves different use cases, giving you the flexibility to adapt designs for your application’s needs.

## Conversion Methods[#](#conversion-methods)

There are two main ways to trigger a conversion:

*   **Programmatically:**  
    Use CE.SDK’s API methods to perform conversions directly from your code. This gives you full control over the export process, allowing you to customize settings, automate workflows, and integrate with other systems.
    
*   **Through the UI:**  
    End users can trigger exports manually through CE.SDK’s built-in export options. The UI provides an intuitive way to export designs without writing code, ideal for non-technical users.
    

Both methods provide access to core conversion features, ensuring you can choose the workflow that fits your project.

## Customization Options[#](#customization-options)

When exporting designs, CE.SDK offers several customization options to meet specific output requirements:

*   **Resolution and DPI Settings:**  
    Adjust the resolution for raster exports like PNG to optimize for screen or print.
    
*   **Output Dimensions:**  
    Define custom width and height settings for the exported file, independent of the original design size.
    
*   **File Quality:**  
    For formats that support compression (such as PNG or PDF), you can control the quality level to balance file size and visual fidelity.
    
*   **Background Transparency:**  
    Choose whether to preserve transparent backgrounds or export with a solid background color.
    
*   **Page Selection:**  
    When exporting multi-page documents (e.g., PDFs), you can select specific pages or export all pages at once.
    
*   **Video Frame Selection:**  
    When exporting from a video, you can select a specific frame to export as an image, allowing for thumbnail generation or frame captures.
    

These options help ensure that your exported content is optimized for its intended platform, whether it’s a website, a mobile app, or a print-ready document.

---



[Source](https:/img.ly/docs/cesdk/vue/concepts/undo-and-history-99479d)