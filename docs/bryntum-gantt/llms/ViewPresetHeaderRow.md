# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/preset/ViewPresetHeaderRow.md

# [ViewPresetHeaderRow](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPresetHeaderRow)

A part of the [ViewPreset](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPreset) declaration. Not used directly, but the properties below are instead provided inline as seen in sources of [PresetManager](https://bryntum.com/docs/gantt/api/#Scheduler/preset/PresetManager). This class is just provided for documentation purposes.

A sample header configuration can look like below

```
headers    : {
    {
        unit        : "month",
        renderer : function(start, end, headerConfig, index) {
            var month = start.getMonth();
            // Simple alternating month in bold
            if (start.getMonth() % 2) {
                return '<strong>' + month + '</strong>';
            }
            return month;
        },
        align       : 'start' // `start` or `end`, omit to center content (default)
    },
    {
        unit        : "week",
        increment   : 1,
        renderer    : function(start, end, headerConfig, index) {
            return 'foo';
        }
    },
}
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[align](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPresetHeaderRow#config-align)
The text alignment for the cell. Valid values are `start` or `end`, omit this to center text content (default). Can also be added programmatically in the [renderer](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPresetHeaderRow#config-renderer)

[unit](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPresetHeaderRow#config-unit)
The unit of time represented by each cell in this header row. See also increment property. Valid values are "millisecond", "second", "minute", "hour", "day", "week", "month", "quarter", "year".

[headerCellCls](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPresetHeaderRow#config-headerCellCls)
A CSS class to add to the cells in the time axis header row. Can also be added programmatically in the [renderer](https://bryntum.com/docs/gantt/api/#Scheduler/preset/ViewPresetHeaderRow#config-renderer)

[increment](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPresetHeaderRow#config-increment)
The number of units each header cell will represent (e.g. 30 together with unit: "minute" for 30 minute cells)

[dateFormat](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPresetHeaderRow#config-dateFormat)
Defines how the cell date will be formatted

[renderer](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPresetHeaderRow#config-renderer)
A custom renderer function used to render the cell content. It should return text/HTML to put in the header cell. The render function is called with the following parameters:

```
function (startDate, endDate, headerConfig, i) {
  headerConfig.align = "start"; // applies special CSS class to align header left
  headerConfig.headerCellCls = "myClass"; // will be added as a CSS class of the header cell DOM element

  return DateHelper.format(startDate, 'YYYY-MM-DD');
}
```

[thisObj](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPresetHeaderRow#config-thisObj)
`this` reference for the renderer function

[cellGenerator](https://bryntum.com/docs/gantt/api/Scheduler/preset/ViewPresetHeaderRow#config-cellGenerator)
A function that should return an array of objects containing 'start', 'end' and 'header' properties. Use this if you want full control over how the header rows are generated.

**Note:** `cellGenerator` cannot be used for the bottom level of your headers.

Example :

```
viewPreset : {
    displayDateFormat : 'H:mm',
    shiftIncrement    : 1,
    shiftUnit         : 'WEEK',
    timeResolution    : {
        unit      : 'MINUTE',
        increment : 10
    },
    headers           : [
        {
            unit          : 'year',
            // Simplified scenario, assuming view will always just show one US fiscal year
            cellGenerator : (viewStart, viewEnd) => [{
                start  : viewStart,
                end    : viewEnd,
                header : `Fiscal Year ${viewStart.getFullYear() + 1}`
            }]
        },
        {
            unit : 'quarter',
            renderer(start, end, cfg) {
                const
                    quarter       = Math.floor(start.getMonth() / 3) + 1,
                    fiscalQuarter = quarter === 4 ? 1 : (quarter + 1);

                return `FQ${fiscalQuarter} ${start.getFullYear() + (fiscalQuarter === 1 ? 1 : 0)}`;
            }
        },
        {
            unit       : 'month',
            dateFormat : 'MMM Y'
        }
    ]
 },
```
