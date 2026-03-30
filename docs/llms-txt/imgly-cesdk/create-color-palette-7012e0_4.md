# Source: https://img.ly/docs/cesdk/ios/colors/create-color-palette-7012e0/

---
title: "Create a Color Palette"
description: "Build reusable color palettes to maintain consistency and streamline user choices."
platform: ios
url: "https://img.ly/docs/cesdk/ios/colors/create-color-palette-7012e0/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Colors](https://img.ly/docs/cesdk/ios/colors-a9b79c/) > [Create a Color Palette](https://img.ly/docs/cesdk/ios/colors/create-color-palette-7012e0/)

---

```swift file=@cesdk_swift_examples/editor-guides-configuration-color-palette/ColorPaletteEditorSolution.swift reference-only
import IMGLYDesignEditor
import SwiftUI

struct ColorPaletteEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.colorPalette([
        .init("Blue", .imgly.blue),
        .init("Green", .imgly.green),
        .init("Yellow", .imgly.yellow),
        .init("Red", .imgly.red),
        .init("Black", .imgly.black),
        .init("White", .imgly.white),
        .init("Gray", .imgly.gray),
      ])
  }

  @State private var isPresented = false

  var body: some View {
    Button("Use the Editor") {
      isPresented = true
    }
    .fullScreenCover(isPresented: $isPresented) {
      ModalEditor {
        editor
      }
    }
  }
}

#Preview {
  ColorPaletteEditorSolution()
}
```

In this example, we will show you how to make color palette configurations for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/ios/prebuilt-solutions-d0ed07/).

## Modifiers

After initializing an editor SwiftUI view you can apply any SwiftUI *modifier* to customize it like for any other SwiftUI view.
All public Swift `extension`s of existing types provided by IMG.LY, e.g., for the SwiftUI `View` protocol or for the `CGColor` class, are exposed in a separate `.imgly` property namespace.
The color palette configuration to customize the editor is no exception to this rule and is implemented as a SwiftUI *modifier*.

```swift highlight-editor
DesignEditor(settings)
```

- `colorPalette` - the color palette used for UI elements that contain predefined color options, e.g., for "Fill Color" or "Stroke Color". It expects an array of `NamedColor`s that are composed of a name, required for accessibility, and the actual `CGColor` to use. It should contain seven elements. Six of them are always shown. The seventh is only shown when a color property does not support a disabled state. This example shows the default configuration.

```swift highlight-colorPalette
.imgly.colorPalette([
  .init("Blue", .imgly.blue),
  .init("Green", .imgly.green),
  .init("Yellow", .imgly.yellow),
  .init("Red", .imgly.red),
  .init("Black", .imgly.black),
  .init("White", .imgly.white),
  .init("Gray", .imgly.gray),
])
```

## Full Code

Here's the full code:

```swift
import IMGLYDesignEditor
import SwiftUI

struct ColorPaletteEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey,
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.colorPalette([
        .init("Blue", .imgly.blue),
        .init("Green", .imgly.green),
        .init("Yellow", .imgly.yellow),
        .init("Red", .imgly.red),
        .init("Black", .imgly.black),
        .init("White", .imgly.white),
        .init("Gray", .imgly.gray),
      ])
  }

  @State private var isPresented = false

  var body: some View {
    Button("Use the Editor") {
      isPresented = true
    }
    .fullScreenCover(isPresented: $isPresented) {
      ModalEditor {
        editor
      }
    }
  }
}

#Preview {
  ColorPaletteEditorSolution()
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
