# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/CellTooltip.md

# [CellTooltip](https://bryntum.com/docs/gantt/api/Grid/feature/CellTooltip)

Displays a tooltip when hovering cells.

To show contents when hovering a cell, you can specify a global [tooltipRenderer](https://bryntum.com/docs/gantt/api/#Grid/feature/CellTooltip#config-tooltipRenderer) function for the feature, you can also define a [tooltipRenderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-tooltipRenderer) for individual columns.

```
// Column with its own tooltip renderer
{
  text            : 'Name',
  field           : 'name',
  tooltipRenderer : ({ record }) => `My name is\xa0<b>${record.name}</b>`
}
```

Configuration properties passed into this feature are used to configure the [Tooltip](https://bryntum.com/docs/gantt/api/#Core/widget/Tooltip) instance used.

This feature is **disabled** by default.

Showing async content
---------------------

Showing remotely loaded content is super easy using the [tooltipRenderer](https://bryntum.com/docs/gantt/api/#Grid/feature/CellTooltip#config-tooltipRenderer):

```
// Async tooltip with some custom settings
const grid = new Grid({
  features: {
    cellTooltip: {
      // Time that mouse needs to be over cell before tooltip is shown
      hoverDelay : 4000,
      // Time after mouse out to hide the tooltip, 0 = instantly
      hideDelay  : 0,
      // Async tooltip renderer, return a Promise which yields the text content
      tooltipRenderer({ record, tip }) {
        return fetch(`tip.php?id=${record.id}`).then(response => response.text())
      }
    }
  }
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[tooltipRenderer](https://bryntum.com/docs/gantt/api/Grid/feature/CellTooltip#config-tooltipRenderer)
Function called to generate the HTML content for the cell tooltip. The function should return a string (your HTML), or a Promise yielding a string (for remotely loaded content)

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCellTooltip](https://bryntum.com/docs/gantt/api/Grid/feature/CellTooltip#property-isCellTooltip)
Identifies an object as an instance of [CellTooltip](https://bryntum.com/docs/gantt/api/#Grid/feature/CellTooltip) class, or subclass thereof.

[isCellTooltip](https://bryntum.com/docs/gantt/api/Grid/feature/CellTooltip#property-isCellTooltip-static)
Identifies an object as an instance of [CellTooltip](https://bryntum.com/docs/gantt/api/#Grid/feature/CellTooltip) class, or subclass thereof.

[tooltipRenderer](https://bryntum.com/docs/gantt/api/Grid/feature/CellTooltip#property-tooltipRenderer)
Function called to generate the HTML content for the cell tooltip. The function should return a string (your HTML), or a Promise yielding a string (for remotely loaded content)

[tip](https://bryntum.com/docs/gantt/api/Grid/feature/CellTooltip#property-tip)
Returns the tooltip instance

## Functions

Functions are methods available for calling on the class

[getTooltipContent](https://bryntum.com/docs/gantt/api/Grid/feature/CellTooltip#function-getTooltipContent)
Called from Tooltip to populate it with html.
