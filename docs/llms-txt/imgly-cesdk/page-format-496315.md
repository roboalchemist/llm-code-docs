# Source: https://img.ly/docs/cesdk/android/user-interface/customization/page-format-496315/

---
title: "Page Format"
description: "Define default page size, orientation, and other format settings for your design canvas."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/customization/page-format-496315/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [Customization](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/) > [Page Format](https://img.ly/docs/cesdk/android/user-interface/customization/page-format-496315/)

---

By default, the CreativeEditor SDK ships with an extensive list of commonly used formats, as shown below:

![](./assets/page-presets-android.png)

The CE.SDK can be configured with a series of crop presets by updating the `content.json` from the default asset source - `ly.img.page.presets` - on your CDN. For further reference, [please take a look at the "Serve Assets" section here.](https://img.ly/docs/cesdk/android/serve-assets-b0827c/)

To enable the CE.SDK defaults enable our default asset sources by using `addDefaultAssetSources`.

```kotlin
val baseUri = Uri.parse("YOUR_CDN_URL")
engine.addDefaultAssetSources(baseUri)
```

## Configuring Custom Page Formats

When overriding the `content.json` with your custom crop presets each of the assets in the asset source must define a value for its `payload.transformPreset` property.

When a fixed size preset is applied, the pages of the scene will be resized to the specified `width` and `height`.

```json
{
  "id": "page-sizes-instagram-square",
  "label": {
    "en": "Square Post (1:1)",
    "de": "Quadratischer Post (1:1)"
  },
  "meta": {
    "thumbUri": "{{base_url}}/ly.img.page.presets/thumbnails/instagram/ig-square.png"
  },
  "payload": {
    "transformPreset": {
      "type": "FixedSize",
      "width": 1080,
      "height": 1080,
      "designUnit": "Pixel"
    }
  },
  "groups": ["instagram"]
}
```

- `type` - specifies the preset type.

```json
"type": "FixedSize"
```

- `width` - specifies the width of the page in the specified design unit.

```json
"width": 1280
```

- `height` specifies the height of the page in the specified design unit.

```json
"height": 720
```

- `unit` describes unit in which `width` and `height` are specified. This can either be `Millimeter`, `Inch` or `Pixel`.

```json
"designUnit": "Pixel"
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
