# Source: https://img.ly/docs/cesdk/ios/create-composition/group-and-ungroup-62565a/

---
title: "Group and Ungroup Objects"
description: "Group multiple elements to move or transform them together; ungroup to edit them individually."
platform: ios
url: "https://img.ly/docs/cesdk/ios/create-composition/group-and-ungroup-62565a/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Create and Edit Compositions](https://img.ly/docs/cesdk/ios/create-composition-db709c/) > [Group and Ungroup Objects](https://img.ly/docs/cesdk/ios/create-composition/group-and-ungroup-62565a/)

---

```swift reference-only
// Create blocks and append to scene
let member1 = try engine.block.create(.graphic)
let member2 = try engine.block.create(.graphic)
try engine.block.appendChild(to: scene, child: member1)
try engine.block.appendChild(to: scene, child: member2)

// Check whether the blocks may be grouped
if try engine.block.isGroupable([member1, member2]) {
  let group = try engine.block.group([member1, member2])
  try engine.block.setSelected(group, selected: true)
  try engine.block.enterGroup(group)
  try engine.block.setSelected(member1, selected: true)
  try engine.block.exitGroup(member1)
  try engine.block.ungroup(group)
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to group blocks through the `block` API. Groups form a cohesive unit.

## Grouping

Multiple blocks can be grouped together to form a cohesive unit.
A group being a block, it can itself be part of a group.

> **Note:** **What cannot be grouped*** A scene
> * A block that already is part of a group

```swift
public func isGroupable(_ ids: [DesignBlockID]) throws -> Bool
```

Confirms that a given set of blocks can be grouped together.

- `ids:`: A non-empty array of block ids.
- Returns: Whether the blocks can be grouped together.

```swift
public func group(_ ids: [DesignBlockID]) throws -> DesignBlockID
```

Group blocks together.

- `ids:`: A non-empty array of block ids.
- Returns: The block id of the created group.

```swift
public func ungroup(_ id: DesignBlockID) throws
```

Ungroups a group.

- `id:`: The group id from a previous call to `group`.

```swift
public func enterGroup(_ id: DesignBlockID) throws
```

Changes selection from selected group to a block within that group.
Nothing happens if `id` is not a group.
Required scope: "editor/select"

- `id:`: The group id from a previous call to `group`.

```swift
public func exitGroup(_ id: DesignBlockID) throws
```

Changes selection from a group's selected block to that group.
Nothing happens if the `id` is not part of a group.
Required scope: "editor/select"

- `id:`: A block id.

## Full Code

Here's the full code:

```swift
// Create blocks and append to scene
let member1 = try engine.block.create(.graphic)
let member2 = try engine.block.create(.graphic)
try engine.block.appendChild(to: scene, child: member1)
try engine.block.appendChild(to: scene, child: member2)

// Check whether the blocks may be grouped
if try engine.block.isGroupable([member1, member2]) {
  let group = try engine.block.group([member1, member2])
  try engine.block.setSelected(group, selected: true)
  try engine.block.enterGroup(group)
  try engine.block.setSelected(member1, selected: true)
  try engine.block.exitGroup(member1)
  try engine.block.ungroup(group)
}
```



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
