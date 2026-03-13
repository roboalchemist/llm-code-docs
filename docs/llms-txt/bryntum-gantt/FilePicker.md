# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/FilePicker.md

# [FilePicker](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker)

A file input field wrapped into a [Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button). Clicking the button opens a browser file picker window. When files are chosen, badge appears showing amount of files. Hovering the button shows a tooltip with file names.

By default, only a single file is allowed.

```
let fileField = new FilePicker({
  fileFieldConfig : {
     multiple : true,
     accept   : "image/*"
  },
  buttonConfig : {
      text : 'Pick file...'
  },
  onChange({ files }) {
      // Do cool things
  }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[defaultBindProperty](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#config-defaultBindProperty)
The name of the property to set when a single value is to be applied to this FilePicker. Such as when used in a grid WidgetColumn, this is the property to which the column's `field` is applied.

[buttonConfig](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#config-buttonConfig)
Wrapper button config object. See [Button](https://bryntum.com/docs/gantt/api/#Core/widget/Button) for list of available configs.

[fileFieldConfig](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#config-fileFieldConfig)
Underlying field config object. See [FileField](https://bryntum.com/docs/gantt/api/#Core/widget/FileField) for list of available configs.

[showBadge](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#config-showBadge)
Set to `false` to hide the badge indicating the number of files selected

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFilePicker](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#property-isFilePicker)
Identifies an object as an instance of [FilePicker](https://bryntum.com/docs/gantt/api/#Core/widget/FilePicker) class, or subclass thereof.

[isFilePicker](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#property-isFilePicker-static)
Identifies an object as an instance of [FilePicker](https://bryntum.com/docs/gantt/api/#Core/widget/FilePicker) class, or subclass thereof.

[showBadge](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#property-showBadge)
Set to `false` to hide the badge indicating the number of files selected

[files](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#property-files)
List of selected files

## Functions

Functions are methods available for calling on the class

[clear](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#function-clear)
Clears field

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[change](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#event-change)
Fires after user closes file picker dialog.

[clear](https://bryntum.com/docs/gantt/api/Core/widget/FilePicker#event-clear)
Fires when field is cleared with [clear](https://bryntum.com/docs/gantt/api/#Core/widget/FilePicker#function-clear) method
