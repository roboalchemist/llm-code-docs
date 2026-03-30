# Source: https://img.ly/docs/cesdk/mac-catalyst/create-composition/layer-management-18f07a/

---
title: "Layer Management"
description: "Organize design elements using a layer stack for precise control over stacking and visibility."
platform: mac-catalyst
url: "https://img.ly/docs/cesdk/mac-catalyst/create-composition/layer-management-18f07a/"
---

> This is one page of the CE.SDK Mac Catalyst documentation. For a complete overview, see the [Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/mac-catalyst/guides-8d8b00/) > [Create and Edit Compositions](https://img.ly/docs/cesdk/mac-catalyst/create-composition-db709c/) > [Layers](https://img.ly/docs/cesdk/mac-catalyst/create-composition/layer-management-18f07a/)

---

```swift reference-only
try engine.block.insertChild(into: page, child: block, at: 0)
let parent = try engine.block.getParent(block)
let childIds = try engine.block.getChildren(block)
try engine.block.appendChild(to: parent!, child: block)
```

In this example, we will show you how to use the [CreativeEditor SDK](https://img.ly/products/creative-sdk)'s CreativeEngine to modify the hierarchy of blocks through the `block` API.

## Manipulate the hierarchy of blocks

> **Note:** Only blocks that are direct or indirect children of a `page` block are
> rendered. Scenes without any `page` child may not be properly displayed by the
> CE.SDK editor.

```swift
public func getParent(_ id: DesignBlockID) throws -> DesignBlockID?
```

Query a block's parent.

- `id:`: The block to query.
- Returns: The parent's handle or `nil` if the block has no parent.

```swift
public func getChildren(_ id: DesignBlockID) throws -> [DesignBlockID]
```

Get all children of the given block. Children
are sorted in their rendering order: Last child is rendered
in front of other children.

- `id:`: The block to query.
- Returns: A list of block ids.

```swift
public func insertChild(into parent: DesignBlockID, child: DesignBlockID, at index: Int) throws
```

Insert a new or existing child at a certain position in the parent's children.
Required scope: "editor/add"

- `parent`: The block whose children should be updated.
- `child`: The child to insert. Can be an existing child of `parent`.
- `index`: The index to insert or move to.

```swift
public func appendChild(to parent: DesignBlockID, child: DesignBlockID) throws
```

Appends a new or existing child to a block's children.
Required scope: "editor/add"

- `parent`: The block whose children should be updated.
- `child`: The child to insert. Can be an existing child of `parent`.

When adding a block to a new parent, it is automatically removed from its previous parent.

## Full Code

Here's the full code:

```swift
try engine.block.insertChild(into: page, child: block, at: 0)
let parent = try engine.block.getParent(block)
let childIds = try engine.block.getChildren(block)
try engine.block.appendChild(to: parent!, child: block)
```



---

## More Resources

- **[Mac Catalyst Documentation Index](https://img.ly/docs/cesdk/mac-catalyst.md)** - Browse all Mac Catalyst documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/mac-catalyst/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/mac-catalyst/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
