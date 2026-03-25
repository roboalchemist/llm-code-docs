# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/mixin/Labelable.md

# [Labelable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Labelable)

This mixin provides label functionality to [Field](https://bryntum.com/docs/gantt/api/#Core/widget/Field) and [FieldSet](https://bryntum.com/docs/gantt/api/#Core/widget/FieldSet).

Not to be used directly.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[label](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Labelable#config-label)
Label, prepended to field

[labelPosition](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Labelable#config-labelPosition)
Label position, either 'before' the field or 'above' the field

Leaving it out, or specifying `null`, lets the theme decide on label placement.

[labelCls](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Labelable#config-labelCls)
CSS class name or class names to add to any configured [label](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Labelable#config-label)

[labelWidth](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Labelable#config-labelWidth)
The width to apply to the `<label>` element. If a number is specified, `px` will be used.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isLabelable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Labelable#property-isLabelable)
Identifies an object as an instance of [Labelable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Labelable) class, or subclass thereof.

[isLabelable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Labelable#property-isLabelable-static)
Identifies an object as an instance of [Labelable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Labelable) class, or subclass thereof.

[label](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Labelable#property-label)
Get/set fields label. Please note that the Field needs to have a label specified from start for this to work, otherwise no element is created.
