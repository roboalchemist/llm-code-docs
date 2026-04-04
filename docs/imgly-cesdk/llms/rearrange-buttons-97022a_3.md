# Source: https://img.ly/docs/cesdk/macos/user-interface/customization/rearrange-buttons-97022a/

---
title: "Rearrange Buttons"
description: "Reorder UI buttons across editor components to guide user actions and streamline workflows."
platform: macos
url: "https://img.ly/docs/cesdk/macos/user-interface/customization/rearrange-buttons-97022a/"
---

> This is one page of the CE.SDK macOS documentation. For a complete overview, see the [macOS Documentation Index](https://img.ly/docs/cesdk/macos.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/macos/llms-full.txt).

---

```swift file=@cesdk_swift_examples/editor-guides-customization-rearrange-buttons/RearrangeButtonsEditorSolution.swift reference-only
// swiftlint:disable unused_closure_parameter
// swiftformat:disable unusedArguments
import IMGLYDesignEditor
import SwiftUI

struct RearrangeButtonsEditorSolution: View {
  let settings = EngineSettings(license: secrets.licenseKey,
                                userID: "<your unique user id>")

  var editor: some View {
    DesignEditor(settings)
      .imgly.modifyNavigationBarItems { context, items in
        // Move undo/redo to the leading position
        items.remove(id: NavigationBar.Buttons.ID.undo)
        items.remove(id: NavigationBar.Buttons.ID.redo)
        items.addFirst(placement: .topBarLeading) {
          NavigationBar.Buttons.undo()
          NavigationBar.Buttons.redo()
        }
      }
      .imgly.modifyCanvasMenuItems { context, items in
        // Keep only duplicate and delete, removing layer ordering options
        items.remove(id: CanvasMenu.Buttons.ID.bringForward)
        items.remove(id: CanvasMenu.Buttons.ID.sendBackward)
        items.remove(id: CanvasMenu.Buttons.ID.selectGroup)
      }
      .imgly.modifyDockItems { context, items in
        // Move text library to the beginning for text-focused workflows
        items.remove(id: Dock.Buttons.ID.textLibrary)
        items.addFirst {
          Dock.Buttons.textLibrary()
        }
      }
      .imgly.modifyInspectorBarItems { context, items in
        // Move duplicate button to appear before layer options
        items.remove(id: InspectorBar.Buttons.ID.duplicate)
        items.addBefore(id: InspectorBar.Buttons.ID.layer) {
          InspectorBar.Buttons.duplicate()
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
  RearrangeButtonsEditorSolution()
}
```

Reorder UI buttons across four editor contexts to match specific workflows and prioritize user actions.

We rearrange buttons in the Navigation Bar, Canvas Menu, Dock, and Inspector Bar using ArrayModifier operations to create workflow-optimized interfaces.

![Editor showing rearranged buttons](./assets/ios.hero.webp)

Explore the complete code sample on [GitHub](https://github.com/imgly/cesdk-swift-examples/tree/v$UBQ_VERSION$/editor-guides-customization-rearrange-buttons).

## Understanding Button Rearrangement

CE.SDK iOS uses a consistent pattern for reordering buttons across all UI components. We use `.imgly.modifyXXXItems` modifiers with `ArrayModifier` operations to rearrange buttons within each component.

**Shared Pattern Across Components**:

1. **Modifier Pattern** - All components use `.imgly.modifyXXXItems` modifiers
2. **ArrayModifier Operations** - Consistent API across all components
3. **Remove + Add Pattern** - To reorder, we remove from original position then add at new position
4. **ID-Based Targeting** - We reference buttons using predefined `Buttons.ID` enums

**Context Properties by Component**:

| Component | engine | eventHandler | assetLibrary | selection | state |
|-----------|--------|--------------|--------------|-----------|-------|
| NavigationBar | ✅\* | ✅ | ✅ | ❌ | ✅ |
| CanvasMenu | ✅ | ✅ | ✅ | ✅ | ❌ |
| Dock | ✅ | ✅ | ✅ | ❌ | ❌ |
| InspectorBar | ✅ | ✅ | ✅ | ✅ | ❌ |

\*engine is optional (nil during creation)

This shared pattern means learning to rearrange buttons in one component transfers directly to all other components.

## ArrayModifier Operations

All UI components support the same set of operations for rearranging buttons:

| Operation | Purpose | Throws on Missing ID |
|-----------|---------|---------------------|
| `items.addFirst(_:)` | Add items at beginning | No |
| `items.addLast(_:)` | Add items at end | No |
| `items.addBefore(id:_:)` | Insert before specific item | Yes ✅ |
| `items.addAfter(id:_:)` | Insert after specific item | Yes ✅ |
| `items.replace(id:_:)` | Replace existing item | Yes ✅ |
| `items.remove(id:)` | Remove item by ID | Yes ✅ |

**Important**: Operations that target specific button IDs throw an error if the ID does not exist or was already removed.

**Operation Order**: Operations are applied in a specific sequence:

1. `remove` - Buttons removed first
2. `addBefore` - Insertions before reference buttons
3. `replace` - Replacements of existing buttons
4. `addAfter` - Insertions after reference buttons
5. `addFirst`/`addLast` wrap the entire array

## Rearranging the Navigation Bar

The navigation bar contains essential controls at the editor's top, organized into three placement groups. We reorder buttons to prioritize frequently-used actions.

```swift highlight-rearrange-navbar
.imgly.modifyNavigationBarItems { context, items in
  // Move undo/redo to the leading position
  items.remove(id: NavigationBar.Buttons.ID.undo)
  items.remove(id: NavigationBar.Buttons.ID.redo)
  items.addFirst(placement: .topBarLeading) {
    NavigationBar.Buttons.undo()
    NavigationBar.Buttons.redo()
  }
}
```

**Placement Groups**:

The navigation bar organizes buttons into three distinct placement groups:

| Placement | Description | Common Uses |
|-----------|-------------|-------------|
| `.topBarLeading` | Left side | Close, back, settings |
| `.topBarTrailing` | Right side | Actions, help, export |
| `.principal` | Center | Title, important controls |

**Key Points**:

- Must specify placement group for navigation bar operations
- Use `items.remove(id:)` to remove from current position
- Use `items.addFirst(placement:)` to add at new position
- Access button IDs through `NavigationBar.Buttons.ID.*`

## Rearranging the Canvas Menu

The canvas menu appears when users select elements on the canvas. We reorder buttons to prioritize common selection actions.

```swift highlight-rearrange-canvas-menu
.imgly.modifyCanvasMenuItems { context, items in
  // Keep only duplicate and delete, removing layer ordering options
  items.remove(id: CanvasMenu.Buttons.ID.bringForward)
  items.remove(id: CanvasMenu.Buttons.ID.sendBackward)
  items.remove(id: CanvasMenu.Buttons.ID.selectGroup)
}
```

**Key Points**:

- Context-aware buttons change based on selection type
- Use `items.remove(id:)` to hide less-used options
- Simplified menus improve user focus
- Access button IDs through `CanvasMenu.Buttons.ID.*`

## Rearranging the Dock

The dock provides access to asset libraries and tools at the editor's bottom. We reorder buttons to match workflow priorities.

```swift highlight-rearrange-dock
.imgly.modifyDockItems { context, items in
  // Move text library to the beginning for text-focused workflows
  items.remove(id: Dock.Buttons.ID.textLibrary)
  items.addFirst {
    Dock.Buttons.textLibrary()
  }
}
```

**Key Points**:

- Most frequently accessed component
- No placement groups (single linear array)
- Use `addFirst`/`addLast` for priority positioning
- Use remove+add pattern to move buttons
- Access button IDs through `Dock.Buttons.ID.*`

## Rearranging the Inspector Bar

The inspector bar shows properties and actions for the selected element in the sidebar. We reorder buttons for common property workflows.

```swift highlight-rearrange-inspector-bar
.imgly.modifyInspectorBarItems { context, items in
  // Move duplicate button to appear before layer options
  items.remove(id: InspectorBar.Buttons.ID.duplicate)
  items.addBefore(id: InspectorBar.Buttons.ID.layer) {
    InspectorBar.Buttons.duplicate()
  }
}
```

**Key Points**:

- Dynamic content based on selection type
- Use `items.addBefore(id:)` for precise positioning
- Access button IDs through `InspectorBar.Buttons.ID.*`

## Advanced Techniques

### Conditional Reordering Based on Selection

Canvas Menu and Inspector Bar contexts include a `selection` property for conditional button reordering:

```swift
.imgly.modifyCanvasMenuItems { context, items in
  if let block = context.selection.block,
     let blockType = try? context.engine.block.getType(block) {

    if blockType == "//ly.img.ubq/text" {
      // Prioritize text-specific actions
      items.remove(id: CanvasMenu.Buttons.ID.editText)
      items.addFirst {
        CanvasMenu.Buttons.editText()
      }
    }
  }
}
```

### Complex Multi-Step Reordering

Group related buttons together for better organization:

```swift
.imgly.modifyDockItems { _, items in
  // Group all libraries at the start
  let libraryIDs = [
    Dock.Buttons.ID.textLibrary,
    Dock.Buttons.ID.imagesLibrary,
    Dock.Buttons.ID.shapesLibrary
  ]

  libraryIDs.forEach { items.remove(id: $0) }

  items.addFirst {
    Dock.Buttons.textLibrary()
    Dock.Buttons.imagesLibrary()
    Dock.Buttons.shapesLibrary()
  }
}
```

### Precise Relative Positioning

Use `addBefore` and `addAfter` for exact placement:

```swift
.imgly.modifyInspectorBarItems { _, items in
  items.remove(id: InspectorBar.Buttons.ID.duplicate)
  items.addBefore(id: InspectorBar.Buttons.ID.layer) {
    InspectorBar.Buttons.duplicate()
  }
}
```

## Troubleshooting

### Button Not Appearing After Rearrangement

**Symptom**: Button removed but doesn't appear in new location

**Cause**: Forgot to add button back after removing it

**Solution**:

```swift
// ✅ Correct - always pair remove with add
.imgly.modifyDockItems { _, items in
  items.remove(id: Dock.Buttons.ID.textLibrary)
  items.addFirst {
    Dock.Buttons.textLibrary()
  }
}
```

### Error: "ID Does Not Exist"

**Symptom**: Runtime error about missing ID

**Solutions**:

```swift
// ✅ Use correct component's ID enum
.imgly.modifyDockItems { _, items in
  items.remove(id: Dock.Buttons.ID.textLibrary)  // Dock ID
}

.imgly.modifyNavigationBarItems { _, items in
  items.remove(id: NavigationBar.Buttons.ID.undo)  // Navbar ID
}
```

### Button Order Not Changing

**Solutions**:

```swift
// For navigation bar, always specify placement
items.addFirst(placement: .topBarLeading) {
  NavigationBar.Buttons.export()
}

// For other components, verify reference button ID
items.addBefore(id: Dock.Buttons.ID.crop) {
  Dock.Buttons.filter()
}
```

### Navigation Bar Items Overlapping

**Solution**:

```swift
// Always specify placement for navigation bar
items.addFirst(placement: .topBarLeading) {
  NavigationBar.Buttons.export()
}

items.addLast(placement: .topBarTrailing) {
  NavigationBar.Buttons.undo()
}
```

## Next Steps

Explore related customization guides:

- [Customize Dock](https://img.ly/docs/cesdk/macos/user-interface/customization/dock-cb916c/) - Full dock customization
- [Canvas Menu](https://img.ly/docs/cesdk/macos/user-interface/customization/canvas-menu-0d2b5b/) - Customize canvas context menu
- [Inspector Bar](https://img.ly/docs/cesdk/macos/user-interface/customization/inspector-bar-8ca1cd/) - Configure property inspector



---

## More Resources

- **[macOS Documentation Index](https://img.ly/docs/cesdk/macos.md)** - Browse all macOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/macos/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/macos/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
