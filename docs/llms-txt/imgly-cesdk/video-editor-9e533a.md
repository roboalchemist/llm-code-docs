# Source: https://img.ly/docs/cesdk/android/prebuilt-solutions/video-editor-9e533a/

---
title: "Android Video Editor SDK"
description: "The CreativeEditor SDK offers a comprehensive and versatile solution for video editing on Android devices."
platform: android
url: "https://img.ly/docs/cesdk/android/prebuilt-solutions/video-editor-9e533a/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/) > [Video Editor](https://img.ly/docs/cesdk/android/prebuilt-solutions/video-editor-9e533a/)

---

The CreativeEditor SDK offers a comprehensive and versatile solution for video
editing on Android devices.

The CE.SDK video editor enables developers to integrate powerful video editing capabilities into their Android applications, providing users with an intuitive and fully customizable editing experience.
Whether you're building an app for social media, content creation, or any other platform that requires robust video editing tools, the CE.SDK Android Video Editor is designed to meet your needs.

[Explore Demo](https://img.ly/showcases/cesdk/video-ui/android)

[View on GitHub](https://github.com/imgly/cesdk-android/blob/main/sources/editor/src/main/java/ly/img/editor/VideoEditor.kt)

<ImageContainer image="true" />

## Key Capabilities of the Android Mobile Video Editor SDK

<CapabilityGrid
  features={[
  {
    title: 'Multi-Format Support',
    description:
      'Create videos in various formats, including story reels and Ultra HD, tailored for different channels like Instagram, TikTok, or custom formats.',
    imageId: 'transform',
  },
  {
    title: 'Templating',
    description:
      'Jumpstart your users designs with easily adaptable templates including text variables and placeholders.',
    imageId: 'templating',
  },
  {
    title: 'Asset Management',
    description:
      'Record, upload, or select pre-existing videos, images, and other media from a custom library to enrich video content.',
    imageId: 'asset-libraries',
  },
  {
    title: 'Advanced Editing Tools',
    description:
      'Utilize features such as adjustments, filters, effects, and blur to fine-tune each element or the entire video, delivering a professional finish.',
    imageId: 'empty',
  },
  {
    title: 'Timeline Management',
    description:
      'Arrange multiple video clips, images, text, stickers, and shapes on a timeline for precise control over the final output.',
    imageId: 'timeline',
  },
  {
    title: 'Audio Integration',
    description:
      'Enhance videos with audio tracks, either imported or selected from a custom asset library, to add another layer of creativity.',
    imageId: 'audio',
  },
  {
    title: 'Customizable UI',
    description:
      'Tailor the video editing interface to match your application’s branding and user experience needs, ensuring an intuitive and engaging experience.',
    imageId: 'customizable-u-i',
  },
]}
/>

## What is the Video Editor Solution?

The Video Editor is a prebuilt solution powered by the CreativeEditor SDK (CE.SDK) that enables fast integration of high-performance video editing into web, mobile, and desktop applications. It’s designed to help your users create professional-grade videos—from short social clips to long-form stories—directly within your app.

Skip building a video editor from scratch. This fully client-side solution provides a solid foundation with an extensible UI and a robust engine API to power video editing in any use case.

## Supported Platforms

The Android Mobile Video Editor SDK is compatible with Android applications developed using Kotlin or Java, offering full support for both languages.

## Prerequisites

Ensure that the **IMGLYUI Android Library** is added to your project.
The SDK requires a license key, use `null` or an empty string to run in evaluation mode with watermark. Additionally, you can provide unique user IDs for accurate user tracking.

## Supported Media Types

[IMG.LY](http://img.ly/)'s Creative Editor SDK enables you to load, edit, and save **MP4 files** directly on the device without server dependencies.

### Importing Media

### Exporting Media

### Importing Templates

For detailed information, see the [full file format support list](https://img.ly/docs/cesdk/android/file-format-support-3c4b2a/).

## Understanding CE.SDK Architecture & API

The following sections provide an overview of the key components of the CE.SDK video editor UI and its API architecture.

If you're ready to start integrating CE.SDK into your Android application, check out our Implementation Guide.

### CreativeEditor SDK Mobile Video UI

The CE.SDK video editor UI is a specific configuration of the CreativeEditor SDK, focusing on essential video editing features.
It includes robust tools for video manipulation, customizable to suit different use cases.
Key components include the **Canvas**, the main workspace where users interact with their video content.
The **Timeline** provides control over the sequence and duration of video clips, images, and audio tracks.
The **Tool Bar** provides essential editing options like adjustments, filters, effects, layer management or adding text or images in order of relevance.
Lastly, the **Context Menu** presents relevant editing options for each selected element, simplifying the editing process for users.

Learn more about interacting with and customizing the video editor UI in our design editor UI guide.

### CreativeEngine

At the core of CE.SDK is the CreativeEngine, which handles all rendering and video manipulation tasks.
It can be used in headless mode or alongside the CreativeEditor UI.
Key features and APIs provided by CreativeEngine include functionalities for **Scene Management:** to create, load, save, and manipulate video scenes programmatically.

**Block Management:** to manage video clips,
images, text, and other elements within the timeline.
**Asset Management:** to integrate and
manage video, audio, and image assets from various sources.
**Variable Management:** to define and
manipulate variables for dynamic content within video scenes and
**Event Handling:** to subscribe to events
like clip selection changes or timeline updates for dynamic interaction.

## Customizing the Android Video Editor

CE.SDK provides extensive customization options, allowing you to tailor the UI and functionality to meet your specific needs.
This can range from basic configuration settings to more advanced customizations involving callbacks and custom elements.

### Basic Customizations

- [Configuration Object:](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/) Customize the
  editor’s appearance and functionality by passing a configuration object during
  initialization.

- [Custom Asset Sources:](https://img.ly/docs/cesdk/android/import-media/asset-panel/customize-c9a4de/) Serve custom
  video clips or audio tracks from a remote URL.

See the video editor getting started page for more configuration examples.

### UI Customization Options

The editor's appearance can be customized with options like choosing between 'dark' or 'light' themes.
You can also configure the editor color palette to match a particular CI.

[- Hook into UI Events:](https://img.ly/docs/cesdk/android/user-interface/events-514b70/) Register event
listener for UI events, for example, this would allow you to display a loading
spinner while the editor is being initialized.

## Framework Support

CreativeEditor SDK’s video editor is compatible with Swift and Objective-C, making it easy to integrate into any Android application.

<CallToAction />

<LogoWall />



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
