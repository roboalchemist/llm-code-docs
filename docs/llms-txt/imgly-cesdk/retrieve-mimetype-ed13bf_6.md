# Source: https://img.ly/docs/cesdk/mac-catalyst/import-media/retrieve-mimetype-ed13bf/

---
title: "Retrieve Mimetype"
description: "Detect the file type of an asset to control how it’s handled or displayed."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/import-media/retrieve-mimetype-ed13bf/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Import Media Assets](https://img.ly/docs/cesdk/mac-catalyst/import-media-4e3703/) > [Retrieve Mimetype](https://img.ly/docs/cesdk/mac-catalyst/import-media/retrieve-mimetype-ed13bf/)

---

When working with media assets in CE.SDK, it is often necessary to determine the mimetype of a resource before processing it. This guide explains how to use the `getMimeType(uri: Uri)` function to retrieve the mimetype of a given resource.

Returns the mimetype of the resources at the given Uri.

If the resource is not already downloaded, this function will download it.

- `uri:` the Uri of the resource.
- Returns the mimetype of the resource.

```swift
// Get the mimetype of a resource
let mimeType = try await engine.editor.getMIMEType(url: URL(string: "https://cdn.img.ly/assets/demo/v1/ly.img.image/images/sample_1.jpg")!)
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
