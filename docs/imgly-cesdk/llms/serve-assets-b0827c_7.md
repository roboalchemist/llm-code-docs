# Source: https://img.ly/docs/cesdk/macos/serve-assets-b0827c/

---
title: "Serve Assets From Your Server"
description: "Set up and manage how assets are served to the editor, including local, remote, or CDN-based delivery."
platform: macos
url: "https://img.ly/docs/cesdk/macos/serve-assets-b0827c/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Serve Assets](https://img.ly/docs/cesdk/macos/serve-assets-b0827c/)

---

In this example, we explain how to configure the Creative Engine to use assets hosted on your own servers.
While we serve all assets from our own CDN by default, it is highly recommended
to serve the assets from your own servers in a production environment.

## 1. Register IMG.LY's default assets

If you want to use our default asset sources in your integration, call `engine.addDefaultAssetSources(baseURL: URL, exclude: Set<DefaultAssetSource>)`. Right after initialization:

```swift
let engine = Engine()
Task {
  try await engine.addDefaultAssetSources()
}
```

This call adds IMG.LY's default asset sources for stickers, vectorpaths and filters to your engine instance.
By default, these include the following sources with their corresponding ids (as `rawValue`):

- `.sticker` - `'ly.img.sticker'` - Various stickers.
- `.vectorPath` - `'ly.img.vectorpath'` - Shapes and arrows.
- `.filterLut` - `'ly.img.filter.lut'` - LUT effects of various kinds.
- `.filterDuotone` - `'ly.img.filter.duotone'` - Color effects of various kinds.
- `.colorsDefaultPalette` - `'ly.img.colors.defaultPalette'` - Default color palette.
- `.effect` - `ly.img.effect` - Default effects.
- `.blur` - `ly.img.blur` - Default blurs.
- `.typeface` - `ly.img.typeface` - Default typefaces.
- `.cropPresets` - `ly.img.crop.presets` - Default crop presets.
- `.pagePresets` - `ly.img.page.presets` - Default page resize presets.

If you don't specify a `baseURL` option, the assets are parsed and served from the IMG.LY CDN.
It's it is highly recommended to serve the assets from your own servers in a production environment, if you decide to use them.
To do so, follow the steps below and pass a `baseURL` option to `addDefaultAssetSources`.
If you only need a subset of the categories above, use the `exclude` option to pass a set of ignored sources.

## 2. Copy Assets

Download the IMG.LY default assets from [our CDN](https://cdn.img.ly/packages/imgly/cesdk-swift/$UBQ_VERSION$/imgly-assets.zip).

Copy the IMGLYEngine *default* asset folders to your application bundle. The default asset folders should be located in a new `.bundle` folder. It will create a nested `Bundle` object that can be loaded by your app. The folder structure should look like this:

<br />

<p>![](./assets/bundle-ios.png)</p>

<br />

## 3. Configure the IMGLYEngine to use your self-hosted assets

Next, we need to configure the SDK to use the copied assets instead of the ones served via IMG.LY CDN.

`engine.addDefaultAssetSources` offers a `baseURL` option, that needs to be set to an absolute URL, pointing to a valid `Bundle` or a remote location.

In case of using your own server, the `baseURL` should point to the root of your asset folder, e.g. `https://cdn.your.custom.domain/assets`:

```swift
let remoteURL = URL(string: "https://cdn.your.custom.domain/assets")!
Task {
  try await engine.addDefaultAssetSources(baseURL: remoteURL)
}
```

In case of using a local `Bundle`, the `baseURL` should point to the `.bundle` folder, that we created in the previous step:

```swift
let bundleURL = Bundle.main.url(forResource: "IMGLYAssets", withExtension: "bundle")!
Task {
  try await engine.addDefaultAssetSources(baseURL: bundleURL)
}
```

## 4. Configure Engine-Level Assets

The engine uses additional assets for font fallback (Unicode character coverage) and emoji rendering. By default, these are loaded from `https://cdn.img.ly/assets/v4`. When you configure the `basePath` setting, font fallback files and the emoji font are automatically loaded from that location:

```swift
try engine.editor.setSettingString(key: "basePath", value: "https://cdn.your.custom.domain/cesdk-assets")
```

This setting affects:

- **Font fallback files** — Used when text contains characters not covered by the selected font. Located at `{basePath}/fonts/font-{index}.ttf`.
- **Emoji font** — The default emoji font (NotoColorEmoji.ttf). Located at `{basePath}/emoji/NotoColorEmoji.ttf`.

To self-host these assets:

1. The `fonts/` and `emoji/` directories are already included in the `imgly-assets.zip` download
2. After extracting, set `basePath` to point to your extraction location

For bundled assets:

```swift
let assetBundleURL = Bundle.main.url(forResource: "CESDKAssets", withExtension: "bundle")!
try engine.editor.setSettingString(key: "basePath", value: assetBundleURL.absoluteString)
```



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
