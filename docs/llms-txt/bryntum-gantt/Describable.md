# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/mixin/Describable.md

# [Describable](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable)

Mixin that provides a consistent method for describing the ranges of time presented by a view. This is currently consumed only by the Calendar widget for describing its child views. This mixin is defined here to facilitate using a Scheduler as a child view of a Calendar.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[dateFormat](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#config-dateFormat)
A [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) format string/function to use to create date output for view descriptions.

[dateSeparator](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#config-dateSeparator)
A string used to separate start and end dates in the [descriptionFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-descriptionFormat).

[descriptionFormat](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#config-descriptionFormat)
The date format used by the default [descriptionRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-descriptionRenderer) for rendering the view's description. If this value is `null`, the [dateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-dateFormat) (and potentially [dateSeparator](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-dateSeparator)) will be used.

For views that can span a range of dates, this can be a 2-item array with the following interpretation:

* `descriptionFormat[0]` is either a date format string or `true` (to use [dateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-dateFormat)). The result of formatting the `startDate` with this format specification is used when the formatting both the `startDate` and `endDate` with this specification produces the same result. For example, a week view displays only the month and year components of the date, so this will be used unless the end of the week crosses into the next month.

* `descriptionFormat[1]` is used with [formatRange](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-formatRange-static) when the `startDate` and `endDate` format differently using `descriptionFormat[0]` (as described above). This one format string produces a result for both dates. If this value is `true`, the [dateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-dateFormat) and [dateSeparator](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-dateSeparator) are combined to produce the range format.

[descriptionRenderer](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#config-descriptionRenderer)
A function that provides the textual description for this view. If provided, this function overrides the [descriptionFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-descriptionFormat).

```
 descriptionRenderer() {
     const
         eventsInView = this.eventStore.records.filter(
             eventRec => DateHelper.intersectSpans(
                 this.startDate, this.endDate,
                 eventRec.startDate, eventRec.endDate)).length,
         sd = DateHelper.format(this.startDate, 'DD/MM/YYY'),
         ed = DateHelper.format(this.endDate, 'DD/MM/YYY');

    return `${sd} - ${ed}, ${eventsInView} event${eventsInView === 1 ? '' : 's'}`;
}
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDescribable](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#property-isDescribable)
Identifies an object as an instance of [Describable](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable) class, or subclass thereof.

[isDescribable](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#property-isDescribable-static)
Identifies an object as an instance of [Describable](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable) class, or subclass thereof.

[dateFormat](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#property-dateFormat)
A [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) format string/function to use to create date output for view descriptions.

[dateSeparator](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#property-dateSeparator)
A string used to separate start and end dates in the [descriptionFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-descriptionFormat).

[descriptionFormat](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#property-descriptionFormat)
The date format used by the default [descriptionRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-descriptionRenderer) for rendering the view's description. If this value is `null`, the [dateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-dateFormat) (and potentially [dateSeparator](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-dateSeparator)) will be used.

For views that can span a range of dates, this can be a 2-item array with the following interpretation:

* `descriptionFormat[0]` is either a date format string or `true` (to use [dateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-dateFormat)). The result of formatting the `startDate` with this format specification is used when the formatting both the `startDate` and `endDate` with this specification produces the same result. For example, a week view displays only the month and year components of the date, so this will be used unless the end of the week crosses into the next month.

* `descriptionFormat[1]` is used with [formatRange](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-formatRange-static) when the `startDate` and `endDate` format differently using `descriptionFormat[0]` (as described above). This one format string produces a result for both dates. If this value is `true`, the [dateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-dateFormat) and [dateSeparator](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-dateSeparator) are combined to produce the range format.

[dateBounds](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#property-dateBounds)
Returns the date or ranges of included dates as an array. If there is only one significant date, the array will have only one element. Otherwise, a range of dates is returned as a two-element array with `[0]` being the `startDate` and `[1]` the `lastDate`.

[description](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#property-description)
The textual description generated by the [descriptionRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-descriptionRenderer) if present, or by the view's date (or date _range_ if it has a range) and the [descriptionFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-descriptionFormat).

[formattedDescription](https://bryntum.com/docs/gantt/api/Scheduler/view/mixin/Describable#property-formattedDescription)
Yields the default description value as calculated using the [dateFormat](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#property-dateFormat) which describes this object if no [descriptionRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-descriptionRenderer) was provided.

This may be used in a configured [descriptionRenderer](https://bryntum.com/docs/gantt/api/#Scheduler/view/mixin/Describable#config-descriptionRenderer) to augment the calculated description.
