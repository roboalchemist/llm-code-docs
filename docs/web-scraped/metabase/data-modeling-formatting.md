# Source: https://www.metabase.com/docs/latest/data-modeling/formatting

<div>

1.  [Home](/docs/latest/)
2.  [Data Modeling](/docs/latest/data-modeling/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Formatting defaults

People all around the world use Metabase, and everyone has different preferences for how dates, times, numbers, and currencies should be formatted and displayed. Metabase lets you to customize these formatting options at three different levels:

1.  **Global**. Set global defaults in Admin -\> Settings -\> [Localization](../configuring-metabase/localization).
2.  **Field**. Set field (column) defaults in Admin -\> Table Metadata. Field defaults override global defaults.
3.  **Question**. Set formatting defaults for individual questions in the visualization settings of that question. Question defaults override global and field defaults.

## Field formatting

*Admin settings \> Table Metadata \> Database \> Table \> Field \> Formatting*

You can override the global defaults for a specific field by going to the `Table Metadata` section of the Admin Panel. Select the database and table of the field in question, then click scroll down to the **Formatting**.

## Formatting options depend on the data type and the semantic type

The options you'll see here will depend on the field's data type and it's [semantic type](./semantic-types).

## Text formatting options

*Admin settings \> Table Metadata \> Database \> Table \> Field \> Formatting*

Options depend on the [semantic type](./semantic-types) you select for the field.

### Align

Whether to display the values in the middle, left, or right in table cells.

### Display As

If you have text, like an image URL, you may need to change the semantic type before Metabase will offer you the option to display the text as an image.

-   Text (display "as is").
-   Email link (i.e., if you have a `mailto` link).
-   Image. Metabase will display links to images as images in tables.
-   Automatic. Metabase will detect the string based on its format.
-   Link. You can optionally change the text that you want to display in the **Link text** input field. For example, if you set the **Link URL** for an "Adjective" column to:

``` highlight
https://www.google.com/search?q=}
```

When someone clicks on the value "askew" in the "Adjective" column, they'll be taken to the Google search URL:

``` highlight
https://www.google.com/search?q=askew
```

## Dates and times

*Admin settings \> Table Metadata \> Database \> Table \> Field \> Formatting*

Options depend on the [semantic type](./semantic-types) you select for the field.

### Align

Whether to display the values in the middle, left, or right in table cells.

### Display as

-   **Text** (display "as is").
-   **Link** (display the date/time as a clickable link).

### Date style

Choose how dates are displayed. Options include formats like:

-   January 31, 2018
-   31/1/2018
-   2018/1/31
-   And other regional date formats

### Abbreviate days and months

Check this option to use abbreviated forms for days and months (e.g., "Jan" instead of "January", "Mon" instead of "Monday").

### Show the time

This lets you choose if this time field should be displayed by default without the time; with hours and minutes; with hours, minutes, and seconds; or additionally with milliseconds.

-   **Off** - Display only the date without time
-   **HH:MM** - Display hours and minutes
-   **HH:MM:SS** - Display hours, minutes, and seconds
-   **HH:MM:SS.MS** - Display hours, minutes, seconds, and milliseconds

### Time style

Choose between 12-hour and 24-hour time format:

-   **12-hour clock** (e.g., 5:24 PM)
-   **24-hour clock** (e.g., 17:24)

## Numbers

*Admin settings \> Table Metadata \> Database \> Table \> Field \> Formatting*

Options depend on the [semantic type](./semantic-types) you select for the field.

### Align

Whether to display the values in the middle, left, or right in table cells.

### Show a mini bar chart

Only applies to table visualizations. Displays a bar for each value to show large or small it is relative to the other values in the column.

### Display as

-   **Automatic** - Metabase will automatically detect the best display format
-   **Text** - Display the number as plain text
-   **Link** - Display the number as a clickable link

### Style

Lets you choose to display the number as a plain number, a percent, in scientific notation, or as a currency.

-   **Normal** - Display as a regular number
-   **Percent** - Display as a percentage
-   **Scientific notation** - Display in scientific format (e.g., 1.23e+4)
-   **Currency** - Display with currency formatting

### Currency label style

For fields with Style set to "Currency", choose how to display the currency label. For example, for Canadian dollars:

-   **Symbol**: `CA$`
-   **Local symbol**: `$`
-   **Code**: `CAD`
-   **Name**: `Canadian dollars`

### Where to display the unit of currency

For currency fields, choose where to show the currency symbol:

-   **In the column heading** - Show the currency symbol in the table header
-   **In every table cell** - Show the currency symbol next to each value

### Separator style

This gives you various options for how commas and periods are used to separate the number (e.g., 100,000.00, 100.000,00, 100 000.00).

### Number of decimal places

Forces the number to be displayed with exactly this many decimal places.

### Multiply by a number

Multiplies this number by whatever you type here. Useful for unit conversions or scaling values.

### Add a prefix

Lets you put a symbol, word, etc. before this number (e.g., "\$" for currency).

### Add a suffix

Lets you put a symbol, word, etc. after this number (e.g., "dollars", "%", "units").

### Currency

Currency field formatting settings include all the same options as in the global formatting section, as well as all the options that Number fields have.

See [Currency formatting options](../questions/visualizations/table#currency-formatting-options).

## Question-level formatting

You can also override all formatting settings in any specific saved question or dashboard card by clicking on the gear to open the visualization options. To reset any overridden setting to the default, just click on the rotating arrow icon next to the setting's label. This will reset the setting to the field-level setting if there is one; otherwise it will be reset to the global default.

Formatting options vary depending on the type of visualization:

-   [Combo chart](../questions/visualizations/combo-chart)
-   [Detail](../questions/visualizations/detail)
-   [Funnel](../questions/visualizations/funnel)
-   [Gauge](../questions/visualizations/gauge)
-   [Line, Bar, and area charts](../questions/visualizations/line-bar-and-area-charts)
-   [Maps](../questions/visualizations/map)
-   [Numbers](../questions/visualizations/numbers)
-   [Pie or donut chart](../questions/visualizations/pie-or-donut-chart)
-   [Pivot table](../questions/visualizations/pivot-table)
-   [Progress bar](../questions/visualizations/progress-bar)
-   [Scatter plot or bubble chart](../questions/visualizations/scatterplot-or-bubble-chart)
-   [Tables](../questions/visualizations/table)
-   [Trend](../questions/visualizations/trend)
-   [Waterfall chart](../questions/visualizations/waterfall-chart)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/data-modeling/formatting.md) ]