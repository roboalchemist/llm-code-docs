# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/Filter.md

# [Filter](https://bryntum.com/docs/gantt/api/Grid/feature/Filter)

Feature that allows filtering of the grid by settings filters on columns. The actual filtering is done by the store. For info on programmatically handling filters, see [StoreFilter](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreFilter).

```
// Filtering turned on but no default filter
const grid = new Grid({
  features : {
    filter : true
  }
});

// Using default filter
const grid = new Grid({
  features : {
    filter : { property : 'city', value : 'Gavle' }
  }
});
```

A column can supply a custom filtering function as its [filterable](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-filterable) config. When filtering by that column using the UI that function will be used to determine which records to include. See [Column#filterable](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-filterable) for more information.

```
// Custom filtering function for a column
const grid = new Grid({
   features : {
       filter : true
   },

   columns: [
       {
         field      : 'age',
         text       : 'Age',
         type       : 'number',
         // Custom filtering function that checks "greater than" no matter
         // which field user filled in :)
         filterable : ({ record, value, operator }) => record.age > value
       }
   ]
});
```

If this feature is configured with `prioritizeColumns : true`, those functions will also be used when filtering programmatically:

```
const grid = new Grid({
   features : {
       filter : {
           prioritizeColumns : true
       }
   },

   columns: [
       {
         field      : 'age',
         text       : 'Age',
         type       : 'number',
         filterable : ({ record, value, operator }) => record.age > value
       }
   ]
});

// Because of the prioritizeColumns config above, any custom filterable function
// on a column will be used when programmatically filtering by that columns field
grid.store.filter({
    property : 'age',
    value    : 41
});
```

This feature is **disabled** by default.

Keyboard shortcuts
------------------

This feature has the following default keyboard shortcuts:

Keys

Action

Action description

F

showFilterEditorByKey

When the column header is focused, this shows the filter input field

Please note that `Ctrl` is the equivalent to `Command` and `Alt` is the equivalent to `Option` for Mac users

For more information on how to customize keyboard shortcuts, please see [our guide](https://bryntum.com/docs/gantt/api/#Grid/guides/customization/keymap.md).

Menu items
----------

The following items are populated under the Filter submenu (in the cell and column header context menus) when the Filter feature is active.

Item reference

Text

Weight

Enabled by default

Description

`filterAuto*`

Contains

310

true

Filters records in the store to those where the column field contains the selected cell value

`filterBooleanIsTrue`

True

310

true

Filters records in the store to those where the column field is true

`filterBooleanIsFalse`

False

320

true

Filters records in the store to those where the column field is false

`filterDateEmpty`

Empty

310

true

Filters records in the store to those where the column field empty

`filterDateNotEmpty`

Not empty

320

true

Filters records in the store to those where the column field not empty

`filterDate=`

Equals

330

true

Filters records in the store to those where the column field is equal to the selected cell value

`filterDate!=`

Does not equal

340

true

Filters records in the store to those where the column field is not equal to the selected cell value

`filterDate<`

Less than

350

true

Filters records in the store to those where the column field is less than the selected cell value

`filterDate>`

Greater than

360

true

Filters records in the store to those where the column field is greater than the selected cell value

`filterDateIsToday`

Today

370

true

Filters records in the store to those where the column field is today

`filterDateIsTomorrow`

Tomorrow

380

true

Filters records in the store to those where the column field is tomorrow

`filterDateIsYesterday`

Yesterday

390

true

Filters records in the store to those where the column field is yesterday

`filterDateIsThisWeek`

This week

400

true

Filters records in the store to those where the column field is this week

`filterDateIsNextWeek`

Next week

410

true

Filters records in the store to those where the column field is next week

`filterDateIsLastWeek`

Last week

420

true

Filters records in the store to those where the column field is last week

`filterDateIsThisMonth`

This month

430

true

Filters records in the store to those where the column field is this month

`filterDateIsNextMonth`

Next month

440

true

Filters records in the store to those where the column field is next month

`filterDateIsLastMonth`

Last month

450

true

Filters records in the store to those where the column field is last month

`filterDateIsThisYear`

This year

460

true

Filters records in the store to those where the column field is this year

`filterDateIsNextYear`

Next year

470

true

Filters records in the store to those where the column field is next year

`filterDateIsLastYear`

Last year

480

true

Filters records in the store to those where the column field is last year

`filterDateIsYearToDate`

Year to date

490

true

Filters records in the store to those where the column field is within the year to date

`filterDurationEmpty`

Empty

310

true

Filters records in the store to those where the column field is empty

`filterDurationNotEmpty`

Not empty

320

true

Filters records in the store to those where the column field is not empty

`filterDuration=`

Equals

330

true

Filters records in the store to those where the column field is equal to the selected cell value

`filterDuration!=`

Does not equal

340

true

Filters records in the store to those where the column field is not equal to the selected cell value

`filterDuration>`

Greater than

350

true

Filters records in the store to those where the column field is greater than the selected cell value

`filterDuration<`

Less than

360

true

Filters records in the store to those where the column field is less than the selected cell value

`filterDuration>=`

Greater or equals

370

true

Filters records in the store to those where the column field is greater than or equal to the selected cell value

`filterDuration<=`

Less or equals

380

true

Filters records in the store to those where the column field is less than or equal to the selected cell value

`filterNumberEmpty`

Empty

310

true

Filters records in the store to those where the column field is empty

`filterNumberNotEmpty`

Not empty

320

true

Filters records in the store to those where the column field is not empty

`filterNumber=`

Equals

330

true

Filters records in the store to those where the column field is equal to the selected cell value

`filterNumber!=`

Does not equal

340

true

Filters records in the store to those where the column field is not equal to the selected cell value

`filterNumber>`

Greater than

350

true

Filters records in the store to those where the column field is greater than the selected cell value

`filterNumber<`

Less than

360

true

Filters records in the store to those where the column field is less than the selected cell value

`filterNumber>=`

Greater or equals

370

true

Filters records in the store to those where the column field is greater than or equal to the selected cell value

`filterNumber<=`

Less or equals

380

true

Filters records in the store to those where the column field is less than or equal to the selected cell value

`filterRelationEmpty`

Empty

310

true

Filters records in the store to those where the column field is empty

`filterRelationNotEmpty`

Not empty

320

true

Filters records in the store to those where the column field is not empty

`filterRelation=`

Equals

330

true

Filters records in the store to those where the column field is equal to the selected cell value

`filterRelation!=`

Does not equal

340

true

Filters records in the store to those where the column field is not equal to the selected cell value

`filterStringEmpty`

Empty

310

true

Filters records in the store to those where the column field is empty

`filterStringNotEmpty`

Not empty

320

true

Filters records in the store to those where the column field is not empty

`filterString=`

Equals

330

true

Filters records in the store to those where the column field is equal to the selected cell value

`filterString!=`

Does not equal

340

true

Filters records in the store to those where the column field is not equal to the selected cell value

`filterStringIncludes`

Contains

350

true

Filters records in the store to those where the column field contains the selected cell value

`filterStringDoesNotInclude`

Does not contain

360

true

Filters records in the store to those where the column field does not contain the selected cell value

`filterStringStartsWith`

Starts with

370

true

Filters records in the store to those where the column field starts with to the selected cell value

`filterStringEndsWith`

Ends with

380

true

Filters records in the store to those where the column field ends with to the selected cell value

`filterEdit`

Edit filter

500

false

Opens a popup to edit the current filter. Only shown when current column is filtered.

`filterRemove`

Remove filter

510

false

Stops filtering by selected column field. Only shown when current column is filtered.

`filterDisable`

Disable filter

520

false

Temporarily stops filtering by selected column field. Only shown when current column is filtered.

Legacy UI mode
--------------

To use the more limited legacy UI instead, configure [legacyMode](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter#config-legacyMode) to `true`.

You can supply a field config to use for the filtering field displayed for string type columns (legacy mode only):

```
// For string-type columns you can also replace the filter UI with a custom field:
columns: [
    {
        field : 'city',
        // Filtering for a value out of a list of values
        filterable: {
            filterField : {
                type     : 'combo',
                operator : 'isIncludedIn',
                items    : [
                    'Paris',
                    'Dubai',
                    'Montreal',
                    'London',
                    'New York'
                ]
            }
        }
    }
]
```

You can also change the default fields, for example this will use [DateTimeField](https://bryntum.com/docs/gantt/api/#Core/widget/DateTimeField) in filter popup (legacy mode only):

```
columns : [
    {
        type       : 'date',
        field      : 'start',
        filterable : {
            filterField : {
                type : 'datetime'
            }
        }
    }
]
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[prioritizeColumns](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-prioritizeColumns)
Use custom filtering functions defined on columns also when programmatically filtering by the columns field.

```
const grid = new Grid({
    columns : [
        {
            field : 'age',
            text : 'Age',
            filterable({ record, value }) {
              // Custom filtering, return true/false
            }
        }
    ],

    features : {
        filter : {
            prioritizeColumns : true // <--
        }
    }
});

// Because of the prioritizeColumns config above, any custom
// filterable function on a column will be used when
// programmatically filtering by that columns field
grid.store.filter({
    property : 'age',
    value    : 30
});
```

[keyMap](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-keyMap)
See [Keyboard shortcuts](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter#keyboard-shortcuts) for details

[legacyMode](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-legacyMode)
Set to `true` to enable the more limited legacy UI mode.

[pickerConfig](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-pickerConfig)
Optional configuration to use when configuring the [GridFieldFilterPickerGroup](https://bryntum.com/docs/gantt/api/#Grid/widget/GridFieldFilterPickerGroup) shown in the column header popup, when not in legacy mode.

[closeEmptyPopup](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-closeEmptyPopup)
When true, close the popup when the last filter shown in the popup is removed using the remove button. Not applicable in legacy mode.

[value](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-value)
The value against which to compare the [property](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter#config-property) of candidate objects.

[property](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-property)
The name of a property of candidate objects which yields the value to compare.

[operator](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-operator)
The operator to use when comparing a candidate object's [property](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter#config-property).

[defaultOperators](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-defaultOperators)
Which operator to pre-fill for the blank filter shown by default in the filter pop-up, keyed by the column field's data type. See [CollectionCompareOperator](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#typedef-CollectionCompareOperator) for available operators.

Default value:

```
{
    date     : '=',
    number   : '=',
    string   : 'includes',
    duration : '=',
    relation : null,
    auto     : '*'
}
```

[allowedOperators](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-allowedOperators)
This makes it possible to generally limit the allowed operators which populates the filtering sub-menus. See [CollectionCompareOperator](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#typedef-CollectionCompareOperator) for available operators.

```
const grid = new Grid({
    features : {
        filter : {
            allowedOperators : ['*', '=', '<', '>']
        }
    }
});
```

[defaultEnabled](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-defaultEnabled)
Whether the feature is enabled on all columns by default. A column's `filterable.filter` configuration overrides this setting.

[draggable](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#config-draggable)
Popups are draggable by default. Setting this to `false` will prevent the user from moving the popup by dragging on the picker group's background.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isFilter](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#property-isFilter)
Identifies an object as an instance of [Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter) class, or subclass thereof.

[isFilter](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#property-isFilter-static)
Identifies an object as an instance of [Filter](https://bryntum.com/docs/gantt/api/#Grid/feature/Filter) class, or subclass thereof.

[defaultEnabled](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#property-defaultEnabled)
Whether the feature is enabled on all columns by default. A column's `filterable.filter` configuration overrides this setting.

## Functions

Functions are methods available for calling on the class

[refreshHeaders](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-refreshHeaders)
Update headers to match stores filters. Called on store load and grid header render.

[getPopupItems](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-getPopupItems)
Get fields to display in filter popup.

[showFilterEditor](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-showFilterEditor)
Shows a popup where a filter can be edited.

[closeFilterEditor](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-closeFilterEditor)
Close the filter editor.

[getMenuItems](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-getMenuItems)
In non-legacy mode, gets the cell/header context menu items: a top-level Filter item having a submenu with operator and edit/remove options). Not used by legacy mode.

[onOperatorMenuItem](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-onOperatorMenuItem)
Handle clicking on an operator item in the filter submenu.

[getMenuItemsForFilteredColumn](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-getMenuItemsForFilteredColumn)
Get the context menu items (cell and header) that apply when the column is already filtered, e.g. edit, remove, disable. Used by both legacy and regular modes.

[populateCellMenu](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-populateCellMenu)
Add menu items for filtering.

[columnHasRemovableFilters](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-columnHasRemovableFilters)
Used to determine whether the 'remove filters' menu item should be enabled.

[columnHasEnabledFilters](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-columnHasEnabledFilters)
Used to determine whether the 'disable filters' menu item should be enabled.

[populateHeaderMenu](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-populateHeaderMenu)
Add menu item for removing filter if column is filtered.

[onStoreFilter](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-onStoreFilter)
Store filtered; refresh headers.

[renderHeader](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-renderHeader)
Called after headers are rendered, make headers match stores initial sorters

[onElementClick](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-onElementClick)
Called when user clicks on the grid. Only care about clicks on the filter icon.

[showFilterEditorByKey](https://bryntum.com/docs/gantt/api/Grid/feature/Filter#function-showFilterEditorByKey)
Called when user presses F-key grid.
