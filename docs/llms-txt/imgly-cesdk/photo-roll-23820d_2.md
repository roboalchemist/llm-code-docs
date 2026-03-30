# Source: https://img.ly/docs/cesdk/mac-catalyst/import-media/from-local-source/photo-roll-23820d/

---
title: "From Photo Roll"
description: "Import photos directly from the user’s photo library into your editor."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/import-media/from-local-source/photo-roll-23820d/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

---

In this guide, you’ll learn how to use the built-in **Photo Roll** integration to let users add images from their iOS photo library into your CE.SDK-based app. Unlike a custom upload source, CE.SDK provides Photo Roll as a system-backed asset source with its own tab in the Asset Panel.

## What You’ll Learn

- How the built-in Photo Roll tab works inside the Asset Panel.
- How to handle assets selected from Photo Roll with the `onUpload` callback.
- How to persist Photo Roll imports across app launches.

## When To Use This

- When you want the fastest path to letting users select from their device’s photo library.
- When you don’t need custom UI for picking photos.
- When you want to extend Photo Roll imports with your own metadata or persistence logic.

## Using the Photo Roll Tab

![Design Editor tabs with the Photo Roll tab highlighted](assets/ios-photo-roll-1-159.png)

CE.SDK includes a built-in **Photo Roll** tab in the Dock. You don’t need to register it manually. When tapped, it:

1. Launches the system photo picker (`PHPickerViewController`).
2. Returns one or more images.

Each selected photo appears in a predefined asset source with the ID `"ly.img.image.upload"`. You can intercept these assets in your `onUpload` handler just like you would for a custom source.

![Asset catalog showing Photo Roll source.](assets/ios-photo-roll-2-159.png)

***

## The onUpload Callback for Photo Roll

Whenever the user picks from Photo Roll, CE.SDK fires your `.onUpload` callback. You’ll receive:

- `engine` which is a reference to the CE.SDK engine
- `sourceID` with a value of `"ly.img.image.upload"`
- `asset` an `AssetDefinition` with metadata for the photo

Here’s an example handler:

```swift
.imgly.onUpload { engine, sourceID, asset in
    guard sourceID == "ly.img.image.upload" else { return asset }

    var updated = asset
    // Add searchable labels and tags
    updated.labels = ["Camera Roll"]
    updated.tags = ["photo-roll", "imported"]

    // Persist the file into Documents so it survives relaunch
    return persistAsset(updated)
}
```

The `persistAsset` function is an example described below. It’s not a standard function. It does the following:

1. Copies files into persistent storage.
2. Updates the URI with the new location.

## Persisting Photo Roll Imports

Just like with other asset uploads, Photo Roll imports only exist in memory during the current session by default.

To persist them:

- Copy the selected photo to Documents/Uploads (or upload to your backend).
- Update the URI in the asset definition.
- Save metadata with:
  - UserDefaults
  - Core Data
  - A database.
- Re-register the saved definitions into your asset source when the app launches.

This ensures the Photo Roll tab looks the same even after restarting the app. Here is a minimal example that:

- Uses `FileManager` to copy the URL of an `AssetDefinition` to a safe place.
- Modifies the `AssetDefinition` to point to the new URL.

```swift
func persistAsset(_ asset: AssetDefinition) -> AssetDefinition {
  guard let originalURL = URL(string: asset.meta["uri"] ?? "") else {
    return asset
  }

  let docs = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!
  //This copies the filename to the new path
  let dest = docs.appendingPathComponent(originalURL.lastPathComponent)

  do {
    // Copy the file if it’s not already in Documents
    if !FileManager.default.fileExists(atPath: dest.path) {
      try FileManager.default.copyItem(at: originalURL, to: dest)
    }

    var updated = asset
    updated.meta["uri"] = dest.absoluteString
    return updated

  } catch {
    print("Failed to persist asset: \(error)")
    return asset
  }
}
```

## Troubleshooting

**❌ Error**: Photo Roll tab doesn’t appear

- Make sure you’re including the default tabs in the `imgly.dock`. The photo roll is `Dock.Buttons.photoRoll()`.

**❌ Error**: Photos Disappear After Relaunch

- Photo Roll assets originate in temporary directories. Use a persistence function to save them to the app’s documents directory or your back end. Then reload the assets on app launch.

**❌ Error**: Duplicate Photos

- If the user imports the same photo multiple times, you may want to de-duplicate by comparing URLs or hashes **before** registering new photos.

## Next Steps

Now that you can import from the Photo Roll, you may want to explore:

- [From User Upload](https://img.ly/docs/cesdk/mac-catalyst/import-media/from-local-source/user-upload-c6c7d9/) to let users add files via the camera or Files app.
- [Capture from Camera](https://img.ly/docs/cesdk/mac-catalyst/import-media/capture-from-camera-92f388/) using the IMGLY standalone camera to record video.
- Import media [From a Remote Source](https://img.ly/docs/cesdk/mac-catalyst/import-media/from-remote-source-b65faf/) to bring assets from a service or your backend.



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
