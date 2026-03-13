# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/FileField.md

# [FileField](https://bryntum.com/docs/gantt/api/Core/widget/FileField)

A simple FileField widget that wraps the native `<input type="file" />` element.

There is a nicer styled wrapper for this field, see [FilePicker](https://bryntum.com/docs/gantt/api/#Core/widget/FilePicker)

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[multiple](https://bryntum.com/docs/gantt/api/Core/widget/FileField#config-multiple)
Set to `true` to allow picking multiple files. Note that when set to a truthy value, the field is set to accept multiple files, but the value returned will be an empty string since this is what is rendered into the HTML.

[accept](https://bryntum.com/docs/gantt/api/Core/widget/FileField#config-accept)
Comma-separated list of file extensions or MIME type to accept. E.g. ".jpg,.png,.doc" or "image/\*". Null by default, allowing all files.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFileField](https://bryntum.com/docs/gantt/api/Core/widget/FileField#property-isFileField)
Identifies an object as an instance of [FileField](https://bryntum.com/docs/gantt/api/#Core/widget/FileField) class, or subclass thereof.

[isFileField](https://bryntum.com/docs/gantt/api/Core/widget/FileField#property-isFileField-static)
Identifies an object as an instance of [FileField](https://bryntum.com/docs/gantt/api/#Core/widget/FileField) class, or subclass thereof.

[files](https://bryntum.com/docs/gantt/api/Core/widget/FileField#property-files)
Returns list of selected files

## Functions

Functions are methods available for calling on the class

[pickFile](https://bryntum.com/docs/gantt/api/Core/widget/FileField#function-pickFile)
Opens browser file picker

[clear](https://bryntum.com/docs/gantt/api/Core/widget/FileField#function-clear)
Clears field value
