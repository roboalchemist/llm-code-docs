# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/creating-a-date-prompt.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/creating-a-date-prompt.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-prompts-on-dashboards/other-prompt-types/creating-a-date-prompt.md

# Creating a date prompt

The date picker prompt allows users to select values based on calendar dates. When creating a date picker prompt, you will need to set a date format which the user will select using the date picker prompt. By default, the format used is yyyy-MM-dd.

The date picker prompt uses [Dojo date formats](https://dojotoolkit.org/reference-guide/1.9/dojo/date/locale/format.html). In the past, this component was based on the [JQuery Date Picker](http://api.jqueryui.com/datepicker/), and to support legacy formats, the old formats will be converted automatically.

Not all formats are supported or make sense when a date is selected. For instance, anything with less granularity than a unit of 'day' will default to the Dojo format, so we encourage you to use any format from 'd' to 'y' which is currently supported by the date picker control type. You can use any desired configuration where 'yyyy-MM-dd', 'yy-M-d' or 'd/MM/yyyy' is a valid format.

As a result the pattern can be any combinations of the following patterns of years, quarters, months and days:

| Pattern     | Description                     | Example Date: Monday, January 4, 2016 |
| ----------- | ------------------------------- | ------------------------------------- |
| G           | era                             | AD                                    |
| y or yy     | year (two digit)                | 16                                    |
| yyy or yyyy | year (four digit)               | 2016                                  |
| q or Q      | quarter (one digit)             | 1                                     |
| M           | month numeric (no leading zero) | 1                                     |
| MM          | month numeric (two digit)       | 01                                    |
| MMM         | month name short                | Jan                                   |
| MMMM        | month name long                 | January                               |
| d           | day of month (no leading zero)  | 4                                     |
| dd          | day of month (two digit)        | 04                                    |
| D           | day of the year                 | 4                                     |
| E           | day of the week                 | 2                                     |
