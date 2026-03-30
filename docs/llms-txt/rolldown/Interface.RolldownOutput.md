# Source: https://rolldown.rs/reference/Interface.RolldownOutput.md

---
url: /reference/Interface.RolldownOutput.md
---
# Interface: RolldownOutput

The generated bundle output.

## Extends

* `ExternalMemoryHandle`

## Properties

### output

* **Type**: \[[`OutputChunk`](Interface.OutputChunk.md), ...(OutputAsset | OutputChunk)\[]]

The list of chunks and assets in the generated bundle.

This includes at least one [`OutputChunk`](Interface.OutputChunk.md). It may also include more
[`OutputChunk`](Interface.OutputChunk.md) and/or [`OutputAsset`](Interface.OutputAsset.md)s.
