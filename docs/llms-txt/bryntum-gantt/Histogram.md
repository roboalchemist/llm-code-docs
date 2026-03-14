# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/graph/Histogram.md

# [Histogram](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram)

Displays a simple bar histogram based upon an array of data objects passed in the [data](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram#config-data) config.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[data](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-data)
An array of data objects used to drive the histogram. The property/properties used are defined in the [series](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram#config-series) option.

[values](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-values)
The values to represent in bar form.

[series](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-series)
Object enumerating data series for the histogram. The object keys are treated as series identifiers and values are objects that can contain the following properties:

* `type` A String, either `'bar'` or `'outline'`
* `field` A String, the name of the property to use from the data objects in the [data](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram#config-data) option. If the value is omitted the series identifier is used as the property name.

[topValue](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-topValue)
By default, the bars are scaled based upon the detected max value across all the series. A specific top value to represent the 100% height may be configured.

[omitZeroHeightBars](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-omitZeroHeightBars)
By default, all bars are rendered, even those with zero height. Configure this as `true` to omit zero height bars.

[singleTextForAllBars](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-singleTextForAllBars)
By default, the histogram calls [getBarText](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram#config-getBarText) once per each datum. So the function is supposed to output all the series values the way it needs. Configure this as `false` to call the function for each series value if you need to display the values separately or having different styling.

[getBarClass](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-getBarClass)
A Function which returns a CSS class name to add to a rectangle element representing a "bar"-type series value. The following parameters are passed:

[getOutlineClass](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-getOutlineClass)
A Function which returns a CSS class name to add to a path element built for an `outline` type series. The following parameters are passed:

[getOutlineDOMConfig](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-getOutlineDOMConfig)
A Function which if provided should return a DOM configuration object for a `path` element built for an `outline` type series. The function accepts a default prepared DOM configuration in an argument which then can be processed and returned.

The following parameters are passed to the function:

[getBarTip](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-getBarTip)
A Function which returns the tooltip text to display when hovering a bar. The following parameters are passed:

[getBarText](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-getBarText)
A Function which returns the text to render inside a bar. The following parameters are passed:

[getBarDOMConfig](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-getBarDOMConfig)
A Function which if provided should return a DOM configuration object for a bar (a `RECT` element representing a single "bar"-type value). The function accepts a default prepared DOM configuration in an argument which then can be processed and returned.

The following parameters are passed to the function:

[getBarTextDOMConfig](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#config-getBarTextDOMConfig)
A Function which if provided returns DOM configuration for a bar text (a `TEXT` element accompanying a single "bar"-type value). The function accepts a default prepared DOM configuration in the first argument which then can be processed and returned.

The following parameters are passed to the function:

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isHistogram](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#property-isHistogram)
Identifies an object as an instance of [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) class, or subclass thereof.

[isHistogram](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#property-isHistogram-static)
Identifies an object as an instance of [Histogram](https://bryntum.com/docs/gantt/api/#Core/widget/graph/Histogram) class, or subclass thereof.

## Typedefs

Typedefs are type definitions for the class

[HistogramSeries](https://bryntum.com/docs/gantt/api/Core/widget/graph/Histogram#typedef-HistogramSeries)
An object representing a series settings.
