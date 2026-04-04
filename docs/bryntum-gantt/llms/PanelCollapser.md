# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/panel/PanelCollapser.md

# [PanelCollapser](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapser)

Instances of this class are used to implement the [collapsible](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-collapsible) config.

For example, the following creates an instance of this class:

```
     {
         type        : 'panel',
         collapsible : true
     }
```

In this mode, a panel will collapse inline, within its container.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[animation](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapser#config-animation)
An animation config object.

[collapsed](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapser#config-collapsed)
Tracks whether or not the panel is collapsed.

[direction](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapser#config-direction)
Specifies the direction of panel collapse. The default value for this config is determined dynamically based on the [header's](https://bryntum.com/docs/gantt/api/#Core/widget/Panel#config-header) `dock` property and the containing layout's flex direction and, therefore, often does not need to be explicitly specified.

This config can be any of the following:

* `'up'`
* `'down'`
* `'left'`
* `'right'`

The default `direction` property is inferred from the position of the Panel in a flexbox layout.

If the Panel is the last child of a flexbox container, the `direction` is `'right'` for a horizontal flexbox layout and `'down'` for a vertical layout.

All other Panels in a flexbox container have the `direction` set to `'left'` for a horizontal layout and `'up'` for a vertical layout.

[collapseTooltip](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapser#config-collapseTooltip)
The tooltip to use for the collapse tool when the panel is expanded.

[expandTooltip](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapser#config-expandTooltip)
The tooltip to use for the expand tool when the panel is collapsed.

[supportAxis](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapser#config-supportAxis)
To support the panel's collapsed size, a minimum width and height may be assigned to the panel's header, based on this config and the panel's positioning style.

When a panel is collapsed it may need to retain the pre-collapse dimension perpendicular to the collapse [direction](https://bryntum.com/docs/gantt/api/#Core/widget/panel/PanelCollapser#config-direction). For example, the height of a panel that collapses to the left. The dimension parallel to the collapse (the width in this example) may also need to be supported using the pre-collapse size of the panel's header.

When this config is set to `true`, or by default when the owning panel is `position: absolute`, both axes are given a minimum size based on the panel's pre-collapse size. When this config is `false`, no minimum sizes will be assigned.

This config can also be a string containing the single letters 'w' and/or 'h' indicating which axis/axes of the panel header should be assigned a minimum size. That is, 'w' to assign only a minimum width, 'h' for only a minimum height, or 'wh' to assign both.

[tool](https://bryntum.com/docs/gantt/api/Core/widget/panel/PanelCollapser#config-tool)
The collapse/expand tool. The `type` of this instance should not be changed but the tool instance can be configured in other ways via this config property.
