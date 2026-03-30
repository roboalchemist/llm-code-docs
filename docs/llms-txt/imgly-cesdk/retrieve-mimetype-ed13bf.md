# Source: https://img.ly/docs/cesdk/android/import-media/retrieve-mimetype-ed13bf/

---
title: "Retrieve Mimetype"
description: "Detect the file type of an asset to control how it’s handled or displayed."
platform: android
url: "https://img.ly/docs/cesdk/android/import-media/retrieve-mimetype-ed13bf/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/android/import-media-4e3703/) > [Retrieve Mimetype](https://img.ly/docs/cesdk/android/import-media/retrieve-mimetype-ed13bf/)

---

When working with media assets in CE.SDK, it is often necessary to determine the mimetype of a resource before processing it. This guide explains how to use the `getMimeType(uri: Uri)` function to retrieve the mimetype of a given resource.

Returns the mimetype of the resources at the given Uri.

If the resource is not already downloaded, this function will download it.

- `uri:` the Uri of the resource.
- Returns the mimetype of the resource.

```kotlin
// Get the mimetype of a resource
val mimeType = engine.editor.getMimeType(Uri.parse("https://cdn.img.ly/assets/demo/v1/ly.img.image/images/sample_1.jpg"))
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
