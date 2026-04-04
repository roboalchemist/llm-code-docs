# Source: https://img.ly/docs/cesdk/macos/user-interface/customization/crop-presets-f94f26/

---
title: "Crop Presets"
description: "Define crop presets settings for your design."
platform: macos
url: "https://img.ly/docs/cesdk/macos/user-interface/customization/crop-presets-f94f26/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

---

By default, the CreativeEditor SDK ships with an extensive list of commonly used crop presets, as shown below:

![](./assets/crop-presets-ios.png)

The CE.SDK can be configured with a series of crop presets by updating the `content.json` from the default asset sources - `ly.img.crop.presets` for fixed aspect ratio assets and `ly.img.page.presets` for fixed size assets - on your CDN. For further reference, [please take a look at the "Serve Assets" section here.](https://img.ly/docs/cesdk/macos/serve-assets-b0827c/)

To enable the CE.SDK defaults enable our default asset sources by using `addDefaultAssetSources`.

```swift
let baseURL = URL(string: "YOUR_CDN_URL")!
try await engine.addDefaultAssetSources(baseURL: baseURL)
```

## Configuring Custom Crop Presets

When overriding the `content.json` with your custom crop presets each of the assets in the asset source must define a value for its `payload.transformPreset` property.

### Fixed Aspect Ratio

When a fixed aspect ratio preset is applied it will resize the crop frame based on the `width` and `height` values provided. On iOS, the fixed aspect ratio assets will be automatically rendered based on the dimensions and therefore do not need a separate icon.

```json
{
  "id": "aspect-ratio-9-16",
  "label": {
    "en": "9:16",
    "de": "9:16"
  },
  "payload": {
    "transformPreset": {
      "type": "FixedAspectRatio",
      "width": 9,
      "height": 16
    }
  },
  "groups": ["fixed-ratio"]
}
```

- `type` - specifies the preset type.

```json
"type": "FixedAspectRatio"
```

- `width` - specifies the width of the crop frame.

```json
"width": 16
```

- `height` - specifies the height of the crop frame.

```json
"height": 9
```

### Free Aspect Ratio

When a free aspect ratio preset is applied it will enable the side-handles of the crop frame.

```json
{
  "id": "aspect-ratio-free",
  "label": {
    "en": "Free",
    "de": "Frei"
  },
  "payload": {
    "transformPreset": {
      "type": "FreeAspectRatio"
    }
  },
  "groups": ["fixed-ratio"]
}
```

- `type` - specifies the preset type.

```json
"type": "FreeAspectRatio"
```

### Fixed Size

When a fixed size preset is applied, the selected block will be resized to the specified `width` and `height`. Unlike assets with a fixed aspect ratio, this type of asset requires you to provide an icon.

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

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
