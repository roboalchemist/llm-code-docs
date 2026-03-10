# Source: https://img.ly/docs/cesdk/android/create-composition/layer-management-18f07a/

---
title: "Layer Management"
description: "Organize design elements using a layer stack for precise control over stacking and visibility."
platform: android
url: "https://img.ly/docs/cesdk/android/create-composition/layer-management-18f07a/"
---

> This is one page of the CE.SDK Android documentation. For a complete overview, see the [Android Documentation Index](https://img.ly/docs/cesdk/android.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/android/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/android/guides-8d8b00/) > [Create and Edit Compositions](https://img.ly/docs/cesdk/android/create-composition-db709c/) > [Layers](https://img.ly/docs/cesdk/android/create-composition/layer-management-18f07a/)

---

```kotlin reference-only
engine.block.insertChild(parent = page, child = block, index = 0)
val parent = engine.block.getParent(block)
val childIds = engine.block.getChildren(block)
engine.block.appendChild(parent = parent, child = block)
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify the hierarchy of blocks through the `block` API.

## Manipulate the hierarchy of blocks

> **Note:** Only blocks that are direct or indirect children of a `page` block are
> rendered. Scenes without any `page` child may not be properly displayed by the
> CE.SDK editor.

```kotlin
fun getParent(block: DesignBlock): DesignBlock?
```

Query a block's parent.

- `block`: the block to query.

- Returns the parent's handle or null if the block has no parent.

```kotlin
fun getChildren(block: DesignBlock): List<DesignBlock>
```

Get all children of the given block. Children are sorted in their rendering order:

Last child is rendered in front of other children.

- `block`: the block to query.

- Returns a list of block ids.

```kotlin
fun insertChild(
    parent: DesignBlock,
    child: DesignBlock,
    index: Int,
)
```

Insert a new or existing child at a certain position in the parent's children.

Required scope: "editor/add"

- `parent`: the block to update.

- `child`: the child to insert. Can be an existing child of `parent`.

- `index`: the index to insert or move to.

```kotlin
fun appendChild(
    parent: DesignBlock,
    child: DesignBlock,
)
```

Appends a new or existing child to a block's children.

Required scope: "editor/add"

- `parent`: the block to update.

- `child`: the child to insert. Can be an existing child of `parent`.

When adding a block to a new parent, it is automatically removed from its previous parent.

## Full Code

Here's the full code:

```kotlin
engine.block.insertChild(parent = page, child = block, index = 0)
val parent = engine.block.getParent(block)
val childIds = engine.block.getChildren(block)
engine.block.appendChild(parent = parent, child = block)
```



---

## More Resources

- **[Android Documentation Index](https://img.ly/docs/cesdk/android.md)** - Browse all Android documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/android/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/android/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
