# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/widget/Combo.md

# [Combo](https://bryntum.com/docs/gantt/api/Core/widget/Combo)

Combo (dropdown) widget. Consists of a text field with a trigger icon, which displays a List. Can be populated from a Store.

Please be aware that when populating the Combo with objects or records, you have to configure [valueField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-valueField) and [displayField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-displayField) to point to the correct field names in your data.

This field can be used as an [editor](https://bryntum.com/docs/gantt/api/#Grid/column/Column#config-editor) for the [Column](https://bryntum.com/docs/gantt/api/#Grid/column/Column).

Basic scenarios
---------------

Loading data from simple string array:

Filtering on typing will still work when non-editable. The characters typed are collected and used to filter the list of items in the picker. The typed value expires after 2 seconds of inactivity. This is useful when a non-editable Combo has a very large dataset and you want to filter it by typing.

The combo's configured [primaryFilter](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-primaryFilter) is used which uses the `startsWith` operator by default.

### Basic scenarios

### Strict picker width matching

By default, a Combo's [picker](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#property-picker), auto widths around its visible content, but will be _at least_ the width of the Combo's input area. See the first example above.

To enforce strict width matching of the picker to the input area, configure the combo's picker like this

```
const combo = new Combo({
    items       : ['Small', 'Mediunm', 'Large', 'Ridiculously huge which would cause a very wide dropdown'],
    placeholder : 'Pick size of diamond for ring',
    picker : {
        align : {
            // Override default which is 'min'
            matchSize : true
        }
    }
});
```

### Autocomplete / Type ahead

Implementing remote type-ahead functionality is simple, configure a [store](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-store) with `readUrl` and define the [minChars](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-minChars) required to type before remote loading is triggered.

Snippet: Loading data from simple string array
----------------------------------------------

```
const combo = new Combo({
    items       : ['Small', 'Smaller', 'Really small', 'Tiny'],
    placeholder : 'Pick size of diamond for ring'
});
```

Loading data from array with item configs:

```
const combo = new Combo({
    items : [{ value: 'a', text: 'First' }, { value: 'z', text: 'Last' }]
});
```

Loading data from store:

```
const combo = new Combo({
    store        : memberStore,
    valueField   : 'id',
    displayField : 'name'
});
```

Editability
-----------

When configured with `editable : false`, the field may still be operated and have a value selected from the picker.

This setting just means that the textual input field may not be edited by the UI. In this mode, the picker's displayed dataset my still be filtered by typing while the picker is visible.

The combo's configured [primaryFilter](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-primaryFilter) is used which uses the `startsWith` operator by default.

Grouping the list
-----------------

To group the list contents, simply group your store using [groupers](https://bryntum.com/docs/gantt/api/#Core/data/mixin/StoreGroup#config-groupers). You can decide if clicking a header should toggle all group children (or if it should do nothing) with the [allowGroupSelect](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-allowGroupSelect) flag.

```
const combo = new Combo({
    width            : 400,
    displayField     : 'name',
    valueField       : 'id',
    multiSelect      : true,
    picker : {
        allowGroupSelect : false,
        // Show icon based on group name
        groupHeaderTpl   : (record, groupName) => `
            <i class="icon-${groupName}"></i>${groupName}
        `
    },
    value : [1, 4],
    store : new Store({
        fields : [
            'type'
        ],
        groupers : [
            { field : 'type', ascending : true }
        ],
        data : [
            { id : 1, name : 'pizza', type : 'food' },
            { id : 2, name : 'bacon', type : 'food' },
            { id : 3, name : 'egg', type : 'food' },
            { id : 4, name : 'Gin tonic', type : 'drinks' },
            { id : 5, name : 'Wine', type : 'drinks' },
            { id : 6, name : 'Beer', type : 'drinks' }
        ]
    })
});
```

This demo uses multi-selection and a grouped list:

Shared Stores
-------------

More than one Combo may share a Store if they are required to draw their values from a shared data set.

The only limitation here is that the characteristics of the filter that is applied to the store by typing are inherited from the **first** combo. So for example, all would be [caseSensitive](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-caseSensitive) or all case-insensitve, and all would use the same [filterOperator](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-filterOperator).

In the example below, all three email address inputs use the same store of recipients.

This may be operated using the keyboard. `ArrowDown` opens the picker, and then `ArrowDown` and `ArrowUp` navigate the picker's options. `Enter` selects an active option in the picker. `Escape` closes the picker.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[primaryFilter](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-primaryFilter)
Optionally a [Filter](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter) config object which the combo should use for filtering using the typed value. This may use a `filterBy` property to test its `value` against any field in the passed record.

```
{
    type          : 'combo',
    store         : myStore,
    primaryFilter : {
        filterBy(record) {
            if (this.value == null) {
                return true;
            }
            const value = this.value.toLowerCase();

            // Match typed value with forename or surname
            return record.forename.toLowerCase().startsWith(value)
                || record.surname.toLowerCase().startsWith(value);
        }
    }
}
```

[picker](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-picker)
Configuration object for the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/List) on initialization. Returns the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/List) instance at runtime.

