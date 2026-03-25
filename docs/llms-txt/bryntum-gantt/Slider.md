# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Slider.md

# [Slider](https://bryntum.com/docs/gantt/api/Core/widget/Slider)

A Slider widget wrapping the native <input type="range">

```
const slider = new Slider({
  text: 'Choose value'
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[text](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-text)
Text for the sliders internal label. Appends value if `showValue` is `true`

[showValue](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-showValue)
Show value in internal label (specify `true`), or in the thumb (specify 'thumb').

[showTooltip](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-showTooltip)
Show the slider value in a tooltip

[showSteps](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-showSteps)
Show the step markers

[min](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-min)
Minimum value

[max](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-max)
Maximum value

[step](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-step)
Step size

[value](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-value)
Initial value. `String` value allows to link value by reference name.

Example:

```
new Slider({
    text      : 'Tick height',
    value     : 100,
}

new Slider({
    text      : 'Tick height',
    value     : 'up.tickSize',
}
```

[valueLabelWidth](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-valueLabelWidth)
Width of the value label when `showValue` is enabled. If a number is specified, `px` will be used.

When not specified, the width will be calculated based on the longest possible value string.

[unit](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-unit)
Unit to display next to the value, when configured with `showValue : true`

[tooltip](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-tooltip)
A config object for the tooltip to show while hovering the slider.

[triggerChangeOnInput](https://bryntum.com/docs/gantt/api/Core/widget/Slider#config-triggerChangeOnInput)
By default, the [change](https://bryntum.com/docs/gantt/api/#Core/widget/Slider#event-change) event is fired when a change gesture is completed, ie: on the mouse up gesture of a drag.

Configure this as `true` to fire the [change](https://bryntum.com/docs/gantt/api/#Core/widget/Slider#event-change) event as the value changes _during_ a drag.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSlider](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-isSlider)
Identifies an object as an instance of [Slider](https://bryntum.com/docs/gantt/api/#Core/widget/Slider) class, or subclass thereof.

[isSlider](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-isSlider-static)
Identifies an object as an instance of [Slider](https://bryntum.com/docs/gantt/api/#Core/widget/Slider) class, or subclass thereof.

[input](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-input)
Get input element.

[text](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-text)
Text for the sliders internal label. Appends value if `showValue` is `true`

[min](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-min)
Minimum value

[max](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-max)
Maximum value

[step](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-step)
Step size

[value](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-value)
Initial value. `String` value allows to link value by reference name.

Example:

```
new Slider({
    text      : 'Tick height',
    value     : 100,
}

new Slider({
    text      : 'Tick height',
    value     : 'up.tickSize',
}
```

[valueLabelWidth](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-valueLabelWidth)
Width of the value label when `showValue` is enabled. If a number is specified, `px` will be used.

When not specified, the width will be calculated based on the longest possible value string.

[unit](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-unit)
Unit to display next to the value, when configured with `showValue : true`

[triggerChangeOnInput](https://bryntum.com/docs/gantt/api/Core/widget/Slider#property-triggerChangeOnInput)
By default, the [change](https://bryntum.com/docs/gantt/api/#Core/widget/Slider#event-change) event is fired when a change gesture is completed, ie: on the mouse up gesture of a drag.

Configure this as `true` to fire the [change](https://bryntum.com/docs/gantt/api/#Core/widget/Slider#event-change) event as the value changes _during_ a drag.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[input](https://bryntum.com/docs/gantt/api/Core/widget/Slider#event-input)
Fired while slider thumb is being dragged.

[change](https://bryntum.com/docs/gantt/api/Core/widget/Slider#event-change)
Fired after the slider value changes (on mouse up following slider interaction).
