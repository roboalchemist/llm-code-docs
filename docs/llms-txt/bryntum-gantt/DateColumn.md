# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/column/DateColumn.md

# [DateColumn](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn)

A column that displays a date in the specified [format](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn#config-format). By default `L` format is used, which contains the following info: full year, 2-digit month, and 2-digit day. Depending on the browser locale, the formatted date might look different. [Intl.DateTimeFormat API](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) is used to format the date. Here is an example of possible outputs depending on the browser locale:

```
// These options represent `L` format
const options = { year : 'numeric', month : '2-digit', day : '2-digit' };

new Intl.DateTimeFormat('en-US', options).format(new Date(2021, 6, 1)); // "07/01/2021"
new Intl.DateTimeFormat('ru-RU', options).format(new Date(2021, 6, 1)); // "01.07.2021"

// Formatting using Bryntum API
LocaleManager.applyLocale('En');
DateHelper.format(new Date(2021, 6, 1), 'L'); // "07/01/2021"
LocaleManager.applyLocale('Ru');
DateHelper.format(new Date(2021, 6, 1), 'L'); // "01.07.2021"
```

To learn more about available formats check out [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) docs.

The [field](https://bryntum.com/docs/gantt/api/#Core/data/field/DateDataField) this column reads data from should be a type of date.

Default editor is a [DateField](https://bryntum.com/docs/gantt/api/#Core/widget/DateField).

```
new Grid({
    columns : [
         { type: 'date', text: 'Start date', format: 'YYYY-MM-DD', field: 'start' }
    ]
});
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[renderer](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#config-renderer)
Renderer function, used to style the date displayed in the cell. Can also affect other aspects of the cell, such as styling.

You should never modify any records inside this method.

```
new Grid({
    columns : [
        { type : 'date', text : 'Date of birth', field : 'dob' },
    ]
});
```

You can modify the row element too from inside a renderer to add custom CSS classes:

```
new Grid({
    columns : [
        {
            type : 'date',
            text : 'Date of birth',
            field : 'dob',
            renderer : ({ record, row }) => {
               // Add special CSS class to new rows that have not yet been saved
              row.cls.newRow = record.isPhantom;

              return record.dob;
        }
    ]
});
```

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[min](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#config-min)
Min value for the cell editor

[max](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#config-max)
Max value for the cell editor

[field](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#config-field)
The [name](https://bryntum.com/docs/gantt/api/#Core/data/field/DateDataField#config-name) of the data model date field to read data from.

[format](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#config-format)
Date format to convert a given date object into a string to display. By default `L` format is used, which contains the following info: full year, 2-digit month, and 2-digit day. Depending on the browser locale, the formatted date might look different. [Intl.DateTimeFormat API](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) is used to format the date. Here is an example of possible outputs depending on the browser locale:

```
// These options represent `L` format
const options = { year : 'numeric', month : '2-digit', day : '2-digit' };

new Intl.DateTimeFormat('en-US', options).format(new Date(2021, 6, 1)); // "07/01/2021"
new Intl.DateTimeFormat('ru-RU', options).format(new Date(2021, 6, 1)); // "01.07.2021"

// Formatting using Bryntum API
LocaleManager.applyLocale('En');
DateHelper.format(new Date(2021, 6, 1), 'L'); // "07/01/2021"
LocaleManager.applyLocale('Ru');
DateHelper.format(new Date(2021, 6, 1), 'L'); // "01.07.2021"
```

To learn more about available formats check out [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) docs.

Note, the [field](https://bryntum.com/docs/gantt/api/#Core/data/field/DateDataField) this column reads data from should be a type of date.

[step](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#config-step)
Time increment duration value to apply when clicking the left / right trigger icons. See [step](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-step) for more information Set to `null` to hide the step triggers.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isDateColumn](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#property-isDateColumn)
Identifies an object as an instance of [DateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn) class, or subclass thereof.

[isDateColumn](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#property-isDateColumn-static)
Identifies an object as an instance of [DateColumn](https://bryntum.com/docs/gantt/api/#Grid/column/DateColumn) class, or subclass thereof.

[renderer](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#property-renderer)
Renderer function, used to style the date displayed in the cell. Can also affect other aspects of the cell, such as styling.

You should never modify any records inside this method.

```
new Grid({
    columns : [
        { type : 'date', text : 'Date of birth', field : 'dob' },
    ]
});
```

You can modify the row element too from inside a renderer to add custom CSS classes:

```
new Grid({
    columns : [
        {
            type : 'date',
            text : 'Date of birth',
            field : 'dob',
            renderer : ({ record, row }) => {
               // Add special CSS class to new rows that have not yet been saved
              row.cls.newRow = record.isPhantom;

              return record.dob;
        }
    ]
});
```

When using the Bryntum React wrapper, this renderer can also return JSX elements. See [renderer](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-renderer) for a JSX example and performance considerations.

[min](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#property-min)
Min value for the cell editor

[max](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#property-max)
Max value for the cell editor

[field](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#property-field)
The [name](https://bryntum.com/docs/gantt/api/#Core/data/field/DateDataField#config-name) of the data model date field to read data from.

[format](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#property-format)
Date format to convert a given date object into a string to display. By default `L` format is used, which contains the following info: full year, 2-digit month, and 2-digit day. Depending on the browser locale, the formatted date might look different. [Intl.DateTimeFormat API](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) is used to format the date. Here is an example of possible outputs depending on the browser locale:

```
// These options represent `L` format
const options = { year : 'numeric', month : '2-digit', day : '2-digit' };

new Intl.DateTimeFormat('en-US', options).format(new Date(2021, 6, 1)); // "07/01/2021"
new Intl.DateTimeFormat('ru-RU', options).format(new Date(2021, 6, 1)); // "01.07.2021"

// Formatting using Bryntum API
LocaleManager.applyLocale('En');
DateHelper.format(new Date(2021, 6, 1), 'L'); // "07/01/2021"
LocaleManager.applyLocale('Ru');
DateHelper.format(new Date(2021, 6, 1), 'L'); // "01.07.2021"
```

To learn more about available formats check out [DateHelper](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper) docs.

Note, the [field](https://bryntum.com/docs/gantt/api/#Core/data/field/DateDataField) this column reads data from should be a type of date.

[step](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#property-step)
Time increment duration value to apply when clicking the left / right trigger icons. See [step](https://bryntum.com/docs/gantt/api/#Core/widget/DateField#config-step) for more information Set to `null` to hide the step triggers.

## Functions

Functions are methods available for calling on the class

[defaultRenderer](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#function-defaultRenderer)
Renderer that displays the date with the specified format. Also adds cls 'date-cell' to the cell.

[groupRenderer](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#function-groupRenderer)
Group renderer that displays the date with the specified format.

[formatValue](https://bryntum.com/docs/gantt/api/Grid/column/DateColumn#function-formatValue)
Used by both renderer and groupRenderer to do the actual formatting of the date
