# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/ColorPicker.md

# [ColorPicker](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker)

A color picker that displays a list of [colors](https://bryntum.com/docs/gantt/api/#Core/widget/ColorPicker#config-colors) which the user can select by using mouse or keyboard.

```
new ColorPicker({
   appendTo : 'container',
   width    : '10em',
   colorSelected(...args) {
       console.log(...args);
   }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[colorClasses](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#config-colorClasses)
Array of internal color class names, without prefix, like `red`, `violet` etc.

[colorClassPrefix](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#config-colorClassPrefix)
Prefix to be inserted before the color class names in [colorClasses](https://bryntum.com/docs/gantt/api/#Core/widget/ColorPicker#config-colorClasses), like `b-sch-`

[colors](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#config-colors)
The `colors` property can be an array of string CSS colors or of objects with `color` and `text` properties from which the user can chose from.

Provide an array of string CSS colors:

```
new ColorMenu({
    colors : ['#00FFFF', '#F0FFFF', '#89CFF0', '#0000FF', '#7393B3']
});
```

The colors can also be named. To do that, put them in an object with a `color` and a `text` property, like:

```
new ColorMenu({
   colors : [
       { color : '#000000', text : 'Black'},
       { color : '#FF0000', text : 'Red'},
       { color : '#00FF00', text : 'Green'},
       { color : '#0000FF', text : 'Blue'},
       { color : '#FFFFFF', text : 'White'},
   ]
});
```

Default colors are:

Red

Pink

Magenta

Purple

Violet

Indigo

Blue

Light-blue

Cyan

Teal

Green

Light-green

Lime

Yellow

Amber

Orange

Deep-orange

Brown

Lighter-gray

Light-gray

Gray

Black

[addNoColorItem](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#config-addNoColorItem)
Adds an option to set no background color

[columns](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#config-columns)
The color items is displayed in a grid layout with 6 columns as default. Change this to another number to affect appearance.

[colorSelected](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#config-colorSelected)
A callback function that will be called when the user selects a color in the picker.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isColorPicker](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#property-isColorPicker)
Identifies an object as an instance of [ColorPicker](https://bryntum.com/docs/gantt/api/#Core/widget/ColorPicker) class, or subclass thereof.

[isColorPicker](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#property-isColorPicker-static)
Identifies an object as an instance of [ColorPicker](https://bryntum.com/docs/gantt/api/#Core/widget/ColorPicker) class, or subclass thereof.

[colors](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#property-colors)
The `colors` property can be an array of string CSS colors or of objects with `color` and `text` properties from which the user can chose from.

Provide an array of string CSS colors:

```
new ColorMenu({
    colors : ['#00FFFF', '#F0FFFF', '#89CFF0', '#0000FF', '#7393B3']
});
```

The colors can also be named. To do that, put them in an object with a `color` and a `text` property, like:

```
new ColorMenu({
   colors : [
       { color : '#000000', text : 'Black'},
       { color : '#FF0000', text : 'Red'},
       { color : '#00FF00', text : 'Green'},
       { color : '#0000FF', text : 'Blue'},
       { color : '#FFFFFF', text : 'White'},
   ]
});
```

Default colors are:

Red

Pink

Magenta

Purple

Violet

Indigo

Blue

Light-blue

Cyan

Teal

Green

Light-green

Lime

Yellow

Amber

Orange

Deep-orange

Brown

Lighter-gray

Light-gray

Gray

Black

[addNoColorItem](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#property-addNoColorItem)
Adds an option to set no background color

[columns](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#property-columns)
The color items is displayed in a grid layout with 6 columns as default. Change this to another number to affect appearance.

## Typedefs

Typedefs are type definitions for the class

[ColorDescriptor](https://bryntum.com/docs/gantt/api/Core/widget/ColorPicker#typedef-ColorDescriptor)
Describes a color in the color picker.
