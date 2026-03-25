# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/view/Header.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/view/Header.md

# [Header](https://bryntum.com/docs/gantt/api/Grid/view/Header)

The Grid header, which contains simple columns but also allows grouped columns. One instance is created and used per SubGrid automatically, you should not need to instantiate this class manually. See [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column) for information about column configuration.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isHeader](https://bryntum.com/docs/gantt/api/Grid/view/Header#property-isHeader)
Identifies an object as an instance of [Header](https://bryntum.com/docs/gantt/api/#Grid/view/Header) class, or subclass thereof.

[isHeader](https://bryntum.com/docs/gantt/api/Grid/view/Header#property-isHeader-static)
Identifies an object as an instance of [Header](https://bryntum.com/docs/gantt/api/#Grid/view/Header) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[getColumnConfig](https://bryntum.com/docs/gantt/api/Grid/view/Header#function-getColumnConfig)
Recursive column header config creator. Style not included because of CSP. Widths are fixed up in [fixHeaderWidths](https://bryntum.com/docs/gantt/api/#Grid/view/Header#function-fixHeaderWidths)

[fixHeaderWidths](https://bryntum.com/docs/gantt/api/Grid/view/Header#function-fixHeaderWidths)
Fix header widths (flex or fixed width) after rendering. Not a part of template any longer because of CSP

[initDepths](https://bryntum.com/docs/gantt/api/Grid/view/Header#function-initDepths)
Depths are used for styling of grouped headers. Sets them on meta.

[getHeader](https://bryntum.com/docs/gantt/api/Grid/view/Header#function-getHeader)
Get the header cell element for the specified column.
