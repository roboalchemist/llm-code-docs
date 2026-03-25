# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/PercentColumn.md

# [PercentColumn](https://bryntum.com/docs/gantt/api/Grid/column/PercentColumn)

A column that either displays a basic percent number, a rectangular progress bar, or a circular progress bar.

```
new Grid({
    appendTo : document.body,

    columns : [
        { type: 'percent', text: 'Progress', data: 'progress' }
    ]
});
```

Styling
-------

All cells in this column get a `b-percent-cell` class added.

If [mode](https://bryntum.com/docs/gantt/api/#Grid/column/PercentColumn#config-mode) is set to `bar` (default), the progress bar element in the cell gets a few special CSS classes added:

* If value equals 0, a `b-zero` CSS class is added to the circle element.
* If value is less than [lowThreshold](https://bryntum.com/docs/gantt/api/#Grid/column/PercentColumn#config-lowThreshold), a `b-low` CSS class is added to the bar element.
* If value equals 100, a `b-full` CSS class is added to the bar element.
* If value is > 100, a `b-over` CSS class is added to the bar element.

If [mode](https://bryntum.com/docs/gantt/api/#Grid/column/PercentColumn#config-mode) is set to `circle`, the progress circle element in the cell gets a few special CSS classes added:

* If value equals 0, a `b-empty` CSS class is added to the circle element.
* If value equals 100, a `b-full` CSS class is added to the circle element.
* If value is > 100, a `b-over` CSS class is added to the circle element.

Default editor is a [NumberField](https://bryntum.com/docs/gantt/api/#Core/widget/NumberField).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[mode](https://bryntum.com/docs/gantt/api/Grid/column/PercentColumn#config-mode)
This mode controls the rendering.

* `number` to render a formatted number value (e.g. 15%)
* `circle` to render a circular progress bar
* `bar` to render a plain rectangular progress bar

[showValue](https://bryntum.com/docs/gantt/api/Grid/column/PercentColumn#config-showValue)
Set to `true` to render the number value inside the bar, for example `'15%'`.

[lowThreshold](https://bryntum.com/docs/gantt/api/Grid/column/PercentColumn#config-lowThreshold)
When below this percentage the bar will have `b-low` CSS class added. By default, it turns the bar red.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPercentColumn](https://bryntum.com/docs/gantt/api/Grid/column/PercentColumn#property-isPercentColumn)
Identifies an object as an instance of [PercentColumn](https://bryntum.com/docs/gantt/api/#Grid/column/PercentColumn) class, or subclass thereof.

[isPercentColumn](https://bryntum.com/docs/gantt/api/Grid/column/PercentColumn#property-isPercentColumn-static)
Identifies an object as an instance of [PercentColumn](https://bryntum.com/docs/gantt/api/#Grid/column/PercentColumn) class, or subclass thereof.

[mode](https://bryntum.com/docs/gantt/api/Grid/column/PercentColumn#property-mode)
This mode controls the rendering.

* `number` to render a formatted number value (e.g. 15%)
* `circle` to render a circular progress bar
* `bar` to render a plain rectangular progress bar

[showValue](https://bryntum.com/docs/gantt/api/Grid/column/PercentColumn#property-showValue)
Set to `true` to render the number value inside the bar, for example `'15%'`.

[lowThreshold](https://bryntum.com/docs/gantt/api/Grid/column/PercentColumn#property-lowThreshold)
When below this percentage the bar will have `b-low` CSS class added. By default, it turns the bar red.

## Functions

Functions are methods available for calling on the class

[defaultRenderer](https://bryntum.com/docs/gantt/api/Grid/column/PercentColumn#function-defaultRenderer)
Renderer that displays a progress bar in the cell. If you create a custom renderer, and want to include the default markup you can call `defaultRenderer` from it.

```
new Grid({
    columns: [
        {
            type: 'percent',
            text : 'Percent',
            field : 'percent',
            renderer({ value }) {
                const domConfig = this.defaultRenderer();

                if (value > 100) {
                    domConfig.className = b-percent-bar-outer over-allocated';
                }

                return domConfig;
            }
        }
    ]
}
```
