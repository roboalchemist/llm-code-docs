# Source: https://img.ly/docs/cesdk/ios/user-interface/customization/hide-elements-fe945c/

---
title: "Hide Elements"
description: "Hide the dock completely or remove specific items from UI components to create customized editing experiences."
platform: ios
url: "https://img.ly/docs/cesdk/ios/user-interface/customization/hide-elements-fe945c/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [User Interface](https://img.ly/docs/cesdk/ios/user-interface-5a089a/) > [Customization](https://img.ly/docs/cesdk/ios/user-interface/customization-72b2f8/) > [Hide Elements](https://img.ly/docs/cesdk/ios/user-interface/customization/hide-elements-fe945c/)

---

```swift file=@cesdk_swift_examples/editor-guides-customization-hide-elements/HideElementsEditorSolution.swift reference-only
import IMGLYDesignEditor
import SwiftUI

/// Design Editor demonstrating how to hide UI elements.
///
/// This example shows how to:
/// - Hide the dock completely (the only UI component that fully hides)
/// - Remove specific items from any UI component
/// - Understand the distinction between hiding and removing
struct HideElementsEditorSolution: View {
  let settings = EngineSettings(
    license: secrets.licenseKey,
    userID: "<your unique user id>",
  )

  // To hide the dock completely, provide an empty closure to .imgly.dockItems
  // The dock is the only UI component that fully hides when given no items
  var editorWithHiddenDock: some View {
    DesignEditor(settings)
      .imgly.dockItems { _ in
        // Empty - dock will be completely hidden
      }
  }

  // To remove specific items from any component, use the modify variants
  // The component container remains visible, only the specified items are removed
  var editorWithRemovedItems: some View {
    DesignEditor(settings)
      .imgly.modifyDockItems { _, items in
        items.remove(id: Dock.Buttons.ID.elementsLibrary)
        items.remove(id: Dock.Buttons.ID.shapesLibrary)
      }
      .imgly.modifyNavigationBarItems { _, items in
        items.remove(id: NavigationBar.Buttons.ID.undo)
        items.remove(id: NavigationBar.Buttons.ID.redo)
      }
  }

  @State private var isPresented = false
  @State private var showHiddenDock = true

  var body: some View {
    VStack {
      Toggle("Hide Dock Completely", isOn: $showHiddenDock)
        .padding()

      Button("Use the Editor") {
        isPresented = true
      }
    }
    .fullScreenCover(isPresented: $isPresented) {
      ModalEditor {
        if showHiddenDock {
          editorWithHiddenDock
        } else {
          editorWithRemovedItems
        }
      }
    }
  }
}

#Preview {
  HideElementsEditorSolution()
}
```

Control UI visibility through complete component hiding or selective item removal across editor components.

We configure UI element visibility through two distinct approaches: hiding entire components or removing specific items while keeping containers visible.

![Editor with hidden dock](./assets/ios.hero.webp)

Explore the complete code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/editor-guides-customization-hide-elements).

## Understanding Hide vs. Remove

CE.SDK iOS provides two approaches for controlling UI element visibility:

**Hiding Components** removes the entire UI component from the view hierarchy. We provide an empty closure to `.imgly.dockItems`, which hides the dock container and background completely. This capability is dock-specific—other components don't support full hiding.

**Removing Items** selectively removes individual buttons while keeping the component container visible. We use `.imgly.modify[Component]Items` modifiers with `items.remove(id:)` to remove specific buttons from any component.

**Key Distinction**:

| Approach | Method | Result | Components |
|----------|--------|--------|------------|
| **Hide Component** | `.imgly.dockItems { _ in }` | Entire container hidden | Dock only |
| **Remove Items** | `.modify[Component]Items { _, items in items.remove(id:) }` | Container visible, items removed | All components |

**Why the Difference?**

The dock supports complete hiding because it's a self-contained toolbar. Other components (Navigation Bar, Canvas Menu, Inspector Bar) use SwiftUI layout patterns where the container always renders—removing items affects only the buttons, not the component structure.

## Hiding the Dock

We hide the dock completely by providing an empty closure to `.imgly.dockItems`:

```swift highlight-hideElements-dock
  // To hide the dock completely, provide an empty closure to .imgly.dockItems
  // The dock is the only UI component that fully hides when given no items
  var editorWithHiddenDock: some View {
    DesignEditor(settings)
      .imgly.dockItems { _ in
        // Empty - dock will be completely hidden
      }
  }
```

