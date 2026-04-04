# Source: https://img.ly/docs/cesdk/ios/user-interface/appearance/theming-4b0938/

---
title: "Theming"
description: "Customize the editor's visual theme to match your brand using flexible theming options."
platform: ios
url: "https://img.ly/docs/cesdk/ios/user-interface/appearance/theming-4b0938/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/ios/user-interface-5a089a/) > [Appearance](https://img.ly/docs/cesdk/ios/user-interface/appearance-b155eb/) > [Theming](https://img.ly/docs/cesdk/ios/user-interface/appearance/theming-4b0938/)

---

```swift file=@cesdk_swift_examples/editor-guides-configuration-theming/ThemingEditorSolution.swift reference-only
import IMGLYDesignEditor
import SwiftUI

struct ThemingEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  @Environment(\.colorScheme) private var colorScheme

  var editor: some View {
    DesignEditor(settings)
      .preferredColorScheme(colorScheme == .dark ? .light : .dark)
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
  ThemingEditorSolution()
}
```

In this example, we will show you how to make theming configurations for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/ios/prebuilt-solutions-d0ed07/).

## Modifiers

After initializing an editor SwiftUI view you can apply any SwiftUI *modifier* to customize it like for any other SwiftUI view.

Theming the mobile editor is done like for any other SwiftUI view. The editor respects the SwiftUI [`colorScheme` environment](https://developer.apple.com/documentation/swiftui/colorscheme). It can be configured with the [`preferredColorScheme` modifier](https://developer.apple.com/documentation/swiftui/view/preferredcolorscheme\(_:\)) to override the system's color scheme which is the default if it is not already overridden somewhere in your view hierarchy.
In this example, we use the opposite color scheme that is currently used.

```swift
import IMGLYDesignEditor
import SwiftUI

struct ThemingEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey,
                                userID: "<your unique user id>")

  @Environment(\.colorScheme) private var colorScheme

  var editor: some View {
    DesignEditor(settings)
      .preferredColorScheme(colorScheme == .dark ? .light : .dark)
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
  ThemingEditorSolution()
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
