# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/experimental/FileDrop.md

# [FileDrop](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/FileDrop)

An experimental feature that lets users drop files on a Widget. The widget fires an event when a file is dropped onto it. In the event, you get access to the raw files as strings, that were parsed by calling `readAsBinaryString`.

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

NOTE: Currently only supports dropping one file at a time.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFileDrop](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/FileDrop#property-isFileDrop)
Identifies an object as an instance of [FileDrop](https://bryntum.com/docs/gantt/api/#Grid/feature/experimental/FileDrop) class, or subclass thereof.

[isFileDrop](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/FileDrop#property-isFileDrop-static)
Identifies an object as an instance of [FileDrop](https://bryntum.com/docs/gantt/api/#Grid/feature/experimental/FileDrop) class, or subclass thereof.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[fileDrop](https://bryntum.com/docs/gantt/api/Grid/feature/experimental/FileDrop#event-fileDrop)
Fired when a file is dropped on the widget element
