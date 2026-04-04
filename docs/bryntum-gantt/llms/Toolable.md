# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/mixin/Toolable.md

# [Toolable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Toolable)

A mixin that manages [tools](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Toolable#config-tools).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[tools](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Toolable#config-tools)
The [tools](https://bryntum.com/docs/gantt/api/#Core/widget/Tool) to add either before or after the `title` in the Panel header. Each property name is the reference by which an instantiated tool may be retrieved from the live `[tools](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Toolable#property-tools)` property.

[toolDefaults](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Toolable#config-toolDefaults)
An object containing config defaults for corresponding [tools](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Toolable#config-tools) objects with a matching name.

This object contains a key named `'*'` with default config properties to apply to all tools. This object provides the default `type` (\`'tool').

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isToolable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Toolable#property-isToolable)
Identifies an object as an instance of [Toolable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Toolable) class, or subclass thereof.

[isToolable](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Toolable#property-isToolable-static)
Identifies an object as an instance of [Toolable](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Toolable) class, or subclass thereof.

[tools](https://bryntum.com/docs/gantt/api/Core/widget/mixin/Toolable#property-tools)
The [tools](https://bryntum.com/docs/gantt/api/#Core/widget/Tool) as specified by the [tools](https://bryntum.com/docs/gantt/api/#Core/widget/mixin/Toolable#config-tools) configuration. Each is a [Tool](https://bryntum.com/docs/gantt/api/#Core/widget/Tool) instance which may be hidden, shown and observed and styled just like any other widget.
