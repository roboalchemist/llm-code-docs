# Source: https://img.ly/docs/cesdk/android/prebuilt-solutions/photo-editor-42ccb2/

---
title: "Android Photo Editor SDK"
description: "The CreativeEditor SDK provides a robust and user-friendly solution for photo editing on Android devices."
platform: android
url: "https://img.ly/docs/cesdk/android/prebuilt-solutions/photo-editor-42ccb2/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Solutions](https://img.ly/docs/cesdk/android/prebuilt-solutions-d0ed07/) > [Photo Editor](https://img.ly/docs/cesdk/android/prebuilt-solutions/photo-editor-42ccb2/)

---

The CreativeEditor SDK provides a robust and user-friendly solution for photo
editing on Android devices.

The photo UI is a specific configuration of the CE.SDK UI which enables developers to seamlessly integrate essential photo editing features into their Android applications, offering users a powerful yet intuitive editing experience.
Whether you are developing an app for social media, content creation, or any other platform requiring photo editing tools, the CE.SDK Android Photo Editor is designed to meet your needs.

[Explore Demo](https://img.ly/showcases/cesdk/photo-editor-ui/android)

[View on GitHub](https://github.com/imgly/cesdk-android/blob/main/sources/editor/src/main/java/ly/img/editor/PhotoEditor.kt)

## Key Capabilities of the iOS Mobile Design Editor SDK

<CapabilityGrid
  features={[
  {
    title: 'Transforms',
    description:
      'Includes straightening, scaling, rotation, and flip functions.',
    imageId: 'transform',
  },
  {
    title: 'Advanced Adjustment Tools',
    description:
      'Includes brightness, saturation, contrast, gamma, clarity, exposure, shadows, highlights, and more.',
    imageId: 'templating',
  },
  {
    title: 'Filters',
    description:
      'Provide a wide range of built-in filters and effects or upload your own custom filters.',
    imageId: 'filters',
  },
  {
    title: 'Effects & Blur',
    description: 'Unique effects such as pixelize, glitch, or mirror.',
    imageId: 'effects',
  },
  {
    title: 'Text Editing',
    description:
      'Add and style text blocks with various fonts, colors, and effects.',
    imageId: 'text-editing',
  },
  {
    title: 'Asset Libraries',
    description: 'Add custom assets for stickers, filters, and shapes.',
    imageId: 'asset-libraries',
  },
  {
    title: 'Client-Side Processing',
    description:
      'All design editing operations are executed directly on the device, with no need for server dependencies.',
    imageId: 'client-side',
  },
  {
    title: 'Customizable UI',
    description:
      'Tailor the photo editing interface to align with your application’s branding and UX requirements.',
    imageId: 'customizable-u-i',
  },
]}
/>

## What is the Photo Editor Solution?

The Photo Editor is a fully customizable CE.SDK configuration focused on photo-centric use cases. It strips down the editor interface to include only the most relevant features for image adjustments — giving users a focused and responsive experience. Whether your users need to fine-tune selfies, prepare product photos, or create profile images, this solution makes it easy.

Get a powerful photo editor into your app with minimal setup. The Photo Editor runs entirely client-side — which helps reduce cloud computing costs and improve privacy.

## Platform Compatibility

The CE.SDK Photo Editor is optimized for use on Android devices, providing smooth and efficient performance across a variety of models.

## Prerequisites

To get started with the CE.SDK Photo Editor on Android, ensure you have the latest version of Android Studio and Kotlin installed.

## Supported File Types

The CE.SDK Photo Editor supports various image formats, enabling users to work with popular file types.

### Importing Media

### Exporting Media

### Importing Templates

For detailed information, see the [full file format support list](https://img.ly/docs/cesdk/android/file-format-support-3c4b2a/).

## Understanding CE.SDK Architecture & API

The following sections provide an overview of the key components of the CE.SDK photo editor UI and its API architecture.

If you're ready to start integrating CE.SDK into your Android application, check out our Implementation Guide.

### CreativeEditor SDK Mobile Photo UI

The CE.SDK photo editor UI is a streamlined configuration of the CreativeEditor SDK, focusing on essential photo editing features.

This configuration is fully customizable, allowing developers to adjust the UI and functionality to suit different use cases.

Key components include:

- **Canvas:** The primary workspace where users interact with their photo content.
- **Inspector Bar:** Offers tools for adjusting properties like size, position, and effects for selected elements.
- **Asset Library:** A collection of media resources available for use within the photo editor, including images and stickers.

Learn more about interacting with and customizing the photo editor UI in our design editor UI guide.

### CreativeEngine

At the heart of CE.SDK is the CreativeEngine, which powers all rendering and photo manipulation tasks.

It can be used in headless mode or in combination with the CreativeEditor UI.

Key features and APIs provided by CreativeEngine include:

- **Scene Management:** Create, load, save,
  and manipulate photo scenes programmatically.
- **Block Management:** Manage images, text,
  and other elements within the photo editor.
- **Asset Management:** Integrate and manage
  photo and image assets from various sources.
- **Variable Management:** Define and
  manipulate variables for dynamic content within photo scenes.
- **Event Handling:** Subscribe to events
  like image selection changes or editing actions for dynamic interaction.

## Customizing the Android Image Editor

CE.SDK provides extensive [customization options](https://img.ly/docs/cesdk/android/user-interface-5a089a/), allowing you to tailor the UI and functionality to meet your specific needs.

This can range from basic configuration settings to more advanced customizations involving custom asset sources and [hooking into UIEvents](https://img.ly/docs/cesdk/android/user-interface/events-514b70/).

### Basic Customizations

- **Configuration Object:** Customize the editor’s appearance and functionality by passing a configuration object during initialization.

```kotlin
    val engineConfiguration = EngineConfiguration.rememberForPhoto(
          license = "<your license here>",
          imageUri = Uri.parse("https://img.ly/static/ubq_samples/sample_4.jpg"),
          imageSize = SizeF(1080F, 1920F),
          userId = "<your unique user id>",
      )
```

- **Custom Asset Sources:** Serve custom images or stickers from a remote URL.

### UI Customization Options

- **Theme:** Choose between 'dark' or 'light' themes.

```kotlin
val editorConfiguration = EditorConfiguration.rememberForPhoto(
  uiMode = EditorUiMode.DARK,
)
```

<CallToAction />

<LogoWall />



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
