# Source: https://img.ly/docs/cesdk/android/serve-assets-b0827c/

---
title: "Serve Assets From Your Server"
description: "Set up and manage how assets are served to the editor, including local, remote, or CDN-based delivery."
platform: android
url: "https://img.ly/docs/cesdk/android/serve-assets-b0827c/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Serve Assets](https://img.ly/docs/cesdk/android/serve-assets-b0827c/)

---

In this example, we explain how to configure the Creative Engine to use assets hosted on your own servers.
While we serve all assets from our own CDN by default, it is highly recommended
to serve the assets from your own servers in a production environment.

## 1. Register IMG.LY's default assets

If you want to use our default asset sources in your integration, call `fun Engine.addDefaultAssetSources(baseUri: Uri, exclude: Set<DefaultAssetSource>)`. Right after initialization:

```kotlin
val engine = Engine("ly.img.engine.example")
engine.start()
engine.addDefaultAssetSources()
```

This call adds IMG.LY's default asset sources for stickers, vectorpaths and filters to your engine instance.
By default, these include the following sources represented by `DefaultAssetSource` enum\`:

- `DefaultAssetSource.STICKER` - `ly.img.sticker` - Various stickers.
- `DefaultAssetSource.VECTOR_PATH` - `ly.img.vectorpath` - Shapes and arrows.
- `DefaultAssetSource.FILTER_LUT` - `ly.img.filter.lut` - LUT effects of various kinds.
- `DefaultAssetSource.FILTER_DUO_TONE` - `ly.img.filter.duotone` - Color effects of various kinds.
- `DefaultAssetSource.COLORS_DEFAULT_PALETTE` - `ly.img.colors.defaultPalette` - Default color palette.
- `DefaultAssetSource.EFFECT` - `ly.img.effect` - Default effects.
- `DefaultAssetSource.BLUR` - `ly.img.blur` - Default blurs.
- `DefaultAssetSource.TYPEFACE` - `ly.img.typeface` - Default typefaces.

If you don't specify a `baseUri` option, the assets are parsed and served from the IMG.LY CDN.
It is highly recommended to serve the assets from your own servers in a production environment, if you decide to use them.
To do so, follow the steps below and pass a `baseUri` option to `addDefaultAssetSources`.
If you only need a subset of the IDs above, use the `exclude` option to pass a list of ignored `DefaultAssetSource` objects\`.

## 2. Copy Assets

Download the IMG.LY default assets from [our CDN](https://cdn.img.ly/packages/imgly/cesdk-android/$UBQ_VERSION$/imgly-assets.zip).
Copy the extracted folders to your own CDN server or to the android assets folder if you want to use them offline. It can be on the root or any subfolder.

## 3. Configure the IMGLYEngine to use your self-hosted assets

Next, we need to configure the SDK to use the copied assets instead of the ones served via IMG.LY CDN.

`Engine.addDefaultAssetSources` offers a `baseUri` option, that needs to be set to an absolute Uri, pointing to your newly added assets.

In case you have copied to your own cdn path:

```kotlin
    val baseUri = Uri.parse("https://cdn.your.custom.domain/assets")
    engine.addDefaultAssetSources(baseUri)
```

In case you have copied to android assets folder:

```kotlin
    val baseUri = Uri.parse("file:///android_asset/assets")
    engine.addDefaultAssetSources(baseUri)
```

## 4. Configure Engine-Level Assets

The engine uses additional assets for font fallback (Unicode character coverage) and emoji rendering. By default, these are loaded from `https://cdn.img.ly/assets/v4`. When you configure the `basePath` setting, font fallback files and the emoji font are automatically loaded from that location:

```kotlin
engine.editor.setSettingString("basePath", "https://cdn.your.custom.domain/cesdk-assets")
```

This setting affects:

- **Font fallback files** — Used when text contains characters not covered by the selected font. Located at `{basePath}/fonts/font-{index}.ttf`.
- **Emoji font** — The default emoji font (NotoColorEmoji.ttf). Located at `{basePath}/emoji/NotoColorEmoji.ttf`.

To self-host these assets:

1. The `fonts/` and `emoji/` directories are already included in the `imgly-assets.zip` download
2. After extracting, set `basePath` to point to your extraction location

For android assets folder:

```kotlin
engine.editor.setSettingString("basePath", "file:///android_asset/cesdk-assets")
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
