# Source: https://img.ly/docs/cesdk/ios/user-interface/ui-extensions/add-new-button-74884d/

---
title: "Add a New Button"
description: "Extend editor functionality by adding custom buttons to Dock, Canvas Menu, Inspector Bar, and Navigation Bar."
platform: ios
url: "https://img.ly/docs/cesdk/ios/user-interface/ui-extensions/add-new-button-74884d/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/ios/user-interface-5a089a/) > [UI Extensions](https://img.ly/docs/cesdk/ios/user-interface/ui-extensions-d194d1/) > [Add New Button](https://img.ly/docs/cesdk/ios/user-interface/ui-extensions/add-new-button-74884d/)

---

```swift file=@cesdk_swift_examples/editor-guides-ui-extensions-add-button/AddButtonEditorSolution.swift reference-only
// swiftlint:disable unused_closure_parameter
// swiftformat:disable unusedArguments
import IMGLYDesignEditor
import SwiftUI

/// Design Editor demonstrating how to add custom buttons to different UI locations.
///
/// This example shows how to:
/// - Add a custom button to the Dock
/// - Add a custom button to the Canvas Menu
/// - Add a custom button to the Inspector Bar
/// - Add a custom button to the Navigation Bar
/// - Use conditional visibility and enabled states
/// - Apply proper ID naming conventions
struct AddButtonEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey,
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.modifyDockItems { context, items in
        items.addFirst {
          Dock.Button(
            id: "my.app.dock.button.export",
            action: { context in
              print("Custom export button tapped")
            },
            label: { context in
              Label("Export", systemImage: "square.and.arrow.up")
            },
          )
        }
      }
      .imgly.modifyCanvasMenuItems { context, items in
        items.addFirst {
          CanvasMenu.Button(
            id: "my.app.canvasMenu.button.favorite",
            action: { context in
              print("Favorite button tapped")
            },
            label: { context in
              Label("Favorite", systemImage: "star.fill")
            },
            // Disable for stickers (shows grayed out)
            isEnabled: { context in
              context.selection.kind != "sticker"
            },
            // Only show for graphic blocks (hidden otherwise)
            isVisible: { context in
              context.selection.type == .graphic
            },
          )
        }
      }
      .imgly.modifyInspectorBarItems { context, items in
        items.addFirst {
          InspectorBar.Button(
            id: "my.app.inspectorBar.button.process",
            action: { context in
              print("Process button tapped")
            },
            label: { context in
              Label("Process", systemImage: "gearshape")
            },
            // Disable for text blocks (shows grayed out)
            isEnabled: { context in
              context.selection.type != .text
            },
            // Only show for blocks with fill (hidden otherwise)
            isVisible: { context in
              context.selection.fillType != nil
            },
          )
        }
      }
      .imgly.navigationBarItems { context in
        NavigationBar.ItemGroup(placement: .topBarLeading) {
          NavigationBar.Buttons.closeEditor()
        }
      }
      .imgly.modifyNavigationBarItems { context, items in
        // Add to trailing side
        items.addFirst(placement: .topBarTrailing) {
          NavigationBar.Button(
            id: "my.app.navbar.button.help",
          ) { context in
            print("Help button tapped")
          } label: { context in
            Label("Help", systemImage: "questionmark.circle")
          }
        }

        // Add to leading side
        items.addLast(placement: .topBarLeading) {
          NavigationBar.Button(
            id: "my.app.navbar.button.settings",
          ) { context in
            print("Settings button tapped")
          } label: { context in
            Label("Settings", systemImage: "gearshape")
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
  AddButtonEditorSolution()
}
```

Add custom buttons to extend editor functionality with app-specific actions across four UI components.

![iOS editor with custom buttons](./assets/ios.hero.webp)

> **Reading time:** 8 minutes
>
> **Resources:**
>
> - [View source on GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/editor-guides-ui-extensions-add-button)

## Overview

Add buttons using component-specific modifiers (`.imgly.modifyDockItems`, `.imgly.modifyCanvasMenuItems`, etc.) with `[Component].Button` types. Each component provides context for conditional logic.

| Component | Selection Context | Best For |
|-----------|-------------------|----------|
| Dock | - | Global actions |
| CanvasMenu | `context.selection` | Selection-specific actions |
| InspectorBar | `context.selection` | Property-related actions |
| NavigationBar | - | App-level navigation |

## Adding to Dock

Add global action buttons using `.imgly.modifyDockItems`. Use reverse domain notation for IDs to avoid conflicts.

```swift highlight-addNewButton-dock
.imgly.modifyDockItems { context, items in
  items.addFirst {
    Dock.Button(
      id: "my.app.dock.button.export",
      action: { context in
        print("Custom export button tapped")
      },
      label: { context in
        Label("Export", systemImage: "square.and.arrow.up")
      },
    )
  }
}
```

