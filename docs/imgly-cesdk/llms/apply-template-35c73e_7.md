# Source: https://img.ly/docs/cesdk/macos/use-templates/apply-template-35c73e/

---
title: "Apply a Template"
description: "Learn how to apply template scenes via API in the CreativeEditor SDK."
platform: macos
url: "https://img.ly/docs/cesdk/macos/use-templates/apply-template-35c73e/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/macos/guides-8d8b00/) > [Create and Use Templates](https://img.ly/docs/cesdk/macos/create-templates-3aef79/) > [Apply a Template](https://img.ly/docs/cesdk/macos/use-templates/apply-template-35c73e/)

---

```swift reference-only
try await engine.scene.applyTemplate(from: "UBQ1ewoiZm9ybWF0Ij...")
try await engine.scene
  .applyTemplate(
    from: .init(
      string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene"
    )!
  )
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to apply the contents of a given template scene to the currently loaded scene through the `scene` API.

## Applying Template Scenes

```swift
public func applyTemplate(from string: String) async throws
```

Applies the contents of the given template scene to the currently loaded scene.
This loads the template scene while keeping the design unit and page dimensions
of the current scene. The content of the pages is automatically adjusted to fit
the new dimensions.

- `string:`: The template scene file contents, a base64 string.

```swift
public func applyTemplate(from url: URL) async throws
```

Applies the contents of the given template scene to the currently loaded scene.
This loads the template scene while keeping the design unit and page dimensions
of the current scene. The content of the pages is automatically adjusted to fit
the new dimensions.

- `url:`: The url to the template scene file.

## Full Code

Here's the full code:

```swift
try await engine.scene.applyTemplate(from: "UBQ1ewoiZm9ybWF0Ij...")
try await engine.scene
  .applyTemplate(
    from: .init(
      string: "https://cdn.img.ly/assets/demo/v1/ly.img.template/templates/cesdk_postcard_1.scene"
    )!
  )
```



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
