# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/ColorField.md

# [ColorField](https://bryntum.com/docs/gantt/api/Core/widget/ColorField)

Field that displays a CSS color and lets the user select from a pre-defined [range of CSS colors](https://bryntum.com/docs/gantt/api/#Core/widget/ColorField#config-colors).

This field can be used as an [editor](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-editor) for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column).

This widget may be operated using the keyboard. `ArrowDown` opens the color picker, which itself is keyboard navigable.

```
const colorField = new ColorField({
  field: 'color'
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[colors](https://bryntum.com/docs/gantt/api/Core/widget/ColorField#config-colors)
The `colors` property can be an array of string CSS colors or of objects with `color` and `text` properties from which the user can chose from. This will override the [pickers default colors](https://bryntum.com/docs/gantt/api/#Core/widget/ColorPicker#config-colors).

Provide an array of string CSS colors:

```
new ColorField({
    colors : ['#00FFFF', '#F0FFFF', '#89CFF0', '#0000FF', '#7393B3']
});
```

[addNoColorItem](https://bryntum.com/docs/gantt/api/Core/widget/ColorField#config-addNoColorItem)
Adds an option in the picker to set no background color

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isColorField](https://bryntum.com/docs/gantt/api/Core/widget/ColorField#property-isColorField)
Identifies an object as an instance of [ColorField](https://bryntum.com/docs/gantt/api/#Core/widget/ColorField) class, or subclass thereof.

[isColorField](https://bryntum.com/docs/gantt/api/Core/widget/ColorField#property-isColorField-static)
Identifies an object as an instance of [ColorField](https://bryntum.com/docs/gantt/api/#Core/widget/ColorField) class, or subclass thereof.

[colors](https://bryntum.com/docs/gantt/api/Core/widget/ColorField#property-colors)
The `colors` property can be an array of string CSS colors or of objects with `color` and `text` properties from which the user can chose from. This will override the [pickers default colors](https://bryntum.com/docs/gantt/api/#Core/widget/ColorPicker#config-colors).

Provide an array of string CSS colors:

```
new ColorField({
    colors : ['#00FFFF', '#F0FFFF', '#89CFF0', '#0000FF', '#7393B3']
});
```

[addNoColorItem](https://bryntum.com/docs/gantt/api/Core/widget/ColorField#property-addNoColorItem)
Adds an option in the picker to set no background color
