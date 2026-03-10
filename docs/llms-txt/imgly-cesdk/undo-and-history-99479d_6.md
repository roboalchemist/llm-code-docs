# Source: https://img.ly/docs/cesdk/mac-catalyst/concepts/undo-and-history-99479d/

---
title: "Undo and History"
description: "Manage undo and redo stacks in CE.SDK using multiple histories, callbacks, and API-based controls."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/concepts/undo-and-history-99479d/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/mac-catalyst/concepts-c9ff51/) > [Undo and History](https://img.ly/docs/cesdk/mac-catalyst/concepts/undo-and-history-99479d/)

---

```swift reference-only
// Manage history stacks
let newHistory = engine.editor.createHistory()
let oldHistory = engine.editor.getActiveHistory()
engine.editor.setActiveHistory(newHistory)
engine.editor.destroyHistory(oldHistory)

let historyTask = Task {
  for await _ in engine.editor.onHistoryUpdated {
    let canUndo = try engine.editor.canUndo()
    let canRedo = try engine.editor.canRedo()
    print("History updated: \(canUndo) \(canRedo)")
  }
}

// Push a new state to the undo stack
try engine.editor.addUndoStep()

// Perform an undo, if possible.
if try engine.editor.canUndo() {
  try engine.editor.undo()
}

// Perform a redo, if possible.
if try engine.editor.canRedo() {
  try engine.editor.redo()
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to undo and redo steps in the `editor` API.

## Functions

```swift
public func createHistory() -> History
```

Create a history which consists of an undo/redo stack for editing operations.
There can be multiple. But only one can be active at a time.

- Returns: The handle to the created history.

```swift
public func destroyHistory(_ history: History)
```

Destroy the given history, returns an error if the handle doesn't refer to a history.

- `history:`: The history to be destroyed.

```swift
public func setActiveHistory(_ history: History)
```

Mark the given history as active, returns an error if the handle doesn't refer to a history.
All other histories get cleared from the active state. Undo/redo operations only apply to the active history.

- `history:`: The history to be marked as active.

```swift
public func getActiveHistory() -> History
```

Get the handle to the currently active history. If there's none it will be created.

- Returns: The handle to the active history.

```swift
public func addUndoStep() throws
```

Adds a new history state to the stack, if undoable changes were made.

```swift
public func undo() throws
```

Undo one step in the history if an undo step is available.

```swift
public func canUndo() throws -> Bool
```

If an undo step is available.

- Returns: `true` if an undo step is available.

```swift
public func redo() throws
```

Redo one step in the history if a redo step is available.

```swift
public func canRedo() throws -> Bool
```

If a redo step is available.

- Returns: `true` if a redo step is available.

```swift
public var onHistoryUpdated: AsyncStream<Void> { get }
```

Subscribe to changes to the undo/redo history.

## Full Code

Here's the full code:

```swift
// Manage history stacks
let newHistory = engine.editor.createHistory()
let oldHistory = engine.editor.getActiveHistory()
engine.editor.setActiveHistory(newHistory)
engine.editor.destroyHistory(oldHistory)

let historyTask = Task {
  for await _ in engine.editor.onHistoryUpdated {
    let canUndo = try engine.editor.canUndo()
    let canRedo = try engine.editor.canRedo()
    print("History updated: \(canUndo) \(canRedo)")
  }
}

// Push a new state to the undo stack
try engine.editor.addUndoStep()

// Perform an undo, if possible.
if try engine.editor.canUndo() {
  try engine.editor.undo()
}

// Perform a redo, if possible.
if try engine.editor.canRedo() {
  try engine.editor.redo()
}
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
