# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/CodeEditor.md

# [CodeEditor](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor)

A Panel subclass which encapsulates a [Monaco](https://bryntum.com/docs/gantt/api/https://microsoft.github.io/monaco-editor/) editor to provide rich editing of text.

This requires the Monaco editor to be installed as a Node module, and simply requires a [path](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#config-codePath) to a local `node_modules` directory.

Editing text is as simple as setting the [text](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#config-text) and [language](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#config-language) properties.

```
const
    editorPanel = new CodeEditor({
        codePath : 'node_modules/monaco-editor',
        width    : 1000,
        height   : 600,
        title    : 'This is just a Panel',
        text     : 'This is the text to edit',
        language : 'markdown',
        appendTo : document.body
    }),
    // Direct access to the Monaco Editor API
    monaco = await editorPanel.editorReady;
```

The CodeEditor loads the required modules dynamically from the [codePath](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#config-codePath) and fulfills the [editorReady](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#property-editorReady) Promise, yielding the Monaco editor when it is ready for interaction.

Status bar
----------

The [bottom toolbar](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#property-bbar) of this Panel is used as a status bar. You may reconfigure it or its `items` in the usual way. There are three items provided by default.

These may all be accessed using this Panel's [widgetMap](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#property-widgetMap).

These may all be styled using the selector `[ref="widgetName"]` where "widgetName" is one of the names listed below:

* `readOnly` A read-only indicator which by default uses the Font-Awesome `fa-lock` glyph to indicate that the editor is read-only.
* `status` A widget which may be used to display textual status messages.
* `cursorPos` A widget which displays the current cursor position.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[codePath](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#config-codePath)
The path from which to load the Monaco editor.

For example:

```
{
  codePath : 'node_modules/monaco-editor'
}
```

[editor](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#config-editor)
An editor configuration object to be passed to https://microsoft.github.io/monaco-editor/docs.html#functions/editor.create.html

[readOnly](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#config-readOnly)
The read-only state of the editor may be set and read. This state is by default reflected by an icon in the bottom toolbar.

[text](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#config-text)
The text being edited may be set and read using this property.

[language](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#config-language)
The language being edited may be set and read using this property.

[theme](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#config-theme)
The Monaco theme to use. If not specified, it defaults to `'vs'`;

[status](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#config-status)
The status message displayed un the bottom toolbar may be set and read using this property.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCodeEditor](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#property-isCodeEditor)
Identifies an object as an instance of [CodeEditor](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor) class, or subclass thereof.

[isCodeEditor](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#property-isCodeEditor-static)
Identifies an object as an instance of [CodeEditor](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor) class, or subclass thereof.

[editor](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#property-editor)
The [Monaco](https://bryntum.com/docs/gantt/api/https://microsoft.github.io/monaco-editor/) editor instance. Use this property to manipulate the editor according to https://microsoft.github.io/monaco-editor/typedoc/index.html

Note that this will only exist when the editor has been loaded from the [codePath](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#config-codePath).

This will be indicated by the [editorReady](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#property-editorReady) property which yields the monaco editor as its value.

[readOnly](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#property-readOnly)
The read-only state of the editor may be set and read. This state is by default reflected by an icon in the bottom toolbar.

[text](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#property-text)
The text being edited may be set and read using this property.

[language](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#property-language)
The language being edited may be set and read using this property.

[theme](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#property-theme)
The Monaco theme to use. If not specified, it defaults to `'vs'`;

[status](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#property-status)
The status message displayed un the bottom toolbar may be set and read using this property.

[editorReady](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#property-editorReady)
A promise which resolves when the Monaco editor is loaded from the [codePath](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#config-codePath) and ready for use which yields the Monaco editor instance.

[codeModel](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#property-codeModel)
An instance of https://microsoft.github.io/monaco-editor/docs.html#interfaces/editor.ITextModel.html which is handling the editing of the current [text](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#property-text).

This is created every time [text](https://bryntum.com/docs/gantt/api/#Core/widget/CodeEditor#property-text) is set.

## Functions

Functions are methods available for calling on the class

[construct](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#function-construct)
Constructor for Code Editor.

[focus](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#function-focus)
Focuses the Monaco editor

[loadText](https://bryntum.com/docs/gantt/api/Core/widget/CodeEditor#function-loadText)
Loads text into the editor.
