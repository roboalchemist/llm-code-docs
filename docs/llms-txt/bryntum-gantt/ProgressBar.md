# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/ProgressBar.md

# [ProgressBar](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar)

A progress bar widget which displays a horizontal progress bar with optional label and value text.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[label](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#config-label)
The label text to display at the top left

[valueText](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#config-valueText)
The value text to display at the top right If not specified and max is provided, will auto-generate as "value/max"

[value](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#config-value)
Progress value. If max is specified, this is an absolute value (e.g., 8 out of 10). If max is not specified, this should be between 0 and 1 (e.g., 0.5 for 50%)

[valueRenderer](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#config-valueRenderer)
Template function that can be used to customize the displayed value

[max](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#config-max)
Maximum value for progress calculation. When specified, value is treated as absolute.

[color](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#config-color)
Color of the progress bar ('b-green', 'b-yellow', 'b-orange', etc.)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isProgressBar](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#property-isProgressBar)
Identifies an object as an instance of [ProgressBar](https://bryntum.com/docs/gantt/api/#Core/widget/ProgressBar) class, or subclass thereof.

[isProgressBar](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#property-isProgressBar-static)
Identifies an object as an instance of [ProgressBar](https://bryntum.com/docs/gantt/api/#Core/widget/ProgressBar) class, or subclass thereof.

[label](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#property-label)
The label text to display at the top left

[valueText](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#property-valueText)
The value text to display at the top right If not specified and max is provided, will auto-generate as "value/max"

[value](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#property-value)
Progress value. If max is specified, this is an absolute value (e.g., 8 out of 10). If max is not specified, this should be between 0 and 1 (e.g., 0.5 for 50%)

[valueRenderer](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#property-valueRenderer)
Template function that can be used to customize the displayed value

[max](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#property-max)
Maximum value for progress calculation. When specified, value is treated as absolute.

[color](https://bryntum.com/docs/gantt/api/Core/widget/ProgressBar#property-color)
Color of the progress bar ('b-green', 'b-yellow', 'b-orange', etc.)
