# Source: https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/panel-7ce1ee/

---
title: "Panel"
description: "Show or hide panels to focus the user interface on what matters most for your use case."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/user-interface/customization/panel-7ce1ee/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

---

```swift file=@cesdk_swift_examples/editor-guides-configuration-panel/DefaultPanelSolution.swift reference-only
import IMGLYDesignEditor
import SwiftUI

struct DefaultPanelSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.modifyDockItems { context, items in
        items.addFirst {
          Dock.Button(
            id: "custom_panel",
          ) { context in
            context.eventHandler.send(
              .openSheet(
                type: .libraryAdd { context.assetLibrary.elementsTab },
              ),
            )
          } label: { _ in
            Label("Open Panel", systemImage: "arrow.up.circle")
          }
        }
      }
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
  DefaultPanelSolution()
}
```

```swift file=@cesdk_swift_examples/editor-guides-configuration-panel/CustomPanelSolution.swift reference-only
import IMGLYDesignEditor
import SwiftUI

struct CustomPanelSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.modifyDockItems { context, items in
        items.addFirst {
          Dock.Button(
            id: "custom_panel",
          ) { context in
            context.eventHandler.send(.openSheet(
              style: .default(
                isFloating: false,
                detent: .fraction(0.7),
                detents: [.large, .fraction(0.7)],
              ),
              content: {
                VStack(spacing: 16) {
                  Text("Custom Panel")
                    .font(.headline)
                  Button("Close") {
                    context.eventHandler.send(.closeSheet)
                  }
                  .buttonStyle(.bordered)
                }
                .padding()
              },
            ))
          } label: { _ in
            Label("Open Panel", systemImage: "arrow.up.circle")
          }
        }
      }
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
  CustomPanelSolution()
}
```

A panel is a UI layer that displays above the canvas, and allows the user perform a scoped task like accessing asset library, selecting filters, or any custom action.

![Panel on iOS](./assets/panel-ios.png)

## Controlling a Panel

Panels are implemented as different types of `SheetType` that allow you to display content in nonmodal sheet overlays. Panels are opened using the `.openSheet` event, and passing in the desired `sheetType`

```swift highlight-open-panel
context.eventHandler.send(
  .openSheet(
    type: .libraryAdd { context.assetLibrary.elementsTab },
  ),
)
```

After use, they can be closed using the `.closeSheet` event.

```swift highlight-close-panel
context.eventHandler.send(.closeSheet)
```

## Creating a Custom Panel

To create a custom panel, you can make a new `SheetType.Custom()` and define your UI inside the `content` parameter.

```swift highlight-open-custom-panel
context.eventHandler.send(.openSheet(
  style: .default(
    isFloating: false,
    detent: .fraction(0.7),
    detents: [.large, .fraction(0.7)],
  ),
  content: {
    VStack(spacing: 16) {
      Text("Custom Panel")
        .font(.headline)
      Button("Close") {
        context.eventHandler.send(.closeSheet)
      }
      .buttonStyle(.bordered)
    }
    .padding()
  },
))
```

In the `style` parameter, you can define how the sheet will look like.
These are the parameters available for `.default()` constructor, and what they change:

| Parameter    | Default Value                   | Description                                                                                                                                                                                                                                   |
| ------------ | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `isFloating` | `false`                         | Whether the sheet should be floating. If `true` the sheet will cover the editor's canvas and its content, if `false` the canvas will be zoomed to adjust for the size of the sheet so that the canvas' content won't be covered by the sheet. |
| `detent`     | `.imgly.medium`                 | The initial detent of the sheet. Ensure that the value matches one of the detents that you provide for the `detents` parameter.                                                                                                               |
| `detents`    | `[.imgly.medium, .imgly.large]` | A set of supported detents for the sheet. If you provide more that one detent, people can drag the sheet to resize it.                                                                                                                        |

## Default Sheet Types

The editor provides several built-in sheet types for common functionality:

#### Available Sheet Types

| Sheet Type Call             | Required Parameters             | Description                                                                 |
| --------------------------- | ------------------------------- | --------------------------------------------------------------------------- |
| `.libraryAdd(content:)`     | `content` (AssetLibraryContent) | Add assets from a custom asset library with specified title and content     |
| `.libraryReplace(content:)` | `content` (AssetLibraryContent) | Replace assets from a custom asset library with specified title and content |
| `.voiceover()`              | -                               | Record voiceover audio                                                      |
| `.reorder()`                | -                               | Reorder videos on the background track                                      |
| `.adjustments(id:)`         | `id` (DesignBlockID)            | Make adjustments to design blocks with image and video fills                |
| `.filter(id:)`              | `id` (DesignBlockID)            | Set filters to design blocks with image and video fills                     |
| `.effect(id:)`              | `id` (DesignBlockID)            | Set effects to design blocks with image and video fills                     |
| `.blur(id:)`                | `id` (DesignBlockID)            | Set blurs to design blocks with image and video fills                       |
| `.crop(id:)`                | `id` (DesignBlockID)            | Crop design blocks with image and video fills                               |
| `.resize()`                 | -                               | Resize pages                                                                |
| `.layer()`                  | -                               | Control the layering of design blocks                                       |
| `.formatText()`             | -                               | Control formatting of text blocks                                           |
| `.shape()`                  | -                               | Control the shape of various blocks                                         |
| `.fillStroke()`             | -                               | Control the fill and/or stroke of various blocks                            |
| `.volume()`                 | -                               | Control the volume of audio/video                                           |
| `.textBackground()`         | -                               | Control text background properties                                          |

## Full source code

#### Default Panel Solution

```swift file=@cesdk_swift_examples/editor-guides-configuration-panel/DefaultPanelSolution.swift
import IMGLYDesignEditor
import SwiftUI

struct DefaultPanelSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.modifyDockItems { context, items in
        items.addFirst {
          Dock.Button(
            id: "custom_panel",
          ) { context in
            context.eventHandler.send(
              .openSheet(
                type: .libraryAdd { context.assetLibrary.elementsTab },
              ),
            )
          } label: { _ in
            Label("Open Panel", systemImage: "arrow.up.circle")
          }
        }
      }
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
  DefaultPanelSolution()
}
```

#### Custom Panel Solution

```swift file=@cesdk_swift_examples/editor-guides-configuration-panel/CustomPanelSolution.swift
import IMGLYDesignEditor
import SwiftUI

struct CustomPanelSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey, // pass nil for evaluation mode with watermark
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.modifyDockItems { context, items in
        items.addFirst {
          Dock.Button(
            id: "custom_panel",
          ) { context in
            context.eventHandler.send(.openSheet(
              style: .default(
                isFloating: false,
                detent: .fraction(0.7),
                detents: [.large, .fraction(0.7)],
              ),
              content: {
                VStack(spacing: 16) {
                  Text("Custom Panel")
                    .font(.headline)
                  Button("Close") {
                    context.eventHandler.send(.closeSheet)
                  }
                  .buttonStyle(.bordered)
                }
                .padding()
              },
            ))
          } label: { _ in
            Label("Open Panel", systemImage: "arrow.up.circle")
          }
        }
      }
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
  CustomPanelSolution()
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