**Key Points**:

- Only UI component supporting complete container hiding
- Background and all content removed from view hierarchy
- Useful for minimal or focused editing modes
- Cannot be applied to other components (Navigation Bar, Canvas Menu, Inspector Bar)

**When to Hide the Dock**:

- Distraction-free editing experiences
- Custom toolbar implementations
- Minimal interfaces for specific workflows
- Full-screen canvas-focused modes

## Removing Specific Items

We remove individual items from any component using `.modify[Component]Items` with `items.remove(id:)`:

```swift highlight-hideElements-remove
  // To remove specific items from any component, use the modify variants
  // The component container remains visible, only the specified items are removed
  var editorWithRemovedItems: some View {
    DesignEditor(settings)
      .imgly.modifyDockItems { _, items in
        items.remove(id: Dock.Buttons.ID.elementsLibrary)
        items.remove(id: Dock.Buttons.ID.shapesLibrary)
      }
      .imgly.modifyNavigationBarItems { _, items in
        items.remove(id: NavigationBar.Buttons.ID.undo)
        items.remove(id: NavigationBar.Buttons.ID.redo)
      }
  }
```

**Key Points**:

- Container remains visible, only specified buttons removed
- Works across all components (Dock, Navigation Bar, Canvas Menu, Inspector Bar)
- Use component-specific ID enums (e.g., `Dock.Buttons.ID.*`)
- Multiple items can be removed in sequence

### Removing from Dock

```swift highlight-hideElements-dockRemove
.imgly.modifyDockItems { _, items in
  items.remove(id: Dock.Buttons.ID.elementsLibrary)
  items.remove(id: Dock.Buttons.ID.shapesLibrary)
}
```

We use `Dock.Buttons.ID.*` to reference dock buttons for removal.

### Removing from Navigation Bar

```swift highlight-hideElements-navbarRemove
.imgly.modifyNavigationBarItems { _, items in
  items.remove(id: NavigationBar.Buttons.ID.undo)
  items.remove(id: NavigationBar.Buttons.ID.redo)
}
```

We use `NavigationBar.Buttons.ID.*` to reference navigation bar buttons for removal.

### Removing from Other Components

The same pattern applies to all components:

```swift
// Canvas Menu
.imgly.modifyCanvasMenuItems { _, items in
  items.remove(id: CanvasMenu.Buttons.ID.bringForward)
  items.remove(id: CanvasMenu.Buttons.ID.sendBackward)
}

// Inspector Bar
.imgly.modifyInspectorBarItems { _, items in
  items.remove(id: InspectorBar.Buttons.ID.crop)
  items.remove(id: InspectorBar.Buttons.ID.filter)
}
```

> **Note:** The component container always remains visible when removing items. Only the dock supports complete container hiding through `.imgly.dockItems { _ in }`.

## Common Use Cases

### Hide Dock for Distraction-Free Editing

We hide the dock completely to create focused editing experiences:

```swift
DesignEditor(settings)
  .imgly.dockItems { _ in
    // Empty - dock hidden
  }
```

**Use when**: Maximizing canvas space, creating minimal interfaces, or implementing custom toolbars.

### Remove Specific Items to Simplify Interface

We remove individual buttons to streamline the interface for specific workflows:

```swift
DesignEditor(settings)
  .imgly.modifyDockItems { _, items in
    // Keep only essential tools
    items.remove(id: Dock.Buttons.ID.stickersLibrary)
    items.remove(id: Dock.Buttons.ID.shapesLibrary)
  }
```

**Use when**: Limiting functionality, creating beginner-friendly interfaces, or enforcing workflow constraints.

### Limit Navigation Options

We remove navigation buttons to control user flow:

```swift
DesignEditor(settings)
  .imgly.modifyNavigationBarItems { _, items in
    // Remove undo/redo for simpler interface
    items.remove(id: NavigationBar.Buttons.ID.undo)
    items.remove(id: NavigationBar.Buttons.ID.redo)
  }
```

**Use when**: Guided workflows, simplified editing modes, or workflow enforcement.

## How Hide and Remove Interact

**Hide and Remove are Independent**:

