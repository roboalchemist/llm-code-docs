# Source: https://img.ly/docs/cesdk/android/create-composition/group-and-ungroup-62565a/

---
title: "Group and Ungroup Objects"
description: "Group multiple elements to move or transform them together; ungroup to edit them individually."
platform: android
url: "https://img.ly/docs/cesdk/android/create-composition/group-and-ungroup-62565a/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Compositions](https://img.ly/docs/cesdk/android/create-composition-db709c/) > [Group and Ungroup Objects](https://img.ly/docs/cesdk/android/create-composition/group-and-ungroup-62565a/)

---

```kotlin reference-only
// Create blocks and append to scene
val member1 = engine.block.create(DesignBlockType.Graphic)
val member2 = engine.block.create(DesignBlockType.Graphic)
engine.block.appendChild(scene, child = member1)
engine.block.appendChild(scene, child = member2)

// Check whether the blocks may be grouped
if (engine.block.isGroupable(listOf(member1, member2))) {
	val group = engine.block.group(listOf(member1, member2))
	engine.block.setSelected(group, selected = true)
	engine.block.enterGroup(group)
	engine.block.setSelected(member1, selected = true)
	engine.block.exitGroup(member1)
	engine.block.ungroup(group)
}
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to group blocks through the `block` API. Groups form a cohesive unit.

## Grouping

Multiple blocks can be grouped together to form a cohesive unit.
A group being a block, it can itself be part of a group.

> **Note:** **What cannot be grouped*** A scene
> * A block that already is part of a group

```kotlin
fun isGroupable(blocks: List<DesignBlock>): Boolean
```

Confirms that a given set of blocks can be grouped together.

- `blocks`: a non-empty array of block ids.

- Returns whether the blocks can be grouped together.

```kotlin
fun group(blocks: List<DesignBlock>): DesignBlock
```

Group blocks together.

- `blocks`: a non-empty array of block ids.

- Returns the block id of the created group.

```kotlin
fun ungroup(block: DesignBlock)
```

Ungroups a group.

- `block`: the group id from a previous call to `group`.

```kotlin
fun enterGroup(block: DesignBlock)
```

Changes selection from selected group to a block within that group.

Nothing happens if `block` is not a group.

Required scope: "editor/select"

- `block`: the group id from a previous call to `group`.

```kotlin
fun exitGroup(block: DesignBlock)
```

Changes selection from a group's selected block to that group.

Nothing happens if `block` is not a group.

Required scope: "editor/select"

- `block`: a block id.

## Full Code

Here's the full code:

```kotlin
// Create blocks and append to scene
val member1 = engine.block.create(DesignBlockType.Graphic)
val member2 = engine.block.create(DesignBlockType.Graphic)
engine.block.appendChild(scene, child = member1)
engine.block.appendChild(scene, child = member2)

// Check whether the blocks may be grouped
if (engine.block.isGroupable(listOf(member1, member2))) {
    val group = engine.block.group(listOf(member1, member2))
    engine.block.setSelected(group, selected = true)
    engine.block.enterGroup(group)
    engine.block.setSelected(member1, selected = true)
    engine.block.exitGroup(member1)
    engine.block.ungroup(group)
}
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
