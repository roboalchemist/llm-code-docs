# Source: https://img.ly/docs/cesdk/android/concepts/undo-and-history-99479d/

---
title: "Undo and History"
description: "Manage undo and redo stacks in CE.SDK using multiple histories, callbacks, and API-based controls."
platform: android
url: "https://img.ly/docs/cesdk/android/concepts/undo-and-history-99479d/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Concepts](https://img.ly/docs/cesdk/android/concepts-c9ff51/) > [Undo and History](https://img.ly/docs/cesdk/android/concepts/undo-and-history-99479d/)

---

```kotlin reference-only
// Manage history stacks
val newHistory = engine.editor.createHistory()
val oldHistory = engine.editor.getActiveHistory()
engine.editor.setActiveHistory(newHistory)
engine.editor.destroyHistory(oldHistory)

engine.editor.onHistoryUpdated()
	.onEach { println("Editor history updated") }
	.launchIn(CoroutineScope(Dispatchers.Main))

// Push a new state to the undo stack
engine.editor.addUndoStep()

// Perform an undo, if possible.
if (engine.editor.canUndo()) {
	engine.editor.undo()
}

// Perform a redo, if possible.
if (engine.editor.canRedo()) {
	engine.editor.redo()
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to undo and redo steps in the `editor` API.

## Functions

```kotlin
fun createHistory(): History
```

- Brief: Create a history which consists of an undo/redo stack for editing operations.

There can be multiple. But only one can be active at a time.

- Returns the handle to the created history.

```kotlin
fun destroyHistory(history: History)
```

Destroy the given history, returns an error if the handle doesn't refer to a history.

- `history`: the history to be destroyed.

```kotlin
fun setActiveHistory(history: History)
```

Mark the given history as active, returns an error if the handle doesn't refer to a history.

All other histories get cleared from the active state. Undo/redo operations only apply to the active history.

- `history`: the history to be marked as active.

```kotlin
fun getActiveHistory(): History
```

Get the handle to the currently active history. If there's none it will be created.

- Returns the handle to the active history.

```kotlin
fun addUndoStep()
```

Adds a new history state to the stack, if undoable changes were made.

```kotlin
fun undo()
```

Undo one step in the history if an undo step is available.

```kotlin
fun canUndo(): Boolean
```

If an undo step is available.

- Returns true if an undo step is available.

```kotlin
fun redo()
```

Redo one step in the history if a redo step is available.

```kotlin
fun canRedo(): Boolean
```

If a redo step is available.

- Returns true if a redo step is available.

```kotlin
fun onHistoryUpdated(): Flow<Unit>
```

Subscribe to changes to the undo/redo history.

- Returns flow of history updates.

## Full Code

Here's the full code:

```kotlin
// Manage history stacks
val newHistory = engine.editor.createHistory()
val oldHistory = engine.editor.getActiveHistory()
engine.editor.setActiveHistory(newHistory)
engine.editor.destroyHistory(oldHistory)

engine.editor.onHistoryUpdated()
    .onEach { println("Editor history updated") }
    .launchIn(CoroutineScope(Dispatchers.Main))

// Push a new state to the undo stack
engine.editor.addUndoStep()

// Perform an undo, if possible.
if (engine.editor.canUndo()) {
    engine.editor.undo()
}

// Perform a redo, if possible.
if (engine.editor.canRedo()) {
    engine.editor.redo()
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
