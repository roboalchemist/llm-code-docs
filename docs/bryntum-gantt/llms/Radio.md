# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Radio.md

# [Radio](https://bryntum.com/docs/gantt/api/Core/widget/Radio)

The `Radio` widget wraps an `<input type="radio">` element.

Color can be specified, and you can optionally configure [text](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-text) to display in a label to the right of the radio button instead of, or in addition to, a standard field [label](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-label).

Nested Items
------------

A radio button can also have a [container](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-container) of additional [items](https://bryntum.com/docs/gantt/api/#Core/widget/Container#config-items). These items can be displayed immediately following the field's label (which is the default when there is only one item) or below the radio button. This can be controlled using the [inline](https://bryntum.com/docs/gantt/api/#Core/widget/Radio#config-inline) config.

In the demo below notice how additional fields are displayed for the checked radio button:

For a simpler way to create a set of radio buttons, see the [RadioGroup](https://bryntum.com/docs/gantt/api/#Core/widget/RadioGroup) widget.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[clearable](https://bryntum.com/docs/gantt/api/Core/widget/Radio#config-clearable)
Set this to `true` so that clicking a checked radio button will clear its checked state.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isRadio](https://bryntum.com/docs/gantt/api/Core/widget/Radio#property-isRadio)
Identifies an object as an instance of [Radio](https://bryntum.com/docs/gantt/api/#Core/widget/Radio) class, or subclass thereof.

[isRadio](https://bryntum.com/docs/gantt/api/Core/widget/Radio#property-isRadio-static)
Identifies an object as an instance of [Radio](https://bryntum.com/docs/gantt/api/#Core/widget/Radio) class, or subclass thereof.
