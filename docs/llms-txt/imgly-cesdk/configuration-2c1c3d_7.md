# Source: https://img.ly/docs/cesdk/mac-catalyst/configuration-2c1c3d/

---
title: "Configuration"
description: "Learn how to configure CE.SDK to match your application's functional, visual, and performance requirements."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/configuration-2c1c3d/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Configuration](https://img.ly/docs/cesdk/mac-catalyst/configuration-2c1c3d/)

---

```swift file=@cesdk_swift_examples/editor-guides-configuration-basics/BasicEditorSolution.swift reference-only
import IMGLYDesignEditor
import SwiftUI

struct BasicEditorSolution: View {
  let settings = EngineSettings(
    license: secrets.licenseKey, // pass nil for evaluation mode with watermark
    userID: "<your unique user id>",
    baseURL: URL(string: "https://cdn.img.ly/packages/imgly/cesdk-swift/1.70.0/assets")!,
  )

  var editor: some View {
    DesignEditor(settings)
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
  BasicEditorSolution()
}
```

In this example, we will show you how to make basic configurations for the mobile editor. The example is based on the `Design Editor`, however, it is exactly the same for all the other [solutions](https://img.ly/docs/cesdk/mac-catalyst/prebuilt-solutions-d0ed07/).

## Configuration

All the basic configuration settings are part of the `EngineSettings` which are required to initialize the editor.

```javascript highlight-editor
DesignEditor(settings)
```

- `license` - the license to activate the [Engine](https://img.ly/docs/cesdk/mac-catalyst/get-started/overview-e18f40/) with.

```javascript highlight-license
license: secrets.licenseKey, // pass nil for evaluation mode with watermark
```

- `userID` - an optional unique ID tied to your application's user. This helps us accurately calculate monthly active users (MAU). Especially useful when one person uses the app on multiple devices with a sign-in feature, ensuring they're counted once. Providing this aids in better data accuracy. The default value is `nil`.

```javascript highlight-userID
userID: "<your unique user id>",
```

- `baseURL` - is used to initialize the engine's [setting](https://img.ly/docs/cesdk/mac-catalyst/settings-970c98/) before the editor's `onCreate` callback is run. It is the foundational URL for constructing absolute paths from relative ones. This URL enables the loading of specific scenes or assets using their relative paths. The default value is pointing at the versioned IMG.LY CDN `https://cdn.img.ly/packages/imgly/cesdk-swift/$UBQ_VERSION$/assets` but it should be changed in production environments.

```javascript highlight-baseURL
baseURL: URL(string: "https://cdn.img.ly/packages/imgly/cesdk-swift/1.70.0/assets")!,
```

## Full Code

```swift
import IMGLYDesignEditor
import SwiftUI

struct BasicEditorSolution: View {
  let settings = EngineSettings(
    license: secrets.licenseKey,
    userID: "<your unique user id>",
    baseURL: URL(string: "https://cdn.img.ly/packages/imgly/cesdk-swift/$UBQ_VERSION$/assets")!
  )

  var editor: some View {
    DesignEditor(settings)
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
  BasicEditorSolution()
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