- `id` - Unique identifier (e.g., `"my.app.dock.button.export"`)
- `action` - Closure executed on tap
- `label` - SwiftUI `Label` for button appearance

## Adding to Canvas Menu

Add selection-specific buttons using `.imgly.modifyCanvasMenuItems`. Use `context.selection` to control button state based on the selected element:

```swift highlight-addNewButton-canvasMenu
.imgly.modifyCanvasMenuItems { context, items in
  items.addFirst {
    CanvasMenu.Button(
      id: "my.app.canvasMenu.button.favorite",
      action: { context in
        print("Favorite button tapped")
      },
      label: { context in
        Label("Favorite", systemImage: "star.fill")
      },
      // Disable for stickers (shows grayed out)
      isEnabled: { context in
        context.selection.kind != "sticker"
      },
      // Only show for graphic blocks (hidden otherwise)
      isVisible: { context in
        context.selection.type == .graphic
      },
    )
  }
}
```

Use `isEnabled` and `isVisible` closures to control button state based on selection properties:

```swift highlight-addNewButton-conditional
// Disable for stickers (shows grayed out)
isEnabled: { context in
  context.selection.kind != "sticker"
},
// Only show for graphic blocks (hidden otherwise)
isVisible: { context in
  context.selection.type == .graphic
},
```

## Adding to Inspector Bar

Add property-related buttons using `.imgly.modifyInspectorBarItems`. Use `isEnabled` and `isVisible` to control button state based on selection:

- `isEnabled` - When `false`, the button appears grayed out but remains visible
- `isVisible` - When `false`, the button is completely hidden

```swift highlight-addNewButton-inspectorBar
.imgly.modifyInspectorBarItems { context, items in
  items.addFirst {
    InspectorBar.Button(
      id: "my.app.inspectorBar.button.process",
      action: { context in
        print("Process button tapped")
      },
      label: { context in
        Label("Process", systemImage: "gearshape")
      },
      // Disable for text blocks (shows grayed out)
      isEnabled: { context in
        context.selection.type != .text
      },
      // Only show for blocks with fill (hidden otherwise)
      isVisible: { context in
        context.selection.fillType != nil
      },
    )
  }
}
```

## Adding to Navigation Bar

Add app-level buttons using `.imgly.modifyNavigationBarItems`. Specify placement for each button.

```swift highlight-addNewButton-navbar
      .imgly.modifyNavigationBarItems { context, items in
        // Add to trailing side
        items.addFirst(placement: .topBarTrailing) {
          NavigationBar.Button(
            id: "my.app.navbar.button.help",
          ) { context in
            print("Help button tapped")
          } label: { context in
            Label("Help", systemImage: "questionmark.circle")
          }
        }

        // Add to leading side
        items.addLast(placement: .topBarLeading) {
          NavigationBar.Button(
            id: "my.app.navbar.button.settings",
          ) { context in
            print("Settings button tapped")
          } label: { context in
            Label("Settings", systemImage: "gearshape")
          }
        }
      }
```

| Placement | Position |
|-----------|----------|
| `.topBarLeading` | Leading side |
| `.topBarTrailing` | Trailing side |
| `.principal` | Center |

## Button Parameters

All button types accept these parameters:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `id` | `String` | Yes | - | Unique identifier |
| `action` | `(Context) -> Void` | Yes | - | Closure executed on tap |
| `label` | `(Context) -> Label` | Yes | - | Button appearance |
| `isEnabled` | `(Context) -> Bool` | No | `true` | When `false`, button is grayed out |
| `isVisible` | `(Context) -> Bool` | No | `true` | When `false`, button is hidden |

## API Reference

| API | Description |
|-----|-------------|
| `Dock.Button()` | Create a custom dock button |
| `CanvasMenu.Button()` | Create a canvas menu button |
| `InspectorBar.Button()` | Create an inspector bar button |
| `NavigationBar.Button()` | Create a navigation bar button |
| `.imgly.modifyDockItems()` | Insert buttons into the dock |
| `.imgly.modifyCanvasMenuItems()` | Insert buttons into the canvas menu |
| `.imgly.modifyInspectorBarItems()` | Insert buttons into the inspector bar |
| `.imgly.modifyNavigationBarItems()` | Insert buttons into the navigation bar |

## Next Steps

- [Rearrange Buttons](https://img.ly/docs/cesdk/ios/user-interface/customization/rearrange-buttons-97022a/) - Customize button order in UI components
- [Customize Dock](https://img.ly/docs/cesdk/ios/user-interface/customization/dock-cb916c/) - Full dock customization patterns
- [Customize Navigation Bar](https://img.ly/docs/cesdk/ios/user-interface/customization/navigation-bar-4e5d39/) - Navigation bar configuration
- [Canvas Menu](https://img.ly/docs/cesdk/ios/user-interface/customization/canvas-menu-0d2b5b/) - Contextual menu customization



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
