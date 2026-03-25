# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/ColorColumn.md

# [ColorColumn](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn)

A column that displays color values (built-in color classes or CSS colors) as a colored element similar to the [ColorField](https://bryntum.com/docs/gantt/api/#Core/widget/ColorField). When the user clicks the element, a [ColorPicker](https://bryntum.com/docs/gantt/api/#Core/widget/ColorPicker) lets the user select from a range of colors.

```
new Grid({
   columns : [
      {
         type   : 'color',
         field  : 'color',
         text   : 'Color'
      }
   ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[colors](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn#config-colors)
The `colors` property can be an array of string CSS colors or of objects with `color` and `text` properties from which the user can choose from. This will override the [pickers default colors](https://bryntum.com/docs/gantt/api/#Core/widget/ColorPicker#config-colors).

Provide an array of string CSS colors:

```
new Grid({
   columns : [
      {
         type   : 'color',
         field  : 'color',
         text   : 'Color',
         colors : ['#00FFFF', '#F0FFFF', '#89CFF0', '#0000FF', '#7393B3']
      }
   ]
});
```

[colorNameAsValue](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn#config-colorNameAsValue)
By default, the color code (hex value etc.) is stored in the record field. If you want to store the color name instead, set this to `true`.

[showColorName](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn#config-showColorName)
Show the color name in addition to a colored swatch.

[addNoColorItem](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn#config-addNoColorItem)
Adds an option in the picker to set no background color

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isColorColumn](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn#property-isColorColumn)
Identifies an object as an instance of [ColorColumn](https://bryntum.com/docs/gantt/api/#Grid/column/ColorColumn) class, or subclass thereof.

[isColorColumn](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn#property-isColorColumn-static)
Identifies an object as an instance of [ColorColumn](https://bryntum.com/docs/gantt/api/#Grid/column/ColorColumn) class, or subclass thereof.

[colors](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn#property-colors)
The `colors` property can be an array of string CSS colors or of objects with `color` and `text` properties from which the user can choose from. This will override the [pickers default colors](https://bryntum.com/docs/gantt/api/#Core/widget/ColorPicker#config-colors).

Provide an array of string CSS colors:

```
new Grid({
   columns : [
      {
         type   : 'color',
         field  : 'color',
         text   : 'Color',
         colors : ['#00FFFF', '#F0FFFF', '#89CFF0', '#0000FF', '#7393B3']
      }
   ]
});
```

[colorNameAsValue](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn#property-colorNameAsValue)
By default, the color code (hex value etc.) is stored in the record field. If you want to store the color name instead, set this to `true`.

[showColorName](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn#property-showColorName)
Show the color name in addition to a colored swatch.

[addNoColorItem](https://bryntum.com/docs/gantt/api/Grid/column/ColorColumn#property-addNoColorItem)
Adds an option in the picker to set no background color
