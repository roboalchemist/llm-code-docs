# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/YearPicker.md

# [YearPicker](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker)

A Panel subclass which allows a year to be selected from a range of 12 displayed years.

The panel can be configured with [startYear](https://bryntum.com/docs/gantt/api/#Core/widget/YearPicker#config-startYear) to specify the first year in the displayed range.

The [year](https://bryntum.com/docs/gantt/api/#Core/widget/YearPicker#property-year) indicates and sets the currently selected year.

The [select](https://bryntum.com/docs/gantt/api/#Core/widget/YearPicker#event-select) event is fired when a new year is selected.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[tbar](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#config-tbar)
The definition of the top toolbar which displays the title and "previous" and "next" buttons.

This contains the following predefined `items` which may be reconfigured by application code:

* `title` A widget which displays the visible year range. Weight 100.
* `previous` A button which navigates to the previous block. Weight 200.
* `next` A button which navigates to the next block. Weight 300.

These may be reordered:

```
new YearPicker({
    appendTo : targetElement,
    tbar     : {
        items : {
            // Move title to centre
            title : {
                weight : 250
            }
        }
    },
    width    : '24em'
});
```

[yearButtonCount](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#config-yearButtonCount)
The number of clickable year buttons to display in the widget.

It may be useful to change this if a non-standard shape or size is used.

[year](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#config-year)
The year to use as the selected year. Defaults to the current year.

[minYear](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#config-minYear)
The lowest year to allow.

[maxYear](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#config-maxYear)
The highest year to allow.

[startYear](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#config-startYear)
The year to show at the start of the widget

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isYearPicker](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#property-isYearPicker)
Identifies an object as an instance of [YearPicker](https://bryntum.com/docs/gantt/api/#Core/widget/YearPicker) class, or subclass thereof.

[isYearPicker](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#property-isYearPicker-static)
Identifies an object as an instance of [YearPicker](https://bryntum.com/docs/gantt/api/#Core/widget/YearPicker) class, or subclass thereof.

[year](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#property-year)
The currently selected year.

[startYear](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#property-startYear)
The starting year displayed in the widget.

[value](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#property-value)
The currently selected year.

[endYear](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#property-endYear)
The ending year displayed in the widget.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[select](https://bryntum.com/docs/gantt/api/Core/widget/YearPicker#event-select)
Fired when a year is selected.
