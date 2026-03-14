# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/ButtonGroup.md

# [ButtonGroup](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup)

A specialized container that holds buttons, displaying them in a horizontal group with borders adjusted to make them stick together. Appearance in the built-in themes:

Trying to add other widgets than buttons will throw an exception.

```
new ButtonGroup({
    items : [
        { icon : 'fa-kiwi-bird' },
        { icon : 'fa-kiwi-otter' },
        { icon : 'fa-kiwi-rabbit' },
        ...
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[cls](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#config-cls)
Custom CSS class to add to element.

```
new ButtonGroup({
  cls : 'custom-css-class,
  items : [
      { icon : 'fa fa-unicorn', cls : 'button-cls-class' },
      ...
  ]
});
```

[items](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#config-items)
An array of Buttons or typed Button config objects.

[color](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#config-color)
Default color to apply to all contained buttons, see [Button#color](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-color). Individual buttons can override the default.

[useGap](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#config-useGap)
If you use gaps between your buttons, set this to `true` (controls whether to use border-radius for the button elements)

[toggleGroup](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#config-toggleGroup)
Set to `true` to turn the ButtonGroup into a toggle group, assigning a generated value to each contained buttons [toggleGroup config](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-toggleGroup). Individual buttons can override the default.

[toggleable](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#config-toggleable)
A two-element array containing the minimum and maximum number of toggleable buttons. If a single number is specified, it is converted to an array using that given value as the maximum and 1 is used as the minimum. If `true` is specified, it is equivalent to `[0, Infinity]`, allowing any buttons to be toggled independently or all buttons to be untoggled.

A value of `null` (the default) is similar to `toggleable : 1` unless [toggleGroup](https://bryntum.com/docs/gantt/api/#Core/widget/ButtonGroup#config-toggleGroup) is set, or individual buttons are configured with their own [toggleable](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-toggleable) or [toggleGroup](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-toggleGroup) values. If this config is used, `toggleable` and `toggleGroup` should not be assigned to individual buttons.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#config-rendition)
Predefined style to use for the buttons. Possible values are:

* `'elevated'` - Raised buttons with box-shadow
* `'filled'` - Filled with the primary color
* `'tonal'` - Filled with a faded shade of the primary color
* `'outlined'` - Outlined with borders and pale or transparent fill
* `'text'` - Transparent text-only button
* `'padded'` - Adds a background to the ButtonGroup and padding around the buttons + neutral background for toggled buttons
* `'padded-filled'` - Same as 'padded', but uses a primary color shade for the background of toggled buttons

The supplied value will be part of the button group's and each button's class list, as `b-button-{rendition}`.

If not value is supplied, it will search upwards for one, falling back to using the first button's rendition.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isButtonGroup](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#property-isButtonGroup)
Identifies an object as an instance of [ButtonGroup](https://bryntum.com/docs/gantt/api/#Core/widget/ButtonGroup) class, or subclass thereof.

[isButtonGroup](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#property-isButtonGroup-static)
Identifies an object as an instance of [ButtonGroup](https://bryntum.com/docs/gantt/api/#Core/widget/ButtonGroup) class, or subclass thereof.

[toggleable](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#property-toggleable)
A two-element array containing the minimum and maximum number of toggleable buttons. If a single number is specified, it is converted to an array using that given value as the maximum and 1 is used as the minimum. If `true` is specified, it is equivalent to `[0, Infinity]`, allowing any buttons to be toggled independently or all buttons to be untoggled.

A value of `null` (the default) is similar to `toggleable : 1` unless [toggleGroup](https://bryntum.com/docs/gantt/api/#Core/widget/ButtonGroup#config-toggleGroup) is set, or individual buttons are configured with their own [toggleable](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-toggleable) or [toggleGroup](https://bryntum.com/docs/gantt/api/#Core/widget/Button#config-toggleGroup) values. If this config is used, `toggleable` and `toggleGroup` should not be assigned to individual buttons.

[rendition](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#property-rendition)
Predefined style to use for the buttons. Possible values are:

* `'elevated'` - Raised buttons with box-shadow
* `'filled'` - Filled with the primary color
* `'tonal'` - Filled with a faded shade of the primary color
* `'outlined'` - Outlined with borders and pale or transparent fill
* `'text'` - Transparent text-only button
* `'padded'` - Adds a background to the ButtonGroup and padding around the buttons + neutral background for toggled buttons
* `'padded-filled'` - Same as 'padded', but uses a primary color shade for the background of toggled buttons

The supplied value will be part of the button group's and each button's class list, as `b-button-{rendition}`.

If not value is supplied, it will search upwards for one, falling back to using the first button's rendition.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[click](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#event-click)
Fires when a button in the group is clicked

[action](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#event-action)
Fires when the default action is performed on a button in the group (the button is clicked)

[toggle](https://bryntum.com/docs/gantt/api/Core/widget/ButtonGroup#event-toggle)
Fires when a button in the group is toggled (the [pressed](https://bryntum.com/docs/gantt/api/#Core/widget/Button#property-pressed) state is changed). If you need to process the pressed button only, consider using [click](https://bryntum.com/docs/gantt/api/#Core/widget/ButtonGroup#event-click) event or [action](https://bryntum.com/docs/gantt/api/#Core/widget/ButtonGroup#event-action) event.
