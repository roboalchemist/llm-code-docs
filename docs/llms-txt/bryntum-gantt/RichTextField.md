# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/RichTextField.md

# [RichTextField](https://bryntum.com/docs/gantt/api/Core/widget/RichTextField)

An interface class designed to be used with rich text field editors such as TinyMCE, CKEditor or Quill.

This field uses a simple DIV as the input "field" which the libraries will use as their target element. To use this field, you should subclass this class and implement the `onPaint` method to initialize the rich text editor.

```
import RichTextField from './lib/Core/widget/RichTextField.js';

export default class TinyMceField extends RichTextField {
    static $name = 'TinyMceField';
    static type = 'tinymcefield';

    onPaint() {
        // Initialize TinyMCE when we have a target element
        globalThis.tinymce.init({
            target : this.input,
            inline : true,
            // Update the TinyMceField instance value silently when the TinyMCE content changes
            setup  : editor => editor.on('NodeChange', () => this.richText = editor.getContent())
        }).then(() => this.input.focus());
    }

    // Ensure the CellEdit feature is aware of our ownership of TinyMCEs floating toolbar element
    owns(target) {
        return super.owns(target) || target?.closest('.tox-tinymce');
    }
}

TinyMceField.initClass();
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRichTextField](https://bryntum.com/docs/gantt/api/Core/widget/RichTextField#property-isRichTextField)
Identifies an object as an instance of [RichTextField](https://bryntum.com/docs/gantt/api/#Core/widget/RichTextField) class, or subclass thereof.

[isRichTextField](https://bryntum.com/docs/gantt/api/Core/widget/RichTextField#property-isRichTextField-static)
Identifies an object as an instance of [RichTextField](https://bryntum.com/docs/gantt/api/#Core/widget/RichTextField) class, or subclass thereof.

[richText](https://bryntum.com/docs/gantt/api/Core/widget/RichTextField#property-richText)
Use this property to update this field´s value silently while the rich text contents of this field is being edited. Otherwise, it would reset caret position and completely overwrite the context.
