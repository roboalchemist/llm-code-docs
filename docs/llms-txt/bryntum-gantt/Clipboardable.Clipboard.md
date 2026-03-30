# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Clipboardable.Clipboard.md

# [Clipboardable.Clipboard](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable.Clipboard)

This class is used internally in Clipboardable to create a shared clipboard that can be used from multiple instances of different widgets.

Can read and write to native Clipboard API if allowed, but always holds a local `clipboard` as a fallback.