For example:

```
new Combo({
    ...
    // configure the combobox picker
    picker : {
        listeners : {
            // prevent selection of item with id == 2
            beforeItem : ({ record }) => record.id !== 2
        }
    }
})
```

[multiSelect](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-multiSelect)
Set to `true` to allow selection of multiple values from the dropdown list.

Each value is displayed as a "Chip" to the left of the input area. Chips may be selected using the `LEFT` and `RIGHT` arrow keys and deleted using the `DELETE` key to remove values from the field. There is also a clickable close icon in each chip.

Use [toggleAllIfCtrlPressed](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-toggleAllIfCtrlPressed) to implement "select all" behaviour.

```
{
    type   : 'combo',
    store  : myStore,
    picker : {
        toggleAllIfCtrlPressed : true
    }
}
```

[items](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-items)
Rows to display in the dropdown (list items).

If an object, the property names provide the [value](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-value) for the Combo, and the property values provide the displayed test in the list and input area eg:

```
items : {
    small  : 'Small',
    medium : 'Medium',
    large  : 'Large'
}
```

If an array, each entry may be

* an object containing properties which must include the [valueField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-valueField) and [displayField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-displayField) which populates the dropdown with text and provides the corresponding field value.
* An array whose first value provides the [value](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-value) for the Combo and whose second value provides the displayed test in the list and input area.
* An array of values where the [valueField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-valueField) and [displayField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-displayField) are the same.

eg:

```
items : [
    {value : 'small',  text : 'Small'},
    {value : 'medium', text : 'Medium'},
    {value : 'large',  text : 'Large'},
]
```

or

```
items : [
    ['small',  'Small'],
    ['medium', 'Medium'],
    ['large',  'Large'],
]
```

or

```
items : [ 'Small', 'Medium', 'Large' ]
```

[store](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-store)
Store used to populate items. Also accepts a Store config object

[valueField](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-valueField)
Field used for item value when populating from store. Setting this to `null` will yield the selected record as the Combo's [value](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#property-value).

