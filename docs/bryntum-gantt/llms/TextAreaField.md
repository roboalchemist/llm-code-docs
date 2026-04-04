# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/TextAreaField.md

# [TextAreaField](https://bryntum.com/docs/gantt/api/Core/widget/TextAreaField)

TextAreaField widget for multiline text input. Wraps a native <textarea> HTML element.

```
const textAreaField = new TextAreaField({
  placeholder: 'Enter some text'
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[resize](https://bryntum.com/docs/gantt/api/Core/widget/TextAreaField#config-resize)
The resize style to apply to the `<textarea>` element.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/TextAreaField#config-rendition)
Predefined style to use for the field. Possible values are:

* `'outlined'` (default)
* `'filled'`

The supplied value will be part of the field's class list, as `b-text-field-{rendition}`.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isTextAreaField](https://bryntum.com/docs/gantt/api/Core/widget/TextAreaField#property-isTextAreaField)
Identifies an object as an instance of [TextAreaField](https://bryntum.com/docs/gantt/api/#Core/widget/TextAreaField) class, or subclass thereof.

[isTextAreaField](https://bryntum.com/docs/gantt/api/Core/widget/TextAreaField#property-isTextAreaField-static)
Identifies an object as an instance of [TextAreaField](https://bryntum.com/docs/gantt/api/#Core/widget/TextAreaField) class, or subclass thereof.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/TextAreaField#property-rendition)
Predefined style to use for the field. Possible values are:

* `'outlined'` (default)
* `'filled'`

The supplied value will be part of the field's class list, as `b-text-field-{rendition}`.
