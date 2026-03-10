# Source: https://img.ly/docs/cesdk/android/user-interface/customization/force-crop-c2854e/

---
title: "Force Crop"
description: "Apply predefined crop presets programmatically in the Android SDK."
platform: android
url: "https://img.ly/docs/cesdk/android/user-interface/customization/force-crop-c2854e/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/android/user-interface-5a089a/) > [Customization](https://img.ly/docs/cesdk/android/user-interface/customization-72b2f8/) > [Force Crop](https://img.ly/docs/cesdk/android/user-interface/customization/force-crop-c2854e/)

---

Use the Android SDK's force crop flow by preparing (or isolating) the preset in an asset source and calling `applyForceCrop` from your editor's `onLoaded` callback.

***

## Overview

Force cropping ensures that a page (or any cropable block) uses a specific aspect ratio or fixed size when the editor loads. The helper `ForceCropConfiguration` can be passed to `EngineConfiguration.rememberForPhoto` and is applied during `onLoaded`. Alternatively, you can invoke `applyForceCrop` manually in a custom `onLoaded` implementation.

```kotlin
suspend fun EditorScope.applyForceCrop(
    block: DesignBlock,
    configuration: ForceCropConfiguration,
)
```

***

## Parameters

| Name                   | Type                                  | Description                                                                                                    |
| ---------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `block`                | `DesignBlock`                         | The block to which the preset should be applied. Must support cropping (pages do by default).                  |
| `configuration`        | `ForceCropConfiguration`              | Describes the preset source, preset IDs, optional fallbacks, and application mode.                             |
| `sourceId`             | `String`                              | Asset source that stores the forced preset.                                                                    |
| `presetId`             | `String`                              | Primary preset ID that should be applied.                                                                      |
| `presetCandidates`     | `List<ForceCropPresetCandidate>`      | Additional presets the helper can fall back to. Omit this if you only want to use a single preset.             |
| `mode`                 | `ForceCropMode`                       | Controls whether the crop sheet opens (`Always` / `IfNeeded`) or stays silent (`Silent`).                      |

`ForceCropConfiguration` supports optional fallback candidates so you can reuse the same block-level heuristics on Android.

***

## Modes

| Mode        | Behavior                                                                                                                                  |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `Silent`    | Applies the preset without opening the crop UI.                                                                                           |
| `Always`    | Applies the preset and opens the crop sheet immediately.                                                                                  |
| `IfNeeded`  | Compares the preset with the current frame dimensions. The crop is applied and the sheet opens only if the ratio/size differs materially. |

`ForceCropMode.IfNeeded` accepts an optional `threshold` to tweak the tolerance for aspect-ratio comparisons.

***

## Usage Example

The snippet below shows how to isolate a preset, pass it into `EngineConfiguration.rememberForPhoto`, and let the SDK apply the crop during `onLoaded`.

```kotlin
val forceCropConfig = ForceCropConfiguration(
    sourceId = "ly.img.crop.presets",
    presetId = "aspect-ratio-1-1",
    presetCandidates = listOf(
        ForceCropPresetCandidate(
            sourceId = "ly.img.crop.presets",
            presetId = "aspect-ratio-16-9",
        ),
        ForceCropPresetCandidate(
            sourceId = "ly.img.crop.presets",
            presetId = "aspect-ratio-9-16",
        ),
    ),
    mode = ForceCropMode.IfNeeded(threshold = 0.01f),
)

val engineConfiguration = EngineConfiguration.rememberForPhoto(
    license = license,
    imageUri = imageUri,
    forceCropConfiguration = forceCropConfig,
)
```

When the editor loads, `rememberForPhoto` calls `applyForceCrop(...)` for the first page. If you prefer to control the timing yourself, switch to the generic builder and call `applyForceCrop` in your own `onLoaded` block:

```kotlin
EngineConfiguration.remember(
    license = license,
    onCreate = {
        EditorDefaults.onCreateFromImage(editorContext.engine, imageUri, editorContext.eventHandler)
    },
    onLoaded = {
        val page = editorContext.engine.scene.getPages().first()
        applyForceCrop(page, forceCropConfig)
    },
)
```

If you prefer to keep the configuration logic decoupled from `onLoaded`, dispatch the `ApplyForceCrop` event instead:

```kotlin
editorContext.eventHandler.send(
    ApplyForceCrop(
        block = page,
        configuration = forceCropConfig,
    ),
)
```

### Isolating the Preset

Ensure the user only sees the enforced preset by recreating the asset source ahead of time:

```kotlin
engine.asset.removeSource("ly.img.crop.presets")
engine.asset.addLocalSource("ly.img.crop.presets")
engine.asset.addAssetToSource("ly.img.crop.presets", forcedPreset)
```

***

## Behavior Details

- The helper locks page resizing while the crop sheet is open and restores the previous setting when finished.
- Fixed-size presets adjust the scene size and trigger a zoom recalculation automatically.
- All preset candidates are fetched on the main engine thread. Missing sources or IDs are logged and ignored.
- Matching logic mirrors the iOS implementation: the helper picks the preset whose ratio/size best fits the current frame, then applies it according to the selected `mode`.

***

## See Also

- [Force Crop (Web)](https://img.ly/docs/cesdk/android/edit-image/transform/crop-f67a47/)
- [UI Events (iOS)](https://img.ly/docs/cesdk/android/user-interface/events-514b70/)
- [Asset Library](https://img.ly/docs/cesdk/android/import-media/asset-library-65d6c4/)



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