Leaving this value `undefined` means using the [idField](https://bryntum.com/docs/gantt/api/#Core/data/Model#property-idField-static) of the [modelClass](https://bryntum.com/docs/gantt/api/#Core/data/Store#property-modelClass) of the store as the value field.

[displayField](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-displayField)
Field used for item text when populating from store

[clearWhenInputEmpty](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-clearWhenInputEmpty)
Set to `true` to clear this field when user empties the input element

[pickerWidth](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-pickerWidth)
Width of picker, defaults to this combo's [pickerAlignElement](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-pickerAlignElement) width

[minChars](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-minChars)
The minimum string length to trigger the filtering, only relevant when [editable](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-editable) is `true`.

This defaults to `1` in the case of local filtering, but `4` if the [filterParamName](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-filterParamName) is set to cause remote dropdown loading.

[listItemTpl](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-listItemTpl)
Template string used to render the list items in the dropdown list

```
new Combo({
    listItemTpl : ({ text }) => `<div class="combo-color-box ${text}"></div>${text}`,
    editable    : false,
    items       : [
        'Black',
        'Green',
        'Orange',
        'Pink',
        'Purple',
        'Red',
        'Teal'
    ]
});
```

[displayValueRenderer](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-displayValueRenderer)
Template function that can be used to customize the displayed value

[listCls](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-listCls)
CSS class to add to picker

[filterParamName](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-filterParamName)
If the dropdown is to be populated with a filtered query to a remote server, specify the name of the parameter to pass the typed string here. By default, the string is simply sent as the value of the parameter. For special encoding, configure the combo with [encodeFilterParams](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-encodeFilterParams)

[encodeFilterParams](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-encodeFilterParams)
A function which creates an array of values for the [filterParamName](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-filterParamName) to pass any filters to the server upon load.

The default behaviour is just to set the parameter value to the filter's `value`, but the filter can be fully encoded for example:

```
   {
       encodeFilterParams(filters) {
           const result = [];

           for (const { property, operator, value, caseSensitive } of filters) {
               result.push(JSON.stringify({
                   field : property,
                   operator,
                   value,
                   caseSensitive
               }));
          }
       return result;
   }
```

[filterOnEnter](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-filterOnEnter)
If `false`, filtering will be triggered once you exceed [minChars](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-minChars). To filter only when hitting Enter key, set this to `true`;

[hideTrigger](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-hideTrigger)
Configure as `true` to hide the expand trigger. This is automatically set to `true` if remote filtering is enabled by setting the [filterParamName](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-filterParamName) config.

[overlayAnchor](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-overlayAnchor)
This implies that the picker will display an anchor pointer, but also means that the picker will align closer to the input field so that the pointer pierces the [pickerAlignElement](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-pickerAlignElement)

[keyStrokeFilterDelay](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-keyStrokeFilterDelay)
The delay in milliseconds to wait after the last keystroke before filtering the list.

This is a minimum of 300ms for remote filtering to keep network requests manageable, and defaults to 10ms for locally filtered stores.

[triggerAction](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-triggerAction)
How to query the store upon click of the expand trigger. Specify one of these values:

* `'all'` - Clear the filter and display the whole dataset in the dropdown.
* `'last'` - Filter the dataset using the last filter value.
* `null`/any other - Use the value in the input field to filter the dataset.

[filterOperator](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-filterOperator)
The name of an operator type as implemented in [operator](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-operator) to use when filtering the dropdown list based upon the typed value.

This defaults to `'startsWith'`, but the `'*'` operator may be used to match all values which _contain_ the typed value.

Not used when [filterParamName](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-filterParamName) is set to cause remote dropdown loading. The exact filtering operation is up to the server.

[caseSensitive](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-caseSensitive)
Configure as `true` to force case matching when filtering the dropdown list based upon the typed value.

[hidePickerOnSelect](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-hidePickerOnSelect)
By default, the picker is hidden on selection in single select mode, and remains to allow more selections when [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-multiSelect) is `true`. Setting this to a `Boolean` value can override that default.

[chipView](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-chipView)
A config object to configure the [ChipView](https://bryntum.com/docs/gantt/api/#Core/widget/ChipView) to display the selected value set when [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-multiSelect) is `true`.

For example the [itemTpl](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-itemTpl) or [iconTpl](https://bryntum.com/docs/gantt/api/#Core/widget/ChipView#config-iconTpl) might be configured to display richer chips for selected items.

[filterSelected](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-filterSelected)
When [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-multiSelect) is `true`, you may configure `filterSelected` as `true` to hide items in the dropdown when they are added to the selection. It will appear as if the requested item has "moved" into the field's [ChipView](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-chipView).

[emptyText](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-emptyText)
Text to display in the drop down when there are no items in the underlying store.

Defaults to use the `noResults` localization string ("No results" in En locale).

[value](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-value)
The initial value of this Combo box. In single select mode (default) it's a simple string value, for [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-multiSelect) mode, it should be an array of record ids.

[validateFilter](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-validateFilter)
`true` to cause the field to be in an invalid state while the typed filter string does not match a record in the store.

[clearTextOnPickerHide](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-clearTextOnPickerHide)
`true` to clear value typed to a multiselect combo when picker is collapsed

[clearTextOnSelection](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-clearTextOnSelection)
Specify `false` to not clear value typed to a multiselect combo when an item is selected.

[multiValueSeparator](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-multiValueSeparator)
A key value which, when typed in a [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-multiSelect) Combo, selects the currently active item in the picker, and clears the input field ready for another match to be typed.

[createOnUnmatched](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-createOnUnmatched)
If configured as `true`, this means that when an unmatched string is typed into the combo's input field, and `ENTER`, or the [multiValueSeparator](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-multiValueSeparator) is typed, a new record will be created using the typed string as the [displayField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-displayField).

If configured as a function, or the name of a function in the owning component hierarchy, the function will be called passing the string and combo field instance and should return the record to add (if any).

The new record will be appended to the store, and the value selected.

If the Store is an [AjaxStore](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore), the new record will be eiligible for syncing to the database through its [createUrl](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-createUrl).

If the `AjaxStore` is configured to [autoCommit](https://bryntum.com/docs/gantt/api/#Core/data/AjaxStore#config-autoCommit), the record will be synced immediately. If the server does not accept the new addition, the field is placed temporarily into an invalid state with a message that explains this.

For example:

```
    new Combo({
        label : 'Employee name',
        store : employees,
        createOnUnmatched(name, combo) {
            name = validateEmployeeName(name);

            if (name) {
                return new Employee({
                    name,
                    email : generateEmployeeEmail(name)
                });
            }
            else {
                combo.setError('Invalid new employee name');
            }
        }
    });
```

[inlinePicker](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-inlinePicker)
Configure this as `true` to render the dropdown list as a permanently visible list in the document flow immediately below the input area instead of as a popup.

This also hides the expand trigger since it is not needed.

[localizeDisplayFields](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-localizeDisplayFields)
Configure this as `true` and the items display field values will be localized. The display field values need to be a locale string.

[buildItems](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-buildItems)
Provide a function that returns items to be shown in the combo's selector.

[sortItemsOnLocaleChange](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-sortItemsOnLocaleChange)
Configure this as `true` to reapply sorting after [localizing the items](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-localizeDisplayFields).

[nonEditableFilterTimeout](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-nonEditableFilterTimeout)
When the Combo is `editable : false`, keystrokes are listened for and a filter string built which filters down the visible result. After a timeout of [nonEditableFilterTimeout](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-nonEditableFilterTimeout) milliseconds, the filter string is cleared.

[allowFiltering](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-allowFiltering)
Configure this as `false` to disable keyboard filtering completely

[cacheLastResult](https://bryntum.com/docs/gantt/api/Core/widget/Combo#config-cacheLastResult)
Enable caching of the last retrieved result until the timeout is reached.

Configure this either with:

* a number of minutes,
* a [Duration](https://bryntum.com/docs/gantt/api/#Core/data/Duration) object,
* a [DurationConfig](https://bryntum.com/docs/gantt/api/#Core/data/Duration#typedef-DurationConfig) object, or
* a string parseable by [parseDuration](https://bryntum.com/docs/gantt/api/#Core/helper/DateHelper#function-parseDuration-static), e.g. `10m`, `2 hours`, etc.

This prevents unnecessary request roundtrips to the backend when reopening the picker and the filter has not been changed. The cache expiry timer is restarted on each outgoing request.

The query to return all records when the filter value is empty will only happen when [minChars](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-minChars) config is 0. This might be desirable in some use cases for a consistent experience (e.g. when widening the result by deleting characters from the search term, the picker will not close), but might also return a very large result set, so use with care.

Falsy or unparseable values or negative numbers mean no caching.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isCombo](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-isCombo)
Identifies an object as an instance of [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo) class, or subclass thereof.

[isCombo](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-isCombo-static)
Identifies an object as an instance of [Combo](https://bryntum.com/docs/gantt/api/#Core/widget/Combo) class, or subclass thereof.

[picker](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-picker)
Configuration object for the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/List) on initialization. Returns the [picker](https://bryntum.com/docs/gantt/api/#Core/widget/List) instance at runtime.

For example:

```
new Combo({
    ...
    // configure the combobox picker
    picker : {
        listeners : {
            // prevent selection of item with id == 2
            beforeItem : ({ record }) => record.id !== 2
        }
    }
})
```

[multiSelect](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-multiSelect)
Set to `true` to allow selection of multiple values from the dropdown list.

Each value is displayed as a "Chip" to the left of the input area. Chips may be selected using the `LEFT` and `RIGHT` arrow keys and deleted using the `DELETE` key to remove values from the field. There is also a clickable close icon in each chip.

Use [toggleAllIfCtrlPressed](https://bryntum.com/docs/gantt/api/#Core/widget/List#config-toggleAllIfCtrlPressed) to implement "select all" behaviour.

```
{
    type   : 'combo',
    store  : myStore,
    picker : {
        toggleAllIfCtrlPressed : true
    }
}
```

[store](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-store)
Store used to populate items. Also accepts a Store config object

[filterOperator](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-filterOperator)
The name of an operator type as implemented in [operator](https://bryntum.com/docs/gantt/api/#Core/util/CollectionFilter#config-operator) to use when filtering the dropdown list based upon the typed value.

This defaults to `'startsWith'`, but the `'*'` operator may be used to match all values which _contain_ the typed value.

Not used when [filterParamName](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-filterParamName) is set to cause remote dropdown loading. The exact filtering operation is up to the server.

[value](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-value)
Get/sets combo value, selects corresponding item in the list Setting null clears the field.

If [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-multiSelect) is `true`, then multiple values may be passed as an array. If the values are records, these become the selected record set held by [valueCollection](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#property-valueCollection), and the `value` yielded by this field is an array of all the [valueField](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-valueField)s from the records.

[nonEditableFilterTimeout](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-nonEditableFilterTimeout)
When the Combo is `editable : false`, keystrokes are listened for and a filter string built which filters down the visible result. After a timeout of [nonEditableFilterTimeout](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-nonEditableFilterTimeout) milliseconds, the filter string is cleared.

[queryLast](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-queryLast-static)
A constant value for the [triggerAction](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-triggerAction) config to indicate that clicking the trigger should filter the dataset using the last filter query string, _not_ the input field value.

[innerElements](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-innerElements)
Returns array of the Combo's inner HTML elements. This getter can be overriden.

[isEmpty](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-isEmpty)
Returns `true` if this field has no selected records.

[valueCollection](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-valueCollection)
A [Collection](https://bryntum.com/docs/gantt/api/#Core/util/Collection) which holds the currently selected records from the store which dictates this field's value.

Usually, this will contain one record, the record selected.

When [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-multiSelect) is `true`, there may be several records selected.

[record](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-record)
Get selected record.

[records](https://bryntum.com/docs/gantt/api/Core/widget/Combo#property-records)
Get the selected record(s).

## Functions

Functions are methods available for calling on the class

[changeItems](https://bryntum.com/docs/gantt/api/Core/widget/Combo#function-changeItems)
Prepares items to work in attached menu (converts strings to items)

[onEditComplete](https://bryntum.com/docs/gantt/api/Core/widget/Combo#function-onEditComplete)
Check if field value is valid

[onTriggerClick](https://bryntum.com/docs/gantt/api/Core/widget/Combo#function-onTriggerClick)
User clicked trigger icon, toggle list.

[internalOnInput](https://bryntum.com/docs/gantt/api/Core/widget/Combo#function-internalOnInput)
User types into input field in editable combo, show list and filter it.

[onValueCollectionChange](https://bryntum.com/docs/gantt/api/Core/widget/Combo#function-onValueCollectionChange)
This reacts to our [valueCollection](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#property-valueCollection) being mutated in any way. The `change`, `select` and `action` events are fired here.

This could happen in four ways:

* User selected or deselected an item in the dropdown list.
* `set value` changes the content.
* The [multiSelect](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#config-multiSelect) Chip view (which uses this in its store) deletes a record.
* The application programmatically mutates the [valueCollection](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#property-valueCollection).

[onValueCollectionNoChange](https://bryntum.com/docs/gantt/api/Core/widget/Combo#function-onValueCollectionNoChange)
This listens for when a record from the list is selected, but is already part of the selection and so the [valueCollection](https://bryntum.com/docs/gantt/api/#Core/widget/Combo#property-valueCollection) rejects that as a no-op. At this point, the user will still expect the picker to hide.

[changePicker](https://bryntum.com/docs/gantt/api/Core/widget/Combo#function-changePicker)
Creates default picker widget

[changeCacheLastResult](https://bryntum.com/docs/gantt/api/Core/widget/Combo#function-changeCacheLastResult)
Parses {Core.data.Duration} specifier and returns number of milliseconds.

## Events

Events are triggered for certain actions in this class and can be listened for to react to those actions in your code

[input](https://bryntum.com/docs/gantt/api/Core/widget/Combo#event-input)
User typed into the field. Please note that the value attached to this event is the raw input field value and not the combos value

[select](https://bryntum.com/docs/gantt/api/Core/widget/Combo#event-select)
An item in the list was selected

[action](https://bryntum.com/docs/gantt/api/Core/widget/Combo#event-action)
The default action was performed (an item in the list was selected)