- Hiding the dock (`.imgly.dockItems { _ in }`) affects the entire component
- Removing items (`.imgly.modifyDockItems { _, items in }`) affects individual buttons
- We can use both: hide dock, remove items from other components

**Example Combining Both**:

```swift
DesignEditor(settings)
  .imgly.dockItems { _ in
    // Hide dock completely
  }
  .imgly.modifyNavigationBarItems { _, items in
    // Remove specific navigation buttons
    items.remove(id: NavigationBar.Buttons.ID.undo)
  }
```

## Troubleshooting

### Dock Not Hiding

**Symptom**: Dock still visible after providing empty closure

**Causes**:

- Using `.modifyDockItems` instead of `.dockItems`
- Closure not actually empty (contains code)

**Solutions**:

```swift
// ✅ Correct - hides dock completely
.imgly.dockItems { _ in
  // Empty - dock hidden
}

// ❌ Wrong - modifies items but doesn't hide container
.imgly.modifyDockItems { _, items in
  // Even if empty, container remains visible
}
```

### Other Components Not Hiding

**Symptom**: Navigation Bar, Canvas Menu, or Inspector Bar still visible with empty closures

**Cause**: Only dock supports complete container hiding

**Solution**:

```swift
// ❌ Won't hide navigation bar container
.imgly.navigationBarItems { _ in }

// ✅ Remove all items instead
.imgly.modifyNavigationBarItems { _, items in
  items.remove(id: NavigationBar.Buttons.ID.undo)
  items.remove(id: NavigationBar.Buttons.ID.redo)
  items.remove(id: NavigationBar.Buttons.ID.export)
  items.remove(id: NavigationBar.Buttons.ID.closeEditor)
}
```

> **Note:** Even after removing all items, the component container remains visible. This is by design—only the dock supports full hiding.

### Items Still Visible After Remove

**Symptom**: Button still appears after calling `items.remove(id:)`

**Causes**:

- Wrong component ID enum (e.g., using `Dock.Buttons.ID` in navigation bar)
- Typo in ID
- Modify closure not being called

**Solutions**:

```swift
// ✅ Use correct component's ID enum
.imgly.modifyDockItems { _, items in
  items.remove(id: Dock.Buttons.ID.elementsLibrary)  // Dock ID for dock
}

.imgly.modifyNavigationBarItems { _, items in
  items.remove(id: NavigationBar.Buttons.ID.undo)  // Navbar ID for navbar
}

// ❌ Wrong - mixing component IDs
.imgly.modifyDockItems { _, items in
  items.remove(id: NavigationBar.Buttons.ID.undo)  // Wrong component!
}
```

### Container Remains Visible

**Symptom**: Component background/container still visible after removing all items

**Cause**: Expected behavior—only dock supports container hiding

**Solution**: This is by design. For components other than dock, removing all items leaves an empty container. If container visibility is critical, consider layout adjustments or alternative UI structures.

### Error: ID Does Not Exist

**Symptom**: Runtime error `The 'remove' operation was invoked with id '...' which does not exist`

**Causes**:

- Button ID doesn't exist in component's default configuration
- Typo in ID string
- Button already removed earlier

**Solutions**:

```swift
// ✅ Verify button exists in component
// Check Dock.Buttons.ID, NavigationBar.Buttons.ID, etc. enums

// ✅ Use ID constants, not strings
items.remove(id: Dock.Buttons.ID.elementsLibrary)  // Correct

// ❌ Don't use string literals
items.remove(id: "elementsLibrary")  // Error-prone

// ✅ Don't remove same ID twice
items.remove(id: Dock.Buttons.ID.elementsLibrary)
// items.remove(id: Dock.Buttons.ID.elementsLibrary)  // Error!
```

## Next Steps

Explore related UI customization guides:

- [Customize Dock](https://img.ly/docs/cesdk/ios/user-interface/customization/dock-cb916c/) - Full dock customization patterns
- [Customize Navigation Bar](https://img.ly/docs/cesdk/ios/user-interface/customization/navigation-bar-4e5d39/) - Navigation bar configuration
- [Rearrange Buttons](https://img.ly/docs/cesdk/ios/user-interface/customization/rearrange-buttons-97022a/) - Button positioning across components
- [Add a New Button](https://img.ly/docs/cesdk/ios/user-interface/ui-extensions/add-new-button-74884d/) - Add custom buttons to components



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
