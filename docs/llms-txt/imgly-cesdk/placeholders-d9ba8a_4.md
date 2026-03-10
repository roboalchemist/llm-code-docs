# Source: https://img.ly/docs/cesdk/ios/create-templates/add-dynamic-content/placeholders-d9ba8a/

---
title: "Placeholders"
description: "Use placeholders to mark editable image, video, or text areas within a locked template layout."
platform: ios
url: "https://img.ly/docs/cesdk/ios/create-templates/add-dynamic-content/placeholders-d9ba8a/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Create and Use Templates](https://img.ly/docs/cesdk/ios/create-templates-3aef79/) > [Insert Dynamic Content](https://img.ly/docs/cesdk/ios/create-templates/add-dynamic-content-53fad7/) > [Placeholders](https://img.ly/docs/cesdk/ios/create-templates/add-dynamic-content/placeholders-d9ba8a/)

---

```swift reference-only
// Check if block supports placeholder behavior
if try engine.block.supportsPlaceholderBehavior(block) {
  // Enable the placeholder behavior
  try engine.block.setPlaceholderBehaviorEnabled(block, enabled: true)
  let placeholderBehaviorIsEnabled = try engine.block.isPlaceholderBehaviorEnabled(block)
}

// Enable the placeholder capabilities (interaction in Adopter mode)
try engine.block.setPlaceholderEnabled(block, enabled: true)
let placeholderIsEnabled = try engine.block.isPlaceholderEnabled(block)

// Check if block supports placeholder controls
if try engine.block.supportsPlaceholderControls(block) {
  // Enable the visibility of the placeholder overlay pattern
  try engine.block.setPlaceholderControlsOverlayEnabled(block, enabled: true)
  let overlayEnabled = try engine.block.isPlaceholderControlsOverlayEnabled(block)

  // Enable the visibility of the placeholder button
  try engine.block.setPlaceholderControlsButtonEnabled(block, enabled: true)
  let buttonEnabled = try engine.block.isPlaceholderControlsButtonEnabled(block)
}
```

In this example, we will demonstrate how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to manage placeholder behavior and controls through the block API.

## Placeholder Behavior and Controls

```swift
public func supportsPlaceholderBehavior(_ id: DesignBlockID) throws -> Bool
```

Query if the given block supports placeholder behavior.

- `id:`: The block to query.
- Returns: `true`, if the block supports placeholder behavior.

```swift
public func setPlaceholderBehaviorEnabled(_ id: DesignBlockID, enabled: Bool) throws
```

Enable or disable the placeholder behavior for a block.

- `id`: The block whose placeholder behavior should be enabled or disabled.
- `enabled`: Whether the behavior should be enabled or disabled.

```swift
public func isPlaceholderBehaviorEnabled(_ id: DesignBlockID) throws -> Bool
```

Query if the given block has placeholder behavior enabled.

- `id:`: The block to query.
- Returns: `true`, if the block has placeholder behavior enabled.

```swift
public func setPlaceholderEnabled(_ id: DesignBlockID, enabled: Bool) throws
```

Enable or disable the placeholder function for a block.

- `id`: The block whose placeholder function should be enabled or disabled.
- `enabled`: Whether the function should be enabled or disabled.

```swift
public func isPlaceholderEnabled(_ id: DesignBlockID) throws -> Bool
```

Query whether the placeholder function for a block is enabled.

- `id:`: The block whose placeholder function state should be queried.
- Returns: The enabled state of the placeholder function.

```swift
public func supportsPlaceholderControls(_ id: DesignBlockID) throws -> Bool
```

Checks whether the block supports placeholder controls.

- `id:`: The block to query.
- Returns: `true`, if the block supports placeholder controls.

```swift
public func setPlaceholderControlsOverlayEnabled(_ id: DesignBlockID, enabled: Bool) throws
```

Enable or disable the visibility of the placeholder overlay pattern for a block.

- `id`: The block whose placeholder overlay should be enabled or disabled.
- `enabled`: Whether the placeholder overlay should be shown or not.

```swift
public func isPlaceholderControlsOverlayEnabled(_ id: DesignBlockID) throws -> Bool
```

Query whether the placeholder overlay pattern for a block is shown.

- `id:`: The block whose placeholder overlay visibility state should be queried.
- Returns: the visibility state of the block's placeholder overlay pattern.

```swift
public func setPlaceholderControlsButtonEnabled(_ id: DesignBlockID, enabled: Bool) throws
```

Enable or disable the visibility of the placeholder button for a block.

- `id`: The block whose placeholder button should be enabled or disabled.
- `enabled`: Whether the placeholder button should be shown or not.

```swift
public func isPlaceholderControlsButtonEnabled(_ id: DesignBlockID) throws -> Bool
```

Query whether the placeholder button for a block is shown.

- `id:`: The block whose placeholder button visibility state should be queried.
- Returns: the visibility state of the block's placeholder button.

## Full Code

Here's the full code:

```swift
// Check if block supports placeholder behavior
if try engine.block.supportsPlaceholderBehavior(block) {
  // Enable the placeholder behavior
  try engine.block.setPlaceholderBehaviorEnabled(block, enabled: true)
  let placeholderBehaviorIsEnabled = try engine.block.isPlaceholderBehaviorEnabled(block)
}

// Enable the placeholder capabilities (interaction in Adopter mode)
try engine.block.setPlaceholderEnabled(block, enabled: true)
let placeholderIsEnabled = try engine.block.isPlaceholderEnabled(block)

// Check if block supports placeholder controls
if try engine.block.supportsPlaceholderControls(block) {
  // Enable the visibility of the placeholder overlay pattern
  try engine.block.setPlaceholderControlsOverlayEnabled(block, enabled: true)
  let overlayEnabled = try engine.block.isPlaceholderControlsOverlayEnabled(block)

  // Enable the visibility of the placeholder button
  try engine.block.setPlaceholderControlsButtonEnabled(block, enabled: true)
  let buttonEnabled = try engine.block.isPlaceholderControlsButtonEnabled(block)
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
