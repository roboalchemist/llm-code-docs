# Source: https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content/placeholders-d9ba8a/

---
title: "Placeholders"
description: "Use placeholders to mark editable image, video, or text areas within a locked template layout."
platform: android
url: "https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content/placeholders-d9ba8a/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Use Templates](https://img.ly/docs/cesdk/android/create-templates-3aef79/) > [Insert Dynamic Content](https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content-53fad7/) > [Placeholders](https://img.ly/docs/cesdk/android/create-templates/add-dynamic-content/placeholders-d9ba8a/)

---

```kotlin reference-only
// Check if block supports placeholder behavior
if (engine.block.supportsPlaceholderBehavior(block)) {
	// Enable the placeholder behavior
	engine.block.setPlaceholderBehaviorEnabled(block, enabled = true)
	val placeholderBehaviorIsEnabled = engine.block.isPlaceholderBehaviorEnabled(block)

	// Enable the placeholder capabilities (interaction in Adopter mode)
	engine.block.setPlaceholderEnabled(block, enabled = true)
	val placeholderIsEnabled = engine.block.isPlaceholderEnabled(block)

	// Check if block supports placeholder controls
	if (engine.block.supportsPlaceholderControls(block)) {
		// Enable the visibility of the placeholder overlay pattern
		engine.block.setPlaceholderControlsOverlayEnabled(block, enabled = true)
		val overlayEnabled = engine.block.isPlaceholderControlsOverlayEnabled(block)

		// Enable the visibility of the placeholder button
		engine.block.setPlaceholderControlsButtonEnabled(block, enabled = true)
		val buttonEnabled = engine.block.isPlaceholderControlsButtonEnabled(block)
	}
}

```

In this example, we will demonstrate how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to manage placeholder behavior and controls through the block Api.

## Placeholder Behavior and Controls

```kotlin
fun supportsPlaceholderBehavior(block: DesignBlock): Boolean
```

Query whether the block supports placeholder behavior.

- `block`: the block to query.

- Returns whether the block supports placeholder behavior.

```kotlin
fun setPlaceholderBehaviorEnabled(
    block: DesignBlock,
    enabled: Boolean,
)
```

Enable or disable the placeholder behavior for a block.

- `block`: the block whose placeholder behavior should be enabled or disabled.

- `enabled`: Whether the placeholder behavior should be enabled or disabled.

```kotlin
fun isPlaceholderBehaviorEnabled(block: DesignBlock): Boolean
```

Query whether the placeholder behavior for a block is enabled.

- `block`: the block whose placeholder behavior state should be queried.

- Returns the enabled state of the block's placeholder behavior.

```kotlin
fun setPlaceholderEnabled(
    block: DesignBlock,
    enabled: Boolean,
)
```

Enable or disable the placeholder function for a block.

- `block`: the block whose placeholder function should be enabled or disabled.

- `enabled`: whether the function should be enabled or disabled.

```kotlin
fun isPlaceholderEnabled(block: DesignBlock): Boolean
```

Query whether the placeholder function for a block is enabled.

- `block`: the block whose placeholder function state should be queried.

- Returns the enabled state of the placeholder function.

```kotlin
fun supportsPlaceholderControls(block: DesignBlock): Boolean
```

Checks whether the block supports placeholder controls.

- `block`: The block to query.

- Returns whether the block supports placeholder controls.

```kotlin
fun setPlaceholderControlsOverlayEnabled(
    block: DesignBlock,
    enabled: Boolean,
)
```

Enable or disable the visibility of the placeholder overlay pattern for a block.

- `block`: The block whose placeholder overlay should be enabled or disabled.

- `enabled`: Whether the placeholder overlay should be shown or not.

```kotlin
fun isPlaceholderControlsOverlayEnabled(block: DesignBlock): Boolean
```

Query whether the placeholder overlay pattern for a block is shown.

- `block`: The block whose placeholder overlay visibility state should be queried.

- Returns the visibility state of the block's placeholder overlay pattern.

```kotlin
fun setPlaceholderControlsButtonEnabled(
    block: DesignBlock,
    enabled: Boolean,
)
```

Enable or disable the visibility of the placeholder button for a block.

- `block`: The block whose placeholder button should be shown or not.

- `enabled`: Whether the placeholder button should be shown or not.

```kotlin
fun isPlaceholderControlsButtonEnabled(block: DesignBlock): Boolean
```

Query whether the placeholder button for a block is shown.

- `block`: The block whose placeholder button visibility state should be queried.

- Returns the visibility state of the block's placeholder button.

## Full Code

Here's the full code:

```kotlin
// Check if block supports placeholder behavior
if (engine.block.supportsPlaceholderBehavior(block)) {
    // Enable the placeholder behavior
    engine.block.setPlaceholderBehaviorEnabled(block, enabled = true)
    val placeholderBehaviorIsEnabled = engine.block.isPlaceholderBehaviorEnabled(block)

    // Enable the placeholder capabilities (interaction in Adopter mode)
    engine.block.setPlaceholderEnabled(block, enabled = true)
    val placeholderIsEnabled = engine.block.isPlaceholderEnabled(block)

    // Check if block supports placeholder controls
    if (engine.block.supportsPlaceholderControls(block)) {
        // Enable the visibility of the placeholder overlay pattern
        engine.block.setPlaceholderControlsOverlayEnabled(block, enabled = true)
        val overlayEnabled = engine.block.isPlaceholderControlsOverlayEnabled(block)

        // Enable the visibility of the placeholder button
        engine.block.setPlaceholderControlsButtonEnabled(block, enabled = true)
        val buttonEnabled = engine.block.isPlaceholderControlsButtonEnabled(block)
    }
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
