# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/NumberColumn.md

# [NumberColumn](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn)

A column for showing/editing numbers.

Default editor is a [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField).

```
new Grid({
    appendTo : document.body,
    columns : [
        { type: 'number', min: 0, max : 100, field: 'score' }
    ]
});
```

Provide a [NumberFormat](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat) config as [format](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn#config-format) to be able to show currency. For example:

```
new Grid({
    appendTo : document.body,
    columns : [
        {
            type   : 'number',
            format : {
               style    : 'currency',
               currency : 'USD'
            }
        }
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[format](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#config-format)
The format to use for rendering numbers.

By default, the locale's default number formatter is used. For `en-US`, the locale default is a maximum of 3 decimal digits, using thousands-based grouping. This would render the number `1234567.98765` as `'1,234,567.988'`.

To round to whole integers, with a "," as a thousand delimiter:

```
format : '9,999.'
```

To display USD currency

```
format : {
    style    : 'currency',
    currency : 'USD',
    fraction : 0
}
```

Read more about the formatting options at [NumberFormat](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat)

[min](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#config-min)
The minimum value for the field used during editing.

[max](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#config-max)
The maximum value for the field used during editing.

[step](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#config-step)
Step size for the field used during editing. Also used when pressing up/down keys in the field.

[largeStep](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#config-largeStep)
Large step size, defaults to 10 \* `step`. Applied when pressing SHIFT and stepping either by click or when using the Up/Down keys.

[unit](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#config-unit)
Unit to append to displayed value.

[renderer](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#config-renderer)
Renderer function used to customize and style the number displayed in the cell. Return the cell text you want to display. Can also affect other aspects of the cell, such as styling.

You should never modify any records inside this method.

```
new Grid({
    columns : [
        { text : 'Temperature', type : 'number', renderer : ({ record, value }) => value + 'F' },
    ]
});
```

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[align](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#config-align)
Text align. Accepts `'left'`/`'center'`/`'right'` or direction neutral `'start'`/`'end'`

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isNumberColumn](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#property-isNumberColumn)
Identifies an object as an instance of [NumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn) class, or subclass thereof.

[isNumberColumn](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#property-isNumberColumn-static)
Identifies an object as an instance of [NumberColumn](https://bryntum.com/docs/gantt/api/#Grid/column/NumberColumn) class, or subclass thereof.

[format](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#property-format)
The format to use for rendering numbers.

By default, the locale's default number formatter is used. For `en-US`, the locale default is a maximum of 3 decimal digits, using thousands-based grouping. This would render the number `1234567.98765` as `'1,234,567.988'`.

To round to whole integers, with a "," as a thousand delimiter:

```
format : '9,999.'
```

To display USD currency

```
format : {
    style    : 'currency',
    currency : 'USD',
    fraction : 0
}
```

Read more about the formatting options at [NumberFormat](https://bryntum.com/docs/gantt/api/#Core/helper/util/NumberFormat)

[min](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#property-min)
The minimum value for the field used during editing.

[max](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#property-max)
The maximum value for the field used during editing.

[step](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#property-step)
Step size for the field used during editing. Also used when pressing up/down keys in the field.

[largeStep](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#property-largeStep)
Large step size, defaults to 10 \* `step`. Applied when pressing SHIFT and stepping either by click or when using the Up/Down keys.

[unit](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#property-unit)
Unit to append to displayed value.

[renderer](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#property-renderer)
Renderer function used to customize and style the number displayed in the cell. Return the cell text you want to display. Can also affect other aspects of the cell, such as styling.

You should never modify any records inside this method.

```
new Grid({
    columns : [
        { text : 'Temperature', type : 'number', renderer : ({ record, value }) => value + 'F' },
    ]
});
```

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[align](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#property-align)
Text align. Accepts `'left'`/`'center'`/`'right'` or direction neutral `'start'`/`'end'`

## Functions

Functions are methods available for calling on the class

[defaultRenderer](https://bryntum.com/docs/gantt/api/Grid/column/NumberColumn#function-defaultRenderer)
Renderer that displays a formatted number in the cell. If you create a custom renderer, and want to include the formatted number you can call `defaultRenderer` from it.

```
new Grid({
    columns: [
        {
            type   : 'number',
            text   : 'Total cost',
            field  : 'totalCost',
            format : {
                style    : 'currency',
                currency : 'USD'
            },
            renderer({ value }) {
                 return `Total cost: ${this.defaultRenderer({ value })}`;
            }
        }
    ]
}
```
