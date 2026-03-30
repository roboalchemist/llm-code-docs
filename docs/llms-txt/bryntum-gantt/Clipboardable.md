# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Clipboardable.md

# [Clipboardable](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable)

Mixin for handling clipboard data.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[useNativeClipboard](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable#config-useNativeClipboard)
Set this to `true` to use native Clipboard API if it is available

[allowedDataSources](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable#config-allowedDataSources)
Configure which sources $$name this class allows pasting model data from. Accepts string or array. Unspecified accepts all. If source is not accepted, it will try to use the string value instead.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isClipboardable](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable#property-isClipboardable)
Identifies an object as an instance of [Clipboardable](https://bryntum.com/docs/gantt/api/#Core/mixin/Clipboardable) class, or subclass thereof.

[isClipboardable](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable#property-isClipboardable-static)
Identifies an object as an instance of [Clipboardable](https://bryntum.com/docs/gantt/api/#Core/mixin/Clipboardable) class, or subclass thereof.

[clipboard](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable#property-clipboard)
Gets the current shared Clipboard instance

## Functions

Functions are methods available for calling on the class

[writeToClipboard](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable#function-writeToClipboard)
Writes string data to the shared/native clipboard. Also saves a local copy of the string and the unconverted data.

But firstly, it will call beforeCopy function and wait for a response. If false, the copy will be prevented.

[readFromClipboard](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable#function-readFromClipboard)
Reads string data from the shared/native clipboard. If string matches current instance local clipboard data, a non-modified version will be return. Otherwise, a stringParser function will be called.

But firstly, it will call beforePaste function and wait for a response. If false, the paste will be prevented.

This function will also trigger a paste event on the clipboard instance.

[clearClipboard](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable#function-clearClipboard)
Clears the clipboard data

[transformClipboardText](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable#function-transformClipboardText)
Takes a clipboard text and returns the parsed `data`

[hasClipboardData](https://bryntum.com/docs/gantt/api/Core/mixin/Clipboardable#function-hasClipboardData)
Checks local clipboard if there is clipboard data present. If native clipboard API is available, this function will return `undefined`
