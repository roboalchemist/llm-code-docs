# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/mixin/DependencyTooltip.md

# [DependencyTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyTooltip)

Mixin that adds tooltip support to the [Dependencies](https://bryntum.com/docs/gantt/api/#Scheduler/feature/Dependencies) feature.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[showTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyTooltip#config-showTooltip)
Set to `true` to show a tooltip when hovering a dependency line

[showLagInTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyTooltip#config-showLagInTooltip)
Set to `true` to show the lag in the tooltip

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyTooltip#config-tooltipTemplate)
A template function allowing you to configure the contents of the tooltip shown when hovering a dependency line. You can return either an HTML string or a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object.

[tooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyTooltip#config-tooltip)
A tooltip config object that will be applied to the dependency hover tooltip. Can be used to for example customize delay

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDependencyTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyTooltip#property-isDependencyTooltip)
Identifies an object as an instance of [DependencyTooltip](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/DependencyTooltip) class, or subclass thereof.

[isDependencyTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyTooltip#property-isDependencyTooltip-static)
Identifies an object as an instance of [DependencyTooltip](https://bryntum.com/docs/gantt/api/#Scheduler/feature/mixin/DependencyTooltip) class, or subclass thereof.

[showTooltip](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyTooltip#property-showTooltip)
Set to `true` to show a tooltip when hovering a dependency line

[tooltipTemplate](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyTooltip#property-tooltipTemplate)
A template function allowing you to configure the contents of the tooltip shown when hovering a dependency line. You can return either an HTML string or a [DomConfig](https://bryntum.com/docs/gantt/api/#Core/helper/DomHelper#typedef-DomConfig) object.

## Functions

Functions are methods available for calling on the class

[getHoverTipHtml](https://bryntum.com/docs/gantt/api/Scheduler/feature/mixin/DependencyTooltip#function-getHoverTipHtml)
Generates DomConfig content for the tooltip shown when hovering a dependency
