# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/TextField.md

# [TextField](https://bryntum.com/docs/gantt/api/Core/widget/TextField)

Text field widget, wraps native `<input type="text">`. Supports two [renditions](https://bryntum.com/docs/gantt/api/#Core/widget/TextField#config-rendition), `'outlined'` and `'filled'`:

This field can be used as an [editor](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-editor) for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column). It is used as the default editor for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column), [TemplateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TemplateColumn), [TreeColumn](https://bryntum.com/docs/gantt/api/#Grid/column/TreeColumn), and for other columns if another editor is not specified explicitly, or disabled by setting `false` value.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[minLength](https://bryntum.com/docs/gantt/api/Core/widget/TextField#config-minLength)
The min number of characters for the input field

[maxLength](https://bryntum.com/docs/gantt/api/Core/widget/TextField#config-maxLength)
The max number of characters for the input field

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/TextField#config-rendition)
Predefined style to use for the field. Possible values are:

* `'outlined'` (default)
* `'filled'`

The supplied value will be part of the field's class list, as `b-text-field-{rendition}`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTextField](https://bryntum.com/docs/gantt/api/Core/widget/TextField#property-isTextField)
Identifies an object as an instance of [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField) class, or subclass thereof.

[isTextField](https://bryntum.com/docs/gantt/api/Core/widget/TextField#property-isTextField-static)
Identifies an object as an instance of [TextField](https://bryntum.com/docs/gantt/api/#Core/widget/TextField) class, or subclass thereof.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/TextField#property-rendition)
Predefined style to use for the field. Possible values are:

* `'outlined'` (default)
* `'filled'`

The supplied value will be part of the field's class list, as `b-text-field-{rendition}`.

## Functions

Functions are methods available for calling on the class

[getCurrentToken](https://bryntum.com/docs/gantt/api/Core/widget/TextField#function-getCurrentToken)
Returns the current token - the token that the cursor is within or adjacent to in the input field as separated by space, or the passed regular expression.
