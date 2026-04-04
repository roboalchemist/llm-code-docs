# Source: https://img.ly/docs/cesdk/android/use-templates/apply-template-35c73e/

---
title: "Apply a Template"
description: "Learn how to apply template scenes via API in the CreativeEditor SDK."
platform: android
url: "https://img.ly/docs/cesdk/android/use-templates/apply-template-35c73e/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Use Templates](https://img.ly/docs/cesdk/android/create-templates-3aef79/) > [Apply a Template](https://img.ly/docs/cesdk/android/use-templates/apply-template-35c73e/)

---

```kotlin reference-only
val rawResId = R.raw.cesdk_postcard_1
val rawResourcePath = context.resources.run {
    ContentResolver.SCHEME_ANDROID_RESOURCE + "://"+
        getResourcePackageName(rawResId) + "/"" +
        getResourceTypeName(rawResId) + "/" +
        getResourceEntryName(rawResId)
}

engine.scene.applyTemplate(template = "UBQ1ewoiZm9ybWF0Ij...")
engine.scene.applyTemplate(templateUri = Uri.parse("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene"))
engine.scene.applyTemplate(templateUri = Uri.parse("file:///android_asset/templates/cesdk_postcard_1.scene"))
engine.scene.applyTemplate(templateUri = Uri.fromFile(File(filesDir, "templates/cesdk_postcard_1.scene")))
engine.scene.applyTemplate(templateUri = Uri.parse(rawResourcePath))
engine.scene.get()
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to apply the contents of a given template scene to the currently loaded scene through the `scene` API.

## Applying Template Scenes

```kotlin
suspend fun applyTemplate(template: String)
```

Applies the contents of the given template scene to the currently loaded scene.

This loads the template scene while keeping the design unit and page dimensions

of the current scene. The content of the pages is automatically adjusted to fit

the new dimensions.

- `template`: the template scene file contents, a base64 string.

```kotlin
suspend fun applyTemplate(templateUri: Uri)
```

Applies the contents of the given template scene to the currently loaded scene.

This loads the template scene while keeping the design unit and page dimensions

of the current scene. The content of the pages is automatically adjusted to fit

the new dimensions.

- `templateUri`: the resource of the template scene file.

```kotlin
fun get(): DesignBlock?
```

Return the currently active scene.

- Returns the scene or null, if none was created yet.

## Full Code

Here's the full code:

```kotlin
val rawResId = R.raw.cesdk_postcard_1
val rawResourcePath = context.resources.run {
    ContentResolver.SCHEME_ANDROID_RESOURCE + "://"+
        getResourcePackageName(rawResId) + "/"" +
        getResourceTypeName(rawResId) + "/" +
        getResourceEntryName(rawResId)
}

engine.scene.applyTemplate(template = "UBQ1ewoiZm9ybWF0Ij...")
engine.scene.applyTemplate(templateUri = Uri.parse("https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene"))
engine.scene.applyTemplate(templateUri = Uri.parse("file:///android_asset/templates/cesdk_postcard_1.scene"))
engine.scene.applyTemplate(templateUri = Uri.fromFile(File(filesDir, "templates/cesdk_postcard_1.scene")))
engine.scene.applyTemplate(templateUri = Uri.parse(rawResourcePath))
engine.scene.get()
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
